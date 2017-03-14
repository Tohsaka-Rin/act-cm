# -*- coding:UTF-8 -*-




# 用户名/邮箱/手机号 重复性检验
# key : (userName,mail.cellphone,D_id,...)， value是对应字段的值
# 已被注册返回True，否则返回False

def checkExist(key,value):
    #TODO
    return False



# 通过用户名获取用户某个字段的信息
# key 就是字段名， 比如'password' 'D_id'
# 返回获取的值
def getUserInfo(userName,key):
    #TODO
    return 1

# 获取医生的基本信息
# D_id为医生的编号
# 以字典形式返回获取到的基本信息
def getDoctorBasicInfo(D_id):
    #TODO
    return 1


# 获取医生的详细信息
# D_id为医生的编号
# 以字典形式返回获取到的详细信息
def getDoctorDetailedInfo(D_id):
    #TODO
    return 1

#获取医生管理的实验组信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个实验组的信息
def getExpGroups(D_id):
    list = []
    # TODO
    return list

#获取指定实验组中所有患者的基本信息
#返回一个列表，列表中每个元素都是一个字典，存储着一个患者的基本信息
def getExpGroupsPatientsInfo(D_id,G_id):
    list = []
    # TODO
    return list