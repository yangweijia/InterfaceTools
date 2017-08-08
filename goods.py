#coding=utf-8
import json
import requests
import sys

session=requests.Session()
#赛事商户登录
if sys.argv[1]=="contest":
    session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"wy",
                       "password":"Aa123456"
                      } ))
    #创建商品
    response=session.post(
         url="https://admin.codoon.com/admin/goods/goods",
         data=json.dumps(
                      {
                       "module":"mall",
                       "goods_info":{"l_name":sys.argv[2],"s_name":sys.argv[2],"adv_name":"","sku_desc":u"颜色","limit_count":0,"market_price":0,"promote_rules":False,"pay_use":2,"show_quality":False,"can_use_coupon":1,"unbox_state":2,"dispatch_promise":1,"return_item_promise":1,"class_name":u"颜色","second_class_name":u"黑色","img_list":["https://activity-codoon.b0.upaiyun.com/cdmall63281942889057..name"],"old_sku":[],"sub_tags":[],"graphic_details":"","brand_name":u"阿迪达斯","advertising":[{"adv_content":"","adv_link":""},{"adv_content":"","adv_link":""}]},
                       "sku_config":{"f_attr":u"颜色","":u"蓝色","s_attr":"","post":True,"post_price":0,"can_refund":True,"settle_type":True,"f_attr_list":[u"蓝色",u"白色"],"s_attr_list":[]},
                       "associates":[{"goods_name":"","sku_list":[{"sku_name":u"蓝色","price":1,"num":100,"third_sku":"","cost":1,"rebate":0,"settle_way":"cost","storage":0,"thumbnail":""},{"sku_name":u"白色","price":1,"num":100,"third_sku":"","cost":1,"rebate":0,"settle_way":"cost","storage":0,"thumbnail":""}]}],
                       "is_super":False
                      } ))
#乐活动商户登录
else:
    session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"test123",
                       "password":"Test123456"
                      } ))
    #创建商品
    response=session.post(
         url="https://admin.codoon.com/admin/goods/goods",
         data=json.dumps(
                      {
                       "module":"mall",
                       "goods_info":{"l_name":sys.argv[2],"s_name":sys.argv[2],"adv_name":"","sku_desc":u"颜色","limit_count":0,"market_price":0,"promote_rules":False,"pay_use":2,"show_quality":False,"can_use_coupon":1,"unbox_state":2,"dispatch_promise":1,"return_item_promise":1,"class_name":u"颜色","second_class_name":u"黑色","img_list":["https://activity-codoon.b0.upaiyun.com/cdmall63281942889057..name"],"old_sku":[],"sub_tags":[],"graphic_details":"","brand_name":u"阿迪达斯","advertising":[{"adv_content":"","adv_link":""},{"adv_content":"","adv_link":""}]},
                       "sku_config":{"f_attr":u"颜色","":u"蓝色","s_attr":"","post":True,"post_price":0,"sp_id":"043100065051","can_refund":True,"settle_type":True,"f_attr_list":[u"蓝色",u"白色"],"s_attr_list":[]},
                       "associates":[{"goods_name":"","sku_list":[{"sku_name":u"蓝色","price":1,"num":100,"third_sku":"","cost":1,"rebate":0,"settle_way":"cost","storage":0,"thumbnail":""},{"sku_name":u"白色","price":1,"num":100,"third_sku":"","cost":1,"rebate":0,"settle_way":"cost","storage":0,"thumbnail":""}]}],
                       "is_super":False
                      } ))


j=json.loads(response.text)
#response.encoding="utf-8"
goods_id=j["data"]["good_ids"][0]
#提交审核
re=session.post(
         url="https://admin.codoon.com/admin/goods/onshelve",
         data=json.dumps(
                      {
                       "module":"mall",
                       "goods_id":goods_id,
                       "start_sell_time":"2017-07-03 20:16:07",
                       "expired_time":"3999-12-31 00:00:00"
                      } ))
if sys.argv[1]=="contest":
#三方BOSS登录
    session.post(
         url="https://admin.codoon.com/admin/usr/login",
         data=json.dumps(
                      {
                       "module":"mall",
                       "username":"boss_admin",
                       "password":"Boss123"
                      } )) 
#审核通过
    session.post(
         url="https://admin.codoon.com/admin/goods/audit",
         data=json.dumps(
                      {
                       "module":"mall",
                       "goods_id":goods_id,
                       "handle_state":1
                      } )) 

print "已生成商品，商品ID为:"
print goods_id
