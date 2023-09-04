# Import
import mysql.connector 
# from a_models.patternlist import *  

def xp4Na_get_league_fixture_to_reset(leagueapi_id, prep_col, min_standart, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "xp4Na_get_league_fixture_to_reset()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = "( Select  "
    query += " teams_homeapi_id , " 
    query += " teams_awayapi_id, " 

    query += " leagueapi_id, " 
    query += " season, "   
    query += " fixtureapi_id "  
    
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    if(prep_col == 'pre_'):
        query += " and pre_response != 3 " 
    if(prep_col == 'end_'):
        query += " and end_response != 3 " 
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') " 
    query += ") union (Select  "
    query += " teams_homeapi_id , " 
    query += " teams_awayapi_id, " 

    query += " leagueapi_id, " 
    query += " season, "   
    query += " fixtureapi_id "  
    
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    if(prep_col == 'pre_'):
        query += " and pre_response is null " 
    if(prep_col == 'end_'):
        query += " and end_response is null " 
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') )" 
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
    counter = 0 
    # ----------------------------------------------------------  
    space += "__" 
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        teams_home_id   = x[0] 
        teams_away_id   = x[1] 

        leagueapi_id    = str(x[2])  
        season          = str(x[3])   
        fixtureapi_id   = str(x[4])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += "#" + fixtureapi_id 
        word += " #" + leagueapi_id 
        word += " - " + season 
        print(word, flush=True)      
        # ------------------------------------------------------
        xp4Na_set_pattern(fixtureapi_id, prep_col, min_standart, space)
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

def xp4Na_set_pattern(fixtureapi_id, prep_col, min_standart, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "xp4Na_set_pattern()") 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    ah_total_min_675 = '' 
    ah_total_min_65 = '' 
    ah_total_min_625 = '' 
    ah_total_min_6 = '' 
    # ----------------------------------------------------------  
    ah_total_min_575 = '' 
    ah_total_min_55 = '' 
    ah_total_min_525 = '' 
    ah_total_min_5 = '' 
    # ----------------------------------------------------------  
    ah_total_min_475 = '' 
    ah_total_min_45 = '' 
    ah_total_min_425 = '' 
    ah_total_min_4 = '' 
    # ----------------------------------------------------------  
    ah_total_min_375 = '' 
    ah_total_min_35 = '' 
    ah_total_min_325 = '' 
    ah_total_min_3 = '' 
    # ----------------------------------------------------------  
    ah_total_min_275 = '' 
    ah_total_min_25 = '' 
    ah_total_min_225 = '' 
    ah_total_min_2 = '' 
    # ----------------------------------------------------------  
    ah_total_min_175 = '' 
    ah_total_min_15 = '' 
    ah_total_min_125 = '' 
    ah_total_min_1 = '' 
    # ----------------------------------------------------------  
    ah_total_min_075 = '' 
    ah_total_min_05 = '' 
    ah_total_min_025 = '' 
    ah_total_plus_0 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_025 = '' 
    ah_total_plus_05 = '' 
    ah_total_plus_075 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_1 = '' 
    ah_total_plus_125 = '' 
    ah_total_plus_15 = '' 
    ah_total_plus_175 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_2 = '' 
    ah_total_plus_225 = '' 
    ah_total_plus_25 = '' 
    ah_total_plus_275 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_3 = '' 
    ah_total_plus_325 = '' 
    ah_total_plus_35 = '' 
    ah_total_plus_375 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_4 = '' 
    ah_total_plus_425 = '' 
    ah_total_plus_45 = '' 
    ah_total_plus_475 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_5 = '' 
    ah_total_plus_525 = '' 
    ah_total_plus_55 = '' 
    ah_total_plus_575 = '' 
    # ----------------------------------------------------------  
    ah_total_plus_6 = '' 
    ah_total_plus_625 = '' 
    ah_total_plus_65 = '' 
    ah_total_plus_675 = '' 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    ah_total_min_675_mirror = '' 
    ah_total_min_65_mirror = '' 
    ah_total_min_625_mirror = '' 
    ah_total_min_6_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_575_mirror = '' 
    ah_total_min_55_mirror = '' 
    ah_total_min_525_mirror = '' 
    ah_total_min_5_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_475_mirror = '' 
    ah_total_min_45_mirror = '' 
    ah_total_min_425_mirror = '' 
    ah_total_min_4_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_375_mirror = '' 
    ah_total_min_35_mirror = '' 
    ah_total_min_325_mirror = '' 
    ah_total_min_3_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_275_mirror = '' 
    ah_total_min_25_mirror = '' 
    ah_total_min_225_mirror = '' 
    ah_total_min_2_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_175_mirror = '' 
    ah_total_min_15_mirror = '' 
    ah_total_min_125_mirror = '' 
    ah_total_min_1_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_min_075_mirror = '' 
    ah_total_min_05_mirror = '' 
    ah_total_min_025_mirror = '' 
    ah_total_plus_0_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_025_mirror = '' 
    ah_total_plus_05_mirror = '' 
    ah_total_plus_075_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_1_mirror = '' 
    ah_total_plus_125_mirror = '' 
    ah_total_plus_15_mirror = '' 
    ah_total_plus_175_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_2_mirror = '' 
    ah_total_plus_225_mirror = '' 
    ah_total_plus_25_mirror = '' 
    ah_total_plus_275_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_3_mirror = '' 
    ah_total_plus_325_mirror = '' 
    ah_total_plus_35_mirror = '' 
    ah_total_plus_375_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_4_mirror = '' 
    ah_total_plus_425_mirror = '' 
    ah_total_plus_45_mirror = '' 
    ah_total_plus_475_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_5_mirror = '' 
    ah_total_plus_525_mirror = '' 
    ah_total_plus_55_mirror = '' 
    ah_total_plus_575_mirror = '' 
    # ----------------------------------------------------------  
    ah_total_plus_6_mirror = '' 
    ah_total_plus_625_mirror = '' 
    ah_total_plus_65_mirror = '' 
    ah_total_plus_675_mirror = ''  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    gou_total_05 = '' 
    gou_total_075 = '' 
    # ----------------------------------------------------------  
    gou_total_10 = '' 
    gou_total_125 = '' 
    gou_total_15 = '' 
    gou_total_175 = '' 
    # ----------------------------------------------------------  
    gou_total_20 = '' 
    gou_total_225 = '' 
    gou_total_25 = '' 
    gou_total_275 = '' 
    # ----------------------------------------------------------  
    gou_total_30 = '' 
    gou_total_325 = '' 
    gou_total_35 = '' 
    gou_total_375 = '' 
    # ----------------------------------------------------------  
    gou_total_40 = '' 
    gou_total_425 = '' 
    gou_total_45 = '' 
    gou_total_475 = '' 
    # ----------------------------------------------------------  
    gou_total_50 = '' 
    gou_total_525 = '' 
    gou_total_55 = '' 
    gou_total_575 = '' 
    # ----------------------------------------------------------  
    gou_total_60 = '' 
    gou_total_625 = '' 
    gou_total_65 = '' 
    gou_total_675 = '' 
    # ----------------------------------------------------------  
    gou_total_70 = '' 
    gou_total_75 = '' 
    gou_total_85 = '' 
    gou_total_95 = '' 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------   
    query_1 = " Select fixtureapi_id, date  " 
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_675"
    query_1 += ", " + prep_col + "asian_handicap_away_min_675"
    query_1 += ", " + prep_col + "asian_handicap_home_min_65"
    query_1 += ", " + prep_col + "asian_handicap_away_min_65"
    query_1 += ", " + prep_col + "asian_handicap_home_min_625"
    query_1 += ", " + prep_col + "asian_handicap_away_min_625"
    query_1 += ", " + prep_col + "asian_handicap_home_min_6"
    query_1 += ", " + prep_col + "asian_handicap_away_min_6"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_575"
    query_1 += ", " + prep_col + "asian_handicap_away_min_575"
    query_1 += ", " + prep_col + "asian_handicap_home_min_55"
    query_1 += ", " + prep_col + "asian_handicap_away_min_55"
    query_1 += ", " + prep_col + "asian_handicap_home_min_525"
    query_1 += ", " + prep_col + "asian_handicap_away_min_525"
    query_1 += ", " + prep_col + "asian_handicap_home_min_5"
    query_1 += ", " + prep_col + "asian_handicap_away_min_5"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_475"
    query_1 += ", " + prep_col + "asian_handicap_away_min_475"
    query_1 += ", " + prep_col + "asian_handicap_home_min_45"
    query_1 += ", " + prep_col + "asian_handicap_away_min_45"
    query_1 += ", " + prep_col + "asian_handicap_home_min_425"
    query_1 += ", " + prep_col + "asian_handicap_away_min_425"
    query_1 += ", " + prep_col + "asian_handicap_home_min_4"
    query_1 += ", " + prep_col + "asian_handicap_away_min_4"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_375"
    query_1 += ", " + prep_col + "asian_handicap_away_min_375"
    query_1 += ", " + prep_col + "asian_handicap_home_min_35"
    query_1 += ", " + prep_col + "asian_handicap_away_min_35"
    query_1 += ", " + prep_col + "asian_handicap_home_min_325"
    query_1 += ", " + prep_col + "asian_handicap_away_min_325"
    query_1 += ", " + prep_col + "asian_handicap_home_min_3"
    query_1 += ", " + prep_col + "asian_handicap_away_min_3"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_275"
    query_1 += ", " + prep_col + "asian_handicap_away_min_275"
    query_1 += ", " + prep_col + "asian_handicap_home_min_25"
    query_1 += ", " + prep_col + "asian_handicap_away_min_25"
    query_1 += ", " + prep_col + "asian_handicap_home_min_225"
    query_1 += ", " + prep_col + "asian_handicap_away_min_225"
    query_1 += ", " + prep_col + "asian_handicap_home_min_2"
    query_1 += ", " + prep_col + "asian_handicap_away_min_2"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_175"
    query_1 += ", " + prep_col + "asian_handicap_away_min_175"
    query_1 += ", " + prep_col + "asian_handicap_home_min_15"
    query_1 += ", " + prep_col + "asian_handicap_away_min_15"
    query_1 += ", " + prep_col + "asian_handicap_home_min_125"
    query_1 += ", " + prep_col + "asian_handicap_away_min_125"
    query_1 += ", " + prep_col + "asian_handicap_home_min_1"
    query_1 += ", " + prep_col + "asian_handicap_away_min_1"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_min_075"
    query_1 += ", " + prep_col + "asian_handicap_away_min_075"
    query_1 += ", " + prep_col + "asian_handicap_home_min_05"
    query_1 += ", " + prep_col + "asian_handicap_away_min_05"
    query_1 += ", " + prep_col + "asian_handicap_home_min_025"
    query_1 += ", " + prep_col + "asian_handicap_away_min_025"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_0"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_0"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_025"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_025"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_05"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_05"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_075"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_075"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_1"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_1"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_125"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_125"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_15"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_15"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_175"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_175"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_2"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_2"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_225"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_225"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_25"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_25"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_275"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_275"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_3"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_3"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_325"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_325"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_35"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_35"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_375"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_375"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_4"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_4"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_425"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_425"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_45"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_45"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_475"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_475"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_5"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_5"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_525"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_525"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_55"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_55"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_575"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_575"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "asian_handicap_home_plus_6"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_6"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_625"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_625"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_65"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_65"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_675"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_675"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_05"
    query_1 += ", " + prep_col + "goals_overunder_under_05"
    query_1 += ", " + prep_col + "goals_overunder_over_075"
    query_1 += ", " + prep_col + "goals_overunder_under_075"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_10"
    query_1 += ", " + prep_col + "goals_overunder_under_10"
    query_1 += ", " + prep_col + "goals_overunder_over_125"
    query_1 += ", " + prep_col + "goals_overunder_under_125"
    query_1 += ", " + prep_col + "goals_overunder_over_15"
    query_1 += ", " + prep_col + "goals_overunder_under_15"
    query_1 += ", " + prep_col + "goals_overunder_over_175"
    query_1 += ", " + prep_col + "goals_overunder_under_175"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_20"
    query_1 += ", " + prep_col + "goals_overunder_under_20"
    query_1 += ", " + prep_col + "goals_overunder_over_225"
    query_1 += ", " + prep_col + "goals_overunder_under_225"
    query_1 += ", " + prep_col + "goals_overunder_over_25"
    query_1 += ", " + prep_col + "goals_overunder_under_25"
    query_1 += ", " + prep_col + "goals_overunder_over_275"
    query_1 += ", " + prep_col + "goals_overunder_under_275"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_30"
    query_1 += ", " + prep_col + "goals_overunder_under_30"
    query_1 += ", " + prep_col + "goals_overunder_over_325"
    query_1 += ", " + prep_col + "goals_overunder_under_325"
    query_1 += ", " + prep_col + "goals_overunder_over_35"
    query_1 += ", " + prep_col + "goals_overunder_under_35"
    query_1 += ", " + prep_col + "goals_overunder_over_375"
    query_1 += ", " + prep_col + "goals_overunder_under_375"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_40"
    query_1 += ", " + prep_col + "goals_overunder_under_40"
    query_1 += ", " + prep_col + "goals_overunder_over_425"
    query_1 += ", " + prep_col + "goals_overunder_under_425"
    query_1 += ", " + prep_col + "goals_overunder_over_45"
    query_1 += ", " + prep_col + "goals_overunder_under_45"
    query_1 += ", " + prep_col + "goals_overunder_over_475"
    query_1 += ", " + prep_col + "goals_overunder_under_475"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_50"
    query_1 += ", " + prep_col + "goals_overunder_under_50"
    query_1 += ", " + prep_col + "goals_overunder_over_525"
    query_1 += ", " + prep_col + "goals_overunder_under_525"
    query_1 += ", " + prep_col + "goals_overunder_over_55"
    query_1 += ", " + prep_col + "goals_overunder_under_55"
    query_1 += ", " + prep_col + "goals_overunder_over_575"
    query_1 += ", " + prep_col + "goals_overunder_under_575"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_60"
    query_1 += ", " + prep_col + "goals_overunder_under_60"
    query_1 += ", " + prep_col + "goals_overunder_over_625"
    query_1 += ", " + prep_col + "goals_overunder_under_625"
    query_1 += ", " + prep_col + "goals_overunder_over_65"
    query_1 += ", " + prep_col + "goals_overunder_under_65"
    query_1 += ", " + prep_col + "goals_overunder_over_675"
    query_1 += ", " + prep_col + "goals_overunder_under_675"
    # ----------------------------------------------------------  
    query_1 += ", " + prep_col + "goals_overunder_over_70"
    query_1 += ", " + prep_col + "goals_overunder_under_70"
    query_1 += ", " + prep_col + "goals_overunder_over_75"
    query_1 += ", " + prep_col + "goals_overunder_under_75"
    query_1 += ", " + prep_col + "goals_overunder_over_85"
    query_1 += ", " + prep_col + "goals_overunder_under_85"
    query_1 += ", " + prep_col + "goals_overunder_over_95"
    query_1 += ", " + prep_col + "goals_overunder_under_95"
    # ----------------------------------------------------------  
    query_1 += ", leagueapi_id"
    query_1 += " from football_odds "  
    query_1 += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "    
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query_1)
    result = mycursor.fetchall()
    # ----------------------------------------------------------    
    # ----------------------------------------------------------    
    for rs1 in result: 
        # ------------------------------------------------------
        # ------------------------------------------------------
        counter_col = 0
        fixtureapi_id       = rs1[counter_col]

        counter_col += 1
        rs1_date                = rs1[counter_col] 

        # ------------------------------------------------------
        # ------------------------------------------------------
        counter_col += 1
        asian_handicap_home_min_675 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_675 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_65 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_65 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_625 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_625 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_6 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_6 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_575 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_575 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_55 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_55 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_525 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_525 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_5 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_5 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_475 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_475 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_45 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_45 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_425 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_425 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_4 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_4 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_375 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_375 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_35 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_35 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_325 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_325 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_3 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_3 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_275 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_275 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_25 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_25 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_225 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_225 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_2 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_2 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_175 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_175 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_15 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_15 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_125 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_125 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_1 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_1 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_075 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_075 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_05 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_05 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_min_025 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_min_025 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_0 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_0 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_025 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_025 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_05 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_05 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_075 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_075 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_1 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_1 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_125 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_125 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_15 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_15 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_175 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_175 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_2 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_2 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_225 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_225 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_25 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_25 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_275 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_275 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_3 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_3 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_325 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_325 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_35 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_35 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_375 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_375 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_4 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_4 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_425 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_425 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_45 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_45 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_475 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_475 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_5 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_5 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_525 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_525 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_55 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_55 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_575 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_575 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_6 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_6 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_625 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_625 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_65 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_65 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_home_plus_675 = rs1[counter_col] 

        counter_col += 1
        asian_handicap_away_plus_675 = rs1[counter_col] 
        # ------------------------------------------------------
        # ------------------------------------------------------
        counter_col += 1
        goals_overunder_over_05 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_05 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_075 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_075 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_10 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_10 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_125 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_125 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_15 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_15 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_175 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_175 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_20 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_20 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_225 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_225 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_25 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_25 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_275 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_275 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_30 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_30 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_325 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_325 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_35 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_35 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_375 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_375 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_40 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_40 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_425 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_425 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_45 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_45 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_475 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_475 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_50 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_50 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_525 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_525 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_55 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_55 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_575 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_575 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_60 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_60 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_625 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_625 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_65 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_65 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_675 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_675 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_70 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_70 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_75 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_75 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_85 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_85 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_over_95 = rs1[counter_col] 

        counter_col += 1
        goals_overunder_under_95 = rs1[counter_col] 
        # ------------------------------------------------------
        # ------------------------------------------------------
        ah_pattern = ""

        if( asian_handicap_home_min_675 is not None and asian_handicap_away_min_675 is not None):
            ah_total_min_675 = asian_handicap_home_min_675 + asian_handicap_away_min_675
            if(ah_total_min_675 <= min_standart):
                ah_pattern += "-675"

        if( asian_handicap_home_min_65 is not None and asian_handicap_away_min_65 is not None):
            ah_total_min_65 = asian_handicap_home_min_65 + asian_handicap_away_min_65
            if(ah_total_min_65 <= min_standart):
                ah_pattern += "-65"

        if( asian_handicap_home_min_625 is not None and asian_handicap_away_min_625 is not None):
            ah_total_min_625 = asian_handicap_home_min_625 + asian_handicap_away_min_625
            if(ah_total_min_625 <= min_standart):
                ah_pattern += "-625"

        if( asian_handicap_home_min_6 is not None and asian_handicap_away_min_6 is not None):
            ah_total_min_6 = asian_handicap_home_min_6 + asian_handicap_away_min_6
            if(ah_total_min_6 <= min_standart):
                ah_pattern += "-6"

        if( asian_handicap_home_min_575 is not None and asian_handicap_away_min_575 is not None):
            ah_total_min_575 = asian_handicap_home_min_575 + asian_handicap_away_min_575
            if(ah_total_min_575 <= min_standart):
                ah_pattern += "-575"

        if( asian_handicap_home_min_55 is not None and asian_handicap_away_min_55 is not None):
            ah_total_min_55 = asian_handicap_home_min_55 + asian_handicap_away_min_55
            if(ah_total_min_55 <= min_standart):
                ah_pattern += "-55"

        if( asian_handicap_home_min_525 is not None and asian_handicap_away_min_525 is not None):
            ah_total_min_525 = asian_handicap_home_min_525 + asian_handicap_away_min_525
            if(ah_total_min_525 <= min_standart):
                ah_pattern += "-525"

        if( asian_handicap_home_min_5 is not None and asian_handicap_away_min_5 is not None):
            ah_total_min_5 = asian_handicap_home_min_5 + asian_handicap_away_min_5
            if(ah_total_min_5 <= min_standart):
                ah_pattern += "-5"

        if( asian_handicap_home_min_475 is not None and asian_handicap_away_min_475 is not None):
            ah_total_min_475 = asian_handicap_home_min_475 + asian_handicap_away_min_475
            if(ah_total_min_475 <= min_standart):
                ah_pattern += "-475"

        if( asian_handicap_home_min_45 is not None and asian_handicap_away_min_45 is not None):
            ah_total_min_45 = asian_handicap_home_min_45 + asian_handicap_away_min_45
            if(ah_total_min_45 <= min_standart):
                ah_pattern += "-45"

        if( asian_handicap_home_min_425 is not None and asian_handicap_away_min_425 is not None):
            ah_total_min_425 = asian_handicap_home_min_425 + asian_handicap_away_min_425
            if(ah_total_min_425 <= min_standart):
                ah_pattern += "-425"

        if( asian_handicap_home_min_4 is not None and asian_handicap_away_min_4 is not None):
            ah_total_min_4 = asian_handicap_home_min_4 + asian_handicap_away_min_4
            if(ah_total_min_4 <= min_standart):
                ah_pattern += "-4"

        if( asian_handicap_home_min_375 is not None and asian_handicap_away_min_375 is not None):
            ah_total_min_375 = asian_handicap_home_min_375 + asian_handicap_away_min_375
            if(ah_total_min_375 <= min_standart):
                ah_pattern += "-375"

        if( asian_handicap_home_min_35 is not None and asian_handicap_away_min_35 is not None):
            ah_total_min_35 = asian_handicap_home_min_35 + asian_handicap_away_min_35
            if(ah_total_min_35 <= min_standart):
                ah_pattern += "-35"

        if( asian_handicap_home_min_325 is not None and asian_handicap_away_min_325 is not None):
            ah_total_min_325 = asian_handicap_home_min_325 + asian_handicap_away_min_325
            if(ah_total_min_325 <= min_standart):
                ah_pattern += "-325"

        if( asian_handicap_home_min_3 is not None and asian_handicap_away_min_3 is not None):
            ah_total_min_3 = asian_handicap_home_min_3 + asian_handicap_away_min_3
            if(ah_total_min_3 <= min_standart):
                ah_pattern += "-3"

        if( asian_handicap_home_min_275 is not None and asian_handicap_away_min_275 is not None):
            ah_total_min_275 = asian_handicap_home_min_275 + asian_handicap_away_min_275
            if(ah_total_min_275 <= min_standart):
                ah_pattern += "-275"

        if( asian_handicap_home_min_25 is not None and asian_handicap_away_min_25 is not None):
            ah_total_min_25 = asian_handicap_home_min_25 + asian_handicap_away_min_25
            if(ah_total_min_25 <= min_standart):
                ah_pattern += "-25"

        if( asian_handicap_home_min_225 is not None and asian_handicap_away_min_225 is not None):
            ah_total_min_225 = asian_handicap_home_min_225 + asian_handicap_away_min_225
            if(ah_total_min_225 <= min_standart):
                ah_pattern += "-225"

        if( asian_handicap_home_min_2 is not None and asian_handicap_away_min_2 is not None):
            ah_total_min_2 = asian_handicap_home_min_2 + asian_handicap_away_min_2
            if(ah_total_min_2 <= min_standart):
                ah_pattern += "-2"

        if( asian_handicap_home_min_175 is not None and asian_handicap_away_min_175 is not None):
            ah_total_min_175 = asian_handicap_home_min_175 + asian_handicap_away_min_175
            if(ah_total_min_175 <= min_standart):
                ah_pattern += "-175"

        if( asian_handicap_home_min_15 is not None and asian_handicap_away_min_15 is not None):
            ah_total_min_15 = asian_handicap_home_min_15 + asian_handicap_away_min_15
            if(ah_total_min_15 <= min_standart):
                ah_pattern += "-15"

        if( asian_handicap_home_min_125 is not None and asian_handicap_away_min_125 is not None):
            ah_total_min_125 = asian_handicap_home_min_125 + asian_handicap_away_min_125
            if(ah_total_min_125 <= min_standart):
                ah_pattern += "-125"

        if( asian_handicap_home_min_1 is not None and asian_handicap_away_min_1 is not None):
            ah_total_min_1 = asian_handicap_home_min_1 + asian_handicap_away_min_1
            if(ah_total_min_1 <= min_standart):
                ah_pattern += "-1"

        if( asian_handicap_home_min_075 is not None and asian_handicap_away_min_075 is not None):
            ah_total_min_075 = asian_handicap_home_min_075 + asian_handicap_away_min_075
            if(ah_total_min_075 <= min_standart):
                ah_pattern += "-075"

        if( asian_handicap_home_min_05 is not None and asian_handicap_away_min_05 is not None):
            ah_total_min_05 = asian_handicap_home_min_05 + asian_handicap_away_min_05
            if(ah_total_min_05 <= min_standart):
                ah_pattern += "-05"

        if( asian_handicap_home_min_025 is not None and asian_handicap_away_min_025 is not None):
            ah_total_min_025 = asian_handicap_home_min_025 + asian_handicap_away_min_025
            if(ah_total_min_025 <= min_standart):
                ah_pattern += "-025"

        if( asian_handicap_home_plus_0 is not None and asian_handicap_away_plus_0 is not None):
            ah_total_plus_0 = asian_handicap_home_plus_0 + asian_handicap_away_plus_0
            if(ah_total_plus_0 <= min_standart):
                ah_pattern += "+0"

        if( asian_handicap_home_plus_025 is not None and asian_handicap_away_plus_025 is not None):
            ah_total_plus_025 = asian_handicap_home_plus_025 + asian_handicap_away_plus_025
            if(ah_total_plus_025 <= min_standart):
                ah_pattern += "+025"

        if( asian_handicap_home_plus_05 is not None and asian_handicap_away_plus_05 is not None):
            ah_total_plus_05 = asian_handicap_home_plus_05 + asian_handicap_away_plus_05
            if(ah_total_plus_05 <= min_standart):
                ah_pattern += "+05"

        if( asian_handicap_home_plus_075 is not None and asian_handicap_away_plus_075 is not None):
            ah_total_plus_075 = asian_handicap_home_plus_075 + asian_handicap_away_plus_075
            if(ah_total_plus_075 <= min_standart):
                ah_pattern += "+075"

        if( asian_handicap_home_plus_1 is not None and asian_handicap_away_plus_1 is not None):
            ah_total_plus_1 = asian_handicap_home_plus_1 + asian_handicap_away_plus_1
            if(ah_total_plus_1 <= min_standart):
                ah_pattern += "+1"

        if( asian_handicap_home_plus_125 is not None and asian_handicap_away_plus_125 is not None):
            ah_total_plus_125 = asian_handicap_home_plus_125 + asian_handicap_away_plus_125
            if(ah_total_plus_125 <= min_standart):
                ah_pattern += "+125"

        if( asian_handicap_home_plus_15 is not None and asian_handicap_away_plus_15 is not None):
            ah_total_plus_15 = asian_handicap_home_plus_15 + asian_handicap_away_plus_15
            if(ah_total_plus_15 <= min_standart):
                ah_pattern += "+15"

        if( asian_handicap_home_plus_175 is not None and asian_handicap_away_plus_175 is not None):

            ah_total_plus_175 = asian_handicap_home_plus_175 + asian_handicap_away_plus_175
            if(ah_total_plus_175 <= min_standart):
                ah_pattern += "+175"

        if( asian_handicap_home_plus_2 is not None and asian_handicap_away_plus_2 is not None):
            ah_total_plus_2 = asian_handicap_home_plus_2 + asian_handicap_away_plus_2
            if(ah_total_plus_2 <= min_standart):
                ah_pattern += "+2"

        if( asian_handicap_home_plus_225 is not None and asian_handicap_away_plus_225 is not None):
            ah_total_plus_225 = asian_handicap_home_plus_225 + asian_handicap_away_plus_225
            if(ah_total_plus_225 <= min_standart):
                ah_pattern += "+225"

        if( asian_handicap_home_plus_25 is not None and asian_handicap_away_plus_25 is not None):
            ah_total_plus_25 = asian_handicap_home_plus_25 + asian_handicap_away_plus_25
            if(ah_total_plus_25 <= min_standart):
                ah_pattern += "+25"

        if( asian_handicap_home_plus_275 is not None and asian_handicap_away_plus_275 is not None):
            ah_total_plus_275 = asian_handicap_home_plus_275 + asian_handicap_away_plus_275
            if(ah_total_plus_275 <= min_standart):
                ah_pattern += "+275"

        if( asian_handicap_home_plus_3 is not None and asian_handicap_away_plus_3 is not None):
            ah_total_plus_3 = asian_handicap_home_plus_3 + asian_handicap_away_plus_3
            if(ah_total_plus_3 <= min_standart):
                ah_pattern += "+3"

        if( asian_handicap_home_plus_325 is not None and asian_handicap_away_plus_325 is not None):
            ah_total_plus_325 = asian_handicap_home_plus_325 + asian_handicap_away_plus_325
            if(ah_total_plus_325 <= min_standart):
                ah_pattern += "+325"

        if( asian_handicap_home_plus_35 is not None and asian_handicap_away_plus_35 is not None):
            ah_total_plus_35 = asian_handicap_home_plus_35 + asian_handicap_away_plus_35
            if(ah_total_plus_35 <= min_standart):
                ah_pattern += "+35"

        if( asian_handicap_home_plus_375 is not None and asian_handicap_away_plus_375 is not None):
            ah_total_plus_375 = asian_handicap_home_plus_375 + asian_handicap_away_plus_375
            if(ah_total_plus_375 <= min_standart):
                ah_pattern += "+375"

        if( asian_handicap_home_plus_4 is not None and asian_handicap_away_plus_4 is not None):
            ah_total_plus_4 = asian_handicap_home_plus_4 + asian_handicap_away_plus_4
            if(ah_total_plus_4 <= min_standart):
                ah_pattern += "+4"

        if( asian_handicap_home_plus_425 is not None and asian_handicap_away_plus_425 is not None):
            ah_total_plus_425 = asian_handicap_home_plus_425 + asian_handicap_away_plus_425
            if(ah_total_plus_425 <= min_standart):
                ah_pattern += "+425"

        if( asian_handicap_home_plus_45 is not None and asian_handicap_away_plus_45 is not None):
            ah_total_plus_45 = asian_handicap_home_plus_45 + asian_handicap_away_plus_45
            if(ah_total_plus_45 <= min_standart):
                ah_pattern += "+45"

        if( asian_handicap_home_plus_475 is not None and asian_handicap_away_plus_475 is not None):
            ah_total_plus_475 = asian_handicap_home_plus_475 + asian_handicap_away_plus_475
            if(ah_total_plus_475 <= min_standart):
                ah_pattern += "+475"

        if( asian_handicap_home_plus_5 is not None and asian_handicap_away_plus_5 is not None):
            ah_total_plus_5 = asian_handicap_home_plus_5 + asian_handicap_away_plus_5
            if(ah_total_plus_5 <= min_standart):
                ah_pattern += "+5"

        if( asian_handicap_home_plus_525 is not None and asian_handicap_away_plus_525 is not None):
            ah_total_plus_525 = asian_handicap_home_plus_525 + asian_handicap_away_plus_525
            if(ah_total_plus_525 <= min_standart):
                ah_pattern += "+525"

        if( asian_handicap_home_plus_55 is not None and asian_handicap_away_plus_55 is not None):
            ah_total_plus_55 = asian_handicap_home_plus_55 + asian_handicap_away_plus_55
            if(ah_total_plus_55 <= min_standart):
                ah_pattern += "+55"

        if( asian_handicap_home_plus_575 is not None and asian_handicap_away_plus_575 is not None):
            ah_total_plus_575 = asian_handicap_home_plus_575 + asian_handicap_away_plus_575
            if(ah_total_plus_575 <= min_standart):
                ah_pattern += "+575"

        if( asian_handicap_home_plus_6 is not None and asian_handicap_away_plus_6 is not None):
            ah_total_plus_6 = asian_handicap_home_plus_6 + asian_handicap_away_plus_6
            if(ah_total_plus_6 <= min_standart):
                ah_pattern += "+6"

        if( asian_handicap_home_plus_625 is not None and asian_handicap_away_plus_625 is not None):
            ah_total_plus_625 = asian_handicap_home_plus_625 + asian_handicap_away_plus_625
            if(ah_total_plus_625 <= min_standart):
                ah_pattern += "+625"

        if( asian_handicap_home_plus_65 is not None and asian_handicap_away_plus_65 is not None):
            ah_total_plus_65 = asian_handicap_home_plus_65 + asian_handicap_away_plus_65
            if(ah_total_plus_65 <= min_standart):
                ah_pattern += "+65"

        if( asian_handicap_home_plus_675 is not None and asian_handicap_away_plus_675 is not None):
            ah_total_plus_675 = asian_handicap_home_plus_675 + asian_handicap_away_plus_675
            if(ah_total_plus_675 <= min_standart):
                ah_pattern += "+675"
                
        # ------------------------------------------------------
        # ------------------------------------------------------
        ah_pattern_mirror = ""

        if( asian_handicap_away_plus_675 is not None and asian_handicap_home_plus_675 is not None):
            ah_total_plus_675_mirror = asian_handicap_away_plus_675 + asian_handicap_home_plus_675
            if(ah_total_plus_675_mirror <= min_standart):
                ah_pattern_mirror += "-675"

        if( asian_handicap_away_plus_65 is not None and asian_handicap_home_plus_65 is not None):
            ah_total_plus_65_mirror = asian_handicap_away_plus_65 + asian_handicap_home_plus_65
            if(ah_total_plus_65_mirror <= min_standart):
                ah_pattern_mirror += "-65"

        if( asian_handicap_away_plus_625 is not None and asian_handicap_home_plus_625 is not None):
            ah_total_plus_625_mirror = asian_handicap_away_plus_625 + asian_handicap_home_plus_625
            if(ah_total_plus_625_mirror <= min_standart):
                ah_pattern_mirror += "-625"

        if( asian_handicap_away_plus_6 is not None and asian_handicap_home_plus_6 is not None):
            ah_total_plus_6_mirror = asian_handicap_away_plus_6 + asian_handicap_home_plus_6
            if(ah_total_plus_6_mirror <= min_standart):
                ah_pattern_mirror += "-6"

        if( asian_handicap_away_plus_575 is not None and asian_handicap_home_plus_575 is not None):
            ah_total_plus_575_mirror = asian_handicap_away_plus_575 + asian_handicap_home_plus_575
            if(ah_total_plus_575_mirror <= min_standart):
                ah_pattern_mirror += "-575"

        if( asian_handicap_away_plus_55 is not None and asian_handicap_home_plus_55 is not None):
            ah_total_plus_55_mirror = asian_handicap_away_plus_55 + asian_handicap_home_plus_55
            if(ah_total_plus_55_mirror <= min_standart):
                ah_pattern_mirror += "-55"

        if( asian_handicap_away_plus_525 is not None and asian_handicap_home_plus_525 is not None):
            ah_total_plus_525_mirror = asian_handicap_away_plus_525 + asian_handicap_home_plus_525
            if(ah_total_plus_525_mirror <= min_standart):
                ah_pattern_mirror += "-525"

        if( asian_handicap_away_plus_5 is not None and asian_handicap_home_plus_5 is not None):
            ah_total_plus_5_mirror = asian_handicap_away_plus_5 + asian_handicap_home_plus_5
            if(ah_total_plus_5_mirror <= min_standart):
                ah_pattern_mirror += "-5"

        if( asian_handicap_away_plus_475 is not None and asian_handicap_home_plus_475 is not None):
            ah_total_plus_475_mirror = asian_handicap_away_plus_475 + asian_handicap_home_plus_475
            if(ah_total_plus_475_mirror <= min_standart):
                ah_pattern_mirror += "-475"

        if( asian_handicap_away_plus_45 is not None and asian_handicap_home_plus_45 is not None):
            ah_total_plus_45_mirror = asian_handicap_away_plus_45 + asian_handicap_home_plus_45
            if(ah_total_plus_45_mirror <= min_standart):
                ah_pattern_mirror += "-45"

        if( asian_handicap_away_plus_425 is not None and asian_handicap_home_plus_425 is not None):
            ah_total_plus_425_mirror = asian_handicap_away_plus_425 + asian_handicap_home_plus_425
            if(ah_total_plus_425_mirror <= min_standart):
                ah_pattern_mirror += "-425"

        if( asian_handicap_away_plus_4 is not None and asian_handicap_home_plus_4 is not None):
            ah_total_plus_4_mirror = asian_handicap_away_plus_4 + asian_handicap_home_plus_4
            if(ah_total_plus_4_mirror <= min_standart):
                ah_pattern_mirror += "-4"

        if( asian_handicap_away_plus_375 is not None and asian_handicap_home_plus_375 is not None):
            ah_total_plus_375_mirror = asian_handicap_away_plus_375 + asian_handicap_home_plus_375
            if(ah_total_plus_375_mirror <= min_standart):
                ah_pattern_mirror += "-375"

        if( asian_handicap_away_plus_35 is not None and asian_handicap_home_plus_35 is not None):
            ah_total_plus_35_mirror = asian_handicap_away_plus_35 + asian_handicap_home_plus_35
            if(ah_total_plus_35_mirror <= min_standart):
                ah_pattern_mirror += "-35"

        if( asian_handicap_away_plus_325 is not None and asian_handicap_home_plus_325 is not None):
            ah_total_plus_325_mirror = asian_handicap_away_plus_325 + asian_handicap_home_plus_325
            if(ah_total_plus_325_mirror <= min_standart):
                ah_pattern_mirror += "-325"

        if( asian_handicap_away_plus_3 is not None and asian_handicap_home_plus_3 is not None):
            ah_total_plus_3_mirror = asian_handicap_away_plus_3 + asian_handicap_home_plus_3
            if(ah_total_plus_3_mirror <= min_standart):
                ah_pattern_mirror += "-3"

        if( asian_handicap_away_plus_275 is not None and asian_handicap_home_plus_275 is not None):
            ah_total_plus_275_mirror = asian_handicap_away_plus_275 + asian_handicap_home_plus_275
            if(ah_total_plus_275_mirror <= min_standart):
                ah_pattern_mirror += "-275"

        if( asian_handicap_away_plus_25 is not None and asian_handicap_home_plus_25 is not None):
            ah_total_plus_25_mirror = asian_handicap_away_plus_25 + asian_handicap_home_plus_25
            if(ah_total_plus_25_mirror <= min_standart):
                ah_pattern_mirror += "-25"

        if( asian_handicap_away_plus_225 is not None and asian_handicap_home_plus_225 is not None):
            ah_total_plus_225_mirror = asian_handicap_away_plus_225 + asian_handicap_home_plus_225
            if(ah_total_plus_225_mirror <= min_standart):
                ah_pattern_mirror += "-225"

        if( asian_handicap_away_plus_2 is not None and asian_handicap_home_plus_2 is not None):
            ah_total_plus_2_mirror = asian_handicap_away_plus_2 + asian_handicap_home_plus_2
            if(ah_total_plus_2_mirror <= min_standart):
                ah_pattern_mirror += "-2"

        if( asian_handicap_away_plus_175 is not None and asian_handicap_home_plus_175 is not None):
            ah_total_plus_175_mirror = asian_handicap_away_plus_175 + asian_handicap_home_plus_175
            if(ah_total_plus_175_mirror <= min_standart):
                ah_pattern_mirror += "-175"

        if( asian_handicap_away_plus_15 is not None and asian_handicap_home_plus_15 is not None):
            ah_total_plus_15_mirror = asian_handicap_away_plus_15 + asian_handicap_home_plus_15
            if(ah_total_plus_15_mirror <= min_standart):
                ah_pattern_mirror += "-15"

        if( asian_handicap_away_plus_125 is not None and asian_handicap_home_plus_125 is not None):
            ah_total_plus_125_mirror = asian_handicap_away_plus_125 + asian_handicap_home_plus_125
            if(ah_total_plus_125_mirror <= min_standart):
                ah_pattern_mirror += "-125"

        if( asian_handicap_away_plus_1 is not None and asian_handicap_home_plus_1 is not None):
            ah_total_plus_1_mirror = asian_handicap_away_plus_1 + asian_handicap_home_plus_1
            if(ah_total_plus_1_mirror <= min_standart):
                ah_pattern_mirror += "-1"

        if( asian_handicap_away_plus_075 is not None and asian_handicap_home_plus_075 is not None):
            ah_total_plus_075_mirror = asian_handicap_away_plus_075 + asian_handicap_home_plus_075
            if(ah_total_plus_075_mirror <= min_standart):
                ah_pattern_mirror += "-075"

        if( asian_handicap_away_plus_05 is not None and asian_handicap_home_plus_05 is not None):
            ah_total_plus_05_mirror = asian_handicap_away_plus_05 + asian_handicap_home_plus_05
            if(ah_total_plus_05_mirror <= min_standart):
                ah_pattern_mirror += "-05"

        if( asian_handicap_away_plus_025 is not None and asian_handicap_home_plus_025 is not None):
            ah_total_plus_025_mirror = asian_handicap_away_plus_025 + asian_handicap_home_plus_025
            if(ah_total_plus_025_mirror <= min_standart):
                ah_pattern_mirror += "-025"

        if( asian_handicap_away_plus_0 is not None and asian_handicap_home_plus_0 is not None):
            ah_total_plus_0_mirror = asian_handicap_away_plus_0 + asian_handicap_home_plus_0
            if(ah_total_plus_0_mirror <= min_standart):
                ah_pattern_mirror += "+0"

        if( asian_handicap_away_min_025 is not None and asian_handicap_home_min_025 is not None):
            ah_total_min_025_mirror = asian_handicap_away_min_025 + asian_handicap_home_min_025
            if(ah_total_min_025_mirror <= min_standart):
                ah_pattern_mirror += "+025"

        if( asian_handicap_away_min_05 is not None and asian_handicap_home_min_05 is not None):
            ah_total_min_05_mirror = asian_handicap_away_min_05 + asian_handicap_home_min_05
            if(ah_total_min_05_mirror <= min_standart):
                ah_pattern_mirror += "+05"

        if( asian_handicap_away_min_075 is not None and asian_handicap_home_min_075 is not None):
            ah_total_min_075_mirror = asian_handicap_away_min_075 + asian_handicap_home_min_075
            if(ah_total_min_075_mirror <= min_standart):

                ah_pattern_mirror += "+075"

        if( asian_handicap_away_min_1 is not None and asian_handicap_home_min_1 is not None):
            ah_total_min_1_mirror = asian_handicap_away_min_1 + asian_handicap_home_min_1
            if(ah_total_min_1_mirror <= min_standart):
                ah_pattern_mirror += "+1"

        if( asian_handicap_away_min_125 is not None and asian_handicap_home_min_125 is not None):
            ah_total_min_125_mirror = asian_handicap_away_min_125 + asian_handicap_home_min_125
            if(ah_total_min_125_mirror <= min_standart):
                ah_pattern_mirror += "+125"

        if( asian_handicap_away_min_15 is not None and asian_handicap_home_min_15 is not None):
            ah_total_min_15_mirror = asian_handicap_away_min_15 + asian_handicap_home_min_15
            if(ah_total_min_15_mirror <= min_standart):
                ah_pattern_mirror += "+15"

        if( asian_handicap_away_min_175 is not None and asian_handicap_home_min_175 is not None):
            ah_total_min_175_mirror = asian_handicap_away_min_175 + asian_handicap_home_min_175
            if(ah_total_min_175_mirror <= min_standart):
                ah_pattern_mirror += "+175"

        if( asian_handicap_away_min_2 is not None and asian_handicap_home_min_2 is not None):
            ah_total_min_2_mirror = asian_handicap_away_min_2 + asian_handicap_home_min_2
            if(ah_total_min_2_mirror <= min_standart):
                ah_pattern_mirror += "+2"

        if( asian_handicap_away_min_225 is not None and asian_handicap_home_min_225 is not None):
            ah_total_min_225_mirror = asian_handicap_away_min_225 + asian_handicap_home_min_225
            if(ah_total_min_225_mirror <= min_standart):
                ah_pattern_mirror += "+225"

        if( asian_handicap_away_min_25 is not None and asian_handicap_home_min_25 is not None):
            ah_total_min_25_mirror = asian_handicap_away_min_25 + asian_handicap_home_min_25
            if(ah_total_min_25_mirror <= min_standart):
                ah_pattern_mirror += "+25"

        if( asian_handicap_away_min_275 is not None and asian_handicap_home_min_275 is not None):
            ah_total_min_275_mirror = asian_handicap_away_min_275 + asian_handicap_home_min_275
            if(ah_total_min_275_mirror <= min_standart):
                ah_pattern_mirror += "+275"

        if( asian_handicap_away_min_3 is not None and asian_handicap_home_min_3 is not None):
            ah_total_min_3_mirror = asian_handicap_away_min_3 + asian_handicap_home_min_3
            if(ah_total_min_3_mirror <= min_standart):
                ah_pattern_mirror += "+3"

        if( asian_handicap_away_min_325 is not None and asian_handicap_home_min_325 is not None):
            ah_total_min_325_mirror = asian_handicap_away_min_325 + asian_handicap_home_min_325
            if(ah_total_min_325_mirror <= min_standart):
                ah_pattern_mirror += "+325"

        if( asian_handicap_away_min_35 is not None and asian_handicap_home_min_35 is not None):
            ah_total_min_35_mirror = asian_handicap_away_min_35 + asian_handicap_home_min_35
            if(ah_total_min_35_mirror <= min_standart):
                ah_pattern_mirror += "+35"

        if( asian_handicap_away_min_375 is not None and asian_handicap_home_min_375 is not None):
            ah_total_min_375_mirror = asian_handicap_away_min_375 + asian_handicap_home_min_375
            if(ah_total_min_375_mirror <= min_standart):
                ah_pattern_mirror += "+375"

        if( asian_handicap_away_min_4 is not None and asian_handicap_home_min_4 is not None):
            ah_total_min_4_mirror = asian_handicap_away_min_4 + asian_handicap_home_min_4
            if(ah_total_min_4_mirror <= min_standart):
                ah_pattern_mirror += "+4"

        if( asian_handicap_away_min_425 is not None and asian_handicap_home_min_425 is not None):
            ah_total_min_425_mirror = asian_handicap_away_min_425 + asian_handicap_home_min_425
            if(ah_total_min_425_mirror <= min_standart):
                ah_pattern_mirror += "+425"

        if( asian_handicap_away_min_45 is not None and asian_handicap_home_min_45 is not None):
            ah_total_min_45_mirror = asian_handicap_away_min_45 + asian_handicap_home_min_45
            if(ah_total_min_45_mirror <= min_standart):
                ah_pattern_mirror += "+45"

        if( asian_handicap_away_min_475 is not None and asian_handicap_home_min_475 is not None):
            ah_total_min_475_mirror = asian_handicap_away_min_475 + asian_handicap_home_min_475
            if(ah_total_min_475_mirror <= min_standart):
                ah_pattern_mirror += "+475"

        if( asian_handicap_away_min_5 is not None and asian_handicap_home_min_5 is not None):
            ah_total_min_5_mirror = asian_handicap_away_min_5 + asian_handicap_home_min_5
            if(ah_total_min_5_mirror <= min_standart):
                ah_pattern_mirror += "+5"

        if( asian_handicap_away_min_525 is not None and asian_handicap_home_min_525 is not None):
            ah_total_min_525_mirror = asian_handicap_away_min_525 + asian_handicap_home_min_525
            if(ah_total_min_525_mirror <= min_standart):
                ah_pattern_mirror += "+525"

        if( asian_handicap_away_min_55 is not None and asian_handicap_home_min_55 is not None):
            ah_total_min_55_mirror = asian_handicap_away_min_55 + asian_handicap_home_min_55
            if(ah_total_min_55_mirror <= min_standart):
                ah_pattern_mirror += "+55"

        if( asian_handicap_away_min_575 is not None and asian_handicap_home_min_575 is not None):
            ah_total_min_575_mirror = asian_handicap_away_min_575 + asian_handicap_home_min_575
            if(ah_total_min_575_mirror <= min_standart):
                ah_pattern_mirror += "+575"

        if( asian_handicap_away_min_6 is not None and asian_handicap_home_min_6 is not None):
            ah_total_min_6_mirror = asian_handicap_away_min_6 + asian_handicap_home_min_6
            if(ah_total_min_6_mirror <= min_standart):
                ah_pattern_mirror += "+6"

        if( asian_handicap_away_min_625 is not None and asian_handicap_home_min_625 is not None):
            ah_total_min_625_mirror = asian_handicap_away_min_625 + asian_handicap_home_min_625
            if(ah_total_min_625_mirror <= min_standart):
                ah_pattern_mirror += "+625"

        if( asian_handicap_away_min_65 is not None and asian_handicap_home_min_65 is not None):
            ah_total_min_65_mirror = asian_handicap_away_min_65 + asian_handicap_home_min_65
            if(ah_total_min_65_mirror <= min_standart):
                ah_pattern_mirror += "+65"

        if( asian_handicap_away_min_675 is not None and asian_handicap_home_min_675 is not None):
            ah_total_min_675_mirror = asian_handicap_away_min_675 + asian_handicap_home_min_675
            if(ah_total_min_675_mirror <= min_standart):
                ah_pattern_mirror += "+675"
                
        # ------------------------------------------------------
        # ------------------------------------------------------
        gou_pattern = ""

        if( goals_overunder_over_05 is not None and goals_overunder_under_05 is not None):
            gou_total_05 = goals_overunder_over_05 + goals_overunder_under_05
            if(gou_total_05 <= min_standart):
                gou_pattern += "05g"

        if( goals_overunder_over_075 is not None and goals_overunder_under_075 is not None):
            gou_total_075 = goals_overunder_over_075 + goals_overunder_under_075
            if(gou_total_075 <= min_standart):
                gou_pattern += "075g"

        if( goals_overunder_over_10 is not None and goals_overunder_under_10 is not None):
            gou_total_10 = goals_overunder_over_10 + goals_overunder_under_10
            if(gou_total_10 <= min_standart):
                gou_pattern += "10g"

        if( goals_overunder_over_125 is not None and goals_overunder_under_125 is not None):
            gou_total_125 = goals_overunder_over_125 + goals_overunder_under_125
            if(gou_total_125 <= min_standart):
                gou_pattern += "125g"

        if( goals_overunder_over_15 is not None and goals_overunder_under_15 is not None):
            gou_total_15 = goals_overunder_over_15 + goals_overunder_under_15
            if(gou_total_15 <= min_standart):
                gou_pattern += "15g"

        if( goals_overunder_over_175 is not None and goals_overunder_under_175 is not None):
            gou_total_175 = goals_overunder_over_175 + goals_overunder_under_175
            if(gou_total_175 <= min_standart):
                gou_pattern += "175g"

        if( goals_overunder_over_20 is not None and goals_overunder_under_20 is not None):
            gou_total_20 = goals_overunder_over_20 + goals_overunder_under_20
            if(gou_total_20 <= min_standart):
                gou_pattern += "20g"

        if( goals_overunder_over_225 is not None and goals_overunder_under_225 is not None):
            gou_total_225 = goals_overunder_over_225 + goals_overunder_under_225
            if(gou_total_225 <= min_standart):
                gou_pattern += "225g"

        if( goals_overunder_over_25 is not None and goals_overunder_under_25 is not None):
            gou_total_25 = goals_overunder_over_25 + goals_overunder_under_25
            if(gou_total_25 <= min_standart):
                gou_pattern += "25g"

        if( goals_overunder_over_275 is not None and goals_overunder_under_275 is not None):
            gou_total_275 = goals_overunder_over_275 + goals_overunder_under_275
            if(gou_total_275 <= min_standart):
                gou_pattern += "275g"

        if( goals_overunder_over_30 is not None and goals_overunder_under_30 is not None):
            gou_total_30 = goals_overunder_over_30 + goals_overunder_under_30
            if(gou_total_30 <= min_standart):
                gou_pattern += "30g"

        if( goals_overunder_over_325 is not None and goals_overunder_under_325 is not None):
            gou_total_325 = goals_overunder_over_325 + goals_overunder_under_325
            if(gou_total_325 <= min_standart):
                gou_pattern += "325g"

        if( goals_overunder_over_35 is not None and goals_overunder_under_35 is not None):
            gou_total_35 = goals_overunder_over_35 + goals_overunder_under_35
            if(gou_total_35 <= min_standart):
                gou_pattern += "35g"

        if( goals_overunder_over_375 is not None and goals_overunder_under_375 is not None):
            gou_total_375 = goals_overunder_over_375 + goals_overunder_under_375
            if(gou_total_375 <= min_standart):
                gou_pattern += "375g"

        if( goals_overunder_over_40 is not None and goals_overunder_under_40 is not None):
            gou_total_40 = goals_overunder_over_40 + goals_overunder_under_40
            if(gou_total_40 <= min_standart):
                gou_pattern += "40g"

        if( goals_overunder_over_425 is not None and goals_overunder_under_425 is not None):
            gou_total_425 = goals_overunder_over_425 + goals_overunder_under_425
            if(gou_total_425 <= min_standart):
                gou_pattern += "425g"

        if( goals_overunder_over_45 is not None and goals_overunder_under_45 is not None):
            gou_total_45 = goals_overunder_over_45 + goals_overunder_under_45
            if(gou_total_45 <= min_standart):
                gou_pattern += "45g"

        if( goals_overunder_over_475 is not None and goals_overunder_under_475 is not None):
            gou_total_475 = goals_overunder_over_475 + goals_overunder_under_475
            if(gou_total_475 <= min_standart):
                gou_pattern += "475g"

        if( goals_overunder_over_50 is not None and goals_overunder_under_50 is not None):
            gou_total_50 = goals_overunder_over_50 + goals_overunder_under_50
            if(gou_total_50 <= min_standart):
                gou_pattern += "50g"

        if( goals_overunder_over_525 is not None and goals_overunder_under_525 is not None):
            gou_total_525 = goals_overunder_over_525 + goals_overunder_under_525
            if(gou_total_525 <= min_standart):
                gou_pattern += "525g"

        if( goals_overunder_over_55 is not None and goals_overunder_under_55 is not None):
            gou_total_55 = goals_overunder_over_55 + goals_overunder_under_55
            if(gou_total_55 <= min_standart):
                gou_pattern += "55g"

        if( goals_overunder_over_575 is not None and goals_overunder_under_575 is not None):
            gou_total_575 = goals_overunder_over_575 + goals_overunder_under_575
            if(gou_total_575 <= min_standart):
                gou_pattern += "575g"

        if( goals_overunder_over_60 is not None and goals_overunder_under_60 is not None):
            gou_total_60 = goals_overunder_over_60 + goals_overunder_under_60
            if(gou_total_60 <= min_standart):
                gou_pattern += "60g"

        if( goals_overunder_over_625 is not None and goals_overunder_under_625 is not None):
            gou_total_625 = goals_overunder_over_625 + goals_overunder_under_625
            if(gou_total_625 <= min_standart):
                gou_pattern += "625g"

        if( goals_overunder_over_65 is not None and goals_overunder_under_65 is not None):
            gou_total_65 = goals_overunder_over_65 + goals_overunder_under_65
            if(gou_total_65 <= min_standart):
                gou_pattern += "65g"

        if( goals_overunder_over_675 is not None and goals_overunder_under_675 is not None):
            gou_total_675 = goals_overunder_over_675 + goals_overunder_under_675
            if(gou_total_675 <= min_standart):
                gou_pattern += "675g"

        if( goals_overunder_over_70 is not None and goals_overunder_under_70 is not None):
            gou_total_70 = goals_overunder_over_70 + goals_overunder_under_70
            if(gou_total_70 <= min_standart):
                gou_pattern += "70g"

        if( goals_overunder_over_75 is not None and goals_overunder_under_75 is not None):
            gou_total_75 = goals_overunder_over_75 + goals_overunder_under_75
            if(gou_total_75 <= min_standart):
                gou_pattern += "75g"

        if( goals_overunder_over_85 is not None and goals_overunder_under_85 is not None):
            gou_total_85 = goals_overunder_over_85 + goals_overunder_under_85
            if(gou_total_85 <= min_standart):
                gou_pattern += "85g"

        if( goals_overunder_over_95 is not None and goals_overunder_under_95 is not None):
            gou_total_95 = goals_overunder_over_95 + goals_overunder_under_95
            if(gou_total_95 <= min_standart):
                gou_pattern += "95g"

        # ------------------------------------------------------
        # ------------------------------------------------------
        ah_pattern += "H"
        ah_pattern_mirror += "H"
        gou_pattern += "G"
        # ------------------------------------------------------
        update_3 = "update football_odds set  "  
        # update_3 += " " + prep_col + "response = '3',  "  
        # ------------------------------------------------------
        update_3 += " " + prep_col + "ah_pattern_4 = '" + ah_pattern + "',  "  
        update_3 += " " + prep_col + "ah_pattern_mirror_4 = '" + ah_pattern_mirror + "',  "  
        update_3 += " " + prep_col + "gou_pattern_4 = '" + gou_pattern + "'  "  
        update_3 += " where fixtureapi_id = '" + str(fixtureapi_id) + "' "
        # ------------------------------------------------------
        mycursor.execute(update_3)
        mydb.commit()   
        mycursor.close()
        mydb.close()  
        # ------------------------------------------------------ 
        print(space + "> fixtureapi_id = " + str(fixtureapi_id), flush=True) 
        # ------------------------------------------------------
        print(space + "> " + prep_col + "ah_pattern_4 = " + ah_pattern + "", flush=True)
        print(space + "> " +prep_col + "ah_pattern_mirror_4 = " + ah_pattern_mirror + "", flush=True)
        print(space + "> " +prep_col + "gou_pattern_4 = " + gou_pattern + "", flush=True)
        print(space + "> football_odds update pattern_4 commited", flush=True) 
        # ------------------------------------------------------
    # ---------------------------------------------------------- 

