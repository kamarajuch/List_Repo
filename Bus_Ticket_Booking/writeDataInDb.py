#Write content in file
import pymysql
def create_databsae_connection():
    global db,cursor_obj
    db = pymysql.connect("localhost","root","root","fare_config")
    # prepare a cursor object using cursor() method
    cursor_obj = db.cursor()
    return cursor_obj
def execute_query(sql,cursor_obj):
    val=0
    try:
        val=cursor_obj.execute(sql)
        db.commit()
    except Exception as err :
        db.rollback()
        print(err)
    return val

def update_users_details(start,stop,user_id):
    sql="SELECT COUNTERS FROM USER_DETAILS WHERE SOURCE='%d' AND DESTINATION='%d' AND USER_ID='%d'" % (start,stop,user_id)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    results = cursor_obj.fetchone()
    #print(output)
    if output is 0:
        sql = "INSERT INTO USER_DETAILS(SOURCE,DESTINATION,USER_ID,COUNTERS) \
                 VALUES ('%d', '%d', '%s', '%d')" % \
                 (start, stop, user_id, 1)
    else:
        for val1 in results:
            counts=val1
        val=int(counts) +1
        sql="UPDATE USER_DETAILS SET COUNTERS= '%d' WHERE SOURCE='%d' AND DESTINATION='%d' AND USER_ID='%d'" % (val,start,stop,user_id)
        #print(sql)
    results=execute_query(sql,cursor_obj)
    db.close()
def update_age_limit(child_min_age,adult_min_age,senier_citizen_min_age):
    sql="DELETE FROM AGElIMITS"
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    sql="INSERT INTO AGELIMITS VALUES ('%d',  '%d', '%d');" % (child_min_age,adult_min_age,senier_citizen_min_age)
    print(sql)
    output=execute_query(sql,cursor_obj)
    db.close()
def update_fare(source,destination,fare,passenger_type):
    sql="SELECT * FROM USER_FARE_DETAILS WHERE SOURCE ='%d' and DESTINATION='%d'" % (source,destination)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    #print(output)
    if output is 0:
        print("Source and destination not available in database")
    else:
        if passenger_type=='Adult':
            sql="UPDATE USER_FARE_DETAILS SET ADULT_FARE= '%d' WHERE SOURCE='%d' AND DESTINATION='%d'" % (int(fare),source,destination)
            #print(sql)
        else:
            sql="UPDATE USER_FARE_DETAILS SET CHILD_FARE= '%d' WHERE SOURCE='%d' AND DESTINATION='%d'" % (int(fare),source,destination)
    results=execute_query(sql,cursor_obj)
    db.close()
def validate_stops(source,destination):
    sql="SELECT * FROM USER_FARE_DETAILS WHERE SOURCE ='%d' and DESTINATION='%d'" % (source,destination)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    return output
def update_trip_discount(source,destination,discount,userType,noOfPass):
    sql="UPDATE USER_FARE_DETAILS SET TRIP_DISCOUNT= '%d',DISCOUNT_TYPE='%s',PASSENGER_COUNT='%d' WHERE SOURCE='%d' AND DESTINATION='%d'" % (int(discount),userType,noOfPass,source,destination)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    db.close()
def update_passenger_discount(source,destination,discount,userType,no_of_trvel):
    sql="UPDATE USER_FARE_DETAILS SET PASSENGER_DISCOUNT= '%d',PASSENGER_TYPE='%s',PASSENGER_TRIP_COUNT='%d' WHERE SOURCE='%d' AND DESTINATION='%d'" % (int(discount),userType,no_of_trvel,source,destination)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    db.close()
def add_new_source_destination(source,destination,fare):
    sql="INSERT INTO USER_FARE_DETAILS (SOURCE,DESTINATION,ADULT_FARE) VALUES ('%d','%d','%d');" % (source,destination,fare)
    cursor_obj = create_databsae_connection()
    output=execute_query(sql,cursor_obj)
    db.close()
