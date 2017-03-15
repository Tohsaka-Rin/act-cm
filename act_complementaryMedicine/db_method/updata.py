# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo
from django.core.exceptions import ObjectDoesNotExist

#修改指定医生信息
#data为医生新的信息，包括D_id
#修改成功返回True,否则返回False
def updataDoctorInfo(data):
    #TODO
    #birthday需要处理一下
    try:
        doctor = DoctorInfo.objects.get(id=data['D_id'])
        doctor.name = data['name']
        doctor.sex = data['sex']
        doctor.birthday = data['brithday']
        doctor.userName = data['userName']
        doctor.password = data['password']
        doctor.cellphone = data['cellphone']
        doctor.weChat = data['weChat']
        doctor.mail = data['mail']
        doctor.title = data['title']
        doctor.hospital = data['hospital']
        doctor.department = data['department']
        doctor.userGroup = data['userGroup']
        doctor.save()
        return True
    except:
        return False

#修改指定实验组
#注意判断一下D_id与G_id是否正确
# 成功返回True，失败返回False
def addExpGroup(D_id,G_id,name,info):
    # TODO
    return False


#修改指定患者信息，包括患者所属的实验组
#data为患者新的信息，包括D_id，需要判断一下该患者是否归该医生所管理
#修改成功返回True,否则返回False
def updataPatientInfo(data):
    #TODO
    return False


#修改指定家属信息
#data为患者新的信息，包括D_id，P_id，需要判断一下归属关系
#修改成功返回True,否则返回False
def updataRelationInfo(data):
    # TODO
    return False
