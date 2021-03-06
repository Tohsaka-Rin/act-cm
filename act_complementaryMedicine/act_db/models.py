# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class PatientInfo(models.Model):
    P_id = models.CharField(max_length=10, unique=True)
    sign = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)
    birthday = models.DateField(blank=True)
    age = models.IntegerField()
    nation = models.CharField(max_length=15, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    registerTime = models.DateField(auto_now_add=True)
    education = models.CharField(max_length=10, blank=True)
    career = models.CharField(max_length=20)
    marriage = models.CharField(max_length=20)
    photo = models.CharField(max_length=50, blank=True)
    homeAddr = models.CharField(max_length=150)
    birthAddr = models.CharField(max_length=50)
    activityAddr1 = models.CharField(max_length=150)
    activityAddr2 = models.CharField(max_length=150)
    actionAddr = models.FloatField()  # this details need be filled
    diastolicPressure = models.FloatField()  # same with upper
    systolicPressure = models.FloatField()  # same
    neckCircu = models.FloatField()
    payment = models.CharField(max_length=32)  # example 1,2,3,4,5,6,7
    telephone = models.CharField(max_length=15)
    cellphone = models.CharField(max_length=11)
    partnerPhone = models.CharField(max_length=11)


# created by JK@buaa, 2017/3/17
# table 2


class RelationInfo(models.Model):
    P_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)
    telephone = models.CharField(max_length=15)
    cellphone = models.CharField(max_length=11)
    weChat = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    honeAddr = models.CharField(max_length=150)


# created by JK@buaa, 2017/3/17
# table 3


class DoctorInfo(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)
    birthday = models.DateField()
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=11)
    weChat = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    hospital = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    userGroup = models.CharField(max_length=10)      # doctor/intern/student
    registerDate = models.DateField(auto_now_add=True)


# table 4


class PatientGroup(models.Model):
    G_id = models.IntegerField()
    P_id = models.CharField()


# created by JK@buaa, 2017/3/17
# table 5


class GroupInfo(models.Model):
    name = models.CharField(max_length=100, null=False)
    D_id = models.IntegerField()
    information = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


# created by JK@buaa, 2017/3/17
# table 6


class CATandMRC(models.Model):
    # CM_id = models.CharField(max_length=32,primary_key=True)
    P_id = models.CharField(max_length=10)
    date = models.DateField()
    cat1 = models.CharField(max_length=2)
    cat2 = models.CharField(max_length=2)
    cat3 = models.CharField(max_length=2)
    cat4 = models.CharField(max_length=2)
    cat5 = models.CharField(max_length=2)
    cat6 = models.CharField(max_length=2)
    cat7 = models.CharField(max_length=2)
    cat8 = models.CharField(max_length=2)
    catSum = models.CharField(max_length=3)
    mrc = models.CharField(max_length=2)
    acuteExac = models.CharField(max_length=1)


# created by JK@buaa, 2017/3/17
# table 7


class PmExposure(models.Model):
    P_id = models.CharField(max_length=10)
    date = models.DateField()
    exposure = models.CharField(max_length=10)


# created by JK@buaa, 2017/3/17
# table 8


class TrackInfo(models.Model):
    P_id = models.CharField(max_length=10)
    date = models.DateField()
    name = models.CharField(max_length=32)
    dir = models.CharField(max_length=50)


# created by JK@buaa, 2017/3/17
# table 9


class AttachInfo(models.Model):
    P_id = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    type = models.IntegerField()                # 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
    S_id = models.IntegerField()
    D_id = models.CharField(max_length=10)
    name = models.CharField(max_length=32)
    information = models.CharField(max_length=255)
    source = models.CharField(max_length=32)
    dir = models.CharField(max_length=50)
    #context = models.ImageField(upload_to)


# createdby JK@buaa, 2017/3/17
# table 10


