import hashlib


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()




def dictPackage(keys,values):
    message={}
    i = 0
    for key in keys:
        message[key] = values[i]
        i=i+1

    return message


def getFields():
    keys=[]
    while True:
        key = raw_input()
        if key == 'q':
            break
        keys.append(key)
    for key in keys:
        print "\'"+key+"\'"+",",

def updataField():
    keys = []
    while True:
        key = raw_input()
        if key == 'q':
            break
        keys.append(key)
    for key in keys:
        print "obj." + key +" = data[" + "\'" + key + "\'" + "]"

def addField():
    keys = []
    while True:
        key = raw_input()
        if key == 'q':
            break
        keys.append(key)
    for key in keys:
        print key + " = data[" + "\'" + key + "\'" + "],",

#getFields()
updataField()
#addField()