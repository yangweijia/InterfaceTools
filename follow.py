#coding=utf-8
import requests
import json
import time

f=file('user.txt')
user=[]
while True:
  line=f.readline().strip()
  if len(line)==0:
    break
  else:
    user.append(line)
f.close()

for i in range(1,5500): 
  re=requests.post(
         url="http://121.196.199.184:1504/refactoring/relation_chain/user_follow_people",
         headers={
                 "Content-Type":"application/json",
         },
         data=json.dumps(
                      {
                       "user_id":user[i],
                       "people_id":"a2b4660b-d90a-4ad7-a0c9-0148d0d001e9"
                      })
  )
  print(re.text)
