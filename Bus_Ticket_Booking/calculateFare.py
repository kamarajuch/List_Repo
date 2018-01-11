# Here calculate fare according to source and destination
import pymysql
from writeDataInDb import execute_query,create_databsae_connection,update_users_details
def calculate_trip_discount(source,destination,child_fare,adult_fare,passenger_count):
    sql="SELECT TRIP_DISCOUNT,DISCOUNT_TYPE,PASSENGER_COUNT FROM USER_FARE_DETAILS WHERE SOURCE='%d' AND DESTINATION = '%d';" % (source,destination)
    #print(sql)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    content=cursor_obj.fetchone()
    tripDiscount=content[0]
    discountTypes=content[1]
    minUsers=content[2]
    if tripDiscount != "":
        trip_discount=0
        if discountTypes=='child' and passenger_count>=int(minUsers):
            childTripFare=0
            trip_discount=(child_fare*int(tripDiscount))/100
            return trip_discount
        elif discountTypes=='Adult' and passenger_count>=int(minUsers):
            adultTripFare=0
            trip_discount=(adult_fare*int(tripDiscount))/100
            return trip_discount
        elif discountTypes=='all' and passenger_count>=int(minUsers):
            trip_discount=((child_fare+adult_fare)*int(tripDiscount))/100
            return trip_discount
    return trip_discount
def calculate_passenger_discount(source,destination,child_fare,adult_fare,passenger_count):
    sql="SELECT PASSENGER_DISCOUNT,PASSENGER_TYPE,PASSENGER_TRIP_COUNT FROM USER_FARE_DETAILS WHERE SOURCE='%d' AND DESTINATION = '%d';" % (source,destination)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    content=cursor_obj.fetchone()
    passengerDiscount=content[0]
    discountTypes=content[1]
    minUsers=content[2]
    if passengerDiscount != "":
        passenger_discount=0
        if discountTypes=='child' and passenger_count>=int(minUsers)-1:
            childTripFare=0
            passenger_discount=(child_fare*int(passengerDiscount))/100
            return passenger_discount
        elif discountTypes=='Adult' and passenger_count>=int(minUsers)-1:
            adultTripFare=0
            passenger_discount=(adult_fare*int(passengerDiscount))/100
            return passenger_discount
        elif discountTypes=='all' and passenger_count>=int(minUsers)-1:
            passenger_discount=((child_fare+adult_fare)*int(passengerDiscount))/100
            return passenger_discount
    return passenger_discount
def calculateFare(pasngrDetail,userId):
    sql="select * from agelimits;"
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    content=cursor_obj.fetchone()
    print(content)
    childMinAge=int(content[0])
    adultMinAge=int(content[1])
    senierCitzenMinAge=int(content[2])
    print(childMinAge,adultMinAge,senierCitzenMinAge)
    child=0
    adult=0
    fare=0
    childCount=0
    adultCount=0
    otherCount=0
    otherFare=0
    childFare=0
    adultFare=0
    for details in pasngrDetail:
        start=details[0]
        stop=details[1]
        age=details[2]
        if age <adultMinAge and age >=childMinAge:
            sql="SELECT CHILD_FARE FROM USER_FARE_DETAILS WHERE SOURCE = '%d' AND DESTINATION = '%d';" % (int(start),int(stop))
            cursor_obj = create_databsae_connection()
            output=execute_query(sql,cursor_obj)
            result=cursor_obj.fetchone()
            for val in result:
                print(val)
            if val==None:
                sql="SELECT ADULT_FARE FROM USER_FARE_DETAILS WHERE SOURCE = '%d' AND DESTINATION = '%d';" % (int(start),int(stop))
                output=execute_query(sql,cursor_obj)
                result=cursor_obj.fetchone()
                for val in result:
                    val1=int(val)
                childCount=childCount+1
                childFare = childFare + val1/2
            else:
                val1=int(val)
                childCount=childCount+1
                childFare = childFare + val1
        elif age >=senierCitzenMinAge:
            sql="SELECT ADULT_FARE FROM USER_FARE_DETAILS WHERE SOURCE = '%d' AND DESTINATION = '%d';" % (int(start),int(stop))
            output=execute_query(sql,cursor_obj)
            result=cursor_obj.fetchone()
            for val in result:
                val1=int(val)
            otherCount=otherCount+1
            otherFare = otherFare + val1/2
        elif age >= adultMinAge:
            sql="SELECT ADULT_FARE FROM USER_FARE_DETAILS WHERE SOURCE = '%d' AND DESTINATION = '%d';" % (int(start),int(stop))
            output=execute_query(sql,cursor_obj)
            result=cursor_obj.fetchone()
            for val in result:
                val1=int(val)
            adultCountt=adultCount +1
            adultFare = adultFare + val1
        passenger_count=adultCount+childCount+otherCount
    trip_discount=calculate_trip_discount(start,stop,childFare,(adultFare+otherFare),len(pasngrDetail))
    sql="SELECT COUNTERS FROM USER_DETAILS WHERE SOURCE='%d' AND DESTINATION = '%d' AND USER_ID= '%d';" % (int(start),int(stop),int(userId))
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    content=cursor_obj.fetchone()
    for count in content:
        print(count)
    passenger_discount= calculate_passenger_discount(start,stop,childFare,(adultFare+otherFare),count)
    print("Trip discount available : ",trip_discount)
    print("Passenger discount available : ",passenger_discount)
    print("Total Fare : ",(childFare+adultFare+otherFare))
    if passenger_discount>trip_discount:
        print("After discount fare is : ",(childFare+adultFare+otherFare-passenger_discount))
        update_users_details(int(start),int(stop),int(userId))
        sql="UPDATE USER_DETAILS SET COUNTERS=0 WHERE SOURCE='%d' AND DESTINATION='%d' AND USER_ID='%d'" % (int(start),int(stop),int(userId))
        cursor_obj = create_databsae_connection()
        output=execute_query(sql,cursor_obj)
        return (childFare+adultFare+otherFare-passenger_discount)
    else:
        update_users_details(int(start),int(stop),int(userId))
        print("After discount fare is : ",(childFare+adultFare+otherFare-trip_discount))
        return (childFare+adultFare+otherFare-trip_discount)
if __name__=='__main__':
    lsts=[[2,4,16],[2,5,15]]
    #fare =calculateFare(lsts)
    print (lsts)
