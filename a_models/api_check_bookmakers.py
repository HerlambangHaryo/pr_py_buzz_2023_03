# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *     

import pytz
utc=pytz.UTC 

import requests
import json 
 
def acb_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "acb_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0): 
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space)  
        acb_response_odds(APIkey, DICT, PREP_, space)
    # ----------------------------------------------------------
  
def acb_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "acb_response_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"  
    # ----------------------------------------------------------   
    space += "__" 
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ---------------------------------------------------------- 
    DICTleague          = DICT['league']
    DICTseason          = DICT['season']  
    # ---------------------------------------------------------- 
    print(space + "league : " + str(DICTleague), flush=True)
    print(space + "season : " + str(DICTseason), flush=True) 
    # ----------------------------------------------------------
    querystring = {"league":DICTleague, "season":DICTseason }
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
    try:  
        # ----------------------------------------------------------    
        space += "__"
        # ----------------------------------------------------------   
        total_API_response = len(d['response'])
        # ----------------------------------------------------------   
        print(space + "Total API Response(s) : " + str(total_API_response), flush=True)  
        # ---------------------------------------------------------- 
        counter_response = 0
        # ---------------------------------------------------------- 
        space += "__"
        counter = 0
        current_space = space
        # ----------------------------------------------------------  
        if(total_API_response != 0):
            # ------------------------------------------------------ 
            for i in d['response']:  
                # -------------------------------------------------- 
                bookmakers_Array    = i['bookmakers']   
                # --------------------------------------------------
                for ba in bookmakers_Array:
                    # ----------------------------------------------
                    bookmakersapi_id    = ba['id']
                    bookmakersapi_name  = ba['name']    
                    # ----------------------------------------------
                    bets_Array          = ba['bets']
                    # ----------------------------------------------
                    if(len(bets_Array) > 20):
                        # ------------------------------------------
                        print(space + str(bookmakersapi_name) + " __ " + str(len(bets_Array)), flush=True)
                        # ------------------------------------------
                    # ----------------------------------------------
                # --------------------------------------------------
                print("")
            # ------------------------------------------------------  
        # ----------------------------------------------------------  
        # ----------------------------------------------------------
        # ----------------------------------------------------------
        # ---------------------------------------------------------- 
    # --------------------------------------------------------------
    except KeyError: 
        # ---------------------------------------------------------- 
        print("KeyErrorKeyErrorKeyError")
        # ---------------------------------------------------------- 
    # -------------------------------------------------------------- 
 