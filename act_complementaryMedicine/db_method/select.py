# -*- coding:UTF-8 -*-
from act_db.models import DoctorInfo,GroupInfo,PatientInfo,PatientGroup,RelationInfo,OutPatientServiceInfo,EmergCallInfo,InHospitalInfo,Clinic,ESS,MBQ,SGRO,AttachInfo,AccessoryExamination,CATandMRC,PmExposure
from django.core.exceptions import ObjectDoesNotExist
from control_method import tools


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
        value = DoctorInfo.objects.get(id = D_id).values_list('name','userName','mail','cellphone','hospital','department')
        keys = ['name','userName','mail','cellphone','hospital','department']
        message = tools.dictPackage(keys,value)
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
        value = DoctorInfo.objects.get(id=D_id).values_list('name', 'sex', 'birthday','userName', 'cellphone','weChat','mail', 'title', 'hospital','department','userGroup','registerDate')
        keys = ['name', 'sex', 'birthday','userName','cellphone','weChat','mail', 'title', 'hospital','department']
        value[2] = value[2].strftime("%Y-%m-%d")
        value[12] = value[12].strftime("%Y-%m-%d")
        message = tools.dictPackage(keys, value)
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
        values = GroupInfo.objects.filter(D_id = D_id).values_list('id','name','information','data')
        keys = ['G_id','name','information','data']
        for value in values:
            value[3] = value[3].strftime("%Y-%m-%d")
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass
    return list

#获取指定实验组中所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个患者的基本信息
def getExpGroupPatientsInfo(G_id):
    list = []
    message = {}
    # TODO
    try:
        patient_ids = PatientGroup.objects.filter(G_id=G_id).values_list('P_id')
        keys = ['P_id', 'name', 'sex', 'age', 'cellphone']
        for patient_id in patient_ids:
            value = PatientInfo.objects.get(P_id=patient_id).values_list('P_id','name','sex','age','cellphone')

            message = tools.dictPackage(keys, value)
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
            keys = ['P_id', 'name', 'sex', 'age', 'cellphone']
            for patient_id in patient_ids:
                value = PatientInfo.objects.get(P_id=patient_id).values_list('P_id','name','sex','age','cellphone')

                message = tools.dictPackage(keys, value)
                list.append(message)
                message.clear()
    except:
        pass

    return list



#获取指定医生管理的所有患者的基本信息
#还要返回患者所在实验组的信息
#注意判断一下P_id的正确性，失败返回一个空字典
def getPatientDetailedInfo(P_id):
    message={}
    # TODO
    try:
        value = PatientInfo.objects.get(P_id = P_id).values_list('P_id','sign','name','sex','birthday','age','nation','height','weight','admissionTime','education',
                                                                   'career','marriage','photo','homeAddr','birthAddr','activityAddr1','activityAddr2','actionAddr',
                                                                   'diastolicPressure','systolicPressure','neckCircu','payment','telephone','cellphone','partnerPhone')

        keys = ['P_id','sign','name','sex','birthday','age','nation','height','weight','admissionTime','education',
                'career','marriage','photo','homeAddr','birthAddr','activityAddr1','activityAddr2','actionAddr',
                'diastolicPressure','systolicPressure','neckCircu','payment','telephone','cellphone','partnerPhone']
        message = tools.dictPackage(keys, value)

        group_id = PatientGroup.objects.get(P_id = P_id)
        group = GroupInfo.objects.get(id = group_id).values_list('name','information')
        message['groupName'] = group[0]
        message['groupInfo'] = group[1]
    except:
        pass
    return message


#获取指定患者的所有家属信息基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个家属的信息
def getRelationInfos(P_id):
    list=[]
    message = {}
    # TODO
    try:
        values = RelationInfo.objects.filter(P_id = P_id).values_list('P_id','name','sex','telephone','cellphone','weChat','mail','homeAddr')
        keys = ['P_id','name','sex','telephone','cellphone','weChat','mail','homeAddr']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass
    return list


#获取临床基本信息
def getBasicClinicInfos(type,S_id):
    list = []
    message = {}
    try:
        values = Clinic.objects.filter(type = type, S_id = S_id).values_list('id','lung3')
        keys = ['Cli_id','lung3']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list

#获取问卷的基本信息
#返回值type:
#ESS   0
#MBQ   1
#SGRO  2
def getBasicQuestionnaireInfos(type,S_id):
    list = []
    message = {}
    try:
        values = ESS.objects.filter(type = type, S_id = S_id).values_list('id','score')
        keys = ['ESS_id','score']
        for value in values:
            message = tools.dictPackage(keys, value)
            message['type'] = 0
            list.append(message)
            message.clear()

        values = MBQ.objects.filter(type=type, S_id=S_id).values_list('id', 'BMI')
        keys = ['MBQ_id', 'BMI']
        for value in values:
            message = tools.dictPackage(keys, value)
            message['type'] = 1
            list.append(message)
            message.clear()

        values = SGRO.objects.filter(type=type, S_id=S_id).values_list('id')
        keys = ['SGRO_id']
        for value in values:
            message = tools.dictPackage(keys, value)
            message['type'] = 2
            list.append(message)
            message.clear()
    except:
        pass

    return list


