# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 我没有使用外码，如果你们看懂他是怎么用的话可以使用models.ForeignKey


class DoctorInfo(models.Model):
    GROUP_CHOICES = (
        ('doctor','医生'),
        ('intern','实习生'),
        ('student','学生')
    )

    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)
    birthday = models.DateField(null=True,blank=True)
    userName = models.CharField(max_length=50,unique=True,null=False)
    password = models.CharField(max_length=30,null=False)
    cellphone = models.CharField(max_length=11)
    weChat = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    hospital = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    userGroup = models.CharField(max_length=20,choices=GROUP_CHOICES)
    registerDate = models.DateField(auto_now_add=True)


class PatientGroup(models.Model):
    G_id = models.IntegerField()
    P_id = models.IntegerField()

class GroupInfo(models.Model):
    name = models.CharField(max_length=100,null=False)
    D_id = models.IntegerField()
    information = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)