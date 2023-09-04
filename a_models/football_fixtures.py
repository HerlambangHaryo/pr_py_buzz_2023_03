# Import
import mysql.connector 
from a_models.api_fixtures_new import * 
import pandas as pd  
from a_models.api_fixtures_players import * 
from a_models.api_odds_new import *   
from a_models.football_leagues import *   
 

def ff_predates_league_today(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_predates_league_today()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    
    # // select `leagueapi_id`, `season`, count(*) as counter 
    # // from `football_fixtures` 
    # // where `date` >= 2023-08-29 04:47:27 
    # // and `date` <= 2023-08-30 04:47:27 
    # // and `fixture_status` in (Not Started, Not Started Goto, Not Started One) 
    # // and `deleted_at` is null 
    # // group by `leagueapi_id`, `season` 
    # // order by `datex` asc
    
    query = "Select "
    query += " leagueapi_id " 
    query += " , season  "   
    query += " from football_fixtures " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') " 
    query += " and deleted_at is null "
    query += " and fixture_status like 'Not Started'  "  
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
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        print(word, flush=True)    
        # ------------------------------------------------------
        bookmaker       = fl_check_league(leagueapi_id, "bookmakersapi_id", space)
        date_0          = get_today_adds(0, space).strftime("%Y-%m-%d") 
        date_raw        = get_today_adds(0, space) 
        # ------------------------------------------------------
        DICT = {
            'date' : date_0,
            'date_raw' : date_raw,
            'league' : leagueapi_id,
            'season' : season,
            'bookmaker' : bookmaker,
            'page' : 1,
            'counter_loop' : 0,
            'date_diff' : 0, 
            'max_page' : 0, 
        } 
        # ------------------------------------------------------
        PREP_ = "preleague_"
        # ------------------------------------------------------ 
        aoN_controll_match_update(DICT, PREP_, space) 
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   


def ff_not_started(day1, day2, today, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_not_started()", flush=True)
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
    query += " , (select bookmakersapi_id FROM football_leagues WHERE leagueapi_id = football_fixtures.leagueapi_id ) as  bookmakersapi_id "    

    query += " from football_fixtures " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') " 
    query += " and deleted_at is null "
    query += " and fixture_status like 'Not Started'  "  
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
        bookmakersapi_id  = str(x[4])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " -> " + fixtureapi_id 
        word += " __ " + bookmakersapi_id 
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
        word = space2 + " bookmakersapi_id: " + bookmakersapi_id  
        print(word, flush=True)     
        # ------------------------------------------------------  
        ROUTES = 'fixtureapi_id'
        word = space2 + " ROUTES: " + ROUTES  
        print(word, flush=True)      
        # ------------------------------------------------------
        # DICT = {
        #     'fixtureapi_id' :fixtureapi_id, 
        #     'fixture_updated_at' :today, 
        # }
        # # ------------------------------------------------------ 
        # afN_controll_match_update(DICT, ROUTES, space)
        # # ------------------------------------------------------ 
        # print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
 
def ff_controll_predates_time_to_be_defined(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_controll_predates_time_to_be_defined()", flush=True)
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
    query += " DATE(date) as date_FX "   
    query += " , count(*) as counter  "  
    query += " , fixture_status  "  
    query += " , leagueapi_id  "  
    query += " , season  "  
    query += " , fixture_updated_at  "  
    query += " from football_fixtures " 
    query += " where DATE(date) >= '"+str(day1)+"' " 
    query += " and DATE(date) <= '"+str(day2)+"' " 
    query += " and DATE(fixture_updated_at) != '"+str(day1)+"' " 
    query += " and fixture_status = 'Time to be defined'  " 
    query += " group by  fixture_status, leagueapi_id, season, fixture_updated_at " 
    query += " order by fixture_status, DATE(date) desc "   
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description]) 
    # ---------------------------------------------------------- 
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 120)
    # ---------------------------------------------------------- 
    total_rows = len(rows)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    print("", flush=True)
    print(df, flush=True)
    print("", flush=True)
    # ----------------------------------------------------------  
    continuex    = input(space + "Do you want to continue? ") 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------  
    if(continuex == "yes"): 
        # ------------------------------------------------------        
        for x in rows:    
            # --------------------------------------------------
            counter        += 1
            # --------------------------------------------------
            leagueapi_id   = str(x[3])  
            season         = str(x[4])  
            countrows      = str(x[1])  
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += " #" + leagueapi_id 
            word += " - " + season 
            print(word, flush=True)    
            # --------------------------------------------------
            space2 = "              " 
            # --------------------------------------------------
            word = space2 + " day1: " + day1 
            print(word, flush=True)    
            # --------------------------------------------------
            word = space2 + " day2: " + day2 
            print(word, flush=True)      
            # --------------------------------------------------
            ROUTES = 'timetobedefined'
            word = space2 + " ROUTES: " + ROUTES  
            print(word, flush=True)     
            # --------------------------------------------------
            DICT = {
                'leagueapi_id' :leagueapi_id,
                'season' :season,
                'from' :day1,
                'to' :day2, 
            }
            # --------------------------------------------------
            afN_controll_match_update(DICT, ROUTES, space)
            # --------------------------------------------------
            print("  ___________________________________________________", flush=True)
            # --------------------------------------------------
        # ------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def ff_controll_predates(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_controll_predates()", flush=True)
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
    query += " DATE(date) as date_FX "   
    query += " , leagueapi_id  "  
    query += " , season  "  
    query += " , count(*) as counter  "  
    query += " , fixture_status  "  
    query += " , fixture_updated_at  "   
    query += " from football_fixtures " 
    query += " where DATE(date) >= '"+str(day1)+"' " 
    query += " and DATE(date) <= '"+str(day2)+"' " 
    query += " group by  fixture_status, leagueapi_id, season " 
    query += " order by leagueapi_id, fixture_status, DATE(date) desc "   
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description]) 
    # ---------------------------------------------------------- 
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 120)
    # ---------------------------------------------------------- 
    total_rows = len(rows)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    print("", flush=True)
    print(df, flush=True)
    print("", flush=True)
    # ---------------------------------------------------------- 


