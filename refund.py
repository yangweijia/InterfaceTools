#coding=utf-8
import json
import requests
import MySQLdb
import sys

conn= MySQLdb.connect(
        host='db_mall',
        port = 3306,
        user='root',
        passwd='codoon20140312',
        db ='mall_db',
        )
cur = conn.cursor()
return_sku_total=0

if sys.argv[1]=="contest":
  #某用户的三方商户的已支付待确认且没有完全退款的订单
  cur.execute("select mall_db.`order`.order_id from mall_db.`order` where (mall_db.`order`.state=2) and (mall_db.order.user_id='"+sys.argv[2]+"') and (mall_db.order.sp_type=2) and (mall_db.`order`.user_pay_amount>0) and (mall_db.`order`.pay_time>'2017-01-01 00:00:00') and  (mall_db.`order`.order_id not IN (select mall_db.`order`.order_id from mall_db.`order` inner join mall_db.refund where mall_db.`order`.order_id=mall_db.refund.order_id and mall_db.refund.is_last_refund=1))")
else:
  cur.execute("select mall_db.`order`.order_id from mall_db.`order` where (mall_db.`order`.state=2) and (mall_db.order.user_id='"+sys.argv[2]+"') and (mall_db.order.sp_id='090100024068') and (mall_db.`order`.user_pay_amount>0) and (mall_db.`order`.pay_time>'2017-01-01 00:01:00') and  (mall_db.`order`.order_id not IN (select mall_db.`order`.order_id from mall_db.`order` inner join mall_db.refund where mall_db.`order`.order_id=mall_db.refund.order_id and mall_db.refund.is_last_refund=1))")

rows=cur.fetchall()
for row in rows:
  session=requests.Session()
  #一个订单中每个sku和对应的数量
  cur.execute("select mall_db.order_sku_detail.sku_id,mall_db.order_sku_detail.count from order_sku_detail where order_id=%s",row[0]) 
  sku_list=cur.fetchall()
  for sku in sku_list:
     order_id=row[0]
     sku_id=sku[0]
     total_num=sku[1]
     #一个订单中某个sku已经退款的数量
     up="SELECT sum(mall_db.refund_sku_detail.sku_count) from mall_db.order_sku_detail inner join mall_db.refund_sku_detail where mall_db.order_sku_detail.order_id=mall_db.refund_sku_detail.order_id AND mall_db.order_sku_detail.sku_id=mall_db.refund_sku_detail.sku_id AND mall_db.order_sku_detail.order_id=%s AND mall_db.order_sku_detail.sku_id=%s"%(order_id,sku_id)
     cur.execute(up)
     return_num=cur.fetchone()
     
     if return_num[0]==None:
       left_num=total_num
     else:
       left_num=total_num-return_num[0]

     if left_num>0:
       return_sku_total=return_sku_total+left_num
       #赛事
       if sys.argv[1]=="contest":
         session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"boss_admin",
                       "password":"Boss123"
                      } ) )
       #乐活动
       else:
         session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"test123",
                       "password":"Test123456"
                      } ) )
         
       te=session.post(
         url="https://admin.codoon.com/admin/order/refund",
         data=json.dumps(
                      {
                       "module":"mall",
                       "order_id":order_id,
                       "reason":"reason",
                       "sku_list":[{"sku_id":sku_id,"return_num":int(left_num)}],
                       "use_custom_refund_fee":False
                      } ))
if return_sku_total==0:
  print "暂无退款"
else:
 print "已为你退款%s个sku，请查收"%return_sku_total
cur.close()
conn.close()
