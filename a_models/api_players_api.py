# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.api_football_player_seasons import *   
 
import pytz
utc=pytz.UTC 

import requests
import json 

def aPaI_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aPaIcontroll_match_update()", flush=True)
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
        aPaIresponse_odds(APIkey, DICT, PREP_, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------
 
def aPaIresponse_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "aPaIresponse_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/players"  
    # ----------------------------------------------------------   
    space += "__" 
    # ---------------------------------------------------------- 
    DICTid          = DICT['id'] 
    DICTseason      = DICT['season']   
    # ----------------------------------------------------------
    print(space + "id : " + str(DICTid), flush=True) 
    print(space + "season : " + str(DICTseason), flush=True)  
    # ----------------------------------------------------------
    querystring         = {"id":DICTid, "season":DICTseason}
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
    try:  
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



                # --------------------------------------------------
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # -------------------------------------------------- 
                query = " Select  * " 
                query += " from football_players "    
                query += " where playerapi_id = "+str(playerapi_id)+" "     
                # --------------------------------------------------
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result =  mycursor.fetchall()
                # --------------------------------------------------
                mycursor.close()
                mydb.close() 
                # -------------------------------------------------- 
                update_or_insert = len(result)
                # --------------------------------------------------









                # --------------------------------------------------
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # --------------------------------------------------
                if(update_or_insert == 0):
                    # ---------------------------------------------- 
                    query_commit = "INSERT INTO `football_players`( "
                    # ----------------------------------------------
                    query_commit += " `playerapi_id`, "
                    query_commit += " `name`, "
                    query_commit += " `firstname`, " 
                    query_commit += " `lastname`, "  
                    query_commit += " `age`, "  
                    # query_commit += " `number`, "  
                    # query_commit += " `position`, "  
                    query_commit += " `birth_date`, "  
                    query_commit += " `birth_place`, "  
                    query_commit += " `birth_country`, "  
                    query_commit += " `nationality`, "  
                    query_commit += " `height`, "  
                    query_commit += " `weight`, "  
                    query_commit += " `injured`, "  
                    query_commit += " `photo`, "  
                    # ----------------------------------------------
                    query_commit += " `created_at`, "   
                    query_commit += " `api_players_updated_at` "   
                    # ----------------------------------------------
                    query_commit += " ) VALUES ( "
                    # ---------------------------------------------- 
                    query_commit += " '" + str(playerapi_id) + "', "
                    query_commit += " '" + str(player_name).replace("'", "\\'")  + "', "
                    query_commit += " '" + str(player_firstname).replace("'", "\\'")  + "', " 
                    query_commit += " '" + str(player_lastname).replace("'", "\\'")  + "', "  
                    query_commit += " '" + str(player_age) + "', "  
                    # query_commit += " '" + str(player_number) + "', "  
                    # query_commit += " '" + str(player_position) + "', "  
                    query_commit += " '" + str(player_birth_date) + "', "  
                    query_commit += " '" + str(player_birth_place) + "', "  
                    query_commit += " '" + str(player_birth_country).replace("'", "\\'")  + "', "  
                    query_commit += " '" + str(player_nationality).replace("'", "\\'")  + "', "  
                    query_commit += " '" + str(player_height) + "', "  
                    query_commit += " '" + str(player_weight) + "', "  
                    query_commit += " '" + str(player_injured).replace("'", "\\'")  + "', "  
                    query_commit += " '" + str(player_photo).replace("'", "\\'")  + "', "  
    
                    # ----------------------------------------------
                    query_commit += " current_timestamp, "     
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
                    query_commit = "UPDATE `football_players` SET "
                    # ----------------------------------------------  
                    query_commit += " `name` = '"+str(player_name).replace("'", "\\'")+"', "
                    query_commit += " `firstname` = '"+str(player_firstname).replace("'", "\\'")+"', " 
                    query_commit += " `lastname` = '"+str(player_lastname).replace("'", "\\'")+"', "  
                    query_commit += " `age` = '"+str(player_age)+"', "  
                    # query_commit += " `number` = '"+str(DICTcountry)+"', "  
                    # query_commit += " `position` = '"+str(DICTcountry)+"', "  
                    query_commit += " `birth_date` = '"+str(player_birth_date)+"', "  
                    query_commit += " `birth_place` = '"+str(player_birth_place)+"', "  
                    query_commit += " `birth_country` = '"+str(player_birth_country).replace("'", "\\'")+"', "  
                    query_commit += " `nationality` = '"+str(player_nationality).replace("'", "\\'")+"', "  
                    query_commit += " `height` = '"+str(player_height)+"', "  
                    query_commit += " `weight` = '"+str(player_weight)+"', "  
                    query_commit += " `injured` = '"+str(player_injured).replace("'", "\\'")+"', "  
                    query_commit += " `photo` = '"+str(player_photo).replace("'", "\\'")+"', "  

                    # ----------------------------------------------
                    query_commit += " `api_players_updated_at` = now() "
                    # ----------------------------------------------
                    query_commit += " where playerapi_id = "+str(playerapi_id)+" "    
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
        # ----------------------------------------------------------  
        elif(total_API_response == 0):
            # ------------------------------------------------------
            print(space + "SKIPPED because its Nothing total_API_response:" + str(total_API_response), flush=True) 
            # ------------------------------------------------------
    
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")
    # ----------------------------------------------------------  
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------