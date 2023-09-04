# Import
import mysql.connector 
 
def fua_update_or_insert(leagueapi_id, 
                        season, 
                        fixtureapi_id, 
                        date, 
                        col_name, 
                        value, 
                        space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fua_update_or_insert()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id  "   
    query += " , season  "
    query += " from football_ultimate_assessments " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' " 
    query += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ---------------------------------------------------------- 
    if(total_rows == 0): 
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `football_ultimate_assessments`( "
        # ------------------------------------------------------  
        query_commit += " `leagueapi_id`, "
        query_commit += " `season`, " 
        query_commit += " `fixtureapi_id`, " 
        query_commit += " `date`, " 
        query_commit += " `"+col_name+"`, " 
        # ------------------------------------------------------ 
        query_commit += " `created_at` "   
        # ------------------------------------------------------ 
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------  
        query_commit += " " + str(leagueapi_id) + ", " 
        query_commit += " " + str(season) + ", "  
        query_commit += " " + str(fixtureapi_id) + ", "  
        query_commit += " '" + str(date) + "', "  
        query_commit += " " + str(value) + ", "  
        query_commit += " current_timestamp "    
        # ------------------------------------------------------ 
        query_commit += " ) "
        # ------------------------------------------------------ 
        mycursor = mydb.cursor()
        mycursor.execute(query_commit)
        mydb.commit()   
        # ------------------------------------------------------ 
        mycursor.close()
        mydb.close()
        # ------------------------------------------------------ 
        print(space + "football_ultimate_assessments INSERTED", flush=True) 
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
    if(total_rows == 1): 
        # ------------------------------------------------------  
        # ------------------------------------------------------ 
        query_commit = "update football_ultimate_assessments set "  
        # ------------------------------------------------------ 
        query_commit += " "+col_name+"  = '"+str(value)+"', "   
        query_commit += " date          = '"+str(date)+"', "   
        query_commit += " updated_at    = current_timestamp " 
        # ------------------------------------------------------ 
        query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "  
        query_commit += " and leagueapi_id = '"+leagueapi_id+"' "
        query_commit += " and season = '"+season+"' "
        # ------------------------------------------------------ 
        mycursor = mydb.cursor()
        mycursor.execute(query_commit)
        mydb.commit()  
        # ------------------------------------------------------ 
        mycursor.close()
        mydb.close()
        # ------------------------------------------------------ 
        print(space + "football_ultimate_assessments UPDATED", flush=True) 
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 