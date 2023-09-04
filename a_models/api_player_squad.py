# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.football_players import *   
from a_models.football_teams import *   

import pytz
utc=pytz.UTC 

import requests
import json 

def aps_group_by_all_team(leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aps_group_by_all_team()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " teams_homeapi_id "  
    query += " from football_fixtures " 
    query += " where leagueapi_id =  '"+str(leagueapi_id)+"' " 
    query += " group by teams_homeapi_id " 
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
        teamapi_id   = str(x[0])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + teamapi_id  
        print(word, flush=True)    
        # ------------------------------------------------------
        DICT = {
            'teamapi_id' :teamapi_id, 
            'leagueapi_id' :leagueapi_id, 
        }
        aps_controll_match_update(DICT, 'Null', space)
        # ------------------------------------------------------
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   


def aps_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aps_controll_match_update()", flush=True)
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
        aps_response_odds(APIkey, DICT, PREP_, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------
 
def aps_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "aps_response_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/players/squads"  
    # ----------------------------------------------------------   
    space += "__" 
    # ---------------------------------------------------------- 
    DICTteamapi_id              = DICT['teamapi_id'] 
    DICTleagueapi_id            = DICT['leagueapi_id']  
    # ----------------------------------------------------------
    print(space + "leagueapi_id : " + str(DICTleagueapi_id), flush=True) 
    print(space + "teamapi_id : " + str(DICTteamapi_id), flush=True) 
    # ----------------------------------------------------------
    querystring         = {"team":DICTteamapi_id}
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
    counter_response = 0
    # ---------------------------------------------------------- 
    space += "__"
    counter = 0
    # ----------------------------------------------------------  
    if(total_API_response != 0):
        # ------------------------------------------------------  
        # ------------------------------------------------------ 
        # Iterate through team data
        for team_data in data['response']:
            # -------------------------------------------------- 
            team_id = data['response'][0]['team']['id']
            # -------------------------------------------------- 
            # Delete all data by teamapi_id
            aps_delete(team_id, space)
            # -------------------------------------------------- 
            teamapi_id  = team_data['team']['id']
            team_name   = team_data['team']['name']
            team_logo   = team_data['team']['logo']
            # --------------------------------------------------
            # print("Team ID:", team_id)
            # print("Team Name:", team_name)
            # print("Team Logo:", team_logo)
            # --------------------------------------------------
            
            # --------------------------------------------------
            # Iterate through player data within the team
            for player in team_data['players']:
                # ----------------------------------------------
                playerapi_id    = player['id']
                player_name     = player['name']
                player_age      = player['age']
                player_number   = player['number']
                player_position = player['position']
                player_photo    = player['photo']
                # ---------------------------------------------- 
                # ---------------------------------------------- 
                # ---------------------------------------------- 
                # ------------------------------------------------------------------------------------ Insert player 
                fP_update_or_insert(playerapi_id, 
                        player_name, 
                        player_age, 
                        player_number,  
                        player_position,  
                        player_photo,  
                        space)
                # ---------------------------------------------- 
                # ---------------------------------------------- 
                # ---------------------------------------------- 
                # ------------------------------------------------------------------------------------ Insert player squad
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # ----------------------------------------------
                query_commit = "INSERT INTO `football_player_squads`( "
                # ----------------------------------------------
                query_commit += " `teamapi_id`, "
                query_commit += " `playerapi_id`, "  
                # ----------------------------------------------
                query_commit += " `created_at` "  
                # ----------------------------------------------
                query_commit += " ) VALUES ( "
                # ----------------------------------------------
                query_commit += " '" + str(teamapi_id) + "', " 
                query_commit += " '" + str(playerapi_id) + "', " 
                # ----------------------------------------------
                query_commit += " now() )"  
                # ----------------------------------------------
                mycursor.execute(query_commit)
                mydb.commit()        
                # ----------------------------------------------
                mycursor.close()
                mydb.close() 
                # ---------------------------------------------- 
            # --------------------------------------------------
            print()  # Separate each team's data
            # --------------------------------------------------
        # ------------------------------------------------------
        fT_insert_new(teamapi_id, team_name, team_logo, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    elif(total_API_response == 0):
        # ------------------------------------------------------
        print(space + "SKIPPED because its Nothing total_API_response:" + str(total_API_response), flush=True) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    
def aps_delete(teamapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "aps_delete()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------   
    print(space + "teamapi_id : " + str(teamapi_id), flush=True)  
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query_commit = " delete " 
    query_commit += " from football_player_squads "    
    query_commit += " where teamapi_id = "+str(teamapi_id)+" "     
    # ----------------------------------------------------------  
    mycursor.execute(query_commit)
    mydb.commit()        
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  
    space += "__"   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)     
    # ----------------------------------------------------------  