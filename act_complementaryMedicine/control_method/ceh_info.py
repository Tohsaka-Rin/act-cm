#多个问卷怎么处理？？？


from db_method import insert,delete,updata,select

def getBasicInfo(data):
    list = []
    if data['type'] == 0:
        list = select.getPatientBasicCEHInfo(data)
    elif data['type'] == 1:
        list = select.getPatientBasicClinicInfo(data)
    elif data['type'] == 2:
        list = select.getPatientBasicQuestionnaireInfo(data)
    return list

def getDetailedInfo(data):
    list = []
    message = {}
    if data['type'] == 0:
        message = select.getPatientDetailedCEHInfo(data)
    elif data['type'] == 1:
        message = select.getPatientDetailedClinicInfo(data)
    elif data['type'] == 2:
        message = select.getPatientDetailedQuestionnaireInfo(data)
    elif data['type'] == 3:
        message = select.getPatientDetailedAccessoryExaminationInfo(data)
    elif data['type'] == 4:
        message = select.getPatientDetailedAttachInfo(data)

    list.append(message)
    return list

def addInfo(data):
    result = False
    if data['type'] == 0 and insert.addPatientCEHInfo(data):
        result = True
    elif data['type'] == 1 and insert.addPatientClinicInfo(data):
        result = True
    elif data['type'] == 2 and insert.addPatientQuestionnaireInfo(data):
        result = True
    elif data['type'] == 3 and insert.addPatientAccessoryExaminationInfo(data):
        result = True
    elif data['type'] == 4 and insert.addPatientAttachInfo(data):
        result = True

    return result

def updataInfo(data):
    result = False
    if data['type'] == 0 and insert.updataPatientCEHInfo(data):
        result = True
    elif data['type'] == 1 and insert.updataPatientClinicInfo(data):
        result = True
    elif data['type'] == 2 and insert.updataPatientQuestionnaireInfo(data):
        result = True
    elif data['type'] == 3 and insert.updataPatientAccessoryExaminationInfo(data):
        result = True
    elif data['type'] == 4 and insert.updataPatientAttachInfo(data):
        result = True

    return result


def deleteInfo(data):
    result = False
    if data['type'] == 0 and insert.addPatientCEHInfo(data):
        result = True
    elif data['type'] == 1 and insert.addPatientClinicInfo(data):
        result = True
    elif data['type'] == 2 and insert.addPatientQuestionnaireInfo(data):
        result = True
    elif data['type'] == 3 and insert.addPatientAccessoryExaminationInfo(data):
        result = True
    elif data['type'] == 4 and insert.addPatientAttachInfo(data):
        result = True

    return result