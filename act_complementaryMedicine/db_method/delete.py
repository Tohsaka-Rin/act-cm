# -*- coding:UTF-8 -*-
from act_db.models import GroupInfo,PatientGroup,RelationInfo

#删除指定实验组
#注意判断一下D_id与G_id是否正确，删除时注意一下删除患者与实验组对应关系那张表中的内容
# 成功返回True，失败返回False
def deleteExpGroup(D_id,G_id):
    #TODO
    try:

        group = GroupInfo.objects.get(D_id=D_id,id=G_id)
        group.delete()
        # 没有使用外码
        PatientGroup.objects.filter(G_id=G_id).delete()
        return True
    except:
        return False



# 从实验组中删除患者
# 注意判断一下各种id的正确性
# 成功返回True，失败返回False
def removePatientfromExpGroup(D_id, G_id, P_id):
    # TODO
    try:
        patient = PatientGroup.objects.get(G_id = G_id, P_id = P_id)
        patient.delete()
        return True
    except :
        return False


#删除指定患者
#注意判断一下D_id与P_id是否正确
# 成功返回True，失败返回False
def deleteRelation(D_id, P_id, R_id):
    # TODO
    try:
        relation = RelationInfo.objects.get(id = R_id)
        relation.delete()
        return True
    except:
        return False





