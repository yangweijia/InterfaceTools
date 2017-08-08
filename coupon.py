#coding=utf-8
import json
import requests
import sys
import random

session=requests.Session()
session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"Oper",
                       "password":"Oper"
                      } ))
#创建优惠券
response=session.post(
         url="https://admin.codoon.com/admin/market/coupon/save_coupon_class",
         data=json.dumps(
                      {
                       "module":"mall",
                       "id":"",
                       "name":"全部商家"+str(random.uniform(1,99999)),
                       "desc":"全部商家直减5元",
                       "promote_price_min":0,
                       "promote_price_minus":500,
                       "privilege_code":"",
                       "enable_time":"2017-01-23 15:41:58",
                       "auto_overdue_days":0,
                       "expiry_date":"",
                       "limit_times":99,
                       "limit_pieces":99,
                       "time_start":"00:00:00",
                       "time_end":"23:59:59",
                       "need_coins":"0",
                       "tip":"",
                       "promotion_range":{"goods_id":[],"business":[{"id":"ALL_SHOP","name":"全部商家"}],"category":[],"brand":[],"label":[],"sp_black_list":[]}
                      } ))
j=json.loads(response.text)
api_code=j["data"]["api_code"]


#制作
session.post(
         url="https://admin.codoon.com/admin/market/coupon/update_coupon_stock",
         data=json.dumps(
                      {
                       "module":"mall",
                       "id":api_code,
                       "operate":"create",
                       "num":100
                      } ))
#api上架
session.post(
         url="https://admin.codoon.com/admin/market/coupon/change_coupon_channel",
         data=json.dumps(
                      {
                       "module":"mall",
                       "id":api_code,
                       "type":"api",
                       "operate":'on'
                      } ))
print "优惠券已制作，API码为："
print api_code

