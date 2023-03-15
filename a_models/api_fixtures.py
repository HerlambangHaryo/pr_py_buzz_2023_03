# Import
import mysql.connector 
from a_models.api_accounts import *   

import pytz
utc=pytz.UTC 

import requests
import json 
  
def af_controll_match_update(DICT, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "af_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space)
        # DICT  

        af_response_fixtures(DICT, ROUTES, APIkey, space)
    # ----------------------------------------------------------
 
def af_response_fixtures(DICT, ROUTES, APIkey, space): 
    # ---------------------------------------------------------- 
    # APIkey, leagueapi_id, season, one_week_later, two_weeks_before, space
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "af_response_fixtures()", flush=True) 
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures" 
    # ---------------------------------------------------------- 
    # print(space + "league : " + str(leagueapi_id))
    # print(space + "season : " + str(season))
    # print(space + "from : " + str(day1))
    # print(space + "to : " + str(day2)) 
    # ----------------------------------------------------------  

    if(ROUTES == 'fixtureapi_id'):
        DICTfixtureapi_id = DICT['fixtureapi_id']
        querystring = {"id":DICTfixtureapi_id} 
        print(space + "ROUTES : fixtureapi_id", flush=True) 
        print(space + "fixtureapi_id : " + str(DICTfixtureapi_id), flush=True) 

    if(ROUTES == 'leagueapi_id'):
        print(space + "ROUTES : leagueapi_id", flush=True) 

        DICTleagueapi_id    = DICT['leagueapi_id']
        print(space + "leagueapi_id : " + str(DICTleagueapi_id), flush=True) 

        DICTseason          = DICT['season']
        print(space + "season : " + str(DICTseason), flush=True)

        DICTday1            = DICT['day1']
        print(space + "day1 : " + str(DICTday1), flush=True) 

        DICTday2            = DICT['day2']
        print(space + "day2 : " + str(DICTday2), flush=True) 

        querystring = {"league":DICTleagueapi_id,"season":DICTseason, "from": DICTday1, "to": DICTday2} 
    # ---------------------------------------------------------- 
    headers = {
        "X-RapidAPI-Key": APIkey,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    # ----------------------------------------------------------
    response = requests.request("GET", url, headers=headers, params=querystring)
    d = json.loads(response.text)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------   
    print(space + "Total API Response(s) : " + str(len(d['response'])), flush=True) 
    # ---------------------------------------------------------- 
    counter_response = 0
    # ---------------------------------------------------------- 
    space += "__"
    counter = 0
    # ----------------------------------------------------------  
    if(len(d['response']) != 0):
    # ---------------------------------------------------------- 
        for row in d['response']:
            # -------------------------------------------------- 
            fixtureapi_id     = str(row['fixture']['id'])  
            fixture_date_now  = datetime.fromisoformat(row['fixture']['date'])
            fixture_date      = str(fixture_date_now)
            # --------------------------------------------------
            fixture_status     = str(row['fixture']['status']['long'])  
            leagueapi_id       = str(row['league']['id'])
            season             = str(row['league']['season'])
            xround             = str(row['league']['round'].replace("'", "\\'"))
            league_name        = str(row['league']['name'].replace("'", "\\'"))
            league_country     = str(row['league']['country'].replace("'", "\\'")) 
            teams_home         = str(row['teams']['home']['name'].replace("'", "\\'"))
            teams_away         = str(row['teams']['away']['name'].replace("'", "\\'"))  
            # --------------------------------------------------
            # print(str(fixture_date))
            # --------------------------------------------------
            # print(space + str(fixture_date_now) + " <= " + str(utc.localize(one_week_later)) )
            # print(space + str(fixture_date_now) + " >= " + str(utc.localize(two_weeks_before)) )
            # print("")
            # -------------------------------------------------- 
            # if(fixture_date_now <= utc.localize(one_week_later) and 
            #    fixture_date_now >= utc.localize(two_weeks_before) ):
            # --------------------------------------------------  
            good_to_go = 1
            # -------------------------------------------------- 
            # if(fixture_status == "Match Finished"):
            #     good_to_go = 1 
            # -------------------------------------------------- 
            # print(space + fixture_status)
            # print(space + str(good_to_go))
            # -------------------------------------------------- 
            if(good_to_go == 1):
                # ---------------------------------------------- 
                counter += 1
                # ---------------------------------------------- 
                referee    = row['fixture']['referee']; 
                if( referee is None):
                    referee = "Null"
                else : 
                    referee    = "'" + str(row['fixture']['referee'].replace("'", "\\'")) + "'"
                # ---------------------------------------------- 
                venue_name        = row['fixture']['venue']['name'] 
                if( venue_name is None):
                    venue_name = "Null"
                else : 
                    venue_name    = "'" + str(row['fixture']['venue']['name'].replace("'", "\\'")) + "'"
                # ---------------------------------------------- 
                venue_city        =  row['fixture']['venue']['city']
                if( venue_city is None):
                    venue_city = "Null"
                else : 
                    venue_city    = "'" + str(row['fixture']['venue']['city'].replace("'", "\\'")) + "'"
                # ---------------------------------------------- 
                fixture_elapsed    = row['fixture']['status']['elapsed']; 
                if( fixture_elapsed is None):
                    fixture_elapsed = "Null"
                else : 
                    fixture_elapsed    = "'" + str(row['fixture']['status']['elapsed']) + "'" 
                # ---------------------------------------------- 
                teams_home_id      = str(row['teams']['home']['id']) #
                teams_away_id      = str(row['teams']['away']['id']) #
                teams_home_logo    = str(row['teams']['home']['logo']) #
                teams_away_logo    = str(row['teams']['away']['logo']) #
                league_logo        = str(row['league']['logo']) #
                league_flag        = str(row['league']['flag']) #
                # ---------------------------------------------- 
                goals_home    = row['goals']['home']; 
                if( goals_home is None):
                    goals_home = "Null"
                else : 
                    goals_home    = "'" + str(row['goals']['home']) + "'"
                # ---------------------------------------------- 
                goals_away    = row['goals']['away']; 
                if( goals_away is None):
                    goals_away = "Null"
                else : 
                    goals_away    = "'" + str(row['goals']['away']) + "'"
                # ---------------------------------------------- 
                score_halftime_home    = row['score']['halftime']['home']; 
                if( score_halftime_home is None):
                    score_halftime_home = "Null"
                else : 
                    score_halftime_home    = "'" + str(row['score']['halftime']['home']) + "'"
                # ---------------------------------------------- 
                score_halftime_away    = row['score']['halftime']['away']; 
                if( score_halftime_away is None):
                    score_halftime_away = "Null"
                else : 
                    score_halftime_away    = "'" + str(row['score']['halftime']['away']) + "'"
                # ---------------------------------------------- 
                score_fulltime_home    = row['score']['fulltime']['home']; 
                if( score_fulltime_home is None):
                    score_fulltime_home = "Null"
                else : 
                    score_fulltime_home    = "'" + str(row['score']['fulltime']['home']) + "'"
                # ---------------------------------------------- 
                score_fulltime_away    = row['score']['fulltime']['away']
                if( score_fulltime_away is None):
                    score_fulltime_away = "Null"
                else : 
                    score_fulltime_away    = "'" + str(row['score']['fulltime']['away']) + "'"
                # ---------------------------------------------- 
                score_extratime_home   = row['score']['extratime']['home']
                if( score_extratime_home is None):
                    score_extratime_home = "Null"
                else :
                    score_extratime_home    = "'" + str(row['score']['extratime']['home']) + "'"
                # ---------------------------------------------- 
                score_extratime_away   = row['score']['extratime']['away']
                if( score_extratime_away is None):
                    score_extratime_away = "Null"
                else :
                    score_extratime_away    = "'" + str(row['score']['extratime']['away']) + "'"
                # ---------------------------------------------- 
                score_penalty_home     = row['score']['penalty']['home']
                if( score_penalty_home is None):
                    score_penalty_home = "Null"
                else :
                    score_penalty_home    = "'" + str(row['score']['penalty']['home']) + "'"
                # ---------------------------------------------- 
                score_penalty_away     = row['score']['penalty']['away']
                if( score_penalty_away is None):
                    score_penalty_away = "Null"
                else :
                    score_penalty_away    = "'" + str(row['score']['penalty']['away']) + "'"
                # ---------------------------------------------- 
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor() 
                # ----------------------------------------------
                check = " select * "   
                check += " from football_fixtures "   
                check += " where fixtureapi_id = '" + str(fixtureapi_id) + "'"   
                # ----------------------------------------------   
                mycursor = mydb.cursor()
                mycursor.execute(check)
                result_check =  mycursor.fetchall()
                # ----------------------------------------------   
                word = space + str(counter) + ". /" 
                word += fixture_status + "/ "
                word += fixtureapi_id + " / "
                word += teams_home + " vs "
                word += teams_away + " /"
                word += str(fixture_date_now) + "/ " 
                # ---------------------------------------------- 
                if(len(result_check) > 0):
                    # ------------------------------------------ 
                    word += " UPDATED "
                    print(word) 
                    # ------------------------------------------ 
                    query_commit = "update football_fixtures set "   
                    # ---------------------------------------------- 
                    query_commit += " date = '"+fixture_date+"', " 
                    query_commit += " fixture_status = '"+fixture_status+"', " 
                    query_commit += " referee = "+referee+", " 
                    query_commit += " leagueapi_id = '"+leagueapi_id+"', " 
                    query_commit += " season = '"+season+"', " 
                    query_commit += " round = '"+xround+"', " 
                    query_commit += " league_name = '"+league_name+"', " 
                    query_commit += " league_country = '"+league_country+"', " 
                    query_commit += " teams_home = '"+teams_home+"', " 
                    query_commit += " teams_away = '"+teams_away+"', " 
                    query_commit += " goals_home = "+goals_home+", " 
                    query_commit += " goals_away = "+goals_away+", " 
                    # ---------------------------------------------- 
                    query_commit += " score_halftime_home = "+score_halftime_home+", " 
                    query_commit += " score_halftime_away = "+score_halftime_away+", " 
                    query_commit += " score_fulltime_home = "+score_fulltime_home+", " 
                    query_commit += " score_fulltime_away = "+score_fulltime_away+", "  
                    query_commit += " score_extratime_home = "+score_extratime_home+", " 
                    query_commit += " score_extratime_away = "+score_extratime_away+", "  
                    query_commit += " score_penalty_home = "+score_penalty_home+", " 
                    query_commit += " score_penalty_away = "+score_penalty_away+", "
                    # ----------------------------------------------    
                    query_commit += " venue_name = "+venue_name+", " 
                    query_commit += " venue_city = "+venue_city+", " 
                    query_commit += " fixture_elapsed = "+fixture_elapsed+", " 
                    query_commit += " teams_home_id = '"+teams_home_id+"', " 
                    query_commit += " teams_away_id = '"+teams_away_id+"', " 
                    query_commit += " teams_home_logo = '"+teams_home_logo+"', " 
                    query_commit += " teams_away_logo = '"+teams_away_logo+"', " 
                    query_commit += " league_logo = '"+league_logo+"', " 
                    query_commit += " league_flag = '"+league_flag+"', " 
                    # ----------------------------------------------   
                    query_commit += " updated_at = current_timestamp " 
                    query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "   
                    # ---------------------------------------------- 
                # insert
                else:
                    # ------------------------------------------ 
                    word += " INSERTED "
                    # print(word) 
                    # ------------------------------------------ 
                    query_commit = "INSERT INTO `football_fixtures`( "
                    # ------------------------------------------ 
                    query_commit += " `fixtureapi_id`, " 
                    query_commit += " `date`, " 
                    query_commit += " `fixture_status`, "  
                    query_commit += " `leagueapi_id`, " 
                    query_commit += " `season`, " 
                    query_commit += " `round`, " 
                    query_commit += " `league_name`, " 
                    query_commit += " `league_country`, " 
                    # ----------------------------------------------    
                    query_commit += " `teams_home`, " 
                    query_commit += " `teams_away`, "   
                    # ----------------------------------------------    
                    query_commit += " `venue_name`, " 
                    query_commit += " `venue_city`, "  
                    # ----------------------------------------------    
                    query_commit += " `teams_home_id`, " 
                    query_commit += " `teams_away_id`, " 
                    query_commit += " `teams_home_logo`, " 
                    query_commit += " `teams_away_logo`, " 
                    # ----------------------------------------------    
                    query_commit += " `league_logo`, " 
                    query_commit += " `league_flag`, "   
                    query_commit += " `updated_at` "   
                    # ----------------------------------------------   
                    query_commit += " ) VALUES ( "
                    # ----------------------------------------------   
                    query_commit += " '" + str(fixtureapi_id) + "', " 
                    query_commit += " '" + str(fixture_date) + "', " 
                    query_commit += " '" + str(fixture_status) + "', "  
                    query_commit += " '" + str(leagueapi_id) + "', " 
                    query_commit += " '" + str(season) + "', " 
                    query_commit += " '" + str(xround) + "', " 
                    query_commit += " '" + str(league_name) + "', " 
                    query_commit += " '" + str(league_country) + "', " 
                    # ----------------------------------------------    
                    query_commit += " '" + str(teams_home) + "', " 
                    query_commit += " '" + str(teams_away) + "', "   
                    # ----------------------------------------------    
                    query_commit += " " + str(venue_name) + ", " 
                    query_commit += " " + str(venue_city) + ", "  
                    # ----------------------------------------------    
                    query_commit += " '" + str(teams_home_id) + "', " 
                    query_commit += " '" + str(teams_away_id) + "', " 
                    query_commit += " '" + str(teams_home_logo) + "', " 
                    query_commit += " '" + str(teams_away_logo) + "', " 
                    # ----------------------------------------------    
                    query_commit += " '" + str(league_logo) + "', "  
                    query_commit += " '" + str(league_flag) + "', "    
                    query_commit += " current_timestamp "    
                    # ----------------------------------------------  
                    query_commit += " ) "
                    # print(query_commit)
                # ---------------------------------------------- 
                mycursor.execute(query_commit)
                mydb.commit()  
    # ---------------------------------------------------------- 
        