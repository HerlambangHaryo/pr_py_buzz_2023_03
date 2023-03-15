# Import
import mysql.connector
from a_models.patternlists_assestment import *  

def pl_updating_all_leagues_to_patternlist():
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select leagueapi_id " 
    query += " from pattern_lists "     
    query += " group by leagueapi_id " 
    # ----------------------------------------------------------   
    query_1 = " select leagueapi_id "  
    query_1 += " from football_fixtures " 
    query_1 += " where leagueapi_id not in ('"+query+"') "
    query_1 += " group by leagueapi_id " 
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query_1)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    for x in result: 
        print(x[0])


    
def pl_country_for_patternlists(yesterday_ago, space):
    # ----------------------------------------------------------  
    print(space + "__pl_country_for_patternlists__")
    # ---------------------------------------------------------- 
    # Update Pattern list 
    space += "  "
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    # OLD QUERY  
    # query = " Select league_country "   
    # query += " FROM `football_fixtures` "   
    # query += " WHERE fixture_status IN ('Match Finished', 'Match Finished Ended') " 
    # query += " AND DATE(date) <= '"+str(yesterday_ago)+"' "  
    # query += " GROUP BY league_country "  

     
    query = " Select leagueapi_id "   
    query += " FROM `football_fixtures` "   
    query += " WHERE fixture_status IN ('Match Finished', 'Match Finished Ended') " 
    query += " AND DATE(date) <= '"+str(yesterday_ago)+"' "  
    query += " GROUP BY leagueapi_id "  
    # ----------------------------------------------------------  
    # print(space + query)
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result))) 
    # ----------------------------------------------------------    
    space += "  "
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
    # ----------------------------------------------------------    
        counter += 1
        leagueapi_id = str(x[0])  
        # ------------------------------------------------------- 
        print("")
        # -------------------------------------------------------
        word = space + str(counter) + ". " 
        word += " #" + str(leagueapi_id) 
        word += " - " + str(yesterday_ago) 
        print(word)
        # ------------------------------------------------------- 
        print("")
        # ------------------------------------------------------- 
        # print(space + "_>pl_league_for_patternlists__")
        # # -------------------------------------------------------   
        # host="localhost"
        # user="root" 
        # database="pr_mmbuzz_2022_06"
        # mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        # mycursor = mydb.cursor()
        # # ------------------------------------------------------- 
        # query = " Select leagueapi_id "   
        # query += " FROM `leagues` "    
        # query += " WHERE country = '"+str(country)+"' "  
        # # ------------------------------------------------------- 
        # # print(space + query)
        # # -------------------------------------------------------
        # mycursor = mydb.cursor()
        # mycursor.execute(query)
        # result =  mycursor.fetchall()
        # # -------------------------------------------------------    
        # print(space + "Total Row(s) : " + str(len(result))) 
        # # -------------------------------------------------------    
        # counter2 = 0
        # # -------------------------------------------------------   
        # for x in result:    
        # # -------------------------------------------------------    
        #     counter2        += 1
        #     leagueapi_id   = str(x[0])  
        #     # --------------------------------------------------- 
        #     print("")
        #     # ---------------------------------------------------
        #     word = space + "  " + str(counter) + "."+ str(counter2) + ". " 
        #     word += " #" + str(leagueapi_id) 
        #     word += " - " + str(yesterday_ago) 
        #     print(word)
        # # ------------------------------------------------------- 
        #     pa_assestment(leagueapi_id, yesterday_ago, space + "  ")
        # ------------------------------------------------------- 
        # ------------------------------------------------------- 
    # -----------------------------------------------------------   

def pl_predates_get_advice(fixtureapi_id, mirror, space):
    # ----------------------------------------------------------  
    print(space + "__pl_predates_get_advice__" + mirror)
    # ---------------------------------------------------------- 
    space += "  "
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query = " Select " 
    query += " pre_ah_pattern, "
    query += " pre_gou_pattern, "
    query += " leagueapi_id, "
    query += " id "
    query += " from football_fixtures "  
    query += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        # ------------------------------------------------------
        pre_ah_pattern      = x[0]
        pre_gou_pattern     = x[1]
        leagueapi_id        = x[2] 
        idx                 = x[3] 
        # ------------------------------------------------------
        end_ah_pattern  = pre_ah_pattern
        end_gou_pattern = pre_gou_pattern
        status = "pre"
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    pl_get_leagueapi_for_advice(pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, leagueapi_id, idx, status, mirror, space)
    # ----------------------------------------------------------  