#获取某个病人所有的门诊的详细信息
def getPatientDetailedOutPatientServiceInfos(P_id):
    list = []
    message = {}
    try:
        values = OutPatientServiceInfo.objects.filter(P_id = P_id).values_list('id','P_id','date','place','isStabel',
                                                                               'symptom','physicalExam','breathErr',
                                                                               'acuteExac','disease','use_abt',
                                                                               'useJmzs','hospital','airRelate',
                                                                               'treatMetho','medicine')
        keys = ['OPS_id','P_id','date','place','isStabel','symptom','physicalExam','breathErr','acuteExac','disease',
                'use_abt','useJmzs','hospital','airRelate','treatMethod','medicine']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list

# 获取某个病人所有的急诊的详细信息
def getPatientDetailedEmergCallInfos(P_id):
    list = []
    message = {}
    try:
        values = EmergCallInfo.objects.filter(P_id=P_id).values_list('id','P_id','date','place','symptom','acuteExac',
                                                                     'disease','byxCheck','byxResult','ycWcTreat',
                                                                     'useAbt','abtType','useJmzs','ecMethod','ecDate',
                                                                     'hospital','treatMethod','airRelate')
        keys = ['EC_id','P_id','date','place','symptom','acuteExac','disease','byxCheck','byxResult','ycWcTreat',
                'useAbt','abtType','useJmzs','ecMethod','ecDate','hospital','treatMethod','airRelate']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list

#获取某个病人所有的住院的详细信息
def getPatientDetailedInHospitalInfos(P_id):
    list = []
    message = {}
    try:
        values = InHospitalInfo.objects.filter(P_id = P_id).values_list('id', 'P_id', 'time', 'place', 'commonIcu',
                                                                        'symptom', 'acuteExac', 'disease', 'byxCheck',
                                                                        'byxResult', 'ycWcTreat', 'useAbt', 'abtType',
                                                                        'useJmzs', 'hospitalDays', 'airRelate',
                                                                        'treatMethod', 'reason', 'docAdvice')
        keys = ['IH_id', 'P_id', 'time', 'place', 'commonIcu', 'symptom', 'acuteExac', 'disease', 'byxCheck',
                'byxResult', 'ycWcTreat', 'useAbt', 'abtType', 'useJmzs', 'hospitalDays', 'airRelate',
                'treatMethod', 'reason', 'docAdvice']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list


#获取指定的某个临床的详细信息
def getDetailedClinicInfo(Cli_id):
    message = {}
    try:
        value = Clinic.objects.get(id = Cli_id).values_list('id', 'P_id', 'type', 'S_id', 'dangerType', 'smoke1',
                                                            'smoke2', 'smoke3', 'smoke4', 'smoke5', 'smoke6', 'smoke7',
                                                            'smoke8', 'smoke9', 'smoke10', 'powder1', 'powder2',
                                                            'powder3', 'biology1', 'biology2', 'hAir1', 'hAir2', 'gm1',
                                                            'gm2', 'drink1', 'drink2', 'drink3', 'drink4', 'lung1',
                                                            'lung2', 'lung3', 'lung4', 'lung5', 'lung6', 'lung7',
                                                            'cure1', 'cure2', 'cure3', 'cure4', 'cure5', 'cure6',
                                                            'cure7', 'cure8', 'cure9', 'cure10', 'cure11', 'cure12',
                                                            'cure13', 'cure14', 'cure15', 'cure16', 'cure17', 'cure18',
                                                            'cure19', 'cure20', 'cure21', 'cure22', 'cure23', 'cure24',
                                                            'cure25', 'cure26', 'comp1', 'comp2', 'comp3', 'comp4',
                                                            'comp5', 'comp6')
        keys = ['Cli_id', 'P_id', 'type', 'S_id', 'dangerType', 'smoke1', 'smoke2', 'smoke3', 'smoke4', 'smoke5',
                'smoke6', 'smoke7', 'smoke8', 'smoke9', 'smoke10', 'powder1', 'powder2', 'powder3', 'biology1',
                'biology2', 'hAir1', 'hAir2', 'gm1', 'gm2', 'drink1', 'drink2', 'drink3', 'drink4', 'lung1', 'lung2',
                'lung3', 'lung4', 'lung5', 'lung6', 'lung7', 'cure1', 'cure2', 'cure3', 'cure4', 'cure5', 'cure6',
                'cure7', 'cure8', 'cure9', 'cure10', 'cure11', 'cure12', 'cure13', 'cure14', 'cure15', 'cure16',
                'cure17', 'cure18', 'cure19', 'cure20', 'cure21', 'cure22', 'cure23', 'cure24', 'cure25', 'cure26',
                'comp1', 'comp2', 'comp3', 'comp4', 'comp5', 'comp6']
        message = tools.dictPackage(keys, value)
    except:
        pass

    return message

