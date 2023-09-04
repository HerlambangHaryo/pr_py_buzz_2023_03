# Import
import mysql.connector 
from a_models.api_accounts import *      
from a_settings.messages import *   
from a_models.api_football_league_standings import *     
# from a_models.api_football_team_reports import *    
# from a_models.api_teams_statistics import *   

import pytz
utc=pytz.UTC 

import requests
import json 

def as_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "as_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):  
        its_api_empty() 
    elif(counterAPI > 0): 
        aa_update_counter(space)  
        as_response_odds(APIkey, DICT, PREP_, space) 
    # ---------------------------------------------------------- 
 
def as_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "as_response_odds()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    DICTleagueapi_id = DICT['leagueapi_id'] 
    DICTseason = DICT['season'] 
    # ----------------------------------------------------------
    print(space + "DICTleagueapi_id : " + str(DICTleagueapi_id), flush=True) 
    print(space + "DICTseason : " + str(DICTseason), flush=True) 
    print(space + "APIkey : " + str(APIkey), flush=True) 
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"
    # ----------------------------------------------------------
    querystring = {"league":DICTleagueapi_id, "season":DICTseason }
    # ----------------------------------------------------------  
    headers = {
        "X-RapidAPI-Key": APIkey,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    # ----------------------------------------------------------
    response = requests.get(url, headers=headers, params=querystring) 
    d = json.loads(response.text)  
    # ----------------------------------------------------------  
    try:  
        # ------------------------------------------------------ 
        total_response = len(d['response'])
        print(space + "Total API Response(s) : " + str(total_response), flush=True) 
        # ------------------------------------------------------ 
        counter_response = 0
        # ------------------------------------------------------ 
        space += "__"
        # ------------------------------------------------------  
        if(total_response == 0):
            # --------------------------------------------------
            aa ="oke"
            # --------------------------------------------------
        # ------------------------------------------------------  
        elif(total_response > 0):
            # --------------------------------------------------
            for i in d['response']: 
                # ----------------------------------------------
                print("", flush=True)
                # ----------------------------------------------
                counter_response += 1
                # ----------------------------------------------
                league_Array        = i['league'] 
                standing_Array      = league_Array['standings'][0]  
                # ----------------------------------------------
                for sa in standing_Array:
                    # ------------------------------------------
                    rank            = sa['rank'] 
                    # ------------------------------------------
                    teamapi_id      = sa['team']['id']
                    # ------------------------------------------
                    if(teamapi_id is None):
                        # --------------------------------------
                        can_we_continue = 0
                    # ------------------------------------------
                    elif(teamapi_id is not None):
                        # --------------------------------------
                        can_we_continue = 1
                        # --------------------------------------
                        print(space + "teamapi_id:" + str(teamapi_id), flush=True)
                        # --------------------------------------
                    # ------------------------------------------
                    points          = sa['points']
                    goalsDiff       = sa['goalsDiff'] 
                    group           = sa['group']
                    form            = sa['form'] 
                    status          = sa['status']
                    description     = sa['description'] 
                    # ------------------------------------------
                    update_DATE          = sa['update']  
                    # ------------------------------------------
                    all_played      = sa['all']['played']
                    all_win         = sa['all']['win']
                    all_draw        = sa['all']['draw']
                    all_lose        = sa['all']['lose'] 
                    # ------------------------------------------
                    all_goals_for               = sa['all']['goals']['for'] 
                    all_goals_againts           = sa['all']['goals']['against'] 
                    # ------------------------------------------ 
                    home_played     = sa['home']['played']
                    home_win        = sa['home']['win']
                    home_draw       = sa['home']['draw']
                    home_lose       = sa['home']['lose'] 
                    # ------------------------------------------
                    home_goals_for               = sa['home']['goals']['for'] 
                    home_goals_againts           = sa['home']['goals']['against'] 
                    # ------------------------------------------
                    away_played     = sa['away']['played']
                    away_win        = sa['away']['win']
                    away_draw       = sa['away']['draw']
                    away_lose       = sa['away']['lose'] 
                    # ------------------------------------------
                    away_goals_for               = sa['away']['goals']['for'] 
                    away_goals_againts           = sa['away']['goals']['against'] 
                    # ------------------------------------------
                    if(can_we_continue == 1):
                        # --------------------------------------------------------------------------------------------- LEAGUE STANDINGS
                        update_or_insert    = aFLS_update_or_insert(DICTleagueapi_id, DICTseason, teamapi_id, space)
                        # --------------------------------------
                        host="localhost"
                        user="root" 
                        database="pr_mmbuzz_2022_06"
                        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                        mycursor = mydb.cursor()
                        # --------------------------------------
                        if(update_or_insert == 1):
                            # ---------------------------------- 
                            query_commit = "UPDATE `api_football_league_standings` SET "
                            # ----------------------------------
                            query_commit += " `rank` = '"+str(rank)+"', "
                            query_commit += " `teamapi_id` = '"+str(teamapi_id)+"', "
                            query_commit += " `points` = '"+str(points)+"', "
                            query_commit += " `goals_diff` = '"+str(goalsDiff)+"', "
                            query_commit += " `group_status` = '"+str(status)+"', "
                            query_commit += " `form` = '"+str(form)+"', "
                            query_commit += " `status` = '"+str(status)+"', "
                            query_commit += " `description` = '"+str(description)+"', "
                            query_commit += " `played` = '"+str(all_played)+"', "
                            # ----------------------------------
                            query_commit += " `win` = '"+str(all_win)+"', "
                            query_commit += " `draw` = '"+str(all_draw)+"', "
                            query_commit += " `lose` = '"+str(all_lose)+"', "
                            # ----------------------------------
                            query_commit += " `goals_for` = '"+str(all_goals_for)+"', "
                            query_commit += " `goals_againts` = '"+str(all_goals_againts)+"', "
                            # ----------------------------------
                            query_commit += " `home_played` = '"+str(home_played)+"', "
                            query_commit += " `home_win` = '"+str(home_win)+"', "
                            query_commit += " `home_draw` = '"+str(home_draw)+"', "
                            query_commit += " `home_lose` = '"+str(home_lose)+"', "
                            query_commit += " `home_goals_for` = '"+str(home_goals_for)+"', "
                            query_commit += " `home_goals_againts` = '"+str(home_goals_againts)+"', "
                            # ----------------------------------
                            query_commit += " `away_played` = '"+str(away_played)+"', "
                            query_commit += " `away_win` = '"+str(away_win)+"', "
                            query_commit += " `away_draw` = '"+str(away_draw)+"', "
                            query_commit += " `away_lose` = '"+str(away_lose)+"', "
                            query_commit += " `away_goals_for` = '"+str(away_goals_for)+"', "
                            query_commit += " `away_goals_againts` = '"+str(away_goals_againts)+"', " 
                            # ----------------------------------
                            query_commit += " `updated_at` = '"+str(update_DATE)+"' " 
                            # ----------------------------------
                            query_commit += " where leagueapi_id = "+str(DICTleagueapi_id)+" "    
                            query_commit += " and season = "+str(DICTseason)+" "     
                            query_commit += " and teamapi_id = "+str(teamapi_id)+" "    
                            # ----------------------------------
                            print(space + "api_football_league_standings UPDATED", flush=True)  
                            # ----------------------------------
                            # ----------------------------------
                            # ----------------------------------
                            # ----------------------------------
                            # ----------------------------------
                        # --------------------------------------
                        elif(update_or_insert == 0):
                            # ----------------------------------
                            query_commit = "INSERT INTO `api_football_league_standings`( "
                            # ----------------------------------
                            query_commit += " `leagueapi_id`, "
                            query_commit += " `season`, "
                            # ----------------------------------
                            query_commit += " `rank`, "
                            query_commit += " `teamapi_id`, "
                            query_commit += " `points`, "
                            query_commit += " `goals_diff`, "
                            query_commit += " `group_status`, "
                            query_commit += " `form`, "
                            query_commit += " `status`, "
                            query_commit += " `description`, "
                            query_commit += " `played`, "
                            # ----------------------------------
                            query_commit += " `win`, "
                            query_commit += " `draw`, "
                            query_commit += " `lose`, "
                            # ----------------------------------
                            query_commit += " `goals_for`, "
                            query_commit += " `goals_againts`, "
                            # ----------------------------------
                            query_commit += " `home_played`, "
                            query_commit += " `home_win`, "
                            query_commit += " `home_draw`, "
                            query_commit += " `home_lose`, "
                            query_commit += " `home_goals_for`, "
                            query_commit += " `home_goals_againts`, "
                            # ----------------------------------
                            query_commit += " `away_played`, "
                            query_commit += " `away_win`, "
                            query_commit += " `away_draw`, "
                            query_commit += " `away_lose`, "
                            query_commit += " `away_goals_for`, "
                            query_commit += " `away_goals_againts`, "
                            # ----------------------------------
                            query_commit += " `updated_at` "
                            # ----------------------------------
                            query_commit += " ) VALUES ( "
                            # ----------------------------------
                            query_commit += " '" + str(DICTleagueapi_id) + "', " 
                            query_commit += " '" + str(DICTseason) + "', " 
                            # ----------------------------------
                            query_commit += " '" + str(rank) + "', " 
                            query_commit += " '" + str(teamapi_id) + "', " 
                            query_commit += " '" + str(points) + "', " 
                            query_commit += " '" + str(goalsDiff) + "', " 
                            query_commit += " '" + str(group) + "', " 
                            query_commit += " '" + str(form) + "', " 
                            query_commit += " '" + str(status) + "', " 
                            query_commit += " '" + str(description) + "', " 
                            query_commit += " '" + str(all_played) + "', " 
                            # ----------------------------------
                            query_commit += " '" + str(all_win) + "', " 
                            query_commit += " '" + str(all_draw) + "', " 
                            query_commit += " '" + str(all_lose) + "', " 
                            query_commit += " '" + str(all_goals_for) + "', " 
                            query_commit += " '" + str(all_goals_againts) + "', " 
                            # ----------------------------------
                            query_commit += " '" + str(home_played) + "', " 
                            query_commit += " '" + str(home_win) + "', " 
                            query_commit += " '" + str(home_draw) + "', " 
                            query_commit += " '" + str(home_lose) + "', " 
                            query_commit += " '" + str(home_goals_for) + "', " 
                            query_commit += " '" + str(home_goals_againts) + "', " 
                            # ----------------------------------
                            query_commit += " '" + str(away_played) + "', " 
                            query_commit += " '" + str(away_win) + "', " 
                            query_commit += " '" + str(away_draw) + "', " 
                            query_commit += " '" + str(away_lose) + "', " 
                            query_commit += " '" + str(away_goals_for) + "', " 
                            query_commit += " '" + str(away_goals_againts) + "', "  
                            # ----------------------------------
                            query_commit += " '" + str(update_DATE) + "') "    
                            # ----------------------------------
                            print(space + "api_football_league_standings INSERTED", flush=True)
                            # ----------------------------------
                        # --------------------------------------
                        mycursor.execute(query_commit)
                        mydb.commit()   
                        # --------------------------------------
                        mycursor.close()
                        mydb.close() 
                        # --------------------------------------
                        # --------------------------------------
                        # -------------------------------------- 
                        # --------------------------------------------------------------------------------------------- UPDATE DATE LEAGUE STANDINGS
                        host="localhost"
                        user="root" 
                        database="pr_mmbuzz_2022_06"
                        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                        mycursor = mydb.cursor()
                        # -------------------------------------- 
                        query_commit = "UPDATE `football_leagues` SET "
                        # -------------------------------------- 
                        query_commit += " `league_standing_updated_at` = now() "
                        # --------------------------------------  
                        query_commit += " where leagueapi_id = "+str(DICTleagueapi_id)+" "     
                        # -------------------------------------- 
                        mycursor.execute(query_commit)
                        mydb.commit()   
                        # --------------------------------------
                        mycursor.close()
                        mydb.close() 
                        # --------------------------------------
                        space += "__"
                        # --------------------------------------
                        print(space + "league_standing_updated_at UPDATED " + str(DICTleagueapi_id), flush=True)  
                        # --------------------------------------
                        # --------------------------------------
                        # --------------------------------------
                        # --------------------------------------
                    # ------------------------------------------
                    elif(can_we_continue == 0):
                        # --------------------------------------
                        print(space + "teamapi_id: None" , flush=True)
                        # --------------------------------------
                        # --------------------------------------
                    # ------------------------------------------
                    # ------------------------------------------
                    # ------------------------------------------
                    # ------------------------------------------
                        

 
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")