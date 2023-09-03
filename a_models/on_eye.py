# Import
import mysql.connector 
from a_models.api_odds import *   
  
def oy_get_fixtures_today(date_0, date_1, date_raw, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "oy_get_fixtures_today()", flush=True)
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
    query += " date " 
    query += " , fixtureapi_id "    
    query += " , (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id) "
 
    query += " from football_odds " 

    query += " where date >= DATE('"+str(date_0)+"') " 
    query += " and date <= DATE('"+str(date_1)+"') " 

    query += " and oneye is not null "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    total_rows = len(result)    
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter             += 1
        # ------------------------------------------------------
        date      = str(x[0]) 
        fixtureapi_id     = str(x[1])    
        bookmaker     = str(x[2])    
        # ------------------------------------------------------ 
        word = space + "[" + str(counter) + "/" + str(total_rows) + "] "  
        word += fixtureapi_id  
        word += " bm:" + bookmaker   
        word += " -> " + date     
        print(word, flush=True)   
        # ------------------------------------------------------  
        

        
        DICT = {
            "fixture" : fixtureapi_id,
            "bookmaker" : bookmaker,  
            # --------------------------------------------------   
            'date_0' : date_0,
            'page' : 1,
            'counter_loop' : 0,
            'date_diff' : 0,
            'date_raw' : date_raw,
        } 
        ao_controll_match_update(DICT, 'eye_', space) 
        # ------------------------------------------------------  