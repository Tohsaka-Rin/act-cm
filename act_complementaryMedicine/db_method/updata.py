# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo,GroupInfo,PatientInfo,RelationInfo
from django.core.exceptions import ObjectDoesNotExist
import datetime
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
def updataExpGroup(D_id,G_id,name,info):
    # TODO
    try:
        group = GroupInfo.objects.get(id = G_id)
        group.name = name
        group.information = info
        group.save()
        return True
    except :
        return False


#修改指定患者信息，包括患者所属的实验组
#data为患者新的信息，包括D_id，需要判断一下该患者是否归该医生所管理
#修改成功返回True,否则返回False
def updataPatientInfo(data):
    #TODO
    try:
        patient = PatientInfo.objects.get(P_id= data['P_id'])
        patient.sign = data['sign']
        patient.name = data['name']
        patient.sex = data['sex']
        patient.birthday = datetime.datetime.strptime(data['birthday'], "%Y-%m-%d").date()
        patient.age = data['age']
        patient.nation = data['nation']
        patient.height = data['height']
        patient.weight = data['weight']
        patient.education = data['education']
        patient.career = data['career']
        patient.marriage = data['marriage']
        patient.photo = data['photo']
        patient.homeAddr = data['homeAddr']
        patient.birthAddr = data['birthAddr']
        patient.activityAddr1 = data['activityAddr1']
        patient.activityAddr2 = data['activityAddr2']
        patient.actionAddr = data['actionAddr']
        patient.diastolicPressure = data['diastolicPressure']
        patient.systolicPressure = data['systolicPressure']
        patient.neckCircu = data['neckCircu']
        patient.payment = data['payment']
        patient.telephone = data['telephone']
        patient.cellphone = data['cellphone']
        patient.partnerPhone = data['partnerPhone']
        patient.save()
    except :
        return False


#修改指定家属信息
#data为患者新的信息，包括D_id，P_id，需要判断一下归属关系
#修改成功返回True,否则返回False
def updataRelationInfo(data):
    # TODO
    try:
        relation = RelationInfo.objects.get(id=data['R_id'])
        relation.name=data['name']
        relation.sex=data['sex']
        relation.telephone=data['telephone']
        relation.cellphone=data['cellphone']
        relation.weChate=data['weChat']
        relation.mail=data['mail']
        relation.homeAddr=data['homeAddr']
        relation.save()
    except :
        return False
