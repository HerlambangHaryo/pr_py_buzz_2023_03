# Import
import mysql.connector 
from a_models.api_accounts import *   
from a_settings.messages import *   
from a_models.football_ultimate_assessment import *   
from a_models.date import *  
from a_models.api_fixtures_new import *   

import pytz
utc=pytz.UTC 

import requests
import json 
 
def aoN_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aoN_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0): 
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space)  
        aoN_response_odds(APIkey, DICT, PREP_, space)
    # ----------------------------------------------------------
  
def aoN_response_odds(APIkey, DICT, PREP_, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "aoN_response_odds()", flush=True) 
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"  
    # ----------------------------------------------------------   
    space += "__" 
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    if(PREP_ == "end_"):
        # ------------------------------------------------------ 
        DICTdate            = DICT['date']
        DICTbookmaker       = DICT['bookmaker']
        DICTseason          = DICT['season']
        DICTleague          = DICT['league']
        DICTpage            = DICT['page']
        DICTmax_page        = DICT['max_page']

        print(space + "date : " + str(DICTdate), flush=True)
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True)
        print(space + "season : " + str(DICTseason), flush=True)
        print(space + "league : " + str(DICTleague), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)

        querystring         = {"date":DICTdate, "bookmaker":DICTbookmaker, "season":DICTseason, "league":DICTleague, "page":DICTpage}
        # ------------------------------------------------------ 
        XPREP_ = "end_"
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------  
    # ----------------------------------------------------------
    elif(PREP_ == "pre_"):
        # ------------------------------------------------------
        DICTdate_0          = DICT['date_0']
        DICTpage            = DICT['page']
        DICTcounter_loop    = DICT['counter_loop']
        DICTdate_diff       = DICT['date_diff']
        DICTdate_raw        = DICT['date_raw']
        DICTmax_page        = DICT['max_page']

        print(space + "date_0 : " + str(DICTdate_0), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)
        print(space + "counter_loop : " + str(DICTcounter_loop), flush=True)
        print(space + "date_diff : " + str(DICTdate_diff), flush=True)
        print(space + "date_raw : " + str(DICTdate_raw), flush=True)
        print(space + "max_page : " + str(DICTmax_page), flush=True)
         
        querystring         = {"date":DICTdate_0, "page":DICTpage}
        # ------------------------------------------------------ 
        XPREP_ = "pre_"
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
    elif(PREP_ == "one_"):
        # ------------------------------------------------------ 
        DICTfixture = DICT['fixture'] 
        DICTbookmaker = DICT['bookmaker'] 
        DICTmax_page        = DICT['max_page']
        DICTpage            = DICT['page']
        DICTmax_page        = DICT['max_page']

        print(space + "fixture : " + str(DICTfixture), flush=True) 
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True) 

        querystring = {"fixture":DICTfixture, "bookmaker":DICTbookmaker }

        PREP_ = "end_"
        XPREP_ = "one_"
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------  
    elif(PREP_ == "preone_"):
        # ------------------------------------------------------ 
        DICTfixture = DICT['fixture'] 
        DICTbookmaker = DICT['bookmaker'] 
        DICTdate_raw        = DICT['date_raw']
        DICTmax_page        = DICT['max_page']

        print(space + "fixture : " + str(DICTfixture), flush=True) 
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True) 

        querystring = {"fixture":DICTfixture, "bookmaker":DICTbookmaker }

        PREP_ = "pre_"
        XPREP_ = "preone_"
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
    elif(PREP_ == "preleague_"):
        # ------------------------------------------------------ 
        DICTdate_0          = DICT['date']
        DICTdate_raw        = DICT['date_raw']
        DICTbookmaker       = DICT['bookmaker']
        DICTseason          = DICT['season']
        DICTleague          = DICT['league']
        DICTpage            = DICT['page']
        DICTcounter_loop    = DICT['counter_loop']
        DICTdate_diff       = DICT['date_diff'] 
        DICTmax_page        = DICT['max_page']

        print(space + "date : " + str(DICTdate_0), flush=True)
        print(space + "date_raw : " + str(DICTdate_raw), flush=True)
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True)
        print(space + "season : " + str(DICTseason), flush=True)
        print(space + "league : " + str(DICTleague), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)

        # querystring = {"date":DICTdate_0, "bookmaker":DICTbookmaker, "season":DICTseason, "league":DICTleague, "page":DICTpage}
        querystring = {"bookmaker":DICTbookmaker, "season":DICTseason, "league":DICTleague, "page":DICTpage}

        PREP_ = "pre_"
        XPREP_ = "preleague_"
        # ----------------------------------------------------------
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
        if(DICTpage == 1):
            total_MAX_PAGE  = d['paging']['total']
        else:
            total_MAX_PAGE  = DICTmax_page
        # ----------------------------------------------------------   
        print(space + "total_MAX_PAGE : " + str(total_MAX_PAGE), flush=True)  
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
                # ------------------------------------------------------------------------------------ # Initialize Response 
                counter_response            += 1 
                ags_update                  = "" 
                ags_val                     = ""
                rbs_odds                    = ""
                first_gs_val                = ""
                last_gs_val                 = ""
                score_more_gs_val           = ""
                last2_gs_val                = ""
                exact_gs_val                = ""
                player_to_be_booked_val     = ""
                special_odds                = ""
                # -------------------------------------------------- 
                array_special_odds          = ["1.83", "1.98"]
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # ------------------------------------------------------------------------------------ # Initialize Response
                leagueapi_id        = str(i['league']['id']) 
                # -------------------------------------------------- 
                # print(space + "leagueapi_id: " + leagueapi_id, flush=True) 
                # -------------------------------------------------- 
                leagueapi_season    = str(i['league']['season']) 
                # -------------------------------------------------- 
                # print(space + "leagueapi_season: " + leagueapi_season, flush=True) 
                # -------------------------------------------------- 
                fixtureapi_id       = str(i['fixture']['id'])
                # -------------------------------------------------- 
                leagueapi_country   = str(i['league']['country'])
                leagueapi_name      = str(i['league']['name'])
                # -------------------------------------------------- 
                fixture_date_now    = datetime.fromisoformat(i['fixture']['date'])
                # -------------------------------------------------- 
                fixture_date        = str(fixture_date_now)
                # -------------------------------------------------- 
                # print(space + "fixture_date: " + fixture_date, flush=True) 
                # -------------------------------------------------- 
                fixture_date_local  = fixture_date_now.replace(tzinfo=pytz.UTC).astimezone(local) 
                # -------------------------------------------------- 
                fixture_timezone      = str(i['fixture']['timezone'])
                # -------------------------------------------------- 
                # print(space + "fixture_timezone: " + fixture_timezone, flush=True)  
                # -------------------------------------------------- 
                bookmakers_Array    = i['bookmakers']  
                # -------------------------------------------------- 
                print(current_space, flush=True) 
                # -------------------------------------------------- 
                word = current_space + str(counter_response) + "/" + str(total_API_response) + " "
                print(word, flush=True)
                # -------------------------------------------------- 
                word = current_space + leagueapi_country + ",  "
                word += leagueapi_name + " "
                word += " #" + leagueapi_id + " - " + leagueapi_season 
                print(word, flush=True)
                # --------------------------------------------------  
                word = current_space + fixture_date  + " // " +fixture_timezone + " // " +  fixtureapi_id
                print(word, flush=True)
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------------------------------------- # CHECK Football_odds
                aoN_football_odds_check(leagueapi_id, leagueapi_season, fixtureapi_id, fixture_date_now, current_space)
                # --------------------------------------------------   
                # --------------------------------------------------   
                # --------------------------------------------------   
                if(PREP_ == "end_"):
                    # ---------------------------------------------- 
                    PREP_check_date = 1 
                    # ----------------------------------------------
                    # ----------------------------------------------
                # -------------------------------------------------- 
                elif(PREP_ == "pre_"):  
                    # ----------------------------------------------  
                    fix_local           = fixture_date_local.strftime("%Y-%m-%d %H:%M:%S")
                    local_date          = local.localize(DICTdate_raw).strftime("%Y-%m-%d %H:%M:%S")
                    # ----------------------------------------------  
                    # -------------------------------------------------------------------------------- # CHECK football_statistics
                    total_football_statistic_row = aoN_football_statistics_check(leagueapi_id, leagueapi_season, fixtureapi_id, str(fix_local), bookmakers_Array, current_space) 
                    # ----------------------------------------------  
                    # ----------------------------------------------   
                    # print(current_space, flush=True) 
                    # ----------------------------------------------   
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    current_space += "__" 
                    # ---------------------------------------------- 
                    PREP_check_date = 0
                    # ---------------------------------------------- 
                    # word = current_space + "fixt date " + str(fixture_date)  
                    # print(word, flush=True)
                    # # ---------------------------------------------- 
                    # word = current_space + "fixture to local " +  str(fix_local) 
                    # print(word, flush=True)
                    # # ----------------------------------------------  
                    # word = current_space + "local_date " + str(local_date) 
                    # print(word, flush=True) 
                    # ----------------------------------------------
                    if(fix_local >= local_date):
                        # ------------------------------------------
                        date_status = '__________Lebih ' + str(fix_local) + ' >= ' + str(local_date) 
                        print(current_space + date_status, flush=True) 
                        # ------------------------------------------ 
                        if(total_football_statistic_row == 1): 
                            # -------------------------------------- 
                            PREP_check_date = 1
                            # --------------------------------------
                    # ---------------------------------------------- 
                    elif(fix_local < local_date):
                        # ------------------------------------------  
                        date_status = '__________Kurang ' + str(fix_local) + ' < ' + str(local_date) 
                        print(current_space + date_status, flush=True)  
                        # ------------------------------------------ 
                        PREP_check_date == 0
                        # ------------------------------------------   
                    # ----------------------------------------------  
                # --------------------------------------------------  
                # --------------------------------------------------  
                # --------------------------------------------------  
                # --------------------------------------------------  
                # --------------------------------------------------  
                if(PREP_check_date == 1): 
                    # ----------------------------------------------
                    for ba in bookmakers_Array:
                        # ------------------------------------------
                        bookmakersapi_id    = ba['id']
                        bookmakersapi_name  = ba['name']   
                        # ------------------------------------------
                        bets_Array          = ba['bets']
                        # ------------------------------------------ 
                        # -------------------------------------- 
                        for bta in bets_Array:
                            # --------------------------------------
                            bets_name           = bta['name']
                            bets_id             = bta['id'] 
                            # --------------------------------------
                            betsvalues_array    = bta['values']
                            # -------------------------------------- 
                            # -------------------------------------- 
                            for bva in betsvalues_array: 
                                # ----------------------------------
                                bets_value      = bva['value']
                                bets_odd        = bva['odd']
                                # ----------------------------------
                                # ----------------------------------
                                bet_id_list = [
                                                1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 19, 20, 
                                                21, 24, 25, 26, 27, 28, 32, 34, 35, 36, 38, 39, 40
                                                , 41, 42, 45, 46, 48, 49, 52, 55, 56, 57, 58, 
                                                73, 74, 75, 76, 79, 80, 81, 82, 83, 86, 91, 97, 99
                                                , 100
                                            ] 
                                
                                # ----------------------------------
                                if bets_id in bet_id_list:  
                                    # ----------------------------------
                                    # print( current_space, flush=True) 
                                    # ----------------------------------  
                                    odds_code = '$' + str(bets_id) + '_' + str(bets_value) + '$' 
                                    # print( current_space + "odds_code: " +  odds_code, flush=True) 
                                    # ----------------------------------  
                                    NEW_colx = bet_id_list_to_colx(odds_code, PREP_, bets_odd) 
                                    # ----------------------------------
                                    if(NEW_colx is not None):
                                        # ------------------------------
                                        # print( current_space + str(NEW_colx), flush=True)  
                                        # ------------------------------
                                        pre_set = NEW_colx
                                        rbs_odds += pre_set 
                                        # ------------------------------
                                    # ----------------------------------
                                    # ----------------------------------
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ----------------------------------
                                #     host="localhost"
                                #     user="root" 
                                #     database="pr_mmbuzz_2022_06"
                                #     mydb2 = mysql.connector.connect(host=host,user=user,password="",database=database)
                                #     # ------------------------------
                                #     query_bets = " Select columnx, category  "
                                #     query_bets += " from bets_old "  
                                #     query_bets += " where bet_id = '"+str(bets_id)+"' "  
                                #     query_bets += " and value like '"+str(bets_value)+"' " 
                                #     # ------------------------------
                                #     mycursor2 = mydb2.cursor() 
                                #     mycursor2.execute(query_bets)
                                #     result_bets2 = mycursor2.fetchall()
                                #     # ------------------------------
                                #     mycursor2.close()
                                #     mydb2.close() 
                                #     # ------------------------------
                                #     for rbs in result_bets2:
                                #         # --------------------------
                                #         colmnx       = rbs[0]  
                                #         category     = rbs[1] 
                                #         # --------------------------
                                #         pre_set = PREP_ + colmnx + " = '" + bets_odd + "', " 
                                #         rbs_odds += pre_set 
                                #         # -------------------------- 
                                #         if str(bets_odd) in array_special_odds:  
                                #             special_odds = 1  
                                #         # --------------------------
                                #         # --------------------------
                                #     # ------------------------------
                                #     # ------------------------------ 
                                # # ---------------------------------- 
                                elif(bets_id == 92): 
                                    # ------------------------------ 
                                    # Anytime goalscorer
                                    pre_ags_val = bets_value + ":" + str(bets_odd) + ";" 
                                    ags_val += pre_ags_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 93):
                                    # ------------------------------ 
                                    # First goalscorer
                                    pre_first_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    first_gs_val += pre_first_gs_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 94):
                                    # ------------------------------ 
                                    # Last goalscorer
                                    pre_last_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    last_gs_val += pre_last_gs_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 95):
                                    # ------------------------------ 
                                    # one or more goalscorer
                                    pre_score_more_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    score_more_gs_val += pre_score_more_gs_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 96):
                                    # ------------------------------ 
                                    # Last goalscorer
                                    pre_last2_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    last2_gs_val += pre_last2_gs_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 10):
                                    # ------------------------------ 
                                    # Exact
                                    pre_exact_gs_val = bets_value + "-" + str(bets_odd) + ";"  
                                    exact_gs_val += pre_exact_gs_val 
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                elif(bets_id == 102):
                                    # ------------------------------ 
                                    # Booked
                                    pre_player_to_be_booked_val = bets_value + ":" + str(bets_odd) + ";"  
                                    player_to_be_booked_val += pre_player_to_be_booked_val
                                    # ------------------------------ 
                                    if str(bets_odd) in array_special_odds:  
                                        special_odds = 1  
                                    # ------------------------------ 
                                    # ------------------------------ 
                                # ---------------------------------- 
                                else:  
                                # ---------------------------------- 
                                    hai = ""
                                    # ------------------------------ 
                                    # ------------------------------ 
                                    # ------------------------------ 
                            # --------------------------------------
                            # --------------------------------------
                        # ------------------------------------------
                    # ----------------------------------------------   
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # pre_anytime_goal_scorer  
                    # pre_first_goal_scorer  
                    # pre_last_goal_scorer 
                    # pre_to_score_two_or_more_goals 
                    # pre_last_goal_scorer2 
                    # pre_exact_score 
                    # pre_player_to_be_booked  
                    ags_update += " "+PREP_+"anytime_goal_scorer = '"+ags_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"first_goal_scorer = '"+first_gs_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"last_goal_scorer = '"+last_gs_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"to_score_two_or_more_goals = '"+score_more_gs_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"last_goal_scorer2 = '"+last2_gs_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"exact_score = '"+exact_gs_val.replace("'", "\\'")+"', "
                    ags_update += " "+PREP_+"player_to_be_booked = '"+player_to_be_booked_val.replace("'", "\\'")+"', "
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ----------------------------------------------   
                    if(XPREP_ == 'one_'):
                        fixture_status_update = " fixture_status = 'Not Started One', "
                    elif(XPREP_ == 'end_'):
                        fixture_status_update = " fixture_status = 'Match Finished Ended', "
                    elif(XPREP_ == 'pre_'):
                        fixture_status_update = " fixture_status = 'Not Started Goto', "
                    elif(XPREP_ == 'preleague_'):
                        fixture_status_update = " fixture_status = 'Not Started Goto', "
                    elif(XPREP_ == 'preone_'):
                        fixture_status_update = " fixture_status = 'Not Started Goto', "
                    # ---------------------------------------------- 
                    if(XPREP_ == 'preleague_'):
                        response_update = " "+PREP_+"response = 1, "
                    elif(XPREP_ == 'preone_'):
                        response_update = " "+PREP_+"response = 1, "
                    elif(XPREP_ == 'one_'):
                        response_update = " "+XPREP_+"response = 1, "
                    else:
                        response_update = " "+XPREP_+"response = 1, "
                    # ----------------------------------------------  
                    if(XPREP_ == 'preleague_'):
                        odd_updated_at_update = " "+PREP_+"odd_updated_at = current_timestamp, "
                    elif(XPREP_ == 'preone_'):
                        odd_updated_at_update = " "+PREP_+"odd_updated_at = current_timestamp, "
                    elif(XPREP_ == 'one_'):
                        odd_updated_at_update = " "+PREP_+"odd_updated_at = current_timestamp, "
                    else:
                        odd_updated_at_update = " "+XPREP_+"odd_updated_at = current_timestamp, "
                    # ----------------------------------------------  
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ----------------------------------------------   
                    if(special_odds == ''):
                        # ------------------------------------------  
                        if(XPREP_ == 'preleague_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = Null "
                            # --------------------------------------
                        # ------------------------------------------
                        elif(XPREP_ == 'one_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = Null "
                            # --------------------------------------
                        # ------------------------------------------
                        elif(XPREP_ == 'preone_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = Null "
                            # --------------------------------------
                        # ------------------------------------------
                        else: 
                            # --------------------------------------
                            special_odds_update = " "+XPREP_+"special_odds = Null "
                            # --------------------------------------
                        # ------------------------------------------
                    elif(special_odds != ''): 
                        # ------------------------------------------
                        if(XPREP_ == 'preleague_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = '"+str(special_odds)+"' " 
                            # --------------------------------------   
                            fua_update_or_insert(leagueapi_id, 
                                leagueapi_season, 
                                fixtureapi_id, 
                                fixture_date,
                                PREP_+"special_odds", 
                                1, 
                                current_space)
                            # -------------------------------------- 
                        # ------------------------------------------
                        elif(XPREP_ == 'one_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = '"+str(special_odds)+"' " 
                            # --------------------------------------   
                            fua_update_or_insert(leagueapi_id, 
                                leagueapi_season, 
                                fixtureapi_id, 
                                fixture_date,
                                PREP_+"special_odds", 
                                1, 
                                current_space)
                            # -------------------------------------- 
                        # ------------------------------------------
                        elif(XPREP_ == 'preone_'):
                            # --------------------------------------
                            special_odds_update = " "+PREP_+"special_odds = '"+str(special_odds)+"' " 
                            # --------------------------------------   
                            fua_update_or_insert(leagueapi_id, 
                                leagueapi_season, 
                                fixtureapi_id, 
                                fixture_date,
                                PREP_+"special_odds", 
                                1, 
                                current_space)
                            # -------------------------------------- 
                        # ------------------------------------------
                        else:  
                            # --------------------------------------
                            special_odds_update = " "+XPREP_+"special_odds = '"+str(special_odds)+"' " 
                            # --------------------------------------   
                            fua_update_or_insert(leagueapi_id, 
                                leagueapi_season, 
                                fixtureapi_id, 
                                fixture_date,
                                XPREP_+"special_odds", 
                                1, 
                                current_space)
                            # --------------------------------------
                        # ------------------------------------------
                        # ------------------------------------------
                        # ------------------------------------------
                        # ------------------------------------------
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    fixture_UPDATE_DATE = " date = '"+fixture_date+"', "
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # -------------------------------------------------------------------------------- # UPDATE 
                    # ---------------------------------------------- 
                    host="localhost"
                    user="root" 
                    database="pr_mmbuzz_2022_06"
                    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                    mycursor = mydb.cursor()
                    # ----------------------------------------------   
                    query_commit = "update football_odds set "   
                    # ----------------------------------------------  
                    query_commit += rbs_odds
                    # ----------------------------------------------  
                    query_commit += ags_update
                    # ----------------------------------------------  
                    query_commit += fixture_status_update     
                    # ----------------------------------------------  
                    query_commit += response_update           
                    # ----------------------------------------------  
                    query_commit += odd_updated_at_update         
                    # ----------------------------------------------  
                    query_commit += fixture_UPDATE_DATE              
                    # ----------------------------------------------  
                    query_commit += special_odds_update
                    # ----------------------------------------------  
                    query_commit += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
                    query_commit += " and leagueapi_id = '"+str(leagueapi_id)+"' "
                    query_commit += " and season = '"+str(leagueapi_season)+"' "
                    # ----------------------------------------------  
                    # print(current_space + query_commit, flush=True)  
                    # ----------------------------------------------  
                    mycursor.execute(query_commit)
                    mydb.commit()  
                    # ----------------------------------------------  
                    mycursor.close()
                    mydb.close() 
                    # ----------------------------------------------  
                    print(current_space + "football_odds UPDATED", flush=True) 
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # -------------------------------------------------------------------------------- # UPDATE 
                    # ---------------------------------------------- 
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    host="localhost"
                    user="root" 
                    database="pr_mmbuzz_2022_06"
                    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                    mycursor = mydb.cursor()
                    # ----------------------------------------------   
                    # ----------------------------------------------   
                    query_commit = "update football_fixtures set "   
                    # ---------------------------------------------- 
                    query_commit += " date = '"+fixture_date+"' "
                    # ---------------------------------------------- 
                    query_commit += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
                    query_commit += " and leagueapi_id = '"+str(leagueapi_id)+"' "
                    query_commit += " and season = '"+str(leagueapi_season)+"' "
                    # ----------------------------------------------  
                    # print(current_space + query_commit, flush=True)  
                    # ----------------------------------------------  
                    mycursor.execute(query_commit)
                    mydb.commit()  
                    # ----------------------------------------------  
                    mycursor.close()
                    mydb.close() 
                    # ----------------------------------------------  
                    print(current_space + "football_fixtures UPDATED", flush=True) 
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # ----------------------------------------------  
                    # -------------------------------------------------------------------------------- # Statement Updated
                    if(PREP_ == "end_" and XPREP_ == "end_"):
                        aoN_football_fixtures_match_finished_ended(leagueapi_id, leagueapi_season, fixtureapi_id, current_space)
                    # ----------------------------------------------  
                    elif(PREP_ == "pre_"):
                        aoN_football_fixtures_not_started_goto(leagueapi_id, leagueapi_season, fixtureapi_id, current_space)
                    # ----------------------------------------------  
                    # ----------------------------------------------  


                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    
                elif(PREP_check_date == 0):
                    # ---------------------------------------------- 
                    print(current_space + "PREP_check_date is not valid", flush=True) 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 
                    # ---------------------------------------------- 

                    
            # # -------------------------------------------------------------------------------- # RE-LOOP RESPONSE = 10 
            # # ---------------------------------------------- 
            if(total_API_response == 10 and DICTpage <= total_MAX_PAGE):
                # ------------------------------------------ 
                print(current_space + "RE-LOOP RESPONSE", flush=True)
                # ------------------------------------------ 
                DICTpage += 1
                # ------------------------------------------ 
                if(PREP_ == "end_"):
                    # -------------------------------------- 
                    DICT = { 
                        "date" : DICTdate,
                        "bookmaker" : DICTbookmaker,
                        "season" : DICTseason,
                        "league" : DICTleague,
                        "page" : DICTpage, 
                        'max_page'  : total_MAX_PAGE
                    } 
                    # -------------------------------------- 
                    aoN_controll_match_update(DICT, 'end_', "____") 
                    # -------------------------------------- 
                    # -------------------------------------- 
                    # --------------------------------------  
                # ------------------------------------------  
                elif(XPREP_ == "pre_"): 
                    # -------------------------------------- 
                    DICT = {
                        'date_0' : DICTdate_0,
                        'page' : DICTpage,
                        'counter_loop' : DICTcounter_loop,
                        'date_diff' : DICTdate_diff,
                        'date_raw' : DICTdate_raw,
                        'max_page'  : total_MAX_PAGE
                    }
                    # -------------------------------------- 
                    aoN_controll_match_update(DICT, 'pre_', "____") 
                    # -------------------------------------- 
                    # -------------------------------------- 
                    # --------------------------------------  
                # ------------------------------------------  
                elif(XPREP_ == "preleague_"): 
                    # --------------------------------------   
                    DICT = {
                        'date' : DICTdate_0,
                        'date_raw' : DICTdate_raw,
                        'league' : DICTleague,
                        'season' : DICTseason,
                        'bookmaker' : DICTbookmaker,
                        'page' : DICTpage,
                        'counter_loop' : DICTcounter_loop,
                        'date_diff' : DICTdate_diff, 
                        'max_page'  : total_MAX_PAGE
                    } 
                    # -------------------------------------- 
                    aoN_controll_match_update(DICT, 'preleague_', "____") 
                    # -------------------------------------- 
                    # -------------------------------------- 
                    # --------------------------------------   
                elif(XPREP_ == "preone_"): 
                    # --------------------------------------    
                    DICT = {
                        'date' : DICTdate_0,
                        'date_raw' : DICTdate_raw,
                        'league' : DICTleague,
                        'season' : DICTseason,
                        'bookmaker' : DICTbookmaker,
                        'page' : DICTpage,
                        'counter_loop' : DICTcounter_loop,
                        'date_diff' : DICTdate_diff, 
                        'max_page'  : total_MAX_PAGE
                    } 
                    # -------------------------------------- 
                    aoN_controll_match_update(DICT, 'preone_', "____") 
                    # -------------------------------------- 
                    # -------------------------------------- 
                    # --------------------------------------  
                # ------------------------------------------  
            # -------------------------------------------------------------------------------- # STOP RESPONSE < 10 
            # ---------------------------------------------- 
            elif(total_API_response < 10): 
                # ------------------------------------------ 
                print(current_space + "STOP RESPONSE", flush=True)
                # ------------------------------------------
                # ------------------------------------------
                # ------------------------------------------
                
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
        elif(total_API_response == 0):
            # ------------------------------------------------------
            print(current_space + "SKIPPED because its Nothing total_API_response:" + str(total_API_response), flush=True) 
        # ----------------------------------------------------------  
        # ----------------------------------------------------------
        # ----------------------------------------------------------
        # ----------------------------------------------------------
    
    except KeyError: 
        print("KeyErrorKeyErrorKeyError")

def aoN_football_odds_check(leagueapi_id, season, fixtureapi_id, date, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "aoN_football_odds_check()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------
    query = " select count(*) "   
    query += " from football_odds "   
    query += " where leagueapi_id = '" + str(leagueapi_id) + "'"   
    query += " and season = '" + str(season) + "'"   
    query += " and fixtureapi_id = '" + str(fixtureapi_id) + "'"   
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    result_check = mycursor.fetchone()
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    total_rows = result_check[0]
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "aoN_football_odds_check: " +str(total_rows), flush=True)
    # ----------------------------------------------------------
    if(total_rows == 0):
        # ------------------------------------------------------
        aoN_football_odds_insert_rows(leagueapi_id, season, fixtureapi_id, date, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def aoN_football_odds_insert_rows(leagueapi_id, season, fixtureapi_id, date, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aoN_football_odds_insert_rows()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------
    query_commit = "INSERT INTO `football_odds`( "
    # ----------------------------------------------------------
    query_commit += " `date`, "
    query_commit += " `fixtureapi_id`, " 
    query_commit += " `leagueapi_id`, "
    query_commit += " `season`, " 
    # ----------------------------------------------------------
    query_commit += " `created_at` "   
    # ----------------------------------------------------------
    query_commit += " ) VALUES ( "
    # ----------------------------------------------------------
    query_commit += " '" + str(date) + "', " 
    query_commit += " " + str(fixtureapi_id) + ", "  
    query_commit += " " + str(leagueapi_id) + ", " 
    query_commit += " " + str(season) + ", "  
    query_commit += " current_timestamp "    
    # ----------------------------------------------------------
    query_commit += " ) "
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    mydb.commit()   
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    print(space + "football_odds INSERTED", flush=True) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  


def aoN_football_fixtures_not_started_goto(leagueapi_id, season, fixtureapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "aoN_football_fixtures_not_started_goto()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ---------------------------------------------------------- 
    query_commit = "update football_fixtures set "  
    # ---------------------------------------------------------- 
    query_commit += " fixture_status = 'Not Started Goto', "   
    query_commit += " updated_at = current_timestamp " 
    # ----------------------------------------------------------
    query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "  
    query_commit += " and leagueapi_id = '"+leagueapi_id+"' "
    query_commit += " and season = '"+season+"' "
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    mydb.commit()  
    # ----------------------------------------------------------
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    print(space + "football_fixtures "+fixtureapi_id+" UPDATED Not Started Goto", flush=True) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def aoN_football_fixtures_match_finished_ended(leagueapi_id, season, fixtureapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "aoN_football_fixtures_match_finished_ended()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ---------------------------------------------------------- 
    query_commit = "update football_fixtures set "  
    # ---------------------------------------------------------- 
    query_commit += " fixture_status = 'Match Finished Ended', "   
    query_commit += " updated_at = current_timestamp " 
    # ----------------------------------------------------------
    query_commit += " where fixtureapi_id = '"+fixtureapi_id+"' "  
    query_commit += " and leagueapi_id = '"+leagueapi_id+"' "
    query_commit += " and season = '"+season+"' "
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    mydb.commit()  
    # ----------------------------------------------------------
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    print(space + "football_fixtures "+fixtureapi_id+" UPDATED match finished ended", flush=True) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def aoN_football_statistics_check(leagueapi_id, season, fixtureapi_id, date, bookmakers_Array, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aoN_football_statistics_check()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ---------------------------------------------------------- 
    query = " select "   
    query += " count(*) "    
    query += " , (select name FROM football_leagues WHERE leagueapi_id = fF.leagueapi_id ) as  name "   
    query += " , (select country_name FROM football_leagues WHERE leagueapi_id = fF.leagueapi_id ) as  country_name "     

    query += " , (select name FROM football_teams WHERE teamapi_id = fF.teams_homeapi_id ) as name_home "  
    query += " , (select name FROM football_teams WHERE teamapi_id = fF.teams_awayapi_id ) as name_away "     

    query += " , (select bookmakersapi_id FROM football_leagues WHERE leagueapi_id = fF.leagueapi_id ) as  bookmakersapi_id "    

    query += " FROM football_fixtures fF "     

    query += " where fF.leagueapi_id = '" + str(leagueapi_id) + "'"   
    query += " and fF.season = '" + str(season) + "'"   
    query += " and fF.fixtureapi_id = '" + str(fixtureapi_id) + "'"  
    # ----------------------------------------------------------   
    # print(space + query, flush=True)
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    result_check = mycursor.fetchone()
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    total_rows          = result_check[0]
    # ----------------------------------------------------------  
    league_name         = result_check[1]
    league_country      = result_check[2]
    # ----------------------------------------------------------  
    name_home           = result_check[3]
    name_away           = result_check[4]
    # ----------------------------------------------------------  
    bookmakersapi_id    = str(result_check[5])
    # ---------------------------------------------------------- 
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "aoN_football_statistics_check: " +str(total_rows), flush=True)
    # ---------------------------------------------------------- 
    space += "__"
    # ----------------------------------------------------------
    if(total_rows == 1):
        # ------------------------------------------------------ 
        word = space + str(league_country) + ",  "
        word += league_name + " - " 
        word += str(season) + " __ " 
        word += str(fixtureapi_id) + " __ "
        word += date  + " __ "
        word += bookmakersapi_id   
        print(word, flush=True) 
        # ------------------------------------------------------ 
        word = space + "__________"
        word += str(name_home) + " vs "
        word += str(name_away)  
        print(word, flush=True) 
        # ------------------------------------------------------ 
    # ----------------------------------------------------------
    if(total_rows == 0 or bookmakersapi_id is None or bookmakersapi_id == 0): 
        # ------------------------------------------------------ 
        bookmakersapi_id_NEW = aoN_football_leagues_check(leagueapi_id, space)
        # ------------------------------------------------------ 
        if(bookmakersapi_id_NEW == 0):
            # -------------------------------------------------- 
            for ba in bookmakers_Array:
                # ---------------------------------------------- 
                bookmakersapi_id        = str(ba['id'])
                bookmakersapi_name      = str(ba['name']) 
                bets_Array              = ba['bets'] 
                bet_id_list_important   = [11, 8]
                # ---------------------------------------------- 
                if ba['id'] in bet_id_list_important:
                    # ------------------------------------------
                    word_belum_ada_bookm = bookmakersapi_id + " "  
                    word_belum_ada_bookm += bookmakersapi_name + " = "
                    word_belum_ada_bookm += str(len(bets_Array))
                    # ------------------------------------------
                    print(space + word_belum_ada_bookm, flush=True)  
                # ----------------------------------------------
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
        elif(bookmakersapi_id_NEW != 0):
            # -------------------------------------------------- 
            fixture_updated_at  =  get_today_adds(0, space) 
            # -------------------------------------------------- 
            DICT = {
                'fixtureapi_id' :fixtureapi_id,
                'fixture_updated_at' :fixture_updated_at, 
            }
            # ---------------------------------------------------------- 
            afN_controll_match_update(DICT, 'fixtureapi_id_INSERT', space) 
            # -------------------------------------------------- 
            total_rows = 1
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    return total_rows
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def aoN_football_leagues_check(leagueapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aoN_football_leagues_check()", flush=True)
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ---------------------------------------------------------- 
    query = " select "   
    query += " bookmakersapi_id"    

    query += " FROM football_leagues  "     

    query += " where leagueapi_id = '" + str(leagueapi_id) + "'"    
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
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------   
    bookm = total_rows
    # ----------------------------------------------------------   
    for x in result:     
        # ------------------------------------------------------
        bookm        = str(x[0])     
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    return bookm
    # ----------------------------------------------------------  


def bet_id_list_to_colx(target_string, PREP_, bets_odd):
    # ----------------------------------------------------------   
    bils = [  
        "$1_Home$match_winner_home",  #1
        "$1_Draw$match_winner_draw",  #2
        "$1_Away$match_winner_away",  #3
        "$2_Home$homeaway_home",  #4
        "$2_Away$homeaway_away",  #5
        "$3_Home$second_half_winner_home",  #6
        "$3_Draw$second_half_winner_draw",  #7
        "$3_Away$second_half_winner_away",  #8
        "$4_Home +0$asian_handicap_home_plus_0",  #9
        "$4_Away +0$asian_handicap_away_plus_0",  #10
        "$4_Home -0.25$asian_handicap_home_min_025",  #11
        "$4_Away -0.25$asian_handicap_away_min_025",  #12
        "$4_Home +0.25$asian_handicap_home_plus_025",  #13
        "$4_Away +0.25$asian_handicap_away_plus_025",  #14
        "$4_Home +0.5$asian_handicap_home_plus_05",  #15
        "$4_Away +0.5$asian_handicap_away_plus_05",  #16
        "$4_Home +0.75$asian_handicap_home_plus_075",  #17
        "$4_Away +0.75$asian_handicap_away_plus_075",  #18
        "$4_Home +1$asian_handicap_home_plus_1",  #19
        "$4_Away +1$asian_handicap_away_plus_1",  #20
        "$4_Home +1.5$asian_handicap_home_plus_15",  #21
        "$4_Away +1.5$asian_handicap_away_plus_15",  #22
        "$4_Home +1.25$asian_handicap_home_plus_125",  #23
        "$4_Away +1.25$asian_handicap_away_plus_125",  #24
        "$4_Home +1.75$asian_handicap_home_plus_175",  #25
        "$4_Away +1.75$asian_handicap_away_plus_175",  #26
        "$5_Over 3.5$goals_overunder_over_35",  #27
        "$5_Under 3.5$goals_overunder_under_35",  #28
        "$5_Over 1.5$goals_overunder_over_15",  #29
        "$5_Under 1.5$goals_overunder_under_15",  #30
        "$5_Over 4.5$goals_overunder_over_45",  #31
        "$5_Under 4.5$goals_overunder_under_45",  #32
        "$5_Over 2.5$goals_overunder_over_25",  #33
        "$5_Under 2.5$goals_overunder_under_25",  #34
        "$5_Over 0.5$goals_overunder_over_05",  #35
        "$5_Under 0.5$goals_overunder_under_05",  #36
        "$5_Over 5.5$goals_overunder_over_55",  #37
        "$5_Under 5.5$goals_overunder_under_55",  #38
        "$5_Over 3.25$goals_overunder_over_325",  #39
        "$5_Under 3.25$goals_overunder_under_325",  #40
        "$5_Over 2.75$goals_overunder_over_275",  #41
        "$5_Under 2.75$goals_overunder_under_275",  #42
        "$5_Over 4.25$goals_overunder_over_425",  #43
        "$5_Under 4.25$goals_overunder_under_425",  #44
        "$5_Over 1.75$goals_overunder_over_175",  #45
        "$5_Under 1.75$goals_overunder_under_175",  #46
        "$5_Over 3.75$goals_overunder_over_375",  #47
        "$5_Under 3.75$goals_overunder_under_375",  #48
        "$5_Over 4.75$goals_overunder_over_475",  #49
        "$5_Under 4.75$goals_overunder_under_475",  #50
        "$5_Over 6.5$goals_overunder_over_65",  #51
        "$5_Under 6.5$goals_overunder_under_65",  #52
        "$5_Over 7.5$goals_overunder_over_75",  #53
        "$5_Under 7.5$goals_overunder_under_75",  #54
        "$5_Over 5.25$goals_overunder_over_525",  #55
        "$5_Under 5.25$goals_overunder_under_525",  #56
        "$5_Over 8.5$goals_overunder_over_85",  #57
        "$5_Under 8.5$goals_overunder_under_85",  #58
        "$5_Over 3.0$goals_overunder_over_30",  #59
        "$5_Under 3.0$goals_overunder_under_30",  #60
        "$5_Over 2.0$goals_overunder_over_20",  #61
        "$5_Under 2.0$goals_overunder_under_20",  #62
        "$5_Over 4.0$goals_overunder_over_40",  #63
        "$5_Under 4.0$goals_overunder_under_40",  #64
        "$5_Over 5.0$goals_overunder_over_50",  #65
        "$5_Under 5.0$goals_overunder_under_50",  #66
        "$6_Over 3.5$goals_overunder_first_half_over_35",  #67
        "$6_Under 3.5$goals_overunder_first_half_under_35",  #68
        "$6_Over 1.5$goals_overunder_first_half_over_15",  #69
        "$6_Under 1.5$goals_overunder_first_half_under_15",  #70
        "$6_Over 2.5$goals_overunder_first_half_over_25",  #71
        "$6_Under 2.5$goals_overunder_first_half_under_25",  #72
        "$6_Over 0.5$goals_overunder_first_half_over_05",  #73
        "$6_Under 0.5$goals_overunder_first_half_under_05",  #74
        "$6_Over 2.25$goals_overunder_first_half_over_225",  #75
        "$6_Under 2.25$goals_overunder_first_half_under_225",  #76
        "$6_Over 2.75$goals_overunder_first_half_over_275",  #77
        "$6_Under 2.75$goals_overunder_first_half_under_275",  #78
        "$6_Over 1.25$goals_overunder_first_half_over_125",  #79
        "$6_Under 1.25$goals_overunder_first_half_under_125",  #80
        "$6_Over 1.75$goals_overunder_first_half_over_175",  #81
        "$6_Under 1.75$goals_overunder_first_half_under_175",  #82
        "$6_Over 0.75$goals_overunder_first_half_over_075",  #83
        "$6_Under 0.75$goals_overunder_first_half_under_075",  #84
        "$6_Over 2.0$goals_overunder_first_half_over_20",  #85
        "$6_Under 2.0$goals_overunder_first_half_under_20",  #86
        "$6_Over 1.0$goals_overunder_first_half_over_10",  #87
        "$6_Under 1.0$goals_overunder_first_half_under_10",  #88
        "$26_Over 3.5$goals_overunder__second_half_over_35",  #89
        "$26_Under 3.5$goals_overunder__second_half_under_35",  #90
        "$26_Over 1.5$goals_overunder__second_half_over_15",  #91
        "$26_Under 1.5$goals_overunder__second_half_under_15",  #92
        "$26_Over 2.5$goals_overunder__second_half_over_25",  #93
        "$26_Under 2.5$goals_overunder__second_half_under_25",  #94
        "$26_Over 0.5$goals_overunder__second_half_over_05",  #95
        "$26_Under 0.5$goals_overunder__second_half_under_05",  #96
        "$7_Home/Draw$htft_double_home_draw",  #97
        "$7_Home/Away$htft_double_home_away",  #98
        "$7_Draw/Away$htft_double_draw_away",  #99
        "$7_Draw/Draw$htft_double_draw_draw",  #100
        "$7_Home/Home$htft_double_home_home",  #101
        "$7_Draw/Home$htft_double_draw_home",  #102
        "$7_Away/Home$htft_double_away_home",  #103
        "$7_Away/Draw$htft_double_away_draw",  #104
        "$7_Away/Away$htft_double_away_away",  #105
        "$27_Yes$clean_sheet__home_yes",  #106
        "$27_No$clean_sheet__home_no",  #107
        "$28_Yes$clean_sheet__away_yes",  #108
        "$28_No$clean_sheet__away_no",  #109
        "$8_Yes$both_teams_score_yes",  #110
        "$8_No$both_teams_score_no",  #111
        "$11_Draw$highest_scoring_half_draw",  #112
        "$11_1st Half$highest_scoring_half_first",  #113
        "$11_2nd Half$highest_scoring_half_second",  #114
        "$12_Home/Draw$double_chance_home_draw",  #115
        "$12_Home/Away$double_chance_home_away",  #116
        "$12_Draw/Away$double_chance_draw_away",  #117
        "$13_Home$first_half_winner_home",  #118
        "$13_Draw$first_half_winner_draw",  #119
        "$13_Away$first_half_winner_away",  #120
        "$32_Home$win_both_halves_home",  #121
        "$32_Away$win_both_halves_away",  #122
        "$19_Home +0$asian_handicap_first_half_home_plus_0",  #123
        "$19_Away +0$asian_handicap_first_half_away_plus_0",  #124
        "$19_Home -0.25$asian_handicap_first_half_home_min_025",  #125
        "$19_Away -0.25$asian_handicap_first_half_away_min_025",  #126
        "$19_Home +0.25$asian_handicap_first_half_home_plus_025",  #127
        "$19_Away +0.25$asian_handicap_first_half_away_plus_025",  #128
        "$19_Home -0.5$asian_handicap_first_half_home_min_05",  #129
        "$19_Away -0.5$asian_handicap_first_half_away_min_05",  #130
        "$19_Home +0.5$asian_handicap_first_half_home_plus_05",  #131
        "$19_Away +0.5$asian_handicap_first_half_away_plus_05",  #132
        "$19_Home +0.75$asian_handicap_first_half_home_plus_075",  #133
        "$19_Away +0.75$asian_handicap_first_half_away_plus_075",  #134
        "$19_Home +1$asian_handicap_first_half_home_plus_1",  #135
        "$19_Away +1$asian_handicap_first_half_away_plus_1",  #136
        "$19_Home +1.5$asian_handicap_first_half_home_plus_15",  #137
        "$19_Away +1.5$asian_handicap_first_half_away_plus_15",  #138
        "$19_Home +1.25$asian_handicap_first_half_home_plus_125",  #139
        "$19_Away +1.25$asian_handicap_first_half_away_plus_125",  #140
        "$19_Home +1.75$asian_handicap_first_half_home_plus_175",  #141
        "$19_Away +1.75$asian_handicap_first_half_away_plus_175",  #142
        "$20_Home/Draw$double_chance__first_half_home_draw",  #143
        "$20_Home/Away$double_chance__first_half_home_away",  #144
        "$20_Draw/Away$double_chance__first_half_draw_away",  #145
        "$34_Yes$both_teams_score__first_half_yes",  #146
        "$34_No$both_teams_score__first_half_no",  #147
        "$35_Yes$both_teams_to_score__second_half_yes",  #148
        "$35_No$both_teams_to_score__second_half_no",  #149
        "$36_Home$win_to_nil_home",  #150
        "$36_Away$win_to_nil_away",  #151
        "$21_Odd$oddeven_odd",  #152
        "$21_Even$oddeven_even",  #153
        "$38_2$exact_goals_number_2",  #154
        "$38_3$exact_goals_number_3",  #155
        "$38_4$exact_goals_number_4",  #156
        "$38_1$exact_goals_number_1",  #157
        "$38_0$exact_goals_number_0",  #158
        "$38_5$exact_goals_number_5",  #159
        "$38_6$exact_goals_number_6",  #160
        "$38_more 7$exact_goals_number_more_7",  #161
        "$39_Home$to_win_either_half_home",  #162
        "$39_Away$to_win_either_half_away",  #163
        "$40_2$home_team_exact_goals_number_2",  #164
        "$40_1$home_team_exact_goals_number_1",  #165
        "$40_0$home_team_exact_goals_number_0",  #166
        "$40_more 3$home_team_exact_goals_number_more_3",  #167
        "$41_2$away_team_exact_goals_number_2",  #168
        "$41_1$away_team_exact_goals_number_1",  #169

        "$41_0$away_team_exact_goals_number_0",  #170
        "$41_more 3$away_team_exact_goals_number_more_3",  #171
        "$42_2$second_half_exact_goals_number_2",  #172
        "$42_3$second_half_exact_goals_number_3",  #173
        "$42_4$second_half_exact_goals_number_4",  #174
        "$42_1$second_half_exact_goals_number_1",  #175
        "$42_0$second_half_exact_goals_number_0",  #176
        "$42_more 5$second_half_exact_goals_number_more_5",  #177
        "$24_Home/Yes$results_both_teams_score_home_yes",  #178
        "$24_Draw/Yes$results_both_teams_score_draw_yes",  #179
        "$24_Away/Yes$results_both_teams_score_away_yes",  #180
        "$24_Home/No$results_both_teams_score_home_no",  #181
        "$24_Draw/No$results_both_teams_score_draw_no",  #182
        "$24_Away/No$results_both_teams_score_away_no",  #183
        "$25_Home/Over 3.5$result_total_goals_home_over_35",  #184
        "$25_Draw/Over 3.5$result_total_goals_draw_over_35",  #185
        "$25_Away/Over 3.5$result_total_goals_away_over_35",  #186
        "$25_Home/Under 3.5$result_total_goals_home_under_35",  #187
        "$25_Draw/Under 3.5$result_total_goals_draw_under_35",  #188
        "$25_Away/Under 3.5$result_total_goals_away_under_35",  #189
        "$25_Home/Over 2.5$result_total_goals_home_over_25",  #190
        "$25_Draw/Over 2.5$result_total_goals_draw_over_25",  #191
        "$25_Away/Over 2.5$result_total_goals_away_over_25",  #192
        "$25_Home/Under 2.5$result_total_goals_home_under_25",  #193
        "$25_Draw/Under 2.5$result_total_goals_draw_under_25",  #194
        "$25_Away/Under 2.5$result_total_goals_away_under_25",  #195
        "$55_Home$corners_winner_home",  #196
        "$55_Draw$corners_winner_draw",  #197
        "$55_Away$corners_winner_away",  #198
        "$46_2$exact_goals_number__first_half_2",  #199
        "$46_3$exact_goals_number__first_half_3",  #200
        "$46_4$exact_goals_number__first_half_4",  #201
        "$46_1$exact_goals_number__first_half_1",  #202
        "$46_0$exact_goals_number__first_half_0",  #203
        "$46_more 5$exact_goals_number__first_half_more_5",  #204
        "$48_Home$to_score_in_both_halves_by_teams_home",  #205
        "$48_Away$to_score_in_both_halves_by_teams_away",  #206
        "$49_o/yes 2.5$total_goals_both_teams_to_score_over_yes_25",  #207
        "$49_o/no 2.5$total_goals_both_teams_to_score_over_no_25",  #208
        "$49_u/yes 2.5$total_goals_both_teams_to_score_under_yes_25",  #209
        "$49_u/no 2.5$total_goals_both_teams_to_score_under_no_25",  #210
        "$52_Home/Yes$halftime_result_both_teams_score_home_yes",  #211
        "$52_Draw/Yes$halftime_result_both_teams_score_draw_yes",  #212
        "$52_Away/Yes$halftime_result_both_teams_score_away_yes",  #213
        "$52_Home/No$halftime_result_both_teams_score_home_no",  #214
        "$52_Draw/No$halftime_result_both_teams_score_draw_no",  #215
        "$52_Away/No$halftime_result_both_teams_score_away_no",  #216
        "$73_Yes/Yes$both_teams_to_score_1st_half__2nd_half_yes_yes",  #217
        "$73_Yes/No$both_teams_to_score_1st_half__2nd_half_yes_no",  #218
        "$73_No/Yes$both_teams_to_score_1st_half__2nd_half_no_yes",  #219
        "$73_No/No$both_teams_to_score_1st_half__2nd_half_no_no",  #220
        "$74_Over 0.5$10_overunder_over_05",  #221
        "$74_Under 0.5$10_overunder_under_05",  #222
        "$79_Home +0$cards_european_handicap_home_plus_0",  #223
        "$79_Away +0$cards_european_handicap_away_plus_0",  #224
        "$79_Draw +0$cards_european_handicap_draw_plus_0",  #225
        "$79_Home -1$cards_european_handicap_home_min_1",  #226
        "$79_Away -1$cards_european_handicap_away_min_1",  #227
        "$79_Draw -1$cards_european_handicap_draw_min_1",  #228
        "$79_Home +1$cards_european_handicap_home_plus_1",  #229
        "$79_Away +1$cards_european_handicap_away_plus_1",  #230
        "$79_Draw +1$cards_european_handicap_draw_plus_1",  #231
        "$79_Home +2$cards_european_handicap_home_plus_2",  #232
        "$79_Draw +2$cards_european_handicap_draw_plus_2",  #233
        "$79_Away +2$cards_european_handicap_away_plus_2",  #234
        "$79_Home -2$cards_european_handicap_home_min_2",  #235
        "$79_Draw -2$cards_european_handicap_draw_min_2",  #236
        "$79_Away -2$cards_european_handicap_away_min_2",  #237
        "$86_Yes$rcard_yes",  #238
        "$86_No$rcard_no",  #239
        "$5_Over 0.75$goals_overunder_over_075",  #240
        "$5_Under 0.75$goals_overunder_under_075",  #241
        "$5_Over 1.0$goals_overunder_over_10",  #242
        "$5_Under 1.0$goals_overunder_under_10",  #243
        "$5_Over 1.25$goals_overunder_over_125",  #244
        "$5_Under 1.25$goals_overunder_under_125",  #245
        "$5_Over 2.25$goals_overunder_over_225",  #246
        "$5_Under 2.25$goals_overunder_under_225",  #247
        "$5_Over 5.75$goals_overunder_over_575",  #248
        "$5_Under 5.75$goals_overunder_under_575",  #249
        "$5_Over 6.0$goals_overunder_over_60",  #250
        "$5_Under 6.0$goals_overunder_under_60",  #251
        "$5_Over 6.25$goals_overunder_over_625",  #252
        "$5_Under 6.25$goals_overunder_under_625",  #253
        "$5_Over 6.75$goals_overunder_over_675",  #254
        "$5_Under 6.75$goals_overunder_under_675",  #255
        "$5_Over 7.0$goals_overunder_over_70",  #256
        "$5_Under 7.0$goals_overunder_under_70",  #257
        "$5_Over 9.5$goals_overunder_over_95",  #258
        "$5_Under 9.5$goals_overunder_under_95",  #259
        "$4_Home -1.25$asian_handicap_home_min_125",  #260
        "$4_Away -1.25$asian_handicap_away_min_125",  #261
        "$4_Home -2.25$asian_handicap_home_min_225",  #262
        "$4_Away -2.25$asian_handicap_away_min_225",  #263
        "$4_Home -3.25$asian_handicap_home_min_325",  #264
        "$4_Away -3.25$asian_handicap_away_min_325",  #265
        "$4_Home -4.25$asian_handicap_home_min_425",  #266
        "$4_Away -4.25$asian_handicap_away_min_425",  #267
        "$4_Home -5.25$asian_handicap_home_min_525",  #268
        "$4_Away -5.25$asian_handicap_away_min_525",  #269
        "$4_Home -6.25$asian_handicap_home_min_625",  #270
        "$4_Away -6.25$asian_handicap_away_min_625",  #271
        "$4_Home -0.75$asian_handicap_home_min_075",  #272
        "$4_Away -0.75$asian_handicap_away_min_075",  #273
        "$4_Home -1.75$asian_handicap_home_min_175",  #274
        "$4_Away -1.75$asian_handicap_away_min_175",  #275
        "$4_Home -2.75$asian_handicap_home_min_275",  #276
        "$4_Away -2.75$asian_handicap_away_min_275",  #277
        "$4_Home -3.75$asian_handicap_home_min_375",  #278
        "$4_Away -3.75$asian_handicap_away_min_375",  #279
        "$4_Home -4.75$asian_handicap_home_min_475",  #280
        "$4_Away -4.75$asian_handicap_away_min_475",  #281
        "$4_Home -5.75$asian_handicap_home_min_575",  #282
        "$4_Away -5.75$asian_handicap_away_min_575",  #283
        "$4_Home -6.75$asian_handicap_home_min_675",  #284
        "$4_Away -6.75$asian_handicap_away_min_675",  #285
        "$4_Home -1.5$asian_handicap_home_min_15",  #286
        "$4_Away -1.5$asian_handicap_away_min_15",  #287
        "$4_Home -2.5$asian_handicap_home_min_25",  #288
        "$4_Away -2.5$asian_handicap_away_min_25",  #289
        "$4_Home -3.5$asian_handicap_home_min_35",  #290
        "$4_Away -3.5$asian_handicap_away_min_35",  #291
        "$4_Home -4.5$asian_handicap_home_min_45",  #292
        "$4_Away -4.5$asian_handicap_away_min_45",  #293
        "$4_Home -5.5$asian_handicap_home_min_55",  #294
        "$4_Away -5.5$asian_handicap_away_min_55",  #295
        "$4_Home -6.5$asian_handicap_home_min_65",  #296
        "$4_Away -6.5$asian_handicap_away_min_65",  #297
        "$4_Home -1$asian_handicap_home_min_1",  #298
        "$4_Away -1$asian_handicap_away_min_1",  #299
        "$4_Home -2$asian_handicap_home_min_2",  #300
        "$4_Away -2$asian_handicap_away_min_2",  #301
        "$4_Home -3$asian_handicap_home_min_3",  #302
        "$4_Away -3$asian_handicap_away_min_3",  #303
        "$4_Home -4$asian_handicap_home_min_4",  #304
        "$4_Away -4$asian_handicap_away_min_4",  #305
        "$4_Home -5$asian_handicap_home_min_5",  #306
        "$4_Away -5$asian_handicap_away_min_5",  #307
        "$4_Home -6$asian_handicap_home_min_6",  #308
        "$4_Away -6$asian_handicap_away_min_6",  #309
        "$4_Home -0.5$asian_handicap_home_min_05",  #310
        "$4_Away -0.5$asian_handicap_away_min_05",  #311
        "$4_Home +2$asian_handicap_home_plus_2",  #312
        "$4_Away +2$asian_handicap_away_plus_2",  #313
        "$4_Home +2.5$asian_handicap_home_plus_25",  #314
        "$4_Away +2.5$asian_handicap_away_plus_25",  #315
        "$4_Home +2.25$asian_handicap_home_plus_225",  #316
        "$4_Away +2.25$asian_handicap_away_plus_225",  #317
        "$4_Home +2.75$asian_handicap_home_plus_275",  #318
        "$4_Away +2.75$asian_handicap_away_plus_275",  #319
        "$4_Away +3.75$asian_handicap_away_plus_375",  #320
        "$4_Home +3.75$asian_handicap_home_plus_375",  #321
        "$4_Away +3.25$asian_handicap_away_plus_325",  #322
        "$4_Home +3.25$asian_handicap_home_plus_325",  #323
        "$4_Away +3.5$asian_handicap_away_plus_35",  #324
        "$4_Home +3.5$asian_handicap_home_plus_35",  #325
        "$4_Away +3$asian_handicap_away_plus_3",  #326
        "$4_Home +3$asian_handicap_home_plus_3",  #327
        "$4_Home +4$asian_handicap_home_plus_4",  #328

        "$4_Away +4$asian_handicap_away_plus_4",  #329
        "$4_Home +4.5$asian_handicap_home_plus_45",  #330
        "$4_Away +4.5$asian_handicap_away_plus_45",  #331
        "$4_Home +4.25$asian_handicap_home_plus_425",  #332
        "$4_Away +4.25$asian_handicap_away_plus_425",  #333
        "$4_Home +4.75$asian_handicap_home_plus_475",  #334
        "$4_Away +4.75$asian_handicap_away_plus_475",  #335
        "$4_Home +5$asian_handicap_home_plus_5",  #336
        "$4_Away +5$asian_handicap_away_plus_5",  #337
        "$4_Home +5.5$asian_handicap_home_plus_55",  #338
        "$4_Away +5.5$asian_handicap_away_plus_55",  #339
        "$4_Home +5.25$asian_handicap_home_plus_525",  #340
        "$4_Away +5.25$asian_handicap_away_plus_525",  #341
        "$4_Home +5.75$asian_handicap_home_plus_575",  #342
        "$4_Away +5.75$asian_handicap_away_plus_575",  #343
        "$4_Home +6$asian_handicap_home_plus_6",  #344
        "$4_Away +6$asian_handicap_away_plus_6",  #345
        "$4_Home +6.5$asian_handicap_home_plus_65",  #346
        "$4_Away +6.5$asian_handicap_away_plus_65",  #347
        "$4_Home +6.25$asian_handicap_home_plus_625",  #348
        "$4_Away +6.25$asian_handicap_away_plus_625",  #349
        "$4_Home +6.75$asian_handicap_home_plus_675",  #350
        "$4_Away +6.75$asian_handicap_away_plus_675",  #351
        "$6_Over 3.0$goals_overunder_first_half_over_30",  #352
        "$6_Over 3.25$goals_overunder_first_half_over_325",  #353
        "$6_Under 3.75$goals_overunder_first_half_under_375",  #354
        "$6_Over 3.75$goals_overunder_first_half_over_375",  #355
        "$6_Under 3.0$goals_overunder_first_half_under_30",  #356
        "$6_Under 3.25$goals_overunder_first_half_under_325",  #357
        "$26_Over 0.75$goals_overunder__second_half_over_075",  #358
        "$26_Over 1.0$goals_overunder__second_half_over_10",  #359
        "$26_Over 1.25$goals_overunder__second_half_over_125",  #360
        "$26_Over 1.75$goals_overunder__second_half_over_175",  #361
        "$26_Over 2.25$goals_overunder__second_half_over_225",  #362
        "$26_Over 2.75$goals_overunder__second_half_over_275",  #363
        "$26_Over 3.0$goals_overunder__second_half_over_30",  #364
        "$26_Over 3.25$goals_overunder__second_half_over_325",  #365
        "$26_Over 3.75$goals_overunder__second_half_over_375",  #366
        "$26_Under 0.75$goals_overunder__second_half_under_075",  #367
        "$26_Under 1.25$goals_overunder__second_half_under_125",  #368
        "$26_Under 1.75$goals_overunder__second_half_under_175",  #369
        "$26_Under 2.25$goals_overunder__second_half_under_225",  #370
        "$26_Under 2.75$goals_overunder__second_half_under_275",  #371
        "$26_Under 3.25$goals_overunder__second_half_under_325",  #372
        "$26_Under 3.75$goals_overunder__second_half_under_375",  #373
        "$26_Under 1.0$goals_overunder__second_half_under_10",  #374
        "$26_Under 2.0$goals_overunder__second_half_under_20",  #375
        "$26_Under 3.0$goals_overunder__second_half_under_30",  #376
        "$26_Over 2.0$goals_overunder__second_half_over_20",  #377
        "$19_Home -0.75$asian_handicap_first_half_home_min_075",  #378
        "$19_Away -0.75$asian_handicap_first_half_away_min_075",  #379
        "$19_Home -1$asian_handicap_first_half_home_min_1",  #380
        "$19_Away -1$asian_handicap_first_half_away_min_1",  #381
        "$19_Home -1.25$asian_handicap_first_half_home_min_125",  #382
        "$19_Away -1.25$asian_handicap_first_half_away_min_125",  #383
        "$19_Home -1.5$asian_handicap_first_half_home_min_15",  #384
        "$19_Away -1.5$asian_handicap_first_half_away_min_15",  #385
        "$19_Home -1.75$asian_handicap_first_half_home_min_175",  #386
        "$19_Away -1.75$asian_handicap_first_half_away_min_175",  #387
        "$45_Over 8.5$corners_over_under_over_850",  #388
        "$45_Under 8.5$corners_over_under_under_850",  #389
        "$45_Over 8$corners_over_under_over_800",  #390
        "$45_Under 8$corners_over_under_under_800",  #391
        "$45_Over 8.25$corners_over_under_over_825",  #392
        "$45_Under 8.25$corners_over_under_under_825",  #393
        "$45_Over 8.75$corners_over_under_over_875",  #394
        "$45_Under 8.75$corners_over_under_under_875",  #395
        "$45_Over 9$corners_over_under_over_900",  #396
        "$45_Under 9$corners_over_under_under_900",  #397
        "$45_Over 9.25$corners_over_under_over_925",  #398
        "$45_Under 9.25$corners_over_under_under_925",  #399
        "$45_Over 9.5$corners_over_under_over_950",  #400
        "$45_Under 9.5$corners_over_under_under_950",  #401
        "$45_Over 9.75$corners_over_under_over_975",  #402
        "$45_Under 9.75$corners_over_under_under_975",  #403
        "$45_Over 10$corners_over_under_over_1000",  #404
        "$45_Under 10$corners_over_under_under_1000",  #405
        "$45_Over 10.25$corners_over_under_over_1025",  #406
        "$45_Under 10.25$corners_over_under_under_1025",  #407
        "$45_Over 10.5$corners_over_under_over_1050",  #408
        "$45_Under 10.5$corners_over_under_under_1050",  #409
        "$45_Over 10.75$corners_over_under_over_1075",  #410
        "$45_Under 10.75$corners_over_under_under_1075",  #411
        "$45_Over 11$corners_over_under_over_1100",  #412
        "$45_Under 11$corners_over_under_under_1100",  #413
        "$45_Over 11.25$corners_over_under_over_1125",  #414
        "$45_Under 11.25$corners_over_under_under_1125",  #415
        "$45_Over 11.5$corners_over_under_over_1150",  #416
        "$45_Under 11.5$corners_over_under_under_1150",  #417
        "$45_Over 11.75$corners_over_under_over_1175",  #418
        "$45_Under 11.75$corners_over_under_under_1175",  #419
        "$45_Over 12$corners_over_under_over_1200",  #420
        "$45_Under 12$corners_over_under_under_1200",  #421
        "$45_Over 12.25$corners_over_under_over_1225",  #422
        "$45_Under 12.25$corners_over_under_under_1225",  #423
        "$45_Over 12.5$corners_over_under_over_1250",  #424
        "$45_Under 12.5$corners_over_under_under_1250",  #425
        "$45_Over 12.75$corners_over_under_over_1275",  #426
        "$45_Under 12.75$corners_over_under_under_1275",  #427
        "$14_Home$team_to_score_first_home",  #428
        "$14_Draw$team_to_score_first_draw",  #429
        "$14_Away$team_to_score_first_away",  #430
        "$15_Home$team_to_score_last_home",  #431
        "$15_Draw$team_to_score_last_draw",  #432
        "$15_Away$team_to_score_last_away",  #433
        "$16_Over 3.5$total_home_over_35",  #434
        "$16_Under 3.5$total_home_under_35",  #435
        "$16_Over 1.5$total_home_over_15",  #436
        "$16_Under 1.5$total_home_under_15",  #437
        "$16_Over 2.5$total_home_over_25",  #438
        "$16_Under 2.5$total_home_under_25",  #439
        "$17_Over 3.5$total_away_over_35",  #440
        "$17_Under 3.5$total_away_under_35",  #441
        "$17_Over 1.5$total_away_over_15",  #442
        "$17_Under 1.5$total_away_under_15",  #443
        "$17_Over 4.5$total_away_over_45",  #444
        "$17_Under 4.5$total_away_under_45",  #445
        "$17_Over 2.5$total_away_over_25",  #446
        "$17_Under 2.5$total_away_under_25",  #447
        "$17_Over 5.5$total_away_over_55",  #448
        "$17_Under 5.5$total_away_under_55",  #449
        "$17_Over 6.5$total_away_over_65",  #450
        "$17_Under 6.5$total_away_under_65",  #451
        "$91_Under 2 $total_goals_under_2",  #452
        "$91_2 Or 3 $total_goals_2_or_3",  #453
        "$91_Over 3 $total_goals_over_3",  #454
        "$97_Shot$first_goal_method_shot",  #455
        "$97_Header$first_goal_method_header",  #456
        "$97_Penalty$first_goal_method_penalty",  #457
        "$97_FreeKick$first_goal_method_freekick",  #458
        "$97_OwnGoal$first_goal_method_owngoal",  #459
        "$97_Draw$first_goal_method_draw",  #460
        "$56_Home +3.5$corners_asian_handicap_home_plus_35",  #461
        "$56_Away +3.5$corners_asian_handicap_away_plus_35",  #462
        "$57_Over 2.5$home_corners_overunder_over_25",  #463
        "$57_Under 2.5$home_corners_overunder_under_25",  #464
        "$58_Over 6.5$away_corners_overunder_over_65",  #465
        "$58_Under 6.5$away_corners_overunder_under_65",  #466
        "$75_Home$last_corner_home",  #467
        "$75_Away$last_corner_away",  #468
        "$76_Home$first_corner_home",  #469
        "$76_Away$first_corner_away",  #470
        "$80_Over 2.5$cards_overunder_over_25",  #471
        "$80_Under 2.5$cards_overunder_under_25",  #472
        "$81_Home -0.5$cards_asian_handicap_home_min_05",  #473
        "$81_Away -0.5$cards_asian_handicap_away_min_05",  #474
        "$82_Over 1.5$home_team_total_cards_over_15",  #475
        "$82_Under 1.5$home_team_total_cards_under_15",  #476
        "$83_Over 1.5$away_team_total_cards_over_15",  #477
        "$83_Under 1.5$away_team_total_cards_under_15",  #478
        "$99_Home$to_score_a_penalty_home",  #479
        "$99_Away$to_score_a_penalty_away",  #480
        "$100_Home$to_miss_a_penalty_home",  #481
        "$100_Away$to_miss_a_penalty_away",  #482
        "$16_Over 4.5$total_home_over_45",  #483
        "$16_Under 4.5$total_home_under_45",  #484
        "$16_Over 5.5$total_home_over_55",  #485
        "$16_Under 5.5$total_home_under_55",  #486
        "$16_Over 6.5$total_home_over_65",  #487
        "$16_Under 6.5$total_home_under_65",  #488
        "$56_Home -0.5$corners_asian_handicap_home_min_05",  #489

        "$56_Away -0.5$corners_asian_handicap_away_min_05",  #490
        "$56_Home -1.5$corners_asian_handicap_home_min_15",  #491
        "$56_Away -1.5$corners_asian_handicap_away_min_15",  #492
        "$56_Away +3$corners_asian_handicap_away_plus_3",  #493
        "$56_Home -3$corners_asian_handicap_home_min_3",  #494
        "$56_Home +0.5$corners_asian_handicap_home_plus_05",  #495
        "$56_Away +0.5$corners_asian_handicap_away_plus_05",  #496
        "$56_Home +0$corners_asian_handicap_home_plus_0",  #497
        "$56_Home +1$corners_asian_handicap_home_plus_1",  #498
        "$56_Away +1$corners_asian_handicap_away_plus_1",  #499
        "$56_Away -2$corners_asian_handicap_away_min_2",  #500
        "$56_Home +3$corners_asian_handicap_home_plus_3",  #501
        "$56_Home +2$corners_asian_handicap_home_plus_2",  #502
        "$56_Away +2$corners_asian_handicap_away_plus_2",  #503
        "$56_Away +0$corners_asian_handicap_away_plus_0",  #504
        "$56_Away -1$corners_asian_handicap_away_min_1",  #505
        "$56_Home -4$corners_asian_handicap_home_min_4",  #506
        "$56_Away -4$corners_asian_handicap_away_min_4",  #507
        "$56_Home -4.5$corners_asian_handicap_home_min_45",  #508
        "$56_Away -2.5$corners_asian_handicap_away_min_25",  #509
        "$56_Home +1.5$corners_asian_handicap_home_plus_15",  #510
        "$56_Away -3$corners_asian_handicap_away_min_3",  #511
        "$56_Home -2.5$corners_asian_handicap_home_min_25",  #512
        "$56_Home -2$corners_asian_handicap_home_min_2",  #513
        "$56_Home -1$corners_asian_handicap_home_min_1",  #514
        "$56_Away +1.5$corners_asian_handicap_away_plus_15",  #515
        "$56_Away -5.5$corners_asian_handicap_away_min_55",  #516
        "$56_Away -3.5$corners_asian_handicap_away_min_35",  #517
        "$56_Away +2.5$corners_asian_handicap_away_plus_25",  #518
        "$56_Home -6.5$corners_asian_handicap_home_min_65",  #519
        "$56_Home -5.5$corners_asian_handicap_home_min_55",  #520
        "$56_Home -3.5$corners_asian_handicap_home_min_35",  #521
        "$56_Home -5$corners_asian_handicap_home_min_5",  #522
        "$56_Away -5$corners_asian_handicap_away_min_5",  #523
        "$56_Away -4.5$corners_asian_handicap_away_min_45",  #524
        "$56_Away -6.5$corners_asian_handicap_away_min_65",  #525
        "$57_Over 5.5$home_corners_overunder_over_55",  #526
        "$57_Under 5.5$home_corners_overunder_under_55",  #527
        "$57_Over 4.5$home_corners_overunder_over_45",  #528
        "$57_Under 4.5$home_corners_overunder_under_45",  #529
        "$57_Over 6.5$home_corners_overunder_over_65",  #530
        "$57_Under 6.5$home_corners_overunder_under_65",  #531
        "$57_Over 7.5$home_corners_overunder_over_75",  #532
        "$57_Under 7.5$home_corners_overunder_under_75",  #533
        "$57_Over 3.5$home_corners_overunder_over_35",  #534
        "$57_Under 3.5$home_corners_overunder_under_35",  #535
        "$57_Over 8.5$home_corners_overunder_over_85",  #536
        "$57_Under 8.5$home_corners_overunder_under_85",  #537
        "$58_Over 5.5$away_corners_overunder_over_55",  #538
        "$58_Under 5.5$away_corners_overunder_under_55",  #539
        "$58_Over 3.5$away_corners_overunder_over_35",  #540
        "$58_Under 3.5$away_corners_overunder_under_35",  #541
        "$58_Over 4.5$away_corners_overunder_over_45",  #542
        "$58_Under 4.5$away_corners_overunder_under_45",  #543
        "$58_Over 2.5$away_corners_overunder_over_25",  #544
        "$58_Under 2.5$away_corners_overunder_under_25",  #545
        "$58_Over 7.5$away_corners_overunder_over_75",  #546
        "$58_Under 7.5$away_corners_overunder_under_75",  #547
        "$58_Over 8.5$away_corners_overunder_over_85",  #548
        "$58_Under 8.5$away_corners_overunder_under_85",  #549
        "$80_Over 3.5$cards_overunder_over_35",  #550
        "$80_Under 3.5$cards_overunder_under_35",  #551
        "$80_Over 4.5$cards_overunder_over_45",  #552
        "$80_Under 4.5$cards_overunder_under_45",  #553
        "$80_Over 5.5$cards_overunder_over_55",  #554
        "$80_Under 5.5$cards_overunder_under_55",  #555
        "$80_Over 6.5$cards_overunder_over_65",  #556
        "$80_Under 6.5$cards_overunder_under_65",  #557
        "$80_Over 7.5$cards_overunder_over_75",  #558
        "$80_Under 7.5$cards_overunder_under_75",  #559
        "$81_Home +0$cards_asian_handicap_home_plus_0",  #560
        "$81_Away +0$cards_asian_handicap_away_plus_0",  #561
        "$81_Home +0.5$cards_asian_handicap_home_plus_05",  #562
        "$81_Away +0.5$cards_asian_handicap_away_plus_05",  #563
        "$82_Over 2.5$home_team_total_cards_over_25",  #564
        "$82_Under 2.5$home_team_total_cards_under_25",  #565
        "$82_Over 3.5$home_team_total_cards_over_35",  #566
        "$82_Under 3.5$home_team_total_cards_under_35",  #567
        "$83_Over 2.5$away_team_total_cards_over_25",  #568
        "$83_Under 2.5$away_team_total_cards_under_25",  #569
        "$83_Over 3.5$away_team_total_cards_over_35",  #570
        "$83_Under 3.5$away_team_total_cards_under_35",  #571
        "$56_Home -6$corners_asian_handicap_home_min_6",  #572
        "$56_Away -6$corners_asian_handicap_away_min_6",  #573
        "$56_Home +2.5$corners_asian_handicap_home_plus_25",  #574
        "$56_Home +4$corners_asian_handicap_home_plus_4",  #575
        "$56_Away +4$corners_asian_handicap_away_plus_4",  #576
        "$56_Home +4.5$corners_asian_handicap_home_plus_45",  #577
        "$56_Away +4.5$corners_asian_handicap_away_plus_45",  #578
        "$56_Home +5$corners_asian_handicap_home_plus_5",  #579
        "$56_Away +5$corners_asian_handicap_away_plus_5",  #580
        "$56_Home +5.5$corners_asian_handicap_home_plus_55",  #581
        "$56_Away +5.5$corners_asian_handicap_away_plus_55",  #582
        "$56_Home +6$corners_asian_handicap_home_plus_6",  #583
        "$56_Away +6$corners_asian_handicap_away_plus_6",  #584
        "$56_Home +6.5$corners_asian_handicap_home_plus_65",  #585
        "$56_Away +6.5$corners_asian_handicap_away_plus_65",  #586
        "$45_Over 7$corners_over_under_over_700",  #587
        "$45_Under 7$corners_over_under_under_700",  #588
        "$45_Over 7.25$corners_over_under_over_725",  #589
        "$45_Under 7.25$corners_over_under_under_725",  #590
        "$45_Over 7.5$corners_over_under_over_750",  #591
        "$45_Under 7.5$corners_over_under_under_750",  #592
        "$45_Over 7.75$corners_over_under_over_775",  #593
        "$45_Under 7.75$corners_over_under_under_775",  #594

    ]
    # ----------------------------------------------------------     
    for item in bils:
        if target_string in item:
            colmnx = item.split(target_string)[1]
            return PREP_ + colmnx + " = '" + bets_odd + "', "  
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
 