def ff_check_fixture(leagueapi_id, season, fixtureapi_id, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_check_fixture()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------
    check = " select count(*) "   
    check += " from football_fixtures "   
    check += " where leagueapi_id = '" + str(leagueapi_id) + "'"   
    check += " and season = '" + str(season) + "'"   
    check += " and fixtureapi_id = '" + str(fixtureapi_id) + "'"   
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(check)
    # result_check =  mycursor.fetchall()
    result_check = mycursor.fetchone()
    total_rows = result_check[0]
    # ---------------------------------------------------------- 
    print(space + "ff_check_fixture: " +str(total_rows), flush=True)
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    return total_rows
    # ----------------------------------------------------------
    # ----------------------------------------------------------

def ff_update_or_insert_by_world(season, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_update_or_insert_by_world()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " country_name  "  
    query += " from football_leagues " 
    query += " group by country_name order by country_name asc" 
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
        country_name   = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + country_name  
        print(word, flush=True)    
        # ------------------------------------------------------
        ff_update_or_insert_by_country(country_name, season, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    
def ff_update_or_insert_by_country(country_name, season, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_update_or_insert_by_country()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id "  
    query += " from football_leagues " 
    query += " where country_name =  '"+country_name+"' " 
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
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------
        # ------------------------------------------------------
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------
        query = "Select "
        query += " count(*) "  
        query += " from football_fixtures " 
        query += " where leagueapi_id =  '"+str(leagueapi_id)+"' " 
        query += " and season =  '"+str(season)+"' " 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        mycursor = mydb.cursor()
        mycursor.execute(query)
        # result_check =  mycursor.fetchall()
        result_check = mycursor.fetchone()
        total_rows = result_check[0]
        # ------------------------------------------------------ 
        print(space + "ff_update_or_insert_by_country: " +str(total_rows), flush=True)
        # ------------------------------------------------------ 
        mycursor.close()
        mydb.close()
        # ------------------------------------------------------ 
        if(total_rows == 0): 
            DICT = {
                'leagueapi_id' :leagueapi_id,
                'season' :season, 
            }
            # ------------------------------------------------------ 
            afN_controll_match_update(DICT, 'league_season', space)
            # ------------------------------------------------------ 
            print("  ___________________________________________________", flush=True)
        # ------------------------------------------------------ 
    # ----------------------------------------------------------   

    
def ff_check_api_fixtures_players(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_check_api_fixtures_players()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " fixtureapi_id  "  
    query += " from football_fixtures " 
    query += " where api_fixtures_players_updated_at is null " 
    query += " and leagueapi_id = 39 " 
    query += " and season = 2023 " 
    query += " and fixture_status IN ('Match Finished' ,'Match Finished Ended') " 
    # ----------------------------------------------------------   
    print(space + query, flush=True)
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
        fixtureapi_id   = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fixtureapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------
        DICT = {
            'fixtureapi_id' :fixtureapi_id, 
        }
        # ------------------------------------------------------ 
        afP_controll_match_update(DICT, 'league_season', space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------  