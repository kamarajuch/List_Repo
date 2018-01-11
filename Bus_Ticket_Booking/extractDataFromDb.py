import re
def readUserDetails():
    with open("userDetails","r") as f:
        content=f.read()
    return content
def checkString(str):
    if len(str.strip().split(',')) > 1:
        str=str.strip('[]')
        str=[int(a) for a in str.split(',')]
    else:
        str=int(str)
    return str
def readFile():
    with open("Db_File","r") as f:
        content=f.read()
        content1 = content.split("\n")
        #print (content1)
        details=[]
        content2=[]
        for val in content1:
            if val.strip() is "" or val.startswith('#'):
                continue
            val=re.split(':',val)
            val =[checkString(lst1) for lst1 in val]
            content2.append(val)
    return content2
def readDiscountFile(start,stop):
    with open("userDiscount","r+") as f:
        content=f.read()
        content1=content.split('\n')
        line=""
        for val  in content1:
            if val.strip() is "" or val.startswith('#'):
                continue
            val1=val.split(';')
            if int(val1[0])==int(start) and int(val1[1])==int(stop):
                return val
        return ""
if __name__=='__main__':
    output =readFile()
    print (output)
