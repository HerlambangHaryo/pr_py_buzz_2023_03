# Import
import mysql.connector 
from a_models.api_standings import *  

def s_league_group(day1, day2, space): 
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "s_league_group()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " FF.leagueapi_id " 
    query += " , FF.season  "  
    query += " , FL.type "
    query += " from football_fixtures as FF " 
    query += " inner join football_leagues as FL " 
    query += " on FF.leagueapi_id = FL.leagueapi_id " 
    query += " where FF.date <= Date('"+day2+"') "
    query += " and FF.date >= Date('"+day1+"') " 
    query += " and FF.deleted_at is null " 
    query += " and FL.type = 'League' " 
    query += " and date(FL.league_standing_updated_at) = Date('"+day1+"') " 
    query += " group by FF.leagueapi_id, FF.season " 
    query += " order by FF.date, FF.leagueapi_id asc  "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        leagueapi_id   = str(x[0])  
        season         = str(x[1])   
        # ------------------------------------------------------
        typex          = str(x[2])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " __ " + typex 
        print(word, flush=True)      
        # ------------------------------------------------------
        DICT = {
            'leagueapi_id' :leagueapi_id,
            'season' :season, 
        }
        # ------------------------------------------------------  
        as_controll_match_update(DICT, "Null", space) 
        # ------------------------------------------------------  
        # ------------------------------------------------------  
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   