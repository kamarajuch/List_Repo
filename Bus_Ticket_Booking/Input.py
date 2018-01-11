#Take input from user
from Admin import adminUse
from Conductor import conductorUse
while True:
    while True:
        userType=input("Please enter the user type Admin/User : ")
        if userType=='admin' or userType=='Admin' :
            userType='Admin'
            break
        elif userType=='User' or userType=='user':
            userType='User'
            break
    if userType=='Admin':
        adminUse()
    else:
        conductorUse()
    flag=0
    while True:
        val=input(" 1 : For continue press 1\n 2 : For Exit")
        if val.isnumeric() and int(val) is 1:
            flag=0
            break
        elif val.isnumeric() and int(val) is 2:
            flag=1
            break
        else:
            print("Please enter correct input")
    if flag==1:
        break
    else:
        continue
