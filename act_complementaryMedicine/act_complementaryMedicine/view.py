# -*- coding:UTF-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import demjson
from db_method import insert,select,updata,delete


def get_test(request):
    if request.method == 'GET':
        data = request.GET
        print data
        message=[{'state':'success','method':'get','data':data}]
        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def post_test(request):
    if request.method == 'POST':
        data = request.POST
        print data
        message=[{'state':'success','method':'post','data':data}]
        js = demjson.encode(message)
        return HttpResponse(js)

#接口1
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        data['password'] = tools.md5(data['password'])
        if insert.addDoctorInfo(data) == True:
            result = 0
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口2
@csrf_exempt
def repeatCheck(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if select.checkExist(data['key'],data['value']):
            result = -1
        else:
            result = 0
        js = demjson.encode({'result':result})

        return HttpResponse(js)
#接口3
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message={'result':-1}
        #判断用户名是否存在
        if select.checkExist('userName',data['userName']):
            password = select.getUserInfo(data['userName'], 'password')
            # 判断密码是否正确
            if password == tools.md5(data['password']):
                message['result'] = 0
                request.session['D_id'] = select.getUserInfo(data['userName'], 'D_id')
            else:
                message['result'] = -1
        else:
            message['result'] = -1
        js =  demjson.encode(message)

        return HttpResponse(js)


#接口5
@csrf_exempt
def getDoctorBasicInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {}
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getDoctorBasicInfo(data['D_id'])
            message['result'] = 0
        else:
            message['result'] = -1
        js = demjson.encode(message)

        return HttpResponse(js)

#接口4
@csrf_exempt
def retrievePassword(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        #mail
        if data['type'] == 1:
            if data['mail_cellphone'] == select.getUserInfo(data['userName'], 'mail'):
                result = 0
                #TODO
            else:
                result = -1
        #cellphone
        else:
            if data['mail_cellphone'] == select.getUserInfo(data['userName'], 'cellphone'):
                result = 0
                #TODO
            else:
                result = -1
        js = demjson.encode({'result': result})
        return HttpResponse(js)

#接口6
@csrf_exempt
def getDoctorDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {}
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getDoctorDetailedInfo(data['D_id'])
            message['result'] = 0
        else:
            message['result'] = -1
        js = demjson.encode(message)
        return HttpResponse(js)


#接口7
@csrf_exempt
def updataDoctorInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if updata.updataDoctorInfo(data) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result': result})
        return HttpResponse(js)

#接口10
@csrf_exempt
def addExpGroup(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if insert.addExpGroup(data['D_id'],data['name'],data['information']) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口11
@csrf_exempt
def deleteExpGroup(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if delete.deleteExpGroup(data['D_id'],data['G_id']) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口8
@csrf_exempt
def getExpGroups(request):
    if request.method == 'POST':
        data = {}
        message = []
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getExpGroups(data['D_id'])
        js = demjson.encode(message)
        return HttpResponse(js)

#接口12
@csrf_exempt
def updataExpGroup(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            if updata.updataExpGroup(data['G_id'],data['name'],data['information']) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口9
@csrf_exempt
def getExpGroupPatientsInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            message = select.getExpGroupPatientsInfo(data['G_id'])
        js = demjson.encode(message)
        return HttpResponse(js)


#接口13
@csrf_exempt
def addPatientToExpGroup(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            if insert.addPatientToExpGroup(data['G_id'],data['P_id']):
                result = 0
            else:
                result = -1
        else:
            result = -1

        js = demjson.encode({'result': result})
        return HttpResponse(js)

#接口14
@csrf_exempt
def removePatientfromExpGroup(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            if delete.removePatientfromExpGroup(data['G_id'],data['P_id']):
                result = 0
            else:
                result = -1
        else:
            result = -1

        js = demjson.encode({'result': result})
        return HttpResponse(js)

#接口15
@csrf_exempt
def getPatientsBasicInfo(request):
    if request.method == 'POST':
        data = {}
        message = []
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getPatientsBasicInfo(data['D_id'])
        js = demjson.encode(message)

        return HttpResponse(js)

#接口16
@csrf_exempt
def getPatientDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getPatientDetailedInfo(data['P_id'])

        js = demjson.encode(message)

        return HttpResponse(js)


#接口17
@csrf_exempt
def addPatientInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if insert.addPatientInfo(data) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口18
@csrf_exempt
def updataPatientInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if updata.updataPatientInfo(data) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口19
@csrf_exempt
def getRelationsInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            message = select.getRelationInfos(data['P_id'])
        js = demjson.encode(message)
        return HttpResponse(js)

#接口20
@csrf_exempt
def updataRelationInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if updata.updataRelationInfo(data) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)

#接口21
@csrf_exempt
def addRelationInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if insert.addRelationInfo(data) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)


#接口22
@csrf_exempt
def deleteRelation(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if delete.deleteRelation(data['R_id']) == True:
                result = 0
            else:
                result = -1
        else:
            result = -1
        js = demjson.encode({'result':result})
        return HttpResponse(js)


#接口23
@csrf_exempt
def getCEHDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if data['type'] == 0:
                message = select.getPatientDetailedOutPatientServiceInfos(data['P_id'])
            elif data['type'] == 1:
                message = select.getPatientDetailedEmergCallInfos(data['P_id'])
            elif data['type'] == 2:
                message = select.getPatientDetailedInHospitalInfos( data['P_id'])

        js = demjson.encode(message)
        return HttpResponse(js)


#接口24
@csrf_exempt
def addCEHInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result':-1}
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if data['type'] == 0:
                result = insert.addOutPatientServiceInfo(data)
            elif data['type'] == 1:
                result = insert.addEmergCallInfo(data)
            elif data['type'] == 2:
                result = insert.addInHospitalInfo(data)
            else:
                result = False

            if result == True:
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)


#接口25
@csrf_exempt
def deleteCEHInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result':-1}
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if data['type'] == 0:
                result = delete.deleteOutPatientServiceInfo(data['id'])
            elif data['type'] == 1:
                result = delete.deleteEmergCallInfo(data['id'])
            elif data['type'] == 2:
                result = delete.deleteInHospitalInfo(data['id'])
            else:
                result = False

            if result == True:
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)

#接口26
@csrf_exempt
def updataCEHInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result':-1}
        if 'D_id' in request.session:
            data['D_id'] = request.session['D_id']
            if data['type'] == 0:
                result = updata.updataOutPatientServiceInfo(data)
            elif data['type'] == 1:
                result = updata.updataEmergCallInfo(data)
            elif data['type'] == 2:
                result = updata.updataInHospitalInfo(data)
            else:
                result = False

            if result == True:
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)


# 接口27
@csrf_exempt
def getCorQBasicInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            if data['kind'] == 0:
                message = select.getBasicClinicInfos(data['type'],data['S_id'])
            else:
                message = select.getBasicQuestionnaireInfos(data['type'],data['S_id'])

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def getClinicDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {}
        if 'D_id' in request.session:
            message = select.getDetailedClinicInfo(data['Cli_id'])

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def getQuestionnaireDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {}
        if 'D_id' in request.session:
            message = select.getDetailedQuestionnaireInfo(data['type'],data['id'])

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def addClinicInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if insert.addClinicInfo(data):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def addQuestionnaireInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if insert.addQuestionnaireInfo(data['type'],data):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def updataClinicInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if updata.updataClinicInfo(data):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)


@csrf_exempt
def updataQuestionnaireInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if updata.updataQuestionnaireInfo(data['type'],data):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)


@csrf_exempt
def deleteClinicInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if delete.deleteClinicInfo(data['Cli_id']):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def deleteQuestionnaireInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if delete.deleteQuestionnaireInfo(data['type'],data['id']):
                message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)



@csrf_exempt
def getAorAEDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = []
        if 'D_id' in request.session:
            if data['kind'] == 0:
                message = select.getDetailedAccessoryExamination(data['type'],data['S_id'])
            else:
                message = select.getDetailedAttachInfos(data['type'],data['S_id'])

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def addAorAEDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if data['kind'] == 0:
                if insert.addAccessoryExamination(data):
                    message['result'] = 0
            else:
                if insert.addAttachInfo(data):
                    message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)


@csrf_exempt
def updataAorAEDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if data['kind'] == 0:
                if updata.updataAccessoryExamination(data['id'],data):
                    message['result'] = 0
            else:
                if updata.updataAttachInfo(data['id'],data):
                    message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)

@csrf_exempt
def deleteAorAEDetailedInfo(request):
    if request.method == 'POST':
        data = demjson.decode(request.POST['data'])
        message = {'result': -1}
        if 'D_id' in request.session:
            if data['kind'] == 0:
                if delete.deleteAccessoryExamination(data['id']):
                    message['result'] = 0
            else:
                if delete.deleteAttachInfo(data['id']):
                    message['result'] = 0

        js = demjson.encode(message)
        return HttpResponse(js)