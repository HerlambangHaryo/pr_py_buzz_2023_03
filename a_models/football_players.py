# Import
import mysql.connector 

def fP_update_or_insert(playerapi_id, 
                        player_name, 
                        player_age, 
                        player_number,  
                        player_position,  
                        player_photo,  
                        space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
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
    query += " from football_players "    
    query += " where playerapi_id = "+str(playerapi_id)+" "     
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    # print(space + "Venue Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------    
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `football_players`( "
        # ------------------------------------------  
        query_commit += " `playerapi_id`, "
        query_commit += " `name`, "
        query_commit += " `age`, " 
        query_commit += " `number`, " 
        query_commit += " `position`, " 
        query_commit += " `photo`, " 
        # ------------------------------------------------------  
        query_commit += " `created_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------ 
        query_commit += " " + str(playerapi_id) + ", " 
        query_commit += " '" + str(player_name) + "', " 
        query_commit += " '" + str(player_age) + "', " 
        query_commit += " '" + str(player_number) + "', " 
        query_commit += " '" + str(player_position) + "', " 
        query_commit += " '" + str(player_photo).replace("'", "\\'") + "', "  
        query_commit += " current_timestamp ) "     
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True)
        # ------------------------------------------------------  
        mycursor.execute(query_commit)
        mydb.commit()     
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    elif(total_rows == 1): 
        # ------------------------------------------------------
        query_commit = "UPDATE `football_players` SET "
        # ------------------------------------------------------   
        query_commit += " `name` = '"+str(player_name)+"', "
        query_commit += " `age` = '"+str(player_age)+"', "
        query_commit += " `number` = '"+str(player_number)+"', "
        query_commit += " `position` = '"+str(player_position)+"', "
        query_commit += " `photo` = '"+str(player_photo).replace("'", "\\'")+"', "
        # ------------------------------------------------------
        query_commit += " `updated_at` = now() "
        # ------------------------------------------------------
        query_commit += " where playerapi_id = "+str(playerapi_id)+" "    
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True) 
        # ------------------------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()    
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
