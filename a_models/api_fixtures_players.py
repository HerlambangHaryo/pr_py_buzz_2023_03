# Import
import mysql.connector 
from a_models.api_accounts import *      
from a_models.api_football_standings import *     
from a_models.api_teams_statistics import *   
from a_models.football_players import *   
from a_models.api_football_player_statistics import *  

import pytz
utc=pytz.UTC 

import requests
import json 
  

def aFp_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------   
    # ao_controll_match_update(DICT, PREP_, space)
    # ao_controll_match_update(date, bookmaker, season, league, 1, space)
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aFp_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0): 
        word = "# ------------- API COUNTER EMPTY ------------- #"
        print(word, flush=True)   
    elif(counterAPI > 0):
        aa_update_counter(space) 
        # ao_response_odds(APIkey, date, bookmaker, season, league, page, space)
        aFp_response_odds(APIkey, DICT, PREP_, space)
    # ----------------------------------------------------------
 
def aFp_response_odds(APIkey, DICT, PREP_, space): 
    # ao_response_odds(APIkey, date, bookmaker, season, league, page, space)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "aFp_response_odds()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    DICTfixture = DICT['fixtureapi_id']  
    DICTleagueapi_id = DICT['leagueapi_id']  
    DICTseason = DICT['season']  
    # ----------------------------------------------------------
    print(space + "DICTfixture : " + str(DICTfixture), flush=True)  
    print(space + "DICTleagueapi_id : " + str(DICTleagueapi_id), flush=True)  
    print(space + "DICTseason : " + str(DICTseason), flush=True)  
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta") 
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/players"
    # ----------------------------------------------------------
    querystring = {"fixture":DICTfixture }
    # ----------------------------------------------------------  
    headers = {
        "X-RapidAPI-Key": APIkey,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    # ----------------------------------------------------------
    response = requests.get(url, headers=headers, params=querystring) 
    d = json.loads(response.text) 
    # ----------------------------------------------------------  
    print(space + "__________________________________________________________________________", flush=True)
    # ----------------------------------------------------------  
    try:  
        total_response = len(d['response'])
        print(space + "Total API Response(s) : " + str(total_response), flush=True) 
        # ---------------------------------------------------------- 
        counter_response = 0
        # ----------------------------------------------------------   
        space += "__"
        # ----------------------------------------------------------  
        if(total_response == 0):
            aa ="oke"
        elif(total_response > 0):
            # ------------------------------------------------------ 
            data = d['response']

            counter = 0
            # Iterate through each team in the data
            for team_data in data:
                # Get the team name
                team_id = team_data['team']['id']
                team_name = team_data['team']['name']
                # print("Team Name: " + team_name)
                
                counter2 = 0
                players_list = team_data['players']
                
                for pl in players_list: 
                    
                    response_player = team_data['players'][counter2]['player'] 
                    #  
                    player_id = response_player['id']
                    # print("  player_id: " + str(player_id))    
                    #  
                    player_name = response_player['name']
                    # print("  player_name: " + str(player_name))    
                    #  
                    player_photo = response_player['photo']
                    # print("  player_photo: " + str(player_photo))
                    
                    # print("") 
                    response_games = team_data['players'][counter2]['statistics'][counter]['games']
                    #  
                    player_games_minutes = response_games['minutes']
                    # print("    player_games_minutes: " + str(player_games_minutes))
                    #  
                    player_games_number = response_games['number']
                    # print("    player_games_number: " + str(player_games_number))
                    #  
                    player_games_position = response_games['position']
                    # print("    player_games_position: " + str(player_games_position))
                    #  
                    player_games_rating = response_games['rating']
                    # print("    player_games_rating: " + str(player_games_rating))
                    #  
                    player_games_captain = response_games['captain']
                    # print("    player_games_captain: " + str(player_games_captain))
                    #  
                    player_games_substitute = response_games['substitute']
                    # print("    player_games_substitute: " + str(player_games_substitute))
                    
                    #  
                    player_offsides = team_data['players'][counter2]['statistics'][counter]['offsides']
                    # print("    player_offsides: " + str(player_offsides))
                    
                    
                    # print("")
                    response_shots = team_data['players'][counter2]['statistics'][counter]['shots']
                    #  
                    player_shots_total = response_shots['total']
                    # print("    player_shots_total: " + str(player_shots_total))
                    #  
                    player_shots_on = response_shots['on']
                    # print("    player_shots_on: " + str(player_shots_on))
                    
                    
                    # print("")
                    response_goals = team_data['players'][counter2]['statistics'][counter]['goals']
                    #  
                    player_goals_total = response_goals['total']
                    # print("    player_goals_total: " + str(player_goals_total))
                    #  
                    player_goals_conceded = response_goals['conceded']
                    # print("    player_goals_conceded: " + str(player_goals_conceded))
                    #  
                    player_goals_assists = response_goals['assists']
                    # print("    player_goals_assists: " + str(player_goals_assists))
                    #  
                    player_goals_saves = response_goals['saves']
                    # print("    player_goals_saves: " + str(player_goals_saves))
                    
                    
                    
                    # print("")
                    response_passes = team_data['players'][counter2]['statistics'][counter]['passes']
                    #  
                    player_passes_total = response_passes['total']
                    # print("    player_passes_total: " + str(player_passes_total))
                    #  
                    player_passes_key = response_passes['key']
                    # print("    player_passes_key: " + str(player_passes_key))
                    #  
                    player_passes_accuracy = response_passes['accuracy']
                    # print("    player_passes_accuracy: " + str(player_passes_accuracy))
                    
                    
                    # print("")
                    response_tackles = team_data['players'][counter2]['statistics'][counter]['tackles']
                    #  
                    player_tackles_total = response_tackles['total']
                    # print("    player_tackles_total: " + str(player_tackles_total))
                    #  
                    player_tackles_blocks = response_tackles['blocks']
                    # print("    player_tackles_blocks: " + str(player_tackles_blocks))
                    #  
                    player_tackles_interceptions = response_tackles['interceptions']
                    # print("    player_tackles_interceptions: " + str(player_tackles_interceptions))
                    
                    
                    
                    # print("")
                    response_duels = team_data['players'][counter2]['statistics'][counter]['duels']
                    #  
                    player_duels_total = response_duels['total']
                    # print("    player_duels_total: " + str(player_duels_total))
                    #  
                    player_duels_won = response_duels['won']
                    # print("    player_duels_won: " + str(player_duels_won))
                    
                    
                    
                    # print("")
                    response_dribbles = team_data['players'][counter2]['statistics'][counter]['dribbles']
                    #  
                    player_dribbles_attempts = response_dribbles['attempts']
                    # print("    player_dribbles_attempts: " + str(player_dribbles_attempts))
                    #  
                    player_dribbles_success = response_dribbles['success']
                    # print("    player_dribbles_success: " + str(player_dribbles_success))
                    #  
                    player_dribbles_past = response_dribbles['past']
                    # print("    player_dribbles_past: " + str(player_dribbles_past))
                    
                    
                    # print("")
                    response_fouls = team_data['players'][counter2]['statistics'][counter]['fouls']
                    #  
                    player_fouls_drawn = response_fouls['drawn']
                    # print("    player_fouls_drawn: " + str(player_fouls_drawn))
                    #  
                    player_fouls_committed = response_fouls['committed']
                    # print("    player_fouls_committed: " + str(player_fouls_committed))
                    
                    
                    
                    
                    # print("")
                    response_cards = team_data['players'][counter2]['statistics'][counter]['cards']
                    #  
                    player_cards_yellow = response_cards['yellow']
                    # print("    player_cards_yellow: " + str(player_cards_yellow))
                    #  
                    player_cards_red = response_cards['red']
                    # print("    player_cards_red: " + str(player_cards_red))
                    
                    
                    
                    # print("")
                    response_penalty = team_data['players'][counter2]['statistics'][counter]['penalty']
                    #  
                    player_penalty_won = response_penalty['won']
                    # print("    player_penalty_won: " + str(player_penalty_won))
                    #  
                    player_penalty_commited = response_penalty['commited']
                    # print("    player_penalty_commited: " + str(player_penalty_commited))
                    #  
                    player_penalty_scored = response_penalty['scored']
                    # print("    player_penalty_scored: " + str(player_penalty_scored))
                    #  
                    player_penalty_missed = response_penalty['missed']
                    # print("    player_penalty_missed: " + str(player_penalty_missed))
                    #  
                    player_penalty_saved = response_penalty['saved']
                    # print("    player_penalty_saved: " + str(player_penalty_saved))
                    
                     
                    counter2 += 1   

                    
                    yes_no_check    = FP_check(player_id, space)
                    # ----------------------------------------------------------
                    host="localhost"
                    user="root" 
                    database="pr_mmbuzz_2022_06"
                    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                    mycursor = mydb.cursor()
                    # ----------------------------------------------------------

                    if(yes_no_check == 1):
                        # ---------------------------------------------- 
                        query_commit = "UPDATE `football_players` SET "  
                        # ----------------------------------------------  
                        query_commit += " `name` = '"+str(player_name).replace("'", "\\'")+"', "
                        query_commit += " `photo` = '"+str(player_photo)+"', "
                        # ---------------------------------------------- 
                        query_commit += " `updated_at` = now() "
                        # ---------------------------------------------- 
                        query_commit += " where playerapi_id = "+str(player_id)+" "    
                        # ---------------------------------------------- 
                        # print(space + query_commit, flush=True)
                        print(space + "football_players UPDATED", flush=True)  
                        # ---------------------------------------------- 
                    elif(yes_no_check == 0):
                        # ---------------------------------------------- 
                        query_commit = "INSERT INTO `football_players`( "
                        # ---------------------------------------------- 
                        query_commit += " `playerapi_id`, "
                        query_commit += " `name`, "
                        query_commit += " `photo`, "
                        query_commit += " `created_at` "
                        # ----------------------------------------------   
                        query_commit += " ) VALUES ( "
                        # ----------------------------------------------   
                        query_commit += " '" + str(player_id) + "', " 
                        query_commit += " '" + str(player_name).replace("'", "\\'") + "', " 
                        query_commit += " '" + str(player_photo) + "', " 
                        query_commit += " now() ) " 
                        # ---------------------------------------------- 
                        # ---------------------------------------------- 
                        # print(space + query_commit, flush=True)
                        print(space + "football_players INSERTED", flush=True)
                    mycursor.execute(query_commit)
                    mydb.commit()   
            
             

             
                    yes_no_check    = aFPS_check(DICTleagueapi_id, DICTseason, team_id, player_id, space)
                    # ----------------------------------------------------------
                    host="localhost"
                    user="root" 
                    database="pr_mmbuzz_2022_06"
                    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                    mycursor = mydb.cursor()
                    # ----------------------------------------------------------

                    if(yes_no_check == 1):
                        # ---------------------------------------------- 
                        query_commit = "UPDATE `api_football_player_statistics` SET "  
                        # ----------------------------------------------  
                        query_commit += " `minutes` = '"+str(player_games_minutes)+"', "
                        query_commit += " `number` = '"+str(player_games_number)+"', "
                        query_commit += " `position` = '"+str(player_games_position)+"', "
                        query_commit += " `rating` = '"+str(player_games_rating)+"', "
                        query_commit += " `captain` = '"+str(player_games_captain)+"', "
                        query_commit += " `substitute` = '"+str(player_games_substitute)+"', "
                        query_commit += " `offsides` = '"+str(player_offsides)+"', "
                        query_commit += " `shots_total` = '"+str(player_shots_total)+"', "
                        query_commit += " `shots_on` = '"+str(player_shots_on)+"', "
                        query_commit += " `goals_total` = '"+str(player_goals_total)+"', "
                        query_commit += " `goals_conceded` = '"+str(player_goals_conceded)+"', "
                        query_commit += " `goals_assists` = '"+str(player_goals_assists)+"', "
                        query_commit += " `goals_saves` = '"+str(player_goals_saves)+"', "
                        query_commit += " `passes_total` = '"+str(player_passes_total)+"', "
                        query_commit += " `passes_key` = '"+str(player_passes_key)+"', "
                        query_commit += " `passes_accuracy` = '"+str(player_passes_accuracy)+"', "
                        query_commit += " `tackles_total` = '"+str(player_tackles_total)+"', "
                        query_commit += " `tackles_blocks` = '"+str(player_tackles_blocks)+"', "
                        query_commit += " `tackles_interceptions` = '"+str(player_tackles_interceptions)+"', "
                        query_commit += " `duels_total` = '"+str(player_duels_total)+"', "
                        query_commit += " `duels_won` = '"+str(player_duels_won)+"', "
                        query_commit += " `dribbles_attempts` = '"+str(player_dribbles_attempts)+"', "
                        query_commit += " `dribbles_success` = '"+str(player_dribbles_success)+"', "
                        query_commit += " `dribbles_past` = '"+str(player_dribbles_past)+"', "
                        query_commit += " `fouls_drawn` = '"+str(player_fouls_drawn)+"', "
                        query_commit += " `fouls_committed` = '"+str(player_fouls_committed)+"', "
                        query_commit += " `cards_yellow` = '"+str(player_cards_yellow)+"', "
                        query_commit += " `cards_red` = '"+str(player_cards_red)+"', "
                        query_commit += " `penalty_won` = '"+str(player_penalty_won)+"', "
                        query_commit += " `penalty_commited` = '"+str(player_penalty_commited)+"', "
                        query_commit += " `penalty_scored` = '"+str(player_penalty_scored)+"', "
                        query_commit += " `penalty_missed` = '"+str(player_penalty_missed)+"', "
                        query_commit += " `penalty_saved` = '"+str(player_penalty_saved)+"', "
                        query_commit += " `fixtureapi_id` = '"+str(DICTfixture)+"', " 
                        # ---------------------------------------------- 
                        query_commit += " `updated_at` = now() "
                        # ---------------------------------------------- 
                        # ---------------------------------------------- 
                        query_commit += " where playerapi_id = "+str(player_id)+" "    
                        query_commit += " and teamapi_id = "+str(team_id)+" "    
                        query_commit += " and leagueapi_id = "+str(DICTleagueapi_id)+" "    
                        query_commit += " and season = "+str(DICTseason)+" "      
                        # ----------------------------------------------  
                        # print(space + query_commit, flush=True)
                        print(space + "api_football_player_statistics UPDATED", flush=True)  
                        # ---------------------------------------------- 
                    elif(yes_no_check == 0):
                        # ---------------------------------------------- 
                        query_commit = "INSERT INTO `api_football_player_statistics`( "
                        # ---------------------------------------------- 
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
                        # ----------------------------------------------   
                        query_commit += " `created_at` "
                        # ----------------------------------------------   
                        query_commit += " ) VALUES ( "
                        # ----------------------------------------------   
                        query_commit += " '" + str(DICTleagueapi_id) + "', "
                        query_commit += " '" + str(DICTseason) + "', "
                        query_commit += " '" + str(team_id) + "', "
                        query_commit += " '" + str(player_id) + "', "
                        query_commit += " '" + str(DICTfixture) + "', "

                        query_commit += " '" + str(player_games_minutes) + "', "
                        query_commit += " '" + str(player_games_number) + "', "
                        query_commit += " '" + str(player_games_position) + "', "
                        query_commit += " '" + str(player_games_rating) + "', "
                        query_commit += " '" + str(player_games_captain) + "', "
                        query_commit += " '" + str(player_games_substitute) + "', "
                        query_commit += " '" + str(player_offsides) + "', "
                        query_commit += " '" + str(player_shots_total) + "', "
                        query_commit += " '" + str(player_shots_on) + "', "
                        query_commit += " '" + str(player_goals_total) + "', "
                        query_commit += " '" + str(player_goals_conceded) + "', "
                        query_commit += " '" + str(player_goals_assists) + "', "
                        query_commit += " '" + str(player_goals_saves) + "', "
                        query_commit += " '" + str(player_passes_total) + "', "
                        query_commit += " '" + str(player_passes_key) + "', "
                        query_commit += " '" + str(player_passes_accuracy) + "', "
                        query_commit += " '" + str(player_tackles_total) + "', "
                        query_commit += " '" + str(player_tackles_blocks) + "', "
                        query_commit += " '" + str(player_tackles_interceptions) + "', "
                        query_commit += " '" + str(player_duels_total) + "', "
                        query_commit += " '" + str(player_duels_won) + "', "
                        query_commit += " '" + str(player_dribbles_attempts) + "', "
                        query_commit += " '" + str(player_dribbles_success) + "', "
                        query_commit += " '" + str(player_dribbles_past) + "', "
                        query_commit += " '" + str(player_fouls_drawn) + "', "
                        query_commit += " '" + str(player_fouls_committed) + "', "
                        query_commit += " '" + str(player_cards_yellow) + "', "
                        query_commit += " '" + str(player_cards_red) + "', "
                        query_commit += " '" + str(player_penalty_won) + "', "
                        query_commit += " '" + str(player_penalty_commited) + "', "
                        query_commit += " '" + str(player_penalty_scored) + "', "
                        query_commit += " '" + str(player_penalty_missed) + "', "
                        query_commit += " '" + str(player_penalty_saved) + "', "
                        query_commit += " now() ) " 
                        # ---------------------------------------------- 
                        # ---------------------------------------------- 
                        # print(space + query_commit, flush=True)
                        print(space + "api_football_player_statistics INSERTED", flush=True)
                    mycursor.execute(query_commit)
                    mydb.commit()   
            
    # ----------------------------------------------------------  
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")