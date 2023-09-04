# Import
import mysql.connector 
from a_models.api_fixtures_new import *   
from a_models.api_odds_new import *   

def mu_fixtures(day1, day2, today, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_league_group()", flush=True)
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
    query += " , fixtureapi_id  " 
    query += " from football_fixtures " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') "
    query += " and fixture_updated_at != Date('"+today+"') "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "  
    query += " group by leagueapi_id, season "
    query += " HAVING COUNT(*) = 1  "  
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
        fixtureapi_id  = str(x[3])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " -> " + fixtureapi_id 
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
        word = space2 + " fixtureapi_id: " + fixtureapi_id  
        print(word, flush=True)     
        # ------------------------------------------------------  
        ROUTES = 'fixtureapi_id'
        word = space2 + " ROUTES: " + ROUTES  
        print(word, flush=True)      
        # ------------------------------------------------------
        DICT = {
            'fixtureapi_id' :fixtureapi_id, 
            'fixture_updated_at' :today, 
        }
        # ------------------------------------------------------ 
        afN_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   

def mu_league_group(day1, day2, today, space): 
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_league_group()", flush=True)
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
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') "
    query += " and fixture_updated_at != Date('"+today+"') "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "  
    query += " group by leagueapi_id, season "
    query += " HAVING COUNT(*) > 1  "  
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
        afN_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   

def mu_fixtures_odds(day1, day2, today, space): 
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_fixtures_odds()", flush=True)
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
    query += " , fixtureapi_id  " 
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_fixtures.leagueapi_id) "
    query += " , fixture_status  "
    query += " , DATE(date) "
    query += " from football_fixtures " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') " 
    query += " and deleted_at is null "
    query += " and fixture_status like 'Match Finished' "
    query += " group by leagueapi_id, season "
    query += " HAVING COUNT(*) = 1  "  
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
        fixtureapi_id  = str(x[3])  
        # ------------------------------------------------------
        bookmakersapi_id    = str(x[4])  
        fixture_status      = str(x[5])  
        date                = str(x[6])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " -> " + fixtureapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        space2 = "              "
        # ------------------------------------------------------
        word = space2 + " bookmakersapi_id: " + bookmakersapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space2 + " fixture_status: " + fixture_status 
        print(word, flush=True)   
        # ------------------------------------------------------
        word = space2 + " date: " + date 
        print(word, flush=True)   
        # ------------------------------------------------------ 
        DICT = {
            "date" : date,
            "bookmaker" : bookmakersapi_id,
            "season" : season,
            "league" : leagueapi_id,
            "page" : 1,
            "max_page" : 0,
        } 
        # ------------------------------------------------------ 
        aoN_controll_match_update(DICT, 'end_', space) 
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def mu_league_group_odds(day1, day2, today, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_league_group_odds()", flush=True)
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
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_fixtures.leagueapi_id) "
    query += " , fixture_status  "
    query += " , DATE(date) "
    query += " from football_fixtures " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') "
    query += " and deleted_at is null "
    # query += " and leagueapi_id = 848"
    query += " and fixture_status like 'Match Finished' "
    query += " group by leagueapi_id, season, date(date) "
    query += " HAVING COUNT(*) > 1  "  
    query += " order by  leagueapi_id, date asc  "   
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
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        countrows      = str(x[2])  
        # ------------------------------------------------------
        bookmakersapi_id    = str(x[3])  
        fixture_status      = str(x[4])  
        date                = str(x[5])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        print(word, flush=True)    
        # ------------------------------------------------------
        mu_league_group_odds_but_detailed(date, leagueapi_id, season, space)
        # ------------------------------------------------------
        space2 = "              "
        # ------------------------------------------------------
        word = space2 + " countrows: " + countrows 
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space2 + " bookmakersapi_id: " + bookmakersapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space2 + " fixture_status: " + fixture_status 
        print(word, flush=True)      
        # ------------------------------------------------------
        word = space2 + " date: " + date 
        print(word, flush=True)       
        # ------------------------------------------------------ 
        DICT = {
            "date" : date,
            "bookmaker" : bookmakersapi_id,
            "season" : season,
            "league" : leagueapi_id,
            "page" : 1,
            'max_page'  : 0
        } 
        # ------------------------------------------------------ 
        aoN_controll_match_update(DICT, 'end_', space) 
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    print(space, flush=True) 
    print(space, flush=True) 
    print(space, flush=True) 
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   

    
def mu_league_group_odds_but_detailed(date, leagueapi_id, season, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_league_group_odds_but_detailed()", flush=True)
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
    query += " , fixture_status  "
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_fixtures.leagueapi_id) "
    query += " , fixture_status  "
    query += " , DATE(date) "
    query += " , fixtureapi_id "
    query += " from football_fixtures " 
    query += " where Date(date) = '"+date+"' " 
    query += " and leagueapi_id = '"+leagueapi_id+"' "
    query += " and season = '"+season+"' "
    query += " and deleted_at is null "
    query += " and fixture_status like 'Match Finished' "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "detailed Row(s) : " + str(total_rows), flush=True) 
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
        fixture_status      = str(x[2])  
        # ------------------------------------------------------
        bookmakersapi_id    = str(x[3])  
        fixture_status      = str(x[4])  
        date                = str(x[5])  
        # ------------------------------------------------------
        fixtureapi_id       = str(x[6])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " __ " + date 
        word += " __ " + fixtureapi_id 
        word += " __ " + fixture_status  
        print(word, flush=True)    
        # ------------------------------------------------------
    print(space, flush=True) 
    # ----------------------------------------------------------  
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
 
def mu_xpattern(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "mu_xpattern()", flush=True)
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
    query += " , fixtureapi_id "
    query += " from football_odds " 
    query += " where end_response = 1 "  
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "  
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
        leagueapi_id    = str(x[0])  
        season          = str(x[1])    
        fixtureapi_id   = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        word += " __ " + fixtureapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 