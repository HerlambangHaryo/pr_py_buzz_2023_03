# Import
import mysql.connector 
from a_models.api_fixtures_new import *   
from a_models.api_odds_new import *  

def po_league_group(day1, day2, today, space): 
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "po_league_group()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id " 
    query += " , season  " 
    query += " , count(*)  "
    query += " from football_fixtures " 
    query += " where date >= Date('"+day1+"') "
    query += " and date <= Date('"+day2+"') " 
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Not Started', 'Not Started Goto' ) "  
    query += " group by leagueapi_id, season "
    query += " order by date, leagueapi_id asc  "  
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
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        countrows      = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        print(word, flush=True)    
        # ------------------------------------------------------
        space2 = "              "
        # ------------------------------------------------------
        word = space2 + " countrows: " + countrows 
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space2 + " day1: " + day1 
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space2 + " day2: " + day2 
        print(word, flush=True)      
        # ------------------------------------------------------ 
        ROUTES = 'leagueapi_id'
        word = space2 + " ROUTES: " + ROUTES  
        print(word, flush=True)     
        # ------------------------------------------------------
        DICT = {
            'leagueapi_id' :leagueapi_id,
            'season' :season,
            'day1' :day1,
            'day2' :day2,
            'today' :today,
        }
        # ------------------------------------------------------ 
        # afN_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    # ----------------------------------------------------------