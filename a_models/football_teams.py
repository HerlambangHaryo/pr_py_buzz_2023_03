# Import
import mysql.connector 
 
def fT_insert_new(teamapi_id, name, logo, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "fT_insert_new()", flush=True) 
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
    query += " from football_teams "    
    query += " where teamapi_id = "+teamapi_id+" "     
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    # print(space + "Venue Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    if(total_rows == 0):
        # ------------------------------------------------------  
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `football_teams`( "
        # ------------------------------------------  
        query_commit += " `teamapi_id`, "
        query_commit += " `name`, "
        query_commit += " `logo`, " 
        # ------------------------------------------------------  
        query_commit += " `created_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------ 
        query_commit += " " + str(teamapi_id) + ", " 
        query_commit += " '" + str(name) + "', " 
        query_commit += " '" + str(logo) + "', " 

        query_commit += " current_timestamp ) "     
    # ----------------------------------------------------------  
        # print(space + query_commit, flush=True)
        print(space + "football_teams INSERTED", flush=True)
        mycursor.execute(query_commit)
        mydb.commit()   
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