class PM25(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 11


class CO(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 12


class NO2(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 13


class SO2(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 14


class PM10(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 15


class O3(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.FloatField()
    yunGang = models.FloatField()
    yongLeDian = models.FloatField()
    dongDingMenNei = models.FloatField()
    yiZhuang = models.FloatField()
    yanQing = models.FloatField()
    xiZhiMenBei = models.FloatField()
    wanShouGongXi = models.FloatField()
    wanLiu = models.FloatField()
    tongZhou = models.FloatField()
    tianTan = models.FloatField()
    qianMen = models.FloatField()
    pingGu = models.FloatField()
    nongZhanGuan = models.FloatField()
    nanSanHuan = models.FloatField()
    miYunShuiKu = models.FloatField()
    menTouGou = models.FloatField()
    liuLiHe = models.FloatField()
    huaiRou = models.FloatField()
    guanYuan = models.FloatField()
    guCheng = models.FloatField()
    fengTaiHuaYuan = models.FloatField()
    fangShan = models.FloatField()
    dongSiHuan = models.FloatField()
    dongSi = models.FloatField()
    dongGaoCun = models.FloatField()
    dingLing = models.FloatField()
    daXing = models.FloatField()
    changPing = models.FloatField()
    beiBuXinQu = models.FloatField()
    baDaLing = models.FloatField()
    aoTiZhongXin = models.FloatField()


# createdby JK@buaa, 2017/3/17
# table 16


class WeatherInfo(models.Model):
    dateTime = models.DateTimeField()
    zhiWuYuan = models.CharField(max_length=15)
    yunGang = models.CharField(max_length=15)
    yongLeDian = models.CharField(max_length=15)
    dongDingMenNei = models.CharField(max_length=15)
    yiZhuang = models.CharField(max_length=15)
    yanQing = models.CharField(max_length=15)
    xiZhiMenBei = models.CharField(max_length=15)
    wanShouGongXi = models.CharField(max_length=15)
    wanLiu = models.CharField(max_length=15)
    tongZhou = models.CharField(max_length=15)
    tianTan = models.CharField(max_length=15)
    qianMen = models.CharField(max_length=15)
    pingGu = models.CharField(max_length=15)
    nongZhanGuan = models.CharField(max_length=15)
    nanSanHuan = models.CharField(max_length=15)
    miYunShuiKu = models.CharField(max_length=15)
    menTouGou = models.CharField(max_length=15)
    liuLiHe = models.CharField(max_length=15)
    huaiRou = models.CharField(max_length=15)
    guanYuan = models.CharField(max_length=15)
    guCheng = models.CharField(max_length=15)
    fengTaiHuaYuan = models.CharField(max_length=15)
    fangShan = models.CharField(max_length=15)
    dongSiHuan = models.CharField(max_length=15)
    dongSi = models.CharField(max_length=15)
    dongGaoCun = models.CharField(max_length=15)
    dingLing = models.CharField(max_length=15)
    daXing = models.CharField(max_length=15)
    changPing = models.CharField(max_length=15)
    beiBuXinQu = models.CharField(max_length=15)
    baDaLing = models.CharField(max_length=15)
    aoTiZhongXin = models.CharField(max_length=15)


# created by CS@buaa, 2017/3/17
# table17:


class OutPatientServiceInfo(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    date = models.DateField(null=False)
    place = models.CharField(max_length=150, null=False)
    isStable = models.CharField(max_length=1, null=False)
    symptom = models.CharField(max_length=10, null=False, )
    physicalExam = models.CharField(max_length=1, null=False)
    breathErr = models.CharField(max_length=50)
    acuteExac = models.CharField(max_length=1)
    disease = models.CharField(max_length=50, null=False)
    use_abt = models.CharField(max_length=20, null=False)
    useJmzs = models.CharField(max_length=1, null=False)
    hospital = models.CharField(max_length=1, null=False)
    airRelate = models.CharField(max_length=1, null=False)
    treatMethod = models.CharField(max_length=1, null=False)
    medicine = models.CharField(max_length=50, null=False)


# created by CS@buaa, 2017/3/17
# table18:


class EmergCallInfo(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    data = models.DateField(null=False)
    place = models.CharField(max_length=250, null=False)
    symptom = models.CharField(max_length=15, null=False)
    acuteExac = models.CharField(max_length=1)
    disease = models.CharField(max_length=50, null=False)
    byxCheck = models.CharField(max_length=1, null=False)
    byxResult = models.CharField(max_length=20)
    ysWcTreat = models.CharField(max_length=1, null=False)
    useAbt = models.CharField(max_length=1, null=False)
    abtType = models.CharField(max_length=20)
    useJmzs = models.CharField(max_length=1, null=False)
    ecMethod = models.CharField(max_length=10)
    ecDate = models.DateField()
    hospital = models.CharField(max_length=1, null=False)
    treatMethod = models.CharField(max_length=1, null=False)
    airRelate = models.CharField(max_length=1, null=False)


# created by CS@buaa, 2017/3/17
# table19:


class InHospitalInfo(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    date = models.DateField(null=False)
    place = models.CharField(max_length=250, null=False)
    commonIcu = models.CharField(max_length=1, null=False)
    symptom = models.CharField(max_length=15, null=False)
    acuteExac = models.CharField(max_length=1)
    disease = models.CharField(max_length=50, null=False)
    byxCheck = models.CharField(max_length=1, null=False)
    byxResult = models.CharField(max_length=20)
    ysWcTreat = models.CharField(max_length=1, null=False)
    useAbt = models.CharField(max_length=1)
    abtType = models.CharField(max_length=20, null=False)
    useJmzs = models.CharField(max_length=1, null=False)
    hospitalDays = models.IntegerField(null=False)
    airRelate = models.CharField(max_length=1, null=False)
    treatMethod = models.CharField(max_length=1, null=False)
    reason = models.CharField(max_length=200, null=False)
    docAdvice = models.CharField(max_length=200)


# created by CS@buaa, 2017/3/17
# table20:


class Clinic(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    type = models.IntegerField(null=False)  # 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
    S_id = models.IntegerField(null=False)
    dangerType = models.CharField(max_length=20, null=False)
    smoke1 = models.CharField(max_length=1, null=False)
    smoke2 = models.IntegerField(null=False)
    smoke3 = models.IntegerField(null=False)
    smoke4 = models.IntegerField(null=False)
    smoke5 = models.IntegerField(null=False)
    smoke6 = models.IntegerField(null=False)
    smoke7 = models.IntegerField(null=False)
    smoke8 = models.CharField(max_length=1, null=False)
    smoke9 = models.IntegerField(null=False)
    smoke10 = models.IntegerField(null=False)
    powder1 = models.IntegerField(null=False)
    powder2 = models.CharField(max_length=50, null=False)
    powder3 = models.CharField(max_length=50, null=False)
    biology1 = models.IntegerField(null=False)
    biology2 = models.CharField(max_length=50, null=False)
    hAir1 = models.IntegerField(null=False)
    hAir2 = models.CharField(max_length=50, null=False)
    gm1 = models.CharField(max_length=1, null=False)
    gm2 = models.CharField(max_length=50, null=False)
    drink1 = models.IntegerField(null=False)
    drink2 = models.IntegerField(null=False)
    drink3 = models.IntegerField(null=False)
    drink4 = models.IntegerField(null=False)
    lung1 = models.IntegerField(null=False)
    lung2 = models.CharField(max_length=50, null=False)
    lung3 = models.IntegerField(null=False)
    lung4 = models.IntegerField(null=False)
    lung5 = models.IntegerField(null=False)
    lung6 = models.IntegerField(null=False)
    lung7 = models.IntegerField(null=False)
    cure1 = models.CharField(max_length=20, null=False)
    cure2 = models.CharField(max_length=1, null=False)
    cure3 = models.CharField(max_length=20, null=False)
    cure4 = models.CharField(max_length=1, null=False)
    cure5 = models.CharField(max_length=1, null=False)
    cure6 = models.IntegerField(null=False)
    cure7 = models.IntegerField(null=False)
    cure8 = models.CharField(max_length=1, null=False)
    cure9 = models.IntegerField(null=False)
    cure10 = models.CharField(max_length=1, null=False)
    cure11 = models.IntegerField(null=False)
    cure12 = models.CharField(max_length=1, null=False)
    cure13 = models.IntegerField(null=False)
    cure14 = models.CharField(max_length=1, null=False)
    cure15 = models.IntegerField(null=False)
    cure16 = models.CharField(max_length=1, null=False)
    cure17 = models.IntegerField(null=False)
    cure18 = models.CharField(max_length=1, null=False)
    cure19 = models.IntegerField(null=False)
    cure20 = models.CharField(max_length=1, null=False)
    cure21 = models.CharField(max_length=200, null=False)
    cure22 = models.IntegerField(null=False)
    cure23 = models.IntegerField(null=False)
    cure24 = models.IntegerField(null=False)
    cure25 = models.IntegerField(null=False)
    cure26 = models.IntegerField(null=False)
    comp1 = models.CharField(max_length=20, null=False)
    comp2 = models.CharField(max_length=20, null=False)
    comp3 = models.CharField(max_length=20, null=False)
    comp4 = models.CharField(max_length=20, null=False)
    comp5 = models.CharField(max_length=20, null=False)
    comp6 = models.CharField(max_length=20, null=False)


# created by CS@buaa, 2017/3/17
# table21


class ESS(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    type = models.IntegerField(null=False)  # 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
    S_id = models.IntegerField(null=False)
    ess4 = models.IntegerField(null=False)
    ess5 = models.IntegerField(null=False)
    ess6 = models.IntegerField(null=False)
    ess7 = models.IntegerField(null=False)
    ess8 = models.IntegerField(null=False)
    score = models.IntegerField(null=False)


# created by CS@buaa, 2017/3/17
# table22


class MBQ(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    type = models.IntegerField(null=False)  # 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
    S_id = models.IntegerField(null=False)
    q4 = models.IntegerField(null=False)
    q5 = models.IntegerField(null=False)
    q6 = models.IntegerField(null=False)
    q7 = models.IntegerField(null=False)
    q8 = models.CharField(max_length=1, null=False)
    q9 = models.IntegerField(null=False)
    q10 = models.CharField(max_length=1, null=False)
    BMI = models.FloatField(null=False)


# created by CS@buaa, 2017/3/17
# table23


class SGRO(models.Model):
    P_id = models.CharField(max_length=10, null=False)
    type = models.IntegerField(null=False)  # 0 OutPatientService   1 Emerg   2 InHospital   3 AccessoryExamination
    S_id = models.IntegerField(null=False)
    H4 = models.IntegerField(null=False)
    H5 = models.IntegerField(null=False)
    H6 = models.IntegerField(null=False)
    H7 = models.IntegerField(null=False)
    H8 = models.CharField(max_length=1, null=False)
    H9 = models.IntegerField(null=False)
    H10 = models.IntegerField(null=False)
    H11_1 = models.CharField(max_length=1, null=False)
    H11_2 = models.CharField(max_length=1, null=False)
    H11_3 = models.CharField(max_length=1, null=False)
    H11_4 = models.CharField(max_length=1, null=False)
    H11_5 = models.CharField(max_length=1, null=False)
    H11_6 = models.CharField(max_length=1, null=False)
    H11_7 = models.CharField(max_length=1, null=False)
    H12_1 = models.CharField(max_length=1, null=False)
    H12_2 = models.CharField(max_length=1, null=False)
    H12_3 = models.CharField(max_length=1, null=False)
    H12_4 = models.CharField(max_length=1, null=False)
    H12_5 = models.CharField(max_length=1, null=False)
    H12_6 = models.CharField(max_length=1, null=False)
    H13_1 = models.CharField(max_length=1, null=False)
    H13_2 = models.CharField(max_length=1, null=False)
    H13_3 = models.CharField(max_length=1, null=False)
    H13_4 = models.CharField(max_length=1, null=False)
    H13_5 = models.CharField(max_length=1, null=False)
    H13_6 = models.CharField(max_length=1, null=False)
    H13_7 = models.CharField(max_length=1, null=False)
    H13_8 = models.CharField(max_length=1, null=False)
    H14 = models.CharField(max_length=1, null=False)
    H15_1 = models.CharField(max_length=1, null=False)
    H15_2 = models.CharField(max_length=1, null=False)
    H15_3 = models.CharField(max_length=1, null=False)
    H15_4 = models.CharField(max_length=1, null=False)
    H16_1 = models.CharField(max_length=1, null=False)
    H16_2 = models.CharField(max_length=1, null=False)
    H16_3 = models.CharField(max_length=1, null=False)
    H16_4 = models.CharField(max_length=1, null=False)
    H16_5 = models.CharField(max_length=1, null=False)
    H16_6 = models.CharField(max_length=1, null=False)
    H16_7 = models.CharField(max_length=1, null=False)
    H16_8 = models.CharField(max_length=1, null=False)
    H16_9 = models.CharField(max_length=1, null=False)
    H16_10 = models.CharField(max_length=1, null=False)
    H17_1 = models.CharField(max_length=1, null=False)
    H17_2 = models.CharField(max_length=1, null=False)
    H17_3 = models.CharField(max_length=1, null=False)
    H17_4 = models.CharField(max_length=1, null=False)
    H17_5 = models.CharField(max_length=1, null=False)
    H18 = models.CharField(max_length=1, null=False)
    actEff = models.CharField(max_length=100, null=False)


class AccessoryExamination(models.Model):
    type = models.IntegerField(null=False)  # 0 OutPatientService   1 Emerg   2 InHospital
    S_id = models.IntegerField(null=False)
    date = models.DateField()
    AE_type = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    D_id = models.IntegerField()



# created by JK@buaa, 2017/3/17
# table 24


class MedialVisit(models.Model):
    #MV_id = models.CharField(max_length=32, primary_key=True)
    times = models.IntegerField()
    P_id = models.CharField(max_length=7)


# created by JK@buaa, 2017/3/17
# table 25


class HealthyCondition(models.Model):
    #HC_id = models.CharField(max_length=32, primary_key=True)
    condition = models.IntegerField()
    P_id = models.CharField(max_length=7)


# created by JK@buaa, 2017/3/17
# table 26


class DiseaseType(models.Model):
    #DT_id = models.CharField(max_length=32, primary_key=True)
    P_id = models.CharField(max_length=7)
    # TODO: need to finish
    #
    #


# created by JK@buaa, 2017/3/17
# table 27


class WarningInfo(models.Model):
    #WI_id = models.CharField(max_length=32)
    warning = models.CharField(max_length=50)
    P_id = models.CharField(max_length=7)


# created by JK@buaa, 2017/3/17
# table 28


class AppInfo(models.Model):
    #AI_id = models.CharField(max_length=32, primary_key=True)
    date = models.DateField()
    P_id = models.CharField(max_length=7)
    type = models.IntegerField()


# created by CS@buaa, 2017/3/17
# table29


class AppAttachment(models.Model):
    name = models.CharField(max_length=10, null=False)
    P_id = models.CharField(max_length=7, null=False)
    AI_id = models.CharField(max_length=32, null=False)
    dir = models.CharField(max_length=50, null=False)


# created by CS@buaa, 2017/3/17
# table30


class MedicineRegular(models.Model):
    regular = models.CharField(max_length=2, null=False)
    P_id = models.CharField(max_length=10, null=False)
    date = models.DateField(auto_now_add=True)


# created by CS@buaa, 2017/3/17
# table31


class MedicineChange(models.Model):
    change = models.CharField(max_length=2, null=False)
    P_id = models.CharField(max_length=10, null=False)
    date = models.DateField(auto_now_add=True)


# created by CS@buaa, 2017/3/17
# table32


class MedicineRecord(models.Model):
    MC_id = models.IntegerField(null=False)
    medicine = models.CharField(max_length=20, null=False)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False)
    producer = models.CharField(max_length=50, null=False)
