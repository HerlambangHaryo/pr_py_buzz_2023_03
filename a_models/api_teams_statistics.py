# Import
import mysql.connector 
from a_models.api_accounts import *      
from a_models.api_football_standings import *     

import pytz
utc=pytz.UTC 

import requests
import json 


def ats_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------   
    # ao_controll_match_update(DICT, PREP_, space)
    # ao_controll_match_update(date, bookmaker, season, league, 1, space)
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ats_controll_match_update()", flush=True)
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
        ats_response_odds(APIkey, DICT, PREP_, space)
    # ----------------------------------------------------------
 
def ats_response_odds(APIkey, DICT, PREP_, space): 
    # ao_response_odds(APIkey, date, bookmaker, season, league, page, space)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "ats_response_odds()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    DICTleagueapi_id = DICT['leagueapi_id'] 
    DICTseason = DICT['season'] 
    DICTteam = DICT['team'] 
    # ----------------------------------------------------------
    print(space + "DICTleagueapi_id : " + str(DICTleagueapi_id), flush=True) 
    print(space + "DICTseason : " + str(DICTseason), flush=True) 
    print(space + "DICTteam : " + str(DICTteam), flush=True) 
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
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    # ----------------------------------------------------------
    querystring = {"league":DICTleagueapi_id, "season":DICTseason,"team":DICTteam }
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
        d_res = d['response']

        long_form = d_res['form']
        # print(long_form)

        # print("")

        #home
        home_goals_for_average = d_res['goals']['for']['average']['home']
        # print("home_goals_for_average:" + str(home_goals_for_average))
        #away
        away_goals_for_average = d_res['goals']['for']['average']['away']
        # print("away_goals_for_average:" + str(away_goals_for_average))
        #total
        goals_for_average = d_res['goals']['for']['average']['total']
        # print("goals_for_average:" + str(goals_for_average))
        

        # print("")
        #home
        home_goals_for_minute_0_15_total = d_res['goals']['for']['minute']['0-15']['total']
        # print("home_goals_for_minute_0_15_total:" + str(home_goals_for_minute_0_15_total))
        home_goals_for_minute_0_15_percentage = d_res['goals']['for']['minute']['0-15']['percentage']
        # print("home_goals_for_minute_0_15_percentage:" + str(home_goals_for_minute_0_15_percentage)) 
        # print("")
        #home
        home_goals_for_minute_16_30_total = d_res['goals']['for']['minute']['16-30']['total']
        # print("home_goals_for_minute_16_30_total:" + str(home_goals_for_minute_16_30_total))
        home_goals_for_minute_16_30_percentage = d_res['goals']['for']['minute']['16-30']['percentage']
        # print("home_goals_for_minute_16_30_percentage:" + str(home_goals_for_minute_16_30_percentage)) 
        # print("")
        #home
        home_goals_for_minute_31_45_total = d_res['goals']['for']['minute']['31-45']['total']
        # print("home_goals_for_minute_31_45_total:" + str(home_goals_for_minute_31_45_total))
        home_goals_for_minute_31_45_percentage = d_res['goals']['for']['minute']['31-45']['percentage']
        # print("home_goals_for_minute_31_45_percentage:" + str(home_goals_for_minute_31_45_percentage)) 
        # print("")
        #home
        home_goals_for_minute_46_60_total = d_res['goals']['for']['minute']['46-60']['total']
        # print("home_goals_for_minute_46_60_total:" + str(home_goals_for_minute_46_60_total))
        home_goals_for_minute_46_60_percentage = d_res['goals']['for']['minute']['46-60']['percentage']
        # print("home_goals_for_minute_46_60_percentage:" + str(home_goals_for_minute_46_60_percentage)) 
        # print("")
        #home
        home_goals_for_minute_61_75_total = d_res['goals']['for']['minute']['61-75']['total']
        # print("home_goals_for_minute_61_75_total:" + str(home_goals_for_minute_61_75_total))
        home_goals_for_minute_61_75_percentage = d_res['goals']['for']['minute']['61-75']['percentage']
        # print("home_goals_for_minute_61_75_percentage:" + str(home_goals_for_minute_61_75_percentage)) 
        # print("")
        #home
        home_goals_for_minute_76_90_total = d_res['goals']['for']['minute']['76-90']['total']
        # print("home_goals_for_minute_76_90_total:" + str(home_goals_for_minute_76_90_total))
        home_goals_for_minute_76_90_percentage = d_res['goals']['for']['minute']['76-90']['percentage']
        # print("home_goals_for_minute_76_90_percentage:" + str(home_goals_for_minute_76_90_percentage)) 
        # print("")
        #home
        home_goals_for_minute_91_105_total = d_res['goals']['for']['minute']['91-105']['total']
        # print("home_goals_for_minute_91_105_total:" + str(home_goals_for_minute_91_105_total))
        home_goals_for_minute_91_105_percentage = d_res['goals']['for']['minute']['91-105']['percentage']
        # print("home_goals_for_minute_91_105_percentage:" + str(home_goals_for_minute_91_105_percentage)) 
        # print("")
        #home
        home_goals_for_minute_106_120_total = d_res['goals']['for']['minute']['106-120']['total']
        # print("home_goals_for_minute_106_120_total:" + str(home_goals_for_minute_106_120_total))
        home_goals_for_minute_106_120_percentage = d_res['goals']['for']['minute']['106-120']['percentage']
        # print("home_goals_for_minute_106_120_percentage:" + str(home_goals_for_minute_106_120_percentage)) 
        # print("")

        #away
        away_goals_for_minute_0_15_total = d_res['goals']['for']['minute']['0-15']['total']
        # print("away_goals_for_minute_0_15_total:" + str(away_goals_for_minute_0_15_total))
        away_goals_for_minute_0_15_percentage = d_res['goals']['for']['minute']['0-15']['percentage']
        # print("away_goals_for_minute_0_15_percentage:" + str(away_goals_for_minute_0_15_percentage)) 
        # print("")
        #away
        away_goals_for_minute_16_30_total = d_res['goals']['for']['minute']['16-30']['total']
        # print("away_goals_for_minute_16_30_total:" + str(away_goals_for_minute_16_30_total))
        away_goals_for_minute_16_30_percentage = d_res['goals']['for']['minute']['16-30']['percentage']
        # print("away_goals_for_minute_16_30_percentage:" + str(away_goals_for_minute_16_30_percentage)) 
        # print("")
        #away
        away_goals_for_minute_31_45_total = d_res['goals']['for']['minute']['31-45']['total']
        # print("away_goals_for_minute_31_45_total:" + str(away_goals_for_minute_31_45_total))
        away_goals_for_minute_31_45_percentage = d_res['goals']['for']['minute']['31-45']['percentage']
        # print("away_goals_for_minute_31_45_percentage:" + str(away_goals_for_minute_31_45_percentage)) 
        # print("")
        #away
        away_goals_for_minute_46_60_total = d_res['goals']['for']['minute']['46-60']['total']
        # print("away_goals_for_minute_46_60_total:" + str(away_goals_for_minute_46_60_total))
        away_goals_for_minute_46_60_percentage = d_res['goals']['for']['minute']['46-60']['percentage']
        # print("away_goals_for_minute_46_60_percentage:" + str(away_goals_for_minute_46_60_percentage)) 
        # print("")
        #away
        away_goals_for_minute_61_75_total = d_res['goals']['for']['minute']['61-75']['total']
        # print("away_goals_for_minute_61_75_total:" + str(away_goals_for_minute_61_75_total))
        away_goals_for_minute_61_75_percentage = d_res['goals']['for']['minute']['61-75']['percentage']
        # print("away_goals_for_minute_61_75_percentage:" + str(away_goals_for_minute_61_75_percentage)) 
        # print("")
        #away
        away_goals_for_minute_76_90_total = d_res['goals']['for']['minute']['76-90']['total']
        # print("away_goals_for_minute_76_90_total:" + str(away_goals_for_minute_76_90_total))
        away_goals_for_minute_76_90_percentage = d_res['goals']['for']['minute']['76-90']['percentage']
        # print("away_goals_for_minute_76_90_percentage:" + str(away_goals_for_minute_76_90_percentage)) 
        # print("")
        #away
        away_goals_for_minute_91_105_total = d_res['goals']['for']['minute']['91-105']['total']
        # print("away_goals_for_minute_91_105_total:" + str(away_goals_for_minute_91_105_total))
        away_goals_for_minute_91_105_percentage = d_res['goals']['for']['minute']['91-105']['percentage']
        # print("away_goals_for_minute_91_105_percentage:" + str(away_goals_for_minute_91_105_percentage)) 
        # print("")
        #away
        away_goals_for_minute_106_120_total = d_res['goals']['for']['minute']['106-120']['total']
        # print("away_goals_for_minute_106_120_total:" + str(away_goals_for_minute_106_120_total))
        away_goals_for_minute_106_120_percentage = d_res['goals']['for']['minute']['106-120']['percentage']
        # print("away_goals_for_minute_106_120_percentage:" + str(away_goals_for_minute_106_120_percentage)) 
        # print("")
        
        #home
        home_goals_against_average = d_res['goals']['against']['average']['home']
        # print("home_goals_against_average:" + str(home_goals_against_average))
        #away
        away_goals_against_average = d_res['goals']['against']['average']['away']
        # print("away_goals_against_average:" + str(away_goals_against_average))
        #total
        goals_against_average = d_res['goals']['against']['average']['total']
        # print("goals_against_average:" + str(goals_against_average))

        # print("")


        # print("")
        #home
        home_goals_against_minute_0_15_total = d_res['goals']['against']['minute']['0-15']['total']
        # print("home_goals_against_minute_0_15_total:" + str(home_goals_against_minute_0_15_total))
        home_goals_against_minute_0_15_percentage = d_res['goals']['against']['minute']['0-15']['percentage']
        # print("home_goals_against_minute_0_15_percentage:" + str(home_goals_against_minute_0_15_percentage)) 
        # print("")
        #home
        home_goals_against_minute_16_30_total = d_res['goals']['against']['minute']['16-30']['total']
        # print("home_goals_against_minute_16_30_total:" + str(home_goals_against_minute_16_30_total))
        home_goals_against_minute_16_30_percentage = d_res['goals']['against']['minute']['16-30']['percentage']
        # print("home_goals_against_minute_16_30_percentage:" + str(home_goals_against_minute_16_30_percentage)) 
        # print("")
        #home
        home_goals_against_minute_31_45_total = d_res['goals']['against']['minute']['31-45']['total']
        # print("home_goals_against_minute_31_45_total:" + str(home_goals_against_minute_31_45_total))
        home_goals_against_minute_31_45_percentage = d_res['goals']['against']['minute']['31-45']['percentage']
        # print("home_goals_against_minute_31_45_percentage:" + str(home_goals_against_minute_31_45_percentage)) 
        # print("")
        #home
        home_goals_against_minute_46_60_total = d_res['goals']['against']['minute']['46-60']['total']
        # print("home_goals_against_minute_46_60_total:" + str(home_goals_against_minute_46_60_total))
        home_goals_against_minute_46_60_percentage = d_res['goals']['against']['minute']['46-60']['percentage']
        # print("home_goals_against_minute_46_60_percentage:" + str(home_goals_against_minute_46_60_percentage)) 
        # print("")
        #home
        home_goals_against_minute_61_75_total = d_res['goals']['against']['minute']['61-75']['total']
        # print("home_goals_against_minute_61_75_total:" + str(home_goals_against_minute_61_75_total))
        home_goals_against_minute_61_75_percentage = d_res['goals']['against']['minute']['61-75']['percentage']
        # print("home_goals_against_minute_61_75_percentage:" + str(home_goals_against_minute_61_75_percentage)) 
        # print("")
        #home
        home_goals_against_minute_76_90_total = d_res['goals']['against']['minute']['76-90']['total']
        # print("home_goals_against_minute_76_90_total:" + str(home_goals_against_minute_76_90_total))
        home_goals_against_minute_76_90_percentage = d_res['goals']['against']['minute']['76-90']['percentage']
        # print("home_goals_against_minute_76_90_percentage:" + str(home_goals_against_minute_76_90_percentage)) 
        # print("")
        #home
        home_goals_against_minute_91_105_total = d_res['goals']['against']['minute']['91-105']['total']
        # print("home_goals_against_minute_91_105_total:" + str(home_goals_against_minute_91_105_total))
        home_goals_against_minute_91_105_percentage = d_res['goals']['against']['minute']['91-105']['percentage']
        # print("home_goals_against_minute_91_105_percentage:" + str(home_goals_against_minute_91_105_percentage)) 
        # print("")
        #home
        home_goals_against_minute_106_120_total = d_res['goals']['against']['minute']['106-120']['total']
        # print("home_goals_against_minute_106_120_total:" + str(home_goals_against_minute_106_120_total))
        home_goals_against_minute_106_120_percentage = d_res['goals']['against']['minute']['106-120']['percentage']
        # print("home_goals_against_minute_106_120_percentage:" + str(home_goals_against_minute_106_120_percentage)) 
        # print("")

        #away
        away_goals_against_minute_0_15_total = d_res['goals']['against']['minute']['0-15']['total']
        # print("away_goals_against_minute_0_15_total:" + str(away_goals_against_minute_0_15_total))
        away_goals_against_minute_0_15_percentage = d_res['goals']['against']['minute']['0-15']['percentage']
        # print("away_goals_against_minute_0_15_percentage:" + str(away_goals_against_minute_0_15_percentage)) 
        # print("")
        #away
        away_goals_against_minute_16_30_total = d_res['goals']['against']['minute']['16-30']['total']
        # print("away_goals_against_minute_16_30_total:" + str(away_goals_against_minute_16_30_total))
        away_goals_against_minute_16_30_percentage = d_res['goals']['against']['minute']['16-30']['percentage']
        # print("away_goals_against_minute_16_30_percentage:" + str(away_goals_against_minute_16_30_percentage)) 
        # print("")
        #away
        away_goals_against_minute_31_45_total = d_res['goals']['against']['minute']['31-45']['total']
        # print("away_goals_against_minute_31_45_total:" + str(away_goals_against_minute_31_45_total))
        away_goals_against_minute_31_45_percentage = d_res['goals']['against']['minute']['31-45']['percentage']
        # print("away_goals_against_minute_31_45_percentage:" + str(away_goals_against_minute_31_45_percentage)) 
        # print("")
        #away
        away_goals_against_minute_46_60_total = d_res['goals']['against']['minute']['46-60']['total']
        # print("away_goals_against_minute_46_60_total:" + str(away_goals_against_minute_46_60_total))
        away_goals_against_minute_46_60_percentage = d_res['goals']['against']['minute']['46-60']['percentage']
        # print("away_goals_against_minute_46_60_percentage:" + str(away_goals_against_minute_46_60_percentage)) 
        # print("")
        #away
        away_goals_against_minute_61_75_total = d_res['goals']['against']['minute']['61-75']['total']
        # print("away_goals_against_minute_61_75_total:" + str(away_goals_against_minute_61_75_total))
        away_goals_against_minute_61_75_percentage = d_res['goals']['against']['minute']['61-75']['percentage']
        # print("away_goals_against_minute_61_75_percentage:" + str(away_goals_against_minute_61_75_percentage)) 
        # print("")
        #away
        away_goals_against_minute_76_90_total = d_res['goals']['against']['minute']['76-90']['total']
        # print("away_goals_against_minute_76_90_total:" + str(away_goals_against_minute_76_90_total))
        away_goals_against_minute_76_90_percentage = d_res['goals']['against']['minute']['76-90']['percentage']
        # print("away_goals_against_minute_76_90_percentage:" + str(away_goals_against_minute_76_90_percentage)) 
        # print("")
        #away
        away_goals_against_minute_91_105_total = d_res['goals']['against']['minute']['91-105']['total']
        # print("away_goals_against_minute_91_105_total:" + str(away_goals_against_minute_91_105_total))
        away_goals_against_minute_91_105_percentage = d_res['goals']['against']['minute']['91-105']['percentage']
        # print("away_goals_against_minute_91_105_percentage:" + str(away_goals_against_minute_91_105_percentage)) 
        # print("")
        #away
        away_goals_against_minute_106_120_total = d_res['goals']['against']['minute']['106-120']['total']
        # print("away_goals_against_minute_106_120_total:" + str(away_goals_against_minute_106_120_total))
        away_goals_against_minute_106_120_percentage = d_res['goals']['against']['minute']['106-120']['percentage']
        # print("away_goals_against_minute_106_120_percentage:" + str(away_goals_against_minute_106_120_percentage)) 
        # print("")


        #
        biggest_streak_wins = d_res['biggest']['streak']['wins'] 
        # print("biggest_streak_wins:" + str(biggest_streak_wins))
        biggest_streak_draws = d_res['biggest']['streak']['draws'] 
        # print("biggest_streak_draws:" + str(biggest_streak_draws)) 
        biggest_streak_loses = d_res['biggest']['streak']['loses'] 
        # print("biggest_streak_loses:" + str(biggest_streak_loses)) 
        # print("")

        #
        biggest_wins_home = d_res['biggest']['wins']['home'] 
        # print("biggest_wins_home:" + str(biggest_wins_home)) 
        biggest_wins_away = d_res['biggest']['wins']['away'] 
        # print("biggest_wins_away:" + str(biggest_wins_away)) 
        # print("")
        #
        biggest_loses_home = d_res['biggest']['loses']['home'] 
        # print("biggest_loses_home:" + str(biggest_loses_home)) 
        biggest_loses_away = d_res['biggest']['loses']['away'] 
        # print("biggest_loses_away:" + str(biggest_loses_away)) 
        # print("")
        #
        biggest_goals_for_home = d_res['biggest']['goals']['for']['home'] 
        # print("biggest_goals_for_home:" + str(biggest_goals_for_home)) 
        biggest_goals_for_away = d_res['biggest']['goals']['for']['away'] 
        # print("biggest_goals_for_away:" + str(biggest_goals_for_away)) 
        # print("")
        #
        biggest_goals_against_home = d_res['biggest']['goals']['against']['home'] 
        # print("biggest_goals_against_home:" + str(biggest_goals_against_home)) 
        biggest_goals_against_away = d_res['biggest']['goals']['against']['away'] 
        # print("biggest_goals_against_away:" + str(biggest_goals_against_away)) 
        # print("")
        #
        clean_sheet_home = d_res['clean_sheet']['home'] 
        # print("clean_sheet_home:" + str(clean_sheet_home))  
        clean_sheet_away = d_res['clean_sheet']['away'] 
        # print("clean_sheet_away:" + str(clean_sheet_away))   
        clean_sheet_total = d_res['clean_sheet']['total'] 
        # print("clean_sheet_total:" + str(clean_sheet_total)) 
        # print("")
        #
        failed_to_score_home = d_res['failed_to_score']['home'] 
        # print("failed_to_score_home:" + str(failed_to_score_home))  
        failed_to_score_away = d_res['failed_to_score']['away'] 
        # print("failed_to_score_away:" + str(failed_to_score_away))   
        failed_to_score_total = d_res['failed_to_score']['total'] 
        # print("failed_to_score_total:" + str(failed_to_score_total)) 
        # print("")
        #
        penalty_scored_total = d_res['penalty']['scored']['total'] 
        # print("penalty_scored_total:" + str(penalty_scored_total))  
        penalty_scored_percentage = d_res['penalty']['scored']['percentage'] 
        # print("penalty_scored_percentage:" + str(penalty_scored_percentage))  
        # print("")
        #
        penalty_missed_total = d_res['penalty']['missed']['total'] 
        # print("penalty_missed_total:" + str(penalty_missed_total))  
        penalty_missed_percentage = d_res['penalty']['missed']['percentage'] 
        # print("penalty_missed_percentage:" + str(penalty_missed_percentage))  
        # print("")
        penalty_total = d_res['penalty']['total']
        # print("penalty_total:" + str(penalty_total))  
        # print("")


        #away
        cards_yellow_0_15_total = d_res['cards']['yellow']['0-15']['total']
        # print("cards_yellow_0_15_total:" + str(cards_yellow_0_15_total))
        cards_yellow_0_15_percentage = d_res['cards']['yellow']['0-15']['percentage']
        # print("cards_yellow_0_15_percentage:" + str(cards_yellow_0_15_percentage)) 
        # print("")
        #away
        cards_yellow_16_30_total = d_res['cards']['yellow']['16-30']['total']
        # print("cards_yellow_16_30_total:" + str(cards_yellow_16_30_total))
        cards_yellow_16_30_percentage = d_res['cards']['yellow']['16-30']['percentage']
        # print("cards_yellow_16_30_percentage:" + str(cards_yellow_16_30_percentage)) 
        # print("")
        #away
        cards_yellow_31_45_total = d_res['cards']['yellow']['31-45']['total']
        # print("cards_yellow_31_45_total:" + str(cards_yellow_31_45_total))
        cards_yellow_31_45_percentage = d_res['cards']['yellow']['31-45']['percentage']
        # print("cards_yellow_31_45_percentage:" + str(cards_yellow_31_45_percentage)) 
        # print("")
        #away
        cards_yellow_46_60_total = d_res['cards']['yellow']['46-60']['total']
        # print("cards_yellow_46_60_total:" + str(cards_yellow_46_60_total))
        cards_yellow_46_60_percentage = d_res['cards']['yellow']['46-60']['percentage']
        # print("cards_yellow_46_60_percentage:" + str(cards_yellow_46_60_percentage)) 
        # print("")
        #away
        cards_yellow_61_75_total = d_res['cards']['yellow']['61-75']['total']
        # print("cards_yellow_61_75_total:" + str(cards_yellow_61_75_total))
        cards_yellow_61_75_percentage = d_res['cards']['yellow']['61-75']['percentage']
        # print("cards_yellow_61_75_percentage:" + str(cards_yellow_61_75_percentage)) 
        # print("")
        #away
        cards_yellow_76_90_total = d_res['cards']['yellow']['76-90']['total']
        # print("cards_yellow_76_90_total:" + str(cards_yellow_76_90_total))
        cards_yellow_76_90_percentage = d_res['cards']['yellow']['76-90']['percentage']
        # print("cards_yellow_76_90_percentage:" + str(cards_yellow_76_90_percentage)) 
        # print("")
        #away
        cards_yellow_91_105_total = d_res['cards']['yellow']['91-105']['total']
        # print("cards_yellow_91_105_total:" + str(cards_yellow_91_105_total))
        cards_yellow_91_105_percentage = d_res['cards']['yellow']['91-105']['percentage']
        # print("cards_yellow_91_105_percentage:" + str(cards_yellow_91_105_percentage)) 
        # print("")
        #away
        cards_yellow_106_120_total = d_res['cards']['yellow']['106-120']['total']
        # print("cards_yellow_106_120_total:" + str(cards_yellow_106_120_total))
        cards_yellow_106_120_percentage = d_res['cards']['yellow']['106-120']['percentage']
        # print("cards_yellow_106_120_percentage:" + str(cards_yellow_106_120_percentage)) 
        # print("")


        #away
        cards_red_0_15_total = d_res['cards']['red']['0-15']['total']
        # print("cards_red_0_15_total:" + str(cards_red_0_15_total))
        cards_red_0_15_percentage = d_res['cards']['red']['0-15']['percentage']
        # print("cards_red_0_15_percentage:" + str(cards_red_0_15_percentage)) 
        # print("")
        #away
        cards_red_16_30_total = d_res['cards']['red']['16-30']['total']
        # print("cards_red_16_30_total:" + str(cards_red_16_30_total))
        cards_red_16_30_percentage = d_res['cards']['red']['16-30']['percentage']
        # print("cards_red_16_30_percentage:" + str(cards_red_16_30_percentage)) 
        # print("")
        #away
        cards_red_31_45_total = d_res['cards']['red']['31-45']['total']
        # print("cards_red_31_45_total:" + str(cards_red_31_45_total))
        cards_red_31_45_percentage = d_res['cards']['red']['31-45']['percentage']
        # print("cards_red_31_45_percentage:" + str(cards_red_31_45_percentage)) 
        # print("")
        #away
        cards_red_46_60_total = d_res['cards']['red']['46-60']['total']
        # print("cards_red_46_60_total:" + str(cards_red_46_60_total))
        cards_red_46_60_percentage = d_res['cards']['red']['46-60']['percentage']
        # print("cards_red_46_60_percentage:" + str(cards_red_46_60_percentage)) 
        # print("")
        #away
        cards_red_61_75_total = d_res['cards']['red']['61-75']['total']
        # print("cards_red_61_75_total:" + str(cards_red_61_75_total))
        cards_red_61_75_percentage = d_res['cards']['red']['61-75']['percentage']
        # print("cards_red_61_75_percentage:" + str(cards_red_61_75_percentage)) 
        # print("")
        #away
        cards_red_76_90_total = d_res['cards']['red']['76-90']['total']
        # print("cards_red_76_90_total:" + str(cards_red_76_90_total))
        cards_red_76_90_percentage = d_res['cards']['red']['76-90']['percentage']
        # print("cards_red_76_90_percentage:" + str(cards_red_76_90_percentage)) 
        # print("")
        #away
        cards_red_91_105_total = d_res['cards']['red']['91-105']['total']
        # print("cards_red_91_105_total:" + str(cards_red_91_105_total))
        cards_red_91_105_percentage = d_res['cards']['red']['91-105']['percentage']
        # print("cards_red_91_105_percentage:" + str(cards_red_91_105_percentage)) 
        # print("")
        #away
        cards_red_106_120_total = d_res['cards']['red']['106-120']['total']
        # print("cards_red_106_120_total:" + str(cards_red_106_120_total))
        cards_red_106_120_percentage = d_res['cards']['red']['106-120']['percentage']
        # print("cards_red_106_120_percentage:" + str(cards_red_106_120_percentage)) 
        # print("")

                            

        # ---------------------------------------------- 
        query_commit = "UPDATE `api_football_standings` SET "
        # ----------------------------------------------  
                            

                            
        query_commit += " `long_form` = '"+str(long_form)+"', "

        query_commit += " `home_goals_for_average` = '"+str(home_goals_for_average)+"', "
        query_commit += " `away_goals_for_average` = '"+str(away_goals_for_average)+"', "
        query_commit += " `goals_for_average` = '"+str(goals_for_average)+"', "

        query_commit += " `home_goals_for_minute_0_15_total` = '"+str(home_goals_for_minute_0_15_total)+"', "
        query_commit += " `home_goals_for_minute_0_15_percentage` = '"+str(home_goals_for_minute_0_15_percentage)+"', "

        query_commit += " `home_goals_for_minute_16_30_total` = '"+str(home_goals_for_minute_16_30_total)+"', "
        query_commit += " `home_goals_for_minute_16_30_percentage` = '"+str(home_goals_for_minute_16_30_percentage)+"', "

        query_commit += " `home_goals_for_minute_31_45_total` = '"+str(home_goals_for_minute_31_45_total)+"', "
        query_commit += " `home_goals_for_minute_31_45_percentage` = '"+str(home_goals_for_minute_31_45_percentage)+"', "

        query_commit += " `home_goals_for_minute_46_60_total` = '"+str(home_goals_for_minute_46_60_total)+"', "
        query_commit += " `home_goals_for_minute_46_60_percentage` = '"+str(home_goals_for_minute_46_60_percentage)+"', "

        query_commit += " `home_goals_for_minute_61_75_total` = '"+str(home_goals_for_minute_61_75_total)+"', "
        query_commit += " `home_goals_for_minute_61_75_percentage` = '"+str(home_goals_for_minute_61_75_percentage)+"', "

        query_commit += " `home_goals_for_minute_76_90_total` = '"+str(home_goals_for_minute_76_90_total)+"', "
        query_commit += " `home_goals_for_minute_76_90_percentage` = '"+str(home_goals_for_minute_76_90_percentage)+"', "

        query_commit += " `home_goals_for_minute_91_105_total` = '"+str(home_goals_for_minute_91_105_total)+"', "
        query_commit += " `home_goals_for_minute_91_105_percentage` = '"+str(home_goals_for_minute_91_105_percentage)+"', "

        query_commit += " `home_goals_for_minute_106_120_total` = '"+str(home_goals_for_minute_106_120_total)+"', "
        query_commit += " `home_goals_for_minute_106_120_percentage` = '"+str(home_goals_for_minute_106_120_percentage)+"', "

        query_commit += " `away_goals_for_minute_0_15_total` = '"+str(away_goals_for_minute_0_15_total)+"', "
        query_commit += " `away_goals_for_minute_0_15_percentage` = '"+str(away_goals_for_minute_0_15_percentage)+"', "

        query_commit += " `away_goals_for_minute_16_30_total` = '"+str(away_goals_for_minute_16_30_total)+"', "
        query_commit += " `away_goals_for_minute_16_30_percentage` = '"+str(away_goals_for_minute_16_30_percentage)+"', "

        query_commit += " `away_goals_for_minute_31_45_total` = '"+str(away_goals_for_minute_31_45_total)+"', "
        query_commit += " `away_goals_for_minute_31_45_percentage` = '"+str(away_goals_for_minute_31_45_percentage)+"', "

        query_commit += " `away_goals_for_minute_46_60_total` = '"+str(away_goals_for_minute_46_60_total)+"', "
        query_commit += " `away_goals_for_minute_46_60_percentage` = '"+str(away_goals_for_minute_46_60_percentage)+"', "

        query_commit += " `away_goals_for_minute_61_75_total` = '"+str(away_goals_for_minute_61_75_total)+"', "
        query_commit += " `away_goals_for_minute_61_75_percentage` = '"+str(away_goals_for_minute_61_75_percentage)+"', "

        query_commit += " `away_goals_for_minute_76_90_total` = '"+str(away_goals_for_minute_76_90_total)+"', "
        query_commit += " `away_goals_for_minute_76_90_percentage` = '"+str(away_goals_for_minute_76_90_percentage)+"', "

        query_commit += " `away_goals_for_minute_91_105_total` = '"+str(away_goals_for_minute_91_105_total)+"', "
        query_commit += " `away_goals_for_minute_91_105_percentage` = '"+str(away_goals_for_minute_91_105_percentage)+"', "

        query_commit += " `away_goals_for_minute_106_120_total` = '"+str(away_goals_for_minute_106_120_total)+"', "
        query_commit += " `away_goals_for_minute_106_120_percentage` = '"+str(away_goals_for_minute_106_120_percentage)+"', "

        query_commit += " `home_goals_against_average` = '"+str(home_goals_against_average)+"', "
        query_commit += " `away_goals_against_average` = '"+str(away_goals_against_average)+"', "
        query_commit += " `goals_against_average` = '"+str(goals_against_average)+"', "


        query_commit += " `home_goals_against_minute_0_15_total` = '"+str(home_goals_against_minute_0_15_total)+"', "
        query_commit += " `home_goals_against_minute_0_15_percentage` = '"+str(home_goals_against_minute_0_15_percentage)+"', "

        query_commit += " `home_goals_against_minute_16_30_total` = '"+str(home_goals_against_minute_16_30_total)+"', "
        query_commit += " `home_goals_against_minute_16_30_percentage` = '"+str(home_goals_against_minute_16_30_percentage)+"', "

        query_commit += " `home_goals_against_minute_31_45_total` = '"+str(home_goals_against_minute_31_45_total)+"', "
        query_commit += " `home_goals_against_minute_31_45_percentage` = '"+str(home_goals_against_minute_31_45_percentage)+"', "

        query_commit += " `home_goals_against_minute_46_60_total` = '"+str(home_goals_against_minute_46_60_total)+"', "
        query_commit += " `home_goals_against_minute_46_60_percentage` = '"+str(home_goals_against_minute_46_60_percentage)+"', "

        query_commit += " `home_goals_against_minute_61_75_total` = '"+str(home_goals_against_minute_61_75_total)+"', "
        query_commit += " `home_goals_against_minute_61_75_percentage` = '"+str(home_goals_against_minute_61_75_percentage)+"', "

        query_commit += " `home_goals_against_minute_76_90_total` = '"+str(home_goals_against_minute_76_90_total)+"', "
        query_commit += " `home_goals_against_minute_76_90_percentage` = '"+str(home_goals_against_minute_76_90_percentage)+"', "

        query_commit += " `home_goals_against_minute_91_105_total` = '"+str(home_goals_against_minute_91_105_total)+"', "
        query_commit += " `home_goals_against_minute_91_105_percentage` = '"+str(home_goals_against_minute_91_105_percentage)+"', "

        query_commit += " `home_goals_against_minute_106_120_total` = '"+str(home_goals_against_minute_106_120_total)+"', "
        query_commit += " `home_goals_against_minute_106_120_percentage` = '"+str(home_goals_against_minute_106_120_percentage)+"', "

        query_commit += " `away_goals_against_minute_0_15_total` = '"+str(away_goals_against_minute_0_15_total)+"', "
        query_commit += " `away_goals_against_minute_0_15_percentage` = '"+str(away_goals_against_minute_0_15_percentage)+"', "

        query_commit += " `away_goals_against_minute_16_30_total` = '"+str(away_goals_against_minute_16_30_total)+"', "
        query_commit += " `away_goals_against_minute_16_30_percentage` = '"+str(away_goals_against_minute_16_30_percentage)+"', "

        query_commit += " `away_goals_against_minute_31_45_total` = '"+str(away_goals_against_minute_31_45_total)+"', "
        query_commit += " `away_goals_against_minute_31_45_percentage` = '"+str(away_goals_against_minute_31_45_percentage)+"', "

        query_commit += " `away_goals_against_minute_46_60_total` = '"+str(away_goals_against_minute_46_60_total)+"', "
        query_commit += " `away_goals_against_minute_46_60_percentage` = '"+str(away_goals_against_minute_46_60_percentage)+"', "

        query_commit += " `away_goals_against_minute_61_75_total` = '"+str(away_goals_against_minute_61_75_total)+"', "
        query_commit += " `away_goals_against_minute_61_75_percentage` = '"+str(away_goals_against_minute_61_75_percentage)+"', "

        query_commit += " `away_goals_against_minute_76_90_total` = '"+str(away_goals_against_minute_76_90_total)+"', "
        query_commit += " `away_goals_against_minute_76_90_percentage` = '"+str(away_goals_against_minute_76_90_percentage)+"', "

        query_commit += " `away_goals_against_minute_91_105_total` = '"+str(away_goals_against_minute_91_105_total)+"', "
        query_commit += " `away_goals_against_minute_91_105_percentage` = '"+str(away_goals_against_minute_91_105_percentage)+"', "

        query_commit += " `away_goals_against_minute_106_120_total` = '"+str(away_goals_against_minute_106_120_total)+"', "
        query_commit += " `away_goals_against_minute_106_120_percentage` = '"+str(away_goals_against_minute_106_120_percentage)+"', "

        query_commit += " `biggest_streak_wins` = '"+str(biggest_streak_wins)+"', "
        query_commit += " `biggest_streak_draws` = '"+str(biggest_streak_draws)+"', "
        query_commit += " `biggest_streak_loses` = '"+str(biggest_streak_loses)+"', "

        query_commit += " `biggest_wins_home` = '"+str(biggest_wins_home)+"', "
        query_commit += " `biggest_wins_away` = '"+str(biggest_wins_away)+"', "

        query_commit += " `biggest_loses_home` = '"+str(biggest_loses_home)+"', "
        query_commit += " `biggest_loses_away` = '"+str(biggest_loses_away)+"', "

        query_commit += " `biggest_goals_for_home` = '"+str(biggest_goals_for_home)+"', "
        query_commit += " `biggest_goals_for_away` = '"+str(biggest_goals_for_away)+"', "

        query_commit += " `biggest_goals_against_home` = '"+str(biggest_goals_against_home)+"', "
        query_commit += " `biggest_goals_against_away` = '"+str(biggest_goals_against_away)+"', "

        query_commit += " `clean_sheet_home` = '"+str(clean_sheet_home)+"', "
        query_commit += " `clean_sheet_away` = '"+str(clean_sheet_away)+"', "
        query_commit += " `clean_sheet_total` = '"+str(clean_sheet_total)+"', "

        query_commit += " `failed_to_score_home` = '"+str(failed_to_score_home)+"', "
        query_commit += " `failed_to_score_away` = '"+str(failed_to_score_away)+"', "
        query_commit += " `failed_to_score_total` = '"+str(failed_to_score_total)+"', "

        query_commit += " `penalty_scored_total` = '"+str(penalty_scored_total)+"', "
        query_commit += " `penalty_scored_percentage` = '"+str(penalty_scored_percentage)+"', "

        query_commit += " `penalty_missed_total` = '"+str(penalty_missed_total)+"', "
        query_commit += " `penalty_missed_percentage` = '"+str(penalty_missed_percentage)+"', "

        query_commit += " `penalty_total` = '"+str(penalty_total)+"', "

        query_commit += " `cards_yellow_0_15_total` = '"+str(cards_yellow_0_15_total)+"', "
        query_commit += " `cards_yellow_0_15_percentage` = '"+str(cards_yellow_0_15_percentage)+"', "

        query_commit += " `cards_yellow_16_30_total` = '"+str(cards_yellow_16_30_total)+"', "
        query_commit += " `cards_yellow_16_30_percentage` = '"+str(cards_yellow_16_30_percentage)+"', "

        query_commit += " `cards_yellow_31_45_total` = '"+str(cards_yellow_31_45_total)+"', "
        query_commit += " `cards_yellow_31_45_percentage` = '"+str(cards_yellow_31_45_percentage)+"', "

        query_commit += " `cards_yellow_46_60_total` = '"+str(cards_yellow_46_60_total)+"', "
        query_commit += " `cards_yellow_46_60_percentage` = '"+str(cards_yellow_46_60_percentage)+"', "

        query_commit += " `cards_yellow_61_75_total` = '"+str(cards_yellow_61_75_total)+"', "
        query_commit += " `cards_yellow_61_75_percentage` = '"+str(cards_yellow_61_75_percentage)+"', "

        query_commit += " `cards_yellow_76_90_total` = '"+str(cards_yellow_76_90_total)+"', "
        query_commit += " `cards_yellow_76_90_percentage` = '"+str(cards_yellow_76_90_percentage)+"', "

        query_commit += " `cards_yellow_91_105_total` = '"+str(cards_yellow_91_105_total)+"', "
        query_commit += " `cards_yellow_91_105_percentage` = '"+str(cards_yellow_91_105_percentage)+"', "

        query_commit += " `cards_yellow_106_120_total` = '"+str(cards_yellow_106_120_total)+"', "
        query_commit += " `cards_yellow_106_120_percentage` = '"+str(cards_yellow_106_120_percentage)+"', "

        query_commit += " `cards_red_0_15_total` = '"+str(cards_red_0_15_total)+"', "
        query_commit += " `cards_red_0_15_percentage` = '"+str(cards_red_0_15_percentage)+"', "

        query_commit += " `cards_red_16_30_total` = '"+str(cards_red_16_30_total)+"', "
        query_commit += " `cards_red_16_30_percentage` = '"+str(cards_red_16_30_percentage)+"', "

        query_commit += " `cards_red_31_45_total` = '"+str(cards_red_31_45_total)+"', "
        query_commit += " `cards_red_31_45_percentage` = '"+str(cards_red_31_45_percentage)+"', "

        query_commit += " `cards_red_46_60_total` = '"+str(cards_red_46_60_total)+"', "
        query_commit += " `cards_red_46_60_percentage` = '"+str(cards_red_46_60_percentage)+"', "

        query_commit += " `cards_red_61_75_total` = '"+str(cards_red_61_75_total)+"', "
        query_commit += " `cards_red_61_75_percentage` = '"+str(cards_red_61_75_percentage)+"', "

        query_commit += " `cards_red_76_90_total` = '"+str(cards_red_76_90_total)+"', "
        query_commit += " `cards_red_76_90_percentage` = '"+str(cards_red_76_90_percentage)+"', "

        query_commit += " `cards_red_91_105_total` = '"+str(cards_red_91_105_total)+"', "
        query_commit += " `cards_red_91_105_percentage` = '"+str(cards_red_91_105_percentage)+"', " 

        query_commit += " `cards_red_106_120_total` = '"+str(cards_red_106_120_total)+"', "
        query_commit += " `cards_red_106_120_percentage` = '"+str(cards_red_106_120_percentage)+"' " 

        
        query_commit += " where leagueapi_id = "+str(DICTleagueapi_id)+" "    
        query_commit += " and season = "+str(DICTseason)+" "     
        query_commit += " and teamapi_id = "+str(DICTteam)+" "    

    
        print(space + "api_football_standings STATISTICS UPDATED", flush=True)  

        
        mycursor.execute(query_commit)
        mydb.commit()   
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")