#获取指定的某个问卷的详细信息
#type:
#ESS   0
#MBQ   1
#SGRO  2
def getDetailedQuestionnaireInfo(type,Q_id):
    message = {}
    try:
        if type == 0:
            value = ESS.objects.filter(id=Q_id).values_list('id', 'P_id', 'type', 'S_id', 'ess4', 'ess5', 'ess6',
                                                            'ess7', 'ess8', 'score')
            keys = ['ESS_id', 'P_id', 'type', 'S_id', 'ess4', 'ess5', 'ess6', 'ess7', 'ess8', 'score']
            message = tools.dictPackage(keys, value)
            message['type'] = 0
        elif type == 1:
            value = MBQ.objects.filter(d=Q_id).values_list('MBQ_id', 'P_id', 'type', 'S_id', 'q4', 'q5', 'q6', 'q7',
                                                           'q8', 'q9', 'q10', 'BMI')
            keys = ['MBQ_id', 'P_id', 'type', 'S_id', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'BMI']
            message = tools.dictPackage(keys, value)
            message['type'] = 1
        elif type == 2:
            value = SGRO.objects.filter(d=Q_id).values_list('Sgro_id', 'P_id', 'type', 'S_id', 'H4', 'H5', 'H6', 'H7',
                                                            'H8', 'H9', 'H10', 'H11_1', 'H11_2', 'H11_3', 'H11_4',
                                                            'H11_5', 'H11_6', 'H11_7', 'H12_1', 'H12_2', 'H12_3',
                                                            'H12_4', 'H12_5', 'H12_6', 'H13_1', 'H13_2', 'H13_3',
                                                            'H13_4', 'H13_5', 'H13_6', 'H13_7', 'H13_8', 'H14',
                                                            'H15_1', 'H15_2', 'H15_3', 'H15_4', 'H16_1', 'H16_2',
                                                            'H16_3', 'H16_4', 'H16_5', 'H16_6', 'H16_7', 'H16_8',
                                                            'H16_9', 'H16_10', 'H17-1', 'H17-2', 'H17-3', 'H17-4',
                                                            'H17-5', 'H18', 'actEff')
            keys = ['Sgro_id', 'P_id', 'type', 'S_id', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11_1', 'H11_2',
                    'H11_3', 'H11_4', 'H11_5', 'H11_6', 'H11_7', 'H12_1', 'H12_2', 'H12_3', 'H12_4', 'H12_5', 'H12_6',
                    'H13_1', 'H13_2', 'H13_3', 'H13_4', 'H13_5', 'H13_6', 'H13_7', 'H13_8', 'H14', 'H15_1', 'H15_2',
                    'H15_3', 'H15_4', 'H16_1', 'H16_2', 'H16_3', 'H16_4', 'H16_5', 'H16_6', 'H16_7', 'H16_8', 'H16_9',
                    'H16_10', 'H17-1', 'H17-2', 'H17-3', 'H17-4', 'H17-5', 'H18', 'actEff']
            message = tools.dictPackage(keys, value)
            message['type'] = 2

    except:
        pass

    return message





#获取某个 门诊/急诊/住院/辅助检查 对应的所有附件信息
# type: 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
def getDetailedAttachInfos(type,S_id):
    list = []
    message = {}
    try:
        values = AttachInfo.objects.filter(type = type, S_id = S_id).values_list('id', 'P_id', 'type', 'S_id', 'D_id', 'name', 'information', 'dir')
        keys = ['A_id', 'P_id', 'type', 'S_id', 'D_id', 'name', 'information', 'dir']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list

#获取某个 门诊/急诊/住院 对应的所有辅助检查信息
def getDetailedAccessoryExamination(type,S_id):
    list = []
    message = {}
    try:
        values = AccessoryExamination.objects.filter(type = type, S_id = S_id).values_list('id', 'S_id', 'type', 'date', 'AE_type', 'name', 'description', 'D_id')
        keys = ['AE_id', 'S_id', 'type', 'date', 'AE_type', 'name', 'description', 'D_id']
        for value in values:
            message = tools.dictPackage(keys, value)
            list.append(message)
            message.clear()
    except:
        pass

    return list

# get the message of a patient for the last 2 weeks
# type = 1 is CAT and MRC sum, type = 2 is explosure
def getMsg2Weeks(P_id, type):
    from django.utils.timezone import now, timedelta
    end = now().date()
    start = end - timedelta(weeks=2)
    message={}
    try:
        if type == 1:
            values = CATandMRC.objects.filter(date_range=(start, end), P_id=P_id).values_list('catSum')
        elif type == 2:
            values = PmExposure.objects.filter(date_range=(start, end), P_id=P_id).values_list('exposure')
        else:
            return message
        keys = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7',
                'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14']
        message = tools.dictPackage(keys, values)
    except:
        pass
    return message