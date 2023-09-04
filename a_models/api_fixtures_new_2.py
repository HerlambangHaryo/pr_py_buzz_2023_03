# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.fixture_statistics import *   

import pytz
utc=pytz.UTC 

import requests
import json 
 
def afN2_controll_match_update(DICT, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afN2_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space) 
        afN2_response_fixtures(DICT, ROUTES, APIkey, space)
    # ----------------------------------------------------------
  
def afN2_response_fixtures(DICT, ROUTES, APIkey, space): 
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afN2_response_fixtures()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures" 
    # ---------------------------------------------------------- 
    space += "__"
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    if(ROUTES == 'fixtureapi_id'):
        # ------------------------------------------------------ 
        DICTfixtureapi_id = DICT['fixtureapi_id']
        print(space + "fixtureapi_id : " + str(DICTfixtureapi_id), flush=True)  
        # ------------------------------------------------------   
        xROUTES = ROUTES
        print(space + "ROUTES : " + xROUTES, flush=True) 
        # ------------------------------------------------------ 
        querystring = {"id":DICTfixtureapi_id}  
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
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
            counter += 1
            # ------------------------------------------------------------------------------------ # Initialize
            # --------------------------------------------------
            print(space , flush=True) 
            # ----------------------------------------------------------   
            fixture_date_now    = datetime.fromisoformat(row['fixture']['date']) 
            fixture_status      = str(row['fixture']['status']['long'])  
            # ----------------------------------------------------------    
            leagueapi_id        = str(row['league']['id']) 
            leagueapi_season        = str(row['league']['season']) 
            # --------------------------------------------------
            word = space + " ["+ str(counter) + "/" 
            word += str(total_rows) + "] "
            word += " __ " + str(leagueapi_id)
            word +=  " __ " + str(fixture_date_now)
            print(word, flush=True) 
            # ----------------------------------------------------------   
            print(space, flush=True) 
            # ----------------------------------------------------------   
            teams_homeapi_id      = str(row['teams']['home']['id'])  
            print(space + "teams_homeapi_id: " + teams_homeapi_id, flush=True) 
            # ----------------------------------------------------------    
            teams_awayapi_id      = str(row['teams']['away']['id'])  
            print(space + "teams_awayapi_id: " + teams_awayapi_id, flush=True) 
            # ----------------------------------------------------------   
            # --------------------------------------------------
            check_cfs = afN2_check_fixture_statistics(leagueapi_id, leagueapi_season, DICTfixtureapi_id, space) 
            # ----------------------------------------------------------   
            afN2_process_api(check_cfs, teams_homeapi_id, teams_awayapi_id, 
                                row['goals'], row['score'],
                                row['lineups'], row['statistics'], 
                                leagueapi_id, 
                                leagueapi_season, 
                                DICTfixtureapi_id, 
                                fixture_status,
                                space)
            # ----------------------------------------------------------    
    # ----------------------------------------------------------
    elif(len(d['response']) == 0):
        print(space + "SKIPPED because its Nothing", flush=True) 
        # ------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------


def afN2_check_fixture_statistics(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afN2_check_fixture_statistics()", flush=True)
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
    query += " *  " 
    query += " from football_statistics " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "
    query += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------     
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "total_rows: " + str(total_rows), flush=True)
    # ----------------------------------------------------------
    return total_rows     
    # ----------------------------------------------------------  
    
