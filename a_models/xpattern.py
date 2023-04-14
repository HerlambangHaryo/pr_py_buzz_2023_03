# Import
import mysql.connector 
from a_models.patternlist import *  

def xp_get_league_fixture_to_reset(leagueapi_id, date, prep_col, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "xp_get_league_fixture_to_reset()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = "Select  "
    query += " teams_home_id, " 
    query += " teams_away_id, " 

    query += " leagueapi_id, " 
    query += " season, "   
    query += " fixtureapi_id "  
    
    query += " from football_fixtures " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and date <= '"+str(date)+"' "  
    query += " and fixture_status  in ('Match Finished', 'Match Finished Ended') " 
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
        xp_set_pattern(fixtureapi_id, prep_col, 'no', space)
        # ------------------------------------------------------

def xp_set_pattern(fixtureapi_id, prep_col, advice_status, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "xp_set_pattern()") 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    ah_total_675_min = ''
    ah_total_65_min = ''
    ah_total_625_min = ''
    ah_total_6_min = ''

    ah_total_575_min = ''
    ah_total_55_min = ''
    ah_total_525_min = ''
    ah_total_5_min = ''

    ah_total_475_min = ''
    ah_total_45_min = ''
    ah_total_425_min = ''
    ah_total_4_min = ''

    ah_total_375_min = ''
    ah_total_35_min = ''
    ah_total_325_min = ''
    ah_total_3_min = ''

    ah_total_275_min = ''
    ah_total_25_min = ''
    ah_total_225_min = ''
    ah_total_2_min = ''

    ah_total_175_min = ''
    ah_total_15_min = ''
    ah_total_125_min = ''
    ah_total_1_min = ''

    ah_total_075_min = ''
    ah_total_05_min = ''
    ah_total_025_min = ''

    ah_total_0 = ''

    ah_total_025 = ''
    ah_total_05 = ''
    ah_total_075 = ''

    ah_total_1 = ''
    ah_total_125 = ''
    ah_total_15 = ''
    ah_total_175 = ''

    ah_total_2 = ''
    ah_total_225 = ''
    ah_total_25 = ''
    ah_total_275 = ''

    ah_total_3 = ''
    ah_total_325 = ''
    ah_total_35 = ''
    ah_total_375 = ''

    ah_total_4 = ''
    ah_total_425 = ''
    ah_total_45 = ''
    ah_total_475 = ''

    ah_total_5 = ''
    ah_total_525 = ''
    ah_total_55 = ''
    ah_total_575 = ''

    ah_total_6 = ''
    ah_total_625 = ''
    ah_total_65 = ''
    ah_total_675 = ''

    # ---------------------------------------------------------- 
    gou_total_05 = ''
    gou_total_075 = ''

    gou_total_1 = ''
    gou_total_125 = ''
    gou_total_15 = ''
    gou_total_175 = ''

    gou_total_2 = ''
    gou_total_225 = ''
    gou_total_25 = ''
    gou_total_275 = ''

    gou_total_3 = ''
    gou_total_325 = ''
    gou_total_35 = ''
    gou_total_375 = ''

    gou_total_4 = ''
    gou_total_425 = ''
    gou_total_45 = ''
    gou_total_475 = ''

    gou_total_5 = ''
    gou_total_525 = ''
    gou_total_55 = ''
    gou_total_575 = ''

    gou_total_6 = ''
    gou_total_625 = ''
    gou_total_65 = ''
    gou_total_675 = ''

    gou_total_7 = ''
    gou_total_75 = ''
    gou_total_85 = ''
    gou_total_95 = ''

    gou_total_05 = ''
    gou_total_075 = ''

    gou_total_1 = ''
    gou_total_125 = ''
    gou_total_15 = ''
    gou_total_175 = ''

    gou_total_2 = ''
    gou_total_225 = ''
    gou_total_25 = ''
    gou_total_275 = ''

    gou_total_3 = ''
    gou_total_325 = ''
    gou_total_35 = ''
    gou_total_375 = ''

    gou_total_4 = ''
    gou_total_425 = ''
    gou_total_45 = ''
    gou_total_475 = ''

    gou_total_5 = ''
    gou_total_525 = ''
    gou_total_55 = ''
    gou_total_575 = ''

    gou_total_6 = ''
    gou_total_625 = ''
    gou_total_65 = ''
    gou_total_675 = ''

    gou_total_7 = ''
    gou_total_75 = ''
    gou_total_85 = ''
    gou_total_95 = ''

    query_1 = " Select fixtureapi_id, date  " 
    #---------------------------------------------------- 
    query_1 += ", " + prep_col + "asian_handicap_home_min_675"
    query_1 += ", " + prep_col + "asian_handicap_away_min_675"
    query_1 += ", " + prep_col + "asian_handicap_home_min_65"
    query_1 += ", " + prep_col + "asian_handicap_away_min_65"
    query_1 += ", " + prep_col + "asian_handicap_home_min_625"
    query_1 += ", " + prep_col + "asian_handicap_away_min_625"
    query_1 += ", " + prep_col + "asian_handicap_home_min_6"
    query_1 += ", " + prep_col + "asian_handicap_away_min_6" 
    #---------------------------------------------------- 
    query_1 += ", " + prep_col + "asian_handicap_home_min_575"
    query_1 += ", " + prep_col + "asian_handicap_away_min_575"
    query_1 += ", " + prep_col + "asian_handicap_home_min_55"
    query_1 += ", " + prep_col + "asian_handicap_away_min_55"
    query_1 += ", " + prep_col + "asian_handicap_home_min_525"
    query_1 += ", " + prep_col + "asian_handicap_away_min_525"
    query_1 += ", " + prep_col + "asian_handicap_home_min_5"
    query_1 += ", " + prep_col + "asian_handicap_away_min_5"

    query_1 += ", " + prep_col + "asian_handicap_home_min_475"
    query_1 += ", " + prep_col + "asian_handicap_away_min_475"
    query_1 += ", " + prep_col + "asian_handicap_home_min_45"
    query_1 += ", " + prep_col + "asian_handicap_away_min_45"
    query_1 += ", " + prep_col + "asian_handicap_home_min_425"
    query_1 += ", " + prep_col + "asian_handicap_away_min_425"
    query_1 += ", " + prep_col + "asian_handicap_home_min_4"
    query_1 += ", " + prep_col + "asian_handicap_away_min_4"

    query_1 += ", " + prep_col + "asian_handicap_home_min_375"
    query_1 += ", " + prep_col + "asian_handicap_away_min_375"
    query_1 += ", " + prep_col + "asian_handicap_home_min_35"
    query_1 += ", " + prep_col + "asian_handicap_away_min_35"
    query_1 += ", " + prep_col + "asian_handicap_home_min_325"
    query_1 += ", " + prep_col + "asian_handicap_away_min_325"
    query_1 += ", " + prep_col + "asian_handicap_home_min_3"
    query_1 += ", " + prep_col + "asian_handicap_away_min_3"

    query_1 += ", " + prep_col + "asian_handicap_home_min_275"
    query_1 += ", " + prep_col + "asian_handicap_away_min_275"
    query_1 += ", " + prep_col + "asian_handicap_home_min_25"
    query_1 += ", " + prep_col + "asian_handicap_away_min_25"
    query_1 += ", " + prep_col + "asian_handicap_home_min_225"
    query_1 += ", " + prep_col + "asian_handicap_away_min_225"
    query_1 += ", " + prep_col + "asian_handicap_home_min_2"
    query_1 += ", " + prep_col + "asian_handicap_away_min_2"
    
    query_1 += ", " + prep_col + "asian_handicap_home_min_175"
    query_1 += ", " + prep_col + "asian_handicap_away_min_175"
    query_1 += ", " + prep_col + "asian_handicap_home_min_15"
    query_1 += ", " + prep_col + "asian_handicap_away_min_15"
    query_1 += ", " + prep_col + "asian_handicap_home_min_125"
    query_1 += ", " + prep_col + "asian_handicap_away_min_125"
    query_1 += ", " + prep_col + "asian_handicap_home_min_1"
    query_1 += ", " + prep_col + "asian_handicap_away_min_1"

    query_1 += ", " + prep_col + "asian_handicap_home_min_075"
    query_1 += ", " + prep_col + "asian_handicap_away_min_075"
    query_1 += ", " + prep_col + "asian_handicap_home_min_05"
    query_1 += ", " + prep_col + "asian_handicap_away_min_05"
    query_1 += ", " + prep_col + "asian_handicap_home_min_025"
    query_1 += ", " + prep_col + "asian_handicap_away_min_025"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_0"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_0"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_025"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_025"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_05"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_05"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_075"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_075"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_1"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_1"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_125"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_125"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_15"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_15"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_175"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_175"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_2"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_2"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_225"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_225"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_25"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_25"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_275"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_275"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_3"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_3"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_325"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_325"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_35"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_35"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_375"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_375"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_4"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_4"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_425"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_425"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_45"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_45"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_475"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_475"

    query_1 += ", " + prep_col + "asian_handicap_home_plus_5"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_5"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_525"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_525"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_55"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_55"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_575"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_575"
    
    #----------------------------------------------------

    query_1 += ", " + prep_col + "asian_handicap_home_plus_6"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_6"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_625"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_625"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_65"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_65"
    query_1 += ", " + prep_col + "asian_handicap_home_plus_675"
    query_1 += ", " + prep_col + "asian_handicap_away_plus_675"
    
    #----------------------------------------------------
    
    query_1 += ", " + prep_col + "goals_overunder_over_05"
    query_1 += ", " + prep_col + "goals_overunder_under_05"
    query_1 += ", " + prep_col + "goals_overunder_over_075"
    query_1 += ", " + prep_col + "goals_overunder_under_075"

    query_1 += ", " + prep_col + "goals_overunder_over_10"
    query_1 += ", " + prep_col + "goals_overunder_under_10"
    query_1 += ", " + prep_col + "goals_overunder_over_125"
    query_1 += ", " + prep_col + "goals_overunder_under_125"
    query_1 += ", " + prep_col + "goals_overunder_over_15"
    query_1 += ", " + prep_col + "goals_overunder_under_15"
    query_1 += ", " + prep_col + "goals_overunder_over_175"
    query_1 += ", " + prep_col + "goals_overunder_under_175"

    query_1 += ", " + prep_col + "goals_overunder_over_20"
    query_1 += ", " + prep_col + "goals_overunder_under_20"
    query_1 += ", " + prep_col + "goals_overunder_over_225"
    query_1 += ", " + prep_col + "goals_overunder_under_225"
    query_1 += ", " + prep_col + "goals_overunder_over_25"
    query_1 += ", " + prep_col + "goals_overunder_under_25"
    query_1 += ", " + prep_col + "goals_overunder_over_275"
    query_1 += ", " + prep_col + "goals_overunder_under_275"

    query_1 += ", " + prep_col + "goals_overunder_over_30"
    query_1 += ", " + prep_col + "goals_overunder_under_30"
    query_1 += ", " + prep_col + "goals_overunder_over_325"
    query_1 += ", " + prep_col + "goals_overunder_under_325"
    query_1 += ", " + prep_col + "goals_overunder_over_35"
    query_1 += ", " + prep_col + "goals_overunder_under_35"
    query_1 += ", " + prep_col + "goals_overunder_over_375"
    query_1 += ", " + prep_col + "goals_overunder_under_375"

    query_1 += ", " + prep_col + "goals_overunder_over_40"
    query_1 += ", " + prep_col + "goals_overunder_under_40"
    query_1 += ", " + prep_col + "goals_overunder_over_425"
    query_1 += ", " + prep_col + "goals_overunder_under_425"
    query_1 += ", " + prep_col + "goals_overunder_over_45"
    query_1 += ", " + prep_col + "goals_overunder_under_45"
    query_1 += ", " + prep_col + "goals_overunder_over_475"
    query_1 += ", " + prep_col + "goals_overunder_under_475"

    query_1 += ", " + prep_col + "goals_overunder_over_50"
    query_1 += ", " + prep_col + "goals_overunder_under_50"
    query_1 += ", " + prep_col + "goals_overunder_over_525"
    query_1 += ", " + prep_col + "goals_overunder_under_525"
    query_1 += ", " + prep_col + "goals_overunder_over_55"
    query_1 += ", " + prep_col + "goals_overunder_under_55"
    query_1 += ", " + prep_col + "goals_overunder_over_575"
    query_1 += ", " + prep_col + "goals_overunder_under_575"

    query_1 += ", " + prep_col + "goals_overunder_over_60"
    query_1 += ", " + prep_col + "goals_overunder_under_60"
    query_1 += ", " + prep_col + "goals_overunder_over_625"
    query_1 += ", " + prep_col + "goals_overunder_under_625"
    query_1 += ", " + prep_col + "goals_overunder_over_65"
    query_1 += ", " + prep_col + "goals_overunder_under_65"
    query_1 += ", " + prep_col + "goals_overunder_over_675"
    query_1 += ", " + prep_col + "goals_overunder_under_675"

    query_1 += ", " + prep_col + "goals_overunder_over_70"
    query_1 += ", " + prep_col + "goals_overunder_under_70"
    query_1 += ", " + prep_col + "goals_overunder_over_75"
    query_1 += ", " + prep_col + "goals_overunder_under_75"

    query_1 += ", " + prep_col + "goals_overunder_over_85"
    query_1 += ", " + prep_col + "goals_overunder_under_85"

    query_1 += ", " + prep_col + "goals_overunder_over_95"
    query_1 += ", " + prep_col + "goals_overunder_under_95"
    
    
    query_1 += ", leagueapi_id"
    query_1 += " from football_fixtures "  
    query_1 += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query_1)
    result = mycursor.fetchall()
    # ----------------------------------------------------------    
    for rs1 in result: 
        counter_col = 0
        # -------------------------------------
        fixtureapi_id       = rs1[counter_col]

        counter_col += 1
        rs1_date                = rs1[counter_col]

        # -------------------------------------

        counter_col += 1
        ah_home_675_min = rs1[counter_col]

        counter_col += 1
        ah_away_675_min = rs1[counter_col]

        counter_col += 1
        ah_home_65_min = rs1[counter_col]

        counter_col += 1
        ah_away_65_min = rs1[counter_col]

        counter_col += 1
        ah_home_625_min = rs1[counter_col]

        counter_col += 1
        ah_away_625_min = rs1[counter_col]

        counter_col += 1
        ah_home_6_min = rs1[counter_col]

        counter_col += 1
        ah_away_6_min = rs1[counter_col]

        # -------------------------------------

        counter_col += 1
        ah_home_575_min = rs1[counter_col]

        counter_col += 1
        ah_away_575_min = rs1[counter_col]

        counter_col += 1
        ah_home_55_min = rs1[counter_col]

        counter_col += 1
        ah_away_55_min = rs1[counter_col]

        counter_col += 1
        ah_home_525_min = rs1[counter_col]

        counter_col += 1
        ah_away_525_min = rs1[counter_col]

        counter_col += 1
        ah_home_5_min = rs1[counter_col]

        counter_col += 1
        ah_away_5_min = rs1[counter_col]
        
        # -------------------------------------

        counter_col += 1
        ah_home_475_min = rs1[counter_col]

        counter_col += 1
        ah_away_475_min = rs1[counter_col]

        counter_col += 1
        ah_home_45_min = rs1[counter_col]

        counter_col += 1
        ah_away_45_min = rs1[counter_col]

        counter_col += 1
        ah_home_425_min = rs1[counter_col]

        counter_col += 1
        ah_away_425_min = rs1[counter_col]

        counter_col += 1
        ah_home_4_min = rs1[counter_col]

        counter_col += 1
        ah_away_4_min = rs1[counter_col]

        counter_col += 1
        ah_home_375_min = rs1[counter_col]

        counter_col += 1
        ah_away_375_min = rs1[counter_col]

        counter_col += 1
        ah_home_35_min = rs1[counter_col]

        counter_col += 1
        ah_away_35_min = rs1[counter_col]

        counter_col += 1
        ah_home_325_min = rs1[counter_col]

        counter_col += 1
        ah_away_325_min = rs1[counter_col]

        counter_col += 1
        ah_home_3_min = rs1[counter_col]

        counter_col += 1
        ah_away_3_min = rs1[counter_col]

        counter_col += 1
        ah_home_275_min = rs1[counter_col]

        counter_col += 1
        ah_away_275_min = rs1[counter_col]

        counter_col += 1
        ah_home_25_min = rs1[counter_col]

        counter_col += 1
        ah_away_25_min = rs1[counter_col]

        counter_col += 1
        ah_home_225_min = rs1[counter_col]

        counter_col += 1
        ah_away_225_min = rs1[counter_col]

        counter_col += 1
        ah_home_2_min = rs1[counter_col]

        counter_col += 1
        ah_away_2_min = rs1[counter_col]

        counter_col += 1
        ah_home_175_min = rs1[counter_col]

        counter_col += 1
        ah_away_175_min = rs1[counter_col]

        counter_col += 1
        ah_home_15_min = rs1[counter_col]

        counter_col += 1
        ah_away_15_min = rs1[counter_col]

        counter_col += 1
        ah_home_125_min = rs1[counter_col]

        counter_col += 1
        ah_away_125_min = rs1[counter_col]

        counter_col += 1
        ah_home_1_min = rs1[counter_col]

        counter_col += 1
        ah_away_1_min = rs1[counter_col]

        counter_col += 1
        ah_home_075_min = rs1[counter_col]

        counter_col += 1
        ah_away_075_min = rs1[counter_col]

        counter_col += 1
        ah_home_05_min = rs1[counter_col]

        counter_col += 1
        ah_away_05_min = rs1[counter_col]

        counter_col += 1
        ah_home_025_min = rs1[counter_col]

        counter_col += 1
        ah_away_025_min = rs1[counter_col]

        counter_col += 1
        ah_home_0 = rs1[counter_col]

        counter_col += 1
        ah_away_0 = rs1[counter_col]

        counter_col += 1
        ah_home_025 = rs1[counter_col]

        counter_col += 1
        ah_away_025 = rs1[counter_col]

        counter_col += 1
        ah_home_05 = rs1[counter_col]

        counter_col += 1
        ah_away_05 = rs1[counter_col]

        counter_col += 1
        ah_home_075 = rs1[counter_col]

        counter_col += 1
        ah_away_075 = rs1[counter_col]

        counter_col += 1
        ah_home_1 = rs1[counter_col]

        counter_col += 1
        ah_away_1 = rs1[counter_col]

        counter_col += 1
        ah_home_125 = rs1[counter_col]

        counter_col += 1
        ah_away_125 = rs1[counter_col]

        counter_col += 1
        ah_home_15 = rs1[counter_col]

        counter_col += 1
        ah_away_15 = rs1[counter_col]

        counter_col += 1
        ah_home_175 = rs1[counter_col]

        counter_col += 1
        ah_away_175 = rs1[counter_col]

        counter_col += 1
        ah_home_2 = rs1[counter_col]

        counter_col += 1
        ah_away_2 = rs1[counter_col]

        counter_col += 1
        ah_home_225 = rs1[counter_col]

        counter_col += 1
        ah_away_225 = rs1[counter_col]

        counter_col += 1
        ah_home_25 = rs1[counter_col]

        counter_col += 1
        ah_away_25 = rs1[counter_col]

        counter_col += 1
        ah_home_275 = rs1[counter_col]

        counter_col += 1
        ah_away_275 = rs1[counter_col]

        counter_col += 1
        ah_home_3 = rs1[counter_col]

        counter_col += 1
        ah_away_3 = rs1[counter_col]

        counter_col += 1
        ah_home_325 = rs1[counter_col]

        counter_col += 1
        ah_away_325 = rs1[counter_col]

        counter_col += 1
        ah_home_35 = rs1[counter_col]

        counter_col += 1
        ah_away_35 = rs1[counter_col]

        counter_col += 1
        ah_home_375 = rs1[counter_col]

        counter_col += 1
        ah_away_375 = rs1[counter_col]

        counter_col += 1
        ah_home_4 = rs1[counter_col]

        counter_col += 1
        ah_away_4 = rs1[counter_col]

        counter_col += 1
        ah_home_425 = rs1[counter_col]

        counter_col += 1
        ah_away_425 = rs1[counter_col]

        counter_col += 1
        ah_home_45 = rs1[counter_col]

        counter_col += 1
        ah_away_45 = rs1[counter_col]

        counter_col += 1
        ah_home_475 = rs1[counter_col]

        counter_col += 1
        ah_away_475 = rs1[counter_col]

        # -------------------------------------

        counter_col += 1
        ah_home_5 = rs1[counter_col]

        counter_col += 1
        ah_away_5 = rs1[counter_col]

        counter_col += 1
        ah_home_525 = rs1[counter_col]

        counter_col += 1
        ah_away_525 = rs1[counter_col]

        counter_col += 1
        ah_home_55 = rs1[counter_col]

        counter_col += 1
        ah_away_55 = rs1[counter_col]

        counter_col += 1
        ah_home_575 = rs1[counter_col]

        counter_col += 1
        ah_away_575 = rs1[counter_col]

        # -------------------------------------
        counter_col += 1
        ah_home_6 = rs1[counter_col]

        counter_col += 1
        ah_away_6 = rs1[counter_col]

        counter_col += 1
        ah_home_625 = rs1[counter_col]

        counter_col += 1
        ah_away_625 = rs1[counter_col]

        counter_col += 1
        ah_home_65 = rs1[counter_col]

        counter_col += 1
        ah_away_65 = rs1[counter_col]

        counter_col += 1
        ah_home_675 = rs1[counter_col]

        counter_col += 1
        ah_away_675 = rs1[counter_col]
        
        # -------------------------------------


        counter_col += 1
        gou_over_05 = rs1[counter_col]

        counter_col += 1
        gou_under_05 = rs1[counter_col]

        counter_col += 1
        gou_over_075 = rs1[counter_col]

        counter_col += 1
        gou_under_075 = rs1[counter_col]

        counter_col += 1
        gou_over_1 = rs1[counter_col]

        counter_col += 1
        gou_under_1 = rs1[counter_col]

        counter_col += 1
        gou_over_125 = rs1[counter_col]

        counter_col += 1
        gou_under_125 = rs1[counter_col]

        counter_col += 1
        gou_over_15 = rs1[counter_col]

        counter_col += 1
        gou_under_15 = rs1[counter_col]

        counter_col += 1
        gou_over_175 = rs1[counter_col]

        counter_col += 1
        gou_under_175 = rs1[counter_col]

        counter_col += 1
        gou_over_2 = rs1[counter_col]

        counter_col += 1
        gou_under_2 = rs1[counter_col]

        counter_col += 1
        gou_over_225 = rs1[counter_col]

        counter_col += 1
        gou_under_225 = rs1[counter_col]

        counter_col += 1
        gou_over_25 = rs1[counter_col]

        counter_col += 1
        gou_under_25 = rs1[counter_col]

        counter_col += 1
        gou_over_275 = rs1[counter_col]

        counter_col += 1
        gou_under_275 = rs1[counter_col]

        counter_col += 1
        gou_over_3 = rs1[counter_col]

        counter_col += 1
        gou_under_3 = rs1[counter_col]

        counter_col += 1
        gou_over_325 = rs1[counter_col]

        counter_col += 1
        gou_under_325 = rs1[counter_col]

        counter_col += 1
        gou_over_35 = rs1[counter_col]

        counter_col += 1
        gou_under_35 = rs1[counter_col]

        counter_col += 1
        gou_over_375 = rs1[counter_col]

        counter_col += 1
        gou_under_375 = rs1[counter_col]

        counter_col += 1
        gou_over_4 = rs1[counter_col]

        counter_col += 1
        gou_under_4 = rs1[counter_col]

        counter_col += 1
        gou_over_425 = rs1[counter_col]

        counter_col += 1
        gou_under_425 = rs1[counter_col]

        counter_col += 1
        gou_over_45 = rs1[counter_col]

        counter_col += 1
        gou_under_45 = rs1[counter_col]

        counter_col += 1
        gou_over_475 = rs1[counter_col]

        counter_col += 1
        gou_under_475 = rs1[counter_col]

        counter_col += 1
        gou_over_5 = rs1[counter_col]

        counter_col += 1
        gou_under_5 = rs1[counter_col]

        counter_col += 1
        gou_over_525 = rs1[counter_col]

        counter_col += 1
        gou_under_525 = rs1[counter_col]

        counter_col += 1
        gou_over_55 = rs1[counter_col]

        counter_col += 1
        gou_under_55 = rs1[counter_col]

        counter_col += 1
        gou_over_575 = rs1[counter_col]

        counter_col += 1
        gou_under_575 = rs1[counter_col]

        counter_col += 1
        gou_over_6 = rs1[counter_col]

        counter_col += 1
        gou_under_6 = rs1[counter_col]

        counter_col += 1
        gou_over_625 = rs1[counter_col]

        counter_col += 1
        gou_under_625 = rs1[counter_col]

        counter_col += 1
        gou_over_65 = rs1[counter_col]

        counter_col += 1
        gou_under_65 = rs1[counter_col]

        counter_col += 1
        gou_over_675 = rs1[counter_col]

        counter_col += 1
        gou_under_675 = rs1[counter_col]

        counter_col += 1
        gou_over_7 = rs1[counter_col]

        counter_col += 1
        gou_under_7 = rs1[counter_col]

        counter_col += 1
        gou_over_75 = rs1[counter_col]

        counter_col += 1
        gou_under_75 = rs1[counter_col]

        counter_col += 1
        gou_over_85 = rs1[counter_col]

        counter_col += 1
        gou_under_85 = rs1[counter_col]

        counter_col += 1
        gou_over_95 = rs1[counter_col]

        counter_col += 1
        gou_under_95 = rs1[counter_col]
        
        counter_col += 1
        leagueapi_id = rs1[counter_col]

        #----------------------------------------------------------------------
        ah_pattern = ""

        #---------------------------------------------------

        if( ah_home_675_min is not None and ah_away_675_min is not None):
            ah_total_675_min = ah_home_675_min + ah_away_675_min
            if(ah_total_675_min < 4):
                ah_pattern += "675_"
                
        if( ah_home_65_min is not None and ah_away_65_min is not None):
            ah_total_65_min = ah_home_65_min + ah_away_65_min
            if(ah_total_65_min < 4):
                ah_pattern += "65_"
                
        if( ah_home_625_min is not None and ah_away_625_min is not None):
            ah_total_625_min = ah_home_625_min + ah_away_625_min
            if(ah_total_625_min < 4):
                ah_pattern += "625_"
                
        if( ah_home_6_min is not None and ah_away_6_min is not None):
            ah_total_6_min = ah_home_6_min + ah_away_6_min
            if(ah_total_6_min < 4):
                ah_pattern += "6_"

        #---------------------------------------------------

        if( ah_home_575_min is not None and ah_away_575_min is not None):
            ah_total_575_min = ah_home_575_min + ah_away_575_min
            if(ah_total_575_min < 4):
                ah_pattern += "575_"
                
        if( ah_home_55_min is not None and ah_away_55_min is not None):
            ah_total_55_min = ah_home_55_min + ah_away_55_min
            if(ah_total_55_min < 4):
                ah_pattern += "55_"
                
        if( ah_home_525_min is not None and ah_away_525_min is not None):
            ah_total_525_min = ah_home_525_min + ah_away_525_min
            if(ah_total_525_min < 4):
                ah_pattern += "525_"
                
        if( ah_home_5_min is not None and ah_away_5_min is not None):
            ah_total_5_min = ah_home_5_min + ah_away_5_min
            if(ah_total_5_min < 4):
                ah_pattern += "5_"
        #---------------------------------------------------
                
        if( ah_home_475_min is not None and ah_away_475_min is not None):
            ah_total_475_min = ah_home_475_min + ah_away_475_min
            if(ah_total_475_min < 4):
                ah_pattern += "475_"
                
        if( ah_home_45_min is not None and ah_away_45_min is not None):
            ah_total_45_min = ah_home_45_min + ah_away_45_min
            if(ah_total_45_min < 4):
                ah_pattern += "45_"
                
        if( ah_home_425_min is not None and ah_away_425_min is not None):
            ah_total_425_min = ah_home_425_min + ah_away_425_min
            if(ah_total_425_min < 4):
                ah_pattern += "425_"
                
        if( ah_home_4_min is not None and ah_away_4_min is not None):
            ah_total_4_min = ah_home_4_min + ah_away_4_min
            if(ah_total_4_min < 4):
                ah_pattern += "4_"
                
        if( ah_home_375_min is not None and ah_away_375_min is not None):
            ah_total_375_min = ah_home_375_min + ah_away_375_min
            if(ah_total_375_min < 4):
                ah_pattern += "375_"
                
        if( ah_home_35_min is not None and ah_away_35_min is not None):
            ah_total_35_min = ah_home_35_min + ah_away_35_min
            if(ah_total_35_min < 4):
                ah_pattern += "35_"
                
        if( ah_home_325_min is not None and ah_away_325_min is not None):
            ah_total_325_min = ah_home_325_min + ah_away_325_min
            if(ah_total_325_min < 4):
                ah_pattern += "325_"
                
        if( ah_home_3_min is not None and ah_away_3_min is not None):
            ah_total_3_min = ah_home_3_min + ah_away_3_min
            if(ah_total_3_min < 4):
                ah_pattern += "3_"
                
        if( ah_home_275_min is not None and ah_away_275_min is not None):
            ah_total_275_min = ah_home_275_min + ah_away_275_min
            if(ah_total_275_min < 4):
                ah_pattern += "275_"
                
        if( ah_home_25_min is not None and ah_away_25_min is not None):
            ah_total_25_min = ah_home_25_min + ah_away_25_min
            if(ah_total_25_min < 4):
                ah_pattern += "25_"
                
        if( ah_home_225_min is not None and ah_away_225_min is not None):
            ah_total_225_min = ah_home_225_min + ah_away_225_min
            if(ah_total_225_min < 4):
                ah_pattern += "225_"
                
        if( ah_home_2_min is not None and ah_away_2_min is not None):
            ah_total_2_min   = ah_home_2_min + ah_away_2_min
            if(ah_total_2_min < 4):
                ah_pattern += "2_"
                
        if( ah_home_175_min is not None and ah_away_175_min is not None):
            ah_total_175_min      = ah_home_175_min + ah_away_175_min
            if(ah_total_175_min < 4):
                ah_pattern += "175_"
                
        if( ah_home_15_min is not None and ah_away_15_min is not None):
            ah_total_15_min      = ah_home_15_min + ah_away_15_min
            if(ah_total_15_min < 4):
                ah_pattern += "15_"
                
        if( ah_home_125_min is not None and ah_away_125_min is not None):
            ah_total_125_min = ah_home_125_min + ah_away_125_min
            if(ah_total_125_min < 4):
                ah_pattern += "125_"
                
        if( ah_home_1_min is not None and ah_away_1_min is not None):
            ah_total_1_min = ah_home_1_min + ah_away_1_min
            if(ah_total_1_min < 4):
                ah_pattern += "1_"
                
        if( ah_home_075_min is not None and ah_away_075_min is not None):
            ah_total_075_min = ah_home_075_min + ah_away_075_min
            if(ah_total_075_min < 4):
                ah_pattern += "075_"
                
        if( ah_home_05_min is not None and ah_away_05_min is not None):
            ah_total_05_min = ah_home_05_min + ah_away_05_min
            if(ah_total_05_min < 4):
                ah_pattern += "05_"
                
        if( ah_home_025_min is not None and ah_away_025_min is not None):
            ah_total_025_min = ah_home_025_min + ah_away_025_min
            if(ah_total_025_min < 4):
                ah_pattern += "025_"
                
        if( ah_home_0 is not None and ah_away_0 is not None):
            ah_total_0 = ah_home_0 + ah_away_0
            if(ah_total_0 < 4):
                ah_pattern += "0#"
                
        if( ah_home_025 is not None and ah_away_025 is not None):
            ah_total_025 = ah_home_025 + ah_away_025
            if(ah_total_025 < 4):
                ah_pattern += "025+"
                
        if( ah_home_05 is not None and ah_away_05 is not None):
            ah_total_05 = ah_home_05 + ah_away_05
            if(ah_total_05 < 4):
                ah_pattern += "05+"
                
        if( ah_home_075 is not None and ah_away_075 is not None):
            ah_total_075 = ah_home_075 + ah_away_075
            if(ah_total_075 < 4):
                ah_pattern += "075+"
                
        if( ah_home_1 is not None and ah_away_1 is not None):
            ah_total_1 = ah_home_1 + ah_away_1
            if(ah_total_1 < 4):
                ah_pattern += "1+"
                
        if( ah_home_125 is not None and ah_away_125 is not None):
            ah_total_125 = ah_home_125 + ah_away_125
            if(ah_total_125 < 4):
                ah_pattern += "125+"
                
        if( ah_home_15 is not None and ah_away_15 is not None):
            ah_total_15 = ah_home_15 + ah_away_15
            if(ah_total_15 < 4):
                ah_pattern += "15+"
                
        if( ah_home_175 is not None and ah_away_175 is not None):
            ah_total_175 = ah_home_175 + ah_away_175
            if(ah_total_175 < 4):
                ah_pattern += "175+"
                
        if( ah_home_2 is not None and ah_away_2 is not None):
            ah_total_2 = ah_home_2 + ah_away_2
            if(ah_total_2 < 4):
                ah_pattern += "2+"
                
        if( ah_home_225 is not None and ah_away_225 is not None):
            ah_total_225 = ah_home_225 + ah_away_225
            if(ah_total_225 < 4):
                ah_pattern += "225+"
                
        if( ah_home_25 is not None and ah_away_25 is not None):
            ah_total_25 = ah_home_25 + ah_away_25
            if(ah_total_25 < 4):
                ah_pattern += "25+"
                
        if( ah_home_275 is not None and ah_away_275 is not None):
            ah_total_275 = ah_home_275 + ah_away_275
            if(ah_total_275 < 4):
                ah_pattern += "275+"
                
        if( ah_home_3 is not None and ah_away_3 is not None):
            ah_total_3 = ah_home_3 + ah_away_3
            if(ah_total_3 < 4):
                ah_pattern += "3+"
                
        if( ah_home_325 is not None and ah_away_325 is not None):
            ah_total_325 = ah_home_325 + ah_away_325
            if(ah_total_325 < 4):
                ah_pattern += "325+"
                
        if( ah_home_35 is not None and ah_away_35 is not None):
            ah_total_35 = ah_home_35 + ah_away_35
            if(ah_total_35 < 4):
                ah_pattern += "35+"
                
        if( ah_home_375 is not None and ah_away_375 is not None):
            ah_total_375 = ah_home_375 + ah_away_375
            if(ah_total_375 < 4):
                ah_pattern += "375+"
                
        if( ah_home_4 is not None and ah_away_4 is not None):
            ah_total_4 = ah_home_4 + ah_away_4
            if(ah_total_4 < 4):
                ah_pattern += "4+"
                
        if( ah_home_425 is not None and ah_away_425 is not None):
            ah_total_425 = ah_home_425 + ah_away_425
            if(ah_total_425 < 4):
                ah_pattern += "425+"
                
        if( ah_home_45 is not None and ah_away_45 is not None):
            ah_total_45 = ah_home_45 + ah_away_45
            if(ah_total_45 < 4):
                ah_pattern += "45+"
                
        if( ah_home_475 is not None and ah_away_475 is not None):
            ah_total_475 = ah_home_475 + ah_away_475
            if(ah_total_475 < 4):
                ah_pattern += "475+"

        # ------------------------------------------------------
                
        if( ah_home_5 is not None and ah_away_5 is not None):
            ah_total_5 = ah_home_5 + ah_away_5
            if(ah_total_5 < 4):
                ah_pattern += "5+"
                
        if( ah_home_525 is not None and ah_away_525 is not None):
            ah_total_525 = ah_home_525 + ah_away_525
            if(ah_total_525 < 4):
                ah_pattern += "525+"
                
        if( ah_home_55 is not None and ah_away_55 is not None):
            ah_total_55 = ah_home_55 + ah_away_55
            if(ah_total_55 < 4):
                ah_pattern += "55+"
                
        if( ah_home_575 is not None and ah_away_575 is not None):
            ah_total_575 = ah_home_575 + ah_away_575
            if(ah_total_575 < 4):
                ah_pattern += "575+"

        # ------------------------------------------------------
                
        if( ah_home_6 is not None and ah_away_6 is not None):
            ah_total_6 = ah_home_6 + ah_away_6
            if(ah_total_6 < 4):
                ah_pattern += "6+"
                
        if( ah_home_625 is not None and ah_away_625 is not None):
            ah_total_625 = ah_home_625 + ah_away_625
            if(ah_total_625 < 4):
                ah_pattern += "625+"
                
        if( ah_home_65 is not None and ah_away_65 is not None):
            ah_total_65 = ah_home_65 + ah_away_65
            if(ah_total_65 < 4):
                ah_pattern += "65+"
                
        if( ah_home_675 is not None and ah_away_675 is not None):
            ah_total_675 = ah_home_675 + ah_away_675
            if(ah_total_675 < 4):
                ah_pattern += "675+"
        # ----------------------------------------------------------------------
        
        # ----------------------------------------------------------------------
        ah_pattern_mirror = ""
        # ------------------------------------------------------

        if( ah_home_675 is not None and ah_away_675 is not None):
            ah_total_675 = ah_home_675 + ah_away_675
            if(ah_total_675 < 4):
                ah_pattern_mirror += "675_"
                
        if( ah_home_65 is not None and ah_away_65 is not None):
            ah_total_65 = ah_home_65 + ah_away_65
            if(ah_total_65 < 4):
                ah_pattern_mirror += "65_"
                
        if( ah_home_625 is not None and ah_away_625 is not None):
            ah_total_625 = ah_home_625 + ah_away_625
            if(ah_total_625 < 4):
                ah_pattern_mirror += "625_"
                
        if( ah_home_6 is not None and ah_away_6 is not None):
            ah_total_6 = ah_home_6 + ah_away_6
            if(ah_total_6 < 4):
                ah_pattern_mirror += "6_"
        # ------------------------------------------------------

        if( ah_home_575 is not None and ah_away_575 is not None):
            ah_total_575 = ah_home_575 + ah_away_575
            if(ah_total_575 < 4):
                ah_pattern_mirror += "575_"
                
        if( ah_home_55 is not None and ah_away_55 is not None):
            ah_total_55 = ah_home_55 + ah_away_55
            if(ah_total_55 < 4):
                ah_pattern_mirror += "55_"
                
        if( ah_home_525 is not None and ah_away_525 is not None):
            ah_total_525 = ah_home_525 + ah_away_525
            if(ah_total_525 < 4):
                ah_pattern_mirror += "525_"
                
        if( ah_home_5 is not None and ah_away_5 is not None):
            ah_total_5 = ah_home_5 + ah_away_5
            if(ah_total_5 < 4):
                ah_pattern_mirror += "5_"

        # ------------------------------------------------------
                
        if( ah_home_475 is not None and ah_away_475 is not None):
            ah_total_475 = ah_home_475 + ah_away_475
            if(ah_total_475 < 4):
                ah_pattern_mirror += "475_"
                
        if( ah_home_45 is not None and ah_away_45 is not None):
            ah_total_45 = ah_home_45 + ah_away_45
            if(ah_total_45 < 4):
                ah_pattern_mirror += "45_"
                
        if( ah_home_425 is not None and ah_away_425 is not None):
            ah_total_425 = ah_home_425 + ah_away_425
            if(ah_total_425 < 4):
                ah_pattern_mirror += "425_"
                
        if( ah_home_4 is not None and ah_away_4 is not None):
            ah_total_4 = ah_home_4 + ah_away_4
            if(ah_total_4 < 4):
                ah_pattern_mirror += "4_"
                
        if( ah_home_375 is not None and ah_away_375 is not None):
            ah_total_375 = ah_home_375 + ah_away_375
            if(ah_total_375 < 4):
                ah_pattern_mirror += "375_"
                
        if( ah_home_35 is not None and ah_away_35 is not None):
            ah_total_35 = ah_home_35 + ah_away_35
            if(ah_total_35 < 4):
                ah_pattern_mirror += "35_"
                
        if( ah_home_325 is not None and ah_away_325 is not None):
            ah_total_325 = ah_home_325 + ah_away_325
            if(ah_total_325 < 4):
                ah_pattern_mirror += "325_"
                
        if( ah_home_3 is not None and ah_away_3 is not None):
            ah_total_3 = ah_home_3 + ah_away_3
            if(ah_total_3 < 4):
                ah_pattern_mirror += "3_"
                
        if( ah_home_275 is not None and ah_away_275 is not None):
            ah_total_275 = ah_home_275 + ah_away_275
            if(ah_total_275 < 4):
                ah_pattern_mirror += "275_"
                
        if( ah_home_25 is not None and ah_away_25 is not None):
            ah_total_25 = ah_home_25 + ah_away_25
            if(ah_total_25 < 4):
                ah_pattern_mirror += "25_"
                
        if( ah_home_225 is not None and ah_away_225 is not None):
            ah_total_225 = ah_home_225 + ah_away_225
            if(ah_total_225 < 4):
                ah_pattern_mirror += "225_"
                
        if( ah_home_2 is not None and ah_away_2 is not None):
            ah_total_2 = ah_home_2 + ah_away_2
            if(ah_total_2 < 4):
                ah_pattern_mirror += "2_"
                
        if( ah_home_175 is not None and ah_away_175 is not None):
            ah_total_175 = ah_home_175 + ah_away_175
            if(ah_total_175 < 4):
                ah_pattern_mirror += "175_"
                
        if( ah_home_15 is not None and ah_away_15 is not None):
            ah_total_15 = ah_home_15 + ah_away_15
            if(ah_total_15 < 4):
                ah_pattern_mirror += "15_"
                
        if( ah_home_125 is not None and ah_away_125 is not None):
            ah_total_125 = ah_home_125 + ah_away_125
            if(ah_total_125 < 4):
                ah_pattern_mirror += "125_"
                
        if( ah_home_1 is not None and ah_away_1 is not None):
            ah_total_1 = ah_home_1 + ah_away_1
            if(ah_total_1 < 4):
                ah_pattern_mirror += "1_"
                
        if( ah_home_075 is not None and ah_away_075 is not None):
            ah_total_075 = ah_home_075 + ah_away_075
            if(ah_total_075 < 4):
                ah_pattern_mirror += "075_"
                
        if( ah_home_05 is not None and ah_away_05 is not None):
            ah_total_05 = ah_home_05 + ah_away_05
            if(ah_total_05 < 4):
                ah_pattern_mirror += "05_"
                
        if( ah_home_025 is not None and ah_away_025 is not None):
            ah_total_025 = ah_home_025 + ah_away_025
            if(ah_total_025 < 4):
                ah_pattern_mirror += "025_"
                
        if( ah_home_0 is not None and ah_away_0 is not None):
            ah_total_0 = ah_home_0 + ah_away_0
            if(ah_total_0 < 4):
                ah_pattern_mirror += "0#"
                
        if( ah_home_025_min is not None and ah_away_025_min is not None):
            ah_total_025_min = ah_home_025_min + ah_away_025_min
            if(ah_total_025_min < 4):
                ah_pattern_mirror += "025+"
                
        if( ah_home_05_min is not None and ah_away_05_min is not None):
            ah_total_05_min = ah_home_05_min + ah_away_05_min
            if(ah_total_05_min < 4):
                ah_pattern_mirror += "05+"
                
        if( ah_home_075_min is not None and ah_away_075_min is not None):
            ah_total_075_min = ah_home_075_min + ah_away_075_min
            if(ah_total_075_min < 4):
                ah_pattern_mirror += "075+"
                
        if( ah_home_1_min is not None and ah_away_1_min is not None):
            ah_total_1_min = ah_home_1_min + ah_away_1_min
            if(ah_total_1_min < 4):
                ah_pattern_mirror += "1+"
                
        if( ah_home_125_min is not None and ah_away_125_min is not None):
            ah_total_125_min = ah_home_125_min + ah_away_125_min
            if(ah_total_125_min < 4):
                ah_pattern_mirror += "125+"
                
        if( ah_home_15_min is not None and ah_away_15_min is not None):
            ah_total_15_min      = ah_home_15_min + ah_away_15_min
            if(ah_total_15_min < 4):
                ah_pattern_mirror += "15+"
                
        if( ah_home_175_min is not None and ah_away_175_min is not None):
            ah_total_175_min      = ah_home_175_min + ah_away_175_min
            if(ah_total_175_min < 4):
                ah_pattern_mirror += "175+"
                
        if( ah_home_2_min is not None and ah_away_2_min is not None):
            ah_total_2_min   = ah_home_2_min + ah_away_2_min
            if(ah_total_2_min < 4):
                ah_pattern_mirror += "2+"
                
        if( ah_home_225_min is not None and ah_away_225_min is not None):
            ah_total_225_min = ah_home_225_min + ah_away_225_min
            if(ah_total_225_min < 4):
                ah_pattern_mirror += "225+"
                
        if( ah_home_25_min is not None and ah_away_25_min is not None):
            ah_total_25_min = ah_home_25_min + ah_away_25_min
            if(ah_total_25_min < 4):
                ah_pattern_mirror += "25+"
                
        if( ah_home_275_min is not None and ah_away_275_min is not None):
            ah_total_275_min = ah_home_275_min + ah_away_275_min
            if(ah_total_275_min < 4):
                ah_pattern_mirror += "275+"
                
        if( ah_home_3_min is not None and ah_away_3_min is not None):
            ah_total_3_min = ah_home_3_min + ah_away_3_min
            if(ah_total_3_min < 4):
                ah_pattern_mirror += "3+"
                
        if( ah_home_325_min is not None and ah_away_325_min is not None):
            ah_total_325_min = ah_home_325_min + ah_away_325_min
            if(ah_total_325_min < 4):
                ah_pattern_mirror += "325+"
                
        if( ah_home_35_min is not None and ah_away_35_min is not None):
            ah_total_35_min = ah_home_35_min + ah_away_35_min
            if(ah_total_35_min < 4):
                ah_pattern_mirror += "35+"
                
        if( ah_home_375_min is not None and ah_away_375_min is not None):
            ah_total_375_min = ah_home_375_min + ah_away_375_min
            if(ah_total_375_min < 4):
                ah_pattern_mirror += "375+"
                
        if( ah_home_4_min is not None and ah_away_4_min is not None):
            ah_total_4_min = ah_home_4_min + ah_away_4_min
            if(ah_total_4_min < 4):
                ah_pattern_mirror += "4+"
                
        if( ah_home_425_min is not None and ah_away_425_min is not None):
            ah_total_425_min = ah_home_425_min + ah_away_425_min
            if(ah_total_425_min < 4):
                ah_pattern_mirror += "425+"
                
        if( ah_home_45_min is not None and ah_away_45_min is not None):
            ah_total_45_min = ah_home_45_min + ah_away_45_min
            if(ah_total_45_min < 4):
                ah_pattern_mirror += "45+"
                
        if( ah_home_475_min is not None and ah_away_475_min is not None):
            ah_total_475_min = ah_home_475_min + ah_away_475_min
            if(ah_total_475_min < 4):
                ah_pattern_mirror += "475+"

        # -----------------------------------------------------------
                
        if( ah_home_5_min is not None and ah_away_5_min is not None):
            ah_total_5_min = ah_home_5_min + ah_away_5_min
            if(ah_total_5_min < 4):
                ah_pattern_mirror += "5+"
                
        if( ah_home_525_min is not None and ah_away_525_min is not None):
            ah_total_525_min = ah_home_525_min + ah_away_525_min
            if(ah_total_525_min < 4):
                ah_pattern_mirror += "525+"
                
        if( ah_home_55_min is not None and ah_away_55_min is not None):
            ah_total_55_min = ah_home_55_min + ah_away_55_min
            if(ah_total_55_min < 4):
                ah_pattern_mirror += "55+"

        if( ah_home_575_min is not None and ah_away_575_min is not None):
            ah_total_575_min = ah_home_575_min + ah_away_575_min
            if(ah_total_575_min < 4):
                ah_pattern_mirror += "575+"
                
                
        # -----------------------------------------------------------
                
        if( ah_home_6_min is not None and ah_away_6_min is not None):
            ah_total_6_min = ah_home_6_min + ah_away_6_min
            if(ah_total_6_min < 4):
                ah_pattern_mirror += "6+"
                
        if( ah_home_625_min is not None and ah_away_625_min is not None):
            ah_total_625_min = ah_home_625_min + ah_away_625_min
            if(ah_total_625_min < 4):
                ah_pattern_mirror += "625+"
                
        if( ah_home_65_min is not None and ah_away_65_min is not None):
            ah_total_65_min = ah_home_65_min + ah_away_65_min
            if(ah_total_65_min < 4):
                ah_pattern_mirror += "65+"

        if( ah_home_675_min is not None and ah_away_675_min is not None):
            ah_total_675_min = ah_home_675_min + ah_away_675_min
            if(ah_total_675_min < 4):
                ah_pattern_mirror += "675+"
        # ----------------------------------------------------------------------
        
        #----------------------------------------------------------------------
        gou_pattern = ""

        if( gou_over_05 is not None and gou_under_05 is not None):
            gou_total_05 = gou_over_05 + gou_under_05
            if(gou_total_05 < 4):
                gou_pattern += "05g"
                
        if( gou_over_075 is not None and gou_under_075 is not None):
            gou_total_075 = gou_over_075 + gou_under_075
            if(gou_total_075 < 4):
                gou_pattern += "075g"
                
        if( gou_over_1 is not None and gou_under_1 is not None):
            gou_total_1 = gou_over_1 + gou_under_1
            if(gou_total_1 < 4):
                gou_pattern += "1g"
                
        if( gou_over_125 is not None and gou_under_125 is not None):
            gou_total_125 = gou_over_125 + gou_under_125
            if(gou_total_125 < 4):
                gou_pattern += "125g"
                
        if( gou_over_15 is not None and gou_under_15 is not None):
            gou_total_15 = gou_over_15 + gou_under_15
            if(gou_total_15 < 4):
                gou_pattern += "15g"
                
        if( gou_over_175 is not None and gou_under_175 is not None):
            gou_total_175 = gou_over_175 + gou_under_175
            if(gou_total_175 < 4):
                gou_pattern += "175g"
                
        if( gou_over_2 is not None and gou_under_2 is not None):
            gou_total_2 = gou_over_2 + gou_under_2
            if(gou_total_2 < 4):
                gou_pattern += "2g"
                
        if( gou_over_225 is not None and gou_under_225 is not None):
            gou_total_225 = gou_over_225 + gou_under_225
            if(gou_total_225 < 4):
                gou_pattern += "225g"
                
        if( gou_over_25 is not None and gou_under_25 is not None):
            gou_total_25 = gou_over_25 + gou_under_25
            if(gou_total_25 < 4):
                gou_pattern += "25g"
                
        if( gou_over_275 is not None and gou_under_275 is not None):
            gou_total_275 = gou_over_275 + gou_under_275
            if(gou_total_275 < 4):
                gou_pattern += "275g"
                
        if( gou_over_3 is not None and gou_under_3 is not None):
            gou_total_3 = gou_over_3 + gou_under_3
            if(gou_total_3 < 4):
                gou_pattern += "3g"
                
        if( gou_over_325 is not None and gou_under_325 is not None):
            gou_total_325 = gou_over_325 + gou_under_325
            if(gou_total_325 < 4):
                gou_pattern += "325g"
                
        if( gou_over_35 is not None and gou_under_35 is not None):
            gou_total_35 = gou_over_35 + gou_under_35
            if(gou_total_35 < 4):
                gou_pattern += "35g"
                
        if( gou_over_375 is not None and gou_under_375 is not None):
            gou_total_375 = gou_over_375 + gou_under_375
            if(gou_total_375 < 4):
                gou_pattern += "375g"
                
        if( gou_over_4 is not None and gou_under_4 is not None):
            gou_total_4 = gou_over_4 + gou_under_4
            if(gou_total_4 < 4):
                gou_pattern += "4g"
                
        if( gou_over_425 is not None and gou_under_425 is not None):
            gou_total_425 = gou_over_425 + gou_under_425
            if(gou_total_425 < 4):
                gou_pattern += "425g"
                
        if( gou_over_45 is not None and gou_under_45 is not None):
            gou_total_45 = gou_over_45 + gou_under_45
            if(gou_total_45 < 4):
                gou_pattern += "45g"
                
        if( gou_over_475 is not None and gou_under_475 is not None):
            gou_total_475 = gou_over_475 + gou_under_475
            if(gou_total_475 < 4):
                gou_pattern += "475g"
                
        if( gou_over_5 is not None and gou_under_5 is not None):
            gou_total_5 = gou_over_5 + gou_under_5
            if(gou_total_5 < 4):
                gou_pattern += "5g"
                
        if( gou_over_525 is not None and gou_under_525 is not None):
            gou_total_525 = gou_over_525 + gou_under_525
            if(gou_total_525 < 4):
                gou_pattern += "525g"
                
        if( gou_over_55 is not None and gou_under_55 is not None):
            gou_total_55 = gou_over_55 + gou_under_55
            if(gou_total_55 < 4):
                gou_pattern += "55g"
                
        if( gou_over_575 is not None and gou_under_575 is not None):
            gou_total_575    = gou_over_575 + gou_under_575
            if(gou_total_575 < 4):
                gou_pattern += "575g"
                
        if( gou_over_6 is not None and gou_under_6 is not None):
            gou_total_6 = gou_over_6 + gou_under_6
            if(gou_total_6 < 4):
                gou_pattern += "6g"
                
        if( gou_over_625 is not None and gou_under_625 is not None):
            gou_total_625 = gou_over_625 + gou_under_625
            if(gou_total_625 < 4):
                gou_pattern += "625g"
                
        if( gou_over_65 is not None and gou_under_65 is not None):
            gou_total_65 = gou_over_65 + gou_under_65
            if(gou_total_65 < 4):
                gou_pattern += "65g"
                
        if( gou_over_675 is not None and gou_under_675 is not None):
            gou_total_675 = gou_over_675 + gou_under_675
            if(gou_total_675 < 4):
                gou_pattern += "675g"
                
        if( gou_over_7 is not None and gou_under_7 is not None):
            gou_total_7  = gou_over_7 + gou_under_7
            if(gou_total_7 < 4):
                gou_pattern += "7g"
                
        if( gou_over_75 is not None and gou_under_75 is not None):
            gou_total_75 = gou_over_75 + gou_under_75
            if(gou_total_75 < 4):
                gou_pattern += "75g"
                
        if( gou_over_85 is not None and gou_under_85 is not None):
            gou_total_85 = gou_over_85 + gou_under_85
            if(gou_total_85 < 4):
                gou_pattern += "85g" 
                
        if( gou_over_95 is not None and gou_under_95 is not None):
            gou_total_95 = gou_over_95 + gou_under_95
            if(gou_total_95 < 4):
                gou_pattern += "95g"  
        # -------------------------------------------------
        update_3 = "update football_fixtures set  "  
        update_3 += " " + prep_col + "ah_pattern = '" + ah_pattern + "H',  "  
        update_3 += " " + prep_col + "ah_pattern_mirror = '" + ah_pattern_mirror + "H',  "  
        update_3 += " " + prep_col + "gou_pattern = '" + gou_pattern + "G'  "  
        update_3 += " where fixtureapi_id = '" + str(fixtureapi_id) + "' " 
        # -------------------------------------------------
        mycursor.execute(update_3)
        mydb.commit()   
        # ------------------------------------------------- 
        print(space + "> fixtureapi_id = " + str(fixtureapi_id), flush=True)
        print(space + "> " + prep_col + "ah_pattern = " + ah_pattern + "H", flush=True)
        print(space + "> " +prep_col + "ah_pattern_mirror = " + ah_pattern_mirror + "H", flush=True)
        print(space + "> " +prep_col + "gou_pattern = " + gou_pattern + "G", flush=True)
        print(space + "> football_fixtures update pattern commited", flush=True)
        # -------------------------------------------------
        if(prep_col == "pre_" and advice_status == 'yes'):
            pl_predates_get_advice(fixtureapi_id, 'no', 'pre', space)
            pl_predates_get_advice(fixtureapi_id, 'yes', 'pre', space)
            aa = ''
        elif(prep_col == "end_" and advice_status == 'yes'):
            pl_predates_get_advice(fixtureapi_id, 'no', 'end', space)
            pl_predates_get_advice(fixtureapi_id, 'yes', 'end', space)
        else:
            print(space + "> no PL predates get advices", flush=True)
        # ------------------------------------------------- 
    # print("")
    
    
    
    