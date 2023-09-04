# Import
import mysql.connector 


def fC_insert_new(coacheapi_id, name, image, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "fC_insert_new()", flush=True) 
    # ----------------------------------------------------------   
    print(space + "coacheapi_id : " + str(coacheapi_id), flush=True) 
    print(space + "name : " + str(name), flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(coacheapi_id != 'None'):
        query = " Select  * " 
        query += " from football_coaches "    
        query += " where coachapi_id = "+str(coacheapi_id)+" "     
        # ----------------------------------------------------------    
        # print(space + query, flush=True)
        # ----------------------------------------------------------    
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result =  mycursor.fetchall()
        # ----------------------------------------------------------    
        total_rows = len(result)
        # ----------------------------------------------------------     
        # print(space + "coaches Row(s) : " + str(total_rows), flush=True) 
        # ----------------------------------------------------------  
        if(total_rows == 0 and coacheapi_id is not None):
            # ------------------------------------------------------  
            # ------------------------------------------------------ 
            query_commit = "INSERT INTO `football_coaches`( "
            # ------------------------------------------  
            query_commit += " `coachapi_id`, "
            query_commit += " `name`, "
            query_commit += " `image`, " 
            # ------------------------------------------------------  
            query_commit += " `created_at` "   
            # ------------------------------------------------------  
            query_commit += " ) VALUES ( "
            # ------------------------------------------------------ 
            query_commit += " " + str(coacheapi_id) + ", " 
            query_commit += " '" + str(name.replace("'", "\\'")) + "', " 
            query_commit += " '" + str(image) + "', " 

            query_commit += " current_timestamp ) "     
        # ----------------------------------------------------------  
            print(space + query_commit, flush=True)
            print(space + "football_coaches INSERTED", flush=True)
            mycursor.execute(query_commit)
            mydb.commit()   
            mycursor.close()
            mydb.close()  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