def afN2_process_api(check_cfs, teams_homeapi_id, teams_awayapi_id, 
                        array_goals, array_score, 
                        array_lineups, array_statistics, 
                        leagueapi_id,
                        season,
                        fixtureapi_id,
                        fixture_status,
                        space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "afN2_process_api()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------    
    print(space + "teams_homeapi_id: " + str(teams_homeapi_id), flush=True)
    print(space + "teams_awayapi_id: " + str(teams_awayapi_id), flush=True)
    # ----------------------------------------------------------  
    lineups_coach_homeapi_id    = "Null"
    lineups_coach_home_name     = "Null"
    lineups_coach_home_photo    = "Null"
    lineups_formation_home      = "Null" 
    # ----------------------------------------------------------  
    lineups_coach_awayapi_id    = "Null"
    lineups_coach_away_name     = "Null"
    lineups_coach_away_photo    = "Null"
    lineups_formation_away      = "Null"
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
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
    # ----------------------------------------------------------   
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
    # ----------------------------------------------------------   
    print(space, flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------- array_goals  
    goals_home    = array_goals['home']; 
    goals_away    = array_goals['away']; 
    # ----------------------------------------------------------  
    if( goals_home is None): 
        goals_home = "Null" 
    else :  
        goals_home    = str(array_goals['home'])
    print(space + "goals_home: " + goals_home, flush=True) 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    if( goals_away is None):
        goals_away = "Null"
    else : 
        goals_away    = str(array_goals['away'])
    print(space + "goals_away: " + goals_away, flush=True) 
    # ----------------------------------------------------------  
    print(space, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ---------------------------------------------- array_score  
    score_halftime_home    = array_score['halftime']['home']; 
    if( score_halftime_home is None):
        score_halftime_home = "Null"
    else : 
        score_halftime_home    = str(array_score['halftime']['home'])
    # ----------------------------------------------------------   
    print(space + "score_halftime_home: " + score_halftime_home, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_halftime_away    = array_score['halftime']['away'];  
    if( score_halftime_away is None):
        score_halftime_away = "Null"
    else : 
        score_halftime_away    = str(array_score['halftime']['away'])
    # ----------------------------------------------------------   
    print(space + "score_halftime_away: " + score_halftime_away, flush=True) 
    # ----------------------------------------------------------   
    print(space, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    if( score_halftime_home is None):
        score_halftime_home = "Null"
        score_secondtime_home = "Null"
    else : 
        score_halftime_home    = str(array_score['halftime']['home'])
        if(fixture_status == "Match Finished"):
            score_secondtime_home = str(array_goals['home'] - array_score['halftime']['home'])
        else : 
            score_secondtime_home = "Null"
    # ----------------------------------------------------------   
    print(space + "score_secondtime_home: " + score_secondtime_home, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    if( score_halftime_away is None):
        score_halftime_away = "Null"
        score_secondtime_away = "Null"
    else : 
        score_halftime_away    = str(array_score['halftime']['away'])
        if(fixture_status == "Match Finished"):
            score_secondtime_away = str(array_goals['away'] - array_score['halftime']['away'])
        else : 
            score_secondtime_away = "Null"
    # ----------------------------------------------------------   
    print(space + "score_secondtime_away: " + score_secondtime_away, flush=True) 
    # ----------------------------------------------------------   
    print(space, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_fulltime_home    = array_score['fulltime']['home']; 
    if( score_fulltime_home is None):
        score_fulltime_home = "Null"
    else : 
        score_fulltime_home    = str(array_score['fulltime']['home'])
    # ----------------------------------------------------------   
    print(space + "score_fulltime_home: " + score_fulltime_home, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_fulltime_away    = array_score['fulltime']['away']
    if( score_fulltime_away is None):
        score_fulltime_away = "Null"
    else : 
        score_fulltime_away    = str(array_score['fulltime']['away'])
    # ----------------------------------------------------------   
    print(space + "score_fulltime_away: " + score_fulltime_away, flush=True) 
    # ----------------------------------------------------------   
    print(space, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_extratime_home   = array_score['extratime']['home']
    if( score_extratime_home is None):
        score_extratime_home = "Null"
    else :
        score_extratime_home    = str(array_score['extratime']['home'])
    # ----------------------------------------------------------   
    print(space + "score_extratime_home: " + score_extratime_home, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_extratime_away   = array_score['extratime']['away']
    if( score_extratime_away is None):
        score_extratime_away = "Null"
    else :
        score_extratime_away    = str(array_score['extratime']['away'])
    # ----------------------------------------------------------   
    print(space + "score_extratime_away: " + score_extratime_away, flush=True) 
    # ----------------------------------------------------------   
    print(space, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_penalty_home     = array_score['penalty']['home']
    if( score_penalty_home is None):
        score_penalty_home = "Null"
    else :
        score_penalty_home    = str(array_score['penalty']['home'])
    # ----------------------------------------------------------   
    print(space + "score_penalty_home: " + score_penalty_home, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    score_penalty_away     = array_score['penalty']['away']
    if( score_penalty_away is None):
        score_penalty_away = "Null"
    else :
        score_penalty_away    = str(array_score['penalty']['away'])
    # ----------------------------------------------------------   
    print(space + "score_penalty_away: " + score_penalty_away, flush=True) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # -------------------------------------------- array_lineups  
    for rwln in array_lineups:
        # ------------------------------------------------------ 
        team_id = rwln['team']['id']
        print(space + "team_id: " + str(team_id), flush=True)
        # ------------------------------------------------------ 
        if(str(teams_homeapi_id) == str(team_id)):   
            # --------------------------------------------------
            try:  
                lineups_coach_homeapi_id = str(rwln['coach']['id']) 
            except KeyError:  
                lineups_coach_homeapi_id = "Null"  
            print(space + "lineups_coach_homeapi_id: " + lineups_coach_homeapi_id, flush=True) 
            # ----------------------------------------------------------   
            # ----------------------------------------------------------    
            try:  
                lineups_formation_home = rwln['formation']  
            except KeyError:  
                lineups_formation_home = "Null" 
            print(space + "lineups_formation_home: " + lineups_formation_home, flush=True) 
            # ----------------------------------------------------------    
        # ------------------------------------------------------   
        if(str(teams_awayapi_id) == str(team_id)):  
            # ----------------------------------------------------------   
            try: 
                lineups_coach_awayapi_id = str(rwln['coach']['id'])
            except KeyError: 
                lineups_coach_awayapi_id = "Null" 
            print(space + "lineups_coach_awayapi_id: " + lineups_coach_awayapi_id, flush=True) 
            # ------------------------------------------
            # ------------------------------------------ 
            try: 
                lineups_formation_away = rwln['formation'] 
            except KeyError: 
                lineups_formation_away = "Null" 
            print(space + "lineups_formation_away: " + lineups_formation_away, flush=True)  
            # ----------------------------------------------------------    
            # ----------------------------------------------------------    
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        print(space, flush=True)  
        # ------------------------------------------------------ 
    # ----------------------------------------------------------
    # ----------------------------------------- array_statistics  
    for rwst in array_statistics:
        # ------------------------------------------------------ 
        team_id = rwst['team']['id'] 
        print(space + "team_id: " + str(team_id), flush=True)
        # ------------------------------------------------------ 
        if(str(teams_homeapi_id) == str(team_id)):   
            # ----------------------------------------------------------    
            for rwstst in rwst['statistics']: 
                # ----------------------------------------------  
                if(rwstst['type'] == 'Shots on Goal'):
                    if( rwstst['value'] is None):
                        shots_on_goal_home = "Null"
                    else: 
                        shots_on_goal_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_on_goal_home: " + shots_on_goal_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------  
                elif(rwstst['type'] == 'Shots off Goal'): 
                    if( rwstst['value'] is None):
                        shots_off_goal_home = "Null"
                    else: 
                        shots_off_goal_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_off_goal_home: " + shots_off_goal_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Total Shots'): 
                    if( rwstst['value'] is None):
                        total_shots_home = "Null"
                    else: 
                        total_shots_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "total_shots_home: " + total_shots_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Blocked Shots'): 
                    if( rwstst['value'] is None):
                        blocked_shots_home = "Null"
                    else: 
                        blocked_shots_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "blocked_shots_home: " + blocked_shots_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ---------------------------------------------- 
                elif(rwstst['type'] == 'Shots insidebox'): 
                    if( rwstst['value'] is None):
                        shots_inside_box_home = "Null"
                    else: 
                        shots_inside_box_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_inside_box_home: " + shots_inside_box_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Shots outsidebox'): 
                    if( rwstst['value'] is None):
                        shots_outside_box_home = "Null"
                    else: 
                        shots_outside_box_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_outside_box_home: " + shots_outside_box_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Fouls'): 
                    if( rwstst['value'] is None):
                        fouls_home = "Null"
                    else: 
                        fouls_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "fouls_home: " + fouls_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Corner Kicks'): 
                    if( rwstst['value'] is None):
                        corner_kicks_home = "Null"
                    else: 
                        corner_kicks_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "corner_kicks_home: " + corner_kicks_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Offsides'): 
                    if( rwstst['value'] is None):
                        offsides_home = "Null"
                    else:
                        offsides_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "offsides_home: " + offsides_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Ball Possession'): 
                    if( rwstst['value'] is None):
                        ball_possession_home = "Null"
                    else: 
                        ball_possession_home = str(rwstst['value'].replace("%", ""))
                    # ------------------------------------------  
                    print(space + "ball_possession_home: " + ball_possession_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Yellow Cards'): 
                    if( rwstst['value'] is None):
                        yellow_cards_home = "Null"
                    else:
                        yellow_cards_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "yellow_cards_home: " + yellow_cards_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Red Cards'): 
                    if( rwstst['value'] is None):
                        red_cards_home = "Null"
                    else:
                        red_cards_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "red_cards_home: " + red_cards_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Goalkeeper Saves'): 
                    if( rwstst['value'] is None):
                        goalkeeper_saves_home = "Null"
                    else: 
                        goalkeeper_saves_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "goalkeeper_saves_home: " + goalkeeper_saves_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Total passes'): 
                    if( rwstst['value'] is None):
                        total_passess_home = "Null"
                    else: 
                        total_passess_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "total_passess_home: " + total_passess_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Passes accurate'): 
                    if( rwstst['value'] is None):
                        passess_accurate_home = "Null"
                    else: 
                        passess_accurate_home = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "passess_accurate_home: " + passess_accurate_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Passes %'): 
                    if( rwstst['value'] is None):
                        passess_home = "Null"
                    else: 
                        passess_home = str(rwstst['value'].replace("%", ""))
                    # ------------------------------------------  
                    print(space + "passess_home: " + passess_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'expected_goals'): 
                    if( rwstst['value'] is None):
                        expected_goals_home = "Null"
                    else: 
                        expected_goals_home = str(rwstst['value'])
                    # ------------------------------------------  
                    print(space + "expected_goals_home: " + expected_goals_home, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
        # ------------------------------------------------------  
        if(str(teams_awayapi_id) == str(team_id)):    
            # ----------------------------------------------------------    
            for rwstst in rwst['statistics']: 
                # ----------------------------------------------
                if(rwstst['type'] == 'Shots on Goal'):
                    if( rwstst['value'] is None):
                        shots_on_goal_away = "Null"
                    else: 
                        shots_on_goal_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_on_goal_away: " + shots_on_goal_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Shots off Goal'): 
                    if( rwstst['value'] is None):
                        shots_off_goal_away = "Null"
                    else: 
                        shots_off_goal_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_off_goal_away: " + shots_off_goal_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Total Shots'): 
                    if( rwstst['value'] is None):
                        total_shots_away = "Null"
                    else: 
                        total_shots_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "total_shots_away: " + total_shots_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Blocked Shots'): 
                    if( rwstst['value'] is None):
                        blocked_shots_away = "Null"
                    else: 
                        blocked_shots_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "blocked_shots_away: " + blocked_shots_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Shots insidebox'): 
                    if( rwstst['value'] is None):
                        shots_inside_box_away = "Null"
                    else: 
                        shots_inside_box_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_inside_box_away: " + shots_inside_box_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Shots outsidebox'): 
                    if( rwstst['value'] is None):
                        shots_outside_box_away = "Null"
                    else: 
                        shots_outside_box_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "shots_outside_box_away: " + shots_outside_box_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Fouls'): 
                    if( rwstst['value'] is None):
                        fouls_away = "Null"
                    else: 
                        fouls_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "fouls_away: " + fouls_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Corner Kicks'): 
                    if( rwstst['value'] is None):
                        corner_kicks_away = "Null"
                    else: 
                        corner_kicks_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "corner_kicks_away: " + corner_kicks_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Offsides'): 
                    if( rwstst['value'] is None):
                        offsides_away = "Null"
                    else:
                        offsides_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "offsides_away: " + offsides_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Ball Possession'): 
                    if( rwstst['value'] is None):
                        ball_possession_away = "Null"
                    else: 
                        ball_possession_away = str(rwstst['value'].replace("%", ""))
                    # ------------------------------------------  
                    print(space + "ball_possession_away: " + ball_possession_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Yellow Cards'): 
                    if( rwstst['value'] is None):
                        yellow_cards_away = "Null"
                    else:
                        yellow_cards_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "yellow_cards_away: " + yellow_cards_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Red Cards'): 
                    if( rwstst['value'] is None):
                        red_cards_away = "Null"
                    else:
                        red_cards_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "red_cards_away: " + red_cards_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Goalkeeper Saves'): 
                    if( rwstst['value'] is None):
                        goalkeeper_saves_away = "Null"
                    else: 
                        goalkeeper_saves_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "goalkeeper_saves_away: " + goalkeeper_saves_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Total passes'): 
                    if( rwstst['value'] is None):
                        total_passess_away = "Null"
                    else: 
                        total_passess_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "total_passess_away: " + total_passess_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Passes accurate'): 
                    if( rwstst['value'] is None):
                        passess_accurate_away = "Null"
                    else: 
                        passess_accurate_away = str(rwstst['value']) 
                    # ------------------------------------------  
                    print(space + "passess_accurate_away: " + passess_accurate_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'Passes %'): 
                    if( rwstst['value'] is None):
                        passess_away = "Null"
                    else: 
                        passess_away = str(rwstst['value'].replace("%", ""))
                    # ------------------------------------------  
                    print(space + "passess_away: " + passess_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
                elif(rwstst['type'] == 'expected_goals'): 
                    if( rwstst['value'] is None):
                        expected_goals_away = "Null"
                    else: 
                        expected_goals_away = str(rwstst['value'])
                    # ------------------------------------------  
                    print(space + "expected_goals_away: " + expected_goals_away, flush=True) 
                    # ------------------------------------------  
                    # ------------------------------------------  
                # ----------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------
    if(check_cfs == 0):
        # ------------------------------------------------------  
        query_commit = "INSERT INTO `football_statistics`( "
        # ------------------------------------------------------  
        query_commit += " `fixture_status`, "
        query_commit += " `teams_homeapi_id`, "
        query_commit += " `teams_awayapi_id`, "
        query_commit += " `goals_home`, "
        query_commit += " `goals_away`, "
        query_commit += " `score_halftime_home`, "
        query_commit += " `score_halftime_away`, "
        query_commit += " `score_secondtime_home`, "
        query_commit += " `score_secondtime_away`, "
        query_commit += " `score_fulltime_home`, "
        query_commit += " `score_fulltime_away`, "
        query_commit += " `score_extratime_home`, "
        query_commit += " `score_extratime_away`, "
        query_commit += " `score_penalty_home`, "
        query_commit += " `score_penalty_away`, "
        query_commit += " `lineups_coach_homeapi_id`, "
        query_commit += " `lineups_coach_awayapi_id`, "
        query_commit += " `lineups_formation_home`, "
        query_commit += " `lineups_formation_away`, "
        query_commit += " `shots_on_goal_home`, "
        query_commit += " `shots_on_goal_away`, "
        query_commit += " `shots_off_goal_home`, "
        query_commit += " `shots_off_goal_away`, "
        query_commit += " `total_shots_home`, "
        query_commit += " `total_shots_away`, "
        query_commit += " `blocked_shots_home`, "
        query_commit += " `blocked_shots_away`, "
        query_commit += " `shots_inside_box_home`, "
        query_commit += " `shots_inside_box_away`, "
        query_commit += " `shots_outside_box_home`, "
        query_commit += " `shots_outside_box_away`, "
        query_commit += " `fouls_home`, "
        query_commit += " `fouls_away`, "
        query_commit += " `corner_kicks_home`, "
        query_commit += " `corner_kicks_away`, "
        query_commit += " `offsides_home`, "
        query_commit += " `offsides_away`, "
        query_commit += " `ball_possession_home`, "
        query_commit += " `ball_possession_away`, "
        query_commit += " `yellow_cards_home`, "
        query_commit += " `yellow_cards_away`, "
        query_commit += " `red_cards_home`, "
        query_commit += " `red_cards_away`, "
        query_commit += " `goalkeeper_saves_home`, "
        query_commit += " `goalkeeper_saves_away`, "
        query_commit += " `total_passess_home`, "
        query_commit += " `total_passess_away`, "
        query_commit += " `passess_accurate_home`, "
        query_commit += " `passess_accurate_away`, "
        query_commit += " `passess_home`, "
        query_commit += " `passess_away`, "
        query_commit += " `expected_goals_home`, "
        query_commit += " `expected_goals_away`, "
        # ------------------------------------------------------   
        query_commit += " `leagueapi_id`, "
        query_commit += " `season`, "
        query_commit += " `fixtureapi_id`, " 
        # ------------------------------------------------------   
        query_commit += " `created_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------  
        query_commit += " '" + str(fixture_status) + "', "
        query_commit += " '" + str(teams_homeapi_id) + "', "
        query_commit += " '" + str(teams_awayapi_id) + "', "
        query_commit += " '" + str(goals_home) + "', "
        query_commit += " '" + str(goals_away) + "', "
        query_commit += " '" + str(score_halftime_home) + "', "
        query_commit += " '" + str(score_halftime_away) + "', "
        query_commit += " '" + str(score_secondtime_home) + "', "
        query_commit += " '" + str(score_secondtime_away) + "', "
        query_commit += " '" + str(score_fulltime_home) + "', "
        query_commit += " '" + str(score_fulltime_away) + "', "
        query_commit += " '" + str(score_extratime_home) + "', "
        query_commit += " '" + str(score_extratime_away) + "', "
        query_commit += " '" + str(score_penalty_home) + "', "
        query_commit += " '" + str(score_penalty_away) + "', "
        query_commit += " '" + str(lineups_coach_homeapi_id) + "', "
        query_commit += " '" + str(lineups_coach_awayapi_id) + "', "
        query_commit += " '" + str(lineups_formation_home) + "', "
        query_commit += " '" + str(lineups_formation_away) + "', "
        query_commit += " '" + str(shots_on_goal_home) + "', "
        query_commit += " '" + str(shots_on_goal_away) + "', "
        query_commit += " '" + str(shots_off_goal_home) + "', "
        query_commit += " '" + str(shots_off_goal_away) + "', "
        query_commit += " '" + str(total_shots_home) + "', "
        query_commit += " '" + str(total_shots_away) + "', "
        query_commit += " '" + str(blocked_shots_home) + "', "
        query_commit += " '" + str(blocked_shots_away) + "', "
        query_commit += " '" + str(shots_inside_box_home) + "', "
        query_commit += " '" + str(shots_inside_box_away) + "', "
        query_commit += " '" + str(shots_outside_box_home) + "', "
        query_commit += " '" + str(shots_outside_box_away) + "', "
        query_commit += " '" + str(fouls_home) + "', "
        query_commit += " '" + str(fouls_away) + "', "
        query_commit += " '" + str(corner_kicks_home) + "', "
        query_commit += " '" + str(corner_kicks_away) + "', "
        query_commit += " '" + str(offsides_home) + "', "
        query_commit += " '" + str(offsides_away) + "', "
        query_commit += " '" + str(ball_possession_home) + "', "
        query_commit += " '" + str(ball_possession_away) + "', "
        query_commit += " '" + str(yellow_cards_home) + "', "
        query_commit += " '" + str(yellow_cards_away) + "', "
        query_commit += " '" + str(red_cards_home) + "', "
        query_commit += " '" + str(red_cards_away) + "', "
        query_commit += " '" + str(goalkeeper_saves_home) + "', "
        query_commit += " '" + str(goalkeeper_saves_away) + "', "
        query_commit += " '" + str(total_passess_home) + "', "
        query_commit += " '" + str(total_passess_away) + "', "
        query_commit += " '" + str(passess_accurate_home) + "', "
        query_commit += " '" + str(passess_accurate_away) + "', "
        query_commit += " '" + str(passess_home) + "', "
        query_commit += " '" + str(passess_away) + "', "
        query_commit += " '" + str(expected_goals_home) + "', "
        query_commit += " '" + str(expected_goals_away) + "', "
        # ------------------------------------------------------   
        query_commit += " '" + str(leagueapi_id) + "', "
        query_commit += " '" + str(season) + "', "
        query_commit += " '" + str(fixtureapi_id) + "', " 
        # ------------------------------------------------------  
        query_commit += " current_timestamp "    
        # ------------------------------------------------------  
        query_commit += " ) "
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        print(space + query_commit, flush=True)
        # ------------------------------------------------------
        print(space + "football_statistics INSERT", flush=True)
        # ------------------------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()      
        # ------------------------------------------------------
        mycursor.close()
        mydb.close()  
        # ------------------------------------------------------  
    elif(check_cfs == 1):
        # ------------------------------------------------------  
        query_commit = "UPDATE `football_statistics` SET " 
        # ------------------------------------------------------
        query_commit += " fixture_status = '"+ str(fixture_status) +"', "
        # ------------------------------------------------------
        query_commit += " teams_homeapi_id = '"+ str(teams_homeapi_id) +"', "
        query_commit += " teams_awayapi_id = '"+ str(teams_awayapi_id) +"', "
        # ------------------------------------------------------
        query_commit += " goals_home = '"+ str(goals_home) +"', "
        query_commit += " goals_away = '"+ str(goals_away) +"', "
        # ------------------------------------------------------
        query_commit += " score_halftime_home = '"+ str(score_halftime_home) +"', "
        query_commit += " score_halftime_away = '"+ str(score_halftime_away) +"', "
        query_commit += " score_secondtime_home = '"+ str(score_secondtime_home) +"', "
        query_commit += " score_secondtime_away = '"+ str(score_secondtime_away) +"', "
        query_commit += " score_fulltime_home = '"+ str(score_fulltime_home) +"', "
        query_commit += " score_fulltime_away = '"+ str(score_fulltime_away) +"', "
        query_commit += " score_extratime_home = '"+ str(score_extratime_home) +"', "
        query_commit += " score_extratime_away = '"+ str(score_extratime_away) +"', "
        query_commit += " score_penalty_home = '"+ str(score_penalty_home) +"', "
        query_commit += " score_penalty_away = '"+ str(score_penalty_away) +"', "
        # ------------------------------------------------------
        query_commit += " lineups_coach_homeapi_id = '"+ str(lineups_coach_homeapi_id) +"', "
        query_commit += " lineups_coach_awayapi_id = '"+ str(lineups_coach_awayapi_id) +"', "
        query_commit += " lineups_formation_home = '"+ str(lineups_formation_home) +"', "
        query_commit += " lineups_formation_away = '"+ str(lineups_formation_away) +"', "
        # ------------------------------------------------------
        query_commit += " shots_on_goal_home = '"+ str(shots_on_goal_home) +"', "
        query_commit += " shots_on_goal_away = '"+ str(shots_on_goal_away) +"', "
        query_commit += " shots_off_goal_home = '"+ str(shots_off_goal_home) +"', "
        query_commit += " shots_off_goal_away = '"+ str(shots_off_goal_away) +"', "
        query_commit += " total_shots_home = '"+ str(total_shots_home) +"', "
        query_commit += " total_shots_away = '"+ str(total_shots_away) +"', "
        query_commit += " blocked_shots_home = '"+ str(blocked_shots_home) +"', "
        query_commit += " blocked_shots_away = '"+ str(blocked_shots_away) +"', "
        query_commit += " shots_inside_box_home = '"+ str(shots_inside_box_home) +"', "
        query_commit += " shots_inside_box_away = '"+ str(shots_inside_box_away) +"', "
        query_commit += " shots_outside_box_home = '"+ str(shots_outside_box_home) +"', "
        query_commit += " shots_outside_box_away = '"+ str(shots_outside_box_away) +"', "
        query_commit += " fouls_home = '"+ str(fouls_home) +"', "
        query_commit += " fouls_away = '"+ str(fouls_away) +"', "
        query_commit += " corner_kicks_home = '"+ str(corner_kicks_home) +"', "
        query_commit += " corner_kicks_away = '"+ str(corner_kicks_away) +"', "
        query_commit += " offsides_home = '"+ str(offsides_home) +"', "
        query_commit += " offsides_away = '"+ str(offsides_away) +"', "
        query_commit += " ball_possession_home = '"+ str(ball_possession_home) +"', "
        query_commit += " ball_possession_away = '"+ str(ball_possession_away) +"', "
        query_commit += " yellow_cards_home = '"+ str(yellow_cards_home) +"', "
        query_commit += " yellow_cards_away = '"+ str(yellow_cards_away) +"', "
        query_commit += " red_cards_home = '"+ str(red_cards_home) +"', "
        query_commit += " red_cards_away = '"+ str(red_cards_away) +"', "
        query_commit += " goalkeeper_saves_home = '"+ str(goalkeeper_saves_home) +"', "
        query_commit += " goalkeeper_saves_away = '"+ str(goalkeeper_saves_away) +"', "
        query_commit += " total_passess_home = '"+ str(total_passess_home) +"', "
        query_commit += " total_passess_away = '"+ str(total_passess_away) +"', "
        query_commit += " passess_accurate_home = '"+ str(passess_accurate_home) +"', "
        query_commit += " passess_accurate_away = '"+ str(passess_accurate_away) +"', "
        query_commit += " passess_home = '"+ str(passess_home) +"', "
        query_commit += " passess_away = '"+ str(passess_away) +"', " 
        query_commit += " expected_goals_home = '"+ str(expected_goals_home) +"', "
        query_commit += " expected_goals_away = '"+ str(expected_goals_away) +"', "
        # ------------------------------------------------------
        query_commit += " updated_at = now() "
        # ------------------------------------------------------
        query_commit += " where leagueapi_id = '"+str(leagueapi_id)+"' "
        query_commit += " and season = '"+str(season)+"' "
        query_commit += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
        # ------------------------------------------------------
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        print(space + query_commit, flush=True)
        # ------------------------------------------------------
        print(space + "football_statistics UPDATED", flush=True)
        # ------------------------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()      
        # ------------------------------------------------------
        mycursor.close()
        mydb.close()  
        # ------------------------------------------------------
    # ----------------------------------------------------------