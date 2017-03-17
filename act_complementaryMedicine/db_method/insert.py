# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo,GroupInfo,PatientGroup,PatientInfo,RelationInfo
import time
import datetime
# 添加新用户
# 参数是一个字典，包含医生的所有信息
# 成功返回True，失败返回False

def addDoctorInfo(data):
    #TODO
    # birthday 需要处理成Date格式
    d = datetime.datetime.strptime(data['birthday'], "%Y-%m-%d").date()
    # registerDate会自动生成
    try:
        newDoctor = DoctorInfo(name=data['name'],sex=data['sex'],birthday=data['birthday'],userName=data['userName'],password=data['password'],
                               cellphone=data['cellphone'],weChat=data['weChat'],mail=data['mail'],title=data['title'],hospital=data['hospital'],
                               department=data['department'],userGroup=data['userGroup'])
        newDoctor.save()
        return True
    except :
        return False

# 添加新的实验组
# 成功返回True，失败返回False
def addExpGroup(D_id,name,info):
    # TODO
    try:
        newExpGroup = GroupInfo(D_id=D_id,name=name,information=info)
        newExpGroup.save()
        return True
    except :
        return False

# 向实验组中添加患者
#注意判断一下各种id的正确性
# 成功返回True，失败返回False
def addPatientToExpGroupdata(D_id,G_id,P_id):
    # TODO
    try:
        newP = PatientGroup(G_id=G_id,P_id=P_id)
        newP.save()
        return True
    except :
        return False

# 添加新患者
# 参数是一个字典，包含患者的所有信息。同时也包含D_id与G_id，需要添加对应的关系表
# 成功返回True，失败返回False
def addPatientInfo(data):
    #TODO
    try:
        newPatient = PatientInfo(P_id=data['P_id'],sign=data['sign'],name=data['name'],sex=data['sex'],birthday=datetime.datetime.strptime(data['birthday'], "%Y-%m-%d").date(),
                                 age=data['age'],nation=data['nation'],height=data['height'],weight=data['weight'],education=data['education'],
                                 career=data['data'],marriage=data['marriage'],photo=data['data'],homeAddr=data['homeAddr'],birthAddr=data['birthAddr'],
                                 activityAddr1=data['activityAddr1'],activityAddr2=data['activityAddr2'],actionAddr=data['actionAddr'],diastolicPressure=data['diastolicPressure'],systolicPressure=data['systolicPressure'],
                                 neckCircu=data['neckCircu'],payment=data['payment'],telephone=data['telephone'],cellphone=data['cellphone'],partnerPhone=data['partnerPhone'])
        newPatient.save()

        newP = PatientGroup(G_id=data['G_id'], P_id=data['P_id'])
        newP.save()
        return True
    except :
        return False

# 添加新家属
# 参数是一个字典，包含患者的所有信息。同时也包含D_id与P_id
# 成功返回True，失败返回False
def addRelationInfo(data):
    try:
        newRelation = RelationInfo(P_id=data['P_id'],name=data['name'],sex=data['sex'],telephone=data['telephone'],cellphone=data['cellphone'],weChat=data['weChat'],mail=data['mail'],homeAddr=data['homeAddr'])
        newRelation.save()
        return True
    except :
        return False


