# Import
import mysql.connector 
from a_models.api_fixtures import *   
from a_models.api_odds import *   
from a_models.xpattern import *   
from a_models.leagues import *   
from a_models.football_statistics import *   
from a_models.statistic_assessment_group import *   
from a_models.xpattern_new import *   

from a_models.api_fixtures_players import *   

from a_models.football_fixtures import *   


import pandas as pd

def fO_pattern_match_finished(date_0, col, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_pattern_match_finished()", flush=True) 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = " Select "
    query += " leagueapi_id "  
    query += " from football_odds " 
    query += " where date <= Date('"+date_0+"') "  
    query += " and "+col+" is null "
    query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') "
    query += " and deleted_at is null " 

    
    query += " and pre_ah_pattern is not null " 
    query += " and pre_gou_pattern is not null " 
    
    query += " and end_ah_pattern is not null " 
    query += " and end_gou_pattern is not null " 

    query += " and pre_ah_pattern != 'H' " 
    query += " and pre_gou_pattern != 'G' " 

    query += " and end_ah_pattern != 'H' " 
    query += " and end_gou_pattern != 'G' " 
    
    query += " and pre_response = 3 " 
    query += " and end_response = 3 " 

    
    query += " group by leagueapi_id " 
    # query += " limit 1 " 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------

        if(col == "pattern_from"):
            ff_get_fixtures_group_by_pre_end_patternlists(leagueapi_id, space) 
        elif(col == "pattern_only"):
            ff_get_fixtures_group_by_only_end_patternlists(leagueapi_id, space)
    # ----------------------------------------------------------    
    # ---------------------------------------------------------- 



def fO_on_eye(leagueapi_id, date_0, date_1, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_all_fixture()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = " UPDATE `football_odds` SET  "
    query += " `oneye` = 1 " 
    query += " where date <= Date('"+date_1+"') "
    query += " and date >= Date('"+date_0+"') "
    query += " and leagueapi_id =  '"+str(leagueapi_id)+"' " 
    query += " and deleted_at is null " 

    mycursor.execute(query)
    mydb.commit()   
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = " Select "
    query += " leagueapi_id " 
    query += " , season  "
    query += " , fixtureapi_id  "
    query += " from football_odds " 
    query += " where date <= Date('"+date_1+"') "
    query += " and date >= Date('"+date_0+"') "
    query += " and leagueapi_id =  '"+str(leagueapi_id)+"' " 
    query += " and oneye = 1 "
    query += " and deleted_at is null " 
    # query += " limit 1 " 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        fixtureapi_id  = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season
        word += " - " + fixtureapi_id
        print(word, flush=True)    
        # ------------------------------------------------------
    # ----------------------------------------------------------    
    # ---------------------------------------------------------- 

def fO_get_all_fixture(leagueapi_id, season, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_all_fixture()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    not_in_query = "Select fixtureapi_id "
    # ----------------------------------------------------------  
    query = " Select "
    query += " leagueapi_id " 
    query += " , season  "
    query += " , fixtureapi_id  "
    query += " from football_odds " 
    query += " where leagueapi_id =  '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "
    query += " and fixtureapi_id not in '"+str(season)+"' "
    query += " and deleted_at is null " 
    # query += " limit 1 " 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        fixtureapi_id  = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season
        word += " - " + fixtureapi_id
        print(word, flush=True)    
        # ------------------------------------------------------
        DICT = {
            'leagueapi_id' :leagueapi_id, 
            'season' :season, 
            'fixtureapi_id' :fixtureapi_id, 
        }
        # ------------------------------------------------------ 
        ROUTES = ''
        aFp_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   

def fO_get_league_group_fixture_status_not_in_match_finished(day1, day2, today, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_league_group_fixture_status_not_in_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select "
    query += " leagueapi_id " 
    query += " , season  "
    query += " from football_odds " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) " 
    # query += " and (updated_at is null or DATE(updated_at) != '"+str(today)+"') " 
    # query += " and DATE(updated_at) != '"+str(today)+"'" 
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
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season
        word += " - " + season
        print(word, flush=True)    
        # ------------------------------------------------------
        DICT = {
            'leagueapi_id' :leagueapi_id,
            'season' :season,
            'day1' :day1,
            'day2' :day2,
        }
        # ------------------------------------------------------ 
        ROUTES = 'leagueapi_id'
        af_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   

def fO_get_league_group_fixture_status_not_in_match_finished_DETAILED(day1, day2, today, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_league_group_fixture_status_not_in_match_finished_DETAILED()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select  "
    query += " leagueapi_id "
    query += " , season  "
    query += " , fixture_status " 
    query += " , DATE(updated_at) " 
    query += " , date " 
    # query += " , league_name "
    # query += " , league_country "
    # query += " , teams_home " 
    # query += " , teams_away " 
    query += " from football_odds " 
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "
    query += " and deleted_at is null "
    # query += " and (updated_at is null or DATE(updated_at) != '"+str(today)+"') " 
    query += " and DATE(updated_at) != '"+str(today)+"'" 
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
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id    = str(x[0]) 
        season          = str(x[1])  
        fixture_status  = str(x[2])  

        updated_at      = str(x[3])  
        date            = str(x[4])  

        # league_name    = str(x[1]) 
        # league_country = str(x[2])  

        # teams_home      = str(x[4]) 
        # teams_away      = str(x[5])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] "
        word += " #" + leagueapi_id
        word += " - " + season 
        word += " / " + fixture_status
        word += " => Updated at :" + updated_at
        word += " => Date : " + date
        print(word, flush=True)    
        # ------------------------------------------------------
    # ----------------------------------------------------------

def fO_get_group_league_status_match_finished(day1, day2, today, space):
    # ----------------------------------------------------------   
    # 2a. Enddates 7-6 Days
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_group_league_status_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    #
    # always double check to ff_get_fixture_status_match_finished
    # same query
    # 
    query = "Select "
    query += " DATE(date) "
    query += " , leagueapi_id"
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_odds.leagueapi_id) "
    query += " , season"
    query += " , DATE(end_odd_updated_at) "
    query += " , fixture_status  "
    query += " , count(*) as count_rows  "

    query += " from football_odds "    

    query += " where  date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    query += " and fixture_status like 'Match Finished' "
    query += " and deleted_at is null " 
    # query += " and DATE(end_odd_updated_at) < DATE('"+str(today)+"') " 
 
    query += " group by DATE(date), leagueapi_id, season "
    query += " order by date "  
    # query += " limit 0,2 "  
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
    counter = 0  
    # ---------------------------------------------------------- 
    # fO_get_group_league_status_match_finished_DETAILED(day1, day2, 'odds', space)
    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        for rs1 in result: 
            # --------------------------------------------------  
            counter += 1
            # -------------------------------------------------- 
            date = rs1[0]
            league = rs1[1]
            bookmaker = rs1[2]
            season  = rs1[3]

            end_odd_updated_at  = rs1[4]
            fixture_status  = rs1[5]
            count_rows  = rs1[6]
            # --------------------------------------------------
            words_001 = space + str(counter) + ". "
            words_001 += str(date) + " // "
            words_001 += str(league) + " // "
            words_001 += str(bookmaker) + " // "
            words_001 += str(season)+ " // "
            words_001 += str(end_odd_updated_at) + " // "
            words_001 += str(fixture_status) + " == "
            words_001 += str(count_rows)
            # -------------------------------------------------- 
            words =  words_001
            print(words, flush=True) 

            # --------------------------------------------------  
            DICT = {
                "date" : date,
                "bookmaker" : bookmaker,
                "season" : season,
                "league" : league,
                "page" : 1,
            }
            # ao_controll_match_update(date, bookmaker, season, league, 1, space) 
            ao_controll_match_update(DICT, 'end_', space) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  

def fO_get_fixture_status_match_finished(day1, day2, today, space):
    # ----------------------------------------------------------   
    # 2a. Enddates 7-6 Days
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_fixture_status_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    #
    # always double check to ff_get_fixture_status_match_finished
    # same query
    # 
    query = "Select "
    query += " DATE(date) "
    query += " , leagueapi_id"
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_odds.leagueapi_id) "
    query += " , season"
    query += " , DATE(end_odd_updated_at) "
    query += " , fixture_status  "
    query += " , fixtureapi_id  "

    query += " from football_odds "    

    query += " where  date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    query += " and end_response is null "
    query += " and deleted_at is null "  
    query += " and fixture_status = 'Match Finished' "  
  
    query += " order by date "  
    # query += " limit 0,2 "  
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
    fO_get_fixture_status_match_finished_DETAILED(day1, day2, 'odds', space)
    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        for rs1 in result: 
            # --------------------------------------------------  
            count_rows += 1
            # -------------------------------------------------- 
            date = rs1[0]
            league = rs1[1]
            bookmaker = rs1[2]
            season  = rs1[3]

            end_odd_updated_at  = rs1[4]
            fixture_status  = rs1[5]
            fixtureapi_id  = rs1[6]
            # --------------------------------------------------
            words_001 = space + str(count_rows) + ". "
            words_001 += str(date) + " // "
            words_001 += str(fixtureapi_id) + " // "
            words_001 += str(bookmaker) + " // " 
            words_001 += str(end_odd_updated_at)+ " // "
            words_001 += str(fixture_status)
            # -------------------------------------------------- 
            words =  words_001
            print(words, flush=True) 
            # --------------------------------------------------  
            DICT = { 
                "bookmaker" : bookmaker,
                "fixture" : fixtureapi_id,  
            }
            # ao_controll_match_update(date, bookmaker, season, league, 1, space) 
            ao_controll_match_update(DICT, 'oneend_', space) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  

def fO_get_fixture_status_match_finished_DETAILED(day1, day2, today, space):
    # ----------------------------------------------------------   
    # 2a. Enddates 7-6 Days
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_fixture_status_match_finished_DETAILED()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    #
    # always double check to ff_get_fixture_status_match_finished
    # same query
    # 
    query = "Select "
    query += " DATE(date) as Date "
    query += " , fixture_status as fs  "
    query += " , fixtureapi_id  as fx "
    query += " , (select bookmakersapi_id from football_leagues where leagueapi_id = football_odds.leagueapi_id)  as bm " 
    query += " , end_response as er " 

    query += " from football_odds "    

    query += " where  date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    query += " and end_response is null "
    query += " and deleted_at is null "  
    query += " and fixture_status = 'Match Finished' "  
  
    query += " order by date "   
    # ----------------------------------------------------------    
    # print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description])
    # ----------------------------------------------------------    
    mycursor.close()
    mydb.close()
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

def fO_get_group_league_status_match_finished_DETAILED(day1, day2, ROUTES, space):
    # ----------------------------------------------------------   
    # ff_get_fixture_status_match_finished
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_group_league_status_match_finished_DETAILED()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " DATE(date), "
    query += " leagueapi_id, "
    query += " (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id), "
    query += " season,  "
    query += " fixtureapi_id,  "
    query += " pre_ah_pattern,  "
    query += " pre_gou_pattern,  "
    query += " fixture_status  "
    query += " from football_odds "     
    if(ROUTES == 'odds'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "  
        query += " and fixture_status like 'Match Finished' "

        query += " and deleted_at is null "  
        query += " order by date desc"  
    elif(ROUTES == 'xpattern'):
        # query += " where date <= '"+day2+"' "
        # query += " and date >= '"+day1+"' "  
        query += " where fixture_status like 'Match Finished Ended' "
        
        query += " and deleted_at is null "  
        query += " and end_response = 1 "  
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  
    elif(ROUTES == 'pre_xpattern'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "   
        
        query += " and deleted_at is null "  
        query += " and pre_response != 3 "  
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  
    elif(ROUTES == 'one_xpattern'):
        query += " where one = 1 " 
        query += " and deleted_at is null "  
        query += " order by date desc"  
    elif(ROUTES == 'all_pre_xpattern'):
        query += " where  deleted_at is null "  
        query += " and pre_response != 3 "  
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  
    elif(ROUTES == 'all_end_xpattern'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "   
        query += " and  deleted_at is null "  
        query += " and end_response != 3 "  
        query += " and fixture_status like 'Match Finished' "
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  



        
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------  
        date = rs1[0]
        league = rs1[1]
        bookmaker = rs1[2]
        season  = rs1[3]

        fixtureapi_id  = rs1[4]
        pre_ah_pattern  = rs1[5]
        pre_gou_pattern  = rs1[6]
        fixture_status  = rs1[7]
        # ------------------------------------------------------  
        words_001 = space + str(count_rows) + ". "
        words_001 += str(date) + " // "
        words_001 += str(league) + " // "
        words_001 += str(bookmaker) + " // "
        words_001 += str(season)+ " // "
        words_001 += str(fixtureapi_id)+ " // "
        words_001 += str(pre_ah_pattern)+ " // "
        words_001 += str(pre_gou_pattern)+ " // "
        words_001 += str(fixture_status)
        # ------------------------------------------------------  
        words =  words_001
        print(words, flush=True)  
        # ------------------------------------------------------  
        if(ROUTES == 'xpattern'): 
            # xp_set_pattern(fixtureapi_id, 'end_', 'no', space)
            xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
        elif(ROUTES == 'pre_xpattern'): 
            # xp_set_pattern(fixtureapi_id, 'pre_', 'no', space)
            xpN_set_pattern(fixtureapi_id, 'pre_', 4, space)
        elif(ROUTES == 'all_pre_xpattern'): 
            # xp_set_pattern(fixtureapi_id, 'pre_', 'no', space)
            xpN_set_pattern(fixtureapi_id, 'pre_', 4, space)
        elif(ROUTES == 'all_end_xpattern'): 
            # xp_set_pattern(fixtureapi_id, 'end_', 'no', space)
            xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
        elif(ROUTES == 'one_xpattern'):
            # xp_set_pattern(fixtureapi_id, 'pre_', 'yes', space)
            # xpN_set_pattern(fixtureapi_id, 'end_', 'no', space) 
            xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
    # ----------------------------------------------------------  
 
def fO_gak_sempet_predates(day0, date_raw, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_gak_sempet_predates()", flush=True)
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
    query += " leagueapi_id, " 
    query += " season, "
    query += " DATE(date),  "
    query += " pre_response,  "
    query += " (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id) "
    query += " from football_odds " 
    query += " where date = '"+day0+"' "  
    query += " and deleted_at is null "  
    query += " and pre_odd_updated_at is null "    
    query += " group by leagueapi_id, season, DATE(date), pre_response "
    query += " order by leagueapi_id asc  "   
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
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
        counter         += 1
        leagueapi_id    = str(x[0])  
        season          = str(x[1])   
        date            = str(x[2])   
        pre_response    = str(x[3])   
        bookmaker       = str(x[4])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " > Date: " + date 
        word += " > pre_response: " + pre_response 
        word += " > bookmaker: " + bookmaker 
        print(word, flush=True)   
        # ------------------------------------------------------  

    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        for x in result:    
            # ------------------------------------------------------
            counter         += 1
            leagueapi_id    = str(x[0])  
            season          = str(x[1])   
            date            = str(x[2])   
            pre_response    = str(x[3])   
            bookmaker       = str(x[4])   
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
            word += " #" + leagueapi_id 
            word += " - " + season 
            word += " > Date: " + date 
            word += " > pre_response: " + pre_response 
            word += " > bookmaker: " + bookmaker 
            print(word, flush=True)   
            # ------------------------------------------------------
            DICT = {
                "date" : date,
                "date_raw" : date_raw,
                "bookmaker" : bookmaker,
                "season" : season,
                "league" : leagueapi_id,
                "page" : 1,
            }
            # ao_controll_match_update(date, bookmaker, season, league, 1, space) 
            ao_controll_match_update(DICT, 'preleague_', space) 
            #------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
 
def fO_get_fixture_one(space):
    # ----------------------------------------------------------  
    #
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_fixture_one()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    #
    # always double check to ff_get_fixture_status_match_finished
    # same query
    # 
    query = "Select "
    query += " DATE(date),  "
    query += " leagueapi_id, "
    query += " (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id), "
    query += " season, "
    query += " DATE(end_odd_updated_at), "
    query += " fixture_status, "
    query += " fixtureapi_id  "

    query += " from football_odds "    

    query += " where one = 1 "  
    query += " order by date asc "  
    # query += " limit 0,2 "  
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------  
        date = rs1[0]
        league = rs1[1]
        bookmaker = rs1[2]
        season  = rs1[3]
        # ------------------------------------------------------  
        end_odd_updated_at  = rs1[4]
        fixture_status  = rs1[5]
        fixtureapi_id  = rs1[6]
        # ------------------------------------------------------  
        words_001 = space + str(count_rows) + ". "
        words_001 += str(date) + " // "
        words_001 += str(league) + " // "
        words_001 += str(bookmaker) + " // "
        words_001 += str(season) + " // "
        words_001 += str(end_odd_updated_at) + " // "
        words_001 += str(fixture_status) + " // "
        words_001 += str(fixtureapi_id)
        # ------------------------------------------------------  
        words =  words_001
        print(words, flush=True) 
        # ------------------------------------------------------  
        DICT = {
            "fixture" : fixtureapi_id,
            "bookmaker" : bookmaker, 
        } 
        ao_controll_match_update(DICT, 'one_', space) 
        # ------------------------------------------------------  
    # ----------------------------------------------------------  

def fO_check_predates(day0, day1, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_predates()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " leagueapi_id as lg " 
    query += " , season as ss "  
    query += " , (select SUBSTR(name, 1, 15) from football_teams where teamapi_id = teams_homeapi_id) as home " 
    query += " , (select SUBSTR(name, 1, 15) from football_teams where teamapi_id = teams_awayapi_id) as away "  
    query += " , SUBSTR(fixture_status, 1, 15)  as fs " 
    query += " , pre_response as pr "   
    query += " , pre_odd_updated_at as odd_date "   
    query += " from football_odds " 
    query += " where date >= '"+str(day0)+"' "  
    query += " and date <= '"+str(day1)+"' "  
    query += " and deleted_at is null "     
    query += " order by leagueapi_id, date asc "     
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

def fO_check_enddates(day0, day1, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_enddates()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " leagueapi_id as lg " 
    query += " , season as ss "  
    query += " , (select SUBSTR(name, 1, 7) from football_teams where teamapi_id = teams_homeapi_id) as home " 
    query += " , (select SUBSTR(name, 1, 7) from football_teams where teamapi_id = teams_awayapi_id) as away "  
    query += " , SUBSTR(fixture_status, 1, 15)  as fs "  
    query += " , end_response as er "  
    query += " , end_ah_pattern as ah "  
    query += " , end_gou_pattern as gou "  
    query += " from football_odds " 
    query += " where date >= '"+str(day0)+"' "  
    query += " and date <= '"+str(day1)+"' "  
    query += " and end_response is null "     
    query += " and deleted_at is null "     
    query += " and fixture_status like 'Match Finished' "      
    query += " order by leagueapi_id, date asc "   
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description])
    # ----------------------------------------------------------    
    mycursor.close()
    mydb.close()
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

def fO_predates_special_fixtures(day0, day1, day14, fixture_status, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_predates_special_fixtures()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(fixture_status == 'None'):   
        query = "Select "
        query += " leagueapi_id, " 
        query += " season, "
        query += " DATE(date),  "
        query += " pre_response,  "
        query += " (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id) "
        query += " from football_odds " 
        query += " where date >= '"+day0+"' "  
        query += " and date <= '"+day1+"' "  
        query += " and deleted_at is null "   
        query += " and fixture_status is null "     
        query += " group by leagueapi_id, season, DATE(date), pre_response "
        query += " order by leagueapi_id asc  "   

        ROUTES = 'Next14days'
    elif(fixture_status == 'Time to be defined'):    
        query = "Select "
        query += " leagueapi_id " 
        query += " , season "  
        query += " from football_odds " 
        query += " where date >= '"+day0+"' "  
        query += " and date <= '"+day1+"' "  
        query += " and fixture_status like 'Time to be defined' "   
        query += " and deleted_at is null "      
        query += " group by leagueapi_id, season "
        query += " order by leagueapi_id asc  "   

        ROUTES = 'Next14days'
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
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
        counter         += 1
        leagueapi_id    = str(x[0])  
        season          = str(x[1])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        print(word, flush=True)   
        # ------------------------------------------------------   
    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        for x in result:    
            # ------------------------------------------------------
            counter         += 1
            leagueapi_id    = str(x[0])  
            season          = str(x[1])    
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
            word += " #" + leagueapi_id 
            word += " - " + season  
            print(word, flush=True)   
            # ------------------------------------------------------
            DICT = { 
                "season" : season,
                "leagueapi_id" : leagueapi_id, 
                "from" : day0,
                "to" : day14,
            }
            af_controll_match_update(DICT, ROUTES, space) 
            #------------------------------------------------------

            
def fO_check_updates(day0, day1, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_updates()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " date as date "  
    query += " , leagueapi_id as lg " 
    query += " , season as ss "  
    query += " , (select SUBSTR(name, 1, 7) from football_teams where teamapi_id = teams_homeapi_id) as home " 
    query += " , (select SUBSTR(name, 1, 7) from football_teams where teamapi_id = teams_awayapi_id) as away "  
    query += " , SUBSTR(fixture_status, 1, 15)  as fs "  
    query += " , end_response as pr "  
    query += " , end_ah_pattern as ah "  
    query += " , end_gou_pattern as gou "  
    query += " from football_odds " 
    query += " where date >= '"+str(day0)+"' "  
    query += " and date <= '"+str(day1)+"' "     
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "
    query += " and deleted_at is null "     
    query += " order by  date, leagueapi_id asc "   
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description])
    # ----------------------------------------------------------    
    mycursor.close()
    mydb.close()
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
            
def fO_check_updates_group_by_league(day0, day1, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_updates_group_by_league()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " leagueapi_id  " 
    query += " , season  "    
    query += " from football_odds " 
    query += " where date >= Date('"+str(day0)+"') "  
    query += " and date <= Date('"+str(day1)+"') "     
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "
    query += " and deleted_at is null "     
    query += " group by leagueapi_id, season asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description])
    # ----------------------------------------------------------    
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    pd.set_option('display.max_rows', None) 
    pd.set_option('display.width', 120)
    # ---------------------------------------------------------- 
    total_rows = len(rows)
    # ----------------------------------------------------------    
    desc = "League yang belum Match Finished"
    print(space + desc, flush=True) 
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
    
def fO_check_updates_group_by_league_only_onedate(day0, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_updates_group_by_league_only_onedate()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " leagueapi_id  " 
    query += " , season  "    
    query += " from football_odds " 
    query += " where date = DATE('"+str(day0)+"') "   
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' ) "
    query += " and deleted_at is null "     
    query += " group by leagueapi_id, season asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description])
    # ----------------------------------------------------------    
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    pd.set_option('display.max_rows', None) 
    pd.set_option('display.width', 120)
    # ---------------------------------------------------------- 
    total_rows = len(rows)
    # ----------------------------------------------------------    
    desc = "League yang belum Match Finished"
    print(space + desc, flush=True) 
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

def fO_get_fixture_today_for_update_pattern(day0, day1, dayZ, space):
    # ----------------------------------------------------------  
    #
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_get_fixture_today_for_update_pattern()", flush=True)
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
    query += " , (select name from football_leagues where leagueapi_id = football_odds.leagueapi_id) as name "  
    query += " , (select country from football_leagues where leagueapi_id = football_odds.leagueapi_id) as country " 

    query += " from football_odds "     

    query += " where date >= '"+day0+"' "  
    query += " and date <= '"+day1+"' "  
    query += " group by "  
    query += " leagueapi_id "  
    query += " , season "  
    query += " order by leagueapi_id asc "  
    # query += " limit 0,2 "  
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id      = rs1[0] 
        season      = rs1[1] 
        name        = rs1[2] 
        country     = rs1[3] 
        # ------------------------------------------------------  
        words = space + str(count_rows) + ". " 
        words += str(country) + "  "  
        words += str(name) + "  " 
        words += str(leagueapi_id) + " - " 
        words += str(season)  
        # ------------------------------------------------------   
        print(words, flush=True) 
        # ------------------------------------------------------ 
        related_league = lg_related_pattern_id(leagueapi_id, space) 
        # ------------------------------------------------------ 
        if(related_league != 0):
            ff_get_fixtures_group_by_pre_end_patternlists(leagueapi_id, space)
        # ------------------------------------------------------ 
        print("")
    # ----------------------------------------------------------  
 
def fO_group_league_to_update_pattern(day0, day1, space):
    # ----------------------------------------------------------  
    #
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_group_league_to_update_pattern()", flush=True)
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
    query += " , (select name from football_leagues where leagueapi_id = football_odds.leagueapi_id) as name "  
    query += " , (select country from football_leagues where leagueapi_id = football_odds.leagueapi_id) as country " 

    query += " from football_odds "     

    query += " where date >= '"+day0+"' "  
    query += " and date <= '"+day1+"' "  
    query += " group by "  
    query += " leagueapi_id "  
    query += " , season "  
    query += " order by leagueapi_id asc "  
    # query += " limit 0, 3 "  
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id      = rs1[0] 
        season      = rs1[1] 
        name        = rs1[2] 
        country     = rs1[3] 
        # ------------------------------------------------------  
        words = space + str(count_rows) + ". " 
        words += str(country) + "  "  
        words += str(name) + "  " 
        words += str(leagueapi_id) + " - " 
        words += str(season)  
        # ------------------------------------------------------   
        print(words, flush=True) 
        # ------------------------------------------------------
        # Null to Pre Response
        # fO_league_to_response_2(leagueapi_id, day0, day1, 'Pre', space)
        # Null to End Response
        # fO_league_to_response_2(leagueapi_id, day0, day1, 'End', space)
        # test Related
        lg_related = lg_related_pattern_id(leagueapi_id, space)
        print(space + "____lg_related: " + str(lg_related), flush=True)
        print("", flush=True)
    # ---------------------------------------------------------- 

def fO_league_to_response_2(leagueapi_id, day0, day1, status, space):
    # ----------------------------------------------------------  
    #
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_league_to_response_2()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    if(status == 'Pre'):
        query = "UPDATE `football_odds` SET  "
        query += " pre_response = 2 "  
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        query += " and fixture_status in ('Match Finished', 'Match Finished Ended') " 

        query += " and pre_ah_pattern is not null " 
        query += " and pre_gou_pattern is not null "  

        query += " and pre_ah_pattern != 'H' " 
        query += " and pre_gou_pattern != 'G' "  
    elif(status == 'End'): 
        query = "UPDATE `football_odds` SET  "
        query += " end_response = 2 "  
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "  
        
        query += " and end_ah_pattern is not null " 
        query += " and end_gou_pattern is not null "  

        query += " and end_ah_pattern != 'H' " 
        query += " and end_gou_pattern != 'G' "  
    # ----------------------------------------------------------    
    mycursor.execute(query)
    mydb.commit()      
    # ----------------------------------------------------------      
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------   

def fO_import_date(fixtureapi_id, leagueapi_id, season, space):
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_import_date()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  ' 
    query += ' date '     
    query += 'FROM football_odds' 
    query += " WHERE leagueapi_id = '"+leagueapi_id+"' " 
    query += " and season = '"+season+"' "   
    query += " and fixtureapi_id = '"+fixtureapi_id+"' "    
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter         += 1
        date            = str(x[0])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " " + date 
        word += " #" + fixtureapi_id 
        word += "  " + leagueapi_id 
        word += " - " + season 
        print(word, flush=True)         
    # ----------------------------------------------------------   
    fO_update_date(fixtureapi_id, leagueapi_id, season, date, space)
    # ----------------------------------------------------------  
 
def fO_update_date(fixtureapi_id, leagueapi_id, season, date, space):
    # ----------------------------------------------------------  
    #
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_update_date()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query = "UPDATE `football_statistics` SET  "
    query += " date = '"+str(date)+"' "  
    query += " where fixtureapi_id = '"+str(fixtureapi_id)+"' " 
    query += " and leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' " 
    # ----------------------------------------------------------    
    mycursor.execute(query)
    mydb.commit()      
    # ----------------------------------------------------------      
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ---------------------------------------------------------- 
            
def fO_league_to_update_pattern_end(day0, day1, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_league_to_update_pattern_end()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select "  
    query += " leagueapi_id as lg " 
    query += " , season as ss "    
    query += " from football_odds " 
    query += " where date >= '"+str(day0)+"' "  
    query += " and date <= '"+str(day1)+"' "      
    query += " and deleted_at is null "     
    query += " group by leagueapi_id, season asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id      = rs1[0] 
        season      = rs1[1] 
        # ------------------------------------------------------ 
        word = space + "[" + str(count_rows) + "/" +str(len(result)) + "] " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(season) 
        # ------------------------------------------------------ 
        sAg_rounder(leagueapi_id, space)
    # ---------------------------------------------------------- 
            

              
def fO_group_by_league_multi_ROUTE(day0, day1, ROUTE, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_group_by_league_multi_ROUTE()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select " 
    query += " leagueapi_id  " 
    query += " , season  "    
    query += " from football_odds " 
    if(ROUTE == 'fixing_pre_xpattern'): 
        query += " where date >= Date('"+str(day0)+"') "  
        query += " and date <= Date('"+str(day1)+"') "      
        query += " and deleted_at is null "     
        query += " group by leagueapi_id, season asc "   
    elif(ROUTE == 'fixing_end_xpattern'): 
        query += " where date >= Date('"+str(day0)+"') "  
        query += " and date <= Date('"+str(day1)+"') "      
        query += " and deleted_at is null "     
        query += " group by leagueapi_id, season asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id      = rs1[0] 
        season      = rs1[1] 
        # ------------------------------------------------------ 
        word = space + "[" + str(count_rows) + "/" +str(len(result)) + "] " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(season) 
        # ------------------------------------------------------ 
        if(ROUTE == 'fixing_pre_xpattern'): 
            xpN_get_league_fixture_to_reset(leagueapi_id, 'pre_', 4, space)
        if(ROUTE == 'fixing_end_xpattern'): 
            xpN_get_league_fixture_to_reset(leagueapi_id, 'end_', 4, space)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

    
def fO_check_pre_end_response(leagueapi_id, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_pre_end_response()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select "  
    query += " leagueapi_id " 
    query += " , season "    
    query += " , pre_response "    
    query += " , end_response "     
    query += " , fixture_status "   
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and deleted_at is null "     
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') " 
    query += " group by leagueapi_id, season, pre_response, end_response, fixture_status  asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id    = rs1[0] 
        season          = rs1[1] 
        pre_response          = rs1[2] 
        end_response          = rs1[3] 
        fixture_status          = rs1[4] 
        # ------------------------------------------------------ 
        word = space + "[" + str(count_rows) + "/" +str(len(result)) + "] " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(season) 
        word += " => " + str(pre_response) 
        word += " / " + str(end_response) 
        word += " == " + str(fixture_status) 
        # ------------------------------------------------------  
        print(word, flush=True)
    # ---------------------------------------------------------- 
            
def fO_check_pattern_from_pattern_only(leagueapi_id, space):
    # ----------------------------------------------------------  
    # 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fO_check_pattern_from_pattern_only()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select "  
    query += " leagueapi_id " 
    query += " , season "      
    query += " , pattern_only "     
    query += " , fixture_status "   
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and deleted_at is null "     
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') " 
    query += " group by leagueapi_id, season, pattern_only, fixture_status  asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id    = rs1[0] 
        season          = rs1[1] 
        pre_response          = rs1[2]  
        fixture_status          = rs1[3] 
        # ------------------------------------------------------ 
        word = space + "[" + str(count_rows) + "/" +str(len(result)) + "] " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(season) 
        word += " only => " + str(pre_response)  
        word += " == " + str(fixture_status) 
        # ------------------------------------------------------  
        print(word, flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06" 
    # ----------------------------------------------------------  
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------  
    query = "Select "  
    query += " leagueapi_id " 
    query += " , season "    
    query += " , pattern_from "       
    query += " , fixture_status "   
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and deleted_at is null "     
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') " 
    query += " group by leagueapi_id, season, pattern_from, fixture_status  asc "   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
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
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------   
        leagueapi_id    = rs1[0] 
        season          = rs1[1] 
        pre_response          = rs1[2]  
        fixture_status          = rs1[3] 
        # ------------------------------------------------------ 
        word = space + "[" + str(count_rows) + "/" +str(len(result)) + "] " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(season) 
        word += " from => " + str(pre_response)  
        word += " == " + str(fixture_status) 
        # ------------------------------------------------------  
        print(word, flush=True)
    # ---------------------------------------------------------- 
            