from django.test import TestCase
import time
import datetime
import demjson
# Create your tests here.

# t = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print t
# print type(t)

str = '2012-01-01'
d = datetime.datetime.strptime(str,"%Y-%m-%d").date()
print d
print type(d)

# message = {'P_id':0}
# js = demjson.encode(message)
# print message
# print type(message)

# keys = ['a','b']
# values = [1,'2']
# message = {}
# i = 0
# for key in keys:
#     message[key] = values[i]
#     i=i+1
#
# print message


