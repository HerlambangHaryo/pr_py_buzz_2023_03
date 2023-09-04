# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.football_venues import *   
from a_models.football_coaches import *   
from a_models.football_teams import *   

import pytz
utc=pytz.UTC 

import requests
import json 
 
def a_ts_controll_match_update(DICT, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "a_ts_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space) 
        a_ts_response_fixtures(DICT, ROUTES, APIkey, space)
    # ----------------------------------------------------------
  
def a_ts_response_fixtures(DICT, ROUTES, APIkey, space): 
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "a_ts_response_fixtures()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures" 
    # ---------------------------------------------------------- 
    space += "__"
    # ----------------------------------------------------------  
    DICTfixtureapi_id = DICT['fixtureapi_id']
    print(space + "fixtureapi_id : " + str(DICTfixtureapi_id), flush=True)  
    # ----------------------------------------------------------   
    DICTfixture_updated_at = DICT['fixture_updated_at']
    print(space + "fixture_updated_at : " + str(DICTfixture_updated_at), flush=True)   
    # ----------------------------------------------------------   
    xROUTES = ROUTES
    print(space + "ROUTES : " + xROUTES, flush=True) 
    # ----------------------------------------------------------   
    querystring = {"id":DICTfixtureapi_id}  
    # ----------------------------------------------------------   
    update_or_insert = 1 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    headers = {
        "X-RapidAPI-Key": APIkey,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    # ----------------------------------------------------------
    response = requests.request("GET", url, headers=headers, params=querystring)
    d = json.loads(response.text)
    # ----------------------------------------------------------    
    try:  
        # ------------------------------------------------------   
        space += "__"
        # ------------------------------------------------------  
        print(space + "Total API Response(s) : " + str(len(d['response'])), flush=True) 
        # ------------------------------------------------------
        counter_response = 0
        total_rows = len(d['response'])
        # ------------------------------------------------------
        space += "__"
        counter = 0
        # ------------------------------------------------------ 
        if(len(d['response']) != 0):
            # --------------------------------------------------
            for row in d['response']:
                # ------------------------------------------
                counter += 1   
                # ------------------------------------------ 
                shots_on_goal_home      = "Null"
                shots_off_goal_home     = "Null"
                total_shots_home        = "Null"
                blocked_shots_home      = "Null"
                shots_inside_box_home   = "Null"
                shots_outside_box_home  = "Null"
                fouls_home              = "Null"
                corner_kicks_home       = "Null"
                offsides_home           = "Null"
                ball_possession_home    = "Null"
                yellow_cards_home       = "Null"
                red_cards_home          = "Null"
                goalkeeper_saves_home   = "Null"
                total_passess_home      = "Null"
                passess_accurate_home   = "Null"
                passess_home            = "Null"    
                expected_goals_home     = "Null"    
                # ------------------------------------------
                shots_on_goal_away      = "Null"
                shots_off_goal_away     = "Null"
                total_shots_away        = "Null"
                blocked_shots_away      = "Null"
                shots_inside_box_away   = "Null"
                shots_outside_box_away  = "Null"
                fouls_away              = "Null"
                corner_kicks_away       = "Null"
                offsides_away           = "Null"
                ball_possession_away    = "Null"
                yellow_cards_away       = "Null"
                red_cards_away          = "Null"
                goalkeeper_saves_away   = "Null"
                total_passess_away      = "Null"
                passess_accurate_away   = "Null"
                passess_away            = "Null"    
                expected_goals_away     = "Null"    
                # ------------------------------------------
                lineups_coach_homeapi_id    = "Null"
                lineups_coach_home_name     = "Null"
                lineups_coach_home_photo    = "Null"
                lineups_formation_home      = "Null"
                # ------------------------------------------
                lineups_coach_awayapi_id    = "Null"
                lineups_coach_away_name     = "Null"
                lineups_coach_away_photo    = "Null"
                lineups_formation_away      = "Null"
                # ------------------------------------------   
                # ------------------------------------------ 
                fixtureapi_id     = str(row['fixture']['id'])  
                fixture_date_now  = datetime.fromisoformat(row['fixture']['date'])
                fixture_date      = str(fixture_date_now)
                # ------------------------------------------ 
                fixture_status     = str(row['fixture']['status']['long'])  
                leagueapi_id       = str(row['league']['id'])
                season             = str(row['league']['season'])
                xround             = str(row['league']['round'].replace("'", "\\'")) 
                # ------------------------------------------ 
                word = space + " ["+ str(counter) + "/" 
                word += str(total_rows) + "] "
                word += "fixture_status: " +str(fixture_status) + " __ " + str(leagueapi_id)
                word +=  " __ " + str(fixture_date_now)
                print(word, flush=True) 
                # ------------------------------------------ 
                referee    = row['fixture']['referee']; 
                if( referee is None):
                    referee = "Null"
                else : 
                    referee    = "'" + str(row['fixture']['referee'].replace("'", "\\'")) + "'"
                # ------------------------------------------ 
                venueapi_id        = row['fixture']['venue']['id'] 
                if( venueapi_id is None):
                    venueapi_id = "Null"
                else : 
                    venueapi_id    = "'" + str(row['fixture']['venue']['id']) + "'"
                # ------------------------------------------ 
                venue_name        = row['fixture']['venue']['name'] 
                if( venue_name is None):
                    venue_name = "Null"
                else : 
                    venue_name    = "'" + str(row['fixture']['venue']['name'].replace("'", "\\'")) + "'"
                # ------------------------------------------ 
                venue_city        =  row['fixture']['venue']['city']
                if( venue_city is None):
                    venue_city = "Null"
                else : 
                    venue_city    = "'" + str(row['fixture']['venue']['city'].replace("'", "\\'")) + "'"
                # ------------------------------------------  
                fixture_elapsed    = row['fixture']['status']['elapsed']; 
                if( fixture_elapsed is None):
                    fixture_elapsed = "Null"
                else : 
                    fixture_elapsed    = "'" + str(row['fixture']['status']['elapsed']) + "'" 
                # ------------------------------------------ 
                teams_homeapi_id      = str(row['teams']['home']['id']) 
                teams_awayapi_id      = str(row['teams']['away']['id'])  

                teams_home_name    = str(row['teams']['home']['name'].replace("'", "\\'")) 
                teams_away_name    = str(row['teams']['away']['name'].replace("'", "\\'")) 

                teams_home_logo    = str(row['teams']['home']['logo']) 
                teams_away_logo    = str(row['teams']['away']['logo'])  
                # ------------------------------------------  
                goals_home    = row['goals']['home']; 
                if( goals_home is None):
                    goals_home = "Null"
                else : 
                    goals_home    = "'" + str(row['goals']['home']) + "'"
                # ------------------------------------------ 
                goals_away    = row['goals']['away']; 
                if( goals_away is None):
                    goals_away = "Null"
                else : 
                    goals_away    = "'" + str(row['goals']['away']) + "'"
                # ------------------------------------------ 
                score_halftime_home    = row['score']['halftime']['home']; 
                if( score_halftime_home is None):
                    score_halftime_home = "Null"
                    score_secondtime_home = "Null"
                else : 
                    score_halftime_home    = "'" + str(row['score']['halftime']['home']) + "'" 
                    if(fixture_status == "Match Finished"):
                        score_secondtime_home = "'" + str(row['goals']['home'] - row['score']['halftime']['home']) + "'"
                    else : 
                        score_secondtime_home = "Null"
                # ------------------------------------------ 
                score_halftime_away    = row['score']['halftime']['away']; 
                if( score_halftime_away is None):
                    score_halftime_away = "Null"
                    score_secondtime_away = "Null"
                else : 
                    score_halftime_away    = "'" + str(row['score']['halftime']['away']) + "'"
                    if(fixture_status == "Match Finished"):
                        score_secondtime_away = "'" + str(row['goals']['away'] - row['score']['halftime']['away']) + "'"
                    else : 
                        score_secondtime_away = "Null"
                # ------------------------------------------ 
                score_fulltime_home    = row['score']['fulltime']['home']; 
                if( score_fulltime_home is None):
                    score_fulltime_home = "Null"
                else : 
                    score_fulltime_home    = "'" + str(row['score']['fulltime']['home']) + "'"
                # ------------------------------------------ 
                score_fulltime_away    = row['score']['fulltime']['away']
                if( score_fulltime_away is None):
                    score_fulltime_away = "Null"
                else : 
                    score_fulltime_away    = "'" + str(row['score']['fulltime']['away']) + "'"
                # ------------------------------------------ 
                score_extratime_home   = row['score']['extratime']['home']
                if( score_extratime_home is None):
                    score_extratime_home = "Null"
                else :
                    score_extratime_home    = "'" + str(row['score']['extratime']['home']) + "'"
                # ------------------------------------------ 
                score_extratime_away   = row['score']['extratime']['away']
                if( score_extratime_away is None):
                    score_extratime_away = "Null"
                else :
                    score_extratime_away    = "'" + str(row['score']['extratime']['away']) + "'"
                # ------------------------------------------ 
                score_penalty_home     = row['score']['penalty']['home']
                if( score_penalty_home is None):
                    score_penalty_home = "Null"
                else :
                    score_penalty_home    = "'" + str(row['score']['penalty']['home']) + "'"
                # ------------------------------------------ 
                score_penalty_away     = row['score']['penalty']['away']
                if( score_penalty_away is None):
                    score_penalty_away = "Null"
                else :
                    score_penalty_away    = "'" + str(row['score']['penalty']['away']) + "'"
                # ------------------------------------------
                # ------------------------------------------  
                # ------------------------------------------
                # ------------------------------------------
                # ------------------------------------------
                for rwln in row['lineups']:
                    # --------------------------------------  
                    team_id = str(rwln['team']['id']) 
                    print("team_id: " + str(team_id), flush=True) 
                    # --------------------------------------  
                    if(teams_homeapi_id == team_id): 
                        # ----------------------------------
                        print("", flush=True)
                        print("ID :" + str(teams_homeapi_id), flush=True) 
                        # ----------------------------------
                        try:
                            lineups_coach_homeapi_id = rwln['coach']['id']  
                        except KeyError:
                            lineups_coach_homeapi_id = "Null" 
                        print("lineups_coach_homeapi_id :" + str(lineups_coach_homeapi_id), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        try: 
                            lineups_coach_home_name = rwln['coach']['name'] 
                        except KeyError: 
                            lineups_coach_home_name = "Null"
                        print("lineups_coach_home_name :" + str(lineups_coach_home_name), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        try:
                            coach_home_photo = rwln['coach']['photo']

                            if coach_home_photo is not None:
                                lineups_coach_home_photo = coach_home_photo.replace("'", "\\'")
                            else:
                                lineups_coach_home_photo = "Null" 
                        except KeyError:
                            lineups_coach_home_photo = "Null" 
                        print("lineups_coach_home_photo :" + str(lineups_coach_home_photo), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        if(lineups_coach_homeapi_id != "Null" and 
                            lineups_coach_home_name != "Null" and 
                            lineups_coach_home_photo != "Null" ):
                            fC_insert_new(lineups_coach_homeapi_id, lineups_coach_home_name, lineups_coach_home_photo, space) 
                        # ----------------------------------
                        # ----------------------------------
                        lineups_formation_home = rwln['formation']  
                        if( lineups_formation_home is None):
                            lineups_formation_home = "Null"
                        print("lineups_formation_home :" + str(lineups_formation_home), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                    elif(teams_awayapi_id == team_id): 
                        # ----------------------------------
                        print("", flush=True)
                        print("ID :" + str(teams_awayapi_id), flush=True) 
                        # ---------------------------------- 
                        try:
                            lineups_coach_awayapi_id = rwln['coach']['id'] 
                        except KeyError:
                            lineups_coach_awayapi_id = "Null"
                        print("lineups_coach_awayapi_id :" + str(lineups_coach_awayapi_id), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        try: 
                            lineups_coach_away_name = rwln['coach']['name'] 
                        except KeyError: 
                            lineups_coach_away_name = "Null"
                        print("lineups_coach_away_name :" + str(lineups_coach_away_name), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        try:
                            coach_away_photo = rwln['coach']['photo']

                            if coach_away_photo is not None:
                                lineups_coach_away_photo = coach_away_photo.replace("'", "\\'")
                            else:
                                lineups_coach_away_photo = "Null" 
                        except KeyError:
                            lineups_coach_away_photo = "Null" 
                        print("lineups_coach_away_photo :" + str(lineups_coach_away_photo), flush=True) 
                        # ----------------------------------
                        # ----------------------------------
                        if(lineups_coach_awayapi_id != "Null" and 
                            lineups_coach_away_name != "Null" and 
                            lineups_coach_away_photo != "Null" ):
                            fC_insert_new(lineups_coach_awayapi_id, lineups_coach_away_name, lineups_coach_away_photo, space) 
                        # ----------------------------------
                        # ----------------------------------
                        # if 'photo' in rwln:  
                        #     lineups_coach_away_photo = "Null"
                        # else: 
                        #     lineups_coach_away_photo = rwln['coach']['photo'].replace("'", "\\'")  
                        # ------------------------------------                
                        # ------------------------------------
                        lineups_formation_away = rwln['formation'] 
                        if( lineups_formation_away is None):
                            lineups_formation_away = "Null"
                        print("lineups_formation_away :" + str(lineups_formation_away), flush=True) 
                        # ----------------------------------
                        # ----------------------------------  
                # --------------------------------------   
                for rwst in row['statistics']:
                    # ----------------------------------  
                    team_id = str(rwst['team']['id']) 
                    # ----------------------------------  
                    if (teams_homeapi_id == team_id): 
                        # ------------------------------  
                        print("", flush=True)
                        # ------------------------------  
                        for rwstst in rwst['statistics']: 
                            # ------------------------------  
                            if(rwstst['type'] == 'Shots on Goal'):
                                if( rwstst['value'] is None):
                                    shots_on_goal_home = "Null"
                                else: 
                                    shots_on_goal_home = str(rwstst['value']) 
                                print("shots_on_goal_home :" + str(shots_on_goal_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Shots off Goal'): 
                                if( rwstst['value'] is None):
                                    shots_off_goal_home = "Null"
                                else: 
                                    shots_off_goal_home = str(rwstst['value']) 
                                print("shots_off_goal_home :" + str(shots_off_goal_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Total Shots'): 
                                if( rwstst['value'] is None):
                                    total_shots_home = "Null"
                                else: 
                                    total_shots_home = str(rwstst['value']) 
                                print("total_shots_home :" + str(total_shots_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Blocked Shots'): 
                                if( rwstst['value'] is None):
                                    blocked_shots_home = "Null"
                                else: 
                                    blocked_shots_home = str(rwstst['value']) 
                                print("blocked_shots_home :" + str(blocked_shots_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Shots insidebox'): 
                                if( rwstst['value'] is None):
                                    shots_inside_box_home = "Null"
                                else: 
                                    shots_inside_box_home = str(rwstst['value']) 
                                print("shots_inside_box_home :" + str(shots_inside_box_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Shots outsidebox'): 
                                if( rwstst['value'] is None):
                                    shots_outside_box_home = "Null"
                                else: 
                                    shots_outside_box_home = str(rwstst['value']) 
                                print("shots_outside_box_home :" + str(shots_outside_box_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Fouls'): 
                                if( rwstst['value'] is None):
                                    fouls_home = "Null"
                                else: 
                                    fouls_home = str(rwstst['value']) 
                                print("fouls_home :" + str(fouls_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Corner Kicks'): 
                                if( rwstst['value'] is None):
                                    corner_kicks_home = "Null"
                                else: 
                                    corner_kicks_home = str(rwstst['value']) 
                                print("corner_kicks_home :" + str(corner_kicks_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Offsides'): 
                                if( rwstst['value'] is None):
                                    offsides_home = "Null"
                                else:
                                    offsides_home = str(rwstst['value']) 
                                print("offsides_home :" + str(offsides_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Ball Possession'): 
                                if( rwstst['value'] is None):
                                    ball_possession_home = "Null"
                                else: 
                                    ball_possession_home = str(rwstst['value'].replace("%", ""))
                                print("ball_possession_home :" + str(ball_possession_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Yellow Cards'): 
                                if( rwstst['value'] is None):
                                    yellow_cards_home = "Null"
                                else:
                                    yellow_cards_home = str(rwstst['value']) 
                                print("yellow_cards_home :" + str(yellow_cards_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Red Cards'): 
                                if( rwstst['value'] is None):
                                    red_cards_home = "Null"
                                else:
                                    red_cards_home = str(rwstst['value']) 
                                print("red_cards_home :" + str(red_cards_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Goalkeeper Saves'): 
                                if( rwstst['value'] is None):
                                    goalkeeper_saves_home = "Null"
                                else: 
                                    goalkeeper_saves_home = str(rwstst['value']) 
                                print("goalkeeper_saves_home :" + str(goalkeeper_saves_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Total passes'): 
                                if( rwstst['value'] is None):
                                    total_passess_home = "Null"
                                else: 
                                    total_passess_home = str(rwstst['value']) 
                                print("total_passess_home :" + str(total_passess_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Passes accurate'): 
                                if( rwstst['value'] is None):
                                    passess_accurate_home = "Null"
                                else: 
                                    passess_accurate_home = str(rwstst['value']) 
                                print("passess_accurate_home :" + str(passess_accurate_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'Passes %'): 
                                if( rwstst['value'] is None):
                                    passess_home = "Null"
                                else: 
                                    passess_home = str(rwstst['value'].replace("%", ""))
                                print("passess_home :" + str(passess_home))
                            # ------------------------------  
                            elif(rwstst['type'] == 'expected_goals'): 
                                if( rwstst['value'] is None):
                                    expected_goals_home = "Null"
                                else:
                                    expected_goals_home = str(rwstst['value'].replace("%", ""))
                                print("expected_goals_home :" + str(expected_goals_home)) 
                            # ------------------------------
                        # ------------------------------  
                    # ----------------------------------  
                    if (teams_awayapi_id == team_id): 
                        # ------------------------------  
                        print("")
                        # ------------------------------  
                        for rwstst in rwst['statistics']: 
                            # ------------------------------  
                            if(rwstst['type'] == 'Shots on Goal'):
                                if( rwstst['value'] is None):
                                    shots_on_goal_away = "Null"
                                else: 
                                    shots_on_goal_away = str(rwstst['value']) 
                                print("shots_on_goal_away :" + str(shots_on_goal_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Shots off Goal'):
                                if( rwstst['value'] is None):
                                    shots_off_goal_away = "Null"
                                else: 
                                    shots_off_goal_away = str(rwstst['value']) 
                                print("shots_off_goal_away :" + str(shots_off_goal_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Total Shots'): 
                                if( rwstst['value'] is None):
                                    total_shots_away = "Null"
                                else:
                                    total_shots_away = str(rwstst['value']) 
                                print("total_shots_away :" + str(total_shots_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Blocked Shots'): 
                                if( rwstst['value'] is None):
                                    blocked_shots_away = "Null"
                                else:
                                    blocked_shots_away = str(rwstst['value']) 
                                print("blocked_shots_away :" + str(blocked_shots_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Shots insidebox'): 
                                if( rwstst['value'] is None):
                                    shots_inside_box_away = "Null"
                                else:
                                    shots_inside_box_away = str(rwstst['value']) 
                                print("shots_inside_box_away :" + str(shots_inside_box_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Shots outsidebox'): 
                                if( rwstst['value'] is None):
                                    shots_outside_box_away = "Null"
                                else:
                                    shots_outside_box_away = str(rwstst['value']) 
                                print("shots_outside_box_away :" + str(shots_outside_box_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Fouls'): 
                                if( rwstst['value'] is None):
                                    fouls_away = "Null"
                                else:
                                    fouls_away = str(rwstst['value']) 
                                print("fouls_away :" + str(fouls_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Corner Kicks'): 
                                if( rwstst['value'] is None):
                                    corner_kicks_away = "Null"
                                else:
                                    corner_kicks_away = str(rwstst['value']) 
                                print("corner_kicks_away :" + str(corner_kicks_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Offsides'): 
                                if( rwstst['value'] is None):
                                    offsides_away = "Null"
                                else:
                                    offsides_away = str(rwstst['value']) 
                                print("offsides_away :" + str(offsides_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Ball Possession'): 
                                if( rwstst['value'] is None):
                                    ball_possession_away = "Null"
                                else:
                                    ball_possession_away = str(rwstst['value'].replace("%", ""))
                                print("ball_possession_away :" + str(ball_possession_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Yellow Cards'): 
                                if( rwstst['value'] is None):
                                    yellow_cards_away = "Null"
                                else:
                                    yellow_cards_away = str(rwstst['value']) 
                                print("yellow_cards_away :" + str(yellow_cards_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Red Cards'): 
                                if( rwstst['value'] is None):
                                    red_cards_away = "Null"
                                else:
                                    red_cards_away = str(rwstst['value']) 
                                print("red_cards_away :" + str(red_cards_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Goalkeeper Saves'): 
                                if( rwstst['value'] is None):
                                    goalkeeper_saves_away = "Null"
                                else:
                                    goalkeeper_saves_away = str(rwstst['value']) 
                                print("goalkeeper_saves_away :" + str(goalkeeper_saves_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Total passes'): 
                                if( rwstst['value'] is None):
                                    total_passess_away = "Null"
                                else:
                                    total_passess_away = str(rwstst['value']) 
                                print("total_passess_away :" + str(total_passess_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Passes accurate'): 
                                if( rwstst['value'] is None):
                                    passess_accurate_away = "Null"
                                else:
                                    passess_accurate_away = str(rwstst['value']) 
                                print("passess_accurate_away :" + str(passess_accurate_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'Passes %'): 
                                if( rwstst['value'] is None):
                                    passess_away = "Null"
                                else:
                                    passess_away = str(rwstst['value'].replace("%", ""))
                                print("passess_away :" + str(passess_away)) 
                            # ------------------------------
                            elif(rwstst['type'] == 'expected_goals'): 
                                if( rwstst['value'] is None):
                                    expected_goals_away = "Null"
                                else:
                                    expected_goals_away = str(rwstst['value'].replace("%", ""))
                                print("expected_goals_away :" + str(expected_goals_away)) 
                            # ------------------------------  
                        # ----------------------------------
                    # --------------------------------------
                # ------------------------------------------
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor() 
                # ------------------------------------------
                check = " select * "   
                check += " from football_statistics "   
                check += " where fixtureapi_id = '" + str(fixtureapi_id) + "'"   
                check += " and leagueapi_id = '" + str(leagueapi_id) + "'"    
                check += " and season = '" + str(season) + "'"   
                # ------------------------------------------   
                mycursor = mydb.cursor()
                mycursor.execute(check)
                result_check =  mycursor.fetchall()
                # ------------------------------------------   
                word = space + "football_statistics: " + str(counter) + ". /" 
                word += fixture_status + "/ "
                word += fixtureapi_id + " / " 
                word += str(fixture_date_now) + "/ " 
                # ------------------------------------------- # football_statistics
                if(len(result_check) > 0):
                    # --------------------------------------- 
                    word += " UPDATED " 
                    # ---------------------------------------   
                    query_commit = "update football_statistics set "    
                    # ---------------------------------------       
                    query_commit += " date = '"+fixture_date+"', "  
                    query_commit += " fixture_status = '"+fixture_status+"', "  
                    # --------------------------------------- 
                    query_commit += " teams_homeapi_id = "+teams_homeapi_id+", " 
                    query_commit += " teams_awayapi_id = "+teams_awayapi_id+", " 
                    # --------------------------------------- 
                    query_commit += " goals_home = "+goals_home+", " 
                    query_commit += " goals_away = "+goals_away+", " 
                    query_commit += " score_halftime_home = "+score_halftime_home+", " 
                    query_commit += " score_halftime_away = "+score_halftime_away+", " 
                    # --------------------------------------  
                    query_commit += " score_secondtime_home = "+score_secondtime_home+", " 
                    query_commit += " score_secondtime_away = "+score_secondtime_away+", " 
                    # --------------------------------------  
                    query_commit += " score_fulltime_home = "+score_fulltime_home+", " 
                    query_commit += " score_fulltime_away = "+score_fulltime_away+", "  
                    query_commit += " score_extratime_home = "+score_extratime_home+", " 
                    query_commit += " score_extratime_away = "+score_extratime_away+", "  
                    query_commit += " score_penalty_home = "+score_penalty_home+", " 
                    query_commit += " score_penalty_away = "+score_penalty_away+", "
                    # ---------------------------------------   
                    query_commit  += " lineups_coach_homeapi_id = '" + str(lineups_coach_homeapi_id) + "', " 
                    query_commit  += " lineups_coach_awayapi_id = '" + str(lineups_coach_awayapi_id) + "', "   
                    query_commit  += " lineups_formation_home = '" + lineups_formation_home + "', " 
                    query_commit  += " lineups_formation_away = '" + lineups_formation_away + "', "  
                    # ---------------------------------------  
                    query_commit  += " shots_on_goal_home = " + shots_on_goal_home + ", " 
                    query_commit  += " shots_on_goal_away = " + shots_on_goal_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " shots_off_goal_home = " + shots_off_goal_home + ", " 
                    query_commit  += " shots_off_goal_away = " + shots_off_goal_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " total_shots_home = " + total_shots_home + ", " 
                    query_commit  += " total_shots_away = " + total_shots_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " blocked_shots_home = " + blocked_shots_home + ", " 
                    query_commit  += " blocked_shots_away = " + blocked_shots_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " shots_inside_box_home = " + shots_inside_box_home + ", " 
                    query_commit  += " shots_inside_box_away = " + shots_inside_box_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " shots_outside_box_home = " + shots_outside_box_home + ", " 
                    query_commit  += " shots_outside_box_away = " + shots_outside_box_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " fouls_home = " + fouls_home + ", " 
                    query_commit  += " fouls_away = " + fouls_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " offsides_home = " + offsides_home + ", " 
                    query_commit  += " offsides_away = " + offsides_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " ball_possession_home = " + ball_possession_home + ", " 
                    query_commit  += " ball_possession_away = " + ball_possession_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " corner_kicks_home = " + corner_kicks_home + ", " 
                    query_commit  += " corner_kicks_away = " + corner_kicks_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " yellow_cards_home = " + yellow_cards_home + ", " 
                    query_commit  += " yellow_cards_away = " + yellow_cards_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " red_cards_home = " + red_cards_home + ", " 
                    query_commit  += " red_cards_away = " + red_cards_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " goalkeeper_saves_home = " + goalkeeper_saves_home + ", " 
                    query_commit  += " goalkeeper_saves_away = " + goalkeeper_saves_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " total_passess_home = " + total_passess_home + ", " 
                    query_commit  += " total_passess_away = " + total_passess_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " passess_accurate_home = " + passess_accurate_home + ", " 
                    query_commit  += " passess_accurate_away = " + passess_accurate_away + ", " 
                    # ---------------------------------------  
                    query_commit  += " passess_home = " + passess_home + ", " 
                    query_commit  += " passess_away = " + passess_away + ", "  
                    # ---------------------------------------  
                    query_commit  += " expected_goals_home = " + expected_goals_home + ", " 
                    query_commit  += " expected_goals_away = " + expected_goals_away + ", "  
                    # ---------------------------------------  
                    query_commit += " updated_at = current_timestamp " 
                    query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "   
                    # ---------------------------------------  
                    print(query_commit)
                    # ---------------------------------------   
                    mycursor.execute(query_commit)
                    mydb.commit()  
                    # ---------------------------------------   
                    mycursor.close()
                    mydb.close()
                    # ---------------------------------------   
                    # ---------------------------------------  
                    # ---------------------------------------  
                    host="localhost"
                    user="root" 
                    database="pr_mmbuzz_2022_06"
                    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                    mycursor = mydb.cursor() 
                    # ---------------------------------------   
                    query_commit = "update football_fixtures set "    
                    # ---------------------------------------      
                    query_commit += " team_statistics_updated_at = now() "  
                    # ---------------------------------------      
                    query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "   
                    # --------------------------------------- 
                    # ---------------------------------------   
                    mycursor.execute(query_commit)
                    mydb.commit()  
                    # ---------------------------------------   
                    mycursor.close()
                    mydb.close()
                # -------------------------------------------   
                else:
                    word += " INSERTED "
                    print(word) 
                    # --------------------------------------   
                    query_commit = "INSERT INTO `football_statistics`( "
                    # --------------------------------------   
                    query_commit += " `fixtureapi_id`, " 
                    query_commit += " `leagueapi_id`, "
                    query_commit += " `season`, "
                    # --------------------------------------   
                    query_commit += " `fixture_status`, "
                    # --------------------------------------  
                    # --------------------------------------  
                    query_commit += " `teams_homeapi_id`, "
                    query_commit += " `teams_awayapi_id`, "
                    # --------------------------------------  
                    query_commit += " `goals_home`, "
                    query_commit += " `goals_away`, "
                    query_commit += " `score_halftime_home`, "
                    query_commit += " `score_halftime_away`, "
                    # --------------------------------------  
                    query_commit += " `score_secondtime_home`, "
                    query_commit += " `score_secondtime_away`, " 
                    # --------------------------------------  
                    query_commit += " `score_fulltime_home`, "
                    query_commit += " `score_fulltime_away`, "
                    query_commit += " `score_extratime_home`, "
                    query_commit += " `score_extratime_away`, "
                    query_commit += " `score_penalty_home`, "
                    query_commit += " `score_penalty_away`, "   
                    # --------------------------------------  
                    query_commit += " `created_at` "   
                    # --------------------------------------   
                    query_commit += " ) VALUES ( "
                    # --------------------------------------    
                    query_commit += " " + str(fixtureapi_id) + ", "  
                    query_commit += " " + str(leagueapi_id) + ", " 
                    query_commit += " " + str(season) + ", " 
                    # --------------------------------------  
                    query_commit += " '" + str(fixture_status) + "', " 
                    # --------------------------------------  
                    query_commit += " " + str(teams_homeapi_id) + ", " 
                    query_commit += " " + str(teams_awayapi_id) + ", " 
                    query_commit += " " + str(goals_home) + ", " 
                    query_commit += " " + str(goals_away) + ", " 
                    query_commit += " " + str(score_halftime_home) + ", " 
                    query_commit += " " + str(score_halftime_away) + ", " 
                    # --------------------------------------  
                    query_commit += " " + str(score_secondtime_home) + ", " 
                    query_commit += " " + str(score_secondtime_away) + ", "  
                    # --------------------------------------  
                    query_commit += " " + str(score_fulltime_home) + ", " 
                    query_commit += " " + str(score_fulltime_away) + ", " 
                    query_commit += " " + str(score_extratime_home) + ", " 
                    query_commit += " " + str(score_extratime_away) + ", " 
                    query_commit += " " + str(score_penalty_home) + ", " 
                    query_commit += " " + str(score_penalty_away) + ", "  
                    query_commit += " current_timestamp "    
                    # --------------------------------------  
                    query_commit += " ) "
                    # --------------------------------------  
                    mycursor.execute(query_commit)
                    mydb.commit()   
                    # --------------------------------------
                    mycursor.close()
                    mydb.close()  
                    # --------------------------------------   
                # ----------------------------------------------  
            # --------------------------------------------------
        # ------------------------------------------------------ 
        elif(len(d['response']) == 0):
            # -------------------------------------------------- 
            print(space + "SKIPPED because its Nothing", flush=True) 
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
    except KeyError: 
        # ------------------------------------------------------ 
        print("KeyErrorKeyErrorKeyError")
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
   