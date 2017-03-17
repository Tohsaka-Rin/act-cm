# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo,GroupInfo,PatientInfo,PatientGroup,RelationInfo
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
    try:
        if key == 'password':
            result = DoctorInfo.objects.get(userName=userName).values_list('password')
        elif key == 'D_id':
            result = DoctorInfo.objects.get(userName=userName).values_list('id')
        else:
            return ""

        return result
    except:
        return ""

# 获取医生的基本信息
# D_id为医生的编号
# 以字典形式返回获取到的基本信息
def getDoctorBasicInfo(D_id):
    message = {}
    # TODO
    try:
        doctor = DoctorInfo.objects.get(id = D_id).values_list('name','userName','mail','cellphone','hospital','department')
        message['name'] = doctor[0]
        message['userName'] = doctor[1]
        message['mail'] = doctor[2]
        message['cellphone'] = doctor[3]
        message['hospital'] = doctor[4]
        message['department'] = doctor[5]
    except:
        print D_id
        print "Error in select.getDoctorBasicInfo"

    return message


# 获取医生的详细信息
# D_id为医生的编号
# 以字典形式返回获取到的详细信息
def getDoctorDetailedInfo(D_id):
    message = {}
    # TODO
    # date数据要处理一下
    try:
        doctor = DoctorInfo.objects.get(id=D_id).values_list('name', 'sex', 'birthday','userName', 'password','cellphone','weChat','mail', 'title', 'hospital','department','userGroup','registerDate')
        message['name'] = doctor[0]
        message['sex'] = doctor[1]
        message['birthday'] = doctor[2].strftime("%Y-%m-%d")
        message['userName'] = doctor[3]
        message['password'] = doctor[4]
        message['cellphone'] = doctor[5]
        message['weChat'] = doctor[6]
        message['mail'] = doctor[7]
        message['title'] = doctor[8]
        message['hospital'] = doctor[9]
        message['department'] = doctor[10]
        message['userGroup'] = doctor[11]
        message['registerDate'] = doctor[12].strftime("%Y-%m-%d")
    except:
        pass

    return message

#获取医生管理的实验组信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个实验组的信息
def getExpGroups(D_id):
    list = []
    # TODO
    try:
        message = {}
        groups = GroupInfo.objects.filter(D_id = D_id).values_list('id','name','information','data')
        for group in groups:
            message['G_id'] = group[0]
            message['name'] = group[1]
            message['information'] = group[2]
            message['data'] = group[3].strftime("%Y-%m-%d")
            list.append(message)
            message.clear()
    except:
        pass
    return list

#获取指定实验组中所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个患者的基本信息
def getExpGroupsPatientsInfo(D_id,G_id):
    list = []
    message = {}
    # TODO
    try:
        patient_ids = PatientGroup.objects.filter(G_id=G_id).values_list('P_id')
        for patient_id in patient_ids:
            patient_info = PatientInfo.objects.get(P_id=patient_id).values_list('P_id','name','sex','age','cellphone')
            message['P_id'] = patient_info[0]
            message['name'] = patient_info[1]
            message['sex'] = patient_info[2]
            message['age'] = patient_info[3]
            message['cellphone'] = patient_info[4]
            list.append(message)
            message.clear()
    except:
        pass

    return list

#获取指定医生管理的所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个实验组的信息
def getPatientsBasicInfo(D_id):
    list = []
    message = {}
    # TODO
    try:
        group_ids = GroupInfo.objects.filter(D_id = D_id).values_list('id')
        for group_id in group_ids:
            patient_ids = PatientGroup.objects.filter(G_id=group_id)
            for patient_id in patient_ids:
                patient_info = PatientInfo.objects.get(P_id=patient_id).values_list('P_id','name','sex','age','cellphone')
                message['P_id'] = patient_info[0]
                message['name'] = patient_info[1]
                message['sex'] = patient_info[2]
                message['age'] = patient_info[3]
                message['cellphone'] = patient_info[4]
                list.append(message)
                message.clear()
    except:
        pass

    return list



#获取指定医生管理的所有患者的基本信息
#还要返回患者所在实验组的信息
#注意判断一下P_id的正确性，失败返回一个空字典
def getPatientDetailedInfo(D_id,P_id):
    message={}
    # TODO
    try:
        patient = PatientInfo.objects.get(P_id = P_id).values_list('P_id','sign','name','sex','birthday','age','nation','height','weight','admissionTime','education',
                                                                   'career','marriage','photo','homeAddr','birthAddr','activityAddr1','activityAddr2','actionAddr',
                                                                   'diastolicPressure','systolicPressure','neckCircu','payment','telephone','cellphone','partnerPhone')
        message['P_id'] = patient[0]
        message['sign'] = patient[1]
        message['name'] = patient[2]
        message['sex'] = patient[3]
        message['birthday'] = patient[4].strftime("%Y-%m-%d")
        message['age'] = patient[5]
        message['nation'] = patient[6]
        message['height'] = patient[7]
        message['weight'] = patient[8]
        message['admissionTime'] = patient[9].strftime("%Y-%m-%d")
        message['education'] = patient[10]
        message['career'] = patient[11]
        message['marriage'] = patient[12]
        message['photo'] = patient[13]
        message['homeAddr'] = patient[14]
        message['birthAddr'] = patient[15]
        message['activityAddr1'] = patient[16]
        message['activityAddr2'] = patient[17]
        message['actionAddr'] = patient[18]
        message['diastolicPressure'] = patient[19]
        message['systolicPressure'] = patient[20]
        message['neckCircu'] = patient[21]
        message['payment'] = patient[22]
        message['telephone'] = patient[23]
        message['cellphone'] = patient[24]
        message['partnerPhone'] = patient[25]

        group_id = PatientGroup.objects.get(P_id = P_id)
        group = GroupInfo.objects.get(id = group_id).values_list('name','information')
        message['groupName'] = group[0]
        message['groupInfo'] = group[1]
    except:
        pass
    return message


#获取指定患者的所有家属信息基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个家属的信息
def getRelationsInfo(D_id,P_id):
    list=[]
    message = {}
    # TODO
    try:
        relations = RelationInfo.objects.filter(P_id = P_id).values_list('P_id','name','sex','telephone','cellphone','weChat','mail','homeAddr')
        for relation in relations:
                message['P_id'] = relation[0]
                message['name'] = relation[1]
                message['sex'] = relation[2]
                message['telephone'] = relation[3]
                message['cellphone'] = relation[4]
                message['weChat'] = relation[5]
                message['mail'] = relation[6]
                message['homeAddr'] = relation[7]
                list.append(message)
                message.clear()
    except:
        pass
    return list



# def getPatientBasicCEHInfo(data):
#     list = []
#     item = {}
#     try:
#         #TODO
#         #检查医患对应关系
#         if data['kind'] == 0:
#             #TODO
#             results = OutPatientServiceInfo.objects.filter(P_id = data['P_id']).values_list('id','date','place','symptom')
#         elif data['kind'] == 1:
#             #TODO
#             results = EmergCallInfo.objects.filter(P_id=data['P_id']).values_list('id','date','place','symptom')
#         elif data['kind'] == 2:
#             #TODO
#             results = InHospitalInfo.objects.filter(P_id=data['P_id']).values_list('id','date','place','symptom')
#         else:
#             return list
#
#         for result in results:
#             item['id'] = result[0]
#             item['date'] = result[1]
#             item['place'] = result[2]
#             item['symptom'] = result[3]
#             list.append(item)
#             item.clear()
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicCEHInfo"
#         print data
#         return list
#
#
# def getPatientBasicClinicInfo(data):
#     list = []
#     item = {}
#     try:
#         # TODO
#         # 检查医患对应关系
#         if data['kind'] == 0:
#             #TODO
#             results = Clinic.objects.filter(id=data['X_id']).values_list('id', 'dangerType')
#         elif data['kind'] == 1:
#             #TODO
#             results = Clinic.objects.filter(id=data['X_id']).values_list('id', 'dangerType')
#         elif data['kind'] == 2:
#             #TODO
#             results = Clinic.objects.filter(id=data['X_id']).values_list('id', 'dangerType')
#         else:
#             return list
#
#         for result in results:
#             item['id'] = result[0]
#             item['dangerType'] = result[1]
#             list.append(item)
#             item.clear()
#
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicClinicInfo"
#         print data
#         return list
#
#
# def getPatientBasicQuestionnaireInfo(data):
#     list = []
#     try:
#         if data['kind'] == 0:
#             #TODO
#         elif data['kind'] == 1:
#             #TODO
#         elif data['kind'] == 2:
#             #TODO
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicQuestionnaireInfo"
#         print data
#         return list
#
#
#
#
# def getPatientDetailedCEHInfo(data):
#     list = []
#     item = {}
#     try:
#         #TODO
#         #检查医患对应关系
#         if data['kind'] == 0:
#             #TODO
#             result = OutPatientServiceInfo.objects.get(id = data['X_id'])
#         elif data['kind'] == 1:
#             #TODO
#             result = EmergCallInfo.objects.get(id = data['X_id'])
#         elif data['kind'] == 2:
#             #TODO
#             result = InHospitalInfo.objects.get(id = data['X_id'])
#         else:
#             return list
#         #TODO
#         #将result改为字典
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicCEHInfo"
#         print data
#         return list
#
#
# def getPatientDetailedClinicInfo(data):
#     list = []
#     item = {}
#     try:
#         # TODO
#         # 检查医患对应关系
#         if data['kind'] == 0:
#             #TODO
#             result = Clinic.objects.get(id = data['Y_id'])
#         elif data['kind'] == 1:
#             #TODO
#             result = Clinic.objects.get(id = data['Y_id'])
#         elif data['kind'] == 2:
#             #TODO
#             result = Clinic.objects.get(id = data['Y_id'])
#         else:
#             return list
#
#         for result in results:
#             item['id'] = result[0]
#             item['dangerType'] = result[1]
#             list.append(item)
#             item.clear()
#
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicClinicInfo"
#         print data
#         return list
#
#
# def getPatientDetailedQuestionnaireInfo(data):
#     list = []
#     try:
#         if data['kind'] == 0:
#             #TODO
#
#         elif data['kind'] == 1:
#             #TODO
#         elif data['kind'] == 2:
#             #TODO
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicQuestionnaireInfo"
#         print data
#         return list
#
#
# def getPatientDetailedAccessoryExaminationInfo(data):
#     list = []
#     try:
#         if data['kind'] == 0:
#             #TODO
#         elif data['kind'] == 1:
#             #TODO
#         elif data['kind'] == 2:
#             #TODO
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicQuestionnaireInfo"
#         print data
#         return list
#
# def getPatientDetailedAttachInfo(data):
#     list = []
#     try:
#         if data['kind'] == 0:
#             #TODO
#             result = AttachInfo.objects.get(id = data['Y_id'])
#         elif data['kind'] == 1:
#             #TODO
#             result = AttachInfo.objects.get(id=data['Y_id'])
#         elif data['kind'] == 2:
#             #TODO
#             result = AttachInfo.objects.get(id=data['Y_id'])
#         else:
#             return list
#
#         return list
#     except:
#         print "ERROR IN select.getPatientBasicQuestionnaireInfo"
#         print data
#         return list