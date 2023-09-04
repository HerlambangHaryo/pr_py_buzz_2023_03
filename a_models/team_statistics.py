# Import
import mysql.connector 
from a_models.api__team_statistics import *   
from a_models.date import *  

def ts_league_season(leagueapi_id, season, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ts_league_season()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = "Select "
    query += " fixtureapi_id "   
    query += " from football_fixtures " 
    query += " where leagueapi_id = '"+leagueapi_id+"' "
    query += " and season = '"+season+"' "   
    query += " and fixture_status like '%Match Finished%' "   
    # query += " and team_statistics_updated_at is null "    
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
        fixtureapi_id    = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " __ " + season  
        word += " __ " + fixtureapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------
        fixture_updated_at  =  get_today_adds(0, space) 
        # ------------------------------------------------------  
        DICT = {
            'fixtureapi_id' :fixtureapi_id,
            'fixture_updated_at' :fixture_updated_at, 
        }
        # ------------------------------------------------------
        a_ts_controll_match_update(DICT, 'fixtureapi_id', space) 
    # ----------------------------------------------------------  
 