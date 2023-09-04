# Import
import mysql.connector 
from a_models.api_odds_new import *  

def fso_setup_one(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fso_setup_one()", flush=True)
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
    query += " , fixtureapi_id  "  
    query += " , (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_set_ones.leagueapi_id) "
    query += " from football_set_ones " 
    query += " where status = 0 " 
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
        leagueapi_id        = str(x[0])   
        season              = str(x[1])   
        fixtureapi_id       = str(x[2])   
        bookmakersapi_id    = str(x[3])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " - " + season  
        word += " __ " + fixtureapi_id  
        word += " __ " + bookmakersapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------ 
        DICT = {
            "fixture" : fixtureapi_id,
            "bookmaker" : bookmakersapi_id, 
        } 
        # ------------------------------------------------------
        aoN_controll_match_update(DICT, 'one_', space) 
        # ------------------------------------------------------