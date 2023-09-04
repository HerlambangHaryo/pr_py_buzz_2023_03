# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *    

import pytz
utc=pytz.UTC 

import requests
import json 

import time
 
def afP_controll_match_update(DICT, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afP_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space) 
        afP_response_fixtures(DICT, ROUTES, APIkey, space)
    # ----------------------------------------------------------
 
def afP_response_fixtures(DICT, ROUTES, APIkey, space): 
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afP_response_fixtures()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/players" 
    # ---------------------------------------------------------- 
    space += "__"
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    DICTfixtureapi_id = DICT['fixtureapi_id']
    print(space + "fixtureapi_id : " + str(DICTfixtureapi_id), flush=True)  
    # ----------------------------------------------------------   
    xROUTES = ROUTES
    print(space + "ROUTES : " + xROUTES, flush=True) 
    # ---------------------------------------------------------- 
    querystring = {"fixture":DICTfixtureapi_id} 
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
    total_rows = len(d['response'])
    # ---------------------------------------------------------- 
    space += "__"
    counter = 0
    # ---------------------------------------------------------- 
    if(len(d['response']) != 0):
        # ------------------------------------------------------
        for row in d['response']:
            # -------------------------------------------------- 
            teamapi_id = row['team']['id']  
            # print(team_id, flush=True)
            # --------------------------------------------------
            team_name = row['team']['name']  
            # print(team_name, flush=True)
            # --------------------------------------------------
            # --------------------------------------------------
            array_players = row['players']
            # --------------------------------------------------
            for ply in array_players:
                # ----------------------------------------------
                # print(ply)
                # ----------------------------------------------
                playerapi_id = ply['player']['id']  
                # print("player_id: " + str(player_id), flush=True)
                # ----------------------------------------------
                player_name = ply['player']['name']  
                # print("player_name: " + str(player_name), flush=True)
                # ----------------------------------------------
                player_photo = ply['player']['photo']  
                # print("player_photo: " + str(player_photo), flush=True)
                # ----------------------------------------------  
                # print("", flush=True) 
                # ----------------------------------------------
                games_minutes = ply['statistics'][0]['games']['minutes']
                if(games_minutes is None):
                    games_minutes = 0
                # print("games_minutes: " + str(games_minutes), flush=True)
                # ----------------------------------------------
                games_number = ply['statistics'][0]['games']['number']
                if(games_number is None):
                    games_number = 0
                # print("games_number: " + str(games_number), flush=True)
                # ----------------------------------------------
                games_position = ply['statistics'][0]['games']['position']
                if(games_position is None):
                    games_position = 0
                # print("games_position: " + str(games_position), flush=True)
                # ----------------------------------------------
                games_rating = ply['statistics'][0]['games']['rating']
                if(games_rating is None):
                    games_rating = 0
                # print("games_rating: " + str(games_rating), flush=True)
                # ----------------------------------------------
                games_captain = ply['statistics'][0]['games']['captain']
                if(games_captain is True):
                    games_captain = 1
                elif(games_captain is False):
                    games_captain = 0
                # print("games_captain: " + str(games_captain), flush=True)
                # ----------------------------------------------
                games_substitute = ply['statistics'][0]['games']['substitute']
                if(games_substitute is True):
                    games_substitute = 1
                elif(games_substitute is False):
                    games_substitute = 0
                # print("games_substitute: " + str(games_substitute), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                offsides = ply['statistics'][0]['offsides']
                if(offsides is None):
                    offsides = 0
                # print("offsides: " + str(offsides), flush=True)
                
        
                # print("", flush=True) 
                # ----------------------------------------------
                shots_total = ply['statistics'][0]['shots']['total']
                if(shots_total is None):
                    shots_total = 0
                # print("shots_total: " + str(shots_total), flush=True)
                # ----------------------------------------------
                shots_on = ply['statistics'][0]['shots']['on']
                if(shots_on is None):
                    shots_on = 0
                # print("shots_on: " + str(shots_on), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                goals_total = ply['statistics'][0]['goals']['total']
                if(goals_total is None):
                    goals_total = 0
                # print("goals_total: " + str(shots_total), flush=True)
                # ----------------------------------------------
                goals_conceded = ply['statistics'][0]['goals']['conceded']
                if(goals_conceded is None):
                    goals_conceded = 0
                # print("goals_conceded: " + str(goals_conceded), flush=True)
                # ----------------------------------------------
                goals_assists = ply['statistics'][0]['goals']['assists']
                if(goals_assists is None):
                    goals_assists = 0
                # print("goals_assists: " + str(goals_assists), flush=True)
                # ----------------------------------------------
                goals_saves = ply['statistics'][0]['goals']['saves']
                if(goals_saves is None):
                    goals_saves = 0
                # print("goals_saves: " + str(goals_saves), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                passes_total = ply['statistics'][0]['passes']['total']
                if(passes_total is None):
                    passes_total = 0
                # print("passes_total: " + str(passes_total), flush=True)
                # ----------------------------------------------
                passes_key = ply['statistics'][0]['passes']['key']
                if(passes_key is None):
                    passes_key = 0
                # print("passes_key: " + str(passes_key), flush=True)
                # ----------------------------------------------
                passes_accuracy = ply['statistics'][0]['passes']['accuracy']
                if(passes_accuracy is None):
                    passes_accuracy = 0
                # print("passes_accuracy: " + str(passes_accuracy), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                tackles_total = ply['statistics'][0]['tackles']['total']
                if(tackles_total is None):
                    tackles_total = 0
                # print("tackles_total: " + str(tackles_total), flush=True)
                # ----------------------------------------------
                tackles_blocks = ply['statistics'][0]['tackles']['blocks']
                if(tackles_blocks is None):
                    tackles_blocks = 0
                # print("tackles_blocks: " + str(tackles_blocks), flush=True)
                # ----------------------------------------------
                tackles_interceptions = ply['statistics'][0]['tackles']['interceptions']
                if(tackles_interceptions is None):
                    tackles_interceptions = 0
                # print("tackles_interceptions: " + str(tackles_interceptions), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                duels_total = ply['statistics'][0]['duels']['total']
                if(duels_total is None):
                    duels_total = 0
                # print("duels_total: " + str(duels_total), flush=True)
                # ----------------------------------------------
                duels_won = ply['statistics'][0]['duels']['won']
                if(duels_won is None):
                    duels_won = 0
                # print("duels_won: " + str(duels_won), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                dribbles_attempts = ply['statistics'][0]['dribbles']['attempts']
                if(dribbles_attempts is None):
                    dribbles_attempts = 0
                # print("dribbles_attempts: " + str(dribbles_attempts), flush=True)
                # ----------------------------------------------
                dribbles_success = ply['statistics'][0]['dribbles']['success']
                if(dribbles_success is None):
                    dribbles_success = 0
                # print("dribbles_success: " + str(dribbles_success), flush=True)
                # ----------------------------------------------
                dribbles_past = ply['statistics'][0]['dribbles']['past']
                if(dribbles_past is None):
                    dribbles_past = 0
                # print("dribbles_past: " + str(dribbles_past), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                fouls_drawn = ply['statistics'][0]['fouls']['drawn']
                if(fouls_drawn is None):
                    fouls_drawn = 0
                # print("fouls_drawn: " + str(fouls_drawn), flush=True)
                # ----------------------------------------------
                fouls_committed = ply['statistics'][0]['fouls']['committed']
                if(fouls_committed is None):
                    fouls_committed = 0
                # print("fouls_committed: " + str(fouls_committed), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                cards_yellow = ply['statistics'][0]['cards']['yellow']
                if(cards_yellow is None):
                    cards_yellow = 0
                # print("cards_yellow: " + str(cards_yellow), flush=True)
                # ----------------------------------------------
                cards_red = ply['statistics'][0]['cards']['red']
                if(cards_red is None):
                    cards_red = 0
                # print("cards_red: " + str(cards_red), flush=True)


                # print("", flush=True) 
                # ----------------------------------------------
                penalty_won = ply['statistics'][0]['penalty']['won']
                if(penalty_won is None):
                    penalty_won = 0
                # print("penalty_won: " + str(penalty_won), flush=True)
                # ----------------------------------------------
                penalty_commited = ply['statistics'][0]['penalty']['commited']
                if(penalty_commited is None):
                    penalty_commited = 0
                # print("penalty_commited: " + str(penalty_commited), flush=True)
                # ----------------------------------------------
                penalty_scored = ply['statistics'][0]['penalty']['scored']
                if(penalty_scored is None):
                    penalty_scored = 0
                # print("penalty_scored: " + str(penalty_scored), flush=True)
                # ----------------------------------------------
                penalty_missed = ply['statistics'][0]['penalty']['missed']
                if(penalty_missed is None):
                    penalty_missed = 0
                # print("penalty_missed: " + str(penalty_missed), flush=True)
                # ----------------------------------------------
                penalty_saved = ply['statistics'][0]['penalty']['saved']
                if(penalty_saved is None):
                    penalty_saved = 0
                # print("penalty_saved: " + str(penalty_saved), flush=True)

 

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
                query += " , date " 
                query += " from football_fixtures " 
                query += " where fixtureapi_id = '"+str(DICTfixtureapi_id)+"' "   
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
                    leagueapi_id   = str(x[0])  
                    season         = str(x[1])  
                    date        = str(x[2])    
                    # ------------------------------------------------------
                # ----------------------------------------------------------  
                # ----------------------------------------------------------  















                # ----------------------------------------------------------  
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # ----------------------------------------------------------   
                query_commit = "INSERT INTO `api_football_player_analysis`( "
                # ------------------------------------------  
                query_commit += " `date`, " 
                query_commit += " `leagueapi_id`, " 
                query_commit += " `season`, " 
                query_commit += " `teamapi_id`, " 
                query_commit += " `playerapi_id`, " 
                query_commit += " `fixtureapi_id`, " 
                query_commit += " `minutes`, " 
                query_commit += " `number`, " 
                query_commit += " `position`, " 
                query_commit += " `rating`, " 
                query_commit += " `captain`, " 
                query_commit += " `substitute`, " 
                query_commit += " `offsides`, " 
                query_commit += " `shots_total`, " 
                query_commit += " `shots_on`, " 
                query_commit += " `goals_total`, " 
                query_commit += " `goals_conceded`, " 
                query_commit += " `goals_assists`, " 
                query_commit += " `goals_saves`, " 
                query_commit += " `passes_total`, " 
                query_commit += " `passes_key`, " 
                query_commit += " `passes_accuracy`, " 
                query_commit += " `tackles_total`, " 
                query_commit += " `tackles_blocks`, " 
                query_commit += " `tackles_interceptions`, " 
                query_commit += " `duels_total`, " 
                query_commit += " `duels_won`, " 
                query_commit += " `dribbles_attempts`, " 
                query_commit += " `dribbles_success`, " 
                query_commit += " `dribbles_past`, " 
                query_commit += " `fouls_drawn`, " 
                query_commit += " `fouls_committed`, " 
                query_commit += " `cards_yellow`, " 
                query_commit += " `cards_red`, " 
                query_commit += " `penalty_won`, " 
                query_commit += " `penalty_commited`, " 
                query_commit += " `penalty_scored`, " 
                query_commit += " `penalty_missed`, " 
                query_commit += " `penalty_saved`, "  
                # ------------------------------------------------------  
                query_commit += " `created_at` "   
                # ------------------------------------------------------  
                query_commit += " ) VALUES ( "
                # ------------------------------------------------------  
                query_commit += " '" + str(date) + "', "  
                query_commit += " " + str(leagueapi_id) + ", "  
                query_commit += " " + str(season) + ", "  
                query_commit += " " + str(teamapi_id) + ", "  
                query_commit += " " + str(playerapi_id) + ", "  
                query_commit += " " + str(DICTfixtureapi_id) + ", "  
                query_commit += " " + str(games_minutes) + ", "  
                query_commit += " " + str(games_number) + ", "  
                query_commit += " '" + str(games_position) + "', "  
                query_commit += " " + str(games_rating) + ", "  
                query_commit += " " + str(games_captain) + ", "  
                query_commit += " " + str(games_substitute) + ", "  
                query_commit += " " + str(offsides) + ", "  
                query_commit += " " + str(shots_total) + ", "  
                query_commit += " " + str(shots_on) + ", "  
                query_commit += " " + str(goals_total) + ", "  
                query_commit += " " + str(goals_conceded) + ", "  
                query_commit += " " + str(goals_assists) + ", "  
                query_commit += " " + str(goals_saves) + ", "  
                query_commit += " " + str(passes_total) + ", "  
                query_commit += " " + str(passes_key) + ", "  
                query_commit += " " + str(passes_accuracy) + ", "  
                query_commit += " " + str(tackles_total) + ", "  
                query_commit += " " + str(tackles_blocks) + ", "  
                query_commit += " " + str(tackles_interceptions) + ", "  
                query_commit += " " + str(duels_total) + ", "  
                query_commit += " " + str(duels_won) + ", "  
                query_commit += " " + str(dribbles_attempts) + ", "  
                query_commit += " " + str(dribbles_success) + ", "  
                query_commit += " " + str(dribbles_past) + ", "  
                query_commit += " " + str(fouls_drawn) + ", "  
                query_commit += " " + str(fouls_committed) + ", "  
                query_commit += " " + str(cards_yellow) + ", "  
                query_commit += " " + str(cards_red) + ", "  
                query_commit += " " + str(penalty_won) + ", "  
                query_commit += " " + str(penalty_commited) + ", "  
                query_commit += " " + str(penalty_scored) + ", "  
                query_commit += " " + str(penalty_missed) + ", "  
                query_commit += " " + str(penalty_saved) + ", "    
                query_commit += " current_timestamp ) "      
                # ----------------------------------------------------------   
                print(space + query_commit, flush=True)  
                # ----------------------------------------------------------   
                # ----------------------------------------------------------  
                mycursor.execute(query_commit)
                mydb.commit()   
                # ----------------------------------------------------------  
                mycursor.close()
                mydb.close()  
                # ----------------------------------------------------------  



                # ----------------------------------------------------------  
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # ----------------------------------------------------------   
                # ------------------------------------------------------
                query_commit = "UPDATE `football_fixtures` SET "
                # ------------------------------------------------------   
                query_commit += " api_fixtures_players_updated_at = now(), "
                # ------------------------------------------------------
                query_commit += " `updated_at` = now() "
                # ------------------------------------------------------
                query_commit += " where fixtureapi_id = "+str(DICTfixtureapi_id)+" "    
                query_commit += " and leagueapi_id = "+str(leagueapi_id)+" "    
                query_commit += " and season = "+str(season)+" "    
                # ------------------------------------------------------ 
                # ----------------------------------------------------------   
                print(space + query_commit, flush=True)  
                # ----------------------------------------------------------   
                # ----------------------------------------------------------  
                mycursor.execute(query_commit)
                mydb.commit()   
                # ----------------------------------------------------------  
                mycursor.close()
                mydb.close()  
                # ----------------------------------------------------------  

                
                time.sleep(1)
            # -------------------------------------------------- 
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 