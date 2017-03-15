# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo
from django.core.exceptions import ObjectDoesNotExist


# 用户名/邮箱/手机号 重复性检验
# key : (userName,mail.cellphone,D_id,...)， value是对应字段的值
# 已被注册返回True，否则返回False

def checkExist(key,value):
    #TODO
    try:
        if key == 'userName':
            doc = DoctorInfo.objects.get(userName=value)
        elif key == 'mail':
            doc = DoctorInfo.objects.get(mail=value)
        elif key == 'cellphone':
            doc = DoctorInfo.objects.get(cellphone=value)
        elif key == 'D_id':
            doc = DoctorInfo.objects.get(D_id=value)

        return True
    except ObjectDoesNotExist:
        return False




# 通过用户名获取用户某个字段的信息
# key 就是字段名， 比如'password' 'D_id'
# 返回获取的值
def getUserInfo(userName,key):
    #TODO
    return 1

# 获取医生的基本信息
# D_id为医生的编号
# 以字典形式返回获取到的基本信息
def getDoctorBasicInfo(D_id):
    message = {}
    # TODO
    return message


# 获取医生的详细信息
# D_id为医生的编号
# 以字典形式返回获取到的详细信息
def getDoctorDetailedInfo(D_id):
    message = {}
    # TODO
    return message

#获取医生管理的实验组信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个实验组的信息
def getExpGroups(D_id):
    list = []
    # TODO
    return list

#获取指定实验组中所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个患者的基本信息
def getExpGroupsPatientsInfo(D_id,G_id):
    list = []
    # TODO
    return list

#获取指定医生管理的所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个实验组的信息
def getPatientsBasicInfo(D_id):
    list = []
    # TODO
    return list



#获取指定医生管理的所有患者的基本信息
#还要返回患者所在实验组的信息
#注意判断一下P_id的正确性，失败返回一个空字典
def getPatientDetailedInfo(D_id,P_id):
    message={}
    # TODO
    return message


#获取指定患者的所有家属信息基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个家属的信息
def getRelationsInfo(D_id,P_id):
    list=[]
    # TODO
    return list








