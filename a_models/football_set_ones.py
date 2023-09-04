# Import
import mysql.connector 
from a_models.api_odds_new import *   

def fso_get_fixture_one(space): 
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fso_get_fixture_one()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = "Select "
    query += " leagueapi_id "
    query += " , season "
    query += " , fixtureapi_id "
    query += " , (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_set_ones.leagueapi_id)  "

    query += " from football_set_ones "    

    query += " where status = 1 "  
    query += " order by id asc "   
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall() 
    # ----------------------------------------------------------    
    space += "__"
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------    
    count_rows = 0  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    for x in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------  
        leagueapi_id        = str(x[0])
        season              = str(x[1]) 
        fixtureapi_id       = str(x[2]) 
        bookmakersapi_id    = str(x[3]) 
        # ------------------------------------------------------  
        words = space + str(count_rows) + ". "
        words += str(leagueapi_id) + " // "
        words += str(season) + " // "
        words += str(fixtureapi_id) + " // "
        words += str(bookmakersapi_id)  
        # ------------------------------------------------------   
        print(space + words, flush=True) 
        # ------------------------------------------------------  
        DICT = {
            "fixture" : fixtureapi_id,
            "bookmaker" : bookmakersapi_id, 
            "max_page" : 0, 
            "page" : 1, 
        } 
        aoN_controll_match_update(DICT, 'one_', space) 
        # ------------------------------------------------------  
    # ----------------------------------------------------------  