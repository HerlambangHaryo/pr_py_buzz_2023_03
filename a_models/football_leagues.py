# Import
import mysql.connector 
from a_models.api_leagues import *   

def fl_check_league(leagueapi_id, col_name, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fl_check_league()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------
    check = " select "+col_name+" "   
    check += " from football_leagues "   
    check += " where leagueapi_id = '" + str(leagueapi_id) + "'"    
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(check)
    # result_check =  mycursor.fetchall()
    result_check = mycursor.fetchone()
    total_rows = result_check[0]
    # ---------------------------------------------------------- 
    # print(space + "ff_check_fixture: " +str(total_rows), flush=True)
    # ---------------------------------------------------------- 
    print(space + col_name + ": " +str(total_rows), flush=True)
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    return total_rows
    # ----------------------------------------------------------
 
def fl_all_leagues(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fl_all_leagues()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " name  " 
    query += " from countries  "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        name   = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name  
        print(word, flush=True)    
        # ------------------------------------------------------ 
        DICT = {
            'country' :name, 
        }
        # ------------------------------------------------------  
        al_controll_match_update(DICT, "Null", space) 
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        
        # ------------------------------------------------------     
        # ------------------------------------------------------  
    # ----------------------------------------------------------    
    # ----------------------------------------------------------    
    # ----------------------------------------------------------  

    