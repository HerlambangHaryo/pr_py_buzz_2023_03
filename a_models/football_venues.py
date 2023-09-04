# Import
import mysql.connector 


def fV_insert_new(venueapi_id, name, city, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "fV_insert_new()", flush=True) 
    # ----------------------------------------------------------  
    # print(space + venueapi_id, flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select  * " 
    query += " from football_venues "    
    query += " where venueapi_id = "+venueapi_id+" "     
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    # print(space + "Venue Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    if(total_rows == 0 and venueapi_id is not None):
        # ------------------------------------------------------  
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `football_venues`( "
        # ------------------------------------------  
        query_commit += " `venueapi_id`, "
        query_commit += " `name`, "
        query_commit += " `city`, " 
        # ------------------------------------------------------  
        query_commit += " `created_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------ 
        query_commit += " " + str(venueapi_id) + ", " 
        query_commit += " " + str(name) + ", " 
        query_commit += " " + str(city) + ", " 

        query_commit += " current_timestamp ) "     
    # ----------------------------------------------------------  
        # print(space + query_commit, flush=True)
        print(space + "football_venues INSERTED", flush=True)
        mycursor.execute(query_commit)
        mydb.commit()   
        mycursor.close()
        mydb.close()  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