def pl_get_leagueapi_for_advice(pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, leagueapi_id, idx, status, mirror, space):
    # ----------------------------------------------------------  
    print(space + "__pl_get_leagueapi_for_advice__")
    # ---------------------------------------------------------- 
    space += "  "
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select " 
    
    query += " total_fixtures, "
    # ---------------------------------------------------------- 
    query += " asian_handicap_home_min_65_perc, "
    query += " asian_handicap_away_min_65_perc, "
    query += " asian_handicap_home_min_6_perc, "
    query += " asian_handicap_away_min_6_perc, "
    query += " asian_handicap_home_min_55_perc, "
    query += " asian_handicap_away_min_55_perc, "
    query += " asian_handicap_home_min_5_perc, "
    query += " asian_handicap_away_min_5_perc, "
    query += " asian_handicap_home_min_45_perc, "
    query += " asian_handicap_away_min_45_perc, "
    query += " asian_handicap_home_min_4_perc, "
    query += " asian_handicap_away_min_4_perc, "
    query += " asian_handicap_home_min_35_perc, "
    query += " asian_handicap_away_min_35_perc, "
    query += " asian_handicap_home_min_3_perc, "
    query += " asian_handicap_away_min_3_perc, "
    query += " asian_handicap_home_min_25_perc, "
    query += " asian_handicap_away_min_25_perc, "
    query += " asian_handicap_home_min_2_perc, "
    query += " asian_handicap_away_min_2_perc, "
    query += " asian_handicap_home_min_15_perc, "
    query += " asian_handicap_away_min_15_perc, "
    query += " asian_handicap_home_min_1_perc, "
    query += " asian_handicap_away_min_1_perc, "
    query += " asian_handicap_home_min_05_perc, "
    query += " asian_handicap_away_min_05_perc, "
    query += " asian_handicap_home_plus_0_perc, "
    query += " asian_handicap_away_plus_0_perc, "
    query += " asian_handicap_home_plus_05_perc, "
    query += " asian_handicap_away_plus_05_perc, "
    query += " asian_handicap_home_plus_1_perc, "
    query += " asian_handicap_away_plus_1_perc, "
    query += " asian_handicap_home_plus_15_perc, "
    query += " asian_handicap_away_plus_15_perc, "
    query += " asian_handicap_home_plus_2_perc, "
    query += " asian_handicap_away_plus_2_perc, "
    query += " asian_handicap_home_plus_25_perc, "
    query += " asian_handicap_away_plus_25_perc, "
    query += " asian_handicap_home_plus_3_perc, "
    query += " asian_handicap_away_plus_3_perc, "
    query += " asian_handicap_home_plus_35_perc, "
    query += " asian_handicap_away_plus_35_perc, "
    query += " asian_handicap_home_plus_4_perc, "
    query += " asian_handicap_away_plus_4_perc, "
    query += " asian_handicap_home_plus_45_perc, "
    query += " asian_handicap_away_plus_45_perc, "
    query += " asian_handicap_home_plus_5_perc, "
    query += " asian_handicap_away_plus_5_perc, "
    query += " asian_handicap_home_plus_55_perc, "
    query += " asian_handicap_away_plus_55_perc, "
    query += " asian_handicap_home_plus_6_perc, "
    query += " asian_handicap_away_plus_6_perc, "
    query += " asian_handicap_home_plus_65_perc, "
    query += " asian_handicap_away_plus_65_perc, "
    # ---------------------------------------------------------- 
    query += " goals_overunder_over_05_perc, "
    query += " goals_overunder_under_05_perc, "
    query += " goals_overunder_over_10_perc, "
    query += " goals_overunder_under_10_perc, "
    query += " goals_overunder_over_15_perc, "
    query += " goals_overunder_under_15_perc, "
    query += " goals_overunder_over_20_perc, "
    query += " goals_overunder_under_20_perc, "
    query += " goals_overunder_over_25_perc, "
    query += " goals_overunder_under_25_perc, "
    query += " goals_overunder_over_30_perc, "
    query += " goals_overunder_under_30_perc, "
    query += " goals_overunder_over_35_perc, "
    query += " goals_overunder_under_35_perc, "
    query += " goals_overunder_over_40_perc, "
    query += " goals_overunder_under_40_perc, "
    query += " goals_overunder_over_45_perc, "
    query += " goals_overunder_under_45_perc, "
    query += " goals_overunder_over_50_perc, "
    query += " goals_overunder_under_50_perc, "
    query += " goals_overunder_over_55_perc, "
    query += " goals_overunder_under_55_perc, "
    query += " goals_overunder_over_60_perc, "
    query += " goals_overunder_under_60_perc, "
    query += " goals_overunder_over_65_perc, "
    query += " goals_overunder_under_65_perc, "
    query += " goals_overunder_over_70_perc, "
    query += " goals_overunder_under_70_perc, "
    query += " goals_overunder_over_75_perc, "
    query += " goals_overunder_under_75_perc, "
    query += " goals_overunder_over_85_perc, "
    query += " goals_overunder_under_85_perc, "
    query += " goals_overunder_over_95_perc, "
    query += " goals_overunder_under_95_perc, "
    # ---------------------------------------------------------- 
    query += " goals_overunder_first_half_over_05_perc, "
    query += " goals_overunder_first_half_under_05_perc, "
    query += " goals_overunder_first_half_over_10_perc, "
    query += " goals_overunder_first_half_under_10_perc, "
    query += " goals_overunder_first_half_over_15_perc, "
    query += " goals_overunder_first_half_under_15_perc, "
    query += " goals_overunder_first_half_over_20_perc, "
    query += " goals_overunder_first_half_under_20_perc, "
    query += " goals_overunder_first_half_over_25_perc, "
    query += " goals_overunder_first_half_under_25_perc, "
    query += " goals_overunder_first_half_over_30_perc, "
    query += " goals_overunder_first_half_under_30_perc, "
    query += " goals_overunder_first_half_over_35_perc, "
    query += " goals_overunder_first_half_under_35_perc, "
    # ---------------------------------------------------------- 
    query += " asian_handicap_first_half_home_min_15_perc, "
    query += " asian_handicap_first_half_away_min_15_perc, "
    query += " asian_handicap_first_half_home_min_1_perc, "
    query += " asian_handicap_first_half_away_min_1_perc, "
    query += " asian_handicap_first_half_home_min_05_perc, "
    query += " asian_handicap_first_half_away_min_05_perc, "
    query += " asian_handicap_first_half_home_plus_0_perc, "
    query += " asian_handicap_first_half_away_plus_0_perc, "
    query += " asian_handicap_first_half_home_plus_05_perc, "
    query += " asian_handicap_first_half_away_plus_05_perc, "
    query += " asian_handicap_first_half_home_plus_1_perc, "
    query += " asian_handicap_first_half_away_plus_1_perc, "
    query += " asian_handicap_first_half_home_plus_15_perc, "
    query += " asian_handicap_first_half_away_plus_15_perc, "
    # ---------------------------------------------------------- 
    query += " goals_overunder__second_half_over_05_perc, "
    query += " goals_overunder__second_half_under_05_perc, "
    query += " goals_overunder__second_half_over_10_perc, "
    query += " goals_overunder__second_half_under_10_perc, "
    query += " goals_overunder__second_half_over_15_perc, "
    query += " goals_overunder__second_half_under_15_perc, "
    query += " goals_overunder__second_half_over_20_perc, "
    query += " goals_overunder__second_half_under_20_perc, "
    query += " goals_overunder__second_half_over_25_perc, "
    query += " goals_overunder__second_half_under_25_perc, "
    query += " goals_overunder__second_half_over_30_perc, "
    query += " goals_overunder__second_half_under_30_perc, "
    query += " goals_overunder__second_half_over_35_perc, "
    query += " goals_overunder__second_half_under_35_perc, "
    # ---------------------------------------------------------- 
    query += " match_winner_home_perc, "
    query += " match_winner_draw_perc, "
    query += " match_winner_away_perc, "
    # ---------------------------------------------------------- 
    query += " homeaway_home_perc, "
    query += " homeaway_away_perc, "
    # ---------------------------------------------------------- 
    query += " second_half_winner_home_perc, "
    query += " second_half_winner_draw_perc, "
    query += " second_half_winner_away_perc, "
    # ---------------------------------------------------------- 
    query += " htft_double_home_home_perc, "
    query += " htft_double_home_draw_perc, "
    query += " htft_double_home_away_perc, "
    query += " htft_double_draw_home_perc, "
    query += " htft_double_draw_draw_perc, "
    query += " htft_double_draw_away_perc, "
    query += " htft_double_away_home_perc, "
    query += " htft_double_away_draw_perc, "
    query += " htft_double_away_away_perc, "
    # ---------------------------------------------------------- 
    query += " both_teams_score_yes_perc, "
    query += " both_teams_score_no_perc, "
    # ---------------------------------------------------------- 
    query += " highest_scoring_half_first_perc, "
    query += " highest_scoring_half_draw_perc, "
    query += " highest_scoring_half_second_perc, "
    # ---------------------------------------------------------- 
    query += " double_chance_home_draw_perc, "
    query += " double_chance_home_away_perc, "
    query += " double_chance_draw_away_perc, "
    # ---------------------------------------------------------- 
    query += " first_half_winner_home_perc, "
    query += " first_half_winner_draw_perc, "
    query += " first_half_winner_away_perc, "
    # ---------------------------------------------------------- 
    query += " double_chance__first_half_home_draw_perc, "
    query += " double_chance__first_half_home_away_perc, "
    query += " double_chance__first_half_draw_away_perc, "
    # ---------------------------------------------------------- 
    query += " oddeven_odd_perc, "
    query += " oddeven_even_perc, "
    # ---------------------------------------------------------- 
    query += " results_both_teams_score_home_yes_perc, "
    query += " results_both_teams_score_draw_yes_perc, "
    query += " results_both_teams_score_away_yes_perc, "
    query += " results_both_teams_score_home_no_perc, "
    query += " results_both_teams_score_draw_no_perc, "
    query += " results_both_teams_score_away_no_perc, "
    # ---------------------------------------------------------- 
    query += " result_total_goals_home_over_35_perc, "
    query += " result_total_goals_draw_over_35_perc, "
    query += " result_total_goals_away_over_35_perc, "
    query += " result_total_goals_home_under_35_perc, "
    query += " result_total_goals_draw_under_35_perc, "
    query += " result_total_goals_away_under_35_perc, "
    query += " result_total_goals_home_over_25_perc, "
    query += " result_total_goals_draw_over_25_perc, "
    query += " result_total_goals_away_over_25_perc, "
    query += " result_total_goals_home_under_25_perc, "
    query += " result_total_goals_draw_under_25_perc, "
    query += " result_total_goals_away_under_25_perc, "
    # ---------------------------------------------------------- 
    query += " clean_sheet__home_yes_perc, "
    query += " clean_sheet__home_no_perc, "
    query += " clean_sheet__away_yes_perc, "
    query += " clean_sheet__away_no_perc, "
    # ---------------------------------------------------------- 
    query += " win_both_halves_home_perc, "
    query += " win_both_halves_away_perc, "
    # ---------------------------------------------------------- 
    query += " both_teams_score__first_half_yes_perc, "
    query += " both_teams_score__first_half_no_perc, "
    # ---------------------------------------------------------- 
    query += " both_teams_to_score__second_half_yes_perc, "
    query += " both_teams_to_score__second_half_no_perc, "
    # ---------------------------------------------------------- 
    query += " win_to_nil_home_perc, "
    query += " win_to_nil_away_perc, "
    # ---------------------------------------------------------- 
    query += " exact_goals_number_0_perc, "
    query += " exact_goals_number_1_perc, "
    query += " exact_goals_number_2_perc, "
    query += " exact_goals_number_3_perc, "
    query += " exact_goals_number_4_perc, "
    query += " exact_goals_number_5_perc, "
    query += " exact_goals_number_6_perc, "
    query += " exact_goals_number_more_7_perc, "
    # ---------------------------------------------------------- 
    query += " to_win_either_half_home_perc, "
    query += " to_win_either_half_away_perc, "
    # ---------------------------------------------------------- 
    query += " home_team_exact_goals_number_0_perc, "
    query += " home_team_exact_goals_number_1_perc, "
    query += " home_team_exact_goals_number_2_perc, "
    query += " home_team_exact_goals_number_more_3_perc, "
    # ---------------------------------------------------------- 
    query += " away_team_exact_goals_number_0_perc, "
    query += " away_team_exact_goals_number_1_perc, "
    query += " away_team_exact_goals_number_2_perc, "
    query += " away_team_exact_goals_number_more_3_perc, "
    # ---------------------------------------------------------- 
    query += " second_half_exact_goals_number_0_perc, "
    query += " second_half_exact_goals_number_1_perc, "
    query += " second_half_exact_goals_number_2_perc, "
    query += " second_half_exact_goals_number_3_perc, "
    query += " second_half_exact_goals_number_4_perc, "
    query += " second_half_exact_goals_number_more_5_perc, "
    # ---------------------------------------------------------- 
    query += " exact_goals_number__first_half_0_perc, "
    query += " exact_goals_number__first_half_1_perc, "
    query += " exact_goals_number__first_half_2_perc, "
    query += " exact_goals_number__first_half_3_perc, "
    query += " exact_goals_number__first_half_4_perc, "
    query += " exact_goals_number__first_half_more_5_perc, "
    # ---------------------------------------------------------- 
    query += " to_score_in_both_halves_by_teams_home_perc, "
    query += " to_score_in_both_halves_by_teams_away_perc, "
    # ---------------------------------------------------------- 
    query += " total_goals_both_teams_to_score_over_yes_25_perc, "
    query += " total_goals_both_teams_to_score_over_no_25_perc, "
    query += " total_goals_both_teams_to_score_under_yes_25_perc, "
    query += " total_goals_both_teams_to_score_under_no_25_perc, "
    # ---------------------------------------------------------- 
    query += " halftime_result_both_teams_score_home_yes_perc, "
    query += " halftime_result_both_teams_score_draw_yes_perc, "
    query += " halftime_result_both_teams_score_away_yes_perc, "
    query += " halftime_result_both_teams_score_home_no_perc, "
    query += " halftime_result_both_teams_score_draw_no_perc, "
    query += " halftime_result_both_teams_score_away_no_perc, "
    # ---------------------------------------------------------- 
    query += " both_teams_to_score_1st_half__2nd_half_yes_yes_perc, "
    query += " both_teams_to_score_1st_half__2nd_half_yes_no_perc, "
    query += " both_teams_to_score_1st_half__2nd_half_no_yes_perc, "
    query += " both_teams_to_score_1st_half__2nd_half_no_no_perc, "
    # ---------------------------------------------------------- 
    query += " rcard_yes_perc, "
    query += " rcard_no_perc, "
    query += " rcard_no_data "
    # ---------------------------------------------------------- 
    query += " from pattern_lists "     
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  

    query_x = " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    print(space + query_x)

    if(mirror == "yes"): 
        query += " and pre_ah_pattern_mirror = '"+str(pre_ah_pattern)+"' "  
        query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  

        query_x = " and pre_ah_pattern_mirror = '"+str(pre_ah_pattern)+"' " 
        print(space + query_x)
        query_x = " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  
        print(space + query_x)

        if(status == "pre"):
            query += " and end_ah_pattern_mirror = '"+str(pre_ah_pattern)+"' "  
            query += " and end_gou_pattern = '"+str(pre_gou_pattern)+"' "  

            query_x = " and end_ah_pattern_mirror = '"+str(pre_ah_pattern)+"' "
            print(space + query_x) 
            query_x = " and end_gou_pattern = '"+str(pre_gou_pattern)+"' "   
            print(space + query_x)

        elif(status == "end"):
            query += " and end_ah_pattern_mirror = '"+str(end_ah_pattern)+"' "  
            query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' " 

            query_x = " and end_ah_pattern_mirror = '"+str(end_ah_pattern)+"' " 
            print(space + query_x) 
            query_x = " and end_gou_pattern = '"+str(end_gou_pattern)+"' "  
            print(space + query_x) 

    elif(mirror == "no"):
        query += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "  
        query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' " 

        query_x = " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' " 
        print(space + query_x)
        query_x = " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   
        print(space + query_x)

        if(status == "pre"):
            query += " and end_ah_pattern = '"+str(pre_ah_pattern)+"' "   
            query += " and end_gou_pattern = '"+str(pre_gou_pattern)+"' "   

            query_x = " and end_ah_pattern = '"+str(pre_ah_pattern)+"' " 
            print(space + query_x) 
            query_x = " and end_gou_pattern = '"+str(pre_gou_pattern)+"' "  
            print(space + query_x)  

        elif(status == "end"):
            query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "  
            query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' " 

            query_x = " and end_ah_pattern = '"+str(end_ah_pattern)+"' " 
            print(space + query_x) 
            query_x = " and end_gou_pattern = '"+str(end_gou_pattern)+"' "  
            print(space + query_x) 
            
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)))   
    # ---------------------------------------------------------- 
    print("")
    # ----------------------------------------------------------  
    col_counter = 0
    advices = ""
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------  
        total_fixtures = x[col_counter]
        # ------------------------------------------------------   
        col_counter += 1 
        asian_handicap_home_min_65_perc = x[col_counter]

        col_counter += 1 
        asian_handicap_away_min_65_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_6_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_6_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_55_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_55_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_5_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_5_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_45_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_45_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_4_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_4_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_35_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_35_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_3_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_3_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_25_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_25_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_2_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_2_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_min_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_min_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_0_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_0_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_2_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_2_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_25_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_25_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_3_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_3_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_35_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_35_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_4_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_4_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_45_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_45_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_5_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_5_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_55_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_55_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_6_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_6_perc = x[col_counter]

        col_counter += 1
        asian_handicap_home_plus_65_perc = x[col_counter]

        col_counter += 1
        asian_handicap_away_plus_65_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_35_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_35_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_40_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_40_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_45_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_45_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_50_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_50_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_55_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_55_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_60_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_60_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_65_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_65_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_70_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_70_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_75_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_75_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_85_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_85_perc = x[col_counter]

        col_counter += 1
        goals_overunder_over_95_perc = x[col_counter]

        col_counter += 1
        goals_overunder_under_95_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_over_35_perc = x[col_counter]

        col_counter += 1
        goals_overunder_first_half_under_35_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_min_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_min_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_min_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_min_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_min_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_min_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_plus_0_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_plus_0_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_plus_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_plus_05_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_plus_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_plus_1_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_home_plus_15_perc = x[col_counter]

        col_counter += 1
        asian_handicap_first_half_away_plus_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_05_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_10_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_15_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_20_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_25_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_30_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_over_35_perc = x[col_counter]

        col_counter += 1
        goals_overunder__second_half_under_35_perc = x[col_counter]

        col_counter += 1
        match_winner_home_perc = x[col_counter]

        col_counter += 1
        match_winner_draw_perc = x[col_counter]

        col_counter += 1
        match_winner_away_perc = x[col_counter]

        col_counter += 1
        homeaway_home_perc = x[col_counter]

        col_counter += 1
        homeaway_away_perc = x[col_counter]

        col_counter += 1
        second_half_winner_home_perc = x[col_counter]

        col_counter += 1
        second_half_winner_draw_perc = x[col_counter]

        col_counter += 1
        second_half_winner_away_perc = x[col_counter]

        col_counter += 1
        htft_double_home_home_perc = x[col_counter]

        col_counter += 1
        htft_double_home_draw_perc = x[col_counter]

        col_counter += 1
        htft_double_home_away_perc = x[col_counter]

        col_counter += 1
        htft_double_draw_home_perc = x[col_counter]

        col_counter += 1
        htft_double_draw_draw_perc = x[col_counter]

        col_counter += 1
        htft_double_draw_away_perc = x[col_counter]

        col_counter += 1
        htft_double_away_home_perc = x[col_counter]

        col_counter += 1
        htft_double_away_draw_perc = x[col_counter]

        col_counter += 1
        htft_double_away_away_perc = x[col_counter]

        col_counter += 1
        both_teams_score_yes_perc = x[col_counter]

        col_counter += 1
        both_teams_score_no_perc = x[col_counter]

        col_counter += 1
        highest_scoring_half_first_perc = x[col_counter]

        col_counter += 1
        highest_scoring_half_draw_perc = x[col_counter]

        col_counter += 1
        highest_scoring_half_second_perc = x[col_counter]

        col_counter += 1
        double_chance_home_draw_perc = x[col_counter]

        col_counter += 1
        double_chance_home_away_perc = x[col_counter]

        col_counter += 1
        double_chance_draw_away_perc = x[col_counter]

        col_counter += 1
        first_half_winner_home_perc = x[col_counter]

        col_counter += 1
        first_half_winner_draw_perc = x[col_counter]

        col_counter += 1
        first_half_winner_away_perc = x[col_counter]

        col_counter += 1
        double_chance__first_half_home_draw_perc = x[col_counter]

        col_counter += 1
        double_chance__first_half_home_away_perc = x[col_counter]

        col_counter += 1
        double_chance__first_half_draw_away_perc = x[col_counter]

        col_counter += 1
        oddeven_odd_perc = x[col_counter]

        col_counter += 1
        oddeven_even_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_home_yes_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_draw_yes_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_away_yes_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_home_no_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_draw_no_perc = x[col_counter]

        col_counter += 1
        results_both_teams_score_away_no_perc = x[col_counter]

        col_counter += 1
        result_total_goals_home_over_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_draw_over_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_away_over_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_home_under_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_draw_under_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_away_under_35_perc = x[col_counter]

        col_counter += 1
        result_total_goals_home_over_25_perc = x[col_counter]

        col_counter += 1
        result_total_goals_draw_over_25_perc = x[col_counter]

        col_counter += 1
        result_total_goals_away_over_25_perc = x[col_counter]

        col_counter += 1
        result_total_goals_home_under_25_perc = x[col_counter]

        col_counter += 1
        result_total_goals_draw_under_25_perc = x[col_counter]

        col_counter += 1
        result_total_goals_away_under_25_perc = x[col_counter]

        col_counter += 1
        clean_sheet__home_yes_perc = x[col_counter]

        col_counter += 1
        clean_sheet__home_no_perc = x[col_counter]

        col_counter += 1
        clean_sheet__away_yes_perc = x[col_counter]

        col_counter += 1
        clean_sheet__away_no_perc = x[col_counter]

        col_counter += 1
        win_both_halves_home_perc = x[col_counter]

        col_counter += 1
        win_both_halves_away_perc = x[col_counter]

        col_counter += 1
        both_teams_score__first_half_yes_perc = x[col_counter]

        col_counter += 1
        both_teams_score__first_half_no_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score__second_half_yes_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score__second_half_no_perc = x[col_counter]

        col_counter += 1
        win_to_nil_home_perc = x[col_counter]

        col_counter += 1
        win_to_nil_away_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_0_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_1_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_2_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_3_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_4_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_5_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_6_perc = x[col_counter]

        col_counter += 1
        exact_goals_number_more_7_perc = x[col_counter]

        col_counter += 1
        to_win_either_half_home_perc = x[col_counter]

        col_counter += 1
        to_win_either_half_away_perc = x[col_counter]

        col_counter += 1
        home_team_exact_goals_number_0_perc = x[col_counter]

        col_counter += 1
        home_team_exact_goals_number_1_perc = x[col_counter]

        col_counter += 1
        home_team_exact_goals_number_2_perc = x[col_counter]

        col_counter += 1
        home_team_exact_goals_number_more_3_perc = x[col_counter]

        col_counter += 1
        away_team_exact_goals_number_0_perc = x[col_counter]

        col_counter += 1
        away_team_exact_goals_number_1_perc = x[col_counter]

        col_counter += 1
        away_team_exact_goals_number_2_perc = x[col_counter]

        col_counter += 1
        away_team_exact_goals_number_more_3_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_0_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_1_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_2_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_3_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_4_perc = x[col_counter]

        col_counter += 1
        second_half_exact_goals_number_more_5_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_0_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_1_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_2_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_3_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_4_perc = x[col_counter]

        col_counter += 1
        exact_goals_number__first_half_more_5_perc = x[col_counter]

        col_counter += 1
        to_score_in_both_halves_by_teams_home_perc = x[col_counter]

        col_counter += 1
        to_score_in_both_halves_by_teams_away_perc = x[col_counter]

        col_counter += 1
        total_goals_both_teams_to_score_over_yes_25_perc = x[col_counter]

        col_counter += 1
        total_goals_both_teams_to_score_over_no_25_perc = x[col_counter]

        col_counter += 1
        total_goals_both_teams_to_score_under_yes_25_perc = x[col_counter]

        col_counter += 1
        total_goals_both_teams_to_score_under_no_25_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_home_yes_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_draw_yes_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_away_yes_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_home_no_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_draw_no_perc = x[col_counter]

        col_counter += 1
        halftime_result_both_teams_score_away_no_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score_1st_half__2nd_half_yes_yes_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score_1st_half__2nd_half_yes_no_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score_1st_half__2nd_half_no_yes_perc = x[col_counter]

        col_counter += 1
        both_teams_to_score_1st_half__2nd_half_no_no_perc = x[col_counter]

        col_counter += 1
        rcard_yes_perc = x[col_counter]

        col_counter += 1
        rcard_no_perc = x[col_counter]

        col_counter += 1
        rcard_no_data = x[col_counter]

        # ------------------------------------------------------  
        print(space + " idx:" + str(idx)) 
        # ------------------------------------------------------  
        print(space + " total_fixtures:" + str(total_fixtures)) 

        status_mirror = ""
        status_mirror_bg = "dark"
        if(mirror == 'yes'):
            status_mirror = "Mirror"
            status_mirror_bg = "gray-800"

        advices = '<span class="badge bg-'+status_mirror_bg+'">Total '+status+' '+status_mirror+' Fixture(s) = '+str(total_fixtures)+'</span><br/> '
        
        advices += "<br/>" 
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
        # ------------------------------------------------------    
        # print(space + " " + "Asian Handicap : ")   
        if(asian_handicap_home_min_65_perc is not None and asian_handicap_home_min_65_perc >= 80):
            # --print(space + "   asian_handicap_home_min_65_perc:" + str(asian_handicap_home_min_65_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-65 - '+str('{:.0f}'.format(asian_handicap_home_min_65_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-65 - '+str('{:.0f}'.format(asian_handicap_home_min_65_perc))+'%</span> '

        elif(asian_handicap_home_min_6_perc is not None and asian_handicap_home_min_6_perc >= 80):
            # --print(space + "   asian_handicap_home_min_6_perc:" + str(asian_handicap_home_min_6_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-6 - '+str('{:.0f}'.format(asian_handicap_home_min_6_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-6 - '+str('{:.0f}'.format(asian_handicap_home_min_6_perc))+'%</span> '

        elif(asian_handicap_home_min_55_perc is not None and asian_handicap_home_min_55_perc >= 80):
            # --print(space + "   asian_handicap_home_min_55_perc:" + str(asian_handicap_home_min_55_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-55 - '+str('{:.0f}'.format(asian_handicap_home_min_55_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-55 - '+str('{:.0f}'.format(asian_handicap_home_min_55_perc))+'%</span> '

        elif(asian_handicap_home_min_5_perc is not None and asian_handicap_home_min_5_perc >= 80):
            # --print(space + "   asian_handicap_home_min_5_perc:" + str(asian_handicap_home_min_5_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-5 - '+str('{:.0f}'.format(asian_handicap_home_min_5_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-5 - '+str('{:.0f}'.format(asian_handicap_home_min_5_perc))+'%</span> '

        elif(asian_handicap_home_min_45_perc is not None and asian_handicap_home_min_45_perc >= 80):
            # --print(space + "   asian_handicap_home_min_45_perc:" + str(asian_handicap_home_min_45_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-45 - '+str('{:.0f}'.format(asian_handicap_home_min_45_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-45 - '+str('{:.0f}'.format(asian_handicap_home_min_45_perc))+'%</span> '

        elif(asian_handicap_home_min_4_perc is not None and asian_handicap_home_min_4_perc >= 80):
            # --print(space + "   asian_handicap_home_min_4_perc:" + str(asian_handicap_home_min_4_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-4 - '+str('{:.0f}'.format(asian_handicap_home_min_4_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-4 - '+str('{:.0f}'.format(asian_handicap_home_min_4_perc))+'%</span> '

        elif(asian_handicap_home_min_35_perc is not None and asian_handicap_home_min_35_perc >= 80):
            # --print(space + "   asian_handicap_home_min_35_perc:" + str(asian_handicap_home_min_35_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-35 - '+str('{:.0f}'.format(asian_handicap_home_min_35_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-35 - '+str('{:.0f}'.format(asian_handicap_home_min_35_perc))+'%</span> '

        elif(asian_handicap_home_min_3_perc is not None and asian_handicap_home_min_3_perc >= 80):
            # --print(space + "   asian_handicap_home_min_3_perc:" + str(asian_handicap_home_min_3_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-3 - '+str('{:.0f}'.format(asian_handicap_home_min_3_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-3 - '+str('{:.0f}'.format(asian_handicap_home_min_3_perc))+'%</span> '

        elif(asian_handicap_home_min_25_perc is not None and asian_handicap_home_min_25_perc >= 80):
            # --print(space + "   asian_handicap_home_min_25_perc:" + str(asian_handicap_home_min_25_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-25 - '+str('{:.0f}'.format(asian_handicap_home_min_25_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-25 - '+str('{:.0f}'.format(asian_handicap_home_min_25_perc))+'%</span> '

        elif(asian_handicap_home_min_2_perc is not None and asian_handicap_home_min_2_perc >= 80):
            # --print(space + "   asian_handicap_home_min_2_perc:" + str(asian_handicap_home_min_2_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-2 - '+str('{:.0f}'.format(asian_handicap_home_min_2_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-2 - '+str('{:.0f}'.format(asian_handicap_home_min_2_perc))+'%</span> '

        elif(asian_handicap_home_min_15_perc is not None and asian_handicap_home_min_15_perc >= 80):
            # --print(space + "   asian_handicap_home_min_15_perc:" + str(asian_handicap_home_min_15_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-15 - '+str('{:.0f}'.format(asian_handicap_home_min_15_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-15 - '+str('{:.0f}'.format(asian_handicap_home_min_15_perc))+'%</span> '

        elif(asian_handicap_home_min_1_perc is not None and asian_handicap_home_min_1_perc >= 80):
            # --print(space + "   asian_handicap_home_min_1_perc:" + str(asian_handicap_home_min_1_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-1 - '+str('{:.0f}'.format(asian_handicap_home_min_1_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-1 - '+str('{:.0f}'.format(asian_handicap_home_min_1_perc))+'%</span> '

        elif(asian_handicap_home_min_05_perc is not None and asian_handicap_home_min_05_perc >= 80):
            # --print(space + "   asian_handicap_home_min_05_perc:" + str(asian_handicap_home_min_05_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-05 - '+str('{:.0f}'.format(asian_handicap_home_min_05_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-05 - '+str('{:.0f}'.format(asian_handicap_home_min_05_perc))+'%</span> '

        # ------------------------------------------------------    
        # print(space + " " + "Over Under : ")    
 
        if(goals_overunder_over_95_perc is not None and goals_overunder_over_95_perc >= 80):
            # --print(space + "   goals_overunder_over_95_perc:" + str(goals_overunder_over_95_perc)) 
            advices += '<span class="badge bg-gradient-success">o95 - '+str('{:.0f}'.format(goals_overunder_over_95_perc))+'%</span> '

        elif(goals_overunder_over_85_perc is not None and goals_overunder_over_85_perc >= 80):
            # --print(space + "   goals_overunder_over_85_perc:" + str(goals_overunder_over_85_perc))
            advices += '<span class="badge bg-gradient-success">o85 - '+str('{:.0f}'.format(goals_overunder_over_85_perc))+'%</span> '

        elif(goals_overunder_over_75_perc is not None and goals_overunder_over_75_perc >= 80):
            # --print(space + "   goals_overunder_over_75_perc:" + str(goals_overunder_over_75_perc))
            advices += '<span class="badge bg-gradient-success">o75 - '+str('{:.0f}'.format(goals_overunder_over_75_perc))+'%</span> '

        elif(goals_overunder_over_70_perc is not None and goals_overunder_over_70_perc >= 80):
            # --print(space + "   goals_overunder_over_70_perc:" + str(goals_overunder_over_70_perc))
            advices += '<span class="badge bg-gradient-success">o70 - '+str('{:.0f}'.format(goals_overunder_over_70_perc))+'%</span> '

        elif(goals_overunder_over_65_perc is not None and goals_overunder_over_65_perc >= 80):
            # --print(space + "   goals_overunder_over_65_perc:" + str(goals_overunder_over_65_perc))
            advices += '<span class="badge bg-gradient-success">o65 - '+str('{:.0f}'.format(goals_overunder_over_65_perc))+'%</span> '

        elif(goals_overunder_over_60_perc is not None and goals_overunder_over_60_perc >= 80):
            # --print(space + "   goals_overunder_over_60_perc:" + str(goals_overunder_over_60_perc))
            advices += '<span class="badge bg-gradient-success">o60 - '+str('{:.0f}'.format(goals_overunder_over_60_perc))+'%</span> '

        elif(goals_overunder_over_55_perc is not None and goals_overunder_over_55_perc >= 80):
            # --print(space + "   goals_overunder_over_55_perc:" + str(goals_overunder_over_55_perc))
            advices += '<span class="badge bg-gradient-success">o55 - '+str('{:.0f}'.format(goals_overunder_over_55_perc))+'%</span> '

        elif(goals_overunder_over_50_perc is not None and goals_overunder_over_50_perc >= 80):
            # --print(space + "   goals_overunder_over_50_perc:" + str(goals_overunder_over_50_perc))
            advices += '<span class="badge bg-gradient-success">o50 - '+str('{:.0f}'.format(goals_overunder_over_50_perc))+'%</span> '

        elif(goals_overunder_over_45_perc is not None and goals_overunder_over_45_perc >= 80):
            # --print(space + "   goals_overunder_over_45_perc:" + str(goals_overunder_over_45_perc))
            advices += '<span class="badge bg-gradient-success">o45 - '+str('{:.0f}'.format(goals_overunder_over_45_perc))+'%</span> '

        elif(goals_overunder_over_40_perc is not None and goals_overunder_over_40_perc >= 80):
            # --print(space + "   goals_overunder_over_40_perc:" + str(goals_overunder_over_40_perc))
            advices += '<span class="badge bg-gradient-success">o40 - '+str('{:.0f}'.format(goals_overunder_over_40_perc))+'%</span> '

        elif(goals_overunder_over_35_perc is not None and goals_overunder_over_35_perc >= 80):
            # --print(space + "   goals_overunder_over_35_perc:" + str(goals_overunder_over_35_perc))
            advices += '<span class="badge bg-gradient-success">o35 - '+str('{:.0f}'.format(goals_overunder_over_35_perc))+'%</span> '

        elif(goals_overunder_over_30_perc is not None and goals_overunder_over_30_perc >= 80):
            # --print(space + "   goals_overunder_over_30_perc:" + str(goals_overunder_over_30_perc))
            advices += '<span class="badge bg-gradient-success">o30 - '+str('{:.0f}'.format(goals_overunder_over_30_perc))+'%</span> '

        elif(goals_overunder_over_25_perc is not None and goals_overunder_over_25_perc >= 80):
            # --print(space + "   goals_overunder_over_25_perc:" + str(goals_overunder_over_25_perc))
            advices += '<span class="badge bg-gradient-success">o25 - '+str('{:.0f}'.format(goals_overunder_over_25_perc))+'%</span> '

        elif(goals_overunder_over_20_perc is not None and goals_overunder_over_20_perc >= 80):
            # --print(space + "   goals_overunder_over_20_perc:" + str(goals_overunder_over_20_perc))
            advices += '<span class="badge bg-gradient-success">o20 - '+str('{:.0f}'.format(goals_overunder_over_20_perc))+'%</span> '

        elif(goals_overunder_over_15_perc is not None and goals_overunder_over_15_perc >= 80):
            # --print(space + "   goals_overunder_over_15_perc:" + str(goals_overunder_over_15_perc))
            advices += '<span class="badge bg-gradient-success">o15 - '+str('{:.0f}'.format(goals_overunder_over_15_perc))+'%</span> '

        elif(goals_overunder_over_10_perc is not None and goals_overunder_over_10_perc >= 80):
            # --print(space + "   goals_overunder_over_10_perc:" + str(goals_overunder_over_10_perc))
            advices += '<span class="badge bg-gradient-success">o10 - '+str('{:.0f}'.format(goals_overunder_over_10_perc))+'%</span> '

        elif(goals_overunder_over_05_perc is not None and goals_overunder_over_05_perc >= 80):
            # --print(space + "   goals_overunder_over_05_perc:" + str(goals_overunder_over_05_perc))
            advices += '<span class="badge bg-gradient-success">o05 - '+str('{:.0f}'.format(goals_overunder_over_05_perc))+'%</span> '
            
             
        if(goals_overunder_under_05_perc is not None and goals_overunder_under_05_perc >= 80):
            # --print(space + "   goals_overunder_under_05_perc:" + str(goals_overunder_under_05_perc)) 
            advices += '<span class="badge bg-gradient-danger">u05 - '+str('{:.0f}'.format(goals_overunder_under_05_perc))+'%</span> '

        elif(goals_overunder_under_10_perc is not None and goals_overunder_under_10_perc >= 80):
            # --print(space + "   goals_overunder_under_10_perc:" + str(goals_overunder_under_10_perc)) 
            advices += '<span class="badge bg-gradient-danger">u10 - '+str('{:.0f}'.format(goals_overunder_under_10_perc))+'%</span> '

        elif(goals_overunder_under_15_perc is not None and goals_overunder_under_15_perc >= 80):
            # --print(space + "   goals_overunder_under_15_perc:" + str(goals_overunder_under_15_perc)) 
            advices += '<span class="badge bg-gradient-danger">u15 - '+str('{:.0f}'.format(goals_overunder_under_15_perc))+'%</span> '

        elif(goals_overunder_under_20_perc is not None and goals_overunder_under_20_perc >= 80):
            # --print(space + "   goals_overunder_under_20_perc:" + str(goals_overunder_under_20_perc)) 
            advices += '<span class="badge bg-gradient-danger">u20 - '+str('{:.0f}'.format(goals_overunder_under_20_perc))+'%</span> '

        elif(goals_overunder_under_25_perc is not None and goals_overunder_under_25_perc >= 80):
            # --print(space + "   goals_overunder_under_25_perc:" + str(goals_overunder_under_25_perc)) 
            advices += '<span class="badge bg-gradient-danger">u25 - '+str('{:.0f}'.format(goals_overunder_under_25_perc))+'%</span> '

        elif(goals_overunder_under_30_perc is not None and goals_overunder_under_30_perc >= 80):
            # --print(space + "   goals_overunder_under_30_perc:" + str(goals_overunder_under_30_perc)) 
            advices += '<span class="badge bg-gradient-danger">u30 - '+str('{:.0f}'.format(goals_overunder_under_30_perc))+'%</span> '

        elif(goals_overunder_under_35_perc is not None and goals_overunder_under_35_perc >= 80):
            # --print(space + "   goals_overunder_under_35_perc:" + str(goals_overunder_under_35_perc)) 
            advices += '<span class="badge bg-gradient-danger">u35 - '+str('{:.0f}'.format(goals_overunder_under_35_perc))+'%</span> '

        elif(goals_overunder_under_40_perc is not None and goals_overunder_under_40_perc >= 80):
            # --print(space + "   goals_overunder_under_40_perc:" + str(goals_overunder_under_40_perc)) 
            advices += '<span class="badge bg-gradient-danger">u40 - '+str('{:.0f}'.format(goals_overunder_under_40_perc))+'%</span> '

        elif(goals_overunder_under_45_perc is not None and goals_overunder_under_45_perc >= 80):
            # --print(space + "   goals_overunder_under_45_perc:" + str(goals_overunder_under_45_perc)) 
            advices += '<span class="badge bg-gradient-danger">u45 - '+str('{:.0f}'.format(goals_overunder_under_45_perc))+'%</span> '

        elif(goals_overunder_under_50_perc is not None and goals_overunder_under_50_perc >= 80):
            # --print(space + "   goals_overunder_under_50_perc:" + str(goals_overunder_under_50_perc))
            advices += '<span class="badge bg-gradient-danger">u50 - '+str('{:.0f}'.format(goals_overunder_under_50_perc))+'%</span> '

        elif(goals_overunder_under_55_perc is not None and goals_overunder_under_55_perc >= 80):
            # --print(space + "   goals_overunder_under_55_perc:" + str(goals_overunder_under_55_perc)) 
            advices += '<span class="badge bg-gradient-danger">u55 - '+str('{:.0f}'.format(goals_overunder_under_55_perc))+'%</span> '

        elif(goals_overunder_under_60_perc is not None and goals_overunder_under_60_perc >= 80):
            # --print(space + "   goals_overunder_under_60_perc:" + str(goals_overunder_under_60_perc)) 
            advices += '<span class="badge bg-gradient-danger">u60 - '+str('{:.0f}'.format(goals_overunder_under_60_perc))+'%</span> '

        elif(goals_overunder_under_65_perc is not None and goals_overunder_under_65_perc >= 80):
            # --print(space + "   goals_overunder_under_65_perc:" + str(goals_overunder_under_65_perc))
            advices += '<span class="badge bg-gradient-danger">u65 - '+str('{:.0f}'.format(goals_overunder_under_65_perc))+'%</span> '

        elif(goals_overunder_under_70_perc is not None and goals_overunder_under_70_perc >= 80):
            # --print(space + "   goals_overunder_under_70_perc:" + str(goals_overunder_under_70_perc))
            advices += '<span class="badge bg-gradient-danger">u70 - '+str('{:.0f}'.format(goals_overunder_under_70_perc))+'%</span> '

        elif(goals_overunder_under_75_perc is not None and goals_overunder_under_75_perc >= 80):
            # --print(space + "   goals_overunder_under_75_perc:" + str(goals_overunder_under_75_perc))
            advices += '<span class="badge bg-gradient-danger">u75 - '+str('{:.0f}'.format(goals_overunder_under_75_perc))+'%</span> '

        elif(goals_overunder_under_85_perc is not None and goals_overunder_under_85_perc >= 80):
            # --print(space + "   goals_overunder_under_85_perc:" + str(goals_overunder_under_85_perc))
            advices += '<span class="badge bg-gradient-danger">u85 - '+str('{:.0f}'.format(goals_overunder_under_85_perc))+'%</span> '

        elif(goals_overunder_under_95_perc is not None and goals_overunder_under_95_perc >= 80):
            # --print(space + "   goals_overunder_under_95_perc:" + str(goals_overunder_under_95_perc))
            advices += '<span class="badge bg-gradient-danger">u95 - '+str('{:.0f}'.format(goals_overunder_under_95_perc))+'%</span> '
 
        
        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
        # ------------------------------------------------------    
        # print(space + " " + "Match Winner : ")      
        if(match_winner_home_perc is not None and match_winner_home_perc >= 80):
            # --print(space + "   match_winner_home_perc:" + str(match_winner_home_perc))   
            if(mirror == 'no'):
                advices += '<a href="" class="badge bg-gradient-primary">Hwin - '+str('{:.0f}'.format(match_winner_home_perc))+'%</a> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">Awin - '+str('{:.0f}'.format(match_winner_away_perc))+'%</span> '

        if(match_winner_draw_perc is not None and match_winner_draw_perc >= 80):
            # --print(space + "   match_winner_draw_perc:" + str(match_winner_draw_perc)) 
            advices += '<span class="badge bg-gray-700">Xdraw - '+str('{:.0f}'.format(match_winner_draw_perc))+'%</span> '

        if(match_winner_away_perc is not None and match_winner_away_perc >= 80):
            # --print(space + "   match_winner_away_perc:" + str(match_winner_away_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-warning">Awin - '+str('{:.0f}'.format(match_winner_away_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-primary">Hwin - '+str('{:.0f}'.format(match_winner_home_perc))+'%</span> '



        # ------------------------------------------------------    
        # print(space + " " + "homeaway : ")      
            
        if(homeaway_home_perc is not None and homeaway_home_perc >= 80):
            # --print(space + "   homeaway_home_perc:" + str(homeaway_home_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">Home0 - '+str('{:.0f}'.format(homeaway_home_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">Away0 - '+str('{:.0f}'.format(homeaway_away_perc))+'%</span> '

        if(homeaway_away_perc is not None and homeaway_away_perc >= 80):
            # --print(space + "   homeaway_away_perc:" + str(homeaway_away_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-warning">Away0 - '+str('{:.0f}'.format(homeaway_away_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-primary">Home0 - '+str('{:.0f}'.format(homeaway_home_perc))+'%</span> '


        # ------------------------------------------------------    
        # print(space + " " + "win_to_nil : ")     

        if(win_to_nil_home_perc is not None and win_to_nil_home_perc >= 80):
            # --print(space + "   win_to_nil_home_perc:" + str(win_to_nil_home_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">Hnil - '+str('{:.0f}'.format(win_to_nil_home_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">Anil - '+str('{:.0f}'.format(win_to_nil_away_perc))+'%</span> '

        if(win_to_nil_away_perc is not None and win_to_nil_away_perc >= 80):
            # --print(space + "   win_to_nil_away_perc:" + str(win_to_nil_away_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-warning">Anil - '+str('{:.0f}'.format(win_to_nil_away_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-primary">Hnil - '+str('{:.0f}'.format(win_to_nil_home_perc))+'%</span> '


        # ------------------------------------------------------    
        # print(space + " " + "to_win_either_half : ")     
	
        if(to_win_either_half_home_perc is not None and to_win_either_half_home_perc >= 80):
            # --print(space + "   to_win_either_half_home_perc:" + str(to_win_either_half_home_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-eithr - '+str('{:.0f}'.format(to_win_either_half_home_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-eithr - '+str('{:.0f}'.format(to_win_either_half_away_perc))+'%</span> '

        if(to_win_either_half_away_perc is not None and to_win_either_half_away_perc >= 80):
            # --print(space + "   to_win_either_half_away_perc:" + str(to_win_either_half_away_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-warning">A-eithr - '+str('{:.0f}'.format(to_win_either_half_away_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-primary">H-eithr - '+str('{:.0f}'.format(to_win_either_half_home_perc))+'%</span> '

        
        # ------------------------------------------------------    
        # print(space + " " + "win_both_halves : ")     
	
        if(win_both_halves_home_perc is not None and win_both_halves_home_perc >= 80):
            # --print(space + "   win_both_halves_home_perc:" + str(win_both_halves_home_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-primary">H-both - '+str('{:.0f}'.format(win_both_halves_home_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-warning">A-both - '+str('{:.0f}'.format(win_both_halves_away_perc))+'%</span> '

        if(win_both_halves_away_perc is not None and win_both_halves_away_perc >= 80):
            # --print(space + "   win_both_halves_away_perc:" + str(win_both_halves_away_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-warning">A-both - '+str('{:.0f}'.format(win_both_halves_away_perc))+'%</span> '
            if(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-primary">H-both - '+str('{:.0f}'.format(win_both_halves_home_perc))+'%</span> '

        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
            
        # if(asian_handicap_away_min_65_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_65_perc:" + str(asian_handicap_away_min_65_perc)) 
        # elif(asian_handicap_away_min_6_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_6_perc:" + str(asian_handicap_away_min_6_perc)) 
        # elif(asian_handicap_away_min_55_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_55_perc:" + str(asian_handicap_away_min_55_perc)) 
        # elif(asian_handicap_away_min_5_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_5_perc:" + str(asian_handicap_away_min_5_perc)) 
        # elif(asian_handicap_away_min_45_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_45_perc:" + str(asian_handicap_away_min_45_perc)) 
        # elif(asian_handicap_away_min_4_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_4_perc:" + str(asian_handicap_away_min_4_perc)) 
        # elif(asian_handicap_away_min_35_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_35_perc:" + str(asian_handicap_away_min_35_perc)) 
        # elif(asian_handicap_away_min_3_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_3_perc:" + str(asian_handicap_away_min_3_perc)) 
        # elif(asian_handicap_away_min_25_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_25_perc:" + str(asian_handicap_away_min_25_perc)) 
        # elif(asian_handicap_away_min_2_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_2_perc:" + str(asian_handicap_away_min_2_perc)) 
        # elif(asian_handicap_away_min_15_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_15_perc:" + str(asian_handicap_away_min_15_perc)) 
        # elif(asian_handicap_away_min_1_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_1_perc:" + str(asian_handicap_away_min_1_perc)) 
        # elif(asian_handicap_away_min_05_perc is not None and asian_handicap_away_min_05_perc >= 80):
        #     # --print(space + "   asian_handicap_away_min_05_perc:" + str(asian_handicap_away_min_05_perc))
            
        # if(asian_handicap_home_plus_0_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_0_perc:" + str(asian_handicap_home_plus_0_perc))
        # elif(asian_handicap_home_plus_05_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_05_perc:" + str(asian_handicap_home_plus_05_perc))
        # elif(asian_handicap_home_plus_1_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_1_perc:" + str(asian_handicap_home_plus_1_perc))
        # elif(asian_handicap_home_plus_15_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_15_perc:" + str(asian_handicap_home_plus_15_perc))
        # elif(asian_handicap_home_plus_2_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_2_perc:" + str(asian_handicap_home_plus_2_perc))
        # elif(asian_handicap_home_plus_25_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_25_perc:" + str(asian_handicap_home_plus_25_perc))
        # elif(asian_handicap_home_plus_3_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_3_perc:" + str(asian_handicap_home_plus_3_perc))
        # elif(asian_handicap_home_plus_35_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_35_perc:" + str(asian_handicap_home_plus_35_perc))
        # elif(asian_handicap_home_plus_4_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_4_perc:" + str(asian_handicap_home_plus_4_perc))
        # elif(asian_handicap_home_plus_45_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_45_perc:" + str(asian_handicap_home_plus_45_perc))
        # elif(asian_handicap_home_plus_5_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_5_perc:" + str(asian_handicap_home_plus_5_perc))
        # elif(asian_handicap_home_plus_55_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_55_perc:" + str(asian_handicap_home_plus_55_perc))
        # elif(asian_handicap_home_plus_6_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_6_perc:" + str(asian_handicap_home_plus_6_perc))
        # elif(asian_handicap_home_plus_65_perc >= 80):
        #     # --print(space + "   asian_handicap_home_plus_65_perc:" + str(asian_handicap_home_plus_65_perc))
            
        # if(asian_handicap_away_plus_0_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_0_perc:" + str(asian_handicap_away_plus_0_perc)) 
        # elif(asian_handicap_away_plus_05_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_05_perc:" + str(asian_handicap_away_plus_05_perc)) 
        # elif(asian_handicap_away_plus_1_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_1_perc:" + str(asian_handicap_away_plus_1_perc)) 
        # elif(asian_handicap_away_plus_15_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_15_perc:" + str(asian_handicap_away_plus_15_perc)) 
        # elif(asian_handicap_away_plus_2_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_2_perc:" + str(asian_handicap_away_plus_2_perc)) 
        # elif(asian_handicap_away_plus_25_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_25_perc:" + str(asian_handicap_away_plus_25_perc)) 
        # elif(asian_handicap_away_plus_3_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_3_perc:" + str(asian_handicap_away_plus_3_perc)) 
        # elif(asian_handicap_away_plus_35_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_35_perc:" + str(asian_handicap_away_plus_35_perc)) 
        # elif(asian_handicap_away_plus_4_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_4_perc:" + str(asian_handicap_away_plus_4_perc)) 
        # elif(asian_handicap_away_plus_45_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_45_perc:" + str(asian_handicap_away_plus_45_perc)) 
        # elif(asian_handicap_away_plus_5_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_5_perc:" + str(asian_handicap_away_plus_5_perc)) 
        # elif(asian_handicap_away_plus_55_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_55_perc:" + str(asian_handicap_away_plus_55_perc)) 
        # elif(asian_handicap_away_plus_6_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_6_perc:" + str(asian_handicap_away_plus_6_perc)) 
        # elif(asian_handicap_away_plus_65_perc >= 80):
        #     # --print(space + "   asian_handicap_away_plus_65_perc:" + str(asian_handicap_away_plus_65_perc))
        
        # ------------------------------------------------------    
        # print(space + " " + "exact_goals_number : ")   
	
        if(exact_goals_number_0_perc is not None and exact_goals_number_0_perc >= 80):
            # --print(space + "   exact_goals_number_0_perc:" + str(exact_goals_number_0_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-0 - '+str('{:.0f}'.format(exact_goals_number_0_perc))+'%</span> '

        if(exact_goals_number_1_perc is not None and exact_goals_number_1_perc >= 80):
            # --print(space + "   exact_goals_number_1_perc:" + str(exact_goals_number_1_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-1 - '+str('{:.0f}'.format(exact_goals_number_1_perc))+'%</span> '

        if(exact_goals_number_2_perc is not None and exact_goals_number_2_perc >= 80):
            # --print(space + "   exact_goals_number_2_perc:" + str(exact_goals_number_2_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-2 - '+str('{:.0f}'.format(exact_goals_number_2_perc))+'%</span> '

        if(exact_goals_number_3_perc is not None and exact_goals_number_3_perc >= 80):
            # --print(space + "   exact_goals_number_3_perc:" + str(exact_goals_number_3_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-3 - '+str('{:.0f}'.format(exact_goals_number_3_perc))+'%</span> '

        if(exact_goals_number_4_perc is not None and exact_goals_number_4_perc >= 80):
            # --print(space + "   exact_goals_number_4_perc:" + str(exact_goals_number_4_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-4 - '+str('{:.0f}'.format(exact_goals_number_4_perc))+'%</span> '

        if(exact_goals_number_5_perc is not None and exact_goals_number_5_perc >= 80):
            # --print(space + "   exact_goals_number_5_perc:" + str(exact_goals_number_5_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-5 - '+str('{:.0f}'.format(exact_goals_number_5_perc))+'%</span> '

        if(exact_goals_number_6_perc is not None and exact_goals_number_6_perc >= 80):
            # --print(space + "   exact_goals_number_6_perc:" + str(exact_goals_number_6_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">xG-6 - '+str('{:.0f}'.format(exact_goals_number_6_perc))+'%</span> '

        if(exact_goals_number_more_7_perc is not None and exact_goals_number_more_7_perc >= 80):
            # --print(space + "   exact_goals_number_more_7_perc:" + str(exact_goals_number_more_7_perc))  
            advices += '<span class="badge bg-gradient-gray-700">xG->7 - '+str('{:.0f}'.format(exact_goals_number_more_7_perc))+'%</span> '

            
        # ------------------------------------------------------    
        # print(space + " " + "home_team_exact_goals_number : ")     

        if(home_team_exact_goals_number_0_perc is not None and home_team_exact_goals_number_0_perc >= 80):
            # --print(space + "   home_team_exact_goals_number_0_perc:" + str(home_team_exact_goals_number_0_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-0 - '+str('{:.0f}'.format(home_team_exact_goals_number_0_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-0 - '+str('{:.0f}'.format(away_team_exact_goals_number_0_perc))+'%</span> '

        if(home_team_exact_goals_number_1_perc is not None and home_team_exact_goals_number_1_perc >= 80):
            # --print(space + "   home_team_exact_goals_number_1_perc:" + str(home_team_exact_goals_number_1_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-1 - '+str('{:.0f}'.format(home_team_exact_goals_number_1_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-1 - '+str('{:.0f}'.format(away_team_exact_goals_number_1_perc))+'%</span> '

        if(home_team_exact_goals_number_2_perc is not None and home_team_exact_goals_number_2_perc >= 80):
            # --print(space + "   home_team_exact_goals_number_2_perc:" + str(home_team_exact_goals_number_2_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-2 - '+str('{:.0f}'.format(home_team_exact_goals_number_2_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-2 - '+str('{:.0f}'.format(away_team_exact_goals_number_2_perc))+'%</span> '

        if(home_team_exact_goals_number_more_3_perc is not None and home_team_exact_goals_number_more_3_perc >= 80):
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgH->3 - '+str('{:.0f}'.format(home_team_exact_goals_number_more_3_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgA->3 - '+str('{:.0f}'.format(away_team_exact_goals_number_more_3_perc))+'%</span> '

            
        # ------------------------------------------------------    
        # print(space + " " + "away_team_exact_goals_number : ")    

        if(away_team_exact_goals_number_0_perc is not None and away_team_exact_goals_number_0_perc >= 80):
            # --print(space + "   away_team_exact_goals_number_0_perc:" + str(away_team_exact_goals_number_0_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-0 - '+str('{:.0f}'.format(away_team_exact_goals_number_0_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-0 - '+str('{:.0f}'.format(home_team_exact_goals_number_0_perc))+'%</span> '

        if(away_team_exact_goals_number_1_perc is not None and away_team_exact_goals_number_1_perc >= 80):
            # --print(space + "   away_team_exact_goals_number_1_perc:" + str(away_team_exact_goals_number_1_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-1 - '+str('{:.0f}'.format(away_team_exact_goals_number_1_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-1 - '+str('{:.0f}'.format(home_team_exact_goals_number_1_perc))+'%</span> '

        if(away_team_exact_goals_number_2_perc is not None and away_team_exact_goals_number_2_perc >= 80):
            # --print(space + "   away_team_exact_goals_number_2_perc:" + str(away_team_exact_goals_number_2_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgA-2 - '+str('{:.0f}'.format(away_team_exact_goals_number_2_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgH-2 - '+str('{:.0f}'.format(home_team_exact_goals_number_2_perc))+'%</span> '

        if(away_team_exact_goals_number_more_3_perc is not None and away_team_exact_goals_number_more_3_perc >= 80):
            # --print(space + "   away_team_exact_goals_number_more_3_perc:" + str(away_team_exact_goals_number_more_3_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-gray-700">xgA->3 - '+str('{:.0f}'.format(away_team_exact_goals_number_more_3_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-gray-700">xgH->3 - '+str('{:.0f}'.format(home_team_exact_goals_number_more_3_perc))+'%</span> '


            
        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 

            
        # ------------------------------------------------------    
        # print(space + " " + "htft_double : ")      
        
        # if(htft_double_home_home_perc >= 80):
        #     # --print(space + "   htft_double_home_home_perc:" + str(htft_double_home_home_perc)) 
        # if(htft_double_home_draw_perc >= 80):
        #     # --print(space + "   htft_double_home_draw_perc:" + str(htft_double_home_draw_perc)) 
        # if(htft_double_home_away_perc >= 80):
        #     # --print(space + "   htft_double_home_away_perc:" + str(htft_double_home_away_perc)) 
        # if(htft_double_draw_home_perc >= 80):
        #     # --print(space + "   htft_double_draw_home_perc:" + str(htft_double_draw_home_perc)) 
        # if(htft_double_draw_draw_perc >= 80):
        #     # --print(space + "   htft_double_draw_draw_perc:" + str(htft_double_draw_draw_perc)) 
        # if(htft_double_draw_away_perc >= 80):
        #     # --print(space + "   htft_double_draw_away_perc:" + str(htft_double_draw_away_perc)) 
        # if(htft_double_away_home_perc >= 80):
        #     # --print(space + "   htft_double_away_home_perc:" + str(htft_double_away_home_perc)) 
        # if(htft_double_away_draw_perc >= 80):
        #     # --print(space + "   htft_double_away_draw_perc:" + str(htft_double_away_draw_perc)) 
        # if(htft_double_away_away_perc >= 80):
        #     # --print(space + "   htft_double_away_away_perc:" + str(htft_double_away_away_perc))
        # ------------------------------------------------------    
        # print(space + " " + "both_teams_score : ")      
	
        if(both_teams_score_yes_perc is not None and both_teams_score_yes_perc >= 80):
            # --print(space + "   both_teams_score_yes_perc:" + str(both_teams_score_yes_perc))  
            advices += '<span class="badge bg-gradient-custom-teal">Bty - '+str('{:.0f}'.format(both_teams_score_yes_perc))+'%</span> '

        if(both_teams_score_no_perc is not None and both_teams_score_no_perc >= 80):
            # --print(space + "   both_teams_score_no_perc:" + str(both_teams_score_no_perc)) 
            advices += '<span class="badge bg-gradient-custom-pink">Btn - '+str('{:.0f}'.format(both_teams_score_no_perc))+'%</span> '
        
        # print(space + " " + "clean_sheet : ")       

        if(clean_sheet__home_yes_perc is not None and clean_sheet__home_yes_perc >= 80):
            # --print(space + "   clean_sheet__home_yes_perc:" + str(clean_sheet__home_yes_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-custom-pink">csy-H - '+str('{:.0f}'.format(clean_sheet__home_yes_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-custom-pink">csy-A - '+str('{:.0f}'.format(clean_sheet__away_yes_perc))+'%</span> '

        if(clean_sheet__home_no_perc is not None and clean_sheet__home_no_perc >= 80):
            # --print(space + "   clean_sheet__home_no_perc:" + str(clean_sheet__home_no_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-custom-teal">csn-H - '+str('{:.0f}'.format(clean_sheet__home_no_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-custom-teal">csn-A - '+str('{:.0f}'.format(clean_sheet__away_no_perc))+'%</span> '

        if(clean_sheet__away_yes_perc is not None and clean_sheet__away_yes_perc >= 80):
            # --print(space + "   clean_sheet__away_yes_perc:" + str(clean_sheet__away_yes_perc)) 
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-custom-pink">csy-A - '+str('{:.0f}'.format(clean_sheet__away_yes_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-custom-pink">csy-H - '+str('{:.0f}'.format(clean_sheet__home_yes_perc))+'%</span> '

        if(clean_sheet__away_no_perc is not None and clean_sheet__away_no_perc >= 80):
            # --print(space + "   clean_sheet__away_no_perc:" + str(clean_sheet__away_no_perc))
            if(mirror == 'no'):
                advices += '<span class="badge bg-gradient-custom-teal">csn-A - '+str('{:.0f}'.format(clean_sheet__away_no_perc))+'%</span> '
            elif(mirror == 'yes'):
                advices += '<span class="badge bg-gradient-custom-teal">csn-H - '+str('{:.0f}'.format(clean_sheet__home_no_perc))+'%</span> '

        # ------------------------------------------------------    
        # print(space + " " + "both_teams_score__first_half : ")    
	
        if(both_teams_score__first_half_yes_perc is not None and both_teams_score__first_half_yes_perc >= 80):
            # --print(space + "   both_teams_score__first_half_yes_perc:" + str(both_teams_score__first_half_yes_perc)) 
            advices += '<span class="badge bg-gradient-purple">1st-Bty - '+str('{:.0f}'.format(both_teams_score__first_half_yes_perc))+'%</span> '

        if(both_teams_score__first_half_no_perc is not None and both_teams_score__first_half_no_perc >= 80):
            # --print(space + "   both_teams_score__first_half_no_perc:" + str(both_teams_score__first_half_no_perc))  
            advices += '<span class="badge bg-gradient-warning">1st-Btn - '+str('{:.0f}'.format(both_teams_score__first_half_no_perc))+'%</span> '
        # ------------------------------------------------------    
        # print(space + " " + "both_teams_to_score__second_half : ")      
	
        if(both_teams_to_score__second_half_yes_perc is not None and both_teams_to_score__second_half_yes_perc >= 80):
            # --print(space + "   both_teams_to_score__second_half_yes_perc:" + str(both_teams_to_score__second_half_yes_perc)) 
            advices += '<span class="badge bg-gradient-purple">2nd-Bty - '+str('{:.0f}'.format(both_teams_to_score__second_half_yes_perc))+'%</span> '

        if(both_teams_to_score__second_half_no_perc is not None and both_teams_to_score__second_half_no_perc >= 80):
            # --print(space + "   both_teams_to_score__second_half_no_perc:" + str(both_teams_to_score__second_half_no_perc))
            advices += '<span class="badge bg-gradient-warning">2nd-Btn - '+str('{:.0f}'.format(both_teams_to_score__second_half_no_perc))+'%</span> '
        
        # ------------------------------------------------------  
        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
        # ------------------------------------------------------    
        # print(space + " " + "oddeven : ")     
	
        if(oddeven_odd_perc is not None and oddeven_odd_perc >= 80):
            # --print(space + "   oddeven_odd_perc:" + str(oddeven_odd_perc)) 
            advices += '<span class="badge bg-gradient-orange-red">odd - '+str('{:.0f}'.format(oddeven_odd_perc))+'%</span> '

        if(oddeven_even_perc is not None and oddeven_even_perc >= 80):
            # --print(space + "   oddeven_even_perc:" + str(oddeven_even_perc))
            advices += '<span class="badge bg-gradient-yellow-green">Even - '+str('{:.0f}'.format(oddeven_even_perc))+'%</span> '
        

        # print(space + " " + "highest_scoring_half : ")     
	
        if(highest_scoring_half_first_perc is not None and highest_scoring_half_first_perc >= 80):
            # --print(space + "   highest_scoring_half_first_perc:" + str(highest_scoring_half_first_perc)) 
            advices += '<span class="badge bg-gradient-purple">o1st - '+str('{:.0f}'.format(highest_scoring_half_first_perc))+'%</span> '

        if(highest_scoring_half_draw_perc is not None and highest_scoring_half_draw_perc >= 80):
            # --print(space + "   highest_scoring_half_draw_perc:" + str(highest_scoring_half_draw_perc)) 
            advices += '<span class="badge bg-gradient-gray-700">=half - '+str('{:.0f}'.format(highest_scoring_half_draw_perc))+'%</span> '

        if(highest_scoring_half_second_perc is not None and highest_scoring_half_second_perc >= 80):
            # --print(space + "   highest_scoring_half_second_perc:" + str(highest_scoring_half_second_perc))
            advices += '<span class="badge bg-gradient-warning">o2nd - '+str('{:.0f}'.format(highest_scoring_half_second_perc))+'%</span> '
            # ------------------------------------------------------    
               
        # print(space + " " + "exact_goals_number__first_half : ")   
	
        if(exact_goals_number__first_half_0_perc is not None and exact_goals_number__first_half_0_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_0_perc:" + str(exact_goals_number__first_half_0_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st-0 - '+str('{:.0f}'.format(exact_goals_number__first_half_0_perc))+'%</span> '

        if(exact_goals_number__first_half_1_perc is not None and exact_goals_number__first_half_1_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_1_perc:" + str(exact_goals_number__first_half_1_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st-1 - '+str('{:.0f}'.format(exact_goals_number__first_half_1_perc))+'%</span> '

        if(exact_goals_number__first_half_2_perc is not None and exact_goals_number__first_half_2_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_2_perc:" + str(exact_goals_number__first_half_2_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st-2 - '+str('{:.0f}'.format(exact_goals_number__first_half_2_perc))+'%</span> '

        if(exact_goals_number__first_half_3_perc is not None and exact_goals_number__first_half_3_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_3_perc:" + str(exact_goals_number__first_half_3_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st-3 - '+str('{:.0f}'.format(exact_goals_number__first_half_3_perc))+'%</span> '

        if(exact_goals_number__first_half_4_perc is not None and exact_goals_number__first_half_4_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_4_perc:" + str(exact_goals_number__first_half_4_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st-4 - '+str('{:.0f}'.format(exact_goals_number__first_half_4_perc))+'%</span> '

        if(exact_goals_number__first_half_more_5_perc is not None and exact_goals_number__first_half_more_5_perc >= 80):
            # --print(space + "   exact_goals_number__first_half_more_5_perc:" + str(exact_goals_number__first_half_more_5_perc)) 
            advices += '<span class="badge bg-gradient-purple">xG1st->5 - '+str('{:.0f}'.format(exact_goals_number__first_half_more_5_perc))+'%</span> '

        # ------------------------------------------------------    
        # print(space + " " + "second_half_exact_goals_number : ")     
	
        if(second_half_exact_goals_number_0_perc is not None and second_half_exact_goals_number_0_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_0_perc:" + str(second_half_exact_goals_number_0_perc)) 
            advices += '<span class="badge bg-gradient-warning">xG2nd-0 - '+str('{:.0f}'.format(second_half_exact_goals_number_0_perc))+'%</span> '
            
        if(second_half_exact_goals_number_1_perc is not None and second_half_exact_goals_number_1_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_1_perc:" + str(second_half_exact_goals_number_1_perc)) 
            advices += '<span class="badge bg-gradient-warning">xG2nd-1 - '+str('{:.0f}'.format(second_half_exact_goals_number_1_perc))+'%</span> '
            
        if(second_half_exact_goals_number_2_perc is not None and second_half_exact_goals_number_2_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_2_perc:" + str(second_half_exact_goals_number_2_perc)) 
            advices += '<span class="badge bg-gradient-warning">xG2nd-2 - '+str('{:.0f}'.format(second_half_exact_goals_number_2_perc))+'%</span> '
            
        if(second_half_exact_goals_number_3_perc is not None and second_half_exact_goals_number_3_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_3_perc:" + str(second_half_exact_goals_number_3_perc)) 
            advices += '<span class="badge bg-gradient-warning">xG2nd-3 - '+str('{:.0f}'.format(second_half_exact_goals_number_3_perc))+'%</span> '
            
        if(second_half_exact_goals_number_4_perc is not None and second_half_exact_goals_number_4_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_4_perc:" + str(second_half_exact_goals_number_4_perc)) 
            advices += '<span class="badge bg-gradient-warning">xG2nd-4 - '+str('{:.0f}'.format(second_half_exact_goals_number_4_perc))+'%</span> '
            
        if(second_half_exact_goals_number_more_5_perc is not None and second_half_exact_goals_number_more_5_perc >= 80):
            # --print(space + "   second_half_exact_goals_number_more_5_perc:" + str(second_half_exact_goals_number_more_5_perc))
            advices += '<span class="badge bg-gradient-warning">xG2nd->5 - '+str('{:.0f}'.format(second_half_exact_goals_number_more_5_perc))+'%</span> '
            
        # ------------------------------------------------------ 
        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
        # ------------------------------------------------------   
        # print(space + " " + "first_half_winner : ")     
	
        # if(first_half_winner_home_perc >= 80):
        #     # --print(space + "   first_half_winner_home_perc:" + str(first_half_winner_home_perc)) 
        # if(first_half_winner_draw_perc >= 80):
        #     # --print(space + "   first_half_winner_draw_perc:" + str(first_half_winner_draw_perc)) 
        # if(first_half_winner_away_perc >= 80):
        #     # --print(space + "   first_half_winner_away_perc:" + str(first_half_winner_away_perc)) 


        # ------------------------------------------------------    
        # print(space + " " + "Asian Handicap First Half : ")    
        # if(asian_handicap_first_half_home_min_15_perc is not None and asian_handicap_first_half_home_min_15_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_min_15_perc:" + str(asian_handicap_first_half_home_min_15_perc))
        # elif(asian_handicap_first_half_home_min_1_perc is not None and asian_handicap_first_half_home_min_1_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_min_1_perc:" + str(asian_handicap_first_half_home_min_1_perc))
        # elif(asian_handicap_first_half_home_min_05_perc is not None and asian_handicap_first_half_home_min_05_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_min_05_perc:" + str(asian_handicap_first_half_home_min_05_perc))
            
        # if(asian_handicap_first_half_away_min_15_perc is not None and asian_handicap_first_half_away_min_15_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_min_15_perc:" + str(asian_handicap_first_half_away_min_15_perc)) 
        # elif(asian_handicap_first_half_away_min_1_perc is not None and asian_handicap_first_half_away_min_1_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_min_1_perc:" + str(asian_handicap_first_half_away_min_1_perc)) 
        # elif(asian_handicap_first_half_away_min_05_perc is not None and asian_handicap_first_half_away_min_05_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_min_05_perc:" + str(asian_handicap_first_half_away_min_05_perc))
            
            
        # if(asian_handicap_first_half_home_plus_0_perc is not None and asian_handicap_first_half_home_plus_0_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_plus_0_perc:" + str(asian_handicap_first_half_home_plus_0_perc))
        # elif(asian_handicap_first_half_home_plus_05_perc is not None and asian_handicap_first_half_home_plus_05_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_plus_05_perc:" + str(asian_handicap_first_half_home_plus_05_perc))
        # elif(asian_handicap_first_half_home_plus_1_perc is not None and asian_handicap_first_half_home_plus_1_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_plus_1_perc:" + str(asian_handicap_first_half_home_plus_1_perc))
        # elif(asian_handicap_first_half_home_plus_15_perc is not None and asian_handicap_first_half_home_plus_15_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_home_plus_15_perc:" + str(asian_handicap_first_half_home_plus_15_perc))

        # if(asian_handicap_first_half_away_plus_0_perc is not None and asian_handicap_first_half_away_plus_0_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_plus_0_perc:" + str(asian_handicap_first_half_away_plus_0_perc))
        # elif(asian_handicap_first_half_away_plus_05_perc is not None and asian_handicap_first_half_away_plus_05_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_plus_05_perc:" + str(asian_handicap_first_half_away_plus_05_perc))
        # elif(asian_handicap_first_half_away_plus_1_perc is not None and asian_handicap_first_half_away_plus_1_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_plus_1_perc:" + str(asian_handicap_first_half_away_plus_1_perc)) 
        # elif(asian_handicap_first_half_away_plus_15_perc is not None and asian_handicap_first_half_away_plus_15_perc >= 80):
        #     # --print(space + "   asian_handicap_first_half_away_plus_15_perc:" + str(asian_handicap_first_half_away_plus_15_perc))

        # # ------------------------------------------------------    
        # # print(space + " " + "Over Under First Half : ")    
         
            
        # if(goals_overunder_first_half_under_05_perc is not None and goals_overunder_first_half_under_05_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_05_perc:" + str(goals_overunder_first_half_under_05_perc))
        # elif(goals_overunder_first_half_under_10_perc is not None and goals_overunder_first_half_under_10_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_10_perc:" + str(goals_overunder_first_half_under_10_perc))
        # elif(goals_overunder_first_half_under_15_perc is not None and goals_overunder_first_half_under_15_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_15_perc:" + str(goals_overunder_first_half_under_15_perc))
        # elif(goals_overunder_first_half_under_20_perc is not None and goals_overunder_first_half_under_20_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_20_perc:" + str(goals_overunder_first_half_under_20_perc))
        # elif(goals_overunder_first_half_under_25_perc is not None and goals_overunder_first_half_under_25_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_25_perc:" + str(goals_overunder_first_half_under_25_perc))
        # elif(goals_overunder_first_half_under_30_perc is not None and goals_overunder_first_half_under_30_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_30_perc:" + str(goals_overunder_first_half_under_30_perc))
        # elif(goals_overunder_first_half_under_35_perc is not None and goals_overunder_first_half_under_35_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_under_35_perc:" + str(goals_overunder_first_half_under_35_perc))
            
        # if(goals_overunder_first_half_over_35_perc is not None and goals_overunder_first_half_over_35_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_35_perc:" + str(goals_overunder_first_half_over_35_perc))
        # elif(goals_overunder_first_half_over_30_perc is not None and goals_overunder_first_half_over_30_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_30_perc:" + str(goals_overunder_first_half_over_30_perc))
        # elif(goals_overunder_first_half_over_25_perc is not None and goals_overunder_first_half_over_25_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_25_perc:" + str(goals_overunder_first_half_over_25_perc))
        # elif(goals_overunder_first_half_over_20_perc is not None and goals_overunder_first_half_over_20_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_20_perc:" + str(goals_overunder_first_half_over_20_perc))
        # elif(goals_overunder_first_half_over_15_perc is not None and goals_overunder_first_half_over_15_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_15_perc:" + str(goals_overunder_first_half_over_15_perc))
        # elif(goals_overunder_first_half_over_10_perc is not None and goals_overunder_first_half_over_10_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_10_perc:" + str(goals_overunder_first_half_over_10_perc))
        # elif(goals_overunder_first_half_over_05_perc is not None and goals_overunder_first_half_over_05_perc >= 80):
        #     # --print(space + "   goals_overunder_first_half_over_05_perc:" + str(goals_overunder_first_half_over_05_perc))
            
              
        # ------------------------------------------------------
        advices += "</div>"
        advices += '<div class="border-bottom border-secondary pt-2 pb-2">' 
        # ------------------------------------------------------   
        # print(space + " " + "second_half_winner : ")      

        # if(second_half_winner_home_perc >= 80):
        #     # --print(space + "   second_half_winner_home_perc:" + str(second_half_winner_home_perc)) 
        # if(second_half_winner_draw_perc >= 80):
        #     # --print(space + "   second_half_winner_draw_perc:" + str(second_half_winner_draw_perc)) 
        # if(second_half_winner_away_perc >= 80):
        #     # --print(space + "   second_half_winner_away_perc:" + str(second_half_winner_away_perc))
            

        # ------------------------------------------------------    
        # print(space + " " + "Over Under Second Half : ")     
        # if(goals_overunder__second_half_over_05_perc is not None and goals_overunder__second_half_over_05_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_05_perc:" + str(goals_overunder__second_half_over_05_perc))
            
        # if(goals_overunder__second_half_under_05_perc is not None and goals_overunder__second_half_under_05_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_05_perc:" + str(goals_overunder__second_half_under_05_perc))
            
        # if(goals_overunder__second_half_over_10_perc is not None and goals_overunder__second_half_over_10_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_10_perc:" + str(goals_overunder__second_half_over_10_perc))
            
        # if(goals_overunder__second_half_under_10_perc is not None and goals_overunder__second_half_under_10_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_10_perc:" + str(goals_overunder__second_half_under_10_perc))
            
        # if(goals_overunder__second_half_over_15_perc is not None and goals_overunder__second_half_over_15_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_15_perc:" + str(goals_overunder__second_half_over_15_perc))
            
        # if(goals_overunder__second_half_under_15_perc is not None and goals_overunder__second_half_under_15_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_15_perc:" + str(goals_overunder__second_half_under_15_perc))
            
        # if(goals_overunder__second_half_over_20_perc is not None and goals_overunder__second_half_over_20_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_20_perc:" + str(goals_overunder__second_half_over_20_perc))
            
        # if(goals_overunder__second_half_under_20_perc is not None and goals_overunder__second_half_under_20_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_20_perc::" + str(goals_overunder__second_half_under_20_perc))
            
        # if(goals_overunder__second_half_over_25_perc is not None and goals_overunder__second_half_over_25_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_25_perc:" + str(goals_overunder__second_half_over_25_perc))
            
        # if(goals_overunder__second_half_under_25_perc is not None and goals_overunder__second_half_under_25_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_25_perc:" + str(goals_overunder__second_half_under_25_perc))
            
        # if(goals_overunder__second_half_over_30_perc is not None and goals_overunder__second_half_over_30_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_30_perc:" + str(goals_overunder__second_half_over_30_perc))
            
        # if(goals_overunder__second_half_under_30_perc is not None and goals_overunder__second_half_under_30_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_30_perc:" + str(goals_overunder__second_half_under_30_perc))
            
        # if(goals_overunder__second_half_over_35_perc is not None and goals_overunder__second_half_over_35_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_over_35_perc:" + str(goals_overunder__second_half_over_35_perc))
            
        # if(goals_overunder__second_half_under_35_perc is not None and goals_overunder__second_half_under_35_perc >= 80):
        #     # --print(space + "   goals_overunder__second_half_under_35_perc:" + str(goals_overunder__second_half_under_35_perc))


        advices += "</div>" 



        # ------------------------------------------------------    
        # print(space + " " + "double_chance : ")      

        # if(double_chance_home_draw_perc is not None and double_chance_home_draw_perc >= 80):
        #     # --print(space + "   double_chance_home_draw_perc:" + str(double_chance_home_draw_perc)) 
        #     advices += "double_chance_home_draw=" + str(double_chance_home_draw_perc) + "; "
        # if(double_chance_home_away_perc is not None and double_chance_home_away_perc >= 80):
        #     # --print(space + "   double_chance_home_away_perc:" + str(double_chance_home_away_perc)) 
        #     advices += "double_chance_home_away=" + str(double_chance_home_away_perc) + "; "
        # if(double_chance_draw_away_perc is not None and double_chance_draw_away_perc >= 80):
        #     # --print(space + "   double_chance_draw_away_perc:" + str(double_chance_draw_away_perc))
        #     advices += "double_chance_draw_away=" + str(double_chance_draw_away_perc) + "; "
        # ------------------------------------------------------    
        # ------------------------------------------------------    
        # print(space + " " + "double_chance__first_half : ")     
	
        # if(aaa is not None and double_chance__first_half_home_draw_perc >= 80):
        #     # --print(space + "   double_chance__first_half_home_draw_perc:" + str(double_chance__first_half_home_draw_perc)) 
        # if(aaa is not None and double_chance__first_half_home_away_perc >= 80):
        #     # --print(space + "   double_chance__first_half_home_away_perc:" + str(double_chance__first_half_home_away_perc)) 
        # if(aaa is not None and double_chance__first_half_draw_away_perc >= 80):
        #     # --print(space + "   double_chance__first_half_draw_away_perc:" + str(double_chance__first_half_draw_away_perc))
        # ------------------------------------------------------    
        # print(space + " " + "results_both_teams_score : ")      
	
        # if(results_both_teams_score_home_yes_perc is not None and results_both_teams_score_home_yes_perc >= 80):
        #     # --print(space + "   results_both_teams_score_home_yes_perc:" + str(results_both_teams_score_home_yes_perc)) 
        # if(results_both_teams_score_draw_yes_perc is not None and results_both_teams_score_draw_yes_perc >= 80):
        #     # --print(space + "   results_both_teams_score_draw_yes_perc:" + str(results_both_teams_score_draw_yes_perc)) 
        # if(results_both_teams_score_away_yes_perc is not None and results_both_teams_score_away_yes_perc >= 80):
        #     # --print(space + "   results_both_teams_score_away_yes_perc:" + str(results_both_teams_score_away_yes_perc)) 
        # if(results_both_teams_score_home_no_perc is not None and results_both_teams_score_home_no_perc >= 80):
        #     # --print(space + "   results_both_teams_score_home_no_perc:" + str(results_both_teams_score_home_no_perc)) 
        # if(results_both_teams_score_draw_no_perc is not None and results_both_teams_score_draw_no_perc >= 80):
        #     # --print(space + "   results_both_teams_score_draw_no_perc:" + str(results_both_teams_score_draw_no_perc)) 
        # if(results_both_teams_score_away_no_perc is not None and results_both_teams_score_away_no_perc >= 80):
        #     # --print(space + "   results_both_teams_score_away_no_perc:" + str(results_both_teams_score_away_no_perc))
        # ------------------------------------------------------    
        # print(space + " " + "result_total_goals : ")      
	
        # if(aaa is not None and result_total_goals_home_over_35_perc >= 80):
        #     # --print(space + "   result_total_goals_home_over_35_perc:" + str(result_total_goals_home_over_35_perc)) 
        # if(result_total_goals_draw_over_35_perc >= 80):
        #     # --print(space + "   result_total_goals_draw_over_35_perc:" + str(result_total_goals_draw_over_35_perc)) 
        # if(aaa is not None and result_total_goals_away_over_35_perc >= 80):
        #     # --print(space + "   result_total_goals_away_over_35_perc:" + str(result_total_goals_away_over_35_perc)) 
        # if(aaa is not None and result_total_goals_home_under_35_perc >= 80):
        #     # --print(space + "   result_total_goals_home_under_35_perc:" + str(result_total_goals_home_under_35_perc)) 
        # if(aaa is not None and result_total_goals_draw_under_35_perc >= 80):
        #     # --print(space + "   result_total_goals_draw_under_35_perc:" + str(result_total_goals_draw_under_35_perc)) 
        # if(aaa is not None and result_total_goals_away_under_35_perc >= 80):
        #     # --print(space + "   result_total_goals_away_under_35_perc:" + str(result_total_goals_away_under_35_perc))
            
        # ------------------------------------------------------    
        # print(space + " " + "result_total_goals_home_over_25_perc : ")      
            
        # if(aaa is not None and result_total_goals_home_over_25_perc >= 80):
        #     # --print(space + "   result_total_goals_home_over_25_perc:" + str(result_total_goals_home_over_25_perc)) 
        # if(aaa is not None and result_total_goals_draw_over_25_perc >= 80):
        #     # --print(space + "   result_total_goals_draw_over_25_perc:" + str(result_total_goals_draw_over_25_perc)) 
        # if(aaa is not None and result_total_goals_away_over_25_perc >= 80):
        #     # --print(space + "   result_total_goals_away_over_25_perc:" + str(result_total_goals_away_over_25_perc)) 
        # if(aaa is not None and result_total_goals_home_under_25_perc >= 80):
        #     # --print(space + "   result_total_goals_home_under_25_perc:" + str(result_total_goals_home_under_25_perc)) 
        # if(aaa is not None and result_total_goals_draw_under_25_perc >= 80):
        #     # --print(space + "   result_total_goals_draw_under_25_perc:" + str(result_total_goals_draw_under_25_perc)) 
        # if(aaa is not None and result_total_goals_away_under_25_perc >= 80):
        #     # --print(space + "   result_total_goals_away_under_25_perc:" + str(result_total_goals_away_under_25_perc))
        
        # ------------------------------------------------------ 
        # ------------------------------------------------------    
        # print(space + " " + "to_score_in_both_halves_by_teams : ")    
	
        # if(aaa is not None and to_score_in_both_halves_by_teams_home_perc >= 80):
        #     # --print(space + "   to_score_in_both_halves_by_teams_home_perc:" + str(to_score_in_both_halves_by_teams_home_perc)) 
        # if(aaa is not None and to_score_in_both_halves_by_teams_away_perc >= 80):
        #     # --print(space + "   to_score_in_both_halves_by_teams_away_perc:" + str(to_score_in_both_halves_by_teams_away_perc)) 
        # ------------------------------------------------------    
        # print(space + " " + "total_goals_both_teams_to_score : ")     
        
	
        # if(aaa is not None and total_goals_both_teams_to_score_over_yes_25_perc >= 80):
        #     # --print(space + "   total_goals_both_teams_to_score_over_yes_25_perc:" + str(total_goals_both_teams_to_score_over_yes_25_perc))
            
        # if(aaa is not None and total_goals_both_teams_to_score_over_no_25_perc >= 80):
        #     # --print(space + "   total_goals_both_teams_to_score_over_no_25_perc:" + str(total_goals_both_teams_to_score_over_no_25_perc))
            
        # if(aaa is not None and total_goals_both_teams_to_score_under_yes_25_perc >= 80):
        #     # --print(space + "   total_goals_both_teams_to_score_under_yes_25_perc:" + str(total_goals_both_teams_to_score_under_yes_25_perc))
            
        # if(aaa is not None and total_goals_both_teams_to_score_under_no_25_perc >= 80):
        #     # --print(space + "   total_goals_both_teams_to_score_under_no_25_perc:" + str(total_goals_both_teams_to_score_under_no_25_perc))
        # ------------------------------------------------------    
        # print(space + " " + "halftime_result_both_teams_score : ")    
        
	
        # if(aaa is not None and halftime_result_both_teams_score_home_yes_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_home_yes_perc:" + str(halftime_result_both_teams_score_home_yes_perc)) 
        # if(aaa is not None and halftime_result_both_teams_score_draw_yes_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_draw_yes_perc:" + str(halftime_result_both_teams_score_draw_yes_perc)) 
        # if(aaa is not None and halftime_result_both_teams_score_away_yes_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_away_yes_perc:" + str(halftime_result_both_teams_score_away_yes_perc)) 
        # if(halftime_result_both_teams_score_home_no_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_home_no_perc:" + str(halftime_result_both_teams_score_home_no_perc)) 
        # if(aaa is not None and halftime_result_both_teams_score_draw_no_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_draw_no_perc:" + str(halftime_result_both_teams_score_draw_no_perc)) 
        # if(aaa is not None and halftime_result_both_teams_score_away_no_perc >= 80):
        #     # --print(space + "   halftime_result_both_teams_score_away_no_perc:" + str(halftime_result_both_teams_score_away_no_perc)) 
        # ------------------------------------------------------    
        # # print(space + " " + "both_teams_to_score_1st_half__2nd : ")     
        
	
        # if(aaa is not None and both_teams_to_score_1st_half__2nd_half_yes_yes_perc >= 80):
        #     # --print(space + "   both_teams_to_score_1st_half__2nd_half_yes_yes_perc:" + str(both_teams_to_score_1st_half__2nd_half_yes_yes_perc))
            
        # if(aaa is not None and both_teams_to_score_1st_half__2nd_half_yes_no_perc >= 80):
        #     # --print(space + "   both_teams_to_score_1st_half__2nd_half_yes_no_perc:" + str(both_teams_to_score_1st_half__2nd_half_yes_no_perc))
            
        # if(aaa is not None and both_teams_to_score_1st_half__2nd_half_no_yes_perc >= 80):
        #     # --print(space + "   both_teams_to_score_1st_half__2nd_half_no_yes_perc:" + str(both_teams_to_score_1st_half__2nd_half_no_yes_perc))
            
        # if(aaa is not None and both_teams_to_score_1st_half__2nd_half_no_no_perc >= 80):
        #     # --print(space + "   both_teams_to_score_1st_half__2nd_half_no_no_perc:" + str(both_teams_to_score_1st_half__2nd_half_no_no_perc))
            
        # ------------------------------------------------------    
        # # print(space + " " + "rcard : ")      
                
        # if(rcard_yes_perc is not None and rcard_yes_perc >= 80):
        #     # --print(space + "   rcard_yes_perc:" + str(rcard_yes_perc)) 
        # if(rcard_no_perc is not None and rcard_no_perc >= 80):
        #     # --print(space + "   rcard_no_perc:" + str(rcard_no_perc)) 
        # ------------------------------------------------------   
    # ----------------------------------------------------------
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ---------------------------------------------------------- 
    # print(space + "   " + advices)
    if(advices != ""):
        star = '<i class="fas fa-star text-yellow"></i>'
        update  = "UPDATE `football_fixtures` "

        if(mirror == "yes"):
            if(status == 'pre'):
                update += "SET `pre_advices_mirror` = '"+str(advices)+"', "
            elif(status == 'end'):
                update += "SET `end_advices_mirror` = '"+str(advices)+"', "

        elif(mirror == "no"):
            if(status == 'pre'):
                update += "SET `pre_advices` = '"+str(advices)+"', "
            elif(status == 'end'):
                update += "SET `end_advices` = '"+str(advices)+"', "


        star = '<i class="fas fa-star text-yellow"></i>'
        update += "  `star` = '"+str(star)+"' " 
    elif(advices == ""):
        update  = "UPDATE `football_fixtures` "
        if(mirror == "yes"):
            if(status == 'pre'):
                update += "SET `pre_advices_mirror` = Null "
            elif(status == 'end'):
                update += "SET `end_advices_mirror` = Null "
        elif(mirror == "no"):
            if(status == 'pre'):
                update += "SET `pre_advices` = Null "
            elif(status == 'end'):
                update += "SET `end_advices` = Null " 

 
    update += "WHERE `id` = "+str(idx)+" "
    # print(space + "   " + update)
    mycursor.execute(update)
    mydb.commit()  
    print(space + "   " + "--UPDATED--")
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

def pl_get_leagueapi_for_other_pattern(idx, leagueapi_id, pre_ah_pattern, pre_gou_pattern, space):
    # ---------------------------------------------------------- 
    space += "    "
    # ----------------------------------------------------------  
    print(space + "__pl_get_leagueapi_for_other_pattern__no_mirror" )
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query = " Select " 
    query += " pre_ah_pattern, "
    query += " pre_gou_pattern, " 
    query += " end_ah_pattern, "
    query += " end_gou_pattern " 
    query += " from pattern_lists "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "   
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ---------------------------------------------------------- 
    count_no = len(myresult)
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    print(space + "__pl_get_leagueapi_for_other_pattern__yes_mirror" )
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query = " Select " 
    query += " pre_ah_pattern, "
    query += " pre_gou_pattern, " 
    query += " end_ah_pattern, "
    query += " end_gou_pattern " 
    query += " from pattern_lists "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and pre_ah_pattern_mirror = '"+str(pre_ah_pattern)+"' "   
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    count_yes = len(myresult)
    # ---------------------------------------------------------- 
    count_total = count_no + count_yes 
    print(space + "counter:" + str(count_total))
    # ----------------------------------------------------------  
    if(count_total > 1): 
        star = '<i class="fas fa-star text-yellow"></i>'
        update  = "UPDATE `football_fixtures` "
        update += " SET `star` = '"+str(star)+"', "
        update += "  `other_pattern` = '"+str(count_total)+"' "
        update += " WHERE `id` = "+str(idx)+" "
        print(space + "   " + update)
        mycursor.execute(update)
        mydb.commit()  
        print(space + "   " + "--UPDATED--")