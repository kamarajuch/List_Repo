#Here admin can add fare for passenger
from writeDataInDb import update_age_limit,validate_stops,update_fare,update_trip_discount,update_passenger_discount,add_new_source_destination
#function to modify user age limits
def modify_user_ageLimit():
    while True:
        minChildAge = input("Enter the min age for child : ")
        if (not minChildAge.isnumeric() or minChildAge == 0):
            continue
        minAdultAge=input("Enter Min age for adult : ")
        if (not minChildAge.isnumeric() or int(minAdultAge)<=int(minChildAge)):
            continue
        minSenierCitizenAge=input("Enter min age for senior citizen : ")
        if (not minSenierCitizenAge.isnumeric() or int(minSenierCitizenAge) <= int(minAdultAge)):
            continue
        break
    update_age_limit(int(minChildAge),int(minAdultAge),int(minSenierCitizenAge))

#
def updateFareInFile ():
    global lst,userType
    while True:
        passengerType=input("Enter the passenger type : \n 1 : For Adult \n 2 : For Children")
        if passengerType.isnumeric() and int(passengerType)==1:
            passengerType='Adult'
            break
        elif passengerType.isnumeric() and int(passengerType)==2:
            passengerType='Children'
            break
        continue
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
    while True:
        fare=input('Enter the updated fare : ')
        if (not fare.isnumeric()):
            print ("Please enter the correct updated fare : ")
            continue
        else:
            fare==int(fare)
            break
    update_fare(start,stop,fare,passengerType)
def addTripDiscount():
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
    while True:
        noOfPass=input("Enter Minimum no of passenger required for discount : ")
        if (not noOfPass.isnumeric() or int(noOfPass)<1 ):
            print ("Please pass correct no of passenger")
            continue
        else:
            noOfPass=int(noOfPass)
            break
    while True:
        discount=input("Enter discount in percentage for trip : ")
        if (not discount.isnumeric() or int(discount)<1 or int(discount)>100):
            continue
        else:
            discount=int(discount)
        break
    while True:
        userType=input("Enter discount type for \n 1 : All passenger\n 2 : Adult passenger \n 3 : Children discount : ")
        if (not userType.isnumeric() or int(userType)<1 or int(userType)>3):
            continue
        elif int(userType) is 1:
            userType='all'
        elif int(userType) is 2:
            userType='Adult'
        else:
            userType='child'
        break
    update_trip_discount(start,stop,discount,userType,noOfPass)
def addPassengerDiscount():
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
    while True:
        noOfTravel=input("Enter Minimum no of travel between two station")
        if (not noOfTravel.isnumeric() or int(noOfTravel)<1 ):
            print ("Please enter correct value")
            continue
        else:
            noOfTravel=int(noOfTravel)
            break
    while True:
        discount=input("Enter discount percentage for trip : ")
        if (not discount.isnumeric() or int(discount)<1 or int(discount)>100 ):
            continue
        else:
            discount=int(discount)
        break
    while True:
        userType=input("Enter discount for \n 1 : All passenger\n 2 : Adult passenger \n 3 : Children discount : ")
        if (not userType.isnumeric() or int(userType)<1 or int(userType)>3):
            continue
        elif int(userType) is 1:
            userType='all'
        elif int(userType) is 2:
            userType='Adult'
        else:
            userType='child'
        break
    update_passenger_discount(start,stop,discount,userType,noOfTravel)
def add_source_destination():
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
        if start ==stop:
            print("Source and destination must be different")
            continue
        break
    while True:
        fare=input("Enter The fare for adult")
        if (not fare.isnumeric()):
            print ("Enter the correct input")
            continue
        fare=int(fare)
        break
    add_new_source_destination(start,stop,fare)
def adminUse():
    while True:
        adminInput=input("Please enter input \n 1 : For Change fare between 2 stops \n 2 : add trip discount between two station \n 3 : Passenger Discount\n 4 : Change the age limit for user \n 5 : For add new source and destination")
        if (not adminInput.isnumeric() or int(adminInput)<1 or int(adminInput)>5):
            continue
        else:
            adminInput=int(adminInput)
            break
    if adminInput==1:
        updatedFare=updateFareInFile()
    elif adminInput==2:
        addTripDiscount()
    elif adminInput==3:
        addPassengerDiscount()
    elif adminInput==4:
        modify_user_ageLimit()
    elif adminInput==5:
        add_source_destination()
if __name__=='__main__':
    print ("avaneesh")

