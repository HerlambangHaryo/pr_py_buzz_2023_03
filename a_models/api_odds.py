# Import
import mysql.connector 
from a_models.api_accounts import *    

import pytz
utc=pytz.UTC 

import requests
import json 

def ao_controll_match_update(DICT, PREP_, space):
    # ----------------------------------------------------------   
    # ao_controll_match_update(DICT, PREP_, space)
    # ao_controll_match_update(date, bookmaker, season, league, 1, space)
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ao_controll_match_update()", flush=True)
    # ----------------------------------------------------------    
    APIkey = aa_check_acccount('APIkey', space)    
    counterAPI = aa_check_acccount('counterAPI', space) 
    # ----------------------------------------------------------
    if(counterAPI <= 0):
        its_api_empty()
    elif(counterAPI > 0):
        aa_update_counter(space) 
        # ao_response_odds(APIkey, date, bookmaker, season, league, page, space)
        ao_response_odds(APIkey, DICT, PREP_, space)
    # ----------------------------------------------------------

def ao_response_odds(APIkey, DICT, PREP_, space): 
    # ao_response_odds(APIkey, date, bookmaker, season, league, page, space)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "ao_response_odds()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------
    from datetime import datetime
    local = pytz.timezone("Asia/Jakarta")
    url = "https://api-football-v1.p.rapidapi.com/v3/odds" 
    # ----------------------------------------------------------
    """
        Updated at: 2023-02-02
            looping yang datanya ada 10 baris
            ditambahkan page
    """
    # ----------------------------------------------------------
    if(PREP_ == "pre_"):
        # ------------------------------------------------------
        DICTdate_0 = DICT['date_0']
        DICTpage = DICT['page']
        DICTcounter_loop = DICT['counter_loop']
        DICTdate_diff = DICT['date_diff']
        DICTdate_raw = DICT['date_raw']
        # ------------------------------------------------------ 
        querystring = {"date":DICTdate_0, "page":DICTpage}
        # ------------------------------------------------------
        print(space + "date_0 : " + str(DICTdate_0), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)
        print(space + "counter_loop : " + str(DICTcounter_loop), flush=True)
        print(space + "date_diff : " + str(DICTdate_diff), flush=True)
        print(space + "date_raw : " + str(DICTdate_raw), flush=True)
        # ------------------------------------------------------ 
        XPREP_ = "pre_"
    # ----------------------------------------------------------
    elif(PREP_ == "end_"):
        # ------------------------------------------------------ 
        DICTdate = DICT['date']
        DICTbookmaker = DICT['bookmaker']
        DICTseason = DICT['season']
        DICTleague = DICT['league']
        DICTpage = DICT['page']

        print(space + "date : " + str(DICTdate), flush=True)
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True)
        print(space + "season : " + str(DICTseason), flush=True)
        print(space + "league : " + str(DICTleague), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)

        querystring = {"date":DICTdate, "bookmaker":DICTbookmaker, "season":DICTseason, "league":DICTleague, "page":DICTpage}
        # ------------------------------------------------------ 
        XPREP_ = "end_"
    # ----------------------------------------------------------
    elif(PREP_ == "preleague_"):
        # ------------------------------------------------------ 
        DICTdate = DICT['date']
        DICTdate_raw = DICT['date_raw']
        DICTbookmaker = DICT['bookmaker']
        DICTseason = DICT['season']
        DICTleague = DICT['league']
        DICTpage = DICT['page']

        print(space + "date : " + str(DICTdate), flush=True)
        print(space + "date_raw : " + str(DICTdate_raw), flush=True)
        print(space + "bookmaker : " + str(DICTbookmaker), flush=True)
        print(space + "season : " + str(DICTseason), flush=True)
        print(space + "league : " + str(DICTleague), flush=True)
        print(space + "page : " + str(DICTpage), flush=True)

        querystring = {"date":DICTdate, "bookmaker":DICTbookmaker, "season":DICTseason, "league":DICTleague, "page":DICTpage}

        PREP_ = "pre_"
        XPREP_ = "preleague_"
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
    print(space + "__________________________________________________________________________")
    # ----------------------------------------------------------  
    total_response = len(d['response'])
    print(space + "Total API Response(s) : " + str(total_response), flush=True) 
    # ---------------------------------------------------------- 
    counter_response = 0
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    if(total_response > 0):
        for i in d['response']: 
            # ------------------------------------------------------
            print("")
            # ------------------------------------------------------
            counter_response += 1
            # ------------------------------------------------------
            leagueapi_id      = str(i['league']['id'])
            leagueapi_name    = str(i['league']['name'])
            leagueapi_country = str(i['league']['country'])
            leagueapi_logo    = str(i['league']['logo'])
            leagueapi_flag    = str(i['league']['flag'])
            leagueapi_season  = str(i['league']['season']) 
            fixtureapi_id     = str(i['fixture']['id'])
            # ------------------------------------------------------
            fixture_date_now     = datetime.fromisoformat(i['fixture']['date'])
            fixture_date         = str(fixture_date_now)
            fixture_date_local   = fixture_date_now.replace(tzinfo=pytz.UTC).astimezone(local) 
            # ------------------------------------------------------
            bookmakers_Array     = i['bookmakers'] 
            # ------------------------------------------------------
            word = space + str(counter_response) + ". "
            word += leagueapi_country + ",  "
            word += leagueapi_name + " "
            word += " #" + leagueapi_id + " - " + leagueapi_season + " / " +fixtureapi_id 
            print(word, flush=True)
            # ------------------------------------------------------  
            if(PREP_ == "end_"):
                good_to_go = 1
            elif(PREP_ == "pre_"): 
                # -------------------------------------------------- 
                # CHECKING DATE
                # -------------------------------------------------- 
                word = space + "fixt date " + str(fixture_date)  
                print(word, flush=True)
                # ------------------------------------------------------ 
                fix_local = fixture_date_local.strftime("%Y-%m-%d %H:%M:%S")
                word = space + "fix local " +  str(fix_local) 
                print(word, flush=True)
                # ------------------------------------------------------   
                tets = local.localize(DICTdate_raw).strftime("%Y-%m-%d %H:%M:%S")
                word = space + "local dat " + str(tets) 
                print(word, flush=True)
                # ------------------------------------------------------ 
                date_status = ''
                # ------------------------------------------------------ 
                if(fix_local >= tets):
                    date_status = 'Lebih'
                    print(space + date_status) 
                    # -------------------------------------------------- 
                    # bookmakersapi_rLeagues_id
                    # --------------------------------------------------  
                    bookmakersapi_rLeagues_id = 0
                    # -------------------------------------------------- 
                    query_a = " Select *  "
                    query_a += " from leagues "  
                    query_a += " where leagueapi_id = '" + leagueapi_id + "'"  
                    # -------------------------------------------------- 
                    mycursor = mydb.cursor()
                    mycursor.execute(query_a)
                    result_leagues = mycursor.fetchall()
                    # -------------------------------------------------- 
                    for rLeagues in result_leagues:  
                        # ----------------------------------------------  
                        league_rLeagues_id          = str(rLeagues[3])
                        league_rLeagues_name            = str(rLeagues[4])
                        bookmakersapi_rLeagues_id       = rLeagues[6] 
                        bookmakers_rLeagues_name        = str(rLeagues[7])
                        # ----------------------------------------------  
                    # --------------------------------------------------   
 
                    if(bookmakersapi_rLeagues_id == 8 ):
                        print(space + "__league_rLeagues_id : " + str(league_rLeagues_id), flush=True)   
                        print(space + "__league_rLeagues_name : " + str(league_rLeagues_name), flush=True)   
                        print(space + "__bookmakersapi_rLeagues_id : " + str(bookmakersapi_rLeagues_id), flush=True)   
                        print(space + "__bookmakers_rLeagues_name : " + str(bookmakers_rLeagues_name), flush=True) 
                        good_to_go_bm = 1

                    elif(bookmakersapi_rLeagues_id == 11 ):
                        print(space + "__league_rLeagues_id : " + str(league_rLeagues_id), flush=True)   
                        print(space + "__league_rLeagues_name : " + str(league_rLeagues_name), flush=True)   
                        print(space + "__bookmakersapi_rLeagues_id : " + str(bookmakersapi_rLeagues_id), flush=True)   
                        print(space + "__bookmakers_rLeagues_name : " + str(bookmakers_rLeagues_name), flush=True) 
                        good_to_go_bm = 1

                    else:
                        bm_status = 'gak ready BM'
                        print(space + bm_status) 
                        good_to_go = 0
                        # ------------------------------------------
                        # print(space + space2 + "Belum ada Bookmakers_ID")
                        # ------------------------------------------ 
                        for ba in bookmakers_Array:
                            # -------------------------------------- 
                            bookmakersapi_id        = str(ba['id'])
                            bookmakersapi_name      = str(ba['name']) 
                            bets_Array              = ba['bets'] 
                            bet_id_list_important   = [11, 8]
                            # --------------------------------------
                            if ba['id'] in bet_id_list_important:
                                # ----------------------------------
                                word_belum_ada_bookm = bookmakersapi_id + " "  
                                word_belum_ada_bookm += bookmakersapi_name + " = "
                                word_belum_ada_bookm += str(len(bets_Array))
                                # ---------------------------------- 
                                print(space + word_belum_ada_bookm)  
                        good_to_go_bm = 0

                    
                    if(good_to_go_bm == 1):
                        # -------------------------------------------------- 
                        # CHECKING Fixture API
                        # -------------------------------------------------- 
                        host="localhost"
                        user="root" 
                        database="pr_mmbuzz_2022_06"
                        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                        mycursor = mydb.cursor()
                        # -------------------------------------------------- 
                        query = " Select *  "
                        query += " from football_fixtures "  
                        query += " where fixtureapi_id = '" + str(fixtureapi_id) + "'"   
                        # ----------------------------------------------------------   
                        mycursor = mydb.cursor()
                        mycursor.execute(query)
                        result =  mycursor.fetchall()
                        # ----------------------------------------------------------    
                        print(space + "Total fixtureapi_id Row(s) : " + str(len(result))) 
                        # -------------------------------------------------- 
                        total_row = len(result)
                        # -------------------------------------------------- 
                        if(total_row == 0):   
                            # ---------------------------------------------- 
                            insert = " INSERT INTO `football_fixtures`( "
                            insert += " `leagueapi_id`, "
                            insert += " `league_name`, "
                            insert += " `league_country`, "
                            insert += " `league_logo`, "
                            insert += " `league_flag`, "
                            insert += " `season`, "
                            insert += "  `fixtureapi_id`, " 
                            insert += "  `fixture_status`, " 
                            insert += "  `date` " 
                            insert += " ) VALUES ( "
                            insert += "  '"+str(leagueapi_id)+"', " 
                            insert += "  '"+str(leagueapi_name)+"', " 
                            insert += "  '"+str(leagueapi_country)+"', " 
                            insert += "  '"+str(leagueapi_logo)+"', " 
                            insert += "  '"+str(leagueapi_flag)+"', " 
                            insert += "  '"+str(leagueapi_season)+"', " 
                            insert += "  '"+str(fixtureapi_id)+"', "  
                            insert += "  'Not Started Yet', " 
                            insert += "  '"+str(fixture_date_now)+"' ) " 
                            mycursor.execute(insert)
                            mydb.commit()      
                            print(space +  "row_inserted")
                            # ---------------------------------------------- 
                        good_to_go = 1
 
                elif(fix_local < tets):
                    date_status = 'Kurang'
                    print(space + date_status)
                    good_to_go = 0

            print(space + "good to Go " + str(good_to_go))
            if(good_to_go == 1):
                # ------------------------------------------------------ 
                # ------------------------------------------------------ 
                # ------------------------------------------------------ 
                # ------------------------------------------------------  
                SET_odds = "" 
                ags_val = ""
                ags_total = 0
                first_gs_val = ""
                last_gs_val = ""
                score_more_gs_val = ""
                last2_gs_val = ""
                exact_gs_val = ""
                # ------------------------------------------------------ 
                space += "__"
                # ------------------------------------------------------ 
                for ba in bookmakers_Array:
                    # -------------------------------------------------- 
                    bookmakersapi_id   = ba['id']
                    bookmakersapi_name = ba['name'] 
                    # -------------------------------------------------- 
                    # GOOD TO GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                    good_to_go_bet = 0
                    # -------------------------------------------------- 
                    if(PREP_ == "pre_"):
                        if(bookmakersapi_rLeagues_id == bookmakersapi_id): 
                            good_to_go_bet = 1 
                            word_bm = str(bookmakersapi_rLeagues_id) + "==" + str(bookmakersapi_id)
                            print(space + word_bm)
                        # else:
                        # word_bm = str(bookmakersapi_rLeagues_id) + "==" + str(bookmakersapi_id)
                        # print(space + word_bm)

                    if(PREP_ == "end_"):
                        good_to_go_bet = 1
                    # --------------------------------------------------
                    # CONTINUE
                    # --------------------------------------------------
                    # if(good_to_go_bet == 0):
                    # print(space + "good_to_go_bet" + str(good_to_go_bet))
                    if(good_to_go_bet == 1):
                        # ----------------------------------------------
                        bets_Array = ba['bets']
                        # ----------------------------------------------
                        for bta in bets_Array:
                            # ------------------------------------------
                            bets_name = bta['name']
                            bets_id   = bta['id'] 
                            # ------------------------------------------
                            word_002 = str(bets_id) + " " + str(bets_name)
                            print(space + "____" + word_002)
                            # ------------------------------------------
                            betsvalues_array = bta['values']
                            # ------------------------------------------
                            ags = "" 
                            # ------------------------------------------
                            for bva in betsvalues_array: 
                                # --------------------------------------
                                bets_value = bva['value']
                                bets_odd   = bva['odd']
                                # --------------------------------------
                                bet_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 19, 20, 
                                            21, 24, 25, 26, 27, 28, 32, 34, 35, 36, 38, 
                                            39, 40, 41, 42, 46, 48, 49, 52, 55, 73, 74, 79, 86]
                                # --------------------------------------
                                if bets_id in bet_id_list: 
                                    # ----------------------------------
                                    word_bets = "res id = " + str(bookmakersapi_name) + "/"  
                                    # ----------------------------------
                                    query_b = " Select *  "
                                    query_b += " from bets "  
                                    query_b += " where bet_id = '"+str(bets_id)+"' "  
                                    query_b += " and value like '"+str(bets_value)+"' "
                                    query_b += " and columny is not null "
                                    # print(query_b)
                                    mycursor.execute(query_b)
                                    result_bets = mycursor.fetchall()
                                    # ----------------------------------
                                    for rbs in result_bets:
                                        # ----------------------------------
                                        colmnx       = rbs[5] 
                                        colmnx       = rbs[5] 
                                        # ----------------------------------
                                        word_rbs1 = "res : " + str(bets_value)
                                        word_rbs2 = "qry : " + colmnx
                                        # ----------------------------------
                                        pre_set = PREP_ + colmnx + " = '" + bets_odd + "', " 
                                        SET_odds += pre_set 
                                        word_003 = pre_set 
                                        print(space + "______" + word_003)
                                    # ----------------------------------
                                # --------------------------------------
                                elif(bets_id == 92):
                                    if(float(bets_odd) < 2.00): 
                                    #     print(space + "ags => " + bets_value + ":" + str(bets_odd) + ";", flush=True)
                                        ags_total += 1
                                    pre_ags_val = bets_value + ":" + str(bets_odd) + ";" 
                                    ags_val += pre_ags_val
                                # --------------------------------------
                                elif(bets_id == 93):
                                    # if(float(bets_odd) <= 4.00):
                                    #     print(space + "fir => " +  bets_value + ":" + str(bets_odd) + ";", flush=True)
                                    pre_first_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    first_gs_val += pre_first_gs_val
                                # --------------------------------------
                                elif(bets_id == 94):
                                    # if(float(bets_odd) <= 2.20):
                                    #     print(space + "las => " +  bets_value + ":" + str(bets_odd) + ";", flush=True )
                                    pre_last_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    last_gs_val += pre_last_gs_val
                                # --------------------------------------
                                elif(bets_id == 95):
                                    # if(float(bets_odd) <= 2.50):
                                    #     print(space + "2mr =>" +  bets_value + ":" + str(bets_odd) + ";", flush=True )
                                    pre_score_more_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    score_more_gs_val += pre_score_more_gs_val
                                # --------------------------------------
                                elif(bets_id == 96):
                                    # if(float(bets_odd) <= 2.20):
                                    #     print(space + "ls2 => " +  bets_value + ":" + str(bets_odd) + ";", flush=True )
                                    pre_last2_gs_val = bets_value + ":" + str(bets_odd) + ";"  
                                    last2_gs_val += pre_last2_gs_val
                                # --------------------------------------
                                elif(bets_id == 10):
                                    # if(float(bets_odd) <= 8.00):
                                    #     print(space + "csx => " + bets_value + "-" + str(bets_odd) + ";", flush=True )
                                    pre_exact_gs_val = bets_value + "-" + str(bets_odd) + ";"  
                                    exact_gs_val += pre_exact_gs_val 
                                else:  
                                    word_else = space + "bet_id: " + str(bets_id)
                                    word_else += " --- bets_value: " + str(bets_value)
                                    word_else += " --- bets_odd: " + str(bets_odd)
                                    print(space +  word_else, flush=True)
                # ------------------------------------------------------ 
                # ------------------------------------------------------
                # print(space + word_else)
                # ------------------------------------------------------
        
                # ------------------------------------------------------
                host="localhost"
                user="root" 
                database="pr_mmbuzz_2022_06"
                mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
                mycursor = mydb.cursor()
                # -------------------------------------------------- 
                update_odds = " UPDATE `football_fixtures` SET "  
                # -------------------------------------------------- 
                date_update = " date = '"+fixture_date+"', "
                date_update += " updated_at = now(), " 
                # -------------------------------------------------- 
                ags_update = " "+PREP_+"anytime_goal_scorer = '"+ags_val.replace("'", "\\'")+"', "
                ags_update += " "+PREP_+"ags_total = '"+str(ags_total)+"', "
                ags_update += " "+PREP_+"first_goal_scorer = '"+first_gs_val.replace("'", "\\'")+"', "
                ags_update += " "+PREP_+"last_goal_scorer = '"+last_gs_val.replace("'", "\\'")+"', "
                ags_update += " "+PREP_+"to_score_two_or_more_goals = '"+score_more_gs_val.replace("'", "\\'")+"', "
                ags_update += " "+PREP_+"last_goal_scorer2 = '"+last2_gs_val.replace("'", "\\'")+"', "
                ags_update += " "+PREP_+"exact_score = '"+exact_gs_val.replace("'", "\\'")+"' "
                # -------------------------------------------------- 
                # print(space + "anytime_goal_scorer:" + str(ags_val), flush=True )
                # print(space + "ags_total:" + str(ags_total), flush=True )
                # print(space + "first_goal_scorer:" + str(first_gs_val), flush=True )
                # print(space + "last_goal_scorer:" + str(last_gs_val), flush=True )
                # print(space + "to_score_two_or_more_goals:" + str(score_more_gs_val), flush=True )
                # print(space + "last_goal_scorer2:" + str(last2_gs_val), flush=True )
                # print(space + "exact_score:" + str(exact_gs_val), flush=True )
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                # -------------------------------------------------- 
                if(PREP_ == "pre_"): 
                    fixture_status_update = " , pre_odd_updated_at = current_timestamp " 
                if(PREP_ == "end_"):
                    fixture_status_update = " , end_odd_updated_at = current_timestamp , fixture_status = 'Match Finished Ended' " 
                # -------------------------------------------------- 
                print(space + "fixture_status_update:" + str(fixture_status_update), flush=True ) 
                # -------------------------------------------------- 
                WHERE_odds = " WHERE fixtureapi_id = '"+fixtureapi_id+"' " 
                # -------------------------------------------------- 
                final_SET_odds = SET_odds +  date_update + ags_update + fixture_status_update 
                query_update = update_odds + final_SET_odds + WHERE_odds  
                info_query = update_odds + date_update + fixture_status_update  
                word_001 = space + info_query 
                # -------------------------------------------------- 
                # print(space + query_update)
                # -------------------------------------------------- 
                mycursor.execute(query_update)
                mydb.commit()      

        if(total_response == 10):
            # ----------------------------------------------------------   
            print(space + "__re_looping__", flush=True)
            # ----------------------------------------------------------   
            DICTpage += 1
            # ----------------------------------------------------------    

            if(XPREP_ == "pre_"): 
                DICT = {
                    'date_0' : DICTdate_0,
                    'page' : DICTpage,
                    'counter_loop' : DICTcounter_loop,
                    'date_diff' : DICTdate_diff,
                    'date_raw' : DICTdate_raw,
                }
                
            elif(XPREP_ == "end_"):
                # ------------------------------------------------------ 
                DICT = {
                    "date" : DICTdate,
                    "bookmaker" : DICTbookmaker,
                    "season" : DICTseason,
                    "league" : DICTleague,
                    "page" : DICTpage,
                }
            # --------------------------------------------------  
            
            elif(XPREP_ == "preleague_"):
                DICT = {
                    "date" : DICTdate,
                    "date_raw" : DICTdate_raw,
                    "bookmaker" : DICTbookmaker,
                    "season" : DICTseason,
                    "league" : DICTleague,
                    'page' : DICTpage,
                }
            print(space + "==========================================================================") 
            ao_controll_match_update(DICT, XPREP_, '  ________')
            # ----------------------------------------------------------   
        elif(total_response < 10): 
            # ----------------------------------------------------------   
            print(space + "__ff_update_unfinished__", flush=True)
            # ---------------------------------------------------------- 
            space += "  "
            # # ----------------------------------------------------------    
            print(space + "> No longer get supported", flush=True)
            # host="localhost"
            # user="root" 
            # database="pr_mmbuzz_2022_06"
            # mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
            # mycursor = mydb.cursor()
            # # ----------------------------------------------------------   
            # unfinished = " UPDATE `football_fixtures` SET "   
            # unfinished += " fixture_status = 'Match Finished Ended' " 
            # unfinished += " WHERE DATE(date) = '"+str(date)+"' " 
            # unfinished += " AND leagueapi_id = '"+str(leagueapi_id)+"' " 
            # unfinished += " AND season = '"+str(season)+"' " 
            # # ----------------------------------------------------------
            # mycursor.execute(unfinished)
            # mydb.commit()      
            # # ----------------------------------------------------------
            # print(space + str(leagueapi_id) + " " + str(date) + " Match Finished Ended")
            # # ----------------------------------------------------------     
            # print("")  
    
    
    
    
    