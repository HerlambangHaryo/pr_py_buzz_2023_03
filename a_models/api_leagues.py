# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *    
 
import pytz
utc=pytz.UTC 

import requests
import json 


def al_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "al_controll_match_update()", flush=True)
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
        al_response_odds(APIkey, DICT, PREP_, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------

    
def al_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "al_response_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"  
    # ----------------------------------------------------------   
    space += "__" 
    # ---------------------------------------------------------- 
    DICTcountry              = DICT['country']  
    # ----------------------------------------------------------
    print(space + "country : " + str(DICTcountry), flush=True)  
    # ----------------------------------------------------------
    querystring         = {"country":DICTcountry}
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
        counter_response = 0
        # ---------------------------------------------------------- 
        space += "__"
        counter = 0
        # ----------------------------------------------------------  
        if(total_API_response != 0):
            # ------------------------------------------------------   
            leagues = data['response']

            for league in leagues:
                league_info = league['league']
                league_name = league_info['name']
                league_type = league_info['type']
                league_logo = league_info['logo']
                league_id   = league_info['id']
                
                # ------------------------------------------------------------------------------------ Insert player 
                al_update_or_insert(league_id, 
                        league_name, 
                        league_type, 
                        league_logo,   
                        DICTcountry,
                        space)
            # ------------------------------------------------------   

            
            # ------------------------------------------------------   
            host="localhost"
            user="root" 
            database="pr_mmbuzz_2022_06"
            mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
            mycursor = mydb.cursor()
            # ------------------------------------------------------
            query_commit = "UPDATE `countries` SET " 
            # ------------------------------------------------------
            query_commit += " `api_league_updated_at` = now() "
            # ------------------------------------------------------
            query_commit += " where name = '"+str(DICTcountry)+"' "    
            # ------------------------------------------------------ 
            print(space + query_commit, flush=True) 
            # ------------------------------------------------------
            mycursor.execute(query_commit)
            mydb.commit()    
            # ------------------------------------------------------   
            mycursor.close()
            mydb.close()   
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
 
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")

    
def al_update_or_insert(league_id, 
                    league_name, 
                    league_type, 
                    league_logo,     
                    DICTcountry,  
                    space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "al_update_or_insert()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select  * " 
    query += " from football_leagues "    
    query += " where leagueapi_id = "+str(league_id)+" "     
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
    # print(space + "Venue Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------    
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `football_leagues`( "
        # ------------------------------------------------------ 
        query_commit += " `leagueapi_id`, "
        query_commit += " `name`, "
        query_commit += " `type`, " 
        query_commit += " `country_name`, "  
        query_commit += " `logo`, "  
        # ------------------------------------------------------  
        query_commit += " `api_league_updated_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------ 
        query_commit += " " + str(league_id) + ", " 
        query_commit += " '" + str(league_name).replace("'", "\\'") + "', " 
        query_commit += " '" + str(league_type) + "', " 
        query_commit += " '" + str(DICTcountry) + "', " 
        query_commit += " '" + str(league_logo).replace("'", "\\'")  + "', "  
        # ------------------------------------------------------ 
        query_commit += " current_timestamp ) "     
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True)
        # ------------------------------------------------------  
        mycursor.execute(query_commit)
        mydb.commit()     
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    elif(total_rows == 1): 
        # ------------------------------------------------------
        query_commit = "UPDATE `football_leagues` SET "
        # ------------------------------------------------------    
        query_commit += " `country_name` = '"+str(DICTcountry)+"', "
        query_commit += " `name` = '"+str(league_name).replace("'", "\\'")+"', "
        query_commit += " `type` = '"+str(league_type)+"', " 
        query_commit += " `logo` = '"+str(league_logo).replace("'", "\\'")+"', "
        # ------------------------------------------------------
        query_commit += " `api_league_updated_at` = now() "
        # ------------------------------------------------------
        query_commit += " where leagueapi_id = "+str(league_id)+" "    
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True) 
        # ------------------------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()    
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  