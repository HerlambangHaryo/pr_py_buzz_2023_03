# Import
import mysql.connector 

def fpa_group_pattern_to_assess(PARAM_1, 
                                pre_ah_pattern, pre_gou_pattern, 
                                end_ah_pattern, end_gou_pattern,  
                                pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                status, TABLE, type_of_pattern,
                                space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fpa_group_pattern_to_assess()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "status: " + status, flush=True)
    # ---------------------------------------------------------- 
    print(space + "pre_ah_pattern: " + pre_ah_pattern, flush=True)
    # ---------------------------------------------------------- 
    print(space + "pre_ah_pattern_mirror: " + pre_ah_pattern_mirror, flush=True)
    # ---------------------------------------------------------- 
    print(space + "pre_gou_pattern: " + pre_gou_pattern, flush=True)
    # ---------------------------------------------------------- 
    print(space + "end_ah_pattern: " + end_ah_pattern, flush=True)
    # ---------------------------------------------------------- 
    print(space + "end_ah_pattern_mirror: " + end_ah_pattern_mirror, flush=True)
    # ---------------------------------------------------------- 
    print(space + "end_gou_pattern: " + end_gou_pattern, flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " fo.leagueapi_id  "   

    query += " , fo.pre_ah_pattern as pre_ah"
    query += " , fo.pre_gou_pattern  "

    query += " , fo.end_ah_pattern as end_ah"
    query += " , fo.end_gou_pattern  " 

    query += " , fo.fixtureapi_id  " 
    query += " , 'Original' as statusx  " 

    # ----------------------------------------------------------  
    query += " , ff.goals_home as gHome  "
    query += " , ff.goals_away as gAway  " 

    query += " , ff.score_halftime_home as hHome  "
    query += " , ff.score_halftime_away as hAway  " 
  
    query += " , ff.score_secondtime_home as sHome  "
    query += " , ff.score_secondtime_away as sAway  " 
    # ----------------------------------------------------------  

    query += " from football_odds as fo " 
    query += " inner join football_fixtures as ff " 
    query += " on fo.leagueapi_id = ff.leagueapi_id " 
    query += " and fo.season = ff.season " 
    query += " and fo.fixtureapi_id = ff.fixtureapi_id " 

    query += " where ff.fixture_status IN ('Match Finished', 'Match Finished Ended') "  

    if(type_of_pattern == 1):
        query += " and fo.leagueapi_id = '"+str(PARAM_1)+"' "  
    elif(type_of_pattern == 2):
        query += " and fo.leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues`  where country_name = '"+str(PARAM_1)+"') " 

    if(status == 'Pre-Pre'): 
        query += " and fo.pre_ah_pattern = '"+str(pre_ah_pattern)+"' "  
        query += " and fo.pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  
        
        query += " and fo.end_ah_pattern = '"+str(pre_ah_pattern)+"' "  
        query += " and fo.end_gou_pattern = '"+str(pre_gou_pattern)+"' "

    elif(status == 'Pre-End'): 
        query += " and fo.pre_ah_pattern = '"+str(pre_ah_pattern)+"' "  
        query += " and fo.pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  
        
        query += " and fo.end_ah_pattern = '"+str(end_ah_pattern)+"' "  
        query += " and fo.end_gou_pattern = '"+str(end_gou_pattern)+"' "

    elif(status == 'Only-Pre'):  
        
        query += " and fo.end_ah_pattern = '"+str(pre_ah_pattern)+"' "  
        query += " and fo.end_gou_pattern = '"+str(pre_gou_pattern)+"' "

    elif(status == 'Only-End'):  
        
        query += " and fo.end_ah_pattern = '"+str(end_ah_pattern)+"' "  
        query += " and fo.end_gou_pattern = '"+str(end_gou_pattern)+"' "
    # ----------------------------------------------------------  
    query2 = "Select "
    query2 += " fo.leagueapi_id  "   

    query2 += " , fo.pre_ah_pattern_mirror as pre_ah"
    query2 += " , fo.pre_gou_pattern  "

    query2 += " , fo.end_ah_pattern_mirror as end_ah "
    query2 += " , fo.end_gou_pattern  " 

    query2 += " , fo.fixtureapi_id  " 
    query2 += " , 'Mirror' as statusx  "  

    # ----------------------------------------------------------  
    query2 += " , ff.goals_away as gHome  "
    query2 += " , ff.goals_home as gAway  " 

    query2 += " , ff.score_halftime_away as hHome  "
    query2 += " , ff.score_halftime_home as hAway  " 
  
    query2 += " , ff.score_secondtime_away as sHome  "
    query2 += " , ff.score_secondtime_home as sAway  " 
    # ----------------------------------------------------------  

    query2 += " from football_odds as fo " 
    query2 += " inner join football_fixtures as ff " 
    query2 += " on fo.leagueapi_id = ff.leagueapi_id " 
    query2 += " and fo.season = ff.season " 
    query2 += " and fo.fixtureapi_id = ff.fixtureapi_id " 

    query2 += " where ff.fixture_status IN ('Match Finished', 'Match Finished Ended') "  
    
    if(type_of_pattern == 1):
        query2 += " and fo.leagueapi_id = '"+str(PARAM_1)+"' "  
    if(type_of_pattern == 2):
        query2 += " and fo.leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues`  where country_name = '"+str(PARAM_1)+"') "  
 
    if(status == 'Pre-Pre'): 
        query2 += " and pre_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "  
        query2 += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  
        
        query2 += " and end_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "  
        query2 += " and end_gou_pattern = '"+str(pre_gou_pattern)+"' " 
        
    elif(status == 'Pre-End'): 
        query2 += " and pre_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "  
        query2 += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  
        
        query2 += " and end_ah_pattern = '"+str(end_ah_pattern_mirror)+"' "  
        query2 += " and end_gou_pattern = '"+str(end_gou_pattern)+"' " 
        
    elif(status == 'Only-Pre'):  
        
        query2 += " and end_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "  
        query2 += " and end_gou_pattern = '"+str(pre_gou_pattern)+"' " 
        
    elif(status == 'Only-End'):  
        
        query2 += " and end_ah_pattern = '"+str(end_ah_pattern_mirror)+"' "  
        query2 += " and end_gou_pattern = '"+str(end_gou_pattern)+"' " 
  
  
    # ----------------------------------------------------------   
    query_total = "("+ query +")union(" + query2 + ")"
    # query_total =   query  
    # ----------------------------------------------------------   
    print(space + query_total)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query_total)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    total_fixtures = total_rows
    # ---------------------------------------------------------- 
    counter = 0
    # ---------------------------------------------------------- 
    if(total_rows > 2):
        # ------------------------------------------------------
        print(space + "Total Row(s) to_assess : " + str(total_rows), flush=True) 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        match_winner_home_data = 0
        match_winner_home_perc = 0
        match_winner_draw_data = 0
        match_winner_draw_perc = 0
        match_winner_away_data = 0
        match_winner_away_perc = 0
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------  
        first_half_winner_home_data = 0
        first_half_winner_home_perc = 0
        first_half_winner_draw_data = 0
        first_half_winner_draw_perc = 0
        first_half_winner_away_data = 0
        first_half_winner_away_perc = 0 
        # ----------------------------------------------------------  
        homeaway_home_data = 0
        homeaway_home_perc = 0
        homeaway_away_data = 0
        homeaway_away_perc = 0
        # ----------------------------------------------------------  
        second_half_winner_home_data = 0
        second_half_winner_home_perc = 0
        second_half_winner_draw_data = 0
        second_half_winner_draw_perc = 0
        second_half_winner_away_data = 0
        second_half_winner_away_perc = 0
        # ----------------------------------------------------------  
        asian_handicap_home_min_65_data = 0
        asian_handicap_home_min_65_perc = 0
        asian_handicap_away_min_65_data = 0
        asian_handicap_away_min_65_perc = 0
        asian_handicap_home_min_6_data = 0
        asian_handicap_home_min_6_perc = 0
        asian_handicap_away_min_6_data = 0
        asian_handicap_away_min_6_perc = 0
        asian_handicap_home_min_55_data = 0
        asian_handicap_home_min_55_perc = 0
        asian_handicap_away_min_55_data = 0
        asian_handicap_away_min_55_perc = 0
        asian_handicap_home_min_5_data = 0
        asian_handicap_home_min_5_perc = 0
        asian_handicap_away_min_5_data = 0
        asian_handicap_away_min_5_perc = 0
        asian_handicap_home_min_45_data = 0
        asian_handicap_home_min_45_perc = 0
        asian_handicap_away_min_45_data = 0
        asian_handicap_away_min_45_perc = 0
        asian_handicap_home_min_4_data = 0
        asian_handicap_home_min_4_perc = 0
        asian_handicap_away_min_4_data = 0
        asian_handicap_away_min_4_perc = 0
        asian_handicap_home_min_35_data = 0
        asian_handicap_home_min_35_perc = 0
        asian_handicap_away_min_35_data = 0
        asian_handicap_away_min_35_perc = 0
        asian_handicap_home_min_3_data = 0
        asian_handicap_home_min_3_perc = 0
        asian_handicap_away_min_3_data = 0
        asian_handicap_away_min_3_perc = 0
        asian_handicap_home_min_25_data = 0
        asian_handicap_home_min_25_perc = 0
        asian_handicap_away_min_25_data = 0
        asian_handicap_away_min_25_perc = 0
        asian_handicap_home_min_2_data = 0
        asian_handicap_home_min_2_perc = 0
        asian_handicap_away_min_2_data = 0
        asian_handicap_away_min_2_perc = 0
        asian_handicap_home_min_15_data = 0
        asian_handicap_home_min_15_perc = 0
        asian_handicap_away_min_15_data = 0
        asian_handicap_away_min_15_perc = 0
        asian_handicap_home_min_1_data = 0
        asian_handicap_home_min_1_perc = 0
        asian_handicap_away_min_1_data = 0
        asian_handicap_away_min_1_perc = 0
        asian_handicap_home_min_05_data = 0
        asian_handicap_home_min_05_perc = 0
        asian_handicap_away_min_05_data = 0
        asian_handicap_away_min_05_perc = 0
        asian_handicap_home_plus_0_data = 0
        asian_handicap_home_plus_0_perc = 0
        asian_handicap_away_plus_0_data = 0
        asian_handicap_away_plus_0_perc = 0
        asian_handicap_home_plus_05_data = 0
        asian_handicap_home_plus_05_perc = 0
        asian_handicap_away_plus_05_data = 0
        asian_handicap_away_plus_05_perc = 0
        asian_handicap_home_plus_1_data = 0
        asian_handicap_home_plus_1_perc = 0
        asian_handicap_away_plus_1_data = 0
        asian_handicap_away_plus_1_perc = 0
        asian_handicap_home_plus_15_data = 0
        asian_handicap_home_plus_15_perc = 0
        asian_handicap_away_plus_15_data = 0
        asian_handicap_away_plus_15_perc = 0
        asian_handicap_home_plus_2_data = 0
        asian_handicap_home_plus_2_perc = 0
        asian_handicap_away_plus_2_data = 0
        asian_handicap_away_plus_2_perc = 0
        asian_handicap_home_plus_25_data = 0
        asian_handicap_home_plus_25_perc = 0
        asian_handicap_away_plus_25_data = 0
        asian_handicap_away_plus_25_perc = 0
        asian_handicap_home_plus_3_data = 0
        asian_handicap_home_plus_3_perc = 0
        asian_handicap_away_plus_3_data = 0
        asian_handicap_away_plus_3_perc = 0
        asian_handicap_home_plus_35_data = 0
        asian_handicap_home_plus_35_perc = 0
        asian_handicap_away_plus_35_data = 0
        asian_handicap_away_plus_35_perc = 0
        asian_handicap_home_plus_4_data = 0
        asian_handicap_home_plus_4_perc = 0
        asian_handicap_away_plus_4_data = 0
        asian_handicap_away_plus_4_perc = 0
        asian_handicap_home_plus_45_data = 0
        asian_handicap_home_plus_45_perc = 0
        asian_handicap_away_plus_45_data = 0
        asian_handicap_away_plus_45_perc = 0
        asian_handicap_home_plus_5_data = 0
        asian_handicap_home_plus_5_perc = 0
        asian_handicap_away_plus_5_data = 0
        asian_handicap_away_plus_5_perc = 0
        asian_handicap_home_plus_55_data = 0
        asian_handicap_home_plus_55_perc = 0
        asian_handicap_away_plus_55_data = 0
        asian_handicap_away_plus_55_perc = 0
        asian_handicap_home_plus_6_data = 0
        asian_handicap_home_plus_6_perc = 0
        asian_handicap_away_plus_6_data = 0
        asian_handicap_away_plus_6_perc = 0
        asian_handicap_home_plus_65_data = 0
        asian_handicap_home_plus_65_perc = 0
        asian_handicap_away_plus_65_data = 0
        asian_handicap_away_plus_65_perc = 0
        # ----------------------------------------------------------  
        goals_overunder_over_05_data = 0
        goals_overunder_over_05_perc = 0
        goals_overunder_under_05_data = 0
        goals_overunder_under_05_perc = 0
        goals_overunder_over_10_data = 0
        goals_overunder_over_10_perc = 0
        goals_overunder_under_10_data = 0
        goals_overunder_under_10_perc = 0
        goals_overunder_over_15_data = 0
        goals_overunder_over_15_perc = 0
        goals_overunder_under_15_data = 0
        goals_overunder_under_15_perc = 0
        goals_overunder_over_20_data = 0
        goals_overunder_over_20_perc = 0
        goals_overunder_under_20_data = 0
        goals_overunder_under_20_perc = 0
        goals_overunder_over_25_data = 0
        goals_overunder_over_25_perc = 0
        goals_overunder_under_25_data = 0
        goals_overunder_under_25_perc = 0
        goals_overunder_over_30_data = 0
        goals_overunder_over_30_perc = 0
        goals_overunder_under_30_data = 0
        goals_overunder_under_30_perc = 0
        goals_overunder_over_35_data = 0
        goals_overunder_over_35_perc = 0
        goals_overunder_under_35_data = 0
        goals_overunder_under_35_perc = 0
        goals_overunder_over_40_data = 0
        goals_overunder_over_40_perc = 0
        goals_overunder_under_40_data = 0
        goals_overunder_under_40_perc = 0
        goals_overunder_over_45_data = 0
        goals_overunder_over_45_perc = 0
        goals_overunder_under_45_data = 0
        goals_overunder_under_45_perc = 0
        goals_overunder_over_50_data = 0
        goals_overunder_over_50_perc = 0
        goals_overunder_under_50_data = 0
        goals_overunder_under_50_perc = 0
        goals_overunder_over_55_data = 0
        goals_overunder_over_55_perc = 0
        goals_overunder_under_55_data = 0
        goals_overunder_under_55_perc = 0
        goals_overunder_over_60_data = 0
        goals_overunder_over_60_perc = 0
        goals_overunder_under_60_data = 0
        goals_overunder_under_60_perc = 0
        goals_overunder_over_65_data = 0
        goals_overunder_over_65_perc = 0
        goals_overunder_under_65_data = 0
        goals_overunder_under_65_perc = 0
        goals_overunder_over_70_data = 0
        goals_overunder_over_70_perc = 0
        goals_overunder_under_70_data = 0
        goals_overunder_under_70_perc = 0
        goals_overunder_over_75_data = 0
        goals_overunder_over_75_perc = 0
        goals_overunder_under_75_data = 0
        goals_overunder_under_75_perc = 0
        goals_overunder_over_85_data = 0
        goals_overunder_over_85_perc = 0
        goals_overunder_under_85_data = 0
        goals_overunder_under_85_perc = 0
        goals_overunder_over_95_data = 0
        goals_overunder_over_95_perc = 0
        goals_overunder_under_95_data = 0
        goals_overunder_under_95_perc = 0
        # ----------------------------------------------------------  
        goals_overunder_first_half_over_05_data = 0
        goals_overunder_first_half_over_05_perc = 0
        goals_overunder_first_half_under_05_data = 0
        goals_overunder_first_half_under_05_perc = 0
        goals_overunder_first_half_over_10_data = 0
        goals_overunder_first_half_over_10_perc = 0
        goals_overunder_first_half_under_10_data = 0
        goals_overunder_first_half_under_10_perc = 0
        goals_overunder_first_half_over_15_data = 0
        goals_overunder_first_half_over_15_perc = 0
        goals_overunder_first_half_under_15_data = 0
        goals_overunder_first_half_under_15_perc = 0
        goals_overunder_first_half_over_20_data = 0
        goals_overunder_first_half_over_20_perc = 0
        goals_overunder_first_half_under_20_data = 0
        goals_overunder_first_half_under_20_perc = 0
        goals_overunder_first_half_over_25_data = 0
        goals_overunder_first_half_over_25_perc = 0
        goals_overunder_first_half_under_25_data = 0
        goals_overunder_first_half_under_25_perc = 0
        goals_overunder_first_half_over_30_data = 0
        goals_overunder_first_half_over_30_perc = 0
        goals_overunder_first_half_under_30_data = 0
        goals_overunder_first_half_under_30_perc = 0
        goals_overunder_first_half_over_35_data = 0
        goals_overunder_first_half_over_35_perc = 0
        goals_overunder_first_half_under_35_data = 0
        goals_overunder_first_half_under_35_perc = 0
        # ----------------------------------------------------------  
        htft_double_home_home_data = 0
        htft_double_home_home_perc = 0
        htft_double_home_draw_data = 0
        htft_double_home_draw_perc = 0
        htft_double_home_away_data = 0
        htft_double_home_away_perc = 0
        htft_double_draw_home_data = 0
        htft_double_draw_home_perc = 0
        htft_double_draw_draw_data = 0
        htft_double_draw_draw_perc = 0
        htft_double_draw_away_data = 0
        htft_double_draw_away_perc = 0
        htft_double_away_home_data = 0
        htft_double_away_home_perc = 0
        htft_double_away_draw_data = 0
        htft_double_away_draw_perc = 0
        htft_double_away_away_data = 0
        htft_double_away_away_perc = 0
        # ----------------------------------------------------------  
        both_teams_score_yes_data = 0
        both_teams_score_yes_perc = 0
        both_teams_score_no_data = 0
        both_teams_score_no_perc = 0
        # ----------------------------------------------------------  
        highest_scoring_half_first_data = 0
        highest_scoring_half_first_perc = 0
        highest_scoring_half_draw_data = 0
        highest_scoring_half_draw_perc = 0
        highest_scoring_half_second_data = 0
        highest_scoring_half_second_perc = 0
        # ----------------------------------------------------------  
        double_chance_home_draw_data = 0
        double_chance_home_draw_perc = 0
        double_chance_home_away_data = 0
        double_chance_home_away_perc = 0
        double_chance_draw_away_data = 0
        double_chance_draw_away_perc = 0
        # ----------------------------------------------------------  
        total_home_over_15_data = 0
        total_home_over_15_perc = 0
        total_home_under_15_data = 0
        total_home_under_15_perc = 0
        total_home_over_25_data = 0
        total_home_over_25_perc = 0
        total_home_under_25_data = 0
        total_home_under_25_perc = 0
        total_home_over_35_data = 0
        total_home_over_35_perc = 0
        total_home_under_35_data = 0
        total_home_under_35_perc = 0
        total_home_over_45_data = 0
        total_home_over_45_perc = 0
        total_home_under_45_data = 0
        total_home_under_45_perc = 0
        total_home_over_55_data = 0
        total_home_over_55_perc = 0
        total_home_under_55_data = 0
        total_home_under_55_perc = 0
        total_home_over_65_data = 0
        total_home_over_65_perc = 0
        total_home_under_65_data = 0
        total_home_under_65_perc = 0
        total_away_over_15_data = 0
        total_away_over_15_perc = 0
        total_away_under_15_data = 0
        total_away_under_15_perc = 0
        total_away_over_25_data = 0
        total_away_over_25_perc = 0
        total_away_under_25_data = 0
        total_away_under_25_perc = 0
        total_away_over_35_data = 0
        total_away_over_35_perc = 0
        total_away_under_35_data = 0
        total_away_under_35_perc = 0
        total_away_over_45_data = 0
        total_away_over_45_perc = 0
        total_away_under_45_data = 0
        total_away_under_45_perc = 0
        total_away_over_55_data = 0
        total_away_over_55_perc = 0
        total_away_under_55_data = 0
        total_away_under_55_perc = 0
        total_away_over_65_data = 0
        total_away_over_65_perc = 0
        total_away_under_65_data = 0
        total_away_under_65_perc = 0
        # ----------------------------------------------------------  
        asian_handicap_first_half_home_min_15_data = 0
        asian_handicap_first_half_home_min_15_perc = 0
        asian_handicap_first_half_away_min_15_data = 0
        asian_handicap_first_half_away_min_15_perc = 0
        asian_handicap_first_half_home_min_1_data = 0
        asian_handicap_first_half_home_min_1_perc = 0
        asian_handicap_first_half_away_min_1_data = 0
        asian_handicap_first_half_away_min_1_perc = 0
        asian_handicap_first_half_home_min_05_data = 0
        asian_handicap_first_half_home_min_05_perc = 0
        asian_handicap_first_half_away_min_05_data = 0
        asian_handicap_first_half_away_min_05_perc = 0
        asian_handicap_first_half_home_plus_0_data = 0
        asian_handicap_first_half_home_plus_0_perc = 0
        asian_handicap_first_half_away_plus_0_data = 0
        asian_handicap_first_half_away_plus_0_perc = 0
        asian_handicap_first_half_home_plus_05_data = 0
        asian_handicap_first_half_home_plus_05_perc = 0
        asian_handicap_first_half_away_plus_05_data = 0
        asian_handicap_first_half_away_plus_05_perc = 0
        asian_handicap_first_half_home_plus_1_data = 0
        asian_handicap_first_half_home_plus_1_perc = 0
        asian_handicap_first_half_away_plus_1_data = 0
        asian_handicap_first_half_away_plus_1_perc = 0
        asian_handicap_first_half_home_plus_15_data = 0
        asian_handicap_first_half_home_plus_15_perc = 0
        asian_handicap_first_half_away_plus_15_data = 0
        asian_handicap_first_half_away_plus_15_perc = 0
        double_chance__first_half_home_draw_data = 0
        double_chance__first_half_home_draw_perc = 0
        double_chance__first_half_home_away_data = 0
        double_chance__first_half_home_away_perc = 0
        double_chance__first_half_draw_away_data = 0
        double_chance__first_half_draw_away_perc = 0
        # ----------------------------------------------------------  
        oddeven_odd_data = 0
        oddeven_odd_perc = 0
        oddeven_even_data = 0
        oddeven_even_perc = 0
        # ----------------------------------------------------------  
        results_both_teams_score_home_yes_data = 0
        results_both_teams_score_home_yes_perc = 0
        results_both_teams_score_draw_yes_data = 0
        results_both_teams_score_draw_yes_perc = 0
        results_both_teams_score_away_yes_data = 0
        results_both_teams_score_away_yes_perc = 0
        results_both_teams_score_home_no_data = 0
        results_both_teams_score_home_no_perc = 0
        results_both_teams_score_draw_no_data = 0
        results_both_teams_score_draw_no_perc = 0
        results_both_teams_score_away_no_data = 0
        results_both_teams_score_away_no_perc = 0
        # ----------------------------------------------------------  
        result_total_goals_home_over_35_data = 0
        result_total_goals_home_over_35_perc = 0
        result_total_goals_draw_over_35_data = 0
        result_total_goals_draw_over_35_perc = 0
        result_total_goals_away_over_35_data = 0
        result_total_goals_away_over_35_perc = 0
        result_total_goals_home_under_35_data = 0
        result_total_goals_home_under_35_perc = 0
        result_total_goals_draw_under_35_data = 0
        result_total_goals_draw_under_35_perc = 0
        result_total_goals_away_under_35_data = 0
        result_total_goals_away_under_35_perc = 0
        result_total_goals_home_over_25_data = 0
        result_total_goals_home_over_25_perc = 0
        result_total_goals_draw_over_25_data = 0
        result_total_goals_draw_over_25_perc = 0
        result_total_goals_away_over_25_data = 0
        result_total_goals_away_over_25_perc = 0
        result_total_goals_home_under_25_data = 0
        result_total_goals_home_under_25_perc = 0
        result_total_goals_draw_under_25_data = 0
        result_total_goals_draw_under_25_perc = 0
        result_total_goals_away_under_25_data = 0
        result_total_goals_away_under_25_perc = 0
        # ----------------------------------------------------------  
        goals_overunder__second_half_over_05_data = 0
        goals_overunder__second_half_over_05_perc = 0
        goals_overunder__second_half_under_05_data = 0
        goals_overunder__second_half_under_05_perc = 0
        goals_overunder__second_half_over_10_data = 0
        goals_overunder__second_half_over_10_perc = 0
        goals_overunder__second_half_under_10_data = 0
        goals_overunder__second_half_under_10_perc = 0
        goals_overunder__second_half_over_15_data = 0
        goals_overunder__second_half_over_15_perc = 0
        goals_overunder__second_half_under_15_data = 0
        goals_overunder__second_half_under_15_perc = 0
        goals_overunder__second_half_over_20_data = 0
        goals_overunder__second_half_over_20_perc = 0
        goals_overunder__second_half_under_20_data = 0
        goals_overunder__second_half_under_20_perc = 0
        goals_overunder__second_half_over_25_data = 0
        goals_overunder__second_half_over_25_perc = 0
        goals_overunder__second_half_under_25_data = 0
        goals_overunder__second_half_under_25_perc = 0
        goals_overunder__second_half_over_30_data = 0
        goals_overunder__second_half_over_30_perc = 0
        goals_overunder__second_half_under_30_data = 0
        goals_overunder__second_half_under_30_perc = 0
        goals_overunder__second_half_over_35_data = 0
        goals_overunder__second_half_over_35_perc = 0
        goals_overunder__second_half_under_35_data = 0
        goals_overunder__second_half_under_35_perc = 0
        # ----------------------------------------------------------  
        clean_sheet__home_yes_data = 0
        clean_sheet__home_yes_perc = 0
        clean_sheet__home_no_data = 0
        clean_sheet__home_no_perc = 0
        # ----------------------------------------------------------  
        clean_sheet__away_yes_data = 0
        clean_sheet__away_yes_perc = 0
        clean_sheet__away_no_data = 0
        clean_sheet__away_no_perc = 0
        # ----------------------------------------------------------  
        win_both_halves_home_data = 0
        win_both_halves_home_perc = 0
        win_both_halves_away_data = 0
        win_both_halves_away_perc = 0
        # ----------------------------------------------------------  
        both_teams_score__first_half_yes_data = 0
        both_teams_score__first_half_yes_perc = 0
        both_teams_score__first_half_no_data = 0
        both_teams_score__first_half_no_perc = 0
        # ----------------------------------------------------------  
        both_teams_to_score__second_half_yes_data = 0
        both_teams_to_score__second_half_yes_perc = 0
        both_teams_to_score__second_half_no_data = 0
        both_teams_to_score__second_half_no_perc = 0
        # ----------------------------------------------------------  
        win_to_nil_home_data = 0
        win_to_nil_home_perc = 0
        win_to_nil_away_data = 0
        win_to_nil_away_perc = 0
        # ----------------------------------------------------------  
        exact_goals_number_0_data = 0
        exact_goals_number_0_perc = 0
        exact_goals_number_1_data = 0
        exact_goals_number_1_perc = 0
        exact_goals_number_2_data = 0
        exact_goals_number_2_perc = 0
        exact_goals_number_3_data = 0
        exact_goals_number_3_perc = 0
        exact_goals_number_4_data = 0
        exact_goals_number_4_perc = 0
        exact_goals_number_5_data = 0
        exact_goals_number_5_perc = 0
        exact_goals_number_6_data = 0
        exact_goals_number_6_perc = 0
        exact_goals_number_more_7_data = 0
        exact_goals_number_more_7_perc = 0
        # ----------------------------------------------------------  
        to_win_either_half_home_data = 0
        to_win_either_half_home_perc = 0
        to_win_either_half_away_data = 0
        to_win_either_half_away_perc = 0
        # ----------------------------------------------------------  
        home_team_exact_goals_number_0_data = 0
        home_team_exact_goals_number_0_perc = 0
        home_team_exact_goals_number_1_data = 0
        home_team_exact_goals_number_1_perc = 0
        home_team_exact_goals_number_2_data = 0
        home_team_exact_goals_number_2_perc = 0
        home_team_exact_goals_number_more_3_data = 0
        home_team_exact_goals_number_more_3_perc = 0
        # ----------------------------------------------------------  
        away_team_exact_goals_number_0_data = 0
        away_team_exact_goals_number_0_perc = 0
        away_team_exact_goals_number_1_data = 0
        away_team_exact_goals_number_1_perc = 0
        away_team_exact_goals_number_2_data = 0
        away_team_exact_goals_number_2_perc = 0
        away_team_exact_goals_number_more_3_data = 0
        away_team_exact_goals_number_more_3_perc = 0
        # ----------------------------------------------------------  
        second_half_exact_goals_number_0_data = 0
        second_half_exact_goals_number_0_perc = 0
        second_half_exact_goals_number_1_data = 0
        second_half_exact_goals_number_1_perc = 0
        second_half_exact_goals_number_2_data = 0
        second_half_exact_goals_number_2_perc = 0
        second_half_exact_goals_number_3_data = 0
        second_half_exact_goals_number_3_perc = 0
        second_half_exact_goals_number_4_data = 0
        second_half_exact_goals_number_4_perc = 0
        second_half_exact_goals_number_more_5_data = 0
        second_half_exact_goals_number_more_5_perc = 0
        # ----------------------------------------------------------  
        exact_goals_number__first_half_0_data = 0
        exact_goals_number__first_half_0_perc = 0
        exact_goals_number__first_half_1_data = 0
        exact_goals_number__first_half_1_perc = 0
        exact_goals_number__first_half_2_data = 0
        exact_goals_number__first_half_2_perc = 0
        exact_goals_number__first_half_3_data = 0
        exact_goals_number__first_half_3_perc = 0
        exact_goals_number__first_half_4_data = 0
        exact_goals_number__first_half_4_perc = 0
        exact_goals_number__first_half_more_5_data = 0
        exact_goals_number__first_half_more_5_perc = 0
        # ----------------------------------------------------------  
        to_score_in_both_halves_by_teams_home_data = 0
        to_score_in_both_halves_by_teams_home_perc = 0
        to_score_in_both_halves_by_teams_away_data = 0
        to_score_in_both_halves_by_teams_away_perc = 0
        # ----------------------------------------------------------  
        total_goals_both_teams_to_score_over_yes_25_data = 0
        total_goals_both_teams_to_score_over_yes_25_perc = 0
        total_goals_both_teams_to_score_over_no_25_data = 0
        total_goals_both_teams_to_score_over_no_25_perc = 0
        total_goals_both_teams_to_score_under_yes_25_data = 0
        total_goals_both_teams_to_score_under_yes_25_perc = 0
        total_goals_both_teams_to_score_under_no_25_data = 0
        total_goals_both_teams_to_score_under_no_25_perc = 0
        # ----------------------------------------------------------  
        halftime_result_both_teams_score_home_yes_data = 0
        halftime_result_both_teams_score_home_yes_perc = 0
        halftime_result_both_teams_score_draw_yes_data = 0
        halftime_result_both_teams_score_draw_yes_perc = 0
        halftime_result_both_teams_score_away_yes_data = 0
        halftime_result_both_teams_score_away_yes_perc = 0
        halftime_result_both_teams_score_home_no_data = 0
        halftime_result_both_teams_score_home_no_perc = 0
        halftime_result_both_teams_score_draw_no_data = 0
        halftime_result_both_teams_score_draw_no_perc = 0
        halftime_result_both_teams_score_away_no_data = 0
        halftime_result_both_teams_score_away_no_perc = 0
        # ----------------------------------------------------------  
        both_teams_to_score_1st_half__2nd_half_yes_yes_data = 0
        both_teams_to_score_1st_half__2nd_half_yes_yes_perc = 0
        both_teams_to_score_1st_half__2nd_half_yes_no_data = 0
        both_teams_to_score_1st_half__2nd_half_yes_no_perc = 0
        both_teams_to_score_1st_half__2nd_half_no_yes_data = 0
        both_teams_to_score_1st_half__2nd_half_no_yes_perc = 0
        both_teams_to_score_1st_half__2nd_half_no_no_data = 0
        both_teams_to_score_1st_half__2nd_half_no_no_perc = 0
        # ----------------------------------------------------------  
        total_goals_under_2_data = 0
        total_goals_under_2_perc = 0
        total_goals_2_or_3_data = 0
        total_goals_2_or_3_perc = 0
        total_goals_over_3_data = 0
        total_goals_over_3_perc = 0
        # ----------------------------------------------------------  
        # ------------------------------------------------------ 
        for x in result:    
            # --------------------------------------------------
            counter             += 1 
            # --------------------------------------------------
            leagueapi_id        = str(x[0])   
            # --------------------------------------------------
            pre_ah_pattern      = str(x[1])    
            pre_gou_pattern     = str(x[2])    
            # --------------------------------------------------
            end_ah_pattern      = str(x[3])    
            end_gou_pattern     = str(x[4])    
            # --------------------------------------------------
            fixtureapi_id       = str(x[5])    
            statusx             = str(x[6])    
            # --------------------------------------------------
            goals_home              = x[7]  
            goals_away              = x[8]  
            # --------------------------------------------------
            score_halftime_home       = x[9]   
            score_halftime_away       = x[10]    
            # --------------------------------------------------
            score_secondtime_home       = x[11]  
            score_secondtime_away       = x[12] 
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += " #" + leagueapi_id   
            word += " __ " + fixtureapi_id    
            # --------------------------------------------------
            word += " _|_ " + str(goals_home)    
            word += " __ " + str(goals_away)    
            # --------------------------------------------------
            word += " _|_ " + str(score_halftime_home)    
            word += " __ " + str(score_halftime_away)    
            # --------------------------------------------------
            word += " _|_ " + str(score_secondtime_home)    
            word += " __ " + str(score_secondtime_away)    
            print(word, flush=True)       
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------  
            # --------------------------------------------------
            btts_sts        = 'no'
            # --------------------------------------------------
            total_goals         = goals_home + goals_away 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------  
            # -------------------------------------------------- betid = 1  
            if(goals_home > goals_away):
                match_winner_home_data += 1 

            elif(goals_home == goals_away):
                match_winner_draw_data += 1

            elif(goals_home < goals_away):
                match_winner_away_data += 1
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # -------------------------------------------------- betid = 8
            if( (goals_home > 0) and (goals_away > 0) ):
                both_teams_score_yes_data += 1
                btts_sts = 'yes'
            else:
                both_teams_score_no_data += 1
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # -------------------------------------------------- betid = 2
            if(goals_home > goals_away):
                homeaway_home_data += 1  
            elif(goals_home < goals_away):
                homeaway_away_data += 1
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # -------------------------------------------------- betid = 4   
            if(goals_home > goals_away):
                asian_handicap_home_plus_0_data += 1
            elif(goals_home < goals_away):
                asian_handicap_away_plus_0_data += 1
            ## ---------------------------------------------
            if(goals_home + 0.5 > goals_away):
                asian_handicap_home_plus_05_data += 1
            elif(goals_home + 0.5 < goals_away):
                asian_handicap_away_plus_05_data += 1
            ## ---------------------------------------------
            if(goals_home + 1 > goals_away):
                asian_handicap_home_plus_1_data += 1
            elif(goals_home + 1 < goals_away):
                asian_handicap_away_plus_1_data += 1
            ## ---------------------------------------------
            if(goals_home + 1.5 > goals_away):
                asian_handicap_home_plus_15_data += 1
            elif(goals_home + 1.5 < goals_away):
                asian_handicap_away_plus_15_data += 1
            ## ---------------------------------------------
            if(goals_home + 2 > goals_away):
                asian_handicap_home_plus_2_data += 1
            elif(goals_home + 2 < goals_away):
                asian_handicap_away_plus_2_data += 1
            ## ---------------------------------------------
            if(goals_home + 2.5 > goals_away):
                asian_handicap_home_plus_25_data += 1
            elif(goals_home + 2.5 < goals_away):
                asian_handicap_away_plus_25_data += 1
            ## ---------------------------------------------
            if(goals_home + 3 > goals_away):
                asian_handicap_home_plus_3_data += 1
            elif(goals_home + 3 < goals_away):
                asian_handicap_away_plus_3_data += 1
            ## ---------------------------------------------
            if(goals_home + 3.5 > goals_away):
                asian_handicap_home_plus_35_data += 1
            elif(goals_home + 3.5 < goals_away):
                asian_handicap_away_plus_35_data += 1
            ## ---------------------------------------------
            if(goals_home + 4 > goals_away):
                asian_handicap_home_plus_4_data += 1
            elif(goals_home + 4 < goals_away):
                asian_handicap_away_plus_4_data += 1
            ## ---------------------------------------------
            if(goals_home + 4.5 > goals_away):
                asian_handicap_home_plus_45_data += 1
            elif(goals_home + 4.5 < goals_away):
                asian_handicap_away_plus_45_data += 1
            ## ---------------------------------------------
            if(goals_home + 5 > goals_away):
                asian_handicap_home_plus_5_data += 1
            elif(goals_home + 5 < goals_away):
                asian_handicap_away_plus_5_data += 1
            ## ---------------------------------------------
            if(goals_home + 5.5 > goals_away):
                asian_handicap_home_plus_55_data += 1
            elif(goals_home + 5.5 < goals_away):
                asian_handicap_away_plus_55_data += 1
            ## ---------------------------------------------
            if(goals_home + 6 > goals_away):
                asian_handicap_home_plus_6_data += 1
            elif(goals_home + 6 < goals_away):
                asian_handicap_away_plus_6_data += 1
            ## ---------------------------------------------
            if(goals_home + 6.5 > goals_away):
                asian_handicap_home_plus_65_data += 1
            elif(goals_home + 6.5 < goals_away):
                asian_handicap_away_plus_65_data += 1
            ## ---------------------------------------------
            if(goals_home - 0.5 > goals_away):
                asian_handicap_home_min_05_data += 1
            elif(goals_home - 0.5 < goals_away):
                asian_handicap_away_min_05_data += 1
            ## ---------------------------------------------
            if(goals_home - 1 > goals_away):
                asian_handicap_home_min_1_data += 1
            elif(goals_home - 1 < goals_away):
                asian_handicap_away_min_1_data += 1
            ## ---------------------------------------------
            if(goals_home - 1.5 > goals_away):
                asian_handicap_home_min_15_data += 1
            elif(goals_home - 1.5 < goals_away):
                asian_handicap_away_min_15_data += 1
            ## ---------------------------------------------
            if(goals_home - 2 > goals_away):
                asian_handicap_home_min_2_data += 1
            elif(goals_home - 2 < goals_away):
                asian_handicap_away_min_2_data += 1
            ## ---------------------------------------------
            if(goals_home - 2.5 > goals_away):
                asian_handicap_home_min_25_data += 1
            elif(goals_home - 2.5 < goals_away):
                asian_handicap_away_min_25_data += 1
            ## ---------------------------------------------
            if(goals_home - 3 > goals_away):
                asian_handicap_home_min_3_data += 1
            elif(goals_home - 3 < goals_away):
                asian_handicap_away_min_3_data += 1
            ## ---------------------------------------------
            if(goals_home - 3.5 > goals_away):
                asian_handicap_home_min_35_data += 1
            elif(goals_home - 3.5 < goals_away):
                asian_handicap_away_min_35_data += 1
            ## ---------------------------------------------
            if(goals_home - 4 > goals_away):
                asian_handicap_home_min_4_data += 1
            elif(goals_home - 4 < goals_away):
                asian_handicap_away_min_4_data += 1
            ## ---------------------------------------------
            if(goals_home - 4.5 > goals_away):
                asian_handicap_home_min_45_data += 1
            elif(goals_home - 4.5 < goals_away):
                asian_handicap_away_min_45_data += 1
            ## ---------------------------------------------
            if(goals_home - 5 > goals_away):
                asian_handicap_home_min_5_data += 1
            elif(goals_home - 5 < goals_away):
                asian_handicap_away_min_5_data += 1
            ## ---------------------------------------------
            if(goals_home - 5.5 > goals_away):
                asian_handicap_home_min_55_data += 1
            elif(goals_home - 5.5 < goals_away):
                asian_handicap_away_min_55_data += 1
            ## ---------------------------------------------
            if(goals_home - 6 > goals_away):
                asian_handicap_home_min_6_data += 1
            elif(goals_home - 6 < goals_away):
                asian_handicap_away_min_6_data += 1
            ## ---------------------------------------------
            if(goals_home - 6.5 > goals_away):
                asian_handicap_home_min_65_data += 1
            elif(goals_home - 6.5 < goals_away):
                asian_handicap_away_min_65_data += 1 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            ## --------------------------------------------- betid = 5 
            if(total_goals > 0):
                goals_overunder_over_05_data += 1
            elif(total_goals < 1):
                goals_overunder_under_05_data += 1
            ## ---------------------------------------------
            if(total_goals > 1):
                goals_overunder_over_15_data += 1
            elif(total_goals < 2):
                goals_overunder_under_15_data += 1
            ## ---------------------------------------------
            if(total_goals > 2):
                goals_overunder_over_25_data += 1
            elif(total_goals < 3):
                goals_overunder_under_25_data += 1
            ## ---------------------------------------------
            if(total_goals > 3):
                goals_overunder_over_35_data += 1
            elif(total_goals < 4):
                goals_overunder_under_35_data += 1
            ## ---------------------------------------------
            if(total_goals > 4):
                goals_overunder_over_45_data += 1
            elif(total_goals < 5):
                goals_overunder_under_45_data += 1
            ## ---------------------------------------------
            if(total_goals > 5):
                goals_overunder_over_55_data += 1
            elif(total_goals < 6):
                goals_overunder_under_55_data += 1 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- betid = 12
            if(goals_home >= goals_away):
                double_chance_home_draw_data += 1 
            elif(goals_home != goals_away):
                double_chance_home_away_data += 1
            elif(goals_home <= goals_away):
                double_chance_draw_away_data += 1 
            # -------------------------------------------------- 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- betid = 21
            if( (total_goals % 2) == 0):
                oddeven_even_data += 1
            else:
                oddeven_odd_data += 1
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- betid = 27
            if(goals_home == 0):
                clean_sheet__away_yes_data += 1 
            else:
                clean_sheet__away_no_data += 1 
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- betid = 28
            if(goals_away == 0):
                clean_sheet__home_yes_data += 1 
            else:
                clean_sheet__home_no_data += 1  
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # -------------------------------------------------- betid = 38 
            if(total_goals == 0):
                exact_goals_number_0_data += 1
            if(total_goals == 1):
                exact_goals_number_1_data += 1
            if(total_goals == 2):
                exact_goals_number_2_data += 1
            if(total_goals == 3):
                exact_goals_number_3_data += 1
            if(total_goals == 4):
                exact_goals_number_4_data += 1
            if(total_goals == 5):
                exact_goals_number_5_data += 1
            if(total_goals == 6):
                exact_goals_number_6_data += 1
            if(total_goals >= 7):
                exact_goals_number_more_7_data += 1 
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # -------------------------------------------------- betid = 40 
            if(goals_home == 0):
                home_team_exact_goals_number_0_data += 1
            if(goals_home == 1):
                home_team_exact_goals_number_1_data += 1
            if(goals_home == 2):
                home_team_exact_goals_number_2_data += 1
            if(goals_home >= 3):
                home_team_exact_goals_number_more_3_data += 1   
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # -------------------------------------------------- betid = 41 
            if(goals_away == 0):
                away_team_exact_goals_number_0_data += 1
            if(goals_away == 1):
                away_team_exact_goals_number_1_data += 1
            if(goals_away == 2):
                away_team_exact_goals_number_2_data += 1
            if(goals_away >= 3):
                away_team_exact_goals_number_more_3_data += 1    
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # -------------------------------------------------- betid = 36 
            if(goals_home > goals_away and goals_away == 0):
                win_to_nil_home_data += 1  
            if(goals_home < goals_away and goals_home == 0):
                win_to_nil_away_data += 1 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # -------------------------------------------------- betid = 25 
            if(goals_home > goals_away): 
                if(total_goals > 2):
                    result_total_goals_home_over_25_data += 1
                if(total_goals > 3):
                    result_total_goals_home_over_35_data += 1
                if(total_goals < 4): 
                    result_total_goals_home_under_35_data += 1
                if(total_goals < 3): 
                    result_total_goals_home_under_25_data += 1
            elif(goals_home == goals_away): 
                if(total_goals > 2):
                    result_total_goals_draw_over_25_data += 1
                if(total_goals > 3):
                    result_total_goals_draw_over_35_data += 1
                if(total_goals < 4): 
                    result_total_goals_draw_under_35_data += 1
                if(total_goals < 3): 
                    result_total_goals_draw_under_25_data += 1
            elif(goals_home < goals_away): 
                if(total_goals > 2):
                    result_total_goals_away_over_25_data += 1
                if(total_goals > 3):
                    result_total_goals_away_over_35_data += 1
                if(total_goals < 4): 
                    result_total_goals_away_under_35_data += 1
                if(total_goals < 3): 
                    result_total_goals_away_under_25_data += 1 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            ## --------------------------------------------- betid = 8
        if(btts_sts == 'yes'): 
            if(goals_home > goals_away):
                results_both_teams_score_home_yes_data += 1 
            elif(goals_home == goals_away):
                results_both_teams_score_draw_yes_data += 1
            elif(goals_home < goals_away):
                results_both_teams_score_away_yes_data += 1
        elif(btts_sts == 'no'): 
            if(goals_home > goals_away):
                results_both_teams_score_home_no_data += 1 
            elif(goals_home == goals_away):
                results_both_teams_score_draw_no_data += 1
            elif(goals_home < goals_away):
                results_both_teams_score_away_no_data += 1
        # ------------------------------------------------------
        ## --------------------------------------------- betid = 49
        if(btts_sts == 'yes'):
            if(total_goals > 2):
                total_goals_both_teams_to_score_over_yes_25_data += 1
            elif(total_goals < 3):
                total_goals_both_teams_to_score_under_yes_25_data += 1 
        elif(btts_sts == 'no'):
            if(total_goals > 2):
                total_goals_both_teams_to_score_over_no_25_data += 1
            elif(total_goals < 3):
                total_goals_both_teams_to_score_under_no_25_data += 1 
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        # ------------------------------------------------------  
        if(score_halftime_home is not None): 
            # -------------------------------------------------- 
            btts_first_sts  = 'no'
            btts_second_sts = 'no'
            total_goals_half    = score_halftime_home + score_halftime_away
            total_goals_second  = score_secondtime_home + score_secondtime_away  
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------  
            # -------------------------------------------------- betid = 13  
            if(score_halftime_home > score_halftime_away):
                first_half_winner_home_data += 1 

            elif(score_halftime_home == score_halftime_away):
                first_half_winner_draw_data += 1

            elif(score_halftime_home < score_halftime_away):
                first_half_winner_away_data += 1
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------  
            # -------------------------------------------------- betid = 3  
            if(score_secondtime_home > score_secondtime_away):
                second_half_winner_home_data += 1  

            elif(score_secondtime_home == score_secondtime_away):
                second_half_winner_draw_data += 1

            elif(score_secondtime_home < score_secondtime_away):
                second_half_winner_away_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 52 
            if(score_halftime_home > score_halftime_away): 
                if(btts_first_sts == 'yes'): 
                    halftime_result_both_teams_score_home_yes_data += 1
                elif(btts_first_sts == 'no'): 
                    halftime_result_both_teams_score_home_no_data += 1
            elif(score_halftime_home == score_halftime_away): 
                if(btts_first_sts == 'yes'): 
                    halftime_result_both_teams_score_draw_yes_data += 1
                elif(btts_first_sts == 'no'): 
                    halftime_result_both_teams_score_draw_no_data += 1
            elif(score_halftime_home < score_halftime_away): 
                if(btts_first_sts == 'yes'): 
                    halftime_result_both_teams_score_away_yes_data += 1
                elif(btts_first_sts == 'no'):  
                    halftime_result_both_teams_score_away_no_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            ## -------------------------------------------------- betid = 39
            if(score_halftime_home > score_halftime_away and 
                score_secondtime_home <= score_secondtime_away) :
                to_win_either_half_home_data += 1
            elif(score_halftime_home <= score_halftime_away and 
                    score_secondtime_home > score_secondtime_away) :
                to_win_either_half_home_data += 1
            elif(score_halftime_home < score_halftime_away and 
                    score_secondtime_home >= score_secondtime_away) :
                to_win_either_half_away_data += 1
            elif(score_halftime_home >= score_halftime_away and 
                    score_secondtime_home < score_secondtime_away) :
                to_win_either_half_away_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 32
            if(score_halftime_home > score_halftime_away and 
                score_secondtime_home > score_secondtime_away) :
                win_both_halves_home_data += 1
            if(score_halftime_home < score_halftime_away and 
                score_secondtime_home < score_secondtime_away) :
                win_both_halves_away_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 48
            if(score_halftime_home > 0 and score_secondtime_home > 0):
                to_score_in_both_halves_by_teams_home = 0
            if(score_halftime_away > 0 and score_secondtime_away > 0):
                to_score_in_both_halves_by_teams_away = 0 
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 11   
            if(total_goals_half > total_goals_second):
                highest_scoring_half_first_data += 1
            elif(total_goals_half == total_goals_second):
                highest_scoring_half_draw_data += 1
            elif(total_goals_half < total_goals_second):
                highest_scoring_half_second_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 7 
            if(score_halftime_home > score_halftime_away and 
                score_secondtime_home == score_secondtime_away):
                htft_double_home_draw_data += 1
            elif(score_halftime_home > score_halftime_away and 
                    score_secondtime_home < score_secondtime_away):
                htft_double_home_away_data += 1
            # -----------------------------------------
            elif(score_halftime_home == score_halftime_away and 
                    score_secondtime_home < score_secondtime_away):
                htft_double_draw_away_data += 1
            elif(score_halftime_home == score_halftime_away and 
                    score_secondtime_home == score_secondtime_away):
                htft_double_draw_draw_data += 1
            # -----------------------------------------
            elif(score_halftime_home > score_halftime_away and 
                    score_secondtime_home > score_secondtime_away):
                htft_double_home_home_data += 1
            elif(score_halftime_home == score_halftime_away and 
                    score_secondtime_home > score_secondtime_away):
                htft_double_draw_home_data += 1
            # -----------------------------------------
            elif(score_halftime_home < score_halftime_away and 
                    score_secondtime_home > score_secondtime_away):
                htft_double_away_home_data += 1
            elif(score_halftime_home < score_halftime_away and 
                    score_secondtime_home == score_secondtime_away):
                htft_double_away_draw_data += 1
            elif(score_halftime_home < score_halftime_away and 
                    score_secondtime_home < score_secondtime_away):
                htft_double_away_away_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 20 
            if(score_halftime_home >= score_halftime_away):
                double_chance__first_half_home_draw_data += 1 
            elif(score_halftime_home != score_halftime_away):
                double_chance__first_half_home_away_data += 1
            elif(score_halftime_home <= score_halftime_away):
                double_chance__first_half_draw_away_data += 1
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 46 
            if(total_goals_half == 0):
                exact_goals_number__first_half_0_data += 1
            elif(total_goals_half == 1):
                exact_goals_number__first_half_1_data += 1
            elif(total_goals_half == 2):
                exact_goals_number__first_half_2_data += 1
            elif(total_goals_half == 3):
                exact_goals_number__first_half_3_data += 1
            elif(total_goals_half == 4):
                exact_goals_number__first_half_4_data += 1
            elif(total_goals_half >= 5):
                exact_goals_number__first_half_more_5_data += 1  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 42
            if(total_goals_second == 0):
                second_half_exact_goals_number_0_data += 1
            elif(total_goals_second == 1):
                second_half_exact_goals_number_1_data += 1
            elif(total_goals_second == 2):
                second_half_exact_goals_number_2_data += 1
            elif(total_goals_second == 3):
                second_half_exact_goals_number_3_data += 1
            elif(total_goals_second == 4):
                second_half_exact_goals_number_4_data += 1
            elif(total_goals_second >= 5):
                second_half_exact_goals_number_more_5_data += 1  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 73
            if(btts_first_sts == 'yes' and btts_second_sts == 'yes'):
                both_teams_to_score_1st_half__2nd_half_yes_yes_data += 1
            elif(btts_first_sts == 'yes' and btts_second_sts == 'no'):
                both_teams_to_score_1st_half__2nd_half_yes_no_data += 1
            elif(btts_first_sts == 'no' and btts_second_sts == 'yes'):
                both_teams_to_score_1st_half__2nd_half_no_yes_data += 1
            elif(btts_first_sts == 'no' and btts_second_sts == 'no'):
                both_teams_to_score_1st_half__2nd_half_no_no_data += 1 
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 19
            if(score_halftime_home > score_halftime_away):
                asian_handicap_first_half_home_plus_0 = 0 
            if(score_halftime_home < score_halftime_away):
                asian_handicap_first_half_away_plus_0 = 0
            ## ----------------------------------------
            if(score_halftime_home + 0.5 > score_halftime_away):
                asian_handicap_first_half_home_plus_05 = 0
            if(score_halftime_home + 0.5 < score_halftime_away):
                asian_handicap_first_half_away_plus_05 = 0
            ## ----------------------------------------
            if(score_halftime_home + 1  > score_halftime_away):
                asian_handicap_first_half_home_plus_1 = 0
            if(score_halftime_home + 1  < score_halftime_away):
                asian_handicap_first_half_away_plus_1 = 0
            ## ----------------------------------------
            if(score_halftime_home + 1.5 > score_halftime_away):
                asian_handicap_first_half_home_plus_15 = 0
            if(score_halftime_home + 1.5 < score_halftime_away):
                asian_handicap_first_half_away_plus_15 = 0 
            ## ----------------------------------------
            if(score_halftime_home - 0.5 > score_halftime_away):
                asian_handicap_first_half_home_min_05 = 0
            if(score_halftime_home - 0.5 < score_halftime_away):
                asian_handicap_first_half_away_min_05 = 0
            ## ----------------------------------------
            if(score_halftime_home - 1 > score_halftime_away):
                asian_handicap_first_half_home_min_1 = 0
            if(score_halftime_home - 1 < score_halftime_away):
                asian_handicap_first_half_away_min_1 = 0
            ## ----------------------------------------
            if(score_halftime_home - 1.5 > score_halftime_away):
                asian_handicap_first_half_home_min_15 = 0
            if(score_halftime_home - 1.5 < score_halftime_away):
                asian_handicap_first_half_away_min_15 = 0
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------  
            # --------------------------------------------------   
            # -------------------------------------------------- betid = 6
            if(total_goals_half > 0):
                goals_overunder_first_half_over_05_data += 1
            if(total_goals_half < 1):
                goals_overunder_first_half_under_05_data += 1
            ## ----------------------------------------
            if(total_goals_half > 1):
                goals_overunder_first_half_over_15_data += 1
            if(total_goals_half < 2):
                goals_overunder_first_half_under_15_data += 1
            ## ----------------------------------------
            if(total_goals_half > 2):
                goals_overunder_first_half_over_25_data += 1
            if(total_goals_half < 3):
                goals_overunder_first_half_under_25_data += 1
            ## ----------------------------------------
            if(total_goals_half > 3):
                goals_overunder_first_half_over_35_data += 1
            if(total_goals_half < 4):
                goals_overunder_first_half_under_35_data += 1  
            # -------------------------------------------------- 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            # -------------------------------------------------- 
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        match_winner_home_perc = str(match_winner_home_data / total_rows * 100)
        if(float(match_winner_home_perc) >= 80  ):
            print(space + "match_winner_home_perc: " + str(match_winner_home_data) + " __ " + match_winner_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        match_winner_draw_perc = str(match_winner_draw_data / total_rows * 100)
        if(float(match_winner_draw_perc) >= 80  ):
            print(space + "match_winner_draw_perc: " + str(match_winner_draw_data) + " __ " + match_winner_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        match_winner_away_perc = str(match_winner_away_data / total_rows * 100)
        if(float(match_winner_away_perc) >= 80  ):
            print(space + "match_winner_away_perc: " + str(match_winner_away_data) + " __ " + match_winner_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        homeaway_home_perc = str(homeaway_home_data / total_rows * 100)
        if(float(homeaway_home_perc) >= 80  ):
            print(space + "homeaway_home_perc: " + str(homeaway_home_data) + " __ " + homeaway_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        homeaway_away_perc = str(homeaway_away_data / total_rows * 100)
        if(float(homeaway_away_perc) >= 80  ):
            print(space + "homeaway_away_perc: " + str(homeaway_away_data) + " __ " + homeaway_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_winner_home_perc = str(second_half_winner_home_data / total_rows * 100)
        if(float(second_half_winner_home_perc) >= 80  ):
            print(space + "second_half_winner_home_perc: " + str(second_half_winner_home_data) + " __ " + second_half_winner_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_winner_draw_perc = str(second_half_winner_draw_data / total_rows * 100)
        if(float(second_half_winner_draw_perc) >= 80  ):
            print(space + "second_half_winner_draw_perc: " + str(second_half_winner_draw_data) + " __ " + second_half_winner_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_winner_away_perc = str(second_half_winner_away_data / total_rows * 100)
        if(float(second_half_winner_away_perc) >= 80  ):
            print(space + "second_half_winner_away_perc: " + str(second_half_winner_away_data) + " __ " + second_half_winner_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_55_perc = str(asian_handicap_home_min_55_data / total_rows * 100)
        if(float(asian_handicap_home_min_55_perc) >= 80  ):
            print(space + "asian_handicap_home_min_55_perc: " + str(asian_handicap_home_min_55_data) + " __ " + asian_handicap_home_min_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_55_perc = str(asian_handicap_away_min_55_data / total_rows * 100)
        if(float(asian_handicap_away_min_55_perc) >= 80  ):
            print(space + "asian_handicap_away_min_55_perc: " + str(asian_handicap_away_min_55_data) + " __ " + asian_handicap_away_min_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_65_perc = str(asian_handicap_home_min_65_data / total_rows * 100)
        if(float(asian_handicap_home_min_65_perc) >= 80  ):
            print(space + "asian_handicap_home_min_65_perc: " + str(asian_handicap_home_min_65_data) + " __ " + asian_handicap_home_min_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_65_perc = str(asian_handicap_away_min_65_data / total_rows * 100)
        if(float(asian_handicap_away_min_65_perc) >= 80  ):
            print(space + "asian_handicap_away_min_65_perc: " + str(asian_handicap_away_min_65_data) + " __ " + asian_handicap_away_min_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_1_perc = str(asian_handicap_home_min_1_data / total_rows * 100)
        if(float(asian_handicap_home_min_1_perc) >= 80  ):
            print(space + "asian_handicap_home_min_1_perc: " + str(asian_handicap_home_min_1_data) + " __ " + asian_handicap_home_min_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_1_perc = str(asian_handicap_away_min_1_data / total_rows * 100)
        if(float(asian_handicap_away_min_1_perc) >= 80  ):
            print(space + "asian_handicap_away_min_1_perc: " + str(asian_handicap_away_min_1_data) + " __ " + asian_handicap_away_min_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_2_perc = str(asian_handicap_home_min_2_data / total_rows * 100)
        if(float(asian_handicap_home_min_2_perc) >= 80  ):
            print(space + "asian_handicap_home_min_2_perc: " + str(asian_handicap_home_min_2_data) + " __ " + asian_handicap_home_min_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_2_perc = str(asian_handicap_away_min_2_data / total_rows * 100)
        if(float(asian_handicap_away_min_2_perc) >= 80  ):
            print(space + "asian_handicap_away_min_2_perc: " + str(asian_handicap_away_min_2_data) + " __ " + asian_handicap_away_min_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_3_perc = str(asian_handicap_home_min_3_data / total_rows * 100)
        if(float(asian_handicap_home_min_3_perc) >= 80  ):
            print(space + "asian_handicap_home_min_3_perc: " + str(asian_handicap_home_min_3_data) + " __ " + asian_handicap_home_min_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_0_perc = str(asian_handicap_home_plus_0_data / total_rows * 100)
        if(float(asian_handicap_home_plus_0_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_0_perc: " + str(asian_handicap_home_plus_0_data) + " __ " + asian_handicap_home_plus_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_3_perc = str(asian_handicap_away_min_3_data / total_rows * 100)
        if(float(asian_handicap_away_min_3_perc) >= 80  ):
            print(space + "asian_handicap_away_min_3_perc: " + str(asian_handicap_away_min_3_data) + " __ " + asian_handicap_away_min_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_0_perc = str(asian_handicap_away_plus_0_data / total_rows * 100)
        if(float(asian_handicap_away_plus_0_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_0_perc: " + str(asian_handicap_away_plus_0_data) + " __ " + asian_handicap_away_plus_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_4_perc = str(asian_handicap_home_min_4_data / total_rows * 100)
        if(float(asian_handicap_home_min_4_perc) >= 80  ):
            print(space + "asian_handicap_home_min_4_perc: " + str(asian_handicap_home_min_4_data) + " __ " + asian_handicap_home_min_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_away_min_4_perc = str(asian_handicap_away_min_4_data / total_rows * 100)
        if(float(asian_handicap_away_min_4_perc) >= 80  ):
            print(space + "asian_handicap_away_min_4_perc: " + str(asian_handicap_away_min_4_data) + " __ " + asian_handicap_away_min_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_min_5_perc = str(asian_handicap_home_min_5_data / total_rows * 100)
        if(float(asian_handicap_home_min_5_perc) >= 80  ):
            print(space + "asian_handicap_home_min_5_perc: " + str(asian_handicap_home_min_5_data) + " __ " + asian_handicap_home_min_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_away_min_5_perc = str(asian_handicap_away_min_5_data / total_rows * 100)
        if(float(asian_handicap_away_min_5_perc) >= 80  ):
            print(space + "asian_handicap_away_min_5_perc: " + str(asian_handicap_away_min_5_data) + " __ " + asian_handicap_away_min_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_min_6_perc = str(asian_handicap_home_min_6_data / total_rows * 100)
        if(float(asian_handicap_home_min_6_perc) >= 80  ):
            print(space + "asian_handicap_home_min_6_perc: " + str(asian_handicap_home_min_6_data) + " __ " + asian_handicap_home_min_6_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_05_perc = str(asian_handicap_home_plus_05_data / total_rows * 100)
        if(float(asian_handicap_home_plus_05_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_05_perc: " + str(asian_handicap_home_plus_05_data) + " __ " + asian_handicap_home_plus_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_6_perc = str(asian_handicap_away_min_6_data / total_rows * 100)
        if(float(asian_handicap_away_min_6_perc) >= 80  ):
            print(space + "asian_handicap_away_min_6_perc: " + str(asian_handicap_away_min_6_data) + " __ " + asian_handicap_away_min_6_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_05_perc = str(asian_handicap_away_plus_05_data / total_rows * 100)
        if(float(asian_handicap_away_plus_05_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_05_perc: " + str(asian_handicap_away_plus_05_data) + " __ " + asian_handicap_away_plus_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_05_perc = str(asian_handicap_home_min_05_data / total_rows * 100)
        if(float(asian_handicap_home_min_05_perc) >= 80  ):
            print(space + "asian_handicap_home_min_05_perc: " + str(asian_handicap_home_min_05_data) + " __ " + asian_handicap_home_min_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_away_min_05_perc = str(asian_handicap_away_min_05_data / total_rows * 100)
        if(float(asian_handicap_away_min_05_perc) >= 80  ):
            print(space + "asian_handicap_away_min_05_perc: " + str(asian_handicap_away_min_05_data) + " __ " + asian_handicap_away_min_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_plus_2_perc = str(asian_handicap_home_plus_2_data / total_rows * 100)
        if(float(asian_handicap_home_plus_2_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_2_perc: " + str(asian_handicap_home_plus_2_data) + " __ " + asian_handicap_home_plus_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_1_perc = str(asian_handicap_home_plus_1_data / total_rows * 100)
        if(float(asian_handicap_home_plus_1_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_1_perc: " + str(asian_handicap_home_plus_1_data) + " __ " + asian_handicap_home_plus_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_2_perc = str(asian_handicap_away_plus_2_data / total_rows * 100)
        if(float(asian_handicap_away_plus_2_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_2_perc: " + str(asian_handicap_away_plus_2_data) + " __ " + asian_handicap_away_plus_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_1_perc = str(asian_handicap_away_plus_1_data / total_rows * 100)
        if(float(asian_handicap_away_plus_1_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_1_perc: " + str(asian_handicap_away_plus_1_data) + " __ " + asian_handicap_away_plus_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_25_perc = str(asian_handicap_home_plus_25_data / total_rows * 100)
        if(float(asian_handicap_home_plus_25_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_25_perc: " + str(asian_handicap_home_plus_25_data) + " __ " + asian_handicap_home_plus_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_15_perc = str(asian_handicap_home_plus_15_data / total_rows * 100)
        if(float(asian_handicap_home_plus_15_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_15_perc: " + str(asian_handicap_home_plus_15_data) + " __ " + asian_handicap_home_plus_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_25_perc = str(asian_handicap_away_plus_25_data / total_rows * 100)
        if(float(asian_handicap_away_plus_25_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_25_perc: " + str(asian_handicap_away_plus_25_data) + " __ " + asian_handicap_away_plus_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_15_perc = str(asian_handicap_away_plus_15_data / total_rows * 100)
        if(float(asian_handicap_away_plus_15_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_15_perc: " + str(asian_handicap_away_plus_15_data) + " __ " + asian_handicap_away_plus_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------  
        asian_handicap_away_plus_35_perc = str(asian_handicap_away_plus_35_data / total_rows * 100)
        if(float(asian_handicap_away_plus_35_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_35_perc: " + str(asian_handicap_away_plus_35_data) + " __ " + asian_handicap_away_plus_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_35_perc = str(asian_handicap_home_plus_35_data / total_rows * 100)
        if(float(asian_handicap_home_plus_35_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_35_perc: " + str(asian_handicap_home_plus_35_data) + " __ " + asian_handicap_home_plus_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_3_perc = str(asian_handicap_away_plus_3_data / total_rows * 100)
        if(float(asian_handicap_away_plus_3_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_3_perc: " + str(asian_handicap_away_plus_3_data) + " __ " + asian_handicap_away_plus_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_3_perc = str(asian_handicap_home_plus_3_data / total_rows * 100)
        if(float(asian_handicap_home_plus_3_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_3_perc: " + str(asian_handicap_home_plus_3_data) + " __ " + asian_handicap_home_plus_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_4_perc = str(asian_handicap_home_plus_4_data / total_rows * 100)
        if(float(asian_handicap_home_plus_4_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_4_perc: " + str(asian_handicap_home_plus_4_data) + " __ " + asian_handicap_home_plus_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_4_perc = str(asian_handicap_away_plus_4_data / total_rows * 100)
        if(float(asian_handicap_away_plus_4_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_4_perc: " + str(asian_handicap_away_plus_4_data) + " __ " + asian_handicap_away_plus_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_45_perc = str(asian_handicap_home_plus_45_data / total_rows * 100)
        if(float(asian_handicap_home_plus_45_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_45_perc: " + str(asian_handicap_home_plus_45_data) + " __ " + asian_handicap_home_plus_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_45_perc = str(asian_handicap_away_plus_45_data / total_rows * 100)
        if(float(asian_handicap_away_plus_45_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_45_perc: " + str(asian_handicap_away_plus_45_data) + " __ " + asian_handicap_away_plus_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_plus_5_perc = str(asian_handicap_home_plus_5_data / total_rows * 100)
        if(float(asian_handicap_home_plus_5_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_5_perc: " + str(asian_handicap_home_plus_5_data) + " __ " + asian_handicap_home_plus_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_5_perc = str(asian_handicap_away_plus_5_data / total_rows * 100)
        if(float(asian_handicap_away_plus_5_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_5_perc: " + str(asian_handicap_away_plus_5_data) + " __ " + asian_handicap_away_plus_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_55_perc = str(asian_handicap_home_plus_55_data / total_rows * 100)
        if(float(asian_handicap_home_plus_55_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_55_perc: " + str(asian_handicap_home_plus_55_data) + " __ " + asian_handicap_home_plus_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_55_perc = str(asian_handicap_away_plus_55_data / total_rows * 100)
        if(float(asian_handicap_away_plus_55_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_55_perc: " + str(asian_handicap_away_plus_55_data) + " __ " + asian_handicap_away_plus_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_plus_6_perc = str(asian_handicap_home_plus_6_data / total_rows * 100)
        if(float(asian_handicap_home_plus_6_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_6_perc: " + str(asian_handicap_home_plus_6_data) + " __ " + asian_handicap_home_plus_6_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_6_perc = str(asian_handicap_away_plus_6_data / total_rows * 100)
        if(float(asian_handicap_away_plus_6_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_6_perc: " + str(asian_handicap_away_plus_6_data) + " __ " + asian_handicap_away_plus_6_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_plus_65_perc = str(asian_handicap_home_plus_65_data / total_rows * 100)
        if(float(asian_handicap_home_plus_65_perc) >= 80  ):
            print(space + "asian_handicap_home_plus_65_perc: " + str(asian_handicap_home_plus_65_data) + " __ " + asian_handicap_home_plus_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_plus_65_perc = str(asian_handicap_away_plus_65_data / total_rows * 100)
        if(float(asian_handicap_away_plus_65_perc) >= 80  ):
            print(space + "asian_handicap_away_plus_65_perc: " + str(asian_handicap_away_plus_65_data) + " __ " + asian_handicap_away_plus_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_home_min_15_perc = str(asian_handicap_home_min_15_data / total_rows * 100)
        if(float(asian_handicap_home_min_15_perc) >= 80  ):
            print(space + "asian_handicap_home_min_15_perc: " + str(asian_handicap_home_min_15_data) + " __ " + asian_handicap_home_min_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_15_perc = str(asian_handicap_away_min_15_data / total_rows * 100)
        if(float(asian_handicap_away_min_15_perc) >= 80  ):
            print(space + "asian_handicap_away_min_15_perc: " + str(asian_handicap_away_min_15_data) + " __ " + asian_handicap_away_min_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_25_perc = str(asian_handicap_home_min_25_data / total_rows * 100)
        if(float(asian_handicap_home_min_25_perc) >= 80  ):
            print(space + "asian_handicap_home_min_25_perc: " + str(asian_handicap_home_min_25_data) + " __ " + asian_handicap_home_min_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_25_perc = str(asian_handicap_away_min_25_data / total_rows * 100)
        if(float(asian_handicap_away_min_25_perc) >= 80  ):
            print(space + "asian_handicap_away_min_25_perc: " + str(asian_handicap_away_min_25_data) + " __ " + asian_handicap_away_min_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_35_perc = str(asian_handicap_home_min_35_data / total_rows * 100)
        if(float(asian_handicap_home_min_35_perc) >= 80  ):
            print(space + "asian_handicap_home_min_35_perc: " + str(asian_handicap_home_min_35_data) + " __ " + asian_handicap_home_min_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_35_perc = str(asian_handicap_away_min_35_data / total_rows * 100)
        if(float(asian_handicap_away_min_35_perc) >= 80  ):
            print(space + "asian_handicap_away_min_35_perc: " + str(asian_handicap_away_min_35_data) + " __ " + asian_handicap_away_min_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_home_min_45_perc = str(asian_handicap_home_min_45_data / total_rows * 100)
        if(float(asian_handicap_home_min_45_perc) >= 80  ):
            print(space + "asian_handicap_home_min_45_perc: " + str(asian_handicap_home_min_45_data) + " __ " + asian_handicap_home_min_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_away_min_45_perc = str(asian_handicap_away_min_45_data / total_rows * 100)
        if(float(asian_handicap_away_min_45_perc) >= 80  ):
            print(space + "asian_handicap_away_min_45_perc: " + str(asian_handicap_away_min_45_data) + " __ " + asian_handicap_away_min_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_35_perc = str(goals_overunder_over_35_data / total_rows * 100)
        if(float(goals_overunder_over_35_perc) >= 80  ):
            print(space + "goals_overunder_over_35_perc: " + str(goals_overunder_over_35_data) + " __ " + goals_overunder_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_35_perc = str(goals_overunder_under_35_data / total_rows * 100)
        if(float(goals_overunder_under_35_perc) >= 80  ):
            print(space + "goals_overunder_under_35_perc: " + str(goals_overunder_under_35_data) + " __ " + goals_overunder_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_15_perc = str(goals_overunder_over_15_data / total_rows * 100)
        if(float(goals_overunder_over_15_perc) >= 80  ):
            print(space + "goals_overunder_over_15_perc: " + str(goals_overunder_over_15_data) + " __ " + goals_overunder_over_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_15_perc = str(goals_overunder_under_15_data / total_rows * 100)
        if(float(goals_overunder_under_15_perc) >= 80  ):
            print(space + "goals_overunder_under_15_perc: " + str(goals_overunder_under_15_data) + " __ " + goals_overunder_under_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_45_perc = str(goals_overunder_over_45_data / total_rows * 100)
        if(float(goals_overunder_over_45_perc) >= 80  ):
            print(space + "goals_overunder_over_45_perc: " + str(goals_overunder_over_45_data) + " __ " + goals_overunder_over_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_45_perc = str(goals_overunder_under_45_data / total_rows * 100)
        if(float(goals_overunder_under_45_perc) >= 80  ):
            print(space + "goals_overunder_under_45_perc: " + str(goals_overunder_under_45_data) + " __ " + goals_overunder_under_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_25_perc = str(goals_overunder_over_25_data / total_rows * 100)
        if(float(goals_overunder_over_25_perc) >= 80  ):
            print(space + "goals_overunder_over_25_perc: " + str(goals_overunder_over_25_data) + " __ " + goals_overunder_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_25_perc = str(goals_overunder_under_25_data / total_rows * 100)
        if(float(goals_overunder_under_25_perc) >= 80  ):
            print(space + "goals_overunder_under_25_perc: " + str(goals_overunder_under_25_data) + " __ " + goals_overunder_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_05_perc = str(goals_overunder_over_05_data / total_rows * 100)
        if(float(goals_overunder_over_05_perc) >= 80  ):
            print(space + "goals_overunder_over_05_perc: " + str(goals_overunder_over_05_data) + " __ " + goals_overunder_over_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_05_perc = str(goals_overunder_under_05_data / total_rows * 100)
        if(float(goals_overunder_under_05_perc) >= 80  ):
            print(space + "goals_overunder_under_05_perc: " + str(goals_overunder_under_05_data) + " __ " + goals_overunder_under_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_55_perc = str(goals_overunder_over_55_data / total_rows * 100)
        if(float(goals_overunder_over_55_perc) >= 80  ):
            print(space + "goals_overunder_over_55_perc: " + str(goals_overunder_over_55_data) + " __ " + goals_overunder_over_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_55_perc = str(goals_overunder_under_55_data / total_rows * 100)
        if(float(goals_overunder_under_55_perc) >= 80  ):
            print(space + "goals_overunder_under_55_perc: " + str(goals_overunder_under_55_data) + " __ " + goals_overunder_under_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_over_65_perc = str(goals_overunder_over_65_data / total_rows * 100)
        if(float(goals_overunder_over_65_perc) >= 80  ):
            print(space + "goals_overunder_over_65_perc: " + str(goals_overunder_over_65_data) + " __ " + goals_overunder_over_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_65_perc = str(goals_overunder_under_65_data / total_rows * 100)
        if(float(goals_overunder_under_65_perc) >= 80  ):
            print(space + "goals_overunder_under_65_perc: " + str(goals_overunder_under_65_data) + " __ " + goals_overunder_under_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_75_perc = str(goals_overunder_over_75_data / total_rows * 100)
        if(float(goals_overunder_over_75_perc) >= 80  ):
            print(space + "goals_overunder_over_75_perc: " + str(goals_overunder_over_75_data) + " __ " + goals_overunder_over_75_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_75_perc = str(goals_overunder_under_75_data / total_rows * 100)
        if(float(goals_overunder_under_75_perc) >= 80  ):
            print(space + "goals_overunder_under_75_perc: " + str(goals_overunder_under_75_data) + " __ " + goals_overunder_under_75_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_over_85_perc = str(goals_overunder_over_85_data / total_rows * 100)
        if(float(goals_overunder_over_85_perc) >= 80  ):
            print(space + "goals_overunder_over_85_perc: " + str(goals_overunder_over_85_data) + " __ " + goals_overunder_over_85_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_85_perc = str(goals_overunder_under_85_data / total_rows * 100)
        if(float(goals_overunder_under_85_perc) >= 80  ):
            print(space + "goals_overunder_under_85_perc: " + str(goals_overunder_under_85_data) + " __ " + goals_overunder_under_85_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_30_perc = str(goals_overunder_over_30_data / total_rows * 100)
        if(float(goals_overunder_over_30_perc) >= 80  ):
            print(space + "goals_overunder_over_30_perc: " + str(goals_overunder_over_30_data) + " __ " + goals_overunder_over_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_30_perc = str(goals_overunder_under_30_data / total_rows * 100)
        if(float(goals_overunder_under_30_perc) >= 80  ):
            print(space + "goals_overunder_under_30_perc: " + str(goals_overunder_under_30_data) + " __ " + goals_overunder_under_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_20_perc = str(goals_overunder_over_20_data / total_rows * 100)
        if(float(goals_overunder_over_20_perc) >= 80  ):
            print(space + "goals_overunder_over_20_perc: " + str(goals_overunder_over_20_data) + " __ " + goals_overunder_over_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_20_perc = str(goals_overunder_under_20_data / total_rows * 100)
        if(float(goals_overunder_under_20_perc) >= 80  ):
            print(space + "goals_overunder_under_20_perc: " + str(goals_overunder_under_20_data) + " __ " + goals_overunder_under_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_40_perc = str(goals_overunder_over_40_data / total_rows * 100)
        if(float(goals_overunder_over_40_perc) >= 80  ):
            print(space + "goals_overunder_over_40_perc: " + str(goals_overunder_over_40_data) + " __ " + goals_overunder_over_40_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_40_perc = str(goals_overunder_under_40_data / total_rows * 100)
        if(float(goals_overunder_under_40_perc) >= 80  ):
            print(space + "goals_overunder_under_40_perc: " + str(goals_overunder_under_40_data) + " __ " + goals_overunder_under_40_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_50_perc = str(goals_overunder_over_50_data / total_rows * 100)
        if(float(goals_overunder_over_50_perc) >= 80  ):
            print(space + "goals_overunder_over_50_perc: " + str(goals_overunder_over_50_data) + " __ " + goals_overunder_over_50_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_50_perc = str(goals_overunder_under_50_data / total_rows * 100)
        if(float(goals_overunder_under_50_perc) >= 80  ):
            print(space + "goals_overunder_under_50_perc: " + str(goals_overunder_under_50_data) + " __ " + goals_overunder_under_50_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_over_10_perc = str(goals_overunder_over_10_data / total_rows * 100)
        if(float(goals_overunder_over_10_perc) >= 80  ):
            print(space + "goals_overunder_over_10_perc: " + str(goals_overunder_over_10_data) + " __ " + goals_overunder_over_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_10_perc = str(goals_overunder_under_10_data / total_rows * 100)
        if(float(goals_overunder_under_10_perc) >= 80  ):
            print(space + "goals_overunder_under_10_perc: " + str(goals_overunder_under_10_data) + " __ " + goals_overunder_under_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_over_60_perc = str(goals_overunder_over_60_data / total_rows * 100)
        if(float(goals_overunder_over_60_perc) >= 80  ):
            print(space + "goals_overunder_over_60_perc: " + str(goals_overunder_over_60_data) + " __ " + goals_overunder_over_60_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_60_perc = str(goals_overunder_under_60_data / total_rows * 100)
        if(float(goals_overunder_under_60_perc) >= 80  ):
            print(space + "goals_overunder_under_60_perc: " + str(goals_overunder_under_60_data) + " __ " + goals_overunder_under_60_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_over_70_perc = str(goals_overunder_over_70_data / total_rows * 100)
        if(float(goals_overunder_over_70_perc) >= 80  ):
            print(space + "goals_overunder_over_70_perc: " + str(goals_overunder_over_70_data) + " __ " + goals_overunder_over_70_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_70_perc = str(goals_overunder_under_70_data / total_rows * 100)
        if(float(goals_overunder_under_70_perc) >= 80  ):
            print(space + "goals_overunder_under_70_perc: " + str(goals_overunder_under_70_data) + " __ " + goals_overunder_under_70_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_over_95_perc = str(goals_overunder_over_95_data / total_rows * 100)
        if(float(goals_overunder_over_95_perc) >= 80  ):
            print(space + "goals_overunder_over_95_perc: " + str(goals_overunder_over_95_data) + " __ " + goals_overunder_over_95_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_under_95_perc = str(goals_overunder_under_95_data / total_rows * 100)
        if(float(goals_overunder_under_95_perc) >= 80  ):
            print(space + "goals_overunder_under_95_perc: " + str(goals_overunder_under_95_data) + " __ " + goals_overunder_under_95_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_over_30_perc = str(goals_overunder_first_half_over_30_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_30_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_30_perc: " + str(goals_overunder_first_half_over_30_data) + " __ " + goals_overunder_first_half_over_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_first_half_under_30_perc = str(goals_overunder_first_half_under_30_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_30_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_30_perc: " + str(goals_overunder_first_half_under_30_data) + " __ " + goals_overunder_first_half_under_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_first_half_over_35_perc = str(goals_overunder_first_half_over_35_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_35_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_35_perc: " + str(goals_overunder_first_half_over_35_data) + " __ " + goals_overunder_first_half_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_35_perc = str(goals_overunder_first_half_under_35_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_35_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_35_perc: " + str(goals_overunder_first_half_under_35_data) + " __ " + goals_overunder_first_half_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_over_15_perc = str(goals_overunder_first_half_over_15_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_15_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_15_perc: " + str(goals_overunder_first_half_over_15_data) + " __ " + goals_overunder_first_half_over_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_15_perc = str(goals_overunder_first_half_under_15_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_15_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_15_perc: " + str(goals_overunder_first_half_under_15_data) + " __ " + goals_overunder_first_half_under_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_over_25_perc = str(goals_overunder_first_half_over_25_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_25_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_25_perc: " + str(goals_overunder_first_half_over_25_data) + " __ " + goals_overunder_first_half_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_25_perc = str(goals_overunder_first_half_under_25_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_25_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_25_perc: " + str(goals_overunder_first_half_under_25_data) + " __ " + goals_overunder_first_half_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_over_05_perc = str(goals_overunder_first_half_over_05_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_05_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_05_perc: " + str(goals_overunder_first_half_over_05_data) + " __ " + goals_overunder_first_half_over_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_05_perc = str(goals_overunder_first_half_under_05_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_05_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_05_perc: " + str(goals_overunder_first_half_under_05_data) + " __ " + goals_overunder_first_half_under_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder_first_half_over_20_perc = str(goals_overunder_first_half_over_20_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_20_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_20_perc: " + str(goals_overunder_first_half_over_20_data) + " __ " + goals_overunder_first_half_over_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_20_perc = str(goals_overunder_first_half_under_20_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_20_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_20_perc: " + str(goals_overunder_first_half_under_20_data) + " __ " + goals_overunder_first_half_under_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_over_10_perc = str(goals_overunder_first_half_over_10_data / total_rows * 100)
        if(float(goals_overunder_first_half_over_10_perc) >= 80  ):
            print(space + "goals_overunder_first_half_over_10_perc: " + str(goals_overunder_first_half_over_10_data) + " __ " + goals_overunder_first_half_over_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder_first_half_under_10_perc = str(goals_overunder_first_half_under_10_data / total_rows * 100)
        if(float(goals_overunder_first_half_under_10_perc) >= 80  ):
            print(space + "goals_overunder_first_half_under_10_perc: " + str(goals_overunder_first_half_under_10_data) + " __ " + goals_overunder_first_half_under_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_home_draw_perc = str(htft_double_home_draw_data / total_rows * 100)
        if(float(htft_double_home_draw_perc) >= 80  ):
            print(space + "htft_double_home_draw_perc: " + str(htft_double_home_draw_data) + " __ " + htft_double_home_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_home_away_perc = str(htft_double_home_away_data / total_rows * 100)
        if(float(htft_double_home_away_perc) >= 80  ):
            print(space + "htft_double_home_away_perc: " + str(htft_double_home_away_data) + " __ " + htft_double_home_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_draw_away_perc = str(htft_double_draw_away_data / total_rows * 100)
        if(float(htft_double_draw_away_perc) >= 80  ):
            print(space + "htft_double_draw_away_perc: " + str(htft_double_draw_away_data) + " __ " + htft_double_draw_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_draw_draw_perc = str(htft_double_draw_draw_data / total_rows * 100)
        if(float(htft_double_draw_draw_perc) >= 80  ):
            print(space + "htft_double_draw_draw_perc: " + str(htft_double_draw_draw_data) + " __ " + htft_double_draw_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_home_home_perc = str(htft_double_home_home_data / total_rows * 100)
        if(float(htft_double_home_home_perc) >= 80  ):
            print(space + "htft_double_home_home_perc: " + str(htft_double_home_home_data) + " __ " + htft_double_home_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_draw_home_perc = str(htft_double_draw_home_data / total_rows * 100)
        if(float(htft_double_draw_home_perc) >= 80  ):
            print(space + "htft_double_draw_home_perc: " + str(htft_double_draw_home_data) + " __ " + htft_double_draw_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_away_home_perc = str(htft_double_away_home_data / total_rows * 100)
        if(float(htft_double_away_home_perc) >= 80  ):
            print(space + "htft_double_away_home_perc: " + str(htft_double_away_home_data) + " __ " + htft_double_away_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_away_draw_perc = str(htft_double_away_draw_data / total_rows * 100)
        if(float(htft_double_away_draw_perc) >= 80  ):
            print(space + "htft_double_away_draw_perc: " + str(htft_double_away_draw_data) + " __ " + htft_double_away_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        htft_double_away_away_perc = str(htft_double_away_away_data / total_rows * 100)
        if(float(htft_double_away_away_perc) >= 80  ):
            print(space + "htft_double_away_away_perc: " + str(htft_double_away_away_data) + " __ " + htft_double_away_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_score_yes_perc = str(both_teams_score_yes_data / total_rows * 100)
        if(float(both_teams_score_yes_perc) >= 80  ):
            print(space + "both_teams_score_yes_perc: " + str(both_teams_score_yes_data) + " __ " + both_teams_score_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_score_no_perc = str(both_teams_score_no_data / total_rows * 100)
        if(float(both_teams_score_no_perc) >= 80  ):
            print(space + "both_teams_score_no_perc: " + str(both_teams_score_no_data) + " __ " + both_teams_score_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        highest_scoring_half_draw_perc = str(highest_scoring_half_draw_data / total_rows * 100)
        if(float(highest_scoring_half_draw_perc) >= 80  ):
            print(space + "highest_scoring_half_draw_perc: " + str(highest_scoring_half_draw_data) + " __ " + highest_scoring_half_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        highest_scoring_half_first_perc = str(highest_scoring_half_first_data / total_rows * 100)
        if(float(highest_scoring_half_first_perc) >= 80  ):
            print(space + "highest_scoring_half_first_perc: " + str(highest_scoring_half_first_data) + " __ " + highest_scoring_half_first_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        highest_scoring_half_second_perc = str(highest_scoring_half_second_data / total_rows * 100)
        if(float(highest_scoring_half_second_perc) >= 80  ):
            print(space + "highest_scoring_half_second_perc: " + str(highest_scoring_half_second_data) + " __ " + highest_scoring_half_second_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        double_chance_home_draw_perc = str(double_chance_home_draw_data / total_rows * 100)
        if(float(double_chance_home_draw_perc) >= 80  ):
            print(space + "double_chance_home_draw_perc: " + str(double_chance_home_draw_data) + " __ " + double_chance_home_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        double_chance_home_away_perc = str(double_chance_home_away_data / total_rows * 100)
        if(float(double_chance_home_away_perc) >= 80  ):
            print(space + "double_chance_home_away_perc: " + str(double_chance_home_away_data) + " __ " + double_chance_home_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        double_chance_draw_away_perc = str(double_chance_draw_away_data / total_rows * 100)
        if(float(double_chance_draw_away_perc) >= 80  ):
            print(space + "double_chance_draw_away_perc: " + str(double_chance_draw_away_data) + " __ " + double_chance_draw_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        first_half_winner_home_perc = str(first_half_winner_home_data / total_rows * 100)
        if(float(first_half_winner_home_perc) >= 80  ):
            print(space + "first_half_winner_home_perc: " + str(first_half_winner_home_data) + " __ " + first_half_winner_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        first_half_winner_draw_perc = str(first_half_winner_draw_data / total_rows * 100)
        if(float(first_half_winner_draw_perc) >= 80  ):
            print(space + "first_half_winner_draw_perc: " + str(first_half_winner_draw_data) + " __ " + first_half_winner_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        first_half_winner_away_perc = str(first_half_winner_away_data / total_rows * 100)
        if(float(first_half_winner_away_perc) >= 80  ):
            print(space + "first_half_winner_away_perc: " + str(first_half_winner_away_data) + " __ " + first_half_winner_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        total_home_over_35_perc = str(total_home_over_35_data / total_rows * 100)
        if(float(total_home_over_35_perc) >= 80  ):
            print(space + "total_home_over_35_perc: " + str(total_home_over_35_data) + " __ " + total_home_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_35_perc = str(total_home_under_35_data / total_rows * 100)
        if(float(total_home_under_35_perc) >= 80  ):
            print(space + "total_home_under_35_perc: " + str(total_home_under_35_data) + " __ " + total_home_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_over_15_perc = str(total_home_over_15_data / total_rows * 100)
        if(float(total_home_over_15_perc) >= 80  ):
            print(space + "total_home_over_15_perc: " + str(total_home_over_15_data) + " __ " + total_home_over_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_15_perc = str(total_home_under_15_data / total_rows * 100)
        if(float(total_home_under_15_perc) >= 80  ):
            print(space + "total_home_under_15_perc: " + str(total_home_under_15_data) + " __ " + total_home_under_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_over_25_perc = str(total_home_over_25_data / total_rows * 100)
        if(float(total_home_over_25_perc) >= 80  ):
            print(space + "total_home_over_25_perc: " + str(total_home_over_25_data) + " __ " + total_home_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_25_perc = str(total_home_under_25_data / total_rows * 100)
        if(float(total_home_under_25_perc) >= 80  ):
            print(space + "total_home_under_25_perc: " + str(total_home_under_25_data) + " __ " + total_home_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_over_45_perc = str(total_home_over_45_data / total_rows * 100)
        if(float(total_home_over_45_perc) >= 80  ):
            print(space + "total_home_over_45_perc: " + str(total_home_over_45_data) + " __ " + total_home_over_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_45_perc = str(total_home_under_45_data / total_rows * 100)
        if(float(total_home_under_45_perc) >= 80  ):
            print(space + "total_home_under_45_perc: " + str(total_home_under_45_data) + " __ " + total_home_under_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_over_55_perc = str(total_home_over_55_data / total_rows * 100)
        if(float(total_home_over_55_perc) >= 80  ):
            print(space + "total_home_over_55_perc: " + str(total_home_over_55_data) + " __ " + total_home_over_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_55_perc = str(total_home_under_55_data / total_rows * 100)
        if(float(total_home_under_55_perc) >= 80  ):
            print(space + "total_home_under_55_perc: " + str(total_home_under_55_data) + " __ " + total_home_under_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_over_65_perc = str(total_home_over_65_data / total_rows * 100)
        if(float(total_home_over_65_perc) >= 80  ):
            print(space + "total_home_over_65_perc: " + str(total_home_over_65_data) + " __ " + total_home_over_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_home_under_65_perc = str(total_home_under_65_data / total_rows * 100)
        if(float(total_home_under_65_perc) >= 80  ):
            print(space + "total_home_under_65_perc: " + str(total_home_under_65_data) + " __ " + total_home_under_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_35_perc = str(total_away_over_35_data / total_rows * 100)
        if(float(total_away_over_35_perc) >= 80  ):
            print(space + "total_away_over_35_perc: " + str(total_away_over_35_data) + " __ " + total_away_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_35_perc = str(total_away_under_35_data / total_rows * 100)
        if(float(total_away_under_35_perc) >= 80  ):
            print(space + "total_away_under_35_perc: " + str(total_away_under_35_data) + " __ " + total_away_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_15_perc = str(total_away_over_15_data / total_rows * 100)
        if(float(total_away_over_15_perc) >= 80  ):
            print(space + "total_away_over_15_perc: " + str(total_away_over_15_data) + " __ " + total_away_over_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_15_perc = str(total_away_under_15_data / total_rows * 100)
        if(float(total_away_under_15_perc) >= 80  ):
            print(space + "total_away_under_15_perc: " + str(total_away_under_15_data) + " __ " + total_away_under_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_45_perc = str(total_away_over_45_data / total_rows * 100)
        if(float(total_away_over_45_perc) >= 80  ):
            print(space + "total_away_over_45_perc: " + str(total_away_over_45_data) + " __ " + total_away_over_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_45_perc = str(total_away_under_45_data / total_rows * 100)
        if(float(total_away_under_45_perc) >= 80  ):
            print(space + "total_away_under_45_perc: " + str(total_away_under_45_data) + " __ " + total_away_under_45_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_25_perc = str(total_away_over_25_data / total_rows * 100)
        if(float(total_away_over_25_perc) >= 80  ):
            print(space + "total_away_over_25_perc: " + str(total_away_over_25_data) + " __ " + total_away_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_25_perc = str(total_away_under_25_data / total_rows * 100)
        if(float(total_away_under_25_perc) >= 80  ):
            print(space + "total_away_under_25_perc: " + str(total_away_under_25_data) + " __ " + total_away_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_55_perc = str(total_away_over_55_data / total_rows * 100)
        if(float(total_away_over_55_perc) >= 80  ):
            print(space + "total_away_over_55_perc: " + str(total_away_over_55_data) + " __ " + total_away_over_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_55_perc = str(total_away_under_55_data / total_rows * 100)
        if(float(total_away_under_55_perc) >= 80  ):
            print(space + "total_away_under_55_perc: " + str(total_away_under_55_data) + " __ " + total_away_under_55_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_over_65_perc = str(total_away_over_65_data / total_rows * 100)
        if(float(total_away_over_65_perc) >= 80  ):
            print(space + "total_away_over_65_perc: " + str(total_away_over_65_data) + " __ " + total_away_over_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_away_under_65_perc = str(total_away_under_65_data / total_rows * 100)
        if(float(total_away_under_65_perc) >= 80  ):
            print(space + "total_away_under_65_perc: " + str(total_away_under_65_data) + " __ " + total_away_under_65_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_home_plus_0_perc = str(asian_handicap_first_half_home_plus_0_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_plus_0_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_plus_0_perc: " + str(asian_handicap_first_half_home_plus_0_data) + " __ " + asian_handicap_first_half_home_plus_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_plus_0_perc = str(asian_handicap_first_half_away_plus_0_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_plus_0_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_plus_0_perc: " + str(asian_handicap_first_half_away_plus_0_data) + " __ " + asian_handicap_first_half_away_plus_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_first_half_home_min_05_perc = str(asian_handicap_first_half_home_min_05_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_min_05_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_min_05_perc: " + str(asian_handicap_first_half_home_min_05_data) + " __ " + asian_handicap_first_half_home_min_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_min_05_perc = str(asian_handicap_first_half_away_min_05_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_min_05_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_min_05_perc: " + str(asian_handicap_first_half_away_min_05_data) + " __ " + asian_handicap_first_half_away_min_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_home_plus_05_perc = str(asian_handicap_first_half_home_plus_05_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_plus_05_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_plus_05_perc: " + str(asian_handicap_first_half_home_plus_05_data) + " __ " + asian_handicap_first_half_home_plus_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_plus_05_perc = str(asian_handicap_first_half_away_plus_05_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_plus_05_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_plus_05_perc: " + str(asian_handicap_first_half_away_plus_05_data) + " __ " + asian_handicap_first_half_away_plus_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_first_half_home_plus_1_perc = str(asian_handicap_first_half_home_plus_1_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_plus_1_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_plus_1_perc: " + str(asian_handicap_first_half_home_plus_1_data) + " __ " + asian_handicap_first_half_home_plus_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_plus_1_perc = str(asian_handicap_first_half_away_plus_1_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_plus_1_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_plus_1_perc: " + str(asian_handicap_first_half_away_plus_1_data) + " __ " + asian_handicap_first_half_away_plus_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_home_plus_15_perc = str(asian_handicap_first_half_home_plus_15_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_plus_15_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_plus_15_perc: " + str(asian_handicap_first_half_home_plus_15_data) + " __ " + asian_handicap_first_half_home_plus_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_plus_15_perc = str(asian_handicap_first_half_away_plus_15_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_plus_15_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_plus_15_perc: " + str(asian_handicap_first_half_away_plus_15_data) + " __ " + asian_handicap_first_half_away_plus_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_first_half_home_min_1_perc = str(asian_handicap_first_half_home_min_1_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_min_1_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_min_1_perc: " + str(asian_handicap_first_half_home_min_1_data) + " __ " + asian_handicap_first_half_home_min_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_min_1_perc = str(asian_handicap_first_half_away_min_1_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_min_1_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_min_1_perc: " + str(asian_handicap_first_half_away_min_1_data) + " __ " + asian_handicap_first_half_away_min_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        asian_handicap_first_half_home_min_15_perc = str(asian_handicap_first_half_home_min_15_data / total_rows * 100)
        if(float(asian_handicap_first_half_home_min_15_perc) >= 80  ):
            print(space + "asian_handicap_first_half_home_min_15_perc: " + str(asian_handicap_first_half_home_min_15_data) + " __ " + asian_handicap_first_half_home_min_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        asian_handicap_first_half_away_min_15_perc = str(asian_handicap_first_half_away_min_15_data / total_rows * 100)
        if(float(asian_handicap_first_half_away_min_15_perc) >= 80  ):
            print(space + "asian_handicap_first_half_away_min_15_perc: " + str(asian_handicap_first_half_away_min_15_data) + " __ " + asian_handicap_first_half_away_min_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        double_chance__first_half_home_draw_perc = str(double_chance__first_half_home_draw_data / total_rows * 100)
        if(float(double_chance__first_half_home_draw_perc) >= 80  ):
            print(space + "double_chance__first_half_home_draw_perc: " + str(double_chance__first_half_home_draw_data) + " __ " + double_chance__first_half_home_draw_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        double_chance__first_half_home_away_perc = str(double_chance__first_half_home_away_data / total_rows * 100)
        if(float(double_chance__first_half_home_away_perc) >= 80  ):
            print(space + "double_chance__first_half_home_away_perc: " + str(double_chance__first_half_home_away_data) + " __ " + double_chance__first_half_home_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        double_chance__first_half_draw_away_perc = str(double_chance__first_half_draw_away_data / total_rows * 100)
        if(float(double_chance__first_half_draw_away_perc) >= 80  ):
            print(space + "double_chance__first_half_draw_away_perc: " + str(double_chance__first_half_draw_away_data) + " __ " + double_chance__first_half_draw_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        oddeven_odd_perc = str(oddeven_odd_data / total_rows * 100)
        if(float(oddeven_odd_perc) >= 80  ):
            print(space + "oddeven_odd_perc: " + str(oddeven_odd_data) + " __ " + oddeven_odd_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        oddeven_even_perc = str(oddeven_even_data / total_rows * 100)
        if(float(oddeven_even_perc) >= 80  ):
            print(space + "oddeven_even_perc: " + str(oddeven_even_data) + " __ " + oddeven_even_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_home_yes_perc = str(results_both_teams_score_home_yes_data / total_rows * 100)
        if(float(results_both_teams_score_home_yes_perc) >= 80  ):
            print(space + "results_both_teams_score_home_yes_perc: " + str(results_both_teams_score_home_yes_data) + " __ " + results_both_teams_score_home_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_draw_yes_perc = str(results_both_teams_score_draw_yes_data / total_rows * 100)
        if(float(results_both_teams_score_draw_yes_perc) >= 80  ):
            print(space + "results_both_teams_score_draw_yes_perc: " + str(results_both_teams_score_draw_yes_data) + " __ " + results_both_teams_score_draw_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_away_yes_perc = str(results_both_teams_score_away_yes_data / total_rows * 100)
        if(float(results_both_teams_score_away_yes_perc) >= 80  ):
            print(space + "results_both_teams_score_away_yes_perc: " + str(results_both_teams_score_away_yes_data) + " __ " + results_both_teams_score_away_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_home_no_perc = str(results_both_teams_score_home_no_data / total_rows * 100)
        if(float(results_both_teams_score_home_no_perc) >= 80  ):
            print(space + "results_both_teams_score_home_no_perc: " + str(results_both_teams_score_home_no_data) + " __ " + results_both_teams_score_home_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_draw_no_perc = str(results_both_teams_score_draw_no_data / total_rows * 100)
        if(float(results_both_teams_score_draw_no_perc) >= 80  ):
            print(space + "results_both_teams_score_draw_no_perc: " + str(results_both_teams_score_draw_no_data) + " __ " + results_both_teams_score_draw_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        results_both_teams_score_away_no_perc = str(results_both_teams_score_away_no_data / total_rows * 100)
        if(float(results_both_teams_score_away_no_perc) >= 80  ):
            print(space + "results_both_teams_score_away_no_perc: " + str(results_both_teams_score_away_no_data) + " __ " + results_both_teams_score_away_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_home_over_35_perc = str(result_total_goals_home_over_35_data / total_rows * 100)
        if(float(result_total_goals_home_over_35_perc) >= 80  ):
            print(space + "result_total_goals_home_over_35_perc: " + str(result_total_goals_home_over_35_data) + " __ " + result_total_goals_home_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_draw_over_35_perc = str(result_total_goals_draw_over_35_data / total_rows * 100)
        if(float(result_total_goals_draw_over_35_perc) >= 80  ):
            print(space + "result_total_goals_draw_over_35_perc: " + str(result_total_goals_draw_over_35_data) + " __ " + result_total_goals_draw_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_away_over_35_perc = str(result_total_goals_away_over_35_data / total_rows * 100)
        if(float(result_total_goals_away_over_35_perc) >= 80  ):
            print(space + "result_total_goals_away_over_35_perc: " + str(result_total_goals_away_over_35_data) + " __ " + result_total_goals_away_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_home_under_35_perc = str(result_total_goals_home_under_35_data / total_rows * 100)
        if(float(result_total_goals_home_under_35_perc) >= 80  ):
            print(space + "result_total_goals_home_under_35_perc: " + str(result_total_goals_home_under_35_data) + " __ " + result_total_goals_home_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_draw_under_35_perc = str(result_total_goals_draw_under_35_data / total_rows * 100)
        if(float(result_total_goals_draw_under_35_perc) >= 80  ):
            print(space + "result_total_goals_draw_under_35_perc: " + str(result_total_goals_draw_under_35_data) + " __ " + result_total_goals_draw_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_away_under_35_perc = str(result_total_goals_away_under_35_data / total_rows * 100)
        if(float(result_total_goals_away_under_35_perc) >= 80  ):
            print(space + "result_total_goals_away_under_35_perc: " + str(result_total_goals_away_under_35_data) + " __ " + result_total_goals_away_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_home_over_25_perc = str(result_total_goals_home_over_25_data / total_rows * 100)
        if(float(result_total_goals_home_over_25_perc) >= 80  ):
            print(space + "result_total_goals_home_over_25_perc: " + str(result_total_goals_home_over_25_data) + " __ " + result_total_goals_home_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_draw_over_25_perc = str(result_total_goals_draw_over_25_data / total_rows * 100)
        if(float(result_total_goals_draw_over_25_perc) >= 80  ):
            print(space + "result_total_goals_draw_over_25_perc: " + str(result_total_goals_draw_over_25_data) + " __ " + result_total_goals_draw_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_away_over_25_perc = str(result_total_goals_away_over_25_data / total_rows * 100)
        if(float(result_total_goals_away_over_25_perc) >= 80  ):
            print(space + "result_total_goals_away_over_25_perc: " + str(result_total_goals_away_over_25_data) + " __ " + result_total_goals_away_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_home_under_25_perc = str(result_total_goals_home_under_25_data / total_rows * 100)
        if(float(result_total_goals_home_under_25_perc) >= 80  ):
            print(space + "result_total_goals_home_under_25_perc: " + str(result_total_goals_home_under_25_data) + " __ " + result_total_goals_home_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_draw_under_25_perc = str(result_total_goals_draw_under_25_data / total_rows * 100)
        if(float(result_total_goals_draw_under_25_perc) >= 80  ):
            print(space + "result_total_goals_draw_under_25_perc: " + str(result_total_goals_draw_under_25_data) + " __ " + result_total_goals_draw_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        result_total_goals_away_under_25_perc = str(result_total_goals_away_under_25_data / total_rows * 100)
        if(float(result_total_goals_away_under_25_perc) >= 80  ):
            print(space + "result_total_goals_away_under_25_perc: " + str(result_total_goals_away_under_25_data) + " __ " + result_total_goals_away_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder__second_half_over_10_perc = str(goals_overunder__second_half_over_10_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_10_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_10_perc: " + str(goals_overunder__second_half_over_10_data) + " __ " + goals_overunder__second_half_over_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder__second_half_over_30_perc = str(goals_overunder__second_half_over_30_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_30_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_30_perc: " + str(goals_overunder__second_half_over_30_data) + " __ " + goals_overunder__second_half_over_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        goals_overunder__second_half_under_10_perc = str(goals_overunder__second_half_under_10_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_10_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_10_perc: " + str(goals_overunder__second_half_under_10_data) + " __ " + goals_overunder__second_half_under_10_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_20_perc = str(goals_overunder__second_half_under_20_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_20_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_20_perc: " + str(goals_overunder__second_half_under_20_data) + " __ " + goals_overunder__second_half_under_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_30_perc = str(goals_overunder__second_half_under_30_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_30_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_30_perc: " + str(goals_overunder__second_half_under_30_data) + " __ " + goals_overunder__second_half_under_30_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_over_20_perc = str(goals_overunder__second_half_over_20_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_20_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_20_perc: " + str(goals_overunder__second_half_over_20_data) + " __ " + goals_overunder__second_half_over_20_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_over_35_perc = str(goals_overunder__second_half_over_35_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_35_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_35_perc: " + str(goals_overunder__second_half_over_35_data) + " __ " + goals_overunder__second_half_over_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_35_perc = str(goals_overunder__second_half_under_35_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_35_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_35_perc: " + str(goals_overunder__second_half_under_35_data) + " __ " + goals_overunder__second_half_under_35_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_over_15_perc = str(goals_overunder__second_half_over_15_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_15_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_15_perc: " + str(goals_overunder__second_half_over_15_data) + " __ " + goals_overunder__second_half_over_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_15_perc = str(goals_overunder__second_half_under_15_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_15_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_15_perc: " + str(goals_overunder__second_half_under_15_data) + " __ " + goals_overunder__second_half_under_15_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_over_25_perc = str(goals_overunder__second_half_over_25_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_25_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_25_perc: " + str(goals_overunder__second_half_over_25_data) + " __ " + goals_overunder__second_half_over_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_25_perc = str(goals_overunder__second_half_under_25_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_25_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_25_perc: " + str(goals_overunder__second_half_under_25_data) + " __ " + goals_overunder__second_half_under_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_over_05_perc = str(goals_overunder__second_half_over_05_data / total_rows * 100)
        if(float(goals_overunder__second_half_over_05_perc) >= 80  ):
            print(space + "goals_overunder__second_half_over_05_perc: " + str(goals_overunder__second_half_over_05_data) + " __ " + goals_overunder__second_half_over_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        goals_overunder__second_half_under_05_perc = str(goals_overunder__second_half_under_05_data / total_rows * 100)
        if(float(goals_overunder__second_half_under_05_perc) >= 80  ):
            print(space + "goals_overunder__second_half_under_05_perc: " + str(goals_overunder__second_half_under_05_data) + " __ " + goals_overunder__second_half_under_05_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        clean_sheet__home_yes_perc = str(clean_sheet__home_yes_data / total_rows * 100)
        if(float(clean_sheet__home_yes_perc) >= 80  ):
            print(space + "clean_sheet__home_yes_perc: " + str(clean_sheet__home_yes_data) + " __ " + clean_sheet__home_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        clean_sheet__home_no_perc = str(clean_sheet__home_no_data / total_rows * 100)
        if(float(clean_sheet__home_no_perc) >= 80  ):
            print(space + "clean_sheet__home_no_perc: " + str(clean_sheet__home_no_data) + " __ " + clean_sheet__home_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        clean_sheet__away_yes_perc = str(clean_sheet__away_yes_data / total_rows * 100)
        if(float(clean_sheet__away_yes_perc) >= 80  ):
            print(space + "clean_sheet__away_yes_perc: " + str(clean_sheet__away_yes_data) + " __ " + clean_sheet__away_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        clean_sheet__away_no_perc = str(clean_sheet__away_no_data / total_rows * 100)
        if(float(clean_sheet__away_no_perc) >= 80  ):
            print(space + "clean_sheet__away_no_perc: " + str(clean_sheet__away_no_data) + " __ " + clean_sheet__away_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        win_both_halves_home_perc = str(win_both_halves_home_data / total_rows * 100)
        if(float(win_both_halves_home_perc) >= 80  ):
            print(space + "win_both_halves_home_perc: " + str(win_both_halves_home_data) + " __ " + win_both_halves_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        win_both_halves_away_perc = str(win_both_halves_away_data / total_rows * 100)
        if(float(win_both_halves_away_perc) >= 80  ):
            print(space + "win_both_halves_away_perc: " + str(win_both_halves_away_data) + " __ " + win_both_halves_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_score__first_half_yes_perc = str(both_teams_score__first_half_yes_data / total_rows * 100)
        if(float(both_teams_score__first_half_yes_perc) >= 80  ):
            print(space + "both_teams_score__first_half_yes_perc: " + str(both_teams_score__first_half_yes_data) + " __ " + both_teams_score__first_half_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_score__first_half_no_perc = str(both_teams_score__first_half_no_data / total_rows * 100)
        if(float(both_teams_score__first_half_no_perc) >= 80  ):
            print(space + "both_teams_score__first_half_no_perc: " + str(both_teams_score__first_half_no_data) + " __ " + both_teams_score__first_half_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_to_score__second_half_yes_perc = str(both_teams_to_score__second_half_yes_data / total_rows * 100)
        if(float(both_teams_to_score__second_half_yes_perc) >= 80  ):
            print(space + "both_teams_to_score__second_half_yes_perc: " + str(both_teams_to_score__second_half_yes_data) + " __ " + both_teams_to_score__second_half_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_to_score__second_half_no_perc = str(both_teams_to_score__second_half_no_data / total_rows * 100)
        if(float(both_teams_to_score__second_half_no_perc) >= 80  ):
            print(space + "both_teams_to_score__second_half_no_perc: " + str(both_teams_to_score__second_half_no_data) + " __ " + both_teams_to_score__second_half_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        win_to_nil_home_perc = str(win_to_nil_home_data / total_rows * 100)
        if(float(win_to_nil_home_perc) >= 80  ):
            print(space + "win_to_nil_home_perc: " + str(win_to_nil_home_data) + " __ " + win_to_nil_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        win_to_nil_away_perc = str(win_to_nil_away_data / total_rows * 100)
        if(float(win_to_nil_away_perc) >= 80  ):
            print(space + "win_to_nil_away_perc: " + str(win_to_nil_away_data) + " __ " + win_to_nil_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_2_perc = str(exact_goals_number_2_data / total_rows * 100)
        if(float(exact_goals_number_2_perc) >= 80  ):
            print(space + "exact_goals_number_2_perc: " + str(exact_goals_number_2_data) + " __ " + exact_goals_number_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_3_perc = str(exact_goals_number_3_data / total_rows * 100)
        if(float(exact_goals_number_3_perc) >= 80  ):
            print(space + "exact_goals_number_3_perc: " + str(exact_goals_number_3_data) + " __ " + exact_goals_number_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_4_perc = str(exact_goals_number_4_data / total_rows * 100)
        if(float(exact_goals_number_4_perc) >= 80  ):
            print(space + "exact_goals_number_4_perc: " + str(exact_goals_number_4_data) + " __ " + exact_goals_number_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_1_perc = str(exact_goals_number_1_data / total_rows * 100)
        if(float(exact_goals_number_1_perc) >= 80  ):
            print(space + "exact_goals_number_1_perc: " + str(exact_goals_number_1_data) + " __ " + exact_goals_number_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_0_perc = str(exact_goals_number_0_data / total_rows * 100)
        if(float(exact_goals_number_0_perc) >= 80  ):
            print(space + "exact_goals_number_0_perc: " + str(exact_goals_number_0_data) + " __ " + exact_goals_number_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_5_perc = str(exact_goals_number_5_data / total_rows * 100)
        if(float(exact_goals_number_5_perc) >= 80  ):
            print(space + "exact_goals_number_5_perc: " + str(exact_goals_number_5_data) + " __ " + exact_goals_number_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_6_perc = str(exact_goals_number_6_data / total_rows * 100)
        if(float(exact_goals_number_6_perc) >= 80  ):
            print(space + "exact_goals_number_6_perc: " + str(exact_goals_number_6_data) + " __ " + exact_goals_number_6_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number_more_7_perc = str(exact_goals_number_more_7_data / total_rows * 100)
        if(float(exact_goals_number_more_7_perc) >= 80  ):
            print(space + "exact_goals_number_more_7_perc: " + str(exact_goals_number_more_7_data) + " __ " + exact_goals_number_more_7_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        to_win_either_half_home_perc = str(to_win_either_half_home_data / total_rows * 100)
        if(float(to_win_either_half_home_perc) >= 80  ):
            print(space + "to_win_either_half_home_perc: " + str(to_win_either_half_home_data) + " __ " + to_win_either_half_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        to_win_either_half_away_perc = str(to_win_either_half_away_data / total_rows * 100)
        if(float(to_win_either_half_away_perc) >= 80  ):
            print(space + "to_win_either_half_away_perc: " + str(to_win_either_half_away_data) + " __ " + to_win_either_half_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        home_team_exact_goals_number_2_perc = str(home_team_exact_goals_number_2_data / total_rows * 100)
        if(float(home_team_exact_goals_number_2_perc) >= 80  ):
            print(space + "home_team_exact_goals_number_2_perc: " + str(home_team_exact_goals_number_2_data) + " __ " + home_team_exact_goals_number_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        home_team_exact_goals_number_1_perc = str(home_team_exact_goals_number_1_data / total_rows * 100)
        if(float(home_team_exact_goals_number_1_perc) >= 80  ):
            print(space + "home_team_exact_goals_number_1_perc: " + str(home_team_exact_goals_number_1_data) + " __ " + home_team_exact_goals_number_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        home_team_exact_goals_number_0_perc = str(home_team_exact_goals_number_0_data / total_rows * 100)
        if(float(home_team_exact_goals_number_0_perc) >= 80  ):
            print(space + "home_team_exact_goals_number_0_perc: " + str(home_team_exact_goals_number_0_data) + " __ " + home_team_exact_goals_number_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        home_team_exact_goals_number_more_3_perc = str(home_team_exact_goals_number_more_3_data / total_rows * 100)
        if(float(home_team_exact_goals_number_more_3_perc) >= 80  ):
            print(space + "home_team_exact_goals_number_more_3_perc: " + str(home_team_exact_goals_number_more_3_data) + " __ " + home_team_exact_goals_number_more_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        away_team_exact_goals_number_2_perc = str(away_team_exact_goals_number_2_data / total_rows * 100)
        if(float(away_team_exact_goals_number_2_perc) >= 80  ):
            print(space + "away_team_exact_goals_number_2_perc: " + str(away_team_exact_goals_number_2_data) + " __ " + away_team_exact_goals_number_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        away_team_exact_goals_number_1_perc = str(away_team_exact_goals_number_1_data / total_rows * 100)
        if(float(away_team_exact_goals_number_1_perc) >= 80  ):
            print(space + "away_team_exact_goals_number_1_perc: " + str(away_team_exact_goals_number_1_data) + " __ " + away_team_exact_goals_number_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        away_team_exact_goals_number_0_perc = str(away_team_exact_goals_number_0_data / total_rows * 100)
        if(float(away_team_exact_goals_number_0_perc) >= 80  ):
            print(space + "away_team_exact_goals_number_0_perc: " + str(away_team_exact_goals_number_0_data) + " __ " + away_team_exact_goals_number_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        away_team_exact_goals_number_more_3_perc = str(away_team_exact_goals_number_more_3_data / total_rows * 100)
        if(float(away_team_exact_goals_number_more_3_perc) >= 80  ):
            print(space + "away_team_exact_goals_number_more_3_perc: " + str(away_team_exact_goals_number_more_3_data) + " __ " + away_team_exact_goals_number_more_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_2_perc = str(second_half_exact_goals_number_2_data / total_rows * 100)
        if(float(second_half_exact_goals_number_2_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_2_perc: " + str(second_half_exact_goals_number_2_data) + " __ " + second_half_exact_goals_number_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_3_perc = str(second_half_exact_goals_number_3_data / total_rows * 100)
        if(float(second_half_exact_goals_number_3_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_3_perc: " + str(second_half_exact_goals_number_3_data) + " __ " + second_half_exact_goals_number_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_4_perc = str(second_half_exact_goals_number_4_data / total_rows * 100)
        if(float(second_half_exact_goals_number_4_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_4_perc: " + str(second_half_exact_goals_number_4_data) + " __ " + second_half_exact_goals_number_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_1_perc = str(second_half_exact_goals_number_1_data / total_rows * 100)
        if(float(second_half_exact_goals_number_1_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_1_perc: " + str(second_half_exact_goals_number_1_data) + " __ " + second_half_exact_goals_number_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_0_perc = str(second_half_exact_goals_number_0_data / total_rows * 100)
        if(float(second_half_exact_goals_number_0_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_0_perc: " + str(second_half_exact_goals_number_0_data) + " __ " + second_half_exact_goals_number_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        second_half_exact_goals_number_more_5_perc = str(second_half_exact_goals_number_more_5_data / total_rows * 100)
        if(float(second_half_exact_goals_number_more_5_perc) >= 80  ):
            print(space + "second_half_exact_goals_number_more_5_perc: " + str(second_half_exact_goals_number_more_5_data) + " __ " + second_half_exact_goals_number_more_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_700_perc = str(corners_over_under_over_700_data / total_rows * 100)
        # if(float(corners_over_under_over_700_perc) >= 80  ):
        #     print(space + "corners_over_under_over_700_perc: " + str(corners_over_under_over_700_data) + " __ " + corners_over_under_over_700_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_700_perc = str(corners_over_under_under_700_data / total_rows * 100)
        # if(float(corners_over_under_under_700_perc) >= 80  ):
        #     print(space + "corners_over_under_under_700_perc: " + str(corners_over_under_under_700_data) + " __ " + corners_over_under_under_700_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_725_perc = str(corners_over_under_over_725_data / total_rows * 100)
        # if(float(corners_over_under_over_725_perc) >= 80  ):
        #     print(space + "corners_over_under_over_725_perc: " + str(corners_over_under_over_725_data) + " __ " + corners_over_under_over_725_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_725_perc = str(corners_over_under_under_725_data / total_rows * 100)
        # if(float(corners_over_under_under_725_perc) >= 80  ):
        #     print(space + "corners_over_under_under_725_perc: " + str(corners_over_under_under_725_data) + " __ " + corners_over_under_under_725_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_750_perc = str(corners_over_under_over_750_data / total_rows * 100)
        # if(float(corners_over_under_over_750_perc) >= 80  ):
        #     print(space + "corners_over_under_over_750_perc: " + str(corners_over_under_over_750_data) + " __ " + corners_over_under_over_750_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_750_perc = str(corners_over_under_under_750_data / total_rows * 100)
        # if(float(corners_over_under_under_750_perc) >= 80  ):
        #     print(space + "corners_over_under_under_750_perc: " + str(corners_over_under_under_750_data) + " __ " + corners_over_under_under_750_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_775_perc = str(corners_over_under_over_775_data / total_rows * 100)
        # if(float(corners_over_under_over_775_perc) >= 80  ):
        #     print(space + "corners_over_under_over_775_perc: " + str(corners_over_under_over_775_data) + " __ " + corners_over_under_over_775_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_775_perc = str(corners_over_under_under_775_data / total_rows * 100)
        # if(float(corners_over_under_under_775_perc) >= 80  ):
        #     print(space + "corners_over_under_under_775_perc: " + str(corners_over_under_under_775_data) + " __ " + corners_over_under_under_775_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_850_perc = str(corners_over_under_over_850_data / total_rows * 100)
        # if(float(corners_over_under_over_850_perc) >= 80  ):
        #     print(space + "corners_over_under_over_850_perc: " + str(corners_over_under_over_850_data) + " __ " + corners_over_under_over_850_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_850_perc = str(corners_over_under_under_850_data / total_rows * 100)
        # if(float(corners_over_under_under_850_perc) >= 80  ):
        #     print(space + "corners_over_under_under_850_perc: " + str(corners_over_under_under_850_data) + " __ " + corners_over_under_under_850_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_800_perc = str(corners_over_under_over_800_data / total_rows * 100)
        # if(float(corners_over_under_over_800_perc) >= 80  ):
        #     print(space + "corners_over_under_over_800_perc: " + str(corners_over_under_over_800_data) + " __ " + corners_over_under_over_800_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_800_perc = str(corners_over_under_under_800_data / total_rows * 100)
        # if(float(corners_over_under_under_800_perc) >= 80  ):
        #     print(space + "corners_over_under_under_800_perc: " + str(corners_over_under_under_800_data) + " __ " + corners_over_under_under_800_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_825_perc = str(corners_over_under_over_825_data / total_rows * 100)
        # if(float(corners_over_under_over_825_perc) >= 80  ):
        #     print(space + "corners_over_under_over_825_perc: " + str(corners_over_under_over_825_data) + " __ " + corners_over_under_over_825_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_825_perc = str(corners_over_under_under_825_data / total_rows * 100)
        # if(float(corners_over_under_under_825_perc) >= 80  ):
        #     print(space + "corners_over_under_under_825_perc: " + str(corners_over_under_under_825_data) + " __ " + corners_over_under_under_825_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_875_perc = str(corners_over_under_over_875_data / total_rows * 100)
        # if(float(corners_over_under_over_875_perc) >= 80  ):
        #     print(space + "corners_over_under_over_875_perc: " + str(corners_over_under_over_875_data) + " __ " + corners_over_under_over_875_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_875_perc = str(corners_over_under_under_875_data / total_rows * 100)
        # if(float(corners_over_under_under_875_perc) >= 80  ):
        #     print(space + "corners_over_under_under_875_perc: " + str(corners_over_under_under_875_data) + " __ " + corners_over_under_under_875_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_900_perc = str(corners_over_under_over_900_data / total_rows * 100)
        # if(float(corners_over_under_over_900_perc) >= 80  ):
        #     print(space + "corners_over_under_over_900_perc: " + str(corners_over_under_over_900_data) + " __ " + corners_over_under_over_900_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_900_perc = str(corners_over_under_under_900_data / total_rows * 100)
        # if(float(corners_over_under_under_900_perc) >= 80  ):
        #     print(space + "corners_over_under_under_900_perc: " + str(corners_over_under_under_900_data) + " __ " + corners_over_under_under_900_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_925_perc = str(corners_over_under_over_925_data / total_rows * 100)
        # if(float(corners_over_under_over_925_perc) >= 80  ):
        #     print(space + "corners_over_under_over_925_perc: " + str(corners_over_under_over_925_data) + " __ " + corners_over_under_over_925_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_925_perc = str(corners_over_under_under_925_data / total_rows * 100)
        # if(float(corners_over_under_under_925_perc) >= 80  ):
        #     print(space + "corners_over_under_under_925_perc: " + str(corners_over_under_under_925_data) + " __ " + corners_over_under_under_925_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_950_perc = str(corners_over_under_over_950_data / total_rows * 100)
        # if(float(corners_over_under_over_950_perc) >= 80  ):
        #     print(space + "corners_over_under_over_950_perc: " + str(corners_over_under_over_950_data) + " __ " + corners_over_under_over_950_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_950_perc = str(corners_over_under_under_950_data / total_rows * 100)
        # if(float(corners_over_under_under_950_perc) >= 80  ):
        #     print(space + "corners_over_under_under_950_perc: " + str(corners_over_under_under_950_data) + " __ " + corners_over_under_under_950_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_975_perc = str(corners_over_under_over_975_data / total_rows * 100)
        # if(float(corners_over_under_over_975_perc) >= 80  ):
        #     print(space + "corners_over_under_over_975_perc: " + str(corners_over_under_over_975_data) + " __ " + corners_over_under_over_975_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_975_perc = str(corners_over_under_under_975_data / total_rows * 100)
        # if(float(corners_over_under_under_975_perc) >= 80  ):
        #     print(space + "corners_over_under_under_975_perc: " + str(corners_over_under_under_975_data) + " __ " + corners_over_under_under_975_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1000_perc = str(corners_over_under_over_1000_data / total_rows * 100)
        # if(float(corners_over_under_over_1000_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1000_perc: " + str(corners_over_under_over_1000_data) + " __ " + corners_over_under_over_1000_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1000_perc = str(corners_over_under_under_1000_data / total_rows * 100)
        # if(float(corners_over_under_under_1000_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1000_perc: " + str(corners_over_under_under_1000_data) + " __ " + corners_over_under_under_1000_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1025_perc = str(corners_over_under_over_1025_data / total_rows * 100)
        # if(float(corners_over_under_over_1025_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1025_perc: " + str(corners_over_under_over_1025_data) + " __ " + corners_over_under_over_1025_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1025_perc = str(corners_over_under_under_1025_data / total_rows * 100)
        # if(float(corners_over_under_under_1025_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1025_perc: " + str(corners_over_under_under_1025_data) + " __ " + corners_over_under_under_1025_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1050_perc = str(corners_over_under_over_1050_data / total_rows * 100)
        # if(float(corners_over_under_over_1050_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1050_perc: " + str(corners_over_under_over_1050_data) + " __ " + corners_over_under_over_1050_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1050_perc = str(corners_over_under_under_1050_data / total_rows * 100)
        # if(float(corners_over_under_under_1050_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1050_perc: " + str(corners_over_under_under_1050_data) + " __ " + corners_over_under_under_1050_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1075_perc = str(corners_over_under_over_1075_data / total_rows * 100)
        # if(float(corners_over_under_over_1075_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1075_perc: " + str(corners_over_under_over_1075_data) + " __ " + corners_over_under_over_1075_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1075_perc = str(corners_over_under_under_1075_data / total_rows * 100)
        # if(float(corners_over_under_under_1075_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1075_perc: " + str(corners_over_under_under_1075_data) + " __ " + corners_over_under_under_1075_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1100_perc = str(corners_over_under_over_1100_data / total_rows * 100)
        # if(float(corners_over_under_over_1100_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1100_perc: " + str(corners_over_under_over_1100_data) + " __ " + corners_over_under_over_1100_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1100_perc = str(corners_over_under_under_1100_data / total_rows * 100)
        # if(float(corners_over_under_under_1100_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1100_perc: " + str(corners_over_under_under_1100_data) + " __ " + corners_over_under_under_1100_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1125_perc = str(corners_over_under_over_1125_data / total_rows * 100)
        # if(float(corners_over_under_over_1125_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1125_perc: " + str(corners_over_under_over_1125_data) + " __ " + corners_over_under_over_1125_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1125_perc = str(corners_over_under_under_1125_data / total_rows * 100)
        # if(float(corners_over_under_under_1125_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1125_perc: " + str(corners_over_under_under_1125_data) + " __ " + corners_over_under_under_1125_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1150_perc = str(corners_over_under_over_1150_data / total_rows * 100)
        # if(float(corners_over_under_over_1150_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1150_perc: " + str(corners_over_under_over_1150_data) + " __ " + corners_over_under_over_1150_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1150_perc = str(corners_over_under_under_1150_data / total_rows * 100)
        # if(float(corners_over_under_under_1150_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1150_perc: " + str(corners_over_under_under_1150_data) + " __ " + corners_over_under_under_1150_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1175_perc = str(corners_over_under_over_1175_data / total_rows * 100)
        # if(float(corners_over_under_over_1175_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1175_perc: " + str(corners_over_under_over_1175_data) + " __ " + corners_over_under_over_1175_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1175_perc = str(corners_over_under_under_1175_data / total_rows * 100)
        # if(float(corners_over_under_under_1175_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1175_perc: " + str(corners_over_under_under_1175_data) + " __ " + corners_over_under_under_1175_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1200_perc = str(corners_over_under_over_1200_data / total_rows * 100)
        # if(float(corners_over_under_over_1200_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1200_perc: " + str(corners_over_under_over_1200_data) + " __ " + corners_over_under_over_1200_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1200_perc = str(corners_over_under_under_1200_data / total_rows * 100)
        # if(float(corners_over_under_under_1200_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1200_perc: " + str(corners_over_under_under_1200_data) + " __ " + corners_over_under_under_1200_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1225_perc = str(corners_over_under_over_1225_data / total_rows * 100)
        # if(float(corners_over_under_over_1225_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1225_perc: " + str(corners_over_under_over_1225_data) + " __ " + corners_over_under_over_1225_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1225_perc = str(corners_over_under_under_1225_data / total_rows * 100)
        # if(float(corners_over_under_under_1225_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1225_perc: " + str(corners_over_under_under_1225_data) + " __ " + corners_over_under_under_1225_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1250_perc = str(corners_over_under_over_1250_data / total_rows * 100)
        # if(float(corners_over_under_over_1250_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1250_perc: " + str(corners_over_under_over_1250_data) + " __ " + corners_over_under_over_1250_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1250_perc = str(corners_over_under_under_1250_data / total_rows * 100)
        # if(float(corners_over_under_under_1250_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1250_perc: " + str(corners_over_under_under_1250_data) + " __ " + corners_over_under_under_1250_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_over_1275_perc = str(corners_over_under_over_1275_data / total_rows * 100)
        # if(float(corners_over_under_over_1275_perc) >= 80  ):
        #     print(space + "corners_over_under_over_1275_perc: " + str(corners_over_under_over_1275_data) + " __ " + corners_over_under_over_1275_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_over_under_under_1275_perc = str(corners_over_under_under_1275_data / total_rows * 100)
        # if(float(corners_over_under_under_1275_perc) >= 80  ):
        #     print(space + "corners_over_under_under_1275_perc: " + str(corners_over_under_under_1275_data) + " __ " + corners_over_under_under_1275_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        exact_goals_number__first_half_2_perc = str(exact_goals_number__first_half_2_data / total_rows * 100)
        if(float(exact_goals_number__first_half_2_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_2_perc: " + str(exact_goals_number__first_half_2_data) + " __ " + exact_goals_number__first_half_2_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number__first_half_3_perc = str(exact_goals_number__first_half_3_data / total_rows * 100)
        if(float(exact_goals_number__first_half_3_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_3_perc: " + str(exact_goals_number__first_half_3_data) + " __ " + exact_goals_number__first_half_3_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number__first_half_4_perc = str(exact_goals_number__first_half_4_data / total_rows * 100)
        if(float(exact_goals_number__first_half_4_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_4_perc: " + str(exact_goals_number__first_half_4_data) + " __ " + exact_goals_number__first_half_4_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number__first_half_1_perc = str(exact_goals_number__first_half_1_data / total_rows * 100)
        if(float(exact_goals_number__first_half_1_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_1_perc: " + str(exact_goals_number__first_half_1_data) + " __ " + exact_goals_number__first_half_1_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number__first_half_0_perc = str(exact_goals_number__first_half_0_data / total_rows * 100)
        if(float(exact_goals_number__first_half_0_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_0_perc: " + str(exact_goals_number__first_half_0_data) + " __ " + exact_goals_number__first_half_0_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        exact_goals_number__first_half_more_5_perc = str(exact_goals_number__first_half_more_5_data / total_rows * 100)
        if(float(exact_goals_number__first_half_more_5_perc) >= 80  ):
            print(space + "exact_goals_number__first_half_more_5_perc: " + str(exact_goals_number__first_half_more_5_data) + " __ " + exact_goals_number__first_half_more_5_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        to_score_in_both_halves_by_teams_home_perc = str(to_score_in_both_halves_by_teams_home_data / total_rows * 100)
        if(float(to_score_in_both_halves_by_teams_home_perc) >= 80  ):
            print(space + "to_score_in_both_halves_by_teams_home_perc: " + str(to_score_in_both_halves_by_teams_home_data) + " __ " + to_score_in_both_halves_by_teams_home_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        to_score_in_both_halves_by_teams_away_perc = str(to_score_in_both_halves_by_teams_away_data / total_rows * 100)
        if(float(to_score_in_both_halves_by_teams_away_perc) >= 80  ):
            print(space + "to_score_in_both_halves_by_teams_away_perc: " + str(to_score_in_both_halves_by_teams_away_data) + " __ " + to_score_in_both_halves_by_teams_away_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_goals_both_teams_to_score_over_yes_25_perc = str(total_goals_both_teams_to_score_over_yes_25_data / total_rows * 100)
        if(float(total_goals_both_teams_to_score_over_yes_25_perc) >= 80  ):
            print(space + "total_goals_both_teams_to_score_over_yes_25_perc: " + str(total_goals_both_teams_to_score_over_yes_25_data) + " __ " + total_goals_both_teams_to_score_over_yes_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_goals_both_teams_to_score_over_no_25_perc = str(total_goals_both_teams_to_score_over_no_25_data / total_rows * 100)
        if(float(total_goals_both_teams_to_score_over_no_25_perc) >= 80  ):
            print(space + "total_goals_both_teams_to_score_over_no_25_perc: " + str(total_goals_both_teams_to_score_over_no_25_data) + " __ " + total_goals_both_teams_to_score_over_no_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_goals_both_teams_to_score_under_yes_25_perc = str(total_goals_both_teams_to_score_under_yes_25_data / total_rows * 100)
        if(float(total_goals_both_teams_to_score_under_yes_25_perc) >= 80  ):
            print(space + "total_goals_both_teams_to_score_under_yes_25_perc: " + str(total_goals_both_teams_to_score_under_yes_25_data) + " __ " + total_goals_both_teams_to_score_under_yes_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        total_goals_both_teams_to_score_under_no_25_perc = str(total_goals_both_teams_to_score_under_no_25_data / total_rows * 100)
        if(float(total_goals_both_teams_to_score_under_no_25_perc) >= 80  ):
            print(space + "total_goals_both_teams_to_score_under_no_25_perc: " + str(total_goals_both_teams_to_score_under_no_25_data) + " __ " + total_goals_both_teams_to_score_under_no_25_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_home_yes_perc = str(halftime_result_both_teams_score_home_yes_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_home_yes_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_home_yes_perc: " + str(halftime_result_both_teams_score_home_yes_data) + " __ " + halftime_result_both_teams_score_home_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_draw_yes_perc = str(halftime_result_both_teams_score_draw_yes_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_draw_yes_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_draw_yes_perc: " + str(halftime_result_both_teams_score_draw_yes_data) + " __ " + halftime_result_both_teams_score_draw_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_away_yes_perc = str(halftime_result_both_teams_score_away_yes_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_away_yes_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_away_yes_perc: " + str(halftime_result_both_teams_score_away_yes_data) + " __ " + halftime_result_both_teams_score_away_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_home_no_perc = str(halftime_result_both_teams_score_home_no_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_home_no_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_home_no_perc: " + str(halftime_result_both_teams_score_home_no_data) + " __ " + halftime_result_both_teams_score_home_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_draw_no_perc = str(halftime_result_both_teams_score_draw_no_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_draw_no_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_draw_no_perc: " + str(halftime_result_both_teams_score_draw_no_data) + " __ " + halftime_result_both_teams_score_draw_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        halftime_result_both_teams_score_away_no_perc = str(halftime_result_both_teams_score_away_no_data / total_rows * 100)
        if(float(halftime_result_both_teams_score_away_no_perc) >= 80  ):
            print(space + "halftime_result_both_teams_score_away_no_perc: " + str(halftime_result_both_teams_score_away_no_data) + " __ " + halftime_result_both_teams_score_away_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_winner_home_perc = str(corners_winner_home_data / total_rows * 100)
        # if(float(corners_winner_home_perc) >= 80  ):
        #     print(space + "corners_winner_home_perc: " + str(corners_winner_home_data) + " __ " + corners_winner_home_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_winner_draw_perc = str(corners_winner_draw_data / total_rows * 100)
        # if(float(corners_winner_draw_perc) >= 80  ):
        #     print(space + "corners_winner_draw_perc: " + str(corners_winner_draw_data) + " __ " + corners_winner_draw_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_winner_away_perc = str(corners_winner_away_data / total_rows * 100)
        # if(float(corners_winner_away_perc) >= 80  ):
        #     print(space + "corners_winner_away_perc: " + str(corners_winner_away_data) + " __ " + corners_winner_away_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_6_perc = str(corners_asian_handicap_home_min_6_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_6_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_6_perc: " + str(corners_asian_handicap_home_min_6_data) + " __ " + corners_asian_handicap_home_min_6_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_6_perc = str(corners_asian_handicap_away_min_6_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_6_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_6_perc: " + str(corners_asian_handicap_away_min_6_data) + " __ " + corners_asian_handicap_away_min_6_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_25_perc = str(corners_asian_handicap_home_plus_25_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_25_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_25_perc: " + str(corners_asian_handicap_home_plus_25_data) + " __ " + corners_asian_handicap_home_plus_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_4_perc = str(corners_asian_handicap_home_plus_4_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_4_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_4_perc: " + str(corners_asian_handicap_home_plus_4_data) + " __ " + corners_asian_handicap_home_plus_4_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_4_perc = str(corners_asian_handicap_away_plus_4_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_4_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_4_perc: " + str(corners_asian_handicap_away_plus_4_data) + " __ " + corners_asian_handicap_away_plus_4_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_45_perc = str(corners_asian_handicap_home_plus_45_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_45_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_45_perc: " + str(corners_asian_handicap_home_plus_45_data) + " __ " + corners_asian_handicap_home_plus_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_45_perc = str(corners_asian_handicap_away_plus_45_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_45_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_45_perc: " + str(corners_asian_handicap_away_plus_45_data) + " __ " + corners_asian_handicap_away_plus_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_5_perc = str(corners_asian_handicap_home_plus_5_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_5_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_5_perc: " + str(corners_asian_handicap_home_plus_5_data) + " __ " + corners_asian_handicap_home_plus_5_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_5_perc = str(corners_asian_handicap_away_plus_5_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_5_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_5_perc: " + str(corners_asian_handicap_away_plus_5_data) + " __ " + corners_asian_handicap_away_plus_5_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_55_perc = str(corners_asian_handicap_home_plus_55_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_55_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_55_perc: " + str(corners_asian_handicap_home_plus_55_data) + " __ " + corners_asian_handicap_home_plus_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_55_perc = str(corners_asian_handicap_away_plus_55_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_55_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_55_perc: " + str(corners_asian_handicap_away_plus_55_data) + " __ " + corners_asian_handicap_away_plus_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_6_perc = str(corners_asian_handicap_home_plus_6_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_6_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_6_perc: " + str(corners_asian_handicap_home_plus_6_data) + " __ " + corners_asian_handicap_home_plus_6_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_6_perc = str(corners_asian_handicap_away_plus_6_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_6_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_6_perc: " + str(corners_asian_handicap_away_plus_6_data) + " __ " + corners_asian_handicap_away_plus_6_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_65_perc = str(corners_asian_handicap_home_plus_65_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_65_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_65_perc: " + str(corners_asian_handicap_home_plus_65_data) + " __ " + corners_asian_handicap_home_plus_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_65_perc = str(corners_asian_handicap_away_plus_65_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_65_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_65_perc: " + str(corners_asian_handicap_away_plus_65_data) + " __ " + corners_asian_handicap_away_plus_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_35_perc = str(corners_asian_handicap_home_plus_35_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_35_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_35_perc: " + str(corners_asian_handicap_home_plus_35_data) + " __ " + corners_asian_handicap_home_plus_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_35_perc = str(corners_asian_handicap_away_plus_35_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_35_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_35_perc: " + str(corners_asian_handicap_away_plus_35_data) + " __ " + corners_asian_handicap_away_plus_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_05_perc = str(corners_asian_handicap_home_min_05_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_05_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_05_perc: " + str(corners_asian_handicap_home_min_05_data) + " __ " + corners_asian_handicap_home_min_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_05_perc = str(corners_asian_handicap_away_min_05_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_05_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_05_perc: " + str(corners_asian_handicap_away_min_05_data) + " __ " + corners_asian_handicap_away_min_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_15_perc = str(corners_asian_handicap_home_min_15_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_15_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_15_perc: " + str(corners_asian_handicap_home_min_15_data) + " __ " + corners_asian_handicap_home_min_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_15_perc = str(corners_asian_handicap_away_min_15_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_15_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_15_perc: " + str(corners_asian_handicap_away_min_15_data) + " __ " + corners_asian_handicap_away_min_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_3_perc = str(corners_asian_handicap_away_plus_3_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_3_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_3_perc: " + str(corners_asian_handicap_away_plus_3_data) + " __ " + corners_asian_handicap_away_plus_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_3_perc = str(corners_asian_handicap_home_min_3_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_3_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_3_perc: " + str(corners_asian_handicap_home_min_3_data) + " __ " + corners_asian_handicap_home_min_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_05_perc = str(corners_asian_handicap_home_plus_05_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_05_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_05_perc: " + str(corners_asian_handicap_home_plus_05_data) + " __ " + corners_asian_handicap_home_plus_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_05_perc = str(corners_asian_handicap_away_plus_05_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_05_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_05_perc: " + str(corners_asian_handicap_away_plus_05_data) + " __ " + corners_asian_handicap_away_plus_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_0_perc = str(corners_asian_handicap_home_plus_0_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_0_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_0_perc: " + str(corners_asian_handicap_home_plus_0_data) + " __ " + corners_asian_handicap_home_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_1_perc = str(corners_asian_handicap_home_plus_1_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_1_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_1_perc: " + str(corners_asian_handicap_home_plus_1_data) + " __ " + corners_asian_handicap_home_plus_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_1_perc = str(corners_asian_handicap_away_plus_1_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_1_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_1_perc: " + str(corners_asian_handicap_away_plus_1_data) + " __ " + corners_asian_handicap_away_plus_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_2_perc = str(corners_asian_handicap_away_min_2_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_2_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_2_perc: " + str(corners_asian_handicap_away_min_2_data) + " __ " + corners_asian_handicap_away_min_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_3_perc = str(corners_asian_handicap_home_plus_3_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_3_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_3_perc: " + str(corners_asian_handicap_home_plus_3_data) + " __ " + corners_asian_handicap_home_plus_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_2_perc = str(corners_asian_handicap_home_plus_2_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_2_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_2_perc: " + str(corners_asian_handicap_home_plus_2_data) + " __ " + corners_asian_handicap_home_plus_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_2_perc = str(corners_asian_handicap_away_plus_2_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_2_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_2_perc: " + str(corners_asian_handicap_away_plus_2_data) + " __ " + corners_asian_handicap_away_plus_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_0_perc = str(corners_asian_handicap_away_plus_0_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_0_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_0_perc: " + str(corners_asian_handicap_away_plus_0_data) + " __ " + corners_asian_handicap_away_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_1_perc = str(corners_asian_handicap_away_min_1_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_1_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_1_perc: " + str(corners_asian_handicap_away_min_1_data) + " __ " + corners_asian_handicap_away_min_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_4_perc = str(corners_asian_handicap_home_min_4_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_4_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_4_perc: " + str(corners_asian_handicap_home_min_4_data) + " __ " + corners_asian_handicap_home_min_4_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_4_perc = str(corners_asian_handicap_away_min_4_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_4_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_4_perc: " + str(corners_asian_handicap_away_min_4_data) + " __ " + corners_asian_handicap_away_min_4_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_45_perc = str(corners_asian_handicap_home_min_45_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_45_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_45_perc: " + str(corners_asian_handicap_home_min_45_data) + " __ " + corners_asian_handicap_home_min_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_25_perc = str(corners_asian_handicap_away_min_25_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_25_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_25_perc: " + str(corners_asian_handicap_away_min_25_data) + " __ " + corners_asian_handicap_away_min_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_plus_15_perc = str(corners_asian_handicap_home_plus_15_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_plus_15_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_plus_15_perc: " + str(corners_asian_handicap_home_plus_15_data) + " __ " + corners_asian_handicap_home_plus_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_3_perc = str(corners_asian_handicap_away_min_3_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_3_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_3_perc: " + str(corners_asian_handicap_away_min_3_data) + " __ " + corners_asian_handicap_away_min_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_25_perc = str(corners_asian_handicap_home_min_25_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_25_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_25_perc: " + str(corners_asian_handicap_home_min_25_data) + " __ " + corners_asian_handicap_home_min_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_2_perc = str(corners_asian_handicap_home_min_2_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_2_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_2_perc: " + str(corners_asian_handicap_home_min_2_data) + " __ " + corners_asian_handicap_home_min_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_1_perc = str(corners_asian_handicap_home_min_1_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_1_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_1_perc: " + str(corners_asian_handicap_home_min_1_data) + " __ " + corners_asian_handicap_home_min_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_15_perc = str(corners_asian_handicap_away_plus_15_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_15_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_15_perc: " + str(corners_asian_handicap_away_plus_15_data) + " __ " + corners_asian_handicap_away_plus_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_55_perc = str(corners_asian_handicap_away_min_55_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_55_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_55_perc: " + str(corners_asian_handicap_away_min_55_data) + " __ " + corners_asian_handicap_away_min_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_35_perc = str(corners_asian_handicap_away_min_35_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_35_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_35_perc: " + str(corners_asian_handicap_away_min_35_data) + " __ " + corners_asian_handicap_away_min_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_plus_25_perc = str(corners_asian_handicap_away_plus_25_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_plus_25_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_plus_25_perc: " + str(corners_asian_handicap_away_plus_25_data) + " __ " + corners_asian_handicap_away_plus_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_65_perc = str(corners_asian_handicap_home_min_65_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_65_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_65_perc: " + str(corners_asian_handicap_home_min_65_data) + " __ " + corners_asian_handicap_home_min_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_55_perc = str(corners_asian_handicap_home_min_55_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_55_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_55_perc: " + str(corners_asian_handicap_home_min_55_data) + " __ " + corners_asian_handicap_home_min_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_35_perc = str(corners_asian_handicap_home_min_35_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_35_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_35_perc: " + str(corners_asian_handicap_home_min_35_data) + " __ " + corners_asian_handicap_home_min_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_home_min_5_perc = str(corners_asian_handicap_home_min_5_data / total_rows * 100)
        # if(float(corners_asian_handicap_home_min_5_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_home_min_5_perc: " + str(corners_asian_handicap_home_min_5_data) + " __ " + corners_asian_handicap_home_min_5_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_5_perc = str(corners_asian_handicap_away_min_5_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_5_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_5_perc: " + str(corners_asian_handicap_away_min_5_data) + " __ " + corners_asian_handicap_away_min_5_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_45_perc = str(corners_asian_handicap_away_min_45_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_45_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_45_perc: " + str(corners_asian_handicap_away_min_45_data) + " __ " + corners_asian_handicap_away_min_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # corners_asian_handicap_away_min_65_perc = str(corners_asian_handicap_away_min_65_data / total_rows * 100)
        # if(float(corners_asian_handicap_away_min_65_perc) >= 80  ):
        #     print(space + "corners_asian_handicap_away_min_65_perc: " + str(corners_asian_handicap_away_min_65_data) + " __ " + corners_asian_handicap_away_min_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_85_perc = str(home_corners_overunder_over_85_data / total_rows * 100)
        # if(float(home_corners_overunder_over_85_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_85_perc: " + str(home_corners_overunder_over_85_data) + " __ " + home_corners_overunder_over_85_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_85_perc = str(home_corners_overunder_under_85_data / total_rows * 100)
        # if(float(home_corners_overunder_under_85_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_85_perc: " + str(home_corners_overunder_under_85_data) + " __ " + home_corners_overunder_under_85_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_25_perc = str(home_corners_overunder_over_25_data / total_rows * 100)
        # if(float(home_corners_overunder_over_25_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_25_perc: " + str(home_corners_overunder_over_25_data) + " __ " + home_corners_overunder_over_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_25_perc = str(home_corners_overunder_under_25_data / total_rows * 100)
        # if(float(home_corners_overunder_under_25_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_25_perc: " + str(home_corners_overunder_under_25_data) + " __ " + home_corners_overunder_under_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_55_perc = str(home_corners_overunder_over_55_data / total_rows * 100)
        # if(float(home_corners_overunder_over_55_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_55_perc: " + str(home_corners_overunder_over_55_data) + " __ " + home_corners_overunder_over_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_55_perc = str(home_corners_overunder_under_55_data / total_rows * 100)
        # if(float(home_corners_overunder_under_55_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_55_perc: " + str(home_corners_overunder_under_55_data) + " __ " + home_corners_overunder_under_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_45_perc = str(home_corners_overunder_over_45_data / total_rows * 100)
        # if(float(home_corners_overunder_over_45_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_45_perc: " + str(home_corners_overunder_over_45_data) + " __ " + home_corners_overunder_over_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_45_perc = str(home_corners_overunder_under_45_data / total_rows * 100)
        # if(float(home_corners_overunder_under_45_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_45_perc: " + str(home_corners_overunder_under_45_data) + " __ " + home_corners_overunder_under_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_65_perc = str(home_corners_overunder_over_65_data / total_rows * 100)
        # if(float(home_corners_overunder_over_65_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_65_perc: " + str(home_corners_overunder_over_65_data) + " __ " + home_corners_overunder_over_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_65_perc = str(home_corners_overunder_under_65_data / total_rows * 100)
        # if(float(home_corners_overunder_under_65_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_65_perc: " + str(home_corners_overunder_under_65_data) + " __ " + home_corners_overunder_under_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_75_perc = str(home_corners_overunder_over_75_data / total_rows * 100)
        # if(float(home_corners_overunder_over_75_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_75_perc: " + str(home_corners_overunder_over_75_data) + " __ " + home_corners_overunder_over_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_75_perc = str(home_corners_overunder_under_75_data / total_rows * 100)
        # if(float(home_corners_overunder_under_75_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_75_perc: " + str(home_corners_overunder_under_75_data) + " __ " + home_corners_overunder_under_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_over_35_perc = str(home_corners_overunder_over_35_data / total_rows * 100)
        # if(float(home_corners_overunder_over_35_perc) >= 80  ):
        #     print(space + "home_corners_overunder_over_35_perc: " + str(home_corners_overunder_over_35_data) + " __ " + home_corners_overunder_over_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_corners_overunder_under_35_perc = str(home_corners_overunder_under_35_data / total_rows * 100)
        # if(float(home_corners_overunder_under_35_perc) >= 80  ):
        #     print(space + "home_corners_overunder_under_35_perc: " + str(home_corners_overunder_under_35_data) + " __ " + home_corners_overunder_under_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_55_perc = str(away_corners_overunder_over_55_data / total_rows * 100)
        # if(float(away_corners_overunder_over_55_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_55_perc: " + str(away_corners_overunder_over_55_data) + " __ " + away_corners_overunder_over_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_55_perc = str(away_corners_overunder_under_55_data / total_rows * 100)
        # if(float(away_corners_overunder_under_55_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_55_perc: " + str(away_corners_overunder_under_55_data) + " __ " + away_corners_overunder_under_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_35_perc = str(away_corners_overunder_over_35_data / total_rows * 100)
        # if(float(away_corners_overunder_over_35_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_35_perc: " + str(away_corners_overunder_over_35_data) + " __ " + away_corners_overunder_over_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_35_perc = str(away_corners_overunder_under_35_data / total_rows * 100)
        # if(float(away_corners_overunder_under_35_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_35_perc: " + str(away_corners_overunder_under_35_data) + " __ " + away_corners_overunder_under_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_45_perc = str(away_corners_overunder_over_45_data / total_rows * 100)
        # if(float(away_corners_overunder_over_45_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_45_perc: " + str(away_corners_overunder_over_45_data) + " __ " + away_corners_overunder_over_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_45_perc = str(away_corners_overunder_under_45_data / total_rows * 100)
        # if(float(away_corners_overunder_under_45_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_45_perc: " + str(away_corners_overunder_under_45_data) + " __ " + away_corners_overunder_under_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_25_perc = str(away_corners_overunder_over_25_data / total_rows * 100)
        # if(float(away_corners_overunder_over_25_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_25_perc: " + str(away_corners_overunder_over_25_data) + " __ " + away_corners_overunder_over_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_25_perc = str(away_corners_overunder_under_25_data / total_rows * 100)
        # if(float(away_corners_overunder_under_25_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_25_perc: " + str(away_corners_overunder_under_25_data) + " __ " + away_corners_overunder_under_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_75_perc = str(away_corners_overunder_over_75_data / total_rows * 100)
        # if(float(away_corners_overunder_over_75_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_75_perc: " + str(away_corners_overunder_over_75_data) + " __ " + away_corners_overunder_over_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_75_perc = str(away_corners_overunder_under_75_data / total_rows * 100)
        # if(float(away_corners_overunder_under_75_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_75_perc: " + str(away_corners_overunder_under_75_data) + " __ " + away_corners_overunder_under_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_85_perc = str(away_corners_overunder_over_85_data / total_rows * 100)
        # if(float(away_corners_overunder_over_85_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_85_perc: " + str(away_corners_overunder_over_85_data) + " __ " + away_corners_overunder_over_85_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_85_perc = str(away_corners_overunder_under_85_data / total_rows * 100)
        # if(float(away_corners_overunder_under_85_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_85_perc: " + str(away_corners_overunder_under_85_data) + " __ " + away_corners_overunder_under_85_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_over_65_perc = str(away_corners_overunder_over_65_data / total_rows * 100)
        # if(float(away_corners_overunder_over_65_perc) >= 80  ):
        #     print(space + "away_corners_overunder_over_65_perc: " + str(away_corners_overunder_over_65_data) + " __ " + away_corners_overunder_over_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_corners_overunder_under_65_perc = str(away_corners_overunder_under_65_data / total_rows * 100)
        # if(float(away_corners_overunder_under_65_perc) >= 80  ):
        #     print(space + "away_corners_overunder_under_65_perc: " + str(away_corners_overunder_under_65_data) + " __ " + away_corners_overunder_under_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        both_teams_to_score_1st_half__2nd_half_yes_yes_perc = str(both_teams_to_score_1st_half__2nd_half_yes_yes_data / total_rows * 100)
        if(float(both_teams_to_score_1st_half__2nd_half_yes_yes_perc) >= 80  ):
            print(space + "both_teams_to_score_1st_half__2nd_half_yes_yes_perc: " + str(both_teams_to_score_1st_half__2nd_half_yes_yes_data) + " __ " + both_teams_to_score_1st_half__2nd_half_yes_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_to_score_1st_half__2nd_half_yes_no_perc = str(both_teams_to_score_1st_half__2nd_half_yes_no_data / total_rows * 100)
        if(float(both_teams_to_score_1st_half__2nd_half_yes_no_perc) >= 80  ):
            print(space + "both_teams_to_score_1st_half__2nd_half_yes_no_perc: " + str(both_teams_to_score_1st_half__2nd_half_yes_no_data) + " __ " + both_teams_to_score_1st_half__2nd_half_yes_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_to_score_1st_half__2nd_half_no_yes_perc = str(both_teams_to_score_1st_half__2nd_half_no_yes_data / total_rows * 100)
        if(float(both_teams_to_score_1st_half__2nd_half_no_yes_perc) >= 80  ):
            print(space + "both_teams_to_score_1st_half__2nd_half_no_yes_perc: " + str(both_teams_to_score_1st_half__2nd_half_no_yes_data) + " __ " + both_teams_to_score_1st_half__2nd_half_no_yes_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------
        both_teams_to_score_1st_half__2nd_half_no_no_perc = str(both_teams_to_score_1st_half__2nd_half_no_no_data / total_rows * 100)
        if(float(both_teams_to_score_1st_half__2nd_half_no_no_perc) >= 80  ):
            print(space + "both_teams_to_score_1st_half__2nd_half_no_no_perc: " + str(both_teams_to_score_1st_half__2nd_half_no_no_data) + " __ " + both_teams_to_score_1st_half__2nd_half_no_no_perc, flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------  
        # ------------------------------------------------------
        # last_corner_home_perc = str(last_corner_home_data / total_rows * 100)
        # if(float(last_corner_home_perc) >= 80  ):
        #     print(space + "last_corner_home_perc: " + str(last_corner_home_data) + " __ " + last_corner_home_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # last_corner_away_perc = str(last_corner_away_data / total_rows * 100)
        # if(float(last_corner_away_perc) >= 80  ):
        #     print(space + "last_corner_away_perc: " + str(last_corner_away_data) + " __ " + last_corner_away_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_corner_home_perc = str(first_corner_home_data / total_rows * 100)
        # if(float(first_corner_home_perc) >= 80  ):
        #     print(space + "first_corner_home_perc: " + str(first_corner_home_data) + " __ " + first_corner_home_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_corner_away_perc = str(first_corner_away_data / total_rows * 100)
        # if(float(first_corner_away_perc) >= 80  ):
        #     print(space + "first_corner_away_perc: " + str(first_corner_away_data) + " __ " + first_corner_away_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_home_plus_0_perc = str(cards_european_handicap_home_plus_0_data / total_rows * 100)
        # if(float(cards_european_handicap_home_plus_0_perc) >= 80  ):
        #     print(space + "cards_european_handicap_home_plus_0_perc: " + str(cards_european_handicap_home_plus_0_data) + " __ " + cards_european_handicap_home_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_away_plus_0_perc = str(cards_european_handicap_away_plus_0_data / total_rows * 100)
        # if(float(cards_european_handicap_away_plus_0_perc) >= 80  ):
        #     print(space + "cards_european_handicap_away_plus_0_perc: " + str(cards_european_handicap_away_plus_0_data) + " __ " + cards_european_handicap_away_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_draw_plus_0_perc = str(cards_european_handicap_draw_plus_0_data / total_rows * 100)
        # if(float(cards_european_handicap_draw_plus_0_perc) >= 80  ):
        #     print(space + "cards_european_handicap_draw_plus_0_perc: " + str(cards_european_handicap_draw_plus_0_data) + " __ " + cards_european_handicap_draw_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_home_min_1_perc = str(cards_european_handicap_home_min_1_data / total_rows * 100)
        # if(float(cards_european_handicap_home_min_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_home_min_1_perc: " + str(cards_european_handicap_home_min_1_data) + " __ " + cards_european_handicap_home_min_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_away_min_1_perc = str(cards_european_handicap_away_min_1_data / total_rows * 100)
        # if(float(cards_european_handicap_away_min_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_away_min_1_perc: " + str(cards_european_handicap_away_min_1_data) + " __ " + cards_european_handicap_away_min_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_draw_min_1_perc = str(cards_european_handicap_draw_min_1_data / total_rows * 100)
        # if(float(cards_european_handicap_draw_min_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_draw_min_1_perc: " + str(cards_european_handicap_draw_min_1_data) + " __ " + cards_european_handicap_draw_min_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_home_plus_1_perc = str(cards_european_handicap_home_plus_1_data / total_rows * 100)
        # if(float(cards_european_handicap_home_plus_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_home_plus_1_perc: " + str(cards_european_handicap_home_plus_1_data) + " __ " + cards_european_handicap_home_plus_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_away_plus_1_perc = str(cards_european_handicap_away_plus_1_data / total_rows * 100)
        # if(float(cards_european_handicap_away_plus_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_away_plus_1_perc: " + str(cards_european_handicap_away_plus_1_data) + " __ " + cards_european_handicap_away_plus_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_draw_plus_1_perc = str(cards_european_handicap_draw_plus_1_data / total_rows * 100)
        # if(float(cards_european_handicap_draw_plus_1_perc) >= 80  ):
        #     print(space + "cards_european_handicap_draw_plus_1_perc: " + str(cards_european_handicap_draw_plus_1_data) + " __ " + cards_european_handicap_draw_plus_1_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_home_plus_2_perc = str(cards_european_handicap_home_plus_2_data / total_rows * 100)
        # if(float(cards_european_handicap_home_plus_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_home_plus_2_perc: " + str(cards_european_handicap_home_plus_2_data) + " __ " + cards_european_handicap_home_plus_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_draw_plus_2_perc = str(cards_european_handicap_draw_plus_2_data / total_rows * 100)
        # if(float(cards_european_handicap_draw_plus_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_draw_plus_2_perc: " + str(cards_european_handicap_draw_plus_2_data) + " __ " + cards_european_handicap_draw_plus_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_away_plus_2_perc = str(cards_european_handicap_away_plus_2_data / total_rows * 100)
        # if(float(cards_european_handicap_away_plus_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_away_plus_2_perc: " + str(cards_european_handicap_away_plus_2_data) + " __ " + cards_european_handicap_away_plus_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_home_min_2_perc = str(cards_european_handicap_home_min_2_data / total_rows * 100)
        # if(float(cards_european_handicap_home_min_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_home_min_2_perc: " + str(cards_european_handicap_home_min_2_data) + " __ " + cards_european_handicap_home_min_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_draw_min_2_perc = str(cards_european_handicap_draw_min_2_data / total_rows * 100)
        # if(float(cards_european_handicap_draw_min_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_draw_min_2_perc: " + str(cards_european_handicap_draw_min_2_data) + " __ " + cards_european_handicap_draw_min_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_european_handicap_away_min_2_perc = str(cards_european_handicap_away_min_2_data / total_rows * 100)
        # if(float(cards_european_handicap_away_min_2_perc) >= 80  ):
        #     print(space + "cards_european_handicap_away_min_2_perc: " + str(cards_european_handicap_away_min_2_data) + " __ " + cards_european_handicap_away_min_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_35_perc = str(cards_overunder_over_35_data / total_rows * 100)
        # if(float(cards_overunder_over_35_perc) >= 80  ):
        #     print(space + "cards_overunder_over_35_perc: " + str(cards_overunder_over_35_data) + " __ " + cards_overunder_over_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_35_perc = str(cards_overunder_under_35_data / total_rows * 100)
        # if(float(cards_overunder_under_35_perc) >= 80  ):
        #     print(space + "cards_overunder_under_35_perc: " + str(cards_overunder_under_35_data) + " __ " + cards_overunder_under_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_45_perc = str(cards_overunder_over_45_data / total_rows * 100)
        # if(float(cards_overunder_over_45_perc) >= 80  ):
        #     print(space + "cards_overunder_over_45_perc: " + str(cards_overunder_over_45_data) + " __ " + cards_overunder_over_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_45_perc = str(cards_overunder_under_45_data / total_rows * 100)
        # if(float(cards_overunder_under_45_perc) >= 80  ):
        #     print(space + "cards_overunder_under_45_perc: " + str(cards_overunder_under_45_data) + " __ " + cards_overunder_under_45_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_55_perc = str(cards_overunder_over_55_data / total_rows * 100)
        # if(float(cards_overunder_over_55_perc) >= 80  ):
        #     print(space + "cards_overunder_over_55_perc: " + str(cards_overunder_over_55_data) + " __ " + cards_overunder_over_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_55_perc = str(cards_overunder_under_55_data / total_rows * 100)
        # if(float(cards_overunder_under_55_perc) >= 80  ):
        #     print(space + "cards_overunder_under_55_perc: " + str(cards_overunder_under_55_data) + " __ " + cards_overunder_under_55_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_65_perc = str(cards_overunder_over_65_data / total_rows * 100)
        # if(float(cards_overunder_over_65_perc) >= 80  ):
        #     print(space + "cards_overunder_over_65_perc: " + str(cards_overunder_over_65_data) + " __ " + cards_overunder_over_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_65_perc = str(cards_overunder_under_65_data / total_rows * 100)
        # if(float(cards_overunder_under_65_perc) >= 80  ):
        #     print(space + "cards_overunder_under_65_perc: " + str(cards_overunder_under_65_data) + " __ " + cards_overunder_under_65_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_75_perc = str(cards_overunder_over_75_data / total_rows * 100)
        # if(float(cards_overunder_over_75_perc) >= 80  ):
        #     print(space + "cards_overunder_over_75_perc: " + str(cards_overunder_over_75_data) + " __ " + cards_overunder_over_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_75_perc = str(cards_overunder_under_75_data / total_rows * 100)
        # if(float(cards_overunder_under_75_perc) >= 80  ):
        #     print(space + "cards_overunder_under_75_perc: " + str(cards_overunder_under_75_data) + " __ " + cards_overunder_under_75_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_over_25_perc = str(cards_overunder_over_25_data / total_rows * 100)
        # if(float(cards_overunder_over_25_perc) >= 80  ):
        #     print(space + "cards_overunder_over_25_perc: " + str(cards_overunder_over_25_data) + " __ " + cards_overunder_over_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_overunder_under_25_perc = str(cards_overunder_under_25_data / total_rows * 100)
        # if(float(cards_overunder_under_25_perc) >= 80  ):
        #     print(space + "cards_overunder_under_25_perc: " + str(cards_overunder_under_25_data) + " __ " + cards_overunder_under_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_home_plus_0_perc = str(cards_asian_handicap_home_plus_0_data / total_rows * 100)
        # if(float(cards_asian_handicap_home_plus_0_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_home_plus_0_perc: " + str(cards_asian_handicap_home_plus_0_data) + " __ " + cards_asian_handicap_home_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_away_plus_0_perc = str(cards_asian_handicap_away_plus_0_data / total_rows * 100)
        # if(float(cards_asian_handicap_away_plus_0_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_away_plus_0_perc: " + str(cards_asian_handicap_away_plus_0_data) + " __ " + cards_asian_handicap_away_plus_0_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_home_plus_05_perc = str(cards_asian_handicap_home_plus_05_data / total_rows * 100)
        # if(float(cards_asian_handicap_home_plus_05_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_home_plus_05_perc: " + str(cards_asian_handicap_home_plus_05_data) + " __ " + cards_asian_handicap_home_plus_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_away_plus_05_perc = str(cards_asian_handicap_away_plus_05_data / total_rows * 100)
        # if(float(cards_asian_handicap_away_plus_05_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_away_plus_05_perc: " + str(cards_asian_handicap_away_plus_05_data) + " __ " + cards_asian_handicap_away_plus_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_home_min_05_perc = str(cards_asian_handicap_home_min_05_data / total_rows * 100)
        # if(float(cards_asian_handicap_home_min_05_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_home_min_05_perc: " + str(cards_asian_handicap_home_min_05_data) + " __ " + cards_asian_handicap_home_min_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # cards_asian_handicap_away_min_05_perc = str(cards_asian_handicap_away_min_05_data / total_rows * 100)
        # if(float(cards_asian_handicap_away_min_05_perc) >= 80  ):
        #     print(space + "cards_asian_handicap_away_min_05_perc: " + str(cards_asian_handicap_away_min_05_data) + " __ " + cards_asian_handicap_away_min_05_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_over_25_perc = str(home_team_total_cards_over_25_data / total_rows * 100)
        # if(float(home_team_total_cards_over_25_perc) >= 80  ):
        #     print(space + "home_team_total_cards_over_25_perc: " + str(home_team_total_cards_over_25_data) + " __ " + home_team_total_cards_over_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_under_25_perc = str(home_team_total_cards_under_25_data / total_rows * 100)
        # if(float(home_team_total_cards_under_25_perc) >= 80  ):
        #     print(space + "home_team_total_cards_under_25_perc: " + str(home_team_total_cards_under_25_data) + " __ " + home_team_total_cards_under_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_over_35_perc = str(home_team_total_cards_over_35_data / total_rows * 100)
        # if(float(home_team_total_cards_over_35_perc) >= 80  ):
        #     print(space + "home_team_total_cards_over_35_perc: " + str(home_team_total_cards_over_35_data) + " __ " + home_team_total_cards_over_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_under_35_perc = str(home_team_total_cards_under_35_data / total_rows * 100)
        # if(float(home_team_total_cards_under_35_perc) >= 80  ):
        #     print(space + "home_team_total_cards_under_35_perc: " + str(home_team_total_cards_under_35_data) + " __ " + home_team_total_cards_under_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_over_15_perc = str(home_team_total_cards_over_15_data / total_rows * 100)
        # if(float(home_team_total_cards_over_15_perc) >= 80  ):
        #     print(space + "home_team_total_cards_over_15_perc: " + str(home_team_total_cards_over_15_data) + " __ " + home_team_total_cards_over_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # home_team_total_cards_under_15_perc = str(home_team_total_cards_under_15_data / total_rows * 100)
        # if(float(home_team_total_cards_under_15_perc) >= 80  ):
        #     print(space + "home_team_total_cards_under_15_perc: " + str(home_team_total_cards_under_15_data) + " __ " + home_team_total_cards_under_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_over_25_perc = str(away_team_total_cards_over_25_data / total_rows * 100)
        # if(float(away_team_total_cards_over_25_perc) >= 80  ):
        #     print(space + "away_team_total_cards_over_25_perc: " + str(away_team_total_cards_over_25_data) + " __ " + away_team_total_cards_over_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_under_25_perc = str(away_team_total_cards_under_25_data / total_rows * 100)
        # if(float(away_team_total_cards_under_25_perc) >= 80  ):
        #     print(space + "away_team_total_cards_under_25_perc: " + str(away_team_total_cards_under_25_data) + " __ " + away_team_total_cards_under_25_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_over_35_perc = str(away_team_total_cards_over_35_data / total_rows * 100)
        # if(float(away_team_total_cards_over_35_perc) >= 80  ):
        #     print(space + "away_team_total_cards_over_35_perc: " + str(away_team_total_cards_over_35_data) + " __ " + away_team_total_cards_over_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_under_35_perc = str(away_team_total_cards_under_35_data / total_rows * 100)
        # if(float(away_team_total_cards_under_35_perc) >= 80  ):
        #     print(space + "away_team_total_cards_under_35_perc: " + str(away_team_total_cards_under_35_data) + " __ " + away_team_total_cards_under_35_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_over_15_perc = str(away_team_total_cards_over_15_data / total_rows * 100)
        # if(float(away_team_total_cards_over_15_perc) >= 80  ):
        #     print(space + "away_team_total_cards_over_15_perc: " + str(away_team_total_cards_over_15_data) + " __ " + away_team_total_cards_over_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # away_team_total_cards_under_15_perc = str(away_team_total_cards_under_15_data / total_rows * 100)
        # if(float(away_team_total_cards_under_15_perc) >= 80  ):
        #     print(space + "away_team_total_cards_under_15_perc: " + str(away_team_total_cards_under_15_data) + " __ " + away_team_total_cards_under_15_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # rcard_yes_perc = str(rcard_yes_data / total_rows * 100)
        # if(float(rcard_yes_perc) >= 80  ):
        #     print(space + "rcard_yes_perc: " + str(rcard_yes_data) + " __ " + rcard_yes_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # rcard_no_perc = str(rcard_no_data / total_rows * 100)
        # if(float(rcard_no_perc) >= 80  ):
        #     print(space + "rcard_no_perc: " + str(rcard_no_data) + " __ " + rcard_no_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # total_goals_under_2_perc = str(total_goals_under_2_data / total_rows * 100)
        # if(float(total_goals_under_2_perc) >= 80  ):
        #     print(space + "total_goals_under_2_perc: " + str(total_goals_under_2_data) + " __ " + total_goals_under_2_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # total_goals_2_or_3_perc = str(total_goals_2_or_3_data / total_rows * 100)
        # if(float(total_goals_2_or_3_perc) >= 80  ):
        #     print(space + "total_goals_2_or_3_perc: " + str(total_goals_2_or_3_data) + " __ " + total_goals_2_or_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # total_goals_over_3_perc = str(total_goals_over_3_data / total_rows * 100)
        # if(float(total_goals_over_3_perc) >= 80  ):
        #     print(space + "total_goals_over_3_perc: " + str(total_goals_over_3_data) + " __ " + total_goals_over_3_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_shot_perc = str(first_goal_method_shot_data / total_rows * 100)
        # if(float(first_goal_method_shot_perc) >= 80  ):
        #     print(space + "first_goal_method_shot_perc: " + str(first_goal_method_shot_data) + " __ " + first_goal_method_shot_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_header_perc = str(first_goal_method_header_data / total_rows * 100)
        # if(float(first_goal_method_header_perc) >= 80  ):
        #     print(space + "first_goal_method_header_perc: " + str(first_goal_method_header_data) + " __ " + first_goal_method_header_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_penalty_perc = str(first_goal_method_penalty_data / total_rows * 100)
        # if(float(first_goal_method_penalty_perc) >= 80  ):
        #     print(space + "first_goal_method_penalty_perc: " + str(first_goal_method_penalty_data) + " __ " + first_goal_method_penalty_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_freekick_perc = str(first_goal_method_freekick_data / total_rows * 100)
        # if(float(first_goal_method_freekick_perc) >= 80  ):
        #     print(space + "first_goal_method_freekick_perc: " + str(first_goal_method_freekick_data) + " __ " + first_goal_method_freekick_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_owngoal_perc = str(first_goal_method_owngoal_data / total_rows * 100)
        # if(float(first_goal_method_owngoal_perc) >= 80  ):
        #     print(space + "first_goal_method_owngoal_perc: " + str(first_goal_method_owngoal_data) + " __ " + first_goal_method_owngoal_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # first_goal_method_draw_perc = str(first_goal_method_draw_data / total_rows * 100)
        # if(float(first_goal_method_draw_perc) >= 80  ):
        #     print(space + "first_goal_method_draw_perc: " + str(first_goal_method_draw_data) + " __ " + first_goal_method_draw_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # to_score_a_penalty_home_perc = str(to_score_a_penalty_home_data / total_rows * 100)
        # if(float(to_score_a_penalty_home_perc) >= 80  ):
        #     print(space + "to_score_a_penalty_home_perc: " + str(to_score_a_penalty_home_data) + " __ " + to_score_a_penalty_home_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # to_score_a_penalty_away_perc = str(to_score_a_penalty_away_data / total_rows * 100)
        # if(float(to_score_a_penalty_away_perc) >= 80  ):
        #     print(space + "to_score_a_penalty_away_perc: " + str(to_score_a_penalty_away_data) + " __ " + to_score_a_penalty_away_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # to_miss_a_penalty_home_perc = str(to_miss_a_penalty_home_data / total_rows * 100)
        # if(float(to_miss_a_penalty_home_perc) >= 80  ):
        #     print(space + "to_miss_a_penalty_home_perc: " + str(to_miss_a_penalty_home_data) + " __ " + to_miss_a_penalty_home_perc, flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # # ------------------------------------------------------
        # to_miss_a_penalty_away_perc = str(to_miss_a_penalty_away_data / total_rows * 100)
        # if(float(to_miss_a_penalty_away_perc) >= 80  ):
        #     print(space + "to_miss_a_penalty_away_perc: " + str(to_miss_a_penalty_away_data) + " __ " + to_miss_a_penalty_away_perc, flush=True)
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        # ------------------------------------------------------
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------
        query_commit = " INSERT INTO `"+TABLE+"`( " 
        # ------------------------------------------------------
        if(type_of_pattern == 1):
            query_commit += " `leagueapi_id`, " 
        if(type_of_pattern == 2):
            query_commit += " `country`, " 
        # ------------------------------------------------------
        query_commit += " `total_fixtures`, " 
        # ------------------------------------------------------
        query_commit += " `pre_ah_pattern`, " 
        query_commit += " `pre_gou_pattern`, " 
        # ------------------------------------------------------
        query_commit += " `end_ah_pattern`, " 
        query_commit += " `end_gou_pattern`, " 
        # ------------------------------------------------------
        query_commit += " `match_winner_home_data`, " 
        query_commit += " `match_winner_home_perc`, " 
        query_commit += " `match_winner_draw_data`, " 
        query_commit += " `match_winner_draw_perc`, " 
        query_commit += " `match_winner_away_data`, " 
        query_commit += " `match_winner_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `homeaway_home_data`, " 
        query_commit += " `homeaway_home_perc`, " 
        query_commit += " `homeaway_away_data`, " 
        query_commit += " `homeaway_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `second_half_winner_home_data`, " 
        query_commit += " `second_half_winner_home_perc`, " 
        query_commit += " `second_half_winner_draw_data`, " 
        query_commit += " `second_half_winner_draw_perc`, " 
        query_commit += " `second_half_winner_away_data`, " 
        query_commit += " `second_half_winner_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `asian_handicap_home_min_65_data`, " 
        query_commit += " `asian_handicap_home_min_65_perc`, " 
        query_commit += " `asian_handicap_away_min_65_data`, " 
        query_commit += " `asian_handicap_away_min_65_perc`, " 
        query_commit += " `asian_handicap_home_min_6_data`, " 
        query_commit += " `asian_handicap_home_min_6_perc`, " 
        query_commit += " `asian_handicap_away_min_6_data`, " 
        query_commit += " `asian_handicap_away_min_6_perc`, " 
        query_commit += " `asian_handicap_home_min_55_data`, " 
        query_commit += " `asian_handicap_home_min_55_perc`, " 
        query_commit += " `asian_handicap_away_min_55_data`, " 
        query_commit += " `asian_handicap_away_min_55_perc`, " 
        query_commit += " `asian_handicap_home_min_5_data`, " 
        query_commit += " `asian_handicap_home_min_5_perc`, " 
        query_commit += " `asian_handicap_away_min_5_data`, " 
        query_commit += " `asian_handicap_away_min_5_perc`, " 
        query_commit += " `asian_handicap_home_min_45_data`, " 
        query_commit += " `asian_handicap_home_min_45_perc`, " 
        query_commit += " `asian_handicap_away_min_45_data`, " 
        query_commit += " `asian_handicap_away_min_45_perc`, " 
        query_commit += " `asian_handicap_home_min_4_data`, " 
        query_commit += " `asian_handicap_home_min_4_perc`, " 
        query_commit += " `asian_handicap_away_min_4_data`, " 
        query_commit += " `asian_handicap_away_min_4_perc`, " 
        query_commit += " `asian_handicap_home_min_35_data`, " 
        query_commit += " `asian_handicap_home_min_35_perc`, " 
        query_commit += " `asian_handicap_away_min_35_data`, " 
        query_commit += " `asian_handicap_away_min_35_perc`, " 
        query_commit += " `asian_handicap_home_min_3_data`, " 
        query_commit += " `asian_handicap_home_min_3_perc`, " 
        query_commit += " `asian_handicap_away_min_3_data`, " 
        query_commit += " `asian_handicap_away_min_3_perc`, " 
        query_commit += " `asian_handicap_home_min_25_data`, " 
        query_commit += " `asian_handicap_home_min_25_perc`, " 
        query_commit += " `asian_handicap_away_min_25_data`, " 
        query_commit += " `asian_handicap_away_min_25_perc`, " 
        query_commit += " `asian_handicap_home_min_2_data`, " 
        query_commit += " `asian_handicap_home_min_2_perc`, " 
        query_commit += " `asian_handicap_away_min_2_data`, " 
        query_commit += " `asian_handicap_away_min_2_perc`, " 
        query_commit += " `asian_handicap_home_min_15_data`, " 
        query_commit += " `asian_handicap_home_min_15_perc`, " 
        query_commit += " `asian_handicap_away_min_15_data`, " 
        query_commit += " `asian_handicap_away_min_15_perc`, " 
        query_commit += " `asian_handicap_home_min_1_data`, " 
        query_commit += " `asian_handicap_home_min_1_perc`, " 
        query_commit += " `asian_handicap_away_min_1_data`, " 
        query_commit += " `asian_handicap_away_min_1_perc`, " 
        query_commit += " `asian_handicap_home_min_05_data`, " 
        query_commit += " `asian_handicap_home_min_05_perc`, " 
        query_commit += " `asian_handicap_away_min_05_data`, " 
        query_commit += " `asian_handicap_away_min_05_perc`, " 
        query_commit += " `asian_handicap_home_plus_0_data`, " 
        query_commit += " `asian_handicap_home_plus_0_perc`, " 
        query_commit += " `asian_handicap_away_plus_0_data`, " 
        query_commit += " `asian_handicap_away_plus_0_perc`, " 
        query_commit += " `asian_handicap_home_plus_05_data`, " 
        query_commit += " `asian_handicap_home_plus_05_perc`, " 
        query_commit += " `asian_handicap_away_plus_05_data`, " 
        query_commit += " `asian_handicap_away_plus_05_perc`, " 
        query_commit += " `asian_handicap_home_plus_1_data`, " 
        query_commit += " `asian_handicap_home_plus_1_perc`, " 
        query_commit += " `asian_handicap_away_plus_1_data`, " 
        query_commit += " `asian_handicap_away_plus_1_perc`, " 
        query_commit += " `asian_handicap_home_plus_15_data`, " 
        query_commit += " `asian_handicap_home_plus_15_perc`, " 
        query_commit += " `asian_handicap_away_plus_15_data`, " 
        query_commit += " `asian_handicap_away_plus_15_perc`, " 
        query_commit += " `asian_handicap_home_plus_2_data`, " 
        query_commit += " `asian_handicap_home_plus_2_perc`, " 
        query_commit += " `asian_handicap_away_plus_2_data`, " 
        query_commit += " `asian_handicap_away_plus_2_perc`, " 
        query_commit += " `asian_handicap_home_plus_25_data`, " 
        query_commit += " `asian_handicap_home_plus_25_perc`, " 
        query_commit += " `asian_handicap_away_plus_25_data`, " 
        query_commit += " `asian_handicap_away_plus_25_perc`, " 
        query_commit += " `asian_handicap_home_plus_3_data`, " 
        query_commit += " `asian_handicap_home_plus_3_perc`, " 
        query_commit += " `asian_handicap_away_plus_3_data`, " 
        query_commit += " `asian_handicap_away_plus_3_perc`, " 
        query_commit += " `asian_handicap_home_plus_35_data`, " 
        query_commit += " `asian_handicap_home_plus_35_perc`, " 
        query_commit += " `asian_handicap_away_plus_35_data`, " 
        query_commit += " `asian_handicap_away_plus_35_perc`, " 
        query_commit += " `asian_handicap_home_plus_4_data`, " 
        query_commit += " `asian_handicap_home_plus_4_perc`, " 
        query_commit += " `asian_handicap_away_plus_4_data`, " 
        query_commit += " `asian_handicap_away_plus_4_perc`, " 
        query_commit += " `asian_handicap_home_plus_45_data`, " 
        query_commit += " `asian_handicap_home_plus_45_perc`, " 
        query_commit += " `asian_handicap_away_plus_45_data`, " 
        query_commit += " `asian_handicap_away_plus_45_perc`, " 
        query_commit += " `asian_handicap_home_plus_5_data`, " 
        query_commit += " `asian_handicap_home_plus_5_perc`, " 
        query_commit += " `asian_handicap_away_plus_5_data`, " 
        query_commit += " `asian_handicap_away_plus_5_perc`, " 
        query_commit += " `asian_handicap_home_plus_55_data`, " 
        query_commit += " `asian_handicap_home_plus_55_perc`, " 
        query_commit += " `asian_handicap_away_plus_55_data`, " 
        query_commit += " `asian_handicap_away_plus_55_perc`, " 
        query_commit += " `asian_handicap_home_plus_6_data`, " 
        query_commit += " `asian_handicap_home_plus_6_perc`, " 
        query_commit += " `asian_handicap_away_plus_6_data`, " 
        query_commit += " `asian_handicap_away_plus_6_perc`, " 
        query_commit += " `asian_handicap_home_plus_65_data`, " 
        query_commit += " `asian_handicap_home_plus_65_perc`, " 
        query_commit += " `asian_handicap_away_plus_65_data`, " 
        query_commit += " `asian_handicap_away_plus_65_perc`, " 
        # ------------------------------------------------------
        query_commit += " `goals_overunder_over_05_data`, " 
        query_commit += " `goals_overunder_over_05_perc`, " 
        query_commit += " `goals_overunder_under_05_data`, " 
        query_commit += " `goals_overunder_under_05_perc`, " 
        query_commit += " `goals_overunder_over_10_data`, " 
        query_commit += " `goals_overunder_over_10_perc`, " 
        query_commit += " `goals_overunder_under_10_data`, " 
        query_commit += " `goals_overunder_under_10_perc`, " 
        query_commit += " `goals_overunder_over_15_data`, " 
        query_commit += " `goals_overunder_over_15_perc`, " 
        query_commit += " `goals_overunder_under_15_data`, " 
        query_commit += " `goals_overunder_under_15_perc`, " 
        query_commit += " `goals_overunder_over_20_data`, " 
        query_commit += " `goals_overunder_over_20_perc`, " 
        query_commit += " `goals_overunder_under_20_data`, " 
        query_commit += " `goals_overunder_under_20_perc`, " 
        query_commit += " `goals_overunder_over_25_data`, " 
        query_commit += " `goals_overunder_over_25_perc`, " 
        query_commit += " `goals_overunder_under_25_data`, " 
        query_commit += " `goals_overunder_under_25_perc`, " 
        query_commit += " `goals_overunder_over_30_data`, " 
        query_commit += " `goals_overunder_over_30_perc`, " 
        query_commit += " `goals_overunder_under_30_data`, " 
        query_commit += " `goals_overunder_under_30_perc`, " 
        query_commit += " `goals_overunder_over_35_data`, " 
        query_commit += " `goals_overunder_over_35_perc`, " 
        query_commit += " `goals_overunder_under_35_data`, " 
        query_commit += " `goals_overunder_under_35_perc`, " 
        query_commit += " `goals_overunder_over_40_data`, " 
        query_commit += " `goals_overunder_over_40_perc`, " 
        query_commit += " `goals_overunder_under_40_data`, " 
        query_commit += " `goals_overunder_under_40_perc`, " 
        query_commit += " `goals_overunder_over_45_data`, " 
        query_commit += " `goals_overunder_over_45_perc`, " 
        query_commit += " `goals_overunder_under_45_data`, " 
        query_commit += " `goals_overunder_under_45_perc`, " 
        query_commit += " `goals_overunder_over_50_data`, " 
        query_commit += " `goals_overunder_over_50_perc`, " 
        query_commit += " `goals_overunder_under_50_data`, " 
        query_commit += " `goals_overunder_under_50_perc`, " 
        query_commit += " `goals_overunder_over_55_data`, " 
        query_commit += " `goals_overunder_over_55_perc`, " 
        query_commit += " `goals_overunder_under_55_data`, " 
        query_commit += " `goals_overunder_under_55_perc`, " 
        query_commit += " `goals_overunder_over_60_data`, " 
        query_commit += " `goals_overunder_over_60_perc`, " 
        query_commit += " `goals_overunder_under_60_data`, " 
        query_commit += " `goals_overunder_under_60_perc`, " 
        query_commit += " `goals_overunder_over_65_data`, " 
        query_commit += " `goals_overunder_over_65_perc`, " 
        query_commit += " `goals_overunder_under_65_data`, " 
        query_commit += " `goals_overunder_under_65_perc`, " 
        query_commit += " `goals_overunder_over_70_data`, " 
        query_commit += " `goals_overunder_over_70_perc`, " 
        query_commit += " `goals_overunder_under_70_data`, " 
        query_commit += " `goals_overunder_under_70_perc`, " 
        query_commit += " `goals_overunder_over_75_data`, " 
        query_commit += " `goals_overunder_over_75_perc`, " 
        query_commit += " `goals_overunder_under_75_data`, " 
        query_commit += " `goals_overunder_under_75_perc`, " 
        query_commit += " `goals_overunder_over_85_data`, " 
        query_commit += " `goals_overunder_over_85_perc`, " 
        query_commit += " `goals_overunder_under_85_data`, " 
        query_commit += " `goals_overunder_under_85_perc`, " 
        query_commit += " `goals_overunder_over_95_data`, " 
        query_commit += " `goals_overunder_over_95_perc`, " 
        query_commit += " `goals_overunder_under_95_data`, " 
        query_commit += " `goals_overunder_under_95_perc`, " 
        # ------------------------------------------------------
        query_commit += " `goals_overunder_first_half_over_05_data`, " 
        query_commit += " `goals_overunder_first_half_over_05_perc`, " 
        query_commit += " `goals_overunder_first_half_under_05_data`, " 
        query_commit += " `goals_overunder_first_half_under_05_perc`, " 
        query_commit += " `goals_overunder_first_half_over_10_data`, " 
        query_commit += " `goals_overunder_first_half_over_10_perc`, " 
        query_commit += " `goals_overunder_first_half_under_10_data`, " 
        query_commit += " `goals_overunder_first_half_under_10_perc`, " 
        query_commit += " `goals_overunder_first_half_over_15_data`, " 
        query_commit += " `goals_overunder_first_half_over_15_perc`, " 
        query_commit += " `goals_overunder_first_half_under_15_data`, " 
        query_commit += " `goals_overunder_first_half_under_15_perc`, " 
        query_commit += " `goals_overunder_first_half_over_20_data`, " 
        query_commit += " `goals_overunder_first_half_over_20_perc`, " 
        query_commit += " `goals_overunder_first_half_under_20_data`, " 
        query_commit += " `goals_overunder_first_half_under_20_perc`, " 
        query_commit += " `goals_overunder_first_half_over_25_data`, " 
        query_commit += " `goals_overunder_first_half_over_25_perc`, " 
        query_commit += " `goals_overunder_first_half_under_25_data`, " 
        query_commit += " `goals_overunder_first_half_under_25_perc`, " 
        query_commit += " `goals_overunder_first_half_over_30_data`, " 
        query_commit += " `goals_overunder_first_half_over_30_perc`, " 
        query_commit += " `goals_overunder_first_half_under_30_data`, " 
        query_commit += " `goals_overunder_first_half_under_30_perc`, " 
        query_commit += " `goals_overunder_first_half_over_35_data`, " 
        query_commit += " `goals_overunder_first_half_over_35_perc`, " 
        query_commit += " `goals_overunder_first_half_under_35_data`, " 
        query_commit += " `goals_overunder_first_half_under_35_perc`, " 
        # ------------------------------------------------------
        query_commit += " `htft_double_home_home_data`, " 
        query_commit += " `htft_double_home_home_perc`, " 
        query_commit += " `htft_double_home_draw_data`, " 
        query_commit += " `htft_double_home_draw_perc`, " 
        query_commit += " `htft_double_home_away_data`, " 
        query_commit += " `htft_double_home_away_perc`, " 
        query_commit += " `htft_double_draw_home_data`, " 
        query_commit += " `htft_double_draw_home_perc`, " 
        query_commit += " `htft_double_draw_draw_data`, " 
        query_commit += " `htft_double_draw_draw_perc`, " 
        query_commit += " `htft_double_draw_away_data`, " 
        query_commit += " `htft_double_draw_away_perc`, " 
        query_commit += " `htft_double_away_home_data`, " 
        query_commit += " `htft_double_away_home_perc`, " 
        query_commit += " `htft_double_away_draw_data`, " 
        query_commit += " `htft_double_away_draw_perc`, " 
        query_commit += " `htft_double_away_away_data`, " 
        query_commit += " `htft_double_away_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `both_teams_score_yes_data`, " 
        query_commit += " `both_teams_score_yes_perc`, " 
        query_commit += " `both_teams_score_no_data`, " 
        query_commit += " `both_teams_score_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `highest_scoring_half_first_data`, " 
        query_commit += " `highest_scoring_half_first_perc`, " 
        query_commit += " `highest_scoring_half_draw_data`, " 
        query_commit += " `highest_scoring_half_draw_perc`, " 
        query_commit += " `highest_scoring_half_second_data`, " 
        query_commit += " `highest_scoring_half_second_perc`, " 
        # ------------------------------------------------------
        query_commit += " `double_chance_home_draw_data`, " 
        query_commit += " `double_chance_home_draw_perc`, " 
        query_commit += " `double_chance_home_away_data`, " 
        query_commit += " `double_chance_home_away_perc`, " 
        query_commit += " `double_chance_draw_away_data`, " 
        query_commit += " `double_chance_draw_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `first_half_winner_home_data`, " 
        query_commit += " `first_half_winner_home_perc`, " 
        query_commit += " `first_half_winner_draw_data`, " 
        query_commit += " `first_half_winner_draw_perc`, " 
        query_commit += " `first_half_winner_away_data`, " 
        query_commit += " `first_half_winner_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `total_home_over_15_data`, " 
        query_commit += " `total_home_over_15_perc`, " 
        query_commit += " `total_home_under_15_data`, " 
        query_commit += " `total_home_under_15_perc`, " 
        query_commit += " `total_home_over_25_data`, " 
        query_commit += " `total_home_over_25_perc`, " 
        query_commit += " `total_home_under_25_data`, " 
        query_commit += " `total_home_under_25_perc`, " 
        query_commit += " `total_home_over_35_data`, " 
        query_commit += " `total_home_over_35_perc`, " 
        query_commit += " `total_home_under_35_data`, " 
        query_commit += " `total_home_under_35_perc`, " 
        query_commit += " `total_home_over_45_data`, " 
        query_commit += " `total_home_over_45_perc`, " 
        query_commit += " `total_home_under_45_data`, " 
        query_commit += " `total_home_under_45_perc`, " 
        query_commit += " `total_home_over_55_data`, " 
        query_commit += " `total_home_over_55_perc`, " 
        query_commit += " `total_home_under_55_data`, " 
        query_commit += " `total_home_under_55_perc`, " 
        query_commit += " `total_home_over_65_data`, " 
        query_commit += " `total_home_over_65_perc`, " 
        query_commit += " `total_home_under_65_data`, " 
        query_commit += " `total_home_under_65_perc`, " 
        # ------------------------------------------------------
        query_commit += " `total_away_over_15_data`, " 
        query_commit += " `total_away_over_15_perc`, " 
        query_commit += " `total_away_under_15_data`, " 
        query_commit += " `total_away_under_15_perc`, " 
        query_commit += " `total_away_over_25_data`, " 
        query_commit += " `total_away_over_25_perc`, " 
        query_commit += " `total_away_under_25_data`, " 
        query_commit += " `total_away_under_25_perc`, " 
        query_commit += " `total_away_over_35_data`, " 
        query_commit += " `total_away_over_35_perc`, " 
        query_commit += " `total_away_under_35_data`, " 
        query_commit += " `total_away_under_35_perc`, " 
        query_commit += " `total_away_over_45_data`, " 
        query_commit += " `total_away_over_45_perc`, " 
        query_commit += " `total_away_under_45_data`, " 
        query_commit += " `total_away_under_45_perc`, " 
        query_commit += " `total_away_over_55_data`, " 
        query_commit += " `total_away_over_55_perc`, " 
        query_commit += " `total_away_under_55_data`, " 
        query_commit += " `total_away_under_55_perc`, " 
        query_commit += " `total_away_over_65_data`, " 
        query_commit += " `total_away_over_65_perc`, " 
        query_commit += " `total_away_under_65_data`, " 
        query_commit += " `total_away_under_65_perc`, " 
        # ------------------------------------------------------
        query_commit += " `asian_handicap_first_half_home_min_15_data`, " 
        query_commit += " `asian_handicap_first_half_home_min_15_perc`, " 
        query_commit += " `asian_handicap_first_half_away_min_15_data`, " 
        query_commit += " `asian_handicap_first_half_away_min_15_perc`, " 
        query_commit += " `asian_handicap_first_half_home_min_1_data`, " 
        query_commit += " `asian_handicap_first_half_home_min_1_perc`, " 
        query_commit += " `asian_handicap_first_half_away_min_1_data`, " 
        query_commit += " `asian_handicap_first_half_away_min_1_perc`, " 
        query_commit += " `asian_handicap_first_half_home_min_05_data`, " 
        query_commit += " `asian_handicap_first_half_home_min_05_perc`, " 
        query_commit += " `asian_handicap_first_half_away_min_05_data`, " 
        query_commit += " `asian_handicap_first_half_away_min_05_perc`, " 
        query_commit += " `asian_handicap_first_half_home_plus_0_data`, " 
        query_commit += " `asian_handicap_first_half_home_plus_0_perc`, " 
        query_commit += " `asian_handicap_first_half_away_plus_0_data`, " 
        query_commit += " `asian_handicap_first_half_away_plus_0_perc`, " 
        query_commit += " `asian_handicap_first_half_home_plus_05_data`, " 
        query_commit += " `asian_handicap_first_half_home_plus_05_perc`, " 
        query_commit += " `asian_handicap_first_half_away_plus_05_data`, " 
        query_commit += " `asian_handicap_first_half_away_plus_05_perc`, " 
        query_commit += " `asian_handicap_first_half_home_plus_1_data`, " 
        query_commit += " `asian_handicap_first_half_home_plus_1_perc`, " 
        query_commit += " `asian_handicap_first_half_away_plus_1_data`, " 
        query_commit += " `asian_handicap_first_half_away_plus_1_perc`, " 
        query_commit += " `asian_handicap_first_half_home_plus_15_data`, " 
        query_commit += " `asian_handicap_first_half_home_plus_15_perc`, " 
        query_commit += " `asian_handicap_first_half_away_plus_15_data`, " 
        query_commit += " `asian_handicap_first_half_away_plus_15_perc`, " 
        # ------------------------------------------------------
        query_commit += " `double_chance__first_half_home_draw_data`, " 
        query_commit += " `double_chance__first_half_home_draw_perc`, " 
        query_commit += " `double_chance__first_half_home_away_data`, " 
        query_commit += " `double_chance__first_half_home_away_perc`, " 
        query_commit += " `double_chance__first_half_draw_away_data`, " 
        query_commit += " `double_chance__first_half_draw_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `oddeven_odd_data`, " 
        query_commit += " `oddeven_odd_perc`, " 
        query_commit += " `oddeven_even_data`, " 
        query_commit += " `oddeven_even_perc`, " 
        # ------------------------------------------------------
        query_commit += " `results_both_teams_score_home_yes_data`, " 
        query_commit += " `results_both_teams_score_home_yes_perc`, " 
        query_commit += " `results_both_teams_score_draw_yes_data`, " 
        query_commit += " `results_both_teams_score_draw_yes_perc`, " 
        query_commit += " `results_both_teams_score_away_yes_data`, " 
        query_commit += " `results_both_teams_score_away_yes_perc`, " 
        query_commit += " `results_both_teams_score_home_no_data`, " 
        query_commit += " `results_both_teams_score_home_no_perc`, " 
        query_commit += " `results_both_teams_score_draw_no_data`, " 
        query_commit += " `results_both_teams_score_draw_no_perc`, " 
        query_commit += " `results_both_teams_score_away_no_data`, " 
        query_commit += " `results_both_teams_score_away_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `result_total_goals_home_over_35_data`, " 
        query_commit += " `result_total_goals_home_over_35_perc`, " 
        query_commit += " `result_total_goals_draw_over_35_data`, " 
        query_commit += " `result_total_goals_draw_over_35_perc`, " 
        query_commit += " `result_total_goals_away_over_35_data`, " 
        query_commit += " `result_total_goals_away_over_35_perc`, " 
        query_commit += " `result_total_goals_home_under_35_data`, " 
        query_commit += " `result_total_goals_home_under_35_perc`, " 
        query_commit += " `result_total_goals_draw_under_35_data`, " 
        query_commit += " `result_total_goals_draw_under_35_perc`, " 
        query_commit += " `result_total_goals_away_under_35_data`, " 
        query_commit += " `result_total_goals_away_under_35_perc`, " 
        query_commit += " `result_total_goals_home_over_25_data`, " 
        query_commit += " `result_total_goals_home_over_25_perc`, " 
        query_commit += " `result_total_goals_draw_over_25_data`, " 
        query_commit += " `result_total_goals_draw_over_25_perc`, " 
        query_commit += " `result_total_goals_away_over_25_data`, " 
        query_commit += " `result_total_goals_away_over_25_perc`, " 
        query_commit += " `result_total_goals_home_under_25_data`, " 
        query_commit += " `result_total_goals_home_under_25_perc`, " 
        query_commit += " `result_total_goals_draw_under_25_data`, " 
        query_commit += " `result_total_goals_draw_under_25_perc`, " 
        query_commit += " `result_total_goals_away_under_25_data`, " 
        query_commit += " `result_total_goals_away_under_25_perc`, " 
        # ------------------------------------------------------
        query_commit += " `goals_overunder__second_half_over_05_data`, " 
        query_commit += " `goals_overunder__second_half_over_05_perc`, " 
        query_commit += " `goals_overunder__second_half_under_05_data`, " 
        query_commit += " `goals_overunder__second_half_under_05_perc`, " 
        query_commit += " `goals_overunder__second_half_over_10_data`, " 
        query_commit += " `goals_overunder__second_half_over_10_perc`, " 
        query_commit += " `goals_overunder__second_half_under_10_data`, " 
        query_commit += " `goals_overunder__second_half_under_10_perc`, " 
        query_commit += " `goals_overunder__second_half_over_15_data`, " 
        query_commit += " `goals_overunder__second_half_over_15_perc`, " 
        query_commit += " `goals_overunder__second_half_under_15_data`, " 
        query_commit += " `goals_overunder__second_half_under_15_perc`, " 
        query_commit += " `goals_overunder__second_half_over_20_data`, " 
        query_commit += " `goals_overunder__second_half_over_20_perc`, " 
        query_commit += " `goals_overunder__second_half_under_20_data`, " 
        query_commit += " `goals_overunder__second_half_under_20_perc`, " 
        query_commit += " `goals_overunder__second_half_over_25_data`, " 
        query_commit += " `goals_overunder__second_half_over_25_perc`, " 
        query_commit += " `goals_overunder__second_half_under_25_data`, " 
        query_commit += " `goals_overunder__second_half_under_25_perc`, " 
        query_commit += " `goals_overunder__second_half_over_30_data`, " 
        query_commit += " `goals_overunder__second_half_over_30_perc`, " 
        query_commit += " `goals_overunder__second_half_under_30_data`, " 
        query_commit += " `goals_overunder__second_half_under_30_perc`, " 
        query_commit += " `goals_overunder__second_half_over_35_data`, " 
        query_commit += " `goals_overunder__second_half_over_35_perc`, " 
        query_commit += " `goals_overunder__second_half_under_35_data`, " 
        query_commit += " `goals_overunder__second_half_under_35_perc`, " 
        # ------------------------------------------------------
        query_commit += " `clean_sheet__home_yes_data`, " 
        query_commit += " `clean_sheet__home_yes_perc`, " 
        query_commit += " `clean_sheet__home_no_data`, " 
        query_commit += " `clean_sheet__home_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `clean_sheet__away_yes_data`, " 
        query_commit += " `clean_sheet__away_yes_perc`, " 
        query_commit += " `clean_sheet__away_no_data`, " 
        query_commit += " `clean_sheet__away_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `win_both_halves_home_data`, " 
        query_commit += " `win_both_halves_home_perc`, " 
        query_commit += " `win_both_halves_away_data`, " 
        query_commit += " `win_both_halves_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `both_teams_score__first_half_yes_data`, " 
        query_commit += " `both_teams_score__first_half_yes_perc`, " 
        query_commit += " `both_teams_score__first_half_no_data`, " 
        query_commit += " `both_teams_score__first_half_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `both_teams_to_score__second_half_yes_data`, " 
        query_commit += " `both_teams_to_score__second_half_yes_perc`, " 
        query_commit += " `both_teams_to_score__second_half_no_data`, " 
        query_commit += " `both_teams_to_score__second_half_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `win_to_nil_home_data`, " 
        query_commit += " `win_to_nil_home_perc`, " 
        query_commit += " `win_to_nil_away_data`, " 
        query_commit += " `win_to_nil_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `exact_goals_number_0_data`, " 
        query_commit += " `exact_goals_number_0_perc`, " 
        query_commit += " `exact_goals_number_1_data`, " 
        query_commit += " `exact_goals_number_1_perc`, " 
        query_commit += " `exact_goals_number_2_data`, " 
        query_commit += " `exact_goals_number_2_perc`, " 
        query_commit += " `exact_goals_number_3_data`, " 
        query_commit += " `exact_goals_number_3_perc`, " 
        query_commit += " `exact_goals_number_4_data`, " 
        query_commit += " `exact_goals_number_4_perc`, " 
        query_commit += " `exact_goals_number_5_data`, " 
        query_commit += " `exact_goals_number_5_perc`, " 
        query_commit += " `exact_goals_number_6_data`, " 
        query_commit += " `exact_goals_number_6_perc`, " 
        query_commit += " `exact_goals_number_more_7_data`, " 
        query_commit += " `exact_goals_number_more_7_perc`, " 
        # ------------------------------------------------------
        query_commit += " `to_win_either_half_home_data`, " 
        query_commit += " `to_win_either_half_home_perc`, " 
        query_commit += " `to_win_either_half_away_data`, " 
        query_commit += " `to_win_either_half_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `home_team_exact_goals_number_0_data`, " 
        query_commit += " `home_team_exact_goals_number_0_perc`, " 
        query_commit += " `home_team_exact_goals_number_1_data`, " 
        query_commit += " `home_team_exact_goals_number_1_perc`, " 
        query_commit += " `home_team_exact_goals_number_2_data`, " 
        query_commit += " `home_team_exact_goals_number_2_perc`, " 
        query_commit += " `home_team_exact_goals_number_more_3_data`, " 
        query_commit += " `home_team_exact_goals_number_more_3_perc`, " 
        # ------------------------------------------------------
        query_commit += " `away_team_exact_goals_number_0_data`, " 
        query_commit += " `away_team_exact_goals_number_0_perc`, " 
        query_commit += " `away_team_exact_goals_number_1_data`, " 
        query_commit += " `away_team_exact_goals_number_1_perc`, " 
        query_commit += " `away_team_exact_goals_number_2_data`, " 
        query_commit += " `away_team_exact_goals_number_2_perc`, " 
        query_commit += " `away_team_exact_goals_number_more_3_data`, " 
        query_commit += " `away_team_exact_goals_number_more_3_perc`, " 
        # ------------------------------------------------------
        query_commit += " `second_half_exact_goals_number_0_data`, " 
        query_commit += " `second_half_exact_goals_number_0_perc`, " 
        query_commit += " `second_half_exact_goals_number_1_data`, " 
        query_commit += " `second_half_exact_goals_number_1_perc`, " 
        query_commit += " `second_half_exact_goals_number_2_data`, " 
        query_commit += " `second_half_exact_goals_number_2_perc`, " 
        query_commit += " `second_half_exact_goals_number_3_data`, " 
        query_commit += " `second_half_exact_goals_number_3_perc`, " 
        query_commit += " `second_half_exact_goals_number_4_data`, " 
        query_commit += " `second_half_exact_goals_number_4_perc`, " 
        query_commit += " `second_half_exact_goals_number_more_5_data`, " 
        query_commit += " `second_half_exact_goals_number_more_5_perc`, " 
        # ------------------------------------------------------
        query_commit += " `exact_goals_number__first_half_0_data`, " 
        query_commit += " `exact_goals_number__first_half_0_perc`, " 
        query_commit += " `exact_goals_number__first_half_1_data`, " 
        query_commit += " `exact_goals_number__first_half_1_perc`, " 
        query_commit += " `exact_goals_number__first_half_2_data`, " 
        query_commit += " `exact_goals_number__first_half_2_perc`, " 
        query_commit += " `exact_goals_number__first_half_3_data`, " 
        query_commit += " `exact_goals_number__first_half_3_perc`, " 
        query_commit += " `exact_goals_number__first_half_4_data`, " 
        query_commit += " `exact_goals_number__first_half_4_perc`, " 
        query_commit += " `exact_goals_number__first_half_more_5_data`, " 
        query_commit += " `exact_goals_number__first_half_more_5_perc`, " 
        # ------------------------------------------------------
        query_commit += " `to_score_in_both_halves_by_teams_home_data`, " 
        query_commit += " `to_score_in_both_halves_by_teams_home_perc`, " 
        query_commit += " `to_score_in_both_halves_by_teams_away_data`, " 
        query_commit += " `to_score_in_both_halves_by_teams_away_perc`, " 
        # ------------------------------------------------------
        query_commit += " `total_goals_both_teams_to_score_over_yes_25_data`, " 
        query_commit += " `total_goals_both_teams_to_score_over_yes_25_perc`, " 
        query_commit += " `total_goals_both_teams_to_score_over_no_25_data`, " 
        query_commit += " `total_goals_both_teams_to_score_over_no_25_perc`, " 
        query_commit += " `total_goals_both_teams_to_score_under_yes_25_data`, " 
        query_commit += " `total_goals_both_teams_to_score_under_yes_25_perc`, " 
        query_commit += " `total_goals_both_teams_to_score_under_no_25_data`, " 
        query_commit += " `total_goals_both_teams_to_score_under_no_25_perc`, " 
        # ------------------------------------------------------
        query_commit += " `halftime_result_both_teams_score_home_yes_data`, " 
        query_commit += " `halftime_result_both_teams_score_home_yes_perc`, " 
        query_commit += " `halftime_result_both_teams_score_draw_yes_data`, " 
        query_commit += " `halftime_result_both_teams_score_draw_yes_perc`, " 
        query_commit += " `halftime_result_both_teams_score_away_yes_data`, " 
        query_commit += " `halftime_result_both_teams_score_away_yes_perc`, " 
        query_commit += " `halftime_result_both_teams_score_home_no_data`, " 
        query_commit += " `halftime_result_both_teams_score_home_no_perc`, " 
        query_commit += " `halftime_result_both_teams_score_draw_no_data`, " 
        query_commit += " `halftime_result_both_teams_score_draw_no_perc`, " 
        query_commit += " `halftime_result_both_teams_score_away_no_data`, " 
        query_commit += " `halftime_result_both_teams_score_away_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `both_teams_to_score_1st_half__2nd_half_yes_yes_data`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_yes_yes_perc`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_yes_no_data`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_yes_no_perc`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_no_yes_data`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_no_yes_perc`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_no_no_data`, " 
        query_commit += " `both_teams_to_score_1st_half__2nd_half_no_no_perc`, " 
        # ------------------------------------------------------
        query_commit += " `total_goals_under_2_data`, " 
        query_commit += " `total_goals_under_2_perc`, " 
        query_commit += " `total_goals_2_or_3_data`, " 
        query_commit += " `total_goals_2_or_3_perc`, " 
        query_commit += " `total_goals_over_3_data`, " 
        query_commit += " `total_goals_over_3_perc`, " 
        # ------------------------------------------------------
        query_commit += " `created_at` " 
        # ------------------------------------------------------
        query_commit += " ) VALUES ( " 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        query_commit += " '" + str(PARAM_1) + "', " 
        # ------------------------------------------------------
        query_commit += " " + str(total_fixtures) + ", " 
        # ------------------------------------------------------
        query_commit += " '" + str(pre_ah_pattern) + "', " 
        query_commit += " '" + str(pre_gou_pattern) + "', " 
        # ------------------------------------------------------
        query_commit += " '" + str(end_ah_pattern) + "', " 
        query_commit += " '" + str(end_gou_pattern) + "', " 
        # ------------------------------------------------------
        query_commit += " " + str(match_winner_home_data) + ", " 
        query_commit += " " + str(match_winner_home_perc) + ", " 
        query_commit += " " + str(match_winner_draw_data) + ", " 
        query_commit += " " + str(match_winner_draw_perc) + ", " 
        query_commit += " " + str(match_winner_away_data) + ", " 
        query_commit += " " + str(match_winner_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(homeaway_home_data) + ", " 
        query_commit += " " + str(homeaway_home_perc) + ", " 
        query_commit += " " + str(homeaway_away_data) + ", " 
        query_commit += " " + str(homeaway_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(second_half_winner_home_data) + ", " 
        query_commit += " " + str(second_half_winner_home_perc) + ", " 
        query_commit += " " + str(second_half_winner_draw_data) + ", " 
        query_commit += " " + str(second_half_winner_draw_perc) + ", " 
        query_commit += " " + str(second_half_winner_away_data) + ", " 
        query_commit += " " + str(second_half_winner_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(asian_handicap_home_min_65_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_65_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_65_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_65_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_6_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_6_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_6_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_6_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_55_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_55_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_55_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_55_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_5_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_5_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_5_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_5_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_45_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_45_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_45_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_45_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_4_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_4_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_4_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_4_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_35_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_35_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_35_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_35_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_3_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_3_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_3_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_3_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_25_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_25_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_25_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_25_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_2_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_2_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_2_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_2_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_15_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_15_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_1_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_1_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_min_05_data) + ", " 
        query_commit += " " + str(asian_handicap_home_min_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_min_05_data) + ", " 
        query_commit += " " + str(asian_handicap_away_min_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_0_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_0_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_0_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_0_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_05_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_05_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_1_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_1_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_15_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_15_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_2_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_2_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_2_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_2_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_25_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_25_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_25_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_25_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_3_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_3_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_3_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_3_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_35_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_35_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_35_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_35_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_4_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_4_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_4_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_4_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_45_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_45_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_45_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_45_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_5_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_5_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_5_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_5_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_55_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_55_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_55_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_55_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_6_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_6_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_6_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_6_perc) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_65_data) + ", " 
        query_commit += " " + str(asian_handicap_home_plus_65_perc) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_65_data) + ", " 
        query_commit += " " + str(asian_handicap_away_plus_65_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(goals_overunder_over_05_data) + ", " 
        query_commit += " " + str(goals_overunder_over_05_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_05_data) + ", " 
        query_commit += " " + str(goals_overunder_under_05_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_10_data) + ", " 
        query_commit += " " + str(goals_overunder_over_10_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_10_data) + ", " 
        query_commit += " " + str(goals_overunder_under_10_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_15_data) + ", " 
        query_commit += " " + str(goals_overunder_over_15_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_15_data) + ", " 
        query_commit += " " + str(goals_overunder_under_15_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_20_data) + ", " 
        query_commit += " " + str(goals_overunder_over_20_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_20_data) + ", " 
        query_commit += " " + str(goals_overunder_under_20_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_25_data) + ", " 
        query_commit += " " + str(goals_overunder_over_25_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_25_data) + ", " 
        query_commit += " " + str(goals_overunder_under_25_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_30_data) + ", " 
        query_commit += " " + str(goals_overunder_over_30_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_30_data) + ", " 
        query_commit += " " + str(goals_overunder_under_30_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_35_data) + ", " 
        query_commit += " " + str(goals_overunder_over_35_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_35_data) + ", " 
        query_commit += " " + str(goals_overunder_under_35_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_40_data) + ", " 
        query_commit += " " + str(goals_overunder_over_40_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_40_data) + ", " 
        query_commit += " " + str(goals_overunder_under_40_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_45_data) + ", " 
        query_commit += " " + str(goals_overunder_over_45_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_45_data) + ", " 
        query_commit += " " + str(goals_overunder_under_45_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_50_data) + ", " 
        query_commit += " " + str(goals_overunder_over_50_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_50_data) + ", " 
        query_commit += " " + str(goals_overunder_under_50_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_55_data) + ", " 
        query_commit += " " + str(goals_overunder_over_55_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_55_data) + ", " 
        query_commit += " " + str(goals_overunder_under_55_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_60_data) + ", " 
        query_commit += " " + str(goals_overunder_over_60_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_60_data) + ", " 
        query_commit += " " + str(goals_overunder_under_60_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_65_data) + ", " 
        query_commit += " " + str(goals_overunder_over_65_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_65_data) + ", " 
        query_commit += " " + str(goals_overunder_under_65_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_70_data) + ", " 
        query_commit += " " + str(goals_overunder_over_70_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_70_data) + ", " 
        query_commit += " " + str(goals_overunder_under_70_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_75_data) + ", " 
        query_commit += " " + str(goals_overunder_over_75_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_75_data) + ", " 
        query_commit += " " + str(goals_overunder_under_75_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_85_data) + ", " 
        query_commit += " " + str(goals_overunder_over_85_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_85_data) + ", " 
        query_commit += " " + str(goals_overunder_under_85_perc) + ", " 
        query_commit += " " + str(goals_overunder_over_95_data) + ", " 
        query_commit += " " + str(goals_overunder_over_95_perc) + ", " 
        query_commit += " " + str(goals_overunder_under_95_data) + ", " 
        query_commit += " " + str(goals_overunder_under_95_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(goals_overunder_first_half_over_05_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_05_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_05_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_05_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_10_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_10_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_10_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_10_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_15_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_15_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_15_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_15_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_20_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_20_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_20_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_20_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_25_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_25_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_25_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_25_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_30_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_30_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_30_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_30_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_35_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_over_35_perc) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_35_data) + ", " 
        query_commit += " " + str(goals_overunder_first_half_under_35_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(htft_double_home_home_data) + ", " 
        query_commit += " " + str(htft_double_home_home_perc) + ", " 
        query_commit += " " + str(htft_double_home_draw_data) + ", " 
        query_commit += " " + str(htft_double_home_draw_perc) + ", " 
        query_commit += " " + str(htft_double_home_away_data) + ", " 
        query_commit += " " + str(htft_double_home_away_perc) + ", " 
        query_commit += " " + str(htft_double_draw_home_data) + ", " 
        query_commit += " " + str(htft_double_draw_home_perc) + ", " 
        query_commit += " " + str(htft_double_draw_draw_data) + ", " 
        query_commit += " " + str(htft_double_draw_draw_perc) + ", " 
        query_commit += " " + str(htft_double_draw_away_data) + ", " 
        query_commit += " " + str(htft_double_draw_away_perc) + ", " 
        query_commit += " " + str(htft_double_away_home_data) + ", " 
        query_commit += " " + str(htft_double_away_home_perc) + ", " 
        query_commit += " " + str(htft_double_away_draw_data) + ", " 
        query_commit += " " + str(htft_double_away_draw_perc) + ", " 
        query_commit += " " + str(htft_double_away_away_data) + ", " 
        query_commit += " " + str(htft_double_away_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(both_teams_score_yes_data) + ", " 
        query_commit += " " + str(both_teams_score_yes_perc) + ", " 
        query_commit += " " + str(both_teams_score_no_data) + ", " 
        query_commit += " " + str(both_teams_score_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(highest_scoring_half_first_data) + ", " 
        query_commit += " " + str(highest_scoring_half_first_perc) + ", " 
        query_commit += " " + str(highest_scoring_half_draw_data) + ", " 
        query_commit += " " + str(highest_scoring_half_draw_perc) + ", " 
        query_commit += " " + str(highest_scoring_half_second_data) + ", " 
        query_commit += " " + str(highest_scoring_half_second_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(double_chance_home_draw_data) + ", " 
        query_commit += " " + str(double_chance_home_draw_perc) + ", " 
        query_commit += " " + str(double_chance_home_away_data) + ", " 
        query_commit += " " + str(double_chance_home_away_perc) + ", " 
        query_commit += " " + str(double_chance_draw_away_data) + ", " 
        query_commit += " " + str(double_chance_draw_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(first_half_winner_home_data) + ", " 
        query_commit += " " + str(first_half_winner_home_perc) + ", " 
        query_commit += " " + str(first_half_winner_draw_data) + ", " 
        query_commit += " " + str(first_half_winner_draw_perc) + ", " 
        query_commit += " " + str(first_half_winner_away_data) + ", " 
        query_commit += " " + str(first_half_winner_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(total_home_over_15_data) + ", " 
        query_commit += " " + str(total_home_over_15_perc) + ", " 
        query_commit += " " + str(total_home_under_15_data) + ", " 
        query_commit += " " + str(total_home_under_15_perc) + ", " 
        query_commit += " " + str(total_home_over_25_data) + ", " 
        query_commit += " " + str(total_home_over_25_perc) + ", " 
        query_commit += " " + str(total_home_under_25_data) + ", " 
        query_commit += " " + str(total_home_under_25_perc) + ", " 
        query_commit += " " + str(total_home_over_35_data) + ", " 
        query_commit += " " + str(total_home_over_35_perc) + ", " 
        query_commit += " " + str(total_home_under_35_data) + ", " 
        query_commit += " " + str(total_home_under_35_perc) + ", " 
        query_commit += " " + str(total_home_over_45_data) + ", " 
        query_commit += " " + str(total_home_over_45_perc) + ", " 
        query_commit += " " + str(total_home_under_45_data) + ", " 
        query_commit += " " + str(total_home_under_45_perc) + ", " 
        query_commit += " " + str(total_home_over_55_data) + ", " 
        query_commit += " " + str(total_home_over_55_perc) + ", " 
        query_commit += " " + str(total_home_under_55_data) + ", " 
        query_commit += " " + str(total_home_under_55_perc) + ", " 
        query_commit += " " + str(total_home_over_65_data) + ", " 
        query_commit += " " + str(total_home_over_65_perc) + ", " 
        query_commit += " " + str(total_home_under_65_data) + ", " 
        query_commit += " " + str(total_home_under_65_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(total_away_over_15_data) + ", " 
        query_commit += " " + str(total_away_over_15_perc) + ", " 
        query_commit += " " + str(total_away_under_15_data) + ", " 
        query_commit += " " + str(total_away_under_15_perc) + ", " 
        query_commit += " " + str(total_away_over_25_data) + ", " 
        query_commit += " " + str(total_away_over_25_perc) + ", " 
        query_commit += " " + str(total_away_under_25_data) + ", " 
        query_commit += " " + str(total_away_under_25_perc) + ", " 
        query_commit += " " + str(total_away_over_35_data) + ", " 
        query_commit += " " + str(total_away_over_35_perc) + ", " 
        query_commit += " " + str(total_away_under_35_data) + ", " 
        query_commit += " " + str(total_away_under_35_perc) + ", " 
        query_commit += " " + str(total_away_over_45_data) + ", " 
        query_commit += " " + str(total_away_over_45_perc) + ", " 
        query_commit += " " + str(total_away_under_45_data) + ", " 
        query_commit += " " + str(total_away_under_45_perc) + ", " 
        query_commit += " " + str(total_away_over_55_data) + ", " 
        query_commit += " " + str(total_away_over_55_perc) + ", " 
        query_commit += " " + str(total_away_under_55_data) + ", " 
        query_commit += " " + str(total_away_under_55_perc) + ", " 
        query_commit += " " + str(total_away_over_65_data) + ", " 
        query_commit += " " + str(total_away_over_65_perc) + ", " 
        query_commit += " " + str(total_away_under_65_data) + ", " 
        query_commit += " " + str(total_away_under_65_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(asian_handicap_first_half_home_min_15_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_min_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_15_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_min_1_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_min_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_1_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_min_05_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_min_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_05_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_min_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_0_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_0_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_0_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_0_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_05_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_05_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_05_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_1_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_1_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_1_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_15_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_home_plus_15_perc) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_15_data) + ", " 
        query_commit += " " + str(asian_handicap_first_half_away_plus_15_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(double_chance__first_half_home_draw_data) + ", " 
        query_commit += " " + str(double_chance__first_half_home_draw_perc) + ", " 
        query_commit += " " + str(double_chance__first_half_home_away_data) + ", " 
        query_commit += " " + str(double_chance__first_half_home_away_perc) + ", " 
        query_commit += " " + str(double_chance__first_half_draw_away_data) + ", " 
        query_commit += " " + str(double_chance__first_half_draw_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(oddeven_odd_data) + ", " 
        query_commit += " " + str(oddeven_odd_perc) + ", " 
        query_commit += " " + str(oddeven_even_data) + ", " 
        query_commit += " " + str(oddeven_even_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(results_both_teams_score_home_yes_data) + ", " 
        query_commit += " " + str(results_both_teams_score_home_yes_perc) + ", " 
        query_commit += " " + str(results_both_teams_score_draw_yes_data) + ", " 
        query_commit += " " + str(results_both_teams_score_draw_yes_perc) + ", " 
        query_commit += " " + str(results_both_teams_score_away_yes_data) + ", " 
        query_commit += " " + str(results_both_teams_score_away_yes_perc) + ", " 
        query_commit += " " + str(results_both_teams_score_home_no_data) + ", " 
        query_commit += " " + str(results_both_teams_score_home_no_perc) + ", " 
        query_commit += " " + str(results_both_teams_score_draw_no_data) + ", " 
        query_commit += " " + str(results_both_teams_score_draw_no_perc) + ", " 
        query_commit += " " + str(results_both_teams_score_away_no_data) + ", " 
        query_commit += " " + str(results_both_teams_score_away_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(result_total_goals_home_over_35_data) + ", " 
        query_commit += " " + str(result_total_goals_home_over_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_draw_over_35_data) + ", " 
        query_commit += " " + str(result_total_goals_draw_over_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_away_over_35_data) + ", " 
        query_commit += " " + str(result_total_goals_away_over_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_home_under_35_data) + ", " 
        query_commit += " " + str(result_total_goals_home_under_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_draw_under_35_data) + ", " 
        query_commit += " " + str(result_total_goals_draw_under_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_away_under_35_data) + ", " 
        query_commit += " " + str(result_total_goals_away_under_35_perc) + ", " 
        query_commit += " " + str(result_total_goals_home_over_25_data) + ", " 
        query_commit += " " + str(result_total_goals_home_over_25_perc) + ", " 
        query_commit += " " + str(result_total_goals_draw_over_25_data) + ", " 
        query_commit += " " + str(result_total_goals_draw_over_25_perc) + ", " 
        query_commit += " " + str(result_total_goals_away_over_25_data) + ", " 
        query_commit += " " + str(result_total_goals_away_over_25_perc) + ", " 
        query_commit += " " + str(result_total_goals_home_under_25_data) + ", " 
        query_commit += " " + str(result_total_goals_home_under_25_perc) + ", " 
        query_commit += " " + str(result_total_goals_draw_under_25_data) + ", " 
        query_commit += " " + str(result_total_goals_draw_under_25_perc) + ", " 
        query_commit += " " + str(result_total_goals_away_under_25_data) + ", " 
        query_commit += " " + str(result_total_goals_away_under_25_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(goals_overunder__second_half_over_05_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_05_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_05_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_05_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_10_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_10_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_10_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_10_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_15_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_15_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_15_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_15_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_20_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_20_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_20_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_20_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_25_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_25_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_25_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_25_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_30_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_30_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_30_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_30_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_35_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_over_35_perc) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_35_data) + ", " 
        query_commit += " " + str(goals_overunder__second_half_under_35_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(clean_sheet__home_yes_data) + ", " 
        query_commit += " " + str(clean_sheet__home_yes_perc) + ", " 
        query_commit += " " + str(clean_sheet__home_no_data) + ", " 
        query_commit += " " + str(clean_sheet__home_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(clean_sheet__away_yes_data) + ", " 
        query_commit += " " + str(clean_sheet__away_yes_perc) + ", " 
        query_commit += " " + str(clean_sheet__away_no_data) + ", " 
        query_commit += " " + str(clean_sheet__away_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(win_both_halves_home_data) + ", " 
        query_commit += " " + str(win_both_halves_home_perc) + ", " 
        query_commit += " " + str(win_both_halves_away_data) + ", " 
        query_commit += " " + str(win_both_halves_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(both_teams_score__first_half_yes_data) + ", " 
        query_commit += " " + str(both_teams_score__first_half_yes_perc) + ", " 
        query_commit += " " + str(both_teams_score__first_half_no_data) + ", " 
        query_commit += " " + str(both_teams_score__first_half_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(both_teams_to_score__second_half_yes_data) + ", " 
        query_commit += " " + str(both_teams_to_score__second_half_yes_perc) + ", " 
        query_commit += " " + str(both_teams_to_score__second_half_no_data) + ", " 
        query_commit += " " + str(both_teams_to_score__second_half_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(win_to_nil_home_data) + ", " 
        query_commit += " " + str(win_to_nil_home_perc) + ", " 
        query_commit += " " + str(win_to_nil_away_data) + ", " 
        query_commit += " " + str(win_to_nil_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(exact_goals_number_0_data) + ", " 
        query_commit += " " + str(exact_goals_number_0_perc) + ", " 
        query_commit += " " + str(exact_goals_number_1_data) + ", " 
        query_commit += " " + str(exact_goals_number_1_perc) + ", " 
        query_commit += " " + str(exact_goals_number_2_data) + ", " 
        query_commit += " " + str(exact_goals_number_2_perc) + ", " 
        query_commit += " " + str(exact_goals_number_3_data) + ", " 
        query_commit += " " + str(exact_goals_number_3_perc) + ", " 
        query_commit += " " + str(exact_goals_number_4_data) + ", " 
        query_commit += " " + str(exact_goals_number_4_perc) + ", " 
        query_commit += " " + str(exact_goals_number_5_data) + ", " 
        query_commit += " " + str(exact_goals_number_5_perc) + ", " 
        query_commit += " " + str(exact_goals_number_6_data) + ", " 
        query_commit += " " + str(exact_goals_number_6_perc) + ", " 
        query_commit += " " + str(exact_goals_number_more_7_data) + ", " 
        query_commit += " " + str(exact_goals_number_more_7_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(to_win_either_half_home_data) + ", " 
        query_commit += " " + str(to_win_either_half_home_perc) + ", " 
        query_commit += " " + str(to_win_either_half_away_data) + ", " 
        query_commit += " " + str(to_win_either_half_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(home_team_exact_goals_number_0_data) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_0_perc) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_1_data) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_1_perc) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_2_data) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_2_perc) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_more_3_data) + ", " 
        query_commit += " " + str(home_team_exact_goals_number_more_3_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(away_team_exact_goals_number_0_data) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_0_perc) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_1_data) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_1_perc) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_2_data) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_2_perc) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_more_3_data) + ", " 
        query_commit += " " + str(away_team_exact_goals_number_more_3_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(second_half_exact_goals_number_0_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_0_perc) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_1_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_1_perc) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_2_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_2_perc) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_3_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_3_perc) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_4_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_4_perc) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_more_5_data) + ", " 
        query_commit += " " + str(second_half_exact_goals_number_more_5_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(exact_goals_number__first_half_0_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_0_perc) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_1_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_1_perc) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_2_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_2_perc) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_3_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_3_perc) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_4_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_4_perc) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_more_5_data) + ", " 
        query_commit += " " + str(exact_goals_number__first_half_more_5_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(to_score_in_both_halves_by_teams_home_data) + ", " 
        query_commit += " " + str(to_score_in_both_halves_by_teams_home_perc) + ", " 
        query_commit += " " + str(to_score_in_both_halves_by_teams_away_data) + ", " 
        query_commit += " " + str(to_score_in_both_halves_by_teams_away_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(total_goals_both_teams_to_score_over_yes_25_data) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_over_yes_25_perc) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_over_no_25_data) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_over_no_25_perc) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_under_yes_25_data) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_under_yes_25_perc) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_under_no_25_data) + ", " 
        query_commit += " " + str(total_goals_both_teams_to_score_under_no_25_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(halftime_result_both_teams_score_home_yes_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_home_yes_perc) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_draw_yes_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_draw_yes_perc) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_away_yes_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_away_yes_perc) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_home_no_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_home_no_perc) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_draw_no_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_draw_no_perc) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_away_no_data) + ", " 
        query_commit += " " + str(halftime_result_both_teams_score_away_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_yes_yes_data) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_yes_yes_perc) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_yes_no_data) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_yes_no_perc) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_no_yes_data) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_no_yes_perc) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_no_no_data) + ", " 
        query_commit += " " + str(both_teams_to_score_1st_half__2nd_half_no_no_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " " + str(total_goals_under_2_data) + ", " 
        query_commit += " " + str(total_goals_under_2_perc) + ", " 
        query_commit += " " + str(total_goals_2_or_3_data) + ", " 
        query_commit += " " + str(total_goals_2_or_3_perc) + ", " 
        query_commit += " " + str(total_goals_over_3_data) + ", " 
        query_commit += " " + str(total_goals_over_3_perc) + ", " 
        # ------------------------------------------------------
        query_commit += " now() "
        # ------------------------------------------------------ 
        query_commit += " ) " 
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        print(space + query_commit, flush=True)
        # ------------------------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()   
        # ------------------------------------------------------
        mycursor.close()
        mydb.close()   
        # ------------------------------------------------------
        print(space + "pattern INSERTED", flush=True)
        # ------------------------------------------------------
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
    else:
        # ------------------------------------------------------
        print(space + "KOSONG : " + str(total_rows), flush=True)
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    if(type_of_pattern == 1):
        fpa_football_pattern_from_updated_at(PARAM_1, 
                                            pre_ah_pattern,
                                            pre_gou_pattern,
                                            end_ah_pattern,
                                            end_gou_pattern,
                                            space)
    # ----------------------------------------------------------  
    print(space, flush=True)
    # ----------------------------------------------------------  

 

def fpa_football_pattern_from_updated_at(leagueapi_id, 
                                                pre_ah_pattern,
                                                pre_gou_pattern,
                                                end_ah_pattern,
                                                end_gou_pattern,
                                                space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "fpa_football_pattern_from_updated_at()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------   
    print(space + "leagueapi_id : " + str(leagueapi_id), flush=True)  
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query_commit = " UPDATE `football_odds` SET  " 
    query_commit += " football_pattern_from_only_updated_at = now() "    
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "   
     
    query_commit += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "     
    query_commit += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    

    query_commit += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "     
    query_commit += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "   
    # ----------------------------------------------------------  
    space += "__"   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)      
    # ----------------------------------------------------------  
    mycursor.execute(query_commit)
    mydb.commit()        
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  