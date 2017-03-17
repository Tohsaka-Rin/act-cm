from django.test import TestCase
import time
import datetime
# Create your tests here.

# t = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print t
# print type(t)

# str = '2012-11-19'
# d = datetime.datetime.strptime(str,"%Y-%m-%d").date()
# print d
# print type(d)

d = datetime.date.today()
str = d.strftime("%Y-%m-%d")
print str
print type(str)