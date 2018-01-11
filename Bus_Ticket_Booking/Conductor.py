#Generate ticket for passenger
import pymysql

from writeDataInDb import update_users_details,validate_stops
from calculateFare import calculateFare

# def addUserIdInDb(start,stop,user_Id):
#     # Open database connection
#     start=int(start)
#     stop=int(stop)
#     user_Id=str(user_Id)
#     db = pymysql.connect("localhost","root","root","fare_config")
#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
#     sql = "INSERT INTO user_details(source,destination,user_Id,count) \
#        VALUES ('%d', '%d', '%s', '%d')" \
#        (start, stop, user_Id, 8)
#
#     # execute SQL query using execute() method.
#     #count=select count
#     try:
#         print("starting................")
#         cursor.execute(sql)
#         db.commit()
#         print("end......................")
#     except Exception as err:
#         print(err)
#     # Fetch a single row using fetchone() method.
#     #data = cursor.fetchone()
#     #print "Database version : %s " % data
#
#     # disconnect from server
#     db.close()
# def addUserIdInDb(start,stop,userType):
#     userDetails=readUserDetails()
#     data=userDetails.split('\n')
#     count=0
#     for line in data:
#         if line.strip() is "" or line.startswith('#'):
#             continue
#         line1=line.split(',')
#         if int(line1[0])==int(start) and int(line1[1])==int(stop) and int(line1[2])==int(userType):
#             count+=1
#             val=int(line1[3])+1
#             line1[3]=str(val)
#             s=','
#             newLine=s.join(line1)
#             replaceLineInUserDetailFile(line,newLine)
#             break
#     if count==0:
#         newLine=str(start)+','+str(stop)+','+str(userType)+','+'1'
#         addNewLineInUserDetailFile(newLine)


def conductorUse():
    while True:
        userId=input("Enter the UserId : ")
        if (not userId.isnumeric() or int(userId)<1):
            print ('Please enter correct userid')
            continue
        break
    pasngrDetails=[]
    details =[]
    count=0
    while True:
        noOfPassenger=input("Enter the No of passenger : ")
        if (not noOfPassenger.isnumeric() or int(noOfPassenger)<1):
            print ('Please enter correct no of passenger')
            continue
        else:
            noOfPassenger=int(noOfPassenger)
            break
    while True:
        while True:
            start=input("Enter the Start station : ")
            if (not start.isnumeric() or int(start)<1):
                print ("Enter the correct input")
                continue
            start=int(start)
            break
        while True:
            stop=input('Enter the stop point : ')
            if (not stop.isnumeric() or int(stop)<1):
                print ("Enter the correct input")
                continue
            stop=int(stop)
            break
        result=validate_stops(start,stop)
        if result is 0:
            print("Invalid source and destination, please enter valid value")
            continue
        else:
            if start ==stop:
                print("Source and destination must be different")
                continue
        break
    while noOfPassenger:
        details =[]
        while True:
            age=input('Enter the age for passenger : ')
            if (not age.isnumeric() or int(age)<1 or int(age)>100):
                print ('Please enter correct age')
                continue
            else:
                break
        details.append(int(start))
        details.append(int(stop))
        details.append(int(age))
        pasngrDetails.append(details)
        noOfPassenger-=1
        count+=1
    fare=0
    fare=calculateFare(pasngrDetails,userId,)
    #addUserIdInDb(int(start),int(stop),int(userId))
    print ("After maximum discount fare is : ",fare)
    # if fare>0:
    #     update_users_details(int(start),int(stop),int(userId))
if __name__=='__main__':
    #fare =calculateFare(pasngrDetails)
    print ("User module")
