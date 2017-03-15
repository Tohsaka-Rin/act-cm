# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo

# 添加新用户
# 参数是一个字典，包含医生的所有信息
# 成功返回True，失败返回False

def addDoctorInfo(data):
    #TODO
    # birthday 需要处理成Date格式
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
    return False

# 向实验组中添加患者
#注意判断一下各种id的正确性
# 成功返回True，失败返回False
def addPatientToExpGroupdata(D_id,G_id,P_id):
    # TODO
    return False

# 添加新患者
# 参数是一个字典，包含患者的所有信息。同时也包含D_id与G_id，需要添加对应的关系表
# 成功返回True，失败返回False
def addPatientInfo(data):
    #TODO
    return False

# 添加新家属
# 参数是一个字典，包含患者的所有信息。同时也包含D_id与P_id
# 成功返回True，失败返回False
def addRelationInfo(data):
    #TODO
    return False


