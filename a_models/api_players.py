# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.api_football_player_seasons import *   
 
import pytz
utc=pytz.UTC 

import requests
import json 

def ap_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ap_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0): 
        # ------------------------------------------------------
        its_api_empty()
        # ------------------------------------------------------
    elif(counterAPI > 0):
        # ------------------------------------------------------
        aa_update_counter(space)  
        ap_response_odds(APIkey, DICT, PREP_, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------
 
def ap_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "ap_response_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/players"  
    # ----------------------------------------------------------   
    space += "__" 
    # ---------------------------------------------------------- 
    DICTleagueapi_id    = DICT['leagueapi_id'] 
    DICTseason          = DICT['season']  
    DICTpage            = DICT['page']  
    # ----------------------------------------------------------
    print(space + "leagueapi_id : " + str(DICTleagueapi_id), flush=True) 
    print(space + "season : " + str(DICTseason), flush=True) 
    print(space + "page : " + str(DICTpage), flush=True)  
    # ----------------------------------------------------------
    querystring         = {"league":DICTleagueapi_id, "season":DICTseason, "page": DICTpage}
    # ----------------------------------------------------------
    # ----------------------------------------------------------  
    headers = {
        "X-RapidAPI-Key": APIkey,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    # ----------------------------------------------------------
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------   
    total_API_response = len(data['response'])
    # ----------------------------------------------------------   
    print(space + "Total API Response(s) : " + str(total_API_response), flush=True)  
    # ----------------------------------------------------------   
    total_MAX_PAGE = data['paging']['total']
    # ----------------------------------------------------------   
    print(space + "total_MAX_PAGE : " + str(total_MAX_PAGE), flush=True)  
    # ---------------------------------------------------------- 
    counter_response = 0
    # ---------------------------------------------------------- 
    space += "__"
    counter = 0
    # ----------------------------------------------------------  
    if(total_API_response != 0):
        # ------------------------------------------------------   
        players = data['response']
        # ------------------------------------------------------ 
        for player_data in players:
            # --------------------------------------------------
            player_info     = player_data['player']
            # --------------------------------------------------
            playerapi_id        = player_info['id']
            player_name         = player_info['name']
            player_firstname    = player_info['firstname']
            player_lastname     = player_info['lastname']
            player_age          = player_info['age']
            # --------------------------------------------------
            player_birth_info       = player_info['birth'] 
            player_birth_date       = player_birth_info['date'] 
            player_birth_place      = player_birth_info['place'] 
            player_birth_country    = player_birth_info['country'] 
            # -------------------------------------------------- 
            player_nationality  = player_info['nationality']
            player_height       = player_info['height']
            player_weight       = player_info['weight']
            player_injured      = player_info['injured']
            player_photo        = player_info['photo']
            # --------------------------------------------------
            statistics          = player_data['statistics'][0]
            # --------------------------------------------------
            teamapi_id         = statistics['team']['id'] 
            # -------------------------------------------------- 
            fouls           = statistics['fouls'] 
            fouls_drawn     = fouls['drawn']
            fouls_committed = fouls['committed']
            # --------------------------------------------------
            cards           = statistics['cards'] 
            yellow_cards    = cards['yellow']
            yellowred_cards = cards['yellowred']
            red_cards       = cards['red']
            # --------------------------------------------------
            games               = statistics['games'] 
            games_appearences   = games['appearences']
            games_lineups       = games['lineups']
            games_minutes       = games['minutes']
            games_number        = games['number']
            games_position      = games['position']
            games_rating        = games['rating']
            games_captain       = games['captain']
            # --------------------------------------------------
            substitutes         = statistics['substitutes'] 
            substitutes_in       = substitutes['in']
            substitutes_out      = substitutes['out']
            substitutes_bench    = substitutes['bench']
            # --------------------------------------------------
            shots               = statistics['shots'] 
            shots_total         = shots['total']
            shots_on            = shots['on'] 
            # --------------------------------------------------
            goals               = statistics['goals'] 
            goals_total         = goals['total']
            goals_conceded      = goals['conceded']
            goals_assists       = goals['assists']
            goals_saves         = goals['saves']
            # --------------------------------------------------
            passes              = statistics['passes'] 
            passes_total        = passes['total']
            passes_key          = passes['key']
            passes_accuracy     = passes['accuracy']
            # --------------------------------------------------
            tackles                 = statistics['tackles'] 
            tackles_total           = tackles['total']
            tackles_blocks          = tackles['blocks']
            tackles_interceptions   = tackles['interceptions'] 
            # --------------------------------------------------
            duels           = statistics['duels'] 
            duels_total     = duels['total']
            duels_won       = duels['won'] 
            # --------------------------------------------------
            dribbles            = statistics['dribbles'] 
            dribbles_attempts   = dribbles['attempts']
            dribbles_success    = dribbles['success']
            dribbles_past       = dribbles['past']
            # --------------------------------------------------
            penalties           = statistics['penalty']   
            penalties_won       = penalties['won']
            penalties_commited  = penalties['commited']
            penalties_scored    = penalties['scored']
            penalties_missed    = penalties['missed']
            penalties_saved     = penalties['saved']
            # --------------------------------------------------
            # --------------------------------------------------
            update_or_insert = aFPS_update_or_insert(DICTleagueapi_id, DICTseason, teamapi_id, playerapi_id, space)
            # --------------------------------------------------
            host="localhost"
            user="root" 
            database="pr_mmbuzz_2022_06"
            mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
            mycursor = mydb.cursor()
            # --------------------------------------------------
            if(update_or_insert == 0):
                # ---------------------------------------------- 
                query_commit = "INSERT INTO `football_leagues`( "
                # ----------------------------------------------
                query_commit += " `leagueapi_id`, "
                query_commit += " `name`, "
                query_commit += " `type`, " 
                query_commit += " `country_name`, "  
                query_commit += " `logo`, "  
                # ----------------------------------------------
                query_commit += " `api_league_updated_at` "   
                # ----------------------------------------------
                query_commit += " ) VALUES ( "
                # ----------------------------------------------
                query_commit += " " + str(league_id) + ", " 
                query_commit += " '" + str(league_name).replace("'", "\\'") + "', " 
                query_commit += " '" + str(league_type) + "', " 
                query_commit += " '" + str(DICTcountry) + "', " 
                query_commit += " '" + str(league_logo).replace("'", "\\'")  + "', "  
                # ----------------------------------------------
                query_commit += " current_timestamp ) "     
                # ----------------------------------------------
                print(space + query_commit, flush=True)
                # ----------------------------------------------
                mycursor.execute(query_commit)
                mydb.commit()     
                # ----------------------------------------------
            # --------------------------------------------------
            elif(update_or_insert == 1):
                # ---------------------------------------------- 
                query_commit = "UPDATE `football_leagues` SET "
                # ---------------------------------------------- 
                query_commit += " `country_name` = '"+str(DICTcountry)+"', "
                query_commit += " `name` = '"+str(league_name).replace("'", "\\'")+"', "
                query_commit += " `type` = '"+str(league_type)+"', " 
                query_commit += " `logo` = '"+str(league_logo).replace("'", "\\'")+"', "
                # ----------------------------------------------
                query_commit += " `api_league_updated_at` = now() "
                # ----------------------------------------------
                query_commit += " where leagueapi_id = "+str(league_id)+" "    
                # ----------------------------------------------
                print(space + query_commit, flush=True) 
                # ----------------------------------------------
                mycursor.execute(query_commit)
                mydb.commit()    
                # ----------------------------------------------
            # --------------------------------------------------
            mycursor.close()
            mydb.close()  
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        # if(DICTpage <= total_MAX_PAGE):
        #     # --------------------------------------------------  
        #     DICTpage += 1
        #     # --------------------------------------------------  
        #     DICT = {
        #         'leagueapi_id' : DICTleagueapi_id,
        #         'season' : DICTseason, 
        #         'page' : DICTpage, 
        #     } 
        #     # --------------------------------------------------  
        #     PREP_ = "Null"
        #     # -------------------------------------------------- 
        #     ap_controll_match_update(DICT, PREP_, space)
        #     # --------------------------------------------------  
        # # ------------------------------------------------------  
    # ----------------------------------------------------------  
    elif(total_API_response == 0):
        # ------------------------------------------------------
        print(space + "SKIPPED because its Nothing total_API_response:" + str(total_API_response), flush=True) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------