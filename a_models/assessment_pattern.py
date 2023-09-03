# Import     
import mysql.connector 
  
def aP_check_patternlist( 
        TABLE,
        leagueapi_id,   

        pre_ah_pattern,  
        pre_gou_pattern, 

        end_ah_pattern,  
        end_gou_pattern, 
        space):
    # ----------------------------------------------------------   
    space += "__"    
    # ----------------------------------------------------------  
    print(space + "aP_check_patternlist()", flush=True)
    # ----------------------------------------------------------  
    total_TABLE = "football_pattern_"+TABLE
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select * " 
    query += " from "+total_TABLE+" "     
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "    

    if(TABLE == "from"):
        query += " and `pre_ah_pattern` like '"+str(pre_ah_pattern)+"' "  
        query += " and `pre_gou_pattern` like '"+str(pre_gou_pattern)+"' "  
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
        
    elif(TABLE == "only"): 
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
    # ----------------------------------------------------------  
    # print(space + query)
    # ----------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # -------------------------------------------------- 
        space += "__"
        # -------------------------------------------------- 
        query = "INSERT INTO `"+total_TABLE+"`( " 
        # --------------------------------------------------  
        
        if(TABLE == "from"):
            # --------------------------------------------------  
            query += " `leagueapi_id`, " 

            query += " `pre_ah_pattern`, " 
            query += " `pre_gou_pattern`, "

            query += " `end_ah_pattern`, " 
            query += " `end_gou_pattern` "
            # -------------------------------------------------- 
            query += " ) VALUES ( " 
            # --------------------------------------------------  
            query += " '"+str(leagueapi_id)+"', " 
            # -------------------------------------------------- 
            query += " '"+str(pre_ah_pattern)+"', " 
            query += " '"+str(pre_gou_pattern)+"', "
            # -------------------------------------------------- 
            query += " '"+str(end_ah_pattern)+"', " 
            query += " '"+str(end_gou_pattern)+"' "
            # --------------------------------------------------  
            
        elif(TABLE == "only"): 
            # --------------------------------------------------  
            query += " `leagueapi_id`, " 
  
            query += " `end_ah_pattern`, " 
            query += " `end_gou_pattern` "
            # -------------------------------------------------- 
            query += " ) VALUES ( " 
            # --------------------------------------------------  
            query += " '"+str(leagueapi_id)+"', "  
            # -------------------------------------------------- 
            query += " '"+str(end_ah_pattern)+"', " 
            query += " '"+str(end_gou_pattern)+"' "
            # -------------------------------------------------- 
            
        query += " ) "
        # -------------------------------------------------- 
        # print(space + query, flush=True)
        mycursor.execute(query)
        mydb.commit() 
        # close the cursor and database connection
        mycursor.close()
        mydb.close()
        print(space + "__insert commited", flush=True)
    elif(total_rows != 0): 
        print(space + "__Already Data", flush=True)
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   

def aP_controll_pattern_ROUTE(TABLE, leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aP_controll_pattern_ROUTE()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " select "  
    query += " fixtureapi_id  "  
    query += " from `football_odds` "  
    query += " where `leagueapi_id` = "+str(leagueapi_id)+" "  

    if(TABLE == "from"):
        query += " and `pre_ah_pattern` like '"+str(pre_ah_pattern)+"' "  
        query += " and `pre_gou_pattern` like '"+str(pre_gou_pattern)+"' "  
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
        
    elif(TABLE == "only"): 
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    # space += "__"
    # ----------------------------------------------------------
    total_rows = len(result)    
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    aP_check_patternlist(TABLE, leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
    aP_final_assestment(query, TABLE, total_rows,
        leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
    # ----------------------------------------------------------
 
def aP_final_assestment(PRE_result, TABLE, PRE_total_rows,
        leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "aP_final_assestment()", flush=True) 
    # ----------------------------------------------------------  
    total_TABLE = "football_pattern_"+TABLE
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    SUM_match_winner_home = 0 
    SUM_match_winner_draw = 0 
    SUM_match_winner_away = 0 
    SUM_homeaway_home = 0 
    SUM_homeaway_away = 0 
    SUM_second_half_winner_home = 0 
    SUM_second_half_winner_draw = 0 
    SUM_second_half_winner_away = 0 
    SUM_asian_handicap_home_min_675 = 0 
    SUM_asian_handicap_away_min_675 = 0 
    SUM_asian_handicap_home_min_65 = 0 
    SUM_asian_handicap_away_min_65 = 0 
    SUM_asian_handicap_home_min_625 = 0 
    SUM_asian_handicap_away_min_625 = 0 
    SUM_asian_handicap_home_min_6 = 0 
    SUM_asian_handicap_away_min_6 = 0 
    SUM_asian_handicap_home_min_575 = 0 
    SUM_asian_handicap_away_min_575 = 0 
    SUM_asian_handicap_home_min_55 = 0 
    SUM_asian_handicap_away_min_55 = 0 
    SUM_asian_handicap_home_min_525 = 0 
    SUM_asian_handicap_away_min_525 = 0 
    SUM_asian_handicap_home_min_5 = 0 
    SUM_asian_handicap_away_min_5 = 0 
    SUM_asian_handicap_home_min_475 = 0 
    SUM_asian_handicap_away_min_475 = 0 
    SUM_asian_handicap_home_min_45 = 0 
    SUM_asian_handicap_away_min_45 = 0 
    SUM_asian_handicap_home_min_425 = 0 
    SUM_asian_handicap_away_min_425 = 0 
    SUM_asian_handicap_home_min_4 = 0 
    SUM_asian_handicap_away_min_4 = 0 
    SUM_asian_handicap_home_min_375 = 0 
    SUM_asian_handicap_away_min_375 = 0 
    SUM_asian_handicap_home_min_35 = 0 
    SUM_asian_handicap_away_min_35 = 0 
    SUM_asian_handicap_home_min_325 = 0 
    SUM_asian_handicap_away_min_325 = 0 
    SUM_asian_handicap_home_min_3 = 0 
    SUM_asian_handicap_away_min_3 = 0 
    SUM_asian_handicap_home_min_275 = 0 
    SUM_asian_handicap_away_min_275 = 0 
    SUM_asian_handicap_home_min_25 = 0 
    SUM_asian_handicap_away_min_25 = 0 
    SUM_asian_handicap_home_min_225 = 0 
    SUM_asian_handicap_away_min_225 = 0 
    SUM_asian_handicap_home_min_2 = 0 
    SUM_asian_handicap_away_min_2 = 0 
    SUM_asian_handicap_home_min_175 = 0 
    SUM_asian_handicap_away_min_175 = 0 
    SUM_asian_handicap_home_min_15 = 0 
    SUM_asian_handicap_away_min_15 = 0 
    SUM_asian_handicap_home_min_125 = 0 
    SUM_asian_handicap_away_min_125 = 0 
    SUM_asian_handicap_home_min_1 = 0 
    SUM_asian_handicap_away_min_1 = 0 
    SUM_asian_handicap_home_min_075 = 0 
    SUM_asian_handicap_away_min_075 = 0 
    SUM_asian_handicap_home_min_05 = 0 
    SUM_asian_handicap_away_min_05 = 0 
    SUM_asian_handicap_home_min_025 = 0 
    SUM_asian_handicap_away_min_025 = 0 
    SUM_asian_handicap_home_plus_0 = 0 
    SUM_asian_handicap_away_plus_0 = 0 
    SUM_asian_handicap_home_plus_025 = 0 
    SUM_asian_handicap_away_plus_025 = 0 
    SUM_asian_handicap_home_plus_05 = 0 
    SUM_asian_handicap_away_plus_05 = 0 
    SUM_asian_handicap_home_plus_075 = 0 
    SUM_asian_handicap_away_plus_075 = 0 
    SUM_asian_handicap_home_plus_1 = 0 
    SUM_asian_handicap_away_plus_1 = 0 
    SUM_asian_handicap_home_plus_125 = 0 
    SUM_asian_handicap_away_plus_125 = 0 
    SUM_asian_handicap_home_plus_15 = 0 
    SUM_asian_handicap_away_plus_15 = 0 
    SUM_asian_handicap_home_plus_175 = 0 
    SUM_asian_handicap_away_plus_175 = 0 
    SUM_asian_handicap_home_plus_2 = 0 
    SUM_asian_handicap_away_plus_2 = 0 
    SUM_asian_handicap_home_plus_225 = 0 
    SUM_asian_handicap_away_plus_225 = 0 
    SUM_asian_handicap_home_plus_25 = 0 
    SUM_asian_handicap_away_plus_25 = 0 
    SUM_asian_handicap_home_plus_275 = 0 
    SUM_asian_handicap_away_plus_275 = 0 
    SUM_asian_handicap_home_plus_3 = 0 
    SUM_asian_handicap_away_plus_3 = 0 
    SUM_asian_handicap_home_plus_325 = 0 
    SUM_asian_handicap_away_plus_325 = 0 
    SUM_asian_handicap_home_plus_35 = 0 
    SUM_asian_handicap_away_plus_35 = 0 
    SUM_asian_handicap_home_plus_375 = 0 
    SUM_asian_handicap_away_plus_375 = 0 
    SUM_asian_handicap_home_plus_4 = 0 
    SUM_asian_handicap_away_plus_4 = 0 
    SUM_asian_handicap_home_plus_425 = 0 
    SUM_asian_handicap_away_plus_425 = 0 
    SUM_asian_handicap_home_plus_45 = 0 
    SUM_asian_handicap_away_plus_45 = 0 
    SUM_asian_handicap_home_plus_475 = 0 
    SUM_asian_handicap_away_plus_475 = 0 
    SUM_asian_handicap_home_plus_5 = 0 
    SUM_asian_handicap_away_plus_5 = 0 
    SUM_asian_handicap_home_plus_525 = 0 
    SUM_asian_handicap_away_plus_525 = 0 
    SUM_asian_handicap_home_plus_55 = 0 
    SUM_asian_handicap_away_plus_55 = 0 
    SUM_asian_handicap_home_plus_575 = 0 
    SUM_asian_handicap_away_plus_575 = 0 
    SUM_asian_handicap_home_plus_6 = 0 
    SUM_asian_handicap_away_plus_6 = 0 
    SUM_asian_handicap_home_plus_625 = 0 
    SUM_asian_handicap_away_plus_625 = 0 
    SUM_asian_handicap_home_plus_65 = 0 
    SUM_asian_handicap_away_plus_65 = 0 
    SUM_asian_handicap_home_plus_675 = 0 
    SUM_asian_handicap_away_plus_675 = 0 
    SUM_goals_overunder_over_05 = 0 
    SUM_goals_overunder_under_05 = 0 
    SUM_goals_overunder_over_075 = 0 
    SUM_goals_overunder_under_075 = 0 
    SUM_goals_overunder_over_10 = 0 
    SUM_goals_overunder_under_10 = 0 
    SUM_goals_overunder_over_125 = 0 
    SUM_goals_overunder_under_125 = 0 
    SUM_goals_overunder_over_15 = 0 
    SUM_goals_overunder_under_15 = 0 
    SUM_goals_overunder_over_175 = 0 
    SUM_goals_overunder_under_175 = 0 
    SUM_goals_overunder_over_20 = 0 
    SUM_goals_overunder_under_20 = 0 
    SUM_goals_overunder_over_225 = 0 
    SUM_goals_overunder_under_225 = 0 
    SUM_goals_overunder_over_25 = 0 
    SUM_goals_overunder_under_25 = 0 
    SUM_goals_overunder_over_275 = 0 
    SUM_goals_overunder_under_275 = 0 
    SUM_goals_overunder_over_30 = 0 
    SUM_goals_overunder_under_30 = 0 
    SUM_goals_overunder_over_325 = 0 
    SUM_goals_overunder_under_325 = 0 
    SUM_goals_overunder_over_35 = 0 
    SUM_goals_overunder_under_35 = 0 
    SUM_goals_overunder_over_375 = 0 
    SUM_goals_overunder_under_375 = 0 
    SUM_goals_overunder_over_40 = 0 
    SUM_goals_overunder_under_40 = 0 
    SUM_goals_overunder_over_425 = 0 
    SUM_goals_overunder_under_425 = 0 
    SUM_goals_overunder_over_45 = 0 
    SUM_goals_overunder_under_45 = 0 
    SUM_goals_overunder_over_475 = 0 
    SUM_goals_overunder_under_475 = 0 
    SUM_goals_overunder_over_50 = 0 
    SUM_goals_overunder_under_50 = 0 
    SUM_goals_overunder_over_525 = 0 
    SUM_goals_overunder_under_525 = 0 
    SUM_goals_overunder_over_55 = 0 
    SUM_goals_overunder_under_55 = 0 
    SUM_goals_overunder_over_575 = 0 
    SUM_goals_overunder_under_575 = 0 
    SUM_goals_overunder_over_60 = 0 
    SUM_goals_overunder_under_60 = 0 
    SUM_goals_overunder_over_625 = 0 
    SUM_goals_overunder_under_625 = 0 
    SUM_goals_overunder_over_65 = 0 
    SUM_goals_overunder_under_65 = 0 
    SUM_goals_overunder_over_675 = 0 
    SUM_goals_overunder_under_675 = 0 
    SUM_goals_overunder_over_70 = 0 
    SUM_goals_overunder_under_70 = 0 
    SUM_goals_overunder_over_75 = 0 
    SUM_goals_overunder_under_75 = 0 
    SUM_goals_overunder_over_85 = 0 
    SUM_goals_overunder_under_85 = 0 
    SUM_goals_overunder_over_95 = 0 
    SUM_goals_overunder_under_95 = 0 
    SUM_goals_overunder_first_half_over_05 = 0 
    SUM_goals_overunder_first_half_under_05 = 0 
    SUM_goals_overunder_first_half_over_075 = 0 
    SUM_goals_overunder_first_half_under_075 = 0 
    SUM_goals_overunder_first_half_over_10 = 0 
    SUM_goals_overunder_first_half_under_10 = 0 
    SUM_goals_overunder_first_half_over_125 = 0 
    SUM_goals_overunder_first_half_under_125 = 0 
    SUM_goals_overunder_first_half_over_15 = 0 
    SUM_goals_overunder_first_half_under_15 = 0 
    SUM_goals_overunder_first_half_over_175 = 0 
    SUM_goals_overunder_first_half_under_175 = 0 
    SUM_goals_overunder_first_half_over_20 = 0 
    SUM_goals_overunder_first_half_under_20 = 0 
    SUM_goals_overunder_first_half_over_225 = 0 
    SUM_goals_overunder_first_half_under_225 = 0 
    SUM_goals_overunder_first_half_over_25 = 0 
    SUM_goals_overunder_first_half_under_25 = 0 
    SUM_goals_overunder_first_half_over_275 = 0 
    SUM_goals_overunder_first_half_under_275 = 0 
    SUM_goals_overunder_first_half_over_30 = 0 
    SUM_goals_overunder_first_half_under_30 = 0 
    SUM_goals_overunder_first_half_over_325 = 0 
    SUM_goals_overunder_first_half_under_325 = 0 
    SUM_goals_overunder_first_half_over_35 = 0 
    SUM_goals_overunder_first_half_under_35 = 0 
    SUM_goals_overunder_first_half_over_375 = 0 
    SUM_goals_overunder_first_half_under_375 = 0 
    SUM_htft_double_home_home = 0 
    SUM_htft_double_home_draw = 0 
    SUM_htft_double_home_away = 0 
    SUM_htft_double_draw_home = 0 
    SUM_htft_double_draw_draw = 0 
    SUM_htft_double_draw_away = 0 
    SUM_htft_double_away_home = 0 
    SUM_htft_double_away_draw = 0 
    SUM_htft_double_away_away = 0 
    SUM_both_teams_score_yes = 0 
    SUM_both_teams_score_no = 0 
    SUM_highest_scoring_half_first = 0 
    SUM_highest_scoring_half_draw = 0 
    SUM_highest_scoring_half_second = 0 
    SUM_double_chance_home_draw = 0 
    SUM_double_chance_home_away = 0 
    SUM_double_chance_draw_away = 0 
    SUM_first_half_winner_home = 0 
    SUM_first_half_winner_draw = 0 
    SUM_first_half_winner_away = 0 

    SUM_total_home_over_15 = 0 
    SUM_total_home_under_15 = 0 
    SUM_total_home_over_25 = 0 
    SUM_total_home_under_25 = 0 
    SUM_total_home_over_35 = 0 
    SUM_total_home_under_35 = 0 
    SUM_total_home_over_45 = 0 
    SUM_total_home_under_45 = 0 
    SUM_total_home_over_55 = 0 
    SUM_total_home_under_55 = 0 
    SUM_total_home_over_65 = 0 
    SUM_total_home_under_65 = 0 
    SUM_total_away_over_15 = 0 
    SUM_total_away_under_15 = 0 
    SUM_total_away_over_25 = 0 
    SUM_total_away_under_25 = 0 
    SUM_total_away_over_35 = 0 
    SUM_total_away_under_35 = 0 
    SUM_total_away_over_45 = 0 
    SUM_total_away_under_45 = 0 
    SUM_total_away_over_55 = 0 
    SUM_total_away_under_55 = 0 
    SUM_total_away_over_65 = 0 
    SUM_total_away_under_65 = 0 
    SUM_asian_handicap_first_half_home_min_175 = 0 
    SUM_asian_handicap_first_half_away_min_175 = 0 
    SUM_asian_handicap_first_half_home_min_15 = 0 
    SUM_asian_handicap_first_half_away_min_15 = 0 
    SUM_asian_handicap_first_half_home_min_125 = 0 
    SUM_asian_handicap_first_half_away_min_125 = 0 
    SUM_asian_handicap_first_half_home_min_1 = 0 
    SUM_asian_handicap_first_half_away_min_1 = 0 
    SUM_asian_handicap_first_half_home_min_075 = 0 
    SUM_asian_handicap_first_half_away_min_075 = 0 
    SUM_asian_handicap_first_half_home_min_05 = 0 
    SUM_asian_handicap_first_half_away_min_05 = 0 
    SUM_asian_handicap_first_half_home_min_025 = 0 
    SUM_asian_handicap_first_half_away_min_025 = 0 
    SUM_asian_handicap_first_half_home_plus_0 = 0 
    SUM_asian_handicap_first_half_away_plus_0 = 0 
    SUM_asian_handicap_first_half_home_plus_025 = 0 
    SUM_asian_handicap_first_half_away_plus_025 = 0 
    SUM_asian_handicap_first_half_home_plus_05 = 0 
    SUM_asian_handicap_first_half_away_plus_05 = 0 
    SUM_asian_handicap_first_half_home_plus_075 = 0 
    SUM_asian_handicap_first_half_away_plus_075 = 0 
    SUM_asian_handicap_first_half_home_plus_1 = 0 
    SUM_asian_handicap_first_half_away_plus_1 = 0 
    SUM_asian_handicap_first_half_home_plus_125 = 0 
    SUM_asian_handicap_first_half_away_plus_125 = 0 
    SUM_asian_handicap_first_half_home_plus_15 = 0 
    SUM_asian_handicap_first_half_away_plus_15 = 0 
    SUM_asian_handicap_first_half_home_plus_175 = 0 
    SUM_asian_handicap_first_half_away_plus_175 = 0 
    SUM_double_chance__first_half_home_draw = 0 
    SUM_double_chance__first_half_home_away = 0 
    SUM_double_chance__first_half_draw_away = 0 
    SUM_oddeven_odd = 0 
    SUM_oddeven_even = 0 
    SUM_results_both_teams_score_home_yes = 0 
    SUM_results_both_teams_score_draw_yes = 0 
    SUM_results_both_teams_score_away_yes = 0 
    SUM_results_both_teams_score_home_no = 0 
    SUM_results_both_teams_score_draw_no = 0 
    SUM_results_both_teams_score_away_no = 0 
    SUM_result_total_goals_home_over_35 = 0 
    SUM_result_total_goals_draw_over_35 = 0 
    SUM_result_total_goals_away_over_35 = 0 
    SUM_result_total_goals_home_under_35 = 0 
    SUM_result_total_goals_draw_under_35 = 0 
    SUM_result_total_goals_away_under_35 = 0 
    SUM_result_total_goals_home_over_25 = 0 
    SUM_result_total_goals_draw_over_25 = 0 
    SUM_result_total_goals_away_over_25 = 0 
    SUM_result_total_goals_home_under_25 = 0 
    SUM_result_total_goals_draw_under_25 = 0 
    SUM_result_total_goals_away_under_25 = 0 
    SUM_goals_overunder__second_half_over_05 = 0 
    SUM_goals_overunder__second_half_under_05 = 0 
    SUM_goals_overunder__second_half_over_075 = 0 
    SUM_goals_overunder__second_half_under_075 = 0 
    SUM_goals_overunder__second_half_over_10 = 0 
    SUM_goals_overunder__second_half_under_10 = 0 
    SUM_goals_overunder__second_half_over_125 = 0 
    SUM_goals_overunder__second_half_under_125 = 0 
    SUM_goals_overunder__second_half_over_15 = 0 
    SUM_goals_overunder__second_half_under_15 = 0 
    SUM_goals_overunder__second_half_over_175 = 0 
    SUM_goals_overunder__second_half_under_175 = 0 
    SUM_goals_overunder__second_half_over_20 = 0 
    SUM_goals_overunder__second_half_under_20 = 0 
    SUM_goals_overunder__second_half_over_225 = 0 
    SUM_goals_overunder__second_half_under_225 = 0 
    SUM_goals_overunder__second_half_over_25 = 0 
    SUM_goals_overunder__second_half_under_25 = 0 
    SUM_goals_overunder__second_half_over_275 = 0 
    SUM_goals_overunder__second_half_under_275 = 0 
    SUM_goals_overunder__second_half_over_30 = 0 
    SUM_goals_overunder__second_half_under_30 = 0 
    SUM_goals_overunder__second_half_over_325 = 0 
    SUM_goals_overunder__second_half_under_325 = 0 
    SUM_goals_overunder__second_half_over_35 = 0 
    SUM_goals_overunder__second_half_under_35 = 0 
    SUM_goals_overunder__second_half_over_375 = 0 
    SUM_goals_overunder__second_half_under_375 = 0 
    SUM_clean_sheet__home_yes = 0 
    SUM_clean_sheet__home_no = 0 
    SUM_clean_sheet__away_yes = 0 
    SUM_clean_sheet__away_no = 0 
    SUM_win_both_halves_home = 0 
    SUM_win_both_halves_away = 0 
    SUM_both_teams_score__first_half_yes = 0 
    SUM_both_teams_score__first_half_no = 0 
    SUM_both_teams_to_score__second_half_yes = 0 
    SUM_both_teams_to_score__second_half_no = 0 
    SUM_win_to_nil_home = 0 
    SUM_win_to_nil_away = 0 
    SUM_exact_goals_number_0 = 0 
    SUM_exact_goals_number_1 = 0 
    SUM_exact_goals_number_2 = 0 
    SUM_exact_goals_number_3 = 0 
    SUM_exact_goals_number_4 = 0 
    SUM_exact_goals_number_5 = 0 
    SUM_exact_goals_number_6 = 0 
    SUM_exact_goals_number_more_7 = 0 
    SUM_to_win_either_half_home = 0 
    SUM_to_win_either_half_away = 0 
    SUM_home_team_exact_goals_number_0 = 0 
    SUM_home_team_exact_goals_number_1 = 0 
    SUM_home_team_exact_goals_number_2 = 0 
    SUM_home_team_exact_goals_number_more_3 = 0 
    SUM_away_team_exact_goals_number_0 = 0 
    SUM_away_team_exact_goals_number_1 = 0 
    SUM_away_team_exact_goals_number_2 = 0 
    SUM_away_team_exact_goals_number_more_3 = 0 
    SUM_second_half_exact_goals_number_0 = 0 
    SUM_second_half_exact_goals_number_1 = 0 
    SUM_second_half_exact_goals_number_2 = 0 
    SUM_second_half_exact_goals_number_3 = 0 
    SUM_second_half_exact_goals_number_4 = 0 
    SUM_second_half_exact_goals_number_more_5 = 0 
    SUM_exact_goals_number__first_half_0 = 0 
    SUM_exact_goals_number__first_half_1 = 0 
    SUM_exact_goals_number__first_half_2 = 0 
    SUM_exact_goals_number__first_half_3 = 0 
    SUM_exact_goals_number__first_half_4 = 0 
    SUM_exact_goals_number__first_half_more_5 = 0 
    SUM_to_score_in_both_halves_by_teams_home = 0 
    SUM_to_score_in_both_halves_by_teams_away = 0 
    SUM_total_goals_both_teams_to_score_over_yes_25 = 0 
    SUM_total_goals_both_teams_to_score_over_no_25 = 0 
    SUM_total_goals_both_teams_to_score_under_yes_25 = 0 
    SUM_total_goals_both_teams_to_score_under_no_25 = 0 
    SUM_halftime_result_both_teams_score_home_yes = 0 
    SUM_halftime_result_both_teams_score_draw_yes = 0 
    SUM_halftime_result_both_teams_score_away_yes = 0 
    SUM_halftime_result_both_teams_score_home_no = 0 
    SUM_halftime_result_both_teams_score_draw_no = 0 
    SUM_halftime_result_both_teams_score_away_no = 0 
    SUM_both_teams_to_score_1st_half__2nd_half_yes_yes = 0 
    SUM_both_teams_to_score_1st_half__2nd_half_yes_no = 0 
    SUM_both_teams_to_score_1st_half__2nd_half_no_yes = 0 
    SUM_both_teams_to_score_1st_half__2nd_half_no_no = 0 
    SUM_total_goals_under_2 = 0 
    SUM_total_goals_2_or_3 = 0 
    SUM_total_goals_over_3 = 0 
    AVG_match_winner_home = 0
    AVG_match_winner_draw = 0
    AVG_match_winner_away = 0
    AVG_homeaway_home = 0
    AVG_homeaway_away = 0
    AVG_second_half_winner_home = 0
    AVG_second_half_winner_draw = 0
    AVG_second_half_winner_away = 0
    AVG_asian_handicap_home_min_675 = 0
    AVG_asian_handicap_away_min_675 = 0
    AVG_asian_handicap_home_min_65 = 0
    AVG_asian_handicap_away_min_65 = 0
    AVG_asian_handicap_home_min_625 = 0
    AVG_asian_handicap_away_min_625 = 0
    AVG_asian_handicap_home_min_6 = 0
    AVG_asian_handicap_away_min_6 = 0
    AVG_asian_handicap_home_min_575 = 0
    AVG_asian_handicap_away_min_575 = 0
    AVG_asian_handicap_home_min_55 = 0
    AVG_asian_handicap_away_min_55 = 0
    AVG_asian_handicap_home_min_525 = 0
    AVG_asian_handicap_away_min_525 = 0
    AVG_asian_handicap_home_min_5 = 0
    AVG_asian_handicap_away_min_5 = 0
    AVG_asian_handicap_home_min_475 = 0
    AVG_asian_handicap_away_min_475 = 0
    AVG_asian_handicap_home_min_45 = 0
    AVG_asian_handicap_away_min_45 = 0
    AVG_asian_handicap_home_min_425 = 0
    AVG_asian_handicap_away_min_425 = 0
    AVG_asian_handicap_home_min_4 = 0
    AVG_asian_handicap_away_min_4 = 0
    AVG_asian_handicap_home_min_375 = 0
    AVG_asian_handicap_away_min_375 = 0
    AVG_asian_handicap_home_min_35 = 0
    AVG_asian_handicap_away_min_35 = 0
    AVG_asian_handicap_home_min_325 = 0
    AVG_asian_handicap_away_min_325 = 0
    AVG_asian_handicap_home_min_3 = 0
    AVG_asian_handicap_away_min_3 = 0
    AVG_asian_handicap_home_min_275 = 0

    AVG_asian_handicap_away_min_275 = 0
    AVG_asian_handicap_home_min_25 = 0
    AVG_asian_handicap_away_min_25 = 0
    AVG_asian_handicap_home_min_225 = 0
    AVG_asian_handicap_away_min_225 = 0
    AVG_asian_handicap_home_min_2 = 0
    AVG_asian_handicap_away_min_2 = 0
    AVG_asian_handicap_home_min_175 = 0
    AVG_asian_handicap_away_min_175 = 0
    AVG_asian_handicap_home_min_15 = 0
    AVG_asian_handicap_away_min_15 = 0
    AVG_asian_handicap_home_min_125 = 0
    AVG_asian_handicap_away_min_125 = 0
    AVG_asian_handicap_home_min_1 = 0
    AVG_asian_handicap_away_min_1 = 0
    AVG_asian_handicap_home_min_075 = 0
    AVG_asian_handicap_away_min_075 = 0
    AVG_asian_handicap_home_min_05 = 0
    AVG_asian_handicap_away_min_05 = 0
    AVG_asian_handicap_home_min_025 = 0
    AVG_asian_handicap_away_min_025 = 0
    AVG_asian_handicap_home_plus_0 = 0
    AVG_asian_handicap_away_plus_0 = 0
    AVG_asian_handicap_home_plus_025 = 0
    AVG_asian_handicap_away_plus_025 = 0
    AVG_asian_handicap_home_plus_05 = 0
    AVG_asian_handicap_away_plus_05 = 0
    AVG_asian_handicap_home_plus_075 = 0
    AVG_asian_handicap_away_plus_075 = 0
    AVG_asian_handicap_home_plus_1 = 0
    AVG_asian_handicap_away_plus_1 = 0
    AVG_asian_handicap_home_plus_125 = 0
    AVG_asian_handicap_away_plus_125 = 0
    AVG_asian_handicap_home_plus_15 = 0
    AVG_asian_handicap_away_plus_15 = 0
    AVG_asian_handicap_home_plus_175 = 0
    AVG_asian_handicap_away_plus_175 = 0
    AVG_asian_handicap_home_plus_2 = 0
    AVG_asian_handicap_away_plus_2 = 0
    AVG_asian_handicap_home_plus_225 = 0
    AVG_asian_handicap_away_plus_225 = 0
    AVG_asian_handicap_home_plus_25 = 0
    AVG_asian_handicap_away_plus_25 = 0
    AVG_asian_handicap_home_plus_275 = 0
    AVG_asian_handicap_away_plus_275 = 0
    AVG_asian_handicap_home_plus_3 = 0
    AVG_asian_handicap_away_plus_3 = 0
    AVG_asian_handicap_home_plus_325 = 0
    AVG_asian_handicap_away_plus_325 = 0
    AVG_asian_handicap_home_plus_35 = 0
    AVG_asian_handicap_away_plus_35 = 0
    AVG_asian_handicap_home_plus_375 = 0
    AVG_asian_handicap_away_plus_375 = 0
    AVG_asian_handicap_home_plus_4 = 0
    AVG_asian_handicap_away_plus_4 = 0
    AVG_asian_handicap_home_plus_425 = 0
    AVG_asian_handicap_away_plus_425 = 0
    AVG_asian_handicap_home_plus_45 = 0
    AVG_asian_handicap_away_plus_45 = 0
    AVG_asian_handicap_home_plus_475 = 0
    AVG_asian_handicap_away_plus_475 = 0
    AVG_asian_handicap_home_plus_5 = 0
    AVG_asian_handicap_away_plus_5 = 0
    AVG_asian_handicap_home_plus_525 = 0
    AVG_asian_handicap_away_plus_525 = 0
    AVG_asian_handicap_home_plus_55 = 0
    AVG_asian_handicap_away_plus_55 = 0
    AVG_asian_handicap_home_plus_575 = 0
    AVG_asian_handicap_away_plus_575 = 0
    AVG_asian_handicap_home_plus_6 = 0
    AVG_asian_handicap_away_plus_6 = 0
    AVG_asian_handicap_home_plus_625 = 0
    AVG_asian_handicap_away_plus_625 = 0
    AVG_asian_handicap_home_plus_65 = 0
    AVG_asian_handicap_away_plus_65 = 0
    AVG_asian_handicap_home_plus_675 = 0
    AVG_asian_handicap_away_plus_675 = 0
    AVG_goals_overunder_over_05 = 0
    AVG_goals_overunder_under_05 = 0
    AVG_goals_overunder_over_075 = 0
    AVG_goals_overunder_under_075 = 0
    AVG_goals_overunder_over_10 = 0
    AVG_goals_overunder_under_10 = 0
    AVG_goals_overunder_over_125 = 0
    AVG_goals_overunder_under_125 = 0
    AVG_goals_overunder_over_15 = 0
    AVG_goals_overunder_under_15 = 0
    AVG_goals_overunder_over_175 = 0
    AVG_goals_overunder_under_175 = 0
    AVG_goals_overunder_over_20 = 0
    AVG_goals_overunder_under_20 = 0
    AVG_goals_overunder_over_225 = 0
    AVG_goals_overunder_under_225 = 0
    AVG_goals_overunder_over_25 = 0
    AVG_goals_overunder_under_25 = 0
    AVG_goals_overunder_over_275 = 0
    AVG_goals_overunder_under_275 = 0
    AVG_goals_overunder_over_30 = 0
    AVG_goals_overunder_under_30 = 0
    AVG_goals_overunder_over_325 = 0
    AVG_goals_overunder_under_325 = 0
    AVG_goals_overunder_over_35 = 0
    AVG_goals_overunder_under_35 = 0
    AVG_goals_overunder_over_375 = 0
    AVG_goals_overunder_under_375 = 0
    AVG_goals_overunder_over_40 = 0
    AVG_goals_overunder_under_40 = 0
    AVG_goals_overunder_over_425 = 0
    AVG_goals_overunder_under_425 = 0
    AVG_goals_overunder_over_45 = 0
    AVG_goals_overunder_under_45 = 0
    AVG_goals_overunder_over_475 = 0
    AVG_goals_overunder_under_475 = 0
    AVG_goals_overunder_over_50 = 0
    AVG_goals_overunder_under_50 = 0
    AVG_goals_overunder_over_525 = 0
    AVG_goals_overunder_under_525 = 0
    AVG_goals_overunder_over_55 = 0
    AVG_goals_overunder_under_55 = 0
    AVG_goals_overunder_over_575 = 0
    AVG_goals_overunder_under_575 = 0
    AVG_goals_overunder_over_60 = 0
    AVG_goals_overunder_under_60 = 0
    AVG_goals_overunder_over_625 = 0
    AVG_goals_overunder_under_625 = 0
    AVG_goals_overunder_over_65 = 0
    AVG_goals_overunder_under_65 = 0
    AVG_goals_overunder_over_675 = 0
    AVG_goals_overunder_under_675 = 0
    AVG_goals_overunder_over_70 = 0
    AVG_goals_overunder_under_70 = 0
    AVG_goals_overunder_over_75 = 0
    AVG_goals_overunder_under_75 = 0
    AVG_goals_overunder_over_85 = 0
    AVG_goals_overunder_under_85 = 0
    AVG_goals_overunder_over_95 = 0
    AVG_goals_overunder_under_95 = 0
    AVG_goals_overunder_first_half_over_05 = 0
    AVG_goals_overunder_first_half_under_05 = 0
    AVG_goals_overunder_first_half_over_075 = 0
    AVG_goals_overunder_first_half_under_075 = 0
    AVG_goals_overunder_first_half_over_10 = 0
    AVG_goals_overunder_first_half_under_10 = 0
    AVG_goals_overunder_first_half_over_125 = 0
    AVG_goals_overunder_first_half_under_125 = 0
    AVG_goals_overunder_first_half_over_15 = 0
    AVG_goals_overunder_first_half_under_15 = 0
    AVG_goals_overunder_first_half_over_175 = 0
    AVG_goals_overunder_first_half_under_175 = 0
    AVG_goals_overunder_first_half_over_20 = 0
    AVG_goals_overunder_first_half_under_20 = 0
    AVG_goals_overunder_first_half_over_225 = 0
    AVG_goals_overunder_first_half_under_225 = 0
    AVG_goals_overunder_first_half_over_25 = 0
    AVG_goals_overunder_first_half_under_25 = 0
    AVG_goals_overunder_first_half_over_275 = 0
    AVG_goals_overunder_first_half_under_275 = 0
    AVG_goals_overunder_first_half_over_30 = 0
    AVG_goals_overunder_first_half_under_30 = 0
    AVG_goals_overunder_first_half_over_325 = 0
    AVG_goals_overunder_first_half_under_325 = 0
    AVG_goals_overunder_first_half_over_35 = 0
    AVG_goals_overunder_first_half_under_35 = 0
    AVG_goals_overunder_first_half_over_375 = 0
    AVG_goals_overunder_first_half_under_375 = 0
    AVG_htft_double_home_home = 0
    AVG_htft_double_home_draw = 0
    AVG_htft_double_home_away = 0
    AVG_htft_double_draw_home = 0
    AVG_htft_double_draw_draw = 0
    AVG_htft_double_draw_away = 0
    AVG_htft_double_away_home = 0
    AVG_htft_double_away_draw = 0
    AVG_htft_double_away_away = 0
    AVG_both_teams_score_yes = 0
    AVG_both_teams_score_no = 0
    AVG_highest_scoring_half_first = 0
    AVG_highest_scoring_half_draw = 0
    AVG_highest_scoring_half_second = 0
    AVG_double_chance_home_draw = 0
    AVG_double_chance_home_away = 0
    AVG_double_chance_draw_away = 0
    AVG_first_half_winner_home = 0
    AVG_first_half_winner_draw = 0
    AVG_first_half_winner_away = 0
    AVG_total_home_over_15 = 0
    AVG_total_home_under_15 = 0
    AVG_total_home_over_25 = 0
    AVG_total_home_under_25 = 0
    AVG_total_home_over_35 = 0
    AVG_total_home_under_35 = 0
    AVG_total_home_over_45 = 0
    AVG_total_home_under_45 = 0
    AVG_total_home_over_55 = 0
    AVG_total_home_under_55 = 0
    AVG_total_home_over_65 = 0
    AVG_total_home_under_65 = 0
    AVG_total_away_over_15 = 0
    AVG_total_away_under_15 = 0
    AVG_total_away_over_25 = 0
    AVG_total_away_under_25 = 0
    AVG_total_away_over_35 = 0
    AVG_total_away_under_35 = 0
    AVG_total_away_over_45 = 0
    AVG_total_away_under_45 = 0
    AVG_total_away_over_55 = 0
    AVG_total_away_under_55 = 0
    AVG_total_away_over_65 = 0
    AVG_total_away_under_65 = 0
    AVG_asian_handicap_first_half_home_min_175 = 0
    AVG_asian_handicap_first_half_away_min_175 = 0
    AVG_asian_handicap_first_half_home_min_15 = 0
    AVG_asian_handicap_first_half_away_min_15 = 0
    AVG_asian_handicap_first_half_home_min_125 = 0
    AVG_asian_handicap_first_half_away_min_125 = 0
    AVG_asian_handicap_first_half_home_min_1 = 0
    AVG_asian_handicap_first_half_away_min_1 = 0
    AVG_asian_handicap_first_half_home_min_075 = 0
    AVG_asian_handicap_first_half_away_min_075 = 0
    AVG_asian_handicap_first_half_home_min_05 = 0
    AVG_asian_handicap_first_half_away_min_05 = 0
    AVG_asian_handicap_first_half_home_min_025 = 0
    AVG_asian_handicap_first_half_away_min_025 = 0
    AVG_asian_handicap_first_half_home_plus_0 = 0
    AVG_asian_handicap_first_half_away_plus_0 = 0
    AVG_asian_handicap_first_half_home_plus_025 = 0
    AVG_asian_handicap_first_half_away_plus_025 = 0
    AVG_asian_handicap_first_half_home_plus_05 = 0
    AVG_asian_handicap_first_half_away_plus_05 = 0

    AVG_asian_handicap_first_half_home_plus_075 = 0
    AVG_asian_handicap_first_half_away_plus_075 = 0
    AVG_asian_handicap_first_half_home_plus_1 = 0
    AVG_asian_handicap_first_half_away_plus_1 = 0
    AVG_asian_handicap_first_half_home_plus_125 = 0
    AVG_asian_handicap_first_half_away_plus_125 = 0
    AVG_asian_handicap_first_half_home_plus_15 = 0
    AVG_asian_handicap_first_half_away_plus_15 = 0
    AVG_asian_handicap_first_half_home_plus_175 = 0
    AVG_asian_handicap_first_half_away_plus_175 = 0
    AVG_double_chance__first_half_home_draw = 0
    AVG_double_chance__first_half_home_away = 0
    AVG_double_chance__first_half_draw_away = 0
    AVG_oddeven_odd = 0
    AVG_oddeven_even = 0
    AVG_results_both_teams_score_home_yes = 0
    AVG_results_both_teams_score_draw_yes = 0
    AVG_results_both_teams_score_away_yes = 0
    AVG_results_both_teams_score_home_no = 0
    AVG_results_both_teams_score_draw_no = 0
    AVG_results_both_teams_score_away_no = 0
    AVG_result_total_goals_home_over_35 = 0
    AVG_result_total_goals_draw_over_35 = 0
    AVG_result_total_goals_away_over_35 = 0
    AVG_result_total_goals_home_under_35 = 0
    AVG_result_total_goals_draw_under_35 = 0
    AVG_result_total_goals_away_under_35 = 0
    AVG_result_total_goals_home_over_25 = 0
    AVG_result_total_goals_draw_over_25 = 0
    AVG_result_total_goals_away_over_25 = 0
    AVG_result_total_goals_home_under_25 = 0
    AVG_result_total_goals_draw_under_25 = 0
    AVG_result_total_goals_away_under_25 = 0
    AVG_goals_overunder__second_half_over_05 = 0
    AVG_goals_overunder__second_half_under_05 = 0
    AVG_goals_overunder__second_half_over_075 = 0
    AVG_goals_overunder__second_half_under_075 = 0
    AVG_goals_overunder__second_half_over_10 = 0
    AVG_goals_overunder__second_half_under_10 = 0
    AVG_goals_overunder__second_half_over_125 = 0
    AVG_goals_overunder__second_half_under_125 = 0
    AVG_goals_overunder__second_half_over_15 = 0
    AVG_goals_overunder__second_half_under_15 = 0
    AVG_goals_overunder__second_half_over_175 = 0
    AVG_goals_overunder__second_half_under_175 = 0
    AVG_goals_overunder__second_half_over_20 = 0
    AVG_goals_overunder__second_half_under_20 = 0
    AVG_goals_overunder__second_half_over_225 = 0
    AVG_goals_overunder__second_half_under_225 = 0
    AVG_goals_overunder__second_half_over_25 = 0
    AVG_goals_overunder__second_half_under_25 = 0
    AVG_goals_overunder__second_half_over_275 = 0
    AVG_goals_overunder__second_half_under_275 = 0
    AVG_goals_overunder__second_half_over_30 = 0
    AVG_goals_overunder__second_half_under_30 = 0
    AVG_goals_overunder__second_half_over_325 = 0
    AVG_goals_overunder__second_half_under_325 = 0
    AVG_goals_overunder__second_half_over_35 = 0
    AVG_goals_overunder__second_half_under_35 = 0
    AVG_goals_overunder__second_half_over_375 = 0
    AVG_goals_overunder__second_half_under_375 = 0
    AVG_clean_sheet__home_yes = 0
    AVG_clean_sheet__home_no = 0
    AVG_clean_sheet__away_yes = 0
    AVG_clean_sheet__away_no = 0
    AVG_win_both_halves_home = 0
    AVG_win_both_halves_away = 0
    AVG_both_teams_score__first_half_yes = 0
    AVG_both_teams_score__first_half_no = 0
    AVG_both_teams_to_score__second_half_yes = 0
    AVG_both_teams_to_score__second_half_no = 0
    AVG_win_to_nil_home = 0
    AVG_win_to_nil_away = 0
    AVG_exact_goals_number_0 = 0
    AVG_exact_goals_number_1 = 0
    AVG_exact_goals_number_2 = 0
    AVG_exact_goals_number_3 = 0
    AVG_exact_goals_number_4 = 0
    AVG_exact_goals_number_5 = 0
    AVG_exact_goals_number_6 = 0
    AVG_exact_goals_number_more_7 = 0
    AVG_to_win_either_half_home = 0
    AVG_to_win_either_half_away = 0
    AVG_home_team_exact_goals_number_0 = 0
    AVG_home_team_exact_goals_number_1 = 0
    AVG_home_team_exact_goals_number_2 = 0
    AVG_home_team_exact_goals_number_more_3 = 0
    AVG_away_team_exact_goals_number_0 = 0
    AVG_away_team_exact_goals_number_1 = 0
    AVG_away_team_exact_goals_number_2 = 0
    AVG_away_team_exact_goals_number_more_3 = 0
    AVG_second_half_exact_goals_number_0 = 0
    AVG_second_half_exact_goals_number_1 = 0
    AVG_second_half_exact_goals_number_2 = 0
    AVG_second_half_exact_goals_number_3 = 0
    AVG_second_half_exact_goals_number_4 = 0
    AVG_second_half_exact_goals_number_more_5 = 0
    AVG_exact_goals_number__first_half_0 = 0
    AVG_exact_goals_number__first_half_1 = 0
    AVG_exact_goals_number__first_half_2 = 0
    AVG_exact_goals_number__first_half_3 = 0
    AVG_exact_goals_number__first_half_4 = 0
    AVG_exact_goals_number__first_half_more_5 = 0
    AVG_to_score_in_both_halves_by_teams_home = 0
    AVG_to_score_in_both_halves_by_teams_away = 0
    AVG_total_goals_both_teams_to_score_over_yes_25 = 0
    AVG_total_goals_both_teams_to_score_over_no_25 = 0
    AVG_total_goals_both_teams_to_score_under_yes_25 = 0
    AVG_total_goals_both_teams_to_score_under_no_25 = 0
    AVG_halftime_result_both_teams_score_home_yes = 0
    AVG_halftime_result_both_teams_score_draw_yes = 0
    AVG_halftime_result_both_teams_score_away_yes = 0
    AVG_halftime_result_both_teams_score_home_no = 0
    AVG_halftime_result_both_teams_score_draw_no = 0
    AVG_halftime_result_both_teams_score_away_no = 0
    AVG_both_teams_to_score_1st_half__2nd_half_yes_yes = 0
    AVG_both_teams_to_score_1st_half__2nd_half_yes_no = 0
    AVG_both_teams_to_score_1st_half__2nd_half_no_yes = 0
    AVG_both_teams_to_score_1st_half__2nd_half_no_no = 0
    AVG_total_goals_under_2 = 0
    AVG_total_goals_2_or_3 = 0
    AVG_total_goals_over_3 = 0

    # ----------------------------------------------------------    
    query = "Select  "
    query += " SUM(match_winner_home), "
    query += " SUM(match_winner_draw), "
    query += " SUM(match_winner_away), "
    query += " SUM(homeaway_home), "
    query += " SUM(homeaway_away), "
    query += " SUM(second_half_winner_home), "
    query += " SUM(second_half_winner_draw), "
    query += " SUM(second_half_winner_away), "
    query += " SUM(asian_handicap_home_min_675), "
    query += " SUM(asian_handicap_away_min_675), "
    query += " SUM(asian_handicap_home_min_65), "
    query += " SUM(asian_handicap_away_min_65), "
    query += " SUM(asian_handicap_home_min_625), "
    query += " SUM(asian_handicap_away_min_625), "
    query += " SUM(asian_handicap_home_min_6), "
    query += " SUM(asian_handicap_away_min_6), "
    query += " SUM(asian_handicap_home_min_575), "
    query += " SUM(asian_handicap_away_min_575), "
    query += " SUM(asian_handicap_home_min_55), "
    query += " SUM(asian_handicap_away_min_55), "
    query += " SUM(asian_handicap_home_min_525), "
    query += " SUM(asian_handicap_away_min_525), "
    query += " SUM(asian_handicap_home_min_5), "
    query += " SUM(asian_handicap_away_min_5), "
    query += " SUM(asian_handicap_home_min_475), "
    query += " SUM(asian_handicap_away_min_475), "
    query += " SUM(asian_handicap_home_min_45), "
    query += " SUM(asian_handicap_away_min_45), "
    query += " SUM(asian_handicap_home_min_425), "
    query += " SUM(asian_handicap_away_min_425), "
    query += " SUM(asian_handicap_home_min_4), "
    query += " SUM(asian_handicap_away_min_4), "
    query += " SUM(asian_handicap_home_min_375), "
    query += " SUM(asian_handicap_away_min_375), "
    query += " SUM(asian_handicap_home_min_35), "
    query += " SUM(asian_handicap_away_min_35), "
    query += " SUM(asian_handicap_home_min_325), "
    query += " SUM(asian_handicap_away_min_325), "
    query += " SUM(asian_handicap_home_min_3), "
    query += " SUM(asian_handicap_away_min_3), "
    query += " SUM(asian_handicap_home_min_275), "
    query += " SUM(asian_handicap_away_min_275), "
    query += " SUM(asian_handicap_home_min_25), "
    query += " SUM(asian_handicap_away_min_25), "
    query += " SUM(asian_handicap_home_min_225), "
    query += " SUM(asian_handicap_away_min_225), "
    query += " SUM(asian_handicap_home_min_2), "
    query += " SUM(asian_handicap_away_min_2), "
    query += " SUM(asian_handicap_home_min_175), "
    query += " SUM(asian_handicap_away_min_175), "
    query += " SUM(asian_handicap_home_min_15), "
    query += " SUM(asian_handicap_away_min_15), "
    query += " SUM(asian_handicap_home_min_125), "
    query += " SUM(asian_handicap_away_min_125), "
    query += " SUM(asian_handicap_home_min_1), "
    query += " SUM(asian_handicap_away_min_1), "
    query += " SUM(asian_handicap_home_min_075), "
    query += " SUM(asian_handicap_away_min_075), "
    query += " SUM(asian_handicap_home_min_05), "
    query += " SUM(asian_handicap_away_min_05), "
    query += " SUM(asian_handicap_home_min_025), "
    query += " SUM(asian_handicap_away_min_025), "
    query += " SUM(asian_handicap_home_plus_0), "
    query += " SUM(asian_handicap_away_plus_0), "
    query += " SUM(asian_handicap_home_plus_025), "
    query += " SUM(asian_handicap_away_plus_025), "
    query += " SUM(asian_handicap_home_plus_05), "
    query += " SUM(asian_handicap_away_plus_05), "
    query += " SUM(asian_handicap_home_plus_075), "
    query += " SUM(asian_handicap_away_plus_075), "
    query += " SUM(asian_handicap_home_plus_1), "
    query += " SUM(asian_handicap_away_plus_1), "
    query += " SUM(asian_handicap_home_plus_125), "
    query += " SUM(asian_handicap_away_plus_125), "
    query += " SUM(asian_handicap_home_plus_15), "
    query += " SUM(asian_handicap_away_plus_15), "
    query += " SUM(asian_handicap_home_plus_175), "
    query += " SUM(asian_handicap_away_plus_175), "
    query += " SUM(asian_handicap_home_plus_2), "
    query += " SUM(asian_handicap_away_plus_2), "
    query += " SUM(asian_handicap_home_plus_225), "
    query += " SUM(asian_handicap_away_plus_225), "
    query += " SUM(asian_handicap_home_plus_25), "
    query += " SUM(asian_handicap_away_plus_25), "
    query += " SUM(asian_handicap_home_plus_275), "
    query += " SUM(asian_handicap_away_plus_275), "
    query += " SUM(asian_handicap_home_plus_3), "
    query += " SUM(asian_handicap_away_plus_3), "
    query += " SUM(asian_handicap_home_plus_325), "
    query += " SUM(asian_handicap_away_plus_325), "
    query += " SUM(asian_handicap_home_plus_35), "
    query += " SUM(asian_handicap_away_plus_35), "
    query += " SUM(asian_handicap_home_plus_375), "
    query += " SUM(asian_handicap_away_plus_375), "
    query += " SUM(asian_handicap_home_plus_4), "
    query += " SUM(asian_handicap_away_plus_4), "
    query += " SUM(asian_handicap_home_plus_425), "
    query += " SUM(asian_handicap_away_plus_425), "
    query += " SUM(asian_handicap_home_plus_45), "
    query += " SUM(asian_handicap_away_plus_45), "
    query += " SUM(asian_handicap_home_plus_475), "
    query += " SUM(asian_handicap_away_plus_475), "
    query += " SUM(asian_handicap_home_plus_5), "
    query += " SUM(asian_handicap_away_plus_5), "
    query += " SUM(asian_handicap_home_plus_525), "
    query += " SUM(asian_handicap_away_plus_525), "
    query += " SUM(asian_handicap_home_plus_55), "
    query += " SUM(asian_handicap_away_plus_55), "
    query += " SUM(asian_handicap_home_plus_575), "
    query += " SUM(asian_handicap_away_plus_575), "
    query += " SUM(asian_handicap_home_plus_6), "
    query += " SUM(asian_handicap_away_plus_6), "
    query += " SUM(asian_handicap_home_plus_625), "
    query += " SUM(asian_handicap_away_plus_625), "
    query += " SUM(asian_handicap_home_plus_65), "
    query += " SUM(asian_handicap_away_plus_65), "
    query += " SUM(asian_handicap_home_plus_675), "
    query += " SUM(asian_handicap_away_plus_675), "
    query += " SUM(goals_overunder_over_05), "
    query += " SUM(goals_overunder_under_05), "
    query += " SUM(goals_overunder_over_075), "
    query += " SUM(goals_overunder_under_075), "
    query += " SUM(goals_overunder_over_10), "
    query += " SUM(goals_overunder_under_10), "
    query += " SUM(goals_overunder_over_125), "
    query += " SUM(goals_overunder_under_125), "
    query += " SUM(goals_overunder_over_15), "
    query += " SUM(goals_overunder_under_15), "
    query += " SUM(goals_overunder_over_175), "
    query += " SUM(goals_overunder_under_175), "
    query += " SUM(goals_overunder_over_20), "
    query += " SUM(goals_overunder_under_20), "
    query += " SUM(goals_overunder_over_225), "
    query += " SUM(goals_overunder_under_225), "
    query += " SUM(goals_overunder_over_25), "
    query += " SUM(goals_overunder_under_25), "
    query += " SUM(goals_overunder_over_275), "
    query += " SUM(goals_overunder_under_275), "
    query += " SUM(goals_overunder_over_30), "
    query += " SUM(goals_overunder_under_30), "
    query += " SUM(goals_overunder_over_325), "
    query += " SUM(goals_overunder_under_325), "
    query += " SUM(goals_overunder_over_35), "
    query += " SUM(goals_overunder_under_35), "
    query += " SUM(goals_overunder_over_375), "
    query += " SUM(goals_overunder_under_375), "
    query += " SUM(goals_overunder_over_40), "
    query += " SUM(goals_overunder_under_40), "
    query += " SUM(goals_overunder_over_425), "
    query += " SUM(goals_overunder_under_425), "
    query += " SUM(goals_overunder_over_45), "
    query += " SUM(goals_overunder_under_45), "
    query += " SUM(goals_overunder_over_475), "
    query += " SUM(goals_overunder_under_475), "
    query += " SUM(goals_overunder_over_50), "
    query += " SUM(goals_overunder_under_50), "
    query += " SUM(goals_overunder_over_525), "
    query += " SUM(goals_overunder_under_525), "
    query += " SUM(goals_overunder_over_55), "
    query += " SUM(goals_overunder_under_55), "
    query += " SUM(goals_overunder_over_575), "
    query += " SUM(goals_overunder_under_575), "
    query += " SUM(goals_overunder_over_60), "
    query += " SUM(goals_overunder_under_60), "
    query += " SUM(goals_overunder_over_625), "
    query += " SUM(goals_overunder_under_625), "
    query += " SUM(goals_overunder_over_65), "
    query += " SUM(goals_overunder_under_65), "
    query += " SUM(goals_overunder_over_675), "
    query += " SUM(goals_overunder_under_675), "
    query += " SUM(goals_overunder_over_70), "
    query += " SUM(goals_overunder_under_70), "
    query += " SUM(goals_overunder_over_75), "
    query += " SUM(goals_overunder_under_75), "
    query += " SUM(goals_overunder_over_85), "
    query += " SUM(goals_overunder_under_85), "
    query += " SUM(goals_overunder_over_95), "
    query += " SUM(goals_overunder_under_95), "
    query += " SUM(goals_overunder_first_half_over_05), "
    query += " SUM(goals_overunder_first_half_under_05), "

    query += " SUM(goals_overunder_first_half_over_075), "
    query += " SUM(goals_overunder_first_half_under_075), "
    query += " SUM(goals_overunder_first_half_over_10), "
    query += " SUM(goals_overunder_first_half_under_10), "
    query += " SUM(goals_overunder_first_half_over_125), "
    query += " SUM(goals_overunder_first_half_under_125), "
    query += " SUM(goals_overunder_first_half_over_15), "
    query += " SUM(goals_overunder_first_half_under_15), "
    query += " SUM(goals_overunder_first_half_over_175), "
    query += " SUM(goals_overunder_first_half_under_175), "
    query += " SUM(goals_overunder_first_half_over_20), "
    query += " SUM(goals_overunder_first_half_under_20), "
    query += " SUM(goals_overunder_first_half_over_225), "
    query += " SUM(goals_overunder_first_half_under_225), "
    query += " SUM(goals_overunder_first_half_over_25), "
    query += " SUM(goals_overunder_first_half_under_25), "
    query += " SUM(goals_overunder_first_half_over_275), "
    query += " SUM(goals_overunder_first_half_under_275), "
    query += " SUM(goals_overunder_first_half_over_30), "
    query += " SUM(goals_overunder_first_half_under_30), "
    query += " SUM(goals_overunder_first_half_over_325), "
    query += " SUM(goals_overunder_first_half_under_325), "
    query += " SUM(goals_overunder_first_half_over_35), "
    query += " SUM(goals_overunder_first_half_under_35), "
    query += " SUM(goals_overunder_first_half_over_375), "
    query += " SUM(goals_overunder_first_half_under_375), "
    query += " SUM(htft_double_home_home), "
    query += " SUM(htft_double_home_draw), "
    query += " SUM(htft_double_home_away), "
    query += " SUM(htft_double_draw_home), "
    query += " SUM(htft_double_draw_draw), "
    query += " SUM(htft_double_draw_away), "
    query += " SUM(htft_double_away_home), "
    query += " SUM(htft_double_away_draw), "
    query += " SUM(htft_double_away_away), "
    query += " SUM(both_teams_score_yes), "
    query += " SUM(both_teams_score_no), "
    query += " SUM(highest_scoring_half_first), "
    query += " SUM(highest_scoring_half_draw), "
    query += " SUM(highest_scoring_half_second), "
    query += " SUM(double_chance_home_draw), "
    query += " SUM(double_chance_home_away), "
    query += " SUM(double_chance_draw_away), "
    query += " SUM(first_half_winner_home), "
    query += " SUM(first_half_winner_draw), "
    query += " SUM(first_half_winner_away), "
    query += " SUM(total_home_over_15), "
    query += " SUM(total_home_under_15), "
    query += " SUM(total_home_over_25), "
    query += " SUM(total_home_under_25), "
    query += " SUM(total_home_over_35), "
    query += " SUM(total_home_under_35), "
    query += " SUM(total_home_over_45), "
    query += " SUM(total_home_under_45), "
    query += " SUM(total_home_over_55), "
    query += " SUM(total_home_under_55), "
    query += " SUM(total_home_over_65), "
    query += " SUM(total_home_under_65), "
    query += " SUM(total_away_over_15), "
    query += " SUM(total_away_under_15), "
    query += " SUM(total_away_over_25), "
    query += " SUM(total_away_under_25), "
    query += " SUM(total_away_over_35), "
    query += " SUM(total_away_under_35), "
    query += " SUM(total_away_over_45), "
    query += " SUM(total_away_under_45), "
    query += " SUM(total_away_over_55), "
    query += " SUM(total_away_under_55), "
    query += " SUM(total_away_over_65), "
    query += " SUM(total_away_under_65), "
    query += " SUM(asian_handicap_first_half_home_min_175), "
    query += " SUM(asian_handicap_first_half_away_min_175), "
    query += " SUM(asian_handicap_first_half_home_min_15), "
    query += " SUM(asian_handicap_first_half_away_min_15), "
    query += " SUM(asian_handicap_first_half_home_min_125), "
    query += " SUM(asian_handicap_first_half_away_min_125), "
    query += " SUM(asian_handicap_first_half_home_min_1), "
    query += " SUM(asian_handicap_first_half_away_min_1), "
    query += " SUM(asian_handicap_first_half_home_min_075), "
    query += " SUM(asian_handicap_first_half_away_min_075), "
    query += " SUM(asian_handicap_first_half_home_min_05), "
    query += " SUM(asian_handicap_first_half_away_min_05), "
    query += " SUM(asian_handicap_first_half_home_min_025), "
    query += " SUM(asian_handicap_first_half_away_min_025), "
    query += " SUM(asian_handicap_first_half_home_plus_0), "
    query += " SUM(asian_handicap_first_half_away_plus_0), "
    query += " SUM(asian_handicap_first_half_home_plus_025), "
    query += " SUM(asian_handicap_first_half_away_plus_025), "
    query += " SUM(asian_handicap_first_half_home_plus_05), "
    query += " SUM(asian_handicap_first_half_away_plus_05), "
    query += " SUM(asian_handicap_first_half_home_plus_075), "
    query += " SUM(asian_handicap_first_half_away_plus_075), "
    query += " SUM(asian_handicap_first_half_home_plus_1), "
    query += " SUM(asian_handicap_first_half_away_plus_1), "
    query += " SUM(asian_handicap_first_half_home_plus_125), "
    query += " SUM(asian_handicap_first_half_away_plus_125), "
    query += " SUM(asian_handicap_first_half_home_plus_15), "
    query += " SUM(asian_handicap_first_half_away_plus_15), "
    query += " SUM(asian_handicap_first_half_home_plus_175), "
    query += " SUM(asian_handicap_first_half_away_plus_175), "
    query += " SUM(double_chance__first_half_home_draw), "
    query += " SUM(double_chance__first_half_home_away), "
    query += " SUM(double_chance__first_half_draw_away), "
    query += " SUM(oddeven_odd), "
    query += " SUM(oddeven_even), "
    query += " SUM(results_both_teams_score_home_yes), "
    query += " SUM(results_both_teams_score_draw_yes), "
    query += " SUM(results_both_teams_score_away_yes), "
    query += " SUM(results_both_teams_score_home_no), "
    query += " SUM(results_both_teams_score_draw_no), "
    query += " SUM(results_both_teams_score_away_no), "
    query += " SUM(result_total_goals_home_over_35), "
    query += " SUM(result_total_goals_draw_over_35), "
    query += " SUM(result_total_goals_away_over_35), "
    query += " SUM(result_total_goals_home_under_35), "
    query += " SUM(result_total_goals_draw_under_35), "
    query += " SUM(result_total_goals_away_under_35), "
    query += " SUM(result_total_goals_home_over_25), "
    query += " SUM(result_total_goals_draw_over_25), "
    query += " SUM(result_total_goals_away_over_25), "
    query += " SUM(result_total_goals_home_under_25), "
    query += " SUM(result_total_goals_draw_under_25), "
    query += " SUM(result_total_goals_away_under_25), "
    query += " SUM(goals_overunder__second_half_over_05), "
    query += " SUM(goals_overunder__second_half_under_05), "
    query += " SUM(goals_overunder__second_half_over_075), "
    query += " SUM(goals_overunder__second_half_under_075), "
    query += " SUM(goals_overunder__second_half_over_10), "
    query += " SUM(goals_overunder__second_half_under_10), "
    query += " SUM(goals_overunder__second_half_over_125), "
    query += " SUM(goals_overunder__second_half_under_125), "
    query += " SUM(goals_overunder__second_half_over_15), "
    query += " SUM(goals_overunder__second_half_under_15), "
    query += " SUM(goals_overunder__second_half_over_175), "
    query += " SUM(goals_overunder__second_half_under_175), "
    query += " SUM(goals_overunder__second_half_over_20), "
    query += " SUM(goals_overunder__second_half_under_20), "
    query += " SUM(goals_overunder__second_half_over_225), "
    query += " SUM(goals_overunder__second_half_under_225), "
    query += " SUM(goals_overunder__second_half_over_25), "
    query += " SUM(goals_overunder__second_half_under_25), "
    query += " SUM(goals_overunder__second_half_over_275), "
    query += " SUM(goals_overunder__second_half_under_275), "
    query += " SUM(goals_overunder__second_half_over_30), "
    query += " SUM(goals_overunder__second_half_under_30), "
    query += " SUM(goals_overunder__second_half_over_325), "
    query += " SUM(goals_overunder__second_half_under_325), "
    query += " SUM(goals_overunder__second_half_over_35), "
    query += " SUM(goals_overunder__second_half_under_35), "
    query += " SUM(goals_overunder__second_half_over_375), "
    query += " SUM(goals_overunder__second_half_under_375), "
    query += " SUM(clean_sheet__home_yes), "
    query += " SUM(clean_sheet__home_no), "
    query += " SUM(clean_sheet__away_yes), "
    query += " SUM(clean_sheet__away_no), "
    query += " SUM(win_both_halves_home), "
    query += " SUM(win_both_halves_away), "
    query += " SUM(both_teams_score__first_half_yes), "
    query += " SUM(both_teams_score__first_half_no), "
    query += " SUM(both_teams_to_score__second_half_yes), "
    query += " SUM(both_teams_to_score__second_half_no), "
    query += " SUM(win_to_nil_home), "
    query += " SUM(win_to_nil_away), "

    query += " SUM(exact_goals_number_0), "
    query += " SUM(exact_goals_number_1), "
    query += " SUM(exact_goals_number_2), "
    query += " SUM(exact_goals_number_3), "
    query += " SUM(exact_goals_number_4), "
    query += " SUM(exact_goals_number_5), "
    query += " SUM(exact_goals_number_6), "
    query += " SUM(exact_goals_number_more_7), "
    query += " SUM(to_win_either_half_home), "
    query += " SUM(to_win_either_half_away), "
    query += " SUM(home_team_exact_goals_number_0), "
    query += " SUM(home_team_exact_goals_number_1), "
    query += " SUM(home_team_exact_goals_number_2), "
    query += " SUM(home_team_exact_goals_number_more_3), "
    query += " SUM(away_team_exact_goals_number_0), "
    query += " SUM(away_team_exact_goals_number_1), "
    query += " SUM(away_team_exact_goals_number_2), "
    query += " SUM(away_team_exact_goals_number_more_3), "
    query += " SUM(second_half_exact_goals_number_0), "
    query += " SUM(second_half_exact_goals_number_1), "
    query += " SUM(second_half_exact_goals_number_2), "
    query += " SUM(second_half_exact_goals_number_3), "
    query += " SUM(second_half_exact_goals_number_4), "
    query += " SUM(second_half_exact_goals_number_more_5), "
    query += " SUM(exact_goals_number__first_half_0), "
    query += " SUM(exact_goals_number__first_half_1), "
    query += " SUM(exact_goals_number__first_half_2), "
    query += " SUM(exact_goals_number__first_half_3), "
    query += " SUM(exact_goals_number__first_half_4), "
    query += " SUM(exact_goals_number__first_half_more_5), "
    query += " SUM(to_score_in_both_halves_by_teams_home), "
    query += " SUM(to_score_in_both_halves_by_teams_away), "
    query += " SUM(total_goals_both_teams_to_score_over_yes_25), "
    query += " SUM(total_goals_both_teams_to_score_over_no_25), "
    query += " SUM(total_goals_both_teams_to_score_under_yes_25), "
    query += " SUM(total_goals_both_teams_to_score_under_no_25), "
    query += " SUM(halftime_result_both_teams_score_home_yes), "
    query += " SUM(halftime_result_both_teams_score_draw_yes), "
    query += " SUM(halftime_result_both_teams_score_away_yes), "
    query += " SUM(halftime_result_both_teams_score_home_no), "
    query += " SUM(halftime_result_both_teams_score_draw_no), "
    query += " SUM(halftime_result_both_teams_score_away_no), "
    query += " SUM(both_teams_to_score_1st_half__2nd_half_yes_yes), "
    query += " SUM(both_teams_to_score_1st_half__2nd_half_yes_no), "
    query += " SUM(both_teams_to_score_1st_half__2nd_half_no_yes), "
    query += " SUM(both_teams_to_score_1st_half__2nd_half_no_no), "
    query += " SUM(total_goals_under_2), "
    query += " SUM(total_goals_2_or_3), "
    query += " SUM(total_goals_over_3), "
    query += " AVG(match_winner_home), "
    query += " AVG(match_winner_draw), "
    query += " AVG(match_winner_away), "
    query += " AVG(homeaway_home), "
    query += " AVG(homeaway_away), "
    query += " AVG(second_half_winner_home), "
    query += " AVG(second_half_winner_draw), "
    query += " AVG(second_half_winner_away), "
    query += " AVG(asian_handicap_home_min_675), "
    query += " AVG(asian_handicap_away_min_675), "
    query += " AVG(asian_handicap_home_min_65), "
    query += " AVG(asian_handicap_away_min_65), "
    query += " AVG(asian_handicap_home_min_625), "
    query += " AVG(asian_handicap_away_min_625), "
    query += " AVG(asian_handicap_home_min_6), "
    query += " AVG(asian_handicap_away_min_6), "
    query += " AVG(asian_handicap_home_min_575), "
    query += " AVG(asian_handicap_away_min_575), "
    query += " AVG(asian_handicap_home_min_55), "
    query += " AVG(asian_handicap_away_min_55), "
    query += " AVG(asian_handicap_home_min_525), "
    query += " AVG(asian_handicap_away_min_525), "
    query += " AVG(asian_handicap_home_min_5), "
    query += " AVG(asian_handicap_away_min_5), "
    query += " AVG(asian_handicap_home_min_475), "
    query += " AVG(asian_handicap_away_min_475), "
    query += " AVG(asian_handicap_home_min_45), "
    query += " AVG(asian_handicap_away_min_45), "
    query += " AVG(asian_handicap_home_min_425), "
    query += " AVG(asian_handicap_away_min_425), "
    query += " AVG(asian_handicap_home_min_4), "
    query += " AVG(asian_handicap_away_min_4), "
    query += " AVG(asian_handicap_home_min_375), "
    query += " AVG(asian_handicap_away_min_375), "
    query += " AVG(asian_handicap_home_min_35), "
    query += " AVG(asian_handicap_away_min_35), "
    query += " AVG(asian_handicap_home_min_325), "
    query += " AVG(asian_handicap_away_min_325), "
    query += " AVG(asian_handicap_home_min_3), "
    query += " AVG(asian_handicap_away_min_3), "
    query += " AVG(asian_handicap_home_min_275), "
    query += " AVG(asian_handicap_away_min_275), "
    query += " AVG(asian_handicap_home_min_25), "
    query += " AVG(asian_handicap_away_min_25), "
    query += " AVG(asian_handicap_home_min_225), "
    query += " AVG(asian_handicap_away_min_225), "
    query += " AVG(asian_handicap_home_min_2), "
    query += " AVG(asian_handicap_away_min_2), "
    query += " AVG(asian_handicap_home_min_175), "
    query += " AVG(asian_handicap_away_min_175), "
    query += " AVG(asian_handicap_home_min_15), "
    query += " AVG(asian_handicap_away_min_15), "
    query += " AVG(asian_handicap_home_min_125), "
    query += " AVG(asian_handicap_away_min_125), "
    query += " AVG(asian_handicap_home_min_1), "
    query += " AVG(asian_handicap_away_min_1), "
    query += " AVG(asian_handicap_home_min_075), "
    query += " AVG(asian_handicap_away_min_075), "
    query += " AVG(asian_handicap_home_min_05), "
    query += " AVG(asian_handicap_away_min_05), "
    query += " AVG(asian_handicap_home_min_025), "
    query += " AVG(asian_handicap_away_min_025), "
    query += " AVG(asian_handicap_home_plus_0), "
    query += " AVG(asian_handicap_away_plus_0), "
    query += " AVG(asian_handicap_home_plus_025), "
    query += " AVG(asian_handicap_away_plus_025), "
    query += " AVG(asian_handicap_home_plus_05), "
    query += " AVG(asian_handicap_away_plus_05), "
    query += " AVG(asian_handicap_home_plus_075), "
    query += " AVG(asian_handicap_away_plus_075), "
    query += " AVG(asian_handicap_home_plus_1), "
    query += " AVG(asian_handicap_away_plus_1), "
    query += " AVG(asian_handicap_home_plus_125), "
    query += " AVG(asian_handicap_away_plus_125), "
    query += " AVG(asian_handicap_home_plus_15), "
    query += " AVG(asian_handicap_away_plus_15), "
    query += " AVG(asian_handicap_home_plus_175), "
    query += " AVG(asian_handicap_away_plus_175), "
    query += " AVG(asian_handicap_home_plus_2), "
    query += " AVG(asian_handicap_away_plus_2), "
    query += " AVG(asian_handicap_home_plus_225), "
    query += " AVG(asian_handicap_away_plus_225), "
    query += " AVG(asian_handicap_home_plus_25), "
    query += " AVG(asian_handicap_away_plus_25), "
    query += " AVG(asian_handicap_home_plus_275), "
    query += " AVG(asian_handicap_away_plus_275), "
    query += " AVG(asian_handicap_home_plus_3), "
    query += " AVG(asian_handicap_away_plus_3), "
    query += " AVG(asian_handicap_home_plus_325), "
    query += " AVG(asian_handicap_away_plus_325), "
    query += " AVG(asian_handicap_home_plus_35), "
    query += " AVG(asian_handicap_away_plus_35), "
    query += " AVG(asian_handicap_home_plus_375), "
    query += " AVG(asian_handicap_away_plus_375), "
    query += " AVG(asian_handicap_home_plus_4), "
    query += " AVG(asian_handicap_away_plus_4), "
    query += " AVG(asian_handicap_home_plus_425), "
    query += " AVG(asian_handicap_away_plus_425), "
    query += " AVG(asian_handicap_home_plus_45), "
    query += " AVG(asian_handicap_away_plus_45), "
    query += " AVG(asian_handicap_home_plus_475), "
    query += " AVG(asian_handicap_away_plus_475), "
    query += " AVG(asian_handicap_home_plus_5), "
    query += " AVG(asian_handicap_away_plus_5), "
    query += " AVG(asian_handicap_home_plus_525), "
    query += " AVG(asian_handicap_away_plus_525), "
    query += " AVG(asian_handicap_home_plus_55), "
    query += " AVG(asian_handicap_away_plus_55), "
    query += " AVG(asian_handicap_home_plus_575), "
    query += " AVG(asian_handicap_away_plus_575), "
    query += " AVG(asian_handicap_home_plus_6), "
    query += " AVG(asian_handicap_away_plus_6), "
    query += " AVG(asian_handicap_home_plus_625), "
    query += " AVG(asian_handicap_away_plus_625), "
    query += " AVG(asian_handicap_home_plus_65), "
    query += " AVG(asian_handicap_away_plus_65), "
    query += " AVG(asian_handicap_home_plus_675), "
    query += " AVG(asian_handicap_away_plus_675), "
    query += " AVG(goals_overunder_over_05), "
    query += " AVG(goals_overunder_under_05), "
    query += " AVG(goals_overunder_over_075), "
    query += " AVG(goals_overunder_under_075), "
    query += " AVG(goals_overunder_over_10), "

    query += " AVG(goals_overunder_under_10), "
    query += " AVG(goals_overunder_over_125), "
    query += " AVG(goals_overunder_under_125), "
    query += " AVG(goals_overunder_over_15), "
    query += " AVG(goals_overunder_under_15), "
    query += " AVG(goals_overunder_over_175), "
    query += " AVG(goals_overunder_under_175), "
    query += " AVG(goals_overunder_over_20), "
    query += " AVG(goals_overunder_under_20), "
    query += " AVG(goals_overunder_over_225), "
    query += " AVG(goals_overunder_under_225), "
    query += " AVG(goals_overunder_over_25), "
    query += " AVG(goals_overunder_under_25), "
    query += " AVG(goals_overunder_over_275), "
    query += " AVG(goals_overunder_under_275), "
    query += " AVG(goals_overunder_over_30), "
    query += " AVG(goals_overunder_under_30), "
    query += " AVG(goals_overunder_over_325), "
    query += " AVG(goals_overunder_under_325), "
    query += " AVG(goals_overunder_over_35), "
    query += " AVG(goals_overunder_under_35), "
    query += " AVG(goals_overunder_over_375), "
    query += " AVG(goals_overunder_under_375), "
    query += " AVG(goals_overunder_over_40), "
    query += " AVG(goals_overunder_under_40), "
    query += " AVG(goals_overunder_over_425), "
    query += " AVG(goals_overunder_under_425), "
    query += " AVG(goals_overunder_over_45), "
    query += " AVG(goals_overunder_under_45), "
    query += " AVG(goals_overunder_over_475), "
    query += " AVG(goals_overunder_under_475), "
    query += " AVG(goals_overunder_over_50), "
    query += " AVG(goals_overunder_under_50), "
    query += " AVG(goals_overunder_over_525), "
    query += " AVG(goals_overunder_under_525), "
    query += " AVG(goals_overunder_over_55), "
    query += " AVG(goals_overunder_under_55), "
    query += " AVG(goals_overunder_over_575), "
    query += " AVG(goals_overunder_under_575), "
    query += " AVG(goals_overunder_over_60), "
    query += " AVG(goals_overunder_under_60), "
    query += " AVG(goals_overunder_over_625), "
    query += " AVG(goals_overunder_under_625), "
    query += " AVG(goals_overunder_over_65), "
    query += " AVG(goals_overunder_under_65), "
    query += " AVG(goals_overunder_over_675), "
    query += " AVG(goals_overunder_under_675), "
    query += " AVG(goals_overunder_over_70), "
    query += " AVG(goals_overunder_under_70), "
    query += " AVG(goals_overunder_over_75), "
    query += " AVG(goals_overunder_under_75), "
    query += " AVG(goals_overunder_over_85), "
    query += " AVG(goals_overunder_under_85), "
    query += " AVG(goals_overunder_over_95), "
    query += " AVG(goals_overunder_under_95), "
    query += " AVG(goals_overunder_first_half_over_05), "
    query += " AVG(goals_overunder_first_half_under_05), "
    query += " AVG(goals_overunder_first_half_over_075), "
    query += " AVG(goals_overunder_first_half_under_075), "
    query += " AVG(goals_overunder_first_half_over_10), "
    query += " AVG(goals_overunder_first_half_under_10), "
    query += " AVG(goals_overunder_first_half_over_125), "
    query += " AVG(goals_overunder_first_half_under_125), "
    query += " AVG(goals_overunder_first_half_over_15), "
    query += " AVG(goals_overunder_first_half_under_15), "
    query += " AVG(goals_overunder_first_half_over_175), "
    query += " AVG(goals_overunder_first_half_under_175), "
    query += " AVG(goals_overunder_first_half_over_20), "
    query += " AVG(goals_overunder_first_half_under_20), "
    query += " AVG(goals_overunder_first_half_over_225), "
    query += " AVG(goals_overunder_first_half_under_225), "
    query += " AVG(goals_overunder_first_half_over_25), "
    query += " AVG(goals_overunder_first_half_under_25), "
    query += " AVG(goals_overunder_first_half_over_275), "
    query += " AVG(goals_overunder_first_half_under_275), "
    query += " AVG(goals_overunder_first_half_over_30), "
    query += " AVG(goals_overunder_first_half_under_30), "
    query += " AVG(goals_overunder_first_half_over_325), "
    query += " AVG(goals_overunder_first_half_under_325), "
    query += " AVG(goals_overunder_first_half_over_35), "
    query += " AVG(goals_overunder_first_half_under_35), "
    query += " AVG(goals_overunder_first_half_over_375), "
    query += " AVG(goals_overunder_first_half_under_375), "
    query += " AVG(htft_double_home_home), "
    query += " AVG(htft_double_home_draw), "
    query += " AVG(htft_double_home_away), "
    query += " AVG(htft_double_draw_home), "
    query += " AVG(htft_double_draw_draw), "
    query += " AVG(htft_double_draw_away), "
    query += " AVG(htft_double_away_home), "
    query += " AVG(htft_double_away_draw), "
    query += " AVG(htft_double_away_away), "
    query += " AVG(both_teams_score_yes), "
    query += " AVG(both_teams_score_no), "
    query += " AVG(highest_scoring_half_first), "
    query += " AVG(highest_scoring_half_draw), "
    query += " AVG(highest_scoring_half_second), "
    query += " AVG(double_chance_home_draw), "
    query += " AVG(double_chance_home_away), "
    query += " AVG(double_chance_draw_away), "
    query += " AVG(first_half_winner_home), "
    query += " AVG(first_half_winner_draw), "
    query += " AVG(first_half_winner_away), "
    query += " AVG(total_home_over_15), "
    query += " AVG(total_home_under_15), "
    query += " AVG(total_home_over_25), "
    query += " AVG(total_home_under_25), "
    query += " AVG(total_home_over_35), "
    query += " AVG(total_home_under_35), "
    query += " AVG(total_home_over_45), "
    query += " AVG(total_home_under_45), "
    query += " AVG(total_home_over_55), "
    query += " AVG(total_home_under_55), "
    query += " AVG(total_home_over_65), "
    query += " AVG(total_home_under_65), "
    query += " AVG(total_away_over_15), "
    query += " AVG(total_away_under_15), "
    query += " AVG(total_away_over_25), "
    query += " AVG(total_away_under_25), "
    query += " AVG(total_away_over_35), "
    query += " AVG(total_away_under_35), "
    query += " AVG(total_away_over_45), "
    query += " AVG(total_away_under_45), "
    query += " AVG(total_away_over_55), "
    query += " AVG(total_away_under_55), "
    query += " AVG(total_away_over_65), "
    query += " AVG(total_away_under_65), "
    query += " AVG(asian_handicap_first_half_home_min_175), "
    query += " AVG(asian_handicap_first_half_away_min_175), "
    query += " AVG(asian_handicap_first_half_home_min_15), "
    query += " AVG(asian_handicap_first_half_away_min_15), "
    query += " AVG(asian_handicap_first_half_home_min_125), "
    query += " AVG(asian_handicap_first_half_away_min_125), "
    query += " AVG(asian_handicap_first_half_home_min_1), "
    query += " AVG(asian_handicap_first_half_away_min_1), "
    query += " AVG(asian_handicap_first_half_home_min_075), "
    query += " AVG(asian_handicap_first_half_away_min_075), "
    query += " AVG(asian_handicap_first_half_home_min_05), "
    query += " AVG(asian_handicap_first_half_away_min_05), "
    query += " AVG(asian_handicap_first_half_home_min_025), "
    query += " AVG(asian_handicap_first_half_away_min_025), "
    query += " AVG(asian_handicap_first_half_home_plus_0), "
    query += " AVG(asian_handicap_first_half_away_plus_0), "
    query += " AVG(asian_handicap_first_half_home_plus_025), "
    query += " AVG(asian_handicap_first_half_away_plus_025), "
    query += " AVG(asian_handicap_first_half_home_plus_05), "
    query += " AVG(asian_handicap_first_half_away_plus_05), "
    query += " AVG(asian_handicap_first_half_home_plus_075), "
    query += " AVG(asian_handicap_first_half_away_plus_075), "
    query += " AVG(asian_handicap_first_half_home_plus_1), "
    query += " AVG(asian_handicap_first_half_away_plus_1), "
    query += " AVG(asian_handicap_first_half_home_plus_125), "
    query += " AVG(asian_handicap_first_half_away_plus_125), "
    query += " AVG(asian_handicap_first_half_home_plus_15), "
    query += " AVG(asian_handicap_first_half_away_plus_15), "
    query += " AVG(asian_handicap_first_half_home_plus_175), "
    query += " AVG(asian_handicap_first_half_away_plus_175), "
    query += " AVG(double_chance__first_half_home_draw), "
    query += " AVG(double_chance__first_half_home_away), "
    query += " AVG(double_chance__first_half_draw_away), "
    query += " AVG(oddeven_odd), "
    query += " AVG(oddeven_even), "
    query += " AVG(results_both_teams_score_home_yes), "
    query += " AVG(results_both_teams_score_draw_yes), "
    query += " AVG(results_both_teams_score_away_yes), "
    query += " AVG(results_both_teams_score_home_no), "
    query += " AVG(results_both_teams_score_draw_no), "
    query += " AVG(results_both_teams_score_away_no), "
    query += " AVG(result_total_goals_home_over_35), "
    query += " AVG(result_total_goals_draw_over_35), "
    query += " AVG(result_total_goals_away_over_35), "
    query += " AVG(result_total_goals_home_under_35), "

    query += " AVG(result_total_goals_draw_under_35), "
    query += " AVG(result_total_goals_away_under_35), "
    query += " AVG(result_total_goals_home_over_25), "
    query += " AVG(result_total_goals_draw_over_25), "
    query += " AVG(result_total_goals_away_over_25), "
    query += " AVG(result_total_goals_home_under_25), "
    query += " AVG(result_total_goals_draw_under_25), "
    query += " AVG(result_total_goals_away_under_25), "
    query += " AVG(goals_overunder__second_half_over_05), "
    query += " AVG(goals_overunder__second_half_under_05), "
    query += " AVG(goals_overunder__second_half_over_075), "
    query += " AVG(goals_overunder__second_half_under_075), "
    query += " AVG(goals_overunder__second_half_over_10), "
    query += " AVG(goals_overunder__second_half_under_10), "
    query += " AVG(goals_overunder__second_half_over_125), "
    query += " AVG(goals_overunder__second_half_under_125), "
    query += " AVG(goals_overunder__second_half_over_15), "
    query += " AVG(goals_overunder__second_half_under_15), "
    query += " AVG(goals_overunder__second_half_over_175), "
    query += " AVG(goals_overunder__second_half_under_175), "
    query += " AVG(goals_overunder__second_half_over_20), "
    query += " AVG(goals_overunder__second_half_under_20), "
    query += " AVG(goals_overunder__second_half_over_225), "
    query += " AVG(goals_overunder__second_half_under_225), "
    query += " AVG(goals_overunder__second_half_over_25), "
    query += " AVG(goals_overunder__second_half_under_25), "
    query += " AVG(goals_overunder__second_half_over_275), "
    query += " AVG(goals_overunder__second_half_under_275), "
    query += " AVG(goals_overunder__second_half_over_30), "
    query += " AVG(goals_overunder__second_half_under_30), "
    query += " AVG(goals_overunder__second_half_over_325), "
    query += " AVG(goals_overunder__second_half_under_325), "
    query += " AVG(goals_overunder__second_half_over_35), "
    query += " AVG(goals_overunder__second_half_under_35), "
    query += " AVG(goals_overunder__second_half_over_375), "
    query += " AVG(goals_overunder__second_half_under_375), "
    query += " AVG(clean_sheet__home_yes), "
    query += " AVG(clean_sheet__home_no), "
    query += " AVG(clean_sheet__away_yes), "
    query += " AVG(clean_sheet__away_no), "
    query += " AVG(win_both_halves_home), "
    query += " AVG(win_both_halves_away), "
    query += " AVG(both_teams_score__first_half_yes), "
    query += " AVG(both_teams_score__first_half_no), "
    query += " AVG(both_teams_to_score__second_half_yes), "
    query += " AVG(both_teams_to_score__second_half_no), "
    query += " AVG(win_to_nil_home), "
    query += " AVG(win_to_nil_away), "
    query += " AVG(exact_goals_number_0), "
    query += " AVG(exact_goals_number_1), "
    query += " AVG(exact_goals_number_2), "
    query += " AVG(exact_goals_number_3), "
    query += " AVG(exact_goals_number_4), "
    query += " AVG(exact_goals_number_5), "
    query += " AVG(exact_goals_number_6), "
    query += " AVG(exact_goals_number_more_7), "
    query += " AVG(to_win_either_half_home), "
    query += " AVG(to_win_either_half_away), "
    query += " AVG(home_team_exact_goals_number_0), "
    query += " AVG(home_team_exact_goals_number_1), "
    query += " AVG(home_team_exact_goals_number_2), "
    query += " AVG(home_team_exact_goals_number_more_3), "
    query += " AVG(away_team_exact_goals_number_0), "
    query += " AVG(away_team_exact_goals_number_1), "
    query += " AVG(away_team_exact_goals_number_2), "
    query += " AVG(away_team_exact_goals_number_more_3), "
    query += " AVG(second_half_exact_goals_number_0), "
    query += " AVG(second_half_exact_goals_number_1), "
    query += " AVG(second_half_exact_goals_number_2), "
    query += " AVG(second_half_exact_goals_number_3), "
    query += " AVG(second_half_exact_goals_number_4), "
    query += " AVG(second_half_exact_goals_number_more_5), "
    query += " AVG(exact_goals_number__first_half_0), "
    query += " AVG(exact_goals_number__first_half_1), "
    query += " AVG(exact_goals_number__first_half_2), "
    query += " AVG(exact_goals_number__first_half_3), "
    query += " AVG(exact_goals_number__first_half_4), "
    query += " AVG(exact_goals_number__first_half_more_5), "
    query += " AVG(to_score_in_both_halves_by_teams_home), "
    query += " AVG(to_score_in_both_halves_by_teams_away), "
    query += " AVG(total_goals_both_teams_to_score_over_yes_25), "
    query += " AVG(total_goals_both_teams_to_score_over_no_25), "
    query += " AVG(total_goals_both_teams_to_score_under_yes_25), "
    query += " AVG(total_goals_both_teams_to_score_under_no_25), "
    query += " AVG(halftime_result_both_teams_score_home_yes), "
    query += " AVG(halftime_result_both_teams_score_draw_yes), "
    query += " AVG(halftime_result_both_teams_score_away_yes), "
    query += " AVG(halftime_result_both_teams_score_home_no), "
    query += " AVG(halftime_result_both_teams_score_draw_no), "
    query += " AVG(halftime_result_both_teams_score_away_no), "
    query += " AVG(both_teams_to_score_1st_half__2nd_half_yes_yes), "
    query += " AVG(both_teams_to_score_1st_half__2nd_half_yes_no), "
    query += " AVG(both_teams_to_score_1st_half__2nd_half_no_yes), "
    query += " AVG(both_teams_to_score_1st_half__2nd_half_no_no), "
    query += " AVG(total_goals_under_2), "
    query += " AVG(total_goals_2_or_3), "
    query += " AVG(total_goals_over_3) "
 
    query += " FROM `football_statistics` "     
    query += " where fixtureapi_id in ( " + str(PRE_result) + " ) "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    # space += "__"
    # ----------------------------------------------------------
    total_rows = len(result)    
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    # ---------------------------------------------------------- 
    for x in result:   
        # ------------------------------------------------------
        counter_col = 0
        SUM_match_winner_home = x[counter_col] 

        counter_col += 1
        SUM_match_winner_draw = x[counter_col] 

        counter_col += 1
        SUM_match_winner_away = x[counter_col] 

        counter_col += 1
        SUM_homeaway_home = x[counter_col] 

        counter_col += 1
        SUM_homeaway_away = x[counter_col] 

        counter_col += 1
        SUM_second_half_winner_home = x[counter_col] 

        counter_col += 1
        SUM_second_half_winner_draw = x[counter_col] 

        counter_col += 1
        SUM_second_half_winner_away = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_675 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_675 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_65 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_65 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_625 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_625 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_6 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_6 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_575 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_575 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_55 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_55 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_525 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_525 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_5 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_5 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_475 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_475 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_45 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_45 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_425 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_425 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_4 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_4 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_375 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_375 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_35 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_35 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_325 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_325 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_3 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_3 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_275 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_275 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_25 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_25 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_225 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_225 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_2 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_2 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_min_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_min_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_0 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_0 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_2 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_2 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_225 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_225 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_25 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_25 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_275 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_275 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_3 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_3 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_325 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_325 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_35 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_35 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_375 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_375 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_4 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_4 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_425 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_425 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_45 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_45 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_475 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_475 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_5 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_5 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_525 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_525 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_55 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_55 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_575 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_575 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_6 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_6 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_625 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_625 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_65 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_65 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_home_plus_675 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_away_plus_675 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_075 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_075 = x[counter_col] 

        counter_col += 1

        SUM_goals_overunder_over_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_375 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_375 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_40 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_40 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_425 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_425 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_45 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_45 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_475 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_475 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_50 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_50 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_525 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_525 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_55 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_55 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_575 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_575 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_60 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_60 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_625 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_625 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_65 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_65 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_675 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_675 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_70 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_70 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_75 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_75 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_85 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_85 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_over_95 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_under_95 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_075 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_075 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_over_375 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder_first_half_under_375 = x[counter_col] 

        counter_col += 1
        SUM_htft_double_home_home = x[counter_col] 

        counter_col += 1
        SUM_htft_double_home_draw = x[counter_col] 

        counter_col += 1
        SUM_htft_double_home_away = x[counter_col] 

        counter_col += 1
        SUM_htft_double_draw_home = x[counter_col] 

        counter_col += 1
        SUM_htft_double_draw_draw = x[counter_col] 

        counter_col += 1
        SUM_htft_double_draw_away = x[counter_col] 

        counter_col += 1
        SUM_htft_double_away_home = x[counter_col] 

        counter_col += 1
        SUM_htft_double_away_draw = x[counter_col] 

        counter_col += 1
        SUM_htft_double_away_away = x[counter_col] 

        counter_col += 1
        SUM_both_teams_score_yes = x[counter_col] 

        counter_col += 1
        SUM_both_teams_score_no = x[counter_col] 

        counter_col += 1
        SUM_highest_scoring_half_first = x[counter_col] 

        counter_col += 1
        SUM_highest_scoring_half_draw = x[counter_col] 

        counter_col += 1
        SUM_highest_scoring_half_second = x[counter_col] 

        counter_col += 1
        SUM_double_chance_home_draw = x[counter_col] 

        counter_col += 1
        SUM_double_chance_home_away = x[counter_col] 

        counter_col += 1
        SUM_double_chance_draw_away = x[counter_col] 

        counter_col += 1
        SUM_first_half_winner_home = x[counter_col] 

        counter_col += 1
        SUM_first_half_winner_draw = x[counter_col] 

        counter_col += 1
        SUM_first_half_winner_away = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_15 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_15 = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_25 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_25 = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_35 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_35 = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_45 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_45 = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_55 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_55 = x[counter_col] 

        counter_col += 1
        SUM_total_home_over_65 = x[counter_col] 

        counter_col += 1
        SUM_total_home_under_65 = x[counter_col] 

        counter_col += 1
        SUM_total_away_over_15 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_15 = x[counter_col] 

        counter_col += 1
        SUM_total_away_over_25 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_25 = x[counter_col] 

        counter_col += 1
        SUM_total_away_over_35 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_35 = x[counter_col] 

        counter_col += 1
        SUM_total_away_over_45 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_45 = x[counter_col] 


        counter_col += 1
        SUM_total_away_over_55 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_55 = x[counter_col] 

        counter_col += 1
        SUM_total_away_over_65 = x[counter_col] 

        counter_col += 1
        SUM_total_away_under_65 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_min_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_min_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_0 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_0 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_025 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_05 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_075 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_1 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_125 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_15 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_home_plus_175 = x[counter_col] 

        counter_col += 1
        SUM_asian_handicap_first_half_away_plus_175 = x[counter_col] 

        counter_col += 1
        SUM_double_chance__first_half_home_draw = x[counter_col] 

        counter_col += 1
        SUM_double_chance__first_half_home_away = x[counter_col] 

        counter_col += 1
        SUM_double_chance__first_half_draw_away = x[counter_col] 

        counter_col += 1
        SUM_oddeven_odd = x[counter_col] 

        counter_col += 1
        SUM_oddeven_even = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_home_yes = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_draw_yes = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_away_yes = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_home_no = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_draw_no = x[counter_col] 

        counter_col += 1
        SUM_results_both_teams_score_away_no = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_home_over_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_draw_over_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_away_over_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_home_under_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_draw_under_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_away_under_35 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_home_over_25 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_draw_over_25 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_away_over_25 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_home_under_25 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_draw_under_25 = x[counter_col] 

        counter_col += 1
        SUM_result_total_goals_away_under_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_05 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_075 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_075 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_10 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_125 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_15 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_175 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_20 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_225 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_25 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_275 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_30 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_325 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_35 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_over_375 = x[counter_col] 

        counter_col += 1
        SUM_goals_overunder__second_half_under_375 = x[counter_col] 

        counter_col += 1
        SUM_clean_sheet__home_yes = x[counter_col] 

        counter_col += 1
        SUM_clean_sheet__home_no = x[counter_col] 

        counter_col += 1
        SUM_clean_sheet__away_yes = x[counter_col] 

        counter_col += 1
        SUM_clean_sheet__away_no = x[counter_col] 

        counter_col += 1
        SUM_win_both_halves_home = x[counter_col] 

        counter_col += 1
        SUM_win_both_halves_away = x[counter_col] 

        counter_col += 1
        SUM_both_teams_score__first_half_yes = x[counter_col] 

        counter_col += 1
        SUM_both_teams_score__first_half_no = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score__second_half_yes = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score__second_half_no = x[counter_col] 

        counter_col += 1
        SUM_win_to_nil_home = x[counter_col] 

        counter_col += 1
        SUM_win_to_nil_away = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_0 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_1 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_2 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_3 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_4 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_5 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_6 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number_more_7 = x[counter_col] 

        counter_col += 1
        SUM_to_win_either_half_home = x[counter_col] 

        counter_col += 1
        SUM_to_win_either_half_away = x[counter_col] 

        counter_col += 1
        SUM_home_team_exact_goals_number_0 = x[counter_col] 

        counter_col += 1
        SUM_home_team_exact_goals_number_1 = x[counter_col] 

        counter_col += 1
        SUM_home_team_exact_goals_number_2 = x[counter_col] 

        counter_col += 1
        SUM_home_team_exact_goals_number_more_3 = x[counter_col] 

        counter_col += 1
        SUM_away_team_exact_goals_number_0 = x[counter_col] 

        counter_col += 1

        SUM_away_team_exact_goals_number_1 = x[counter_col] 

        counter_col += 1
        SUM_away_team_exact_goals_number_2 = x[counter_col] 

        counter_col += 1
        SUM_away_team_exact_goals_number_more_3 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_0 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_1 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_2 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_3 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_4 = x[counter_col] 

        counter_col += 1
        SUM_second_half_exact_goals_number_more_5 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_0 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_1 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_2 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_3 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_4 = x[counter_col] 

        counter_col += 1
        SUM_exact_goals_number__first_half_more_5 = x[counter_col] 

        counter_col += 1
        SUM_to_score_in_both_halves_by_teams_home = x[counter_col] 

        counter_col += 1
        SUM_to_score_in_both_halves_by_teams_away = x[counter_col] 

        counter_col += 1
        SUM_total_goals_both_teams_to_score_over_yes_25 = x[counter_col] 

        counter_col += 1
        SUM_total_goals_both_teams_to_score_over_no_25 = x[counter_col] 

        counter_col += 1
        SUM_total_goals_both_teams_to_score_under_yes_25 = x[counter_col] 

        counter_col += 1
        SUM_total_goals_both_teams_to_score_under_no_25 = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_home_yes = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_draw_yes = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_away_yes = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_home_no = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_draw_no = x[counter_col] 

        counter_col += 1
        SUM_halftime_result_both_teams_score_away_no = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score_1st_half__2nd_half_yes_yes = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score_1st_half__2nd_half_yes_no = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score_1st_half__2nd_half_no_yes = x[counter_col] 

        counter_col += 1
        SUM_both_teams_to_score_1st_half__2nd_half_no_no = x[counter_col] 

        counter_col += 1
        SUM_total_goals_under_2 = x[counter_col] 

        counter_col += 1
        SUM_total_goals_2_or_3 = x[counter_col] 

        counter_col += 1
        SUM_total_goals_over_3 = x[counter_col] 

        counter_col += 1
        AVG_match_winner_home = x[counter_col]

        counter_col += 1
        AVG_match_winner_draw = x[counter_col]

        counter_col += 1
        AVG_match_winner_away = x[counter_col]

        counter_col += 1
        AVG_homeaway_home = x[counter_col]

        counter_col += 1
        AVG_homeaway_away = x[counter_col]

        counter_col += 1
        AVG_second_half_winner_home = x[counter_col]

        counter_col += 1
        AVG_second_half_winner_draw = x[counter_col]

        counter_col += 1
        AVG_second_half_winner_away = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_675 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_675 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_65 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_65 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_625 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_625 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_6 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_6 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_575 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_575 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_55 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_55 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_525 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_525 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_5 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_5 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_475 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_475 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_45 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_45 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_425 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_425 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_4 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_4 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_375 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_375 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_35 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_35 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_325 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_325 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_3 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_3 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_275 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_275 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_25 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_25 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_225 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_225 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_2 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_2 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_min_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_min_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_0 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_0 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_2 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_2 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_225 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_225 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_25 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_25 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_275 = x[counter_col]

        counter_col += 1

        AVG_asian_handicap_away_plus_275 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_3 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_3 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_325 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_325 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_35 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_35 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_375 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_375 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_4 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_4 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_425 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_425 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_45 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_45 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_475 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_475 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_5 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_5 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_525 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_525 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_55 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_55 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_575 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_575 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_6 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_6 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_625 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_625 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_65 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_65 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_home_plus_675 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_away_plus_675 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_30 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_30 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_375 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_375 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_40 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_40 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_425 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_425 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_45 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_45 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_475 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_475 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_50 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_50 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_525 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_525 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_55 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_55 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_575 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_575 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_60 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_60 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_625 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_625 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_65 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_65 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_675 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_675 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_70 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_70 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_75 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_75 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_85 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_85 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_over_95 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_under_95 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_30 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_30 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_over_375 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder_first_half_under_375 = x[counter_col]

        counter_col += 1
        AVG_htft_double_home_home = x[counter_col]


        counter_col += 1
        AVG_htft_double_home_draw = x[counter_col]

        counter_col += 1
        AVG_htft_double_home_away = x[counter_col]

        counter_col += 1
        AVG_htft_double_draw_home = x[counter_col]

        counter_col += 1
        AVG_htft_double_draw_draw = x[counter_col]

        counter_col += 1
        AVG_htft_double_draw_away = x[counter_col]

        counter_col += 1
        AVG_htft_double_away_home = x[counter_col]

        counter_col += 1
        AVG_htft_double_away_draw = x[counter_col]

        counter_col += 1
        AVG_htft_double_away_away = x[counter_col]

        counter_col += 1
        AVG_both_teams_score_yes = x[counter_col]

        counter_col += 1
        AVG_both_teams_score_no = x[counter_col]

        counter_col += 1
        AVG_highest_scoring_half_first = x[counter_col]

        counter_col += 1
        AVG_highest_scoring_half_draw = x[counter_col]

        counter_col += 1
        AVG_highest_scoring_half_second = x[counter_col]

        counter_col += 1
        AVG_double_chance_home_draw = x[counter_col]

        counter_col += 1
        AVG_double_chance_home_away = x[counter_col]

        counter_col += 1
        AVG_double_chance_draw_away = x[counter_col]

        counter_col += 1
        AVG_first_half_winner_home = x[counter_col]

        counter_col += 1
        AVG_first_half_winner_draw = x[counter_col]

        counter_col += 1
        AVG_first_half_winner_away = x[counter_col]

        counter_col += 1
        AVG_total_home_over_15 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_15 = x[counter_col]

        counter_col += 1
        AVG_total_home_over_25 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_25 = x[counter_col]

        counter_col += 1
        AVG_total_home_over_35 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_35 = x[counter_col]

        counter_col += 1
        AVG_total_home_over_45 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_45 = x[counter_col]

        counter_col += 1
        AVG_total_home_over_55 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_55 = x[counter_col]

        counter_col += 1
        AVG_total_home_over_65 = x[counter_col]

        counter_col += 1
        AVG_total_home_under_65 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_15 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_15 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_25 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_25 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_35 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_35 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_45 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_45 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_55 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_55 = x[counter_col]

        counter_col += 1
        AVG_total_away_over_65 = x[counter_col]

        counter_col += 1
        AVG_total_away_under_65 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_min_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_min_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_0 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_0 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_025 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_05 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_075 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_1 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_125 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_15 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_home_plus_175 = x[counter_col]

        counter_col += 1
        AVG_asian_handicap_first_half_away_plus_175 = x[counter_col]

        counter_col += 1
        AVG_double_chance__first_half_home_draw = x[counter_col]

        counter_col += 1
        AVG_double_chance__first_half_home_away = x[counter_col]

        counter_col += 1
        AVG_double_chance__first_half_draw_away = x[counter_col]

        counter_col += 1
        AVG_oddeven_odd = x[counter_col]

        counter_col += 1
        AVG_oddeven_even = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_home_yes = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_draw_yes = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_away_yes = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_home_no = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_draw_no = x[counter_col]

        counter_col += 1
        AVG_results_both_teams_score_away_no = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_home_over_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_draw_over_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_away_over_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_home_under_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_draw_under_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_away_under_35 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_home_over_25 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_draw_over_25 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_away_over_25 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_home_under_25 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_draw_under_25 = x[counter_col]

        counter_col += 1
        AVG_result_total_goals_away_under_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_05 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_075 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_10 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_125 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_15 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_175 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_20 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_225 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_25 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_275 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_30 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_30 = x[counter_col]


        counter_col += 1
        AVG_goals_overunder__second_half_over_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_325 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_35 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_over_375 = x[counter_col]

        counter_col += 1
        AVG_goals_overunder__second_half_under_375 = x[counter_col]

        counter_col += 1
        AVG_clean_sheet__home_yes = x[counter_col]

        counter_col += 1
        AVG_clean_sheet__home_no = x[counter_col]

        counter_col += 1
        AVG_clean_sheet__away_yes = x[counter_col]

        counter_col += 1
        AVG_clean_sheet__away_no = x[counter_col]

        counter_col += 1
        AVG_win_both_halves_home = x[counter_col]

        counter_col += 1
        AVG_win_both_halves_away = x[counter_col]

        counter_col += 1
        AVG_both_teams_score__first_half_yes = x[counter_col]

        counter_col += 1
        AVG_both_teams_score__first_half_no = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score__second_half_yes = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score__second_half_no = x[counter_col]

        counter_col += 1
        AVG_win_to_nil_home = x[counter_col]

        counter_col += 1
        AVG_win_to_nil_away = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_0 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_1 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_2 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_3 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_4 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_5 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_6 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number_more_7 = x[counter_col]

        counter_col += 1
        AVG_to_win_either_half_home = x[counter_col]

        counter_col += 1
        AVG_to_win_either_half_away = x[counter_col]

        counter_col += 1
        AVG_home_team_exact_goals_number_0 = x[counter_col]

        counter_col += 1
        AVG_home_team_exact_goals_number_1 = x[counter_col]

        counter_col += 1
        AVG_home_team_exact_goals_number_2 = x[counter_col]

        counter_col += 1
        AVG_home_team_exact_goals_number_more_3 = x[counter_col]

        counter_col += 1
        AVG_away_team_exact_goals_number_0 = x[counter_col]

        counter_col += 1
        AVG_away_team_exact_goals_number_1 = x[counter_col]

        counter_col += 1
        AVG_away_team_exact_goals_number_2 = x[counter_col]

        counter_col += 1
        AVG_away_team_exact_goals_number_more_3 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_0 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_1 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_2 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_3 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_4 = x[counter_col]

        counter_col += 1
        AVG_second_half_exact_goals_number_more_5 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_0 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_1 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_2 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_3 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_4 = x[counter_col]

        counter_col += 1
        AVG_exact_goals_number__first_half_more_5 = x[counter_col]

        counter_col += 1
        AVG_to_score_in_both_halves_by_teams_home = x[counter_col]

        counter_col += 1
        AVG_to_score_in_both_halves_by_teams_away = x[counter_col]

        counter_col += 1
        AVG_total_goals_both_teams_to_score_over_yes_25 = x[counter_col]

        counter_col += 1
        AVG_total_goals_both_teams_to_score_over_no_25 = x[counter_col]

        counter_col += 1
        AVG_total_goals_both_teams_to_score_under_yes_25 = x[counter_col]

        counter_col += 1
        AVG_total_goals_both_teams_to_score_under_no_25 = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_home_yes = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_draw_yes = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_away_yes = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_home_no = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_draw_no = x[counter_col]

        counter_col += 1
        AVG_halftime_result_both_teams_score_away_no = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score_1st_half__2nd_half_yes_yes = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score_1st_half__2nd_half_yes_no = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score_1st_half__2nd_half_no_yes = x[counter_col]

        counter_col += 1
        AVG_both_teams_to_score_1st_half__2nd_half_no_no = x[counter_col]

        counter_col += 1
        AVG_total_goals_under_2 = x[counter_col]

        counter_col += 1
        AVG_total_goals_2_or_3 = x[counter_col]

        counter_col += 1
        AVG_total_goals_over_3 = x[counter_col]
        # ------------------------------------------------------
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    query_update = " UPDATE `"+total_TABLE+"` SET "   
    query_update += " `match_winner_home_data` = " + str(SUM_match_winner_home) + ", "
    query_update += " `match_winner_draw_data` = " + str(SUM_match_winner_draw) + ", "
    query_update += " `match_winner_away_data` = " + str(SUM_match_winner_away) + ", "
    query_update += " `homeaway_home_data` = " + str(SUM_homeaway_home) + ", "
    query_update += " `homeaway_away_data` = " + str(SUM_homeaway_away) + ", "
    query_update += " `second_half_winner_home_data` = " + str(SUM_second_half_winner_home) + ", "
    query_update += " `second_half_winner_draw_data` = " + str(SUM_second_half_winner_draw) + ", "
    query_update += " `second_half_winner_away_data` = " + str(SUM_second_half_winner_away) + ", "
    # query_update += " `asian_handicap_home_min_675_data` = " + str(SUM_asian_handicap_home_min_675) + ", "
    # query_update += " `asian_handicap_away_min_675_data` = " + str(SUM_asian_handicap_away_min_675) + ", "
    query_update += " `asian_handicap_home_min_65_data` = " + str(SUM_asian_handicap_home_min_65) + ", "
    query_update += " `asian_handicap_away_min_65_data` = " + str(SUM_asian_handicap_away_min_65) + ", "
    # query_update += " `asian_handicap_home_min_625_data` = " + str(SUM_asian_handicap_home_min_625) + ", "
    # query_update += " `asian_handicap_away_min_625_data` = " + str(SUM_asian_handicap_away_min_625) + ", "
    query_update += " `asian_handicap_home_min_6_data` = " + str(SUM_asian_handicap_home_min_6) + ", "
    query_update += " `asian_handicap_away_min_6_data` = " + str(SUM_asian_handicap_away_min_6) + ", "
    # query_update += " `asian_handicap_home_min_575_data` = " + str(SUM_asian_handicap_home_min_575) + ", "
    # query_update += " `asian_handicap_away_min_575_data` = " + str(SUM_asian_handicap_away_min_575) + ", "
    query_update += " `asian_handicap_home_min_55_data` = " + str(SUM_asian_handicap_home_min_55) + ", "
    query_update += " `asian_handicap_away_min_55_data` = " + str(SUM_asian_handicap_away_min_55) + ", "
    # query_update += " `asian_handicap_home_min_525_data` = " + str(SUM_asian_handicap_home_min_525) + ", "
    # query_update += " `asian_handicap_away_min_525_data` = " + str(SUM_asian_handicap_away_min_525) + ", "
    query_update += " `asian_handicap_home_min_5_data` = " + str(SUM_asian_handicap_home_min_5) + ", "
    query_update += " `asian_handicap_away_min_5_data` = " + str(SUM_asian_handicap_away_min_5) + ", "
    # query_update += " `asian_handicap_home_min_475_data` = " + str(SUM_asian_handicap_home_min_475) + ", "
    # query_update += " `asian_handicap_away_min_475_data` = " + str(SUM_asian_handicap_away_min_475) + ", "
    query_update += " `asian_handicap_home_min_45_data` = " + str(SUM_asian_handicap_home_min_45) + ", "
    query_update += " `asian_handicap_away_min_45_data` = " + str(SUM_asian_handicap_away_min_45) + ", "
    # query_update += " `asian_handicap_home_min_425_data` = " + str(SUM_asian_handicap_home_min_425) + ", "
    # query_update += " `asian_handicap_away_min_425_data` = " + str(SUM_asian_handicap_away_min_425) + ", "
    query_update += " `asian_handicap_home_min_4_data` = " + str(SUM_asian_handicap_home_min_4) + ", "
    query_update += " `asian_handicap_away_min_4_data` = " + str(SUM_asian_handicap_away_min_4) + ", "
    # query_update += " `asian_handicap_home_min_375_data` = " + str(SUM_asian_handicap_home_min_375) + ", "
    # query_update += " `asian_handicap_away_min_375_data` = " + str(SUM_asian_handicap_away_min_375) + ", "
    query_update += " `asian_handicap_home_min_35_data` = " + str(SUM_asian_handicap_home_min_35) + ", "
    query_update += " `asian_handicap_away_min_35_data` = " + str(SUM_asian_handicap_away_min_35) + ", "
    # query_update += " `asian_handicap_home_min_325_data` = " + str(SUM_asian_handicap_home_min_325) + ", "
    # query_update += " `asian_handicap_away_min_325_data` = " + str(SUM_asian_handicap_away_min_325) + ", "
    query_update += " `asian_handicap_home_min_3_data` = " + str(SUM_asian_handicap_home_min_3) + ", "
    query_update += " `asian_handicap_away_min_3_data` = " + str(SUM_asian_handicap_away_min_3) + ", "
    # query_update += " `asian_handicap_home_min_275_data` = " + str(SUM_asian_handicap_home_min_275) + ", "
    # query_update += " `asian_handicap_away_min_275_data` = " + str(SUM_asian_handicap_away_min_275) + ", "
    query_update += " `asian_handicap_home_min_25_data` = " + str(SUM_asian_handicap_home_min_25) + ", "
    query_update += " `asian_handicap_away_min_25_data` = " + str(SUM_asian_handicap_away_min_25) + ", "
    # query_update += " `asian_handicap_home_min_225_data` = " + str(SUM_asian_handicap_home_min_225) + ", "
    # query_update += " `asian_handicap_away_min_225_data` = " + str(SUM_asian_handicap_away_min_225) + ", "
    query_update += " `asian_handicap_home_min_2_data` = " + str(SUM_asian_handicap_home_min_2) + ", "
    query_update += " `asian_handicap_away_min_2_data` = " + str(SUM_asian_handicap_away_min_2) + ", "
    # query_update += " `asian_handicap_home_min_175_data` = " + str(SUM_asian_handicap_home_min_175) + ", "
    # query_update += " `asian_handicap_away_min_175_data` = " + str(SUM_asian_handicap_away_min_175) + ", "
    query_update += " `asian_handicap_home_min_15_data` = " + str(SUM_asian_handicap_home_min_15) + ", "
    query_update += " `asian_handicap_away_min_15_data` = " + str(SUM_asian_handicap_away_min_15) + ", "
    # query_update += " `asian_handicap_home_min_125_data` = " + str(SUM_asian_handicap_home_min_125) + ", "
    # query_update += " `asian_handicap_away_min_125_data` = " + str(SUM_asian_handicap_away_min_125) + ", "
    query_update += " `asian_handicap_home_min_1_data` = " + str(SUM_asian_handicap_home_min_1) + ", "
    query_update += " `asian_handicap_away_min_1_data` = " + str(SUM_asian_handicap_away_min_1) + ", "
    # query_update += " `asian_handicap_home_min_075_data` = " + str(SUM_asian_handicap_home_min_075) + ", "
    # query_update += " `asian_handicap_away_min_075_data` = " + str(SUM_asian_handicap_away_min_075) + ", "
    query_update += " `asian_handicap_home_min_05_data` = " + str(SUM_asian_handicap_home_min_05) + ", "
    query_update += " `asian_handicap_away_min_05_data` = " + str(SUM_asian_handicap_away_min_05) + ", "
    # query_update += " `asian_handicap_home_min_025_data` = " + str(SUM_asian_handicap_home_min_025) + ", "
    # query_update += " `asian_handicap_away_min_025_data` = " + str(SUM_asian_handicap_away_min_025) + ", "
    query_update += " `asian_handicap_home_plus_0_data` = " + str(SUM_asian_handicap_home_plus_0) + ", "
    query_update += " `asian_handicap_away_plus_0_data` = " + str(SUM_asian_handicap_away_plus_0) + ", "
    # query_update += " `asian_handicap_home_plus_025_data` = " + str(SUM_asian_handicap_home_plus_025) + ", "
    # query_update += " `asian_handicap_away_plus_025_data` = " + str(SUM_asian_handicap_away_plus_025) + ", "
    query_update += " `asian_handicap_home_plus_05_data` = " + str(SUM_asian_handicap_home_plus_05) + ", "
    query_update += " `asian_handicap_away_plus_05_data` = " + str(SUM_asian_handicap_away_plus_05) + ", "
    # query_update += " `asian_handicap_home_plus_075_data` = " + str(SUM_asian_handicap_home_plus_075) + ", "
    # query_update += " `asian_handicap_away_plus_075_data` = " + str(SUM_asian_handicap_away_plus_075) + ", "
    query_update += " `asian_handicap_home_plus_1_data` = " + str(SUM_asian_handicap_home_plus_1) + ", "
    query_update += " `asian_handicap_away_plus_1_data` = " + str(SUM_asian_handicap_away_plus_1) + ", "
    # query_update += " `asian_handicap_home_plus_125_data` = " + str(SUM_asian_handicap_home_plus_125) + ", "
    # query_update += " `asian_handicap_away_plus_125_data` = " + str(SUM_asian_handicap_away_plus_125) + ", "
    query_update += " `asian_handicap_home_plus_15_data` = " + str(SUM_asian_handicap_home_plus_15) + ", "
    query_update += " `asian_handicap_away_plus_15_data` = " + str(SUM_asian_handicap_away_plus_15) + ", "
    # query_update += " `asian_handicap_home_plus_175_data` = " + str(SUM_asian_handicap_home_plus_175) + ", "
    # query_update += " `asian_handicap_away_plus_175_data` = " + str(SUM_asian_handicap_away_plus_175) + ", "
    query_update += " `asian_handicap_home_plus_2_data` = " + str(SUM_asian_handicap_home_plus_2) + ", "
    query_update += " `asian_handicap_away_plus_2_data` = " + str(SUM_asian_handicap_away_plus_2) + ", "
    # query_update += " `asian_handicap_home_plus_225_data` = " + str(SUM_asian_handicap_home_plus_225) + ", "
    # query_update += " `asian_handicap_away_plus_225_data` = " + str(SUM_asian_handicap_away_plus_225) + ", "

    query_update += " `asian_handicap_home_plus_25_data` = " + str(SUM_asian_handicap_home_plus_25) + ", "
    query_update += " `asian_handicap_away_plus_25_data` = " + str(SUM_asian_handicap_away_plus_25) + ", "
    # query_update += " `asian_handicap_home_plus_275_data` = " + str(SUM_asian_handicap_home_plus_275) + ", "
    # query_update += " `asian_handicap_away_plus_275_data` = " + str(SUM_asian_handicap_away_plus_275) + ", "
    query_update += " `asian_handicap_home_plus_3_data` = " + str(SUM_asian_handicap_home_plus_3) + ", "
    query_update += " `asian_handicap_away_plus_3_data` = " + str(SUM_asian_handicap_away_plus_3) + ", "
    # query_update += " `asian_handicap_home_plus_325_data` = " + str(SUM_asian_handicap_home_plus_325) + ", "
    # query_update += " `asian_handicap_away_plus_325_data` = " + str(SUM_asian_handicap_away_plus_325) + ", "
    query_update += " `asian_handicap_home_plus_35_data` = " + str(SUM_asian_handicap_home_plus_35) + ", "
    query_update += " `asian_handicap_away_plus_35_data` = " + str(SUM_asian_handicap_away_plus_35) + ", "
    # query_update += " `asian_handicap_home_plus_375_data` = " + str(SUM_asian_handicap_home_plus_375) + ", "
    # query_update += " `asian_handicap_away_plus_375_data` = " + str(SUM_asian_handicap_away_plus_375) + ", "
    query_update += " `asian_handicap_home_plus_4_data` = " + str(SUM_asian_handicap_home_plus_4) + ", "
    query_update += " `asian_handicap_away_plus_4_data` = " + str(SUM_asian_handicap_away_plus_4) + ", "
    # query_update += " `asian_handicap_home_plus_425_data` = " + str(SUM_asian_handicap_home_plus_425) + ", "
    # query_update += " `asian_handicap_away_plus_425_data` = " + str(SUM_asian_handicap_away_plus_425) + ", "
    query_update += " `asian_handicap_home_plus_45_data` = " + str(SUM_asian_handicap_home_plus_45) + ", "
    query_update += " `asian_handicap_away_plus_45_data` = " + str(SUM_asian_handicap_away_plus_45) + ", "
    # query_update += " `asian_handicap_home_plus_475_data` = " + str(SUM_asian_handicap_home_plus_475) + ", "
    # query_update += " `asian_handicap_away_plus_475_data` = " + str(SUM_asian_handicap_away_plus_475) + ", "
    query_update += " `asian_handicap_home_plus_5_data` = " + str(SUM_asian_handicap_home_plus_5) + ", "
    query_update += " `asian_handicap_away_plus_5_data` = " + str(SUM_asian_handicap_away_plus_5) + ", "
    # query_update += " `asian_handicap_home_plus_525_data` = " + str(SUM_asian_handicap_home_plus_525) + ", "
    # query_update += " `asian_handicap_away_plus_525_data` = " + str(SUM_asian_handicap_away_plus_525) + ", "
    query_update += " `asian_handicap_home_plus_55_data` = " + str(SUM_asian_handicap_home_plus_55) + ", "
    query_update += " `asian_handicap_away_plus_55_data` = " + str(SUM_asian_handicap_away_plus_55) + ", "
    # query_update += " `asian_handicap_home_plus_575_data` = " + str(SUM_asian_handicap_home_plus_575) + ", "
    # query_update += " `asian_handicap_away_plus_575_data` = " + str(SUM_asian_handicap_away_plus_575) + ", "
    query_update += " `asian_handicap_home_plus_6_data` = " + str(SUM_asian_handicap_home_plus_6) + ", "
    query_update += " `asian_handicap_away_plus_6_data` = " + str(SUM_asian_handicap_away_plus_6) + ", "
    # query_update += " `asian_handicap_home_plus_625_data` = " + str(SUM_asian_handicap_home_plus_625) + ", "
    # query_update += " `asian_handicap_away_plus_625_data` = " + str(SUM_asian_handicap_away_plus_625) + ", "
    query_update += " `asian_handicap_home_plus_65_data` = " + str(SUM_asian_handicap_home_plus_65) + ", "
    query_update += " `asian_handicap_away_plus_65_data` = " + str(SUM_asian_handicap_away_plus_65) + ", "
    # query_update += " `asian_handicap_home_plus_675_data` = " + str(SUM_asian_handicap_home_plus_675) + ", "
    # query_update += " `asian_handicap_away_plus_675_data` = " + str(SUM_asian_handicap_away_plus_675) + ", "
    query_update += " `goals_overunder_over_05_data` = " + str(SUM_goals_overunder_over_05) + ", "
    query_update += " `goals_overunder_under_05_data` = " + str(SUM_goals_overunder_under_05) + ", "
    # query_update += " `goals_overunder_over_075_data` = " + str(SUM_goals_overunder_over_075) + ", "
    # query_update += " `goals_overunder_under_075_data` = " + str(SUM_goals_overunder_under_075) + ", "
    query_update += " `goals_overunder_over_10_data` = " + str(SUM_goals_overunder_over_10) + ", "
    query_update += " `goals_overunder_under_10_data` = " + str(SUM_goals_overunder_under_10) + ", "
    # query_update += " `goals_overunder_over_125_data` = " + str(SUM_goals_overunder_over_125) + ", "
    # query_update += " `goals_overunder_under_125_data` = " + str(SUM_goals_overunder_under_125) + ", "
    query_update += " `goals_overunder_over_15_data` = " + str(SUM_goals_overunder_over_15) + ", "
    query_update += " `goals_overunder_under_15_data` = " + str(SUM_goals_overunder_under_15) + ", "
    # query_update += " `goals_overunder_over_175_data` = " + str(SUM_goals_overunder_over_175) + ", "
    # query_update += " `goals_overunder_under_175_data` = " + str(SUM_goals_overunder_under_175) + ", "
    query_update += " `goals_overunder_over_20_data` = " + str(SUM_goals_overunder_over_20) + ", "
    query_update += " `goals_overunder_under_20_data` = " + str(SUM_goals_overunder_under_20) + ", "
    # query_update += " `goals_overunder_over_225_data` = " + str(SUM_goals_overunder_over_225) + ", "
    # query_update += " `goals_overunder_under_225_data` = " + str(SUM_goals_overunder_under_225) + ", "
    query_update += " `goals_overunder_over_25_data` = " + str(SUM_goals_overunder_over_25) + ", "
    query_update += " `goals_overunder_under_25_data` = " + str(SUM_goals_overunder_under_25) + ", "
    # query_update += " `goals_overunder_over_275_data` = " + str(SUM_goals_overunder_over_275) + ", "
    # query_update += " `goals_overunder_under_275_data` = " + str(SUM_goals_overunder_under_275) + ", "
    query_update += " `goals_overunder_over_30_data` = " + str(SUM_goals_overunder_over_30) + ", "
    query_update += " `goals_overunder_under_30_data` = " + str(SUM_goals_overunder_under_30) + ", "
    # query_update += " `goals_overunder_over_325_data` = " + str(SUM_goals_overunder_over_325) + ", "
    # query_update += " `goals_overunder_under_325_data` = " + str(SUM_goals_overunder_under_325) + ", "
    query_update += " `goals_overunder_over_35_data` = " + str(SUM_goals_overunder_over_35) + ", "
    query_update += " `goals_overunder_under_35_data` = " + str(SUM_goals_overunder_under_35) + ", "
    # query_update += " `goals_overunder_over_375_data` = " + str(SUM_goals_overunder_over_375) + ", "
    # query_update += " `goals_overunder_under_375_data` = " + str(SUM_goals_overunder_under_375) + ", "
    query_update += " `goals_overunder_over_40_data` = " + str(SUM_goals_overunder_over_40) + ", "
    query_update += " `goals_overunder_under_40_data` = " + str(SUM_goals_overunder_under_40) + ", "
    # query_update += " `goals_overunder_over_425_data` = " + str(SUM_goals_overunder_over_425) + ", "
    # query_update += " `goals_overunder_under_425_data` = " + str(SUM_goals_overunder_under_425) + ", "
    query_update += " `goals_overunder_over_45_data` = " + str(SUM_goals_overunder_over_45) + ", "
    query_update += " `goals_overunder_under_45_data` = " + str(SUM_goals_overunder_under_45) + ", "
    # query_update += " `goals_overunder_over_475_data` = " + str(SUM_goals_overunder_over_475) + ", "
    # query_update += " `goals_overunder_under_475_data` = " + str(SUM_goals_overunder_under_475) + ", "
    query_update += " `goals_overunder_over_50_data` = " + str(SUM_goals_overunder_over_50) + ", "
    query_update += " `goals_overunder_under_50_data` = " + str(SUM_goals_overunder_under_50) + ", "
    # query_update += " `goals_overunder_over_525_data` = " + str(SUM_goals_overunder_over_525) + ", "
    # query_update += " `goals_overunder_under_525_data` = " + str(SUM_goals_overunder_under_525) + ", "
    query_update += " `goals_overunder_over_55_data` = " + str(SUM_goals_overunder_over_55) + ", "
    query_update += " `goals_overunder_under_55_data` = " + str(SUM_goals_overunder_under_55) + ", "
    # query_update += " `goals_overunder_over_575_data` = " + str(SUM_goals_overunder_over_575) + ", "
    # query_update += " `goals_overunder_under_575_data` = " + str(SUM_goals_overunder_under_575) + ", "
    query_update += " `goals_overunder_over_60_data` = " + str(SUM_goals_overunder_over_60) + ", "
    query_update += " `goals_overunder_under_60_data` = " + str(SUM_goals_overunder_under_60) + ", "
    # query_update += " `goals_overunder_over_625_data` = " + str(SUM_goals_overunder_over_625) + ", " 
    # query_update += " `goals_overunder_under_625_data` = " + str(SUM_goals_overunder_under_625) + ", "
    query_update += " `goals_overunder_over_65_data` = " + str(SUM_goals_overunder_over_65) + ", "
    query_update += " `goals_overunder_under_65_data` = " + str(SUM_goals_overunder_under_65) + ", "
    # query_update += " `goals_overunder_over_675_data` = " + str(SUM_goals_overunder_over_675) + ", "
    # query_update += " `goals_overunder_under_675_data` = " + str(SUM_goals_overunder_under_675) + ", "
    query_update += " `goals_overunder_over_70_data` = " + str(SUM_goals_overunder_over_70) + ", "
    query_update += " `goals_overunder_under_70_data` = " + str(SUM_goals_overunder_under_70) + ", "
    query_update += " `goals_overunder_over_75_data` = " + str(SUM_goals_overunder_over_75) + ", "
    query_update += " `goals_overunder_under_75_data` = " + str(SUM_goals_overunder_under_75) + ", "
    query_update += " `goals_overunder_over_85_data` = " + str(SUM_goals_overunder_over_85) + ", "
    query_update += " `goals_overunder_under_85_data` = " + str(SUM_goals_overunder_under_85) + ", "
    query_update += " `goals_overunder_over_95_data` = " + str(SUM_goals_overunder_over_95) + ", "
    query_update += " `goals_overunder_under_95_data` = " + str(SUM_goals_overunder_under_95) + ", "
    query_update += " `goals_overunder_first_half_over_05_data` = " + str(SUM_goals_overunder_first_half_over_05) + ", "
    query_update += " `goals_overunder_first_half_under_05_data` = " + str(SUM_goals_overunder_first_half_under_05) + ", "
    # query_update += " `goals_overunder_first_half_over_075_data` = " + str(SUM_goals_overunder_first_half_over_075) + ", "
    # query_update += " `goals_overunder_first_half_under_075_data` = " + str(SUM_goals_overunder_first_half_under_075) + ", "
    query_update += " `goals_overunder_first_half_over_10_data` = " + str(SUM_goals_overunder_first_half_over_10) + ", "
    query_update += " `goals_overunder_first_half_under_10_data` = " + str(SUM_goals_overunder_first_half_under_10) + ", "
    # query_update += " `goals_overunder_first_half_over_125_data` = " + str(SUM_goals_overunder_first_half_over_125) + ", "
    # query_update += " `goals_overunder_first_half_under_125_data` = " + str(SUM_goals_overunder_first_half_under_125) + ", "
    query_update += " `goals_overunder_first_half_over_15_data` = " + str(SUM_goals_overunder_first_half_over_15) + ", "
    query_update += " `goals_overunder_first_half_under_15_data` = " + str(SUM_goals_overunder_first_half_under_15) + ", "
    # query_update += " `goals_overunder_first_half_over_175_data` = " + str(SUM_goals_overunder_first_half_over_175) + ", "
    # query_update += " `goals_overunder_first_half_under_175_data` = " + str(SUM_goals_overunder_first_half_under_175) + ", "
    query_update += " `goals_overunder_first_half_over_20_data` = " + str(SUM_goals_overunder_first_half_over_20) + ", "
    query_update += " `goals_overunder_first_half_under_20_data` = " + str(SUM_goals_overunder_first_half_under_20) + ", "
    # query_update += " `goals_overunder_first_half_over_225_data` = " + str(SUM_goals_overunder_first_half_over_225) + ", "
    # query_update += " `goals_overunder_first_half_under_225_data` = " + str(SUM_goals_overunder_first_half_under_225) + ", "
    query_update += " `goals_overunder_first_half_over_25_data` = " + str(SUM_goals_overunder_first_half_over_25) + ", "
    query_update += " `goals_overunder_first_half_under_25_data` = " + str(SUM_goals_overunder_first_half_under_25) + ", "
    # query_update += " `goals_overunder_first_half_over_275_data` = " + str(SUM_goals_overunder_first_half_over_275) + ", "
    # query_update += " `goals_overunder_first_half_under_275_data` = " + str(SUM_goals_overunder_first_half_under_275) + ", "
    query_update += " `goals_overunder_first_half_over_30_data` = " + str(SUM_goals_overunder_first_half_over_30) + ", "
    query_update += " `goals_overunder_first_half_under_30_data` = " + str(SUM_goals_overunder_first_half_under_30) + ", "
    # query_update += " `goals_overunder_first_half_over_325_data` = " + str(SUM_goals_overunder_first_half_over_325) + ", "
    # query_update += " `goals_overunder_first_half_under_325_data` = " + str(SUM_goals_overunder_first_half_under_325) + ", "
    query_update += " `goals_overunder_first_half_over_35_data` = " + str(SUM_goals_overunder_first_half_over_35) + ", "
    query_update += " `goals_overunder_first_half_under_35_data` = " + str(SUM_goals_overunder_first_half_under_35) + ", "
    # query_update += " `goals_overunder_first_half_over_375_data` = " + str(SUM_goals_overunder_first_half_over_375) + ", "
    # query_update += " `goals_overunder_first_half_under_375_data` = " + str(SUM_goals_overunder_first_half_under_375) + ", "
    query_update += " `htft_double_home_home_data` = " + str(SUM_htft_double_home_home) + ", "
    query_update += " `htft_double_home_draw_data` = " + str(SUM_htft_double_home_draw) + ", "
    query_update += " `htft_double_home_away_data` = " + str(SUM_htft_double_home_away) + ", "
    query_update += " `htft_double_draw_home_data` = " + str(SUM_htft_double_draw_home) + ", "
    query_update += " `htft_double_draw_draw_data` = " + str(SUM_htft_double_draw_draw) + ", "
    query_update += " `htft_double_draw_away_data` = " + str(SUM_htft_double_draw_away) + ", "
    query_update += " `htft_double_away_home_data` = " + str(SUM_htft_double_away_home) + ", "
    query_update += " `htft_double_away_draw_data` = " + str(SUM_htft_double_away_draw) + ", "
    query_update += " `htft_double_away_away_data` = " + str(SUM_htft_double_away_away) + ", "
    query_update += " `both_teams_score_yes_data` = " + str(SUM_both_teams_score_yes) + ", "
    query_update += " `both_teams_score_no_data` = " + str(SUM_both_teams_score_no) + ", "
    query_update += " `highest_scoring_half_first_data` = " + str(SUM_highest_scoring_half_first) + ", "
    query_update += " `highest_scoring_half_draw_data` = " + str(SUM_highest_scoring_half_draw) + ", "
    query_update += " `highest_scoring_half_second_data` = " + str(SUM_highest_scoring_half_second) + ", "
    query_update += " `double_chance_home_draw_data` = " + str(SUM_double_chance_home_draw) + ", "
    query_update += " `double_chance_home_away_data` = " + str(SUM_double_chance_home_away) + ", "
    query_update += " `double_chance_draw_away_data` = " + str(SUM_double_chance_draw_away) + ", "
    query_update += " `first_half_winner_home_data` = " + str(SUM_first_half_winner_home) + ", "
    query_update += " `first_half_winner_draw_data` = " + str(SUM_first_half_winner_draw) + ", "
    query_update += " `first_half_winner_away_data` = " + str(SUM_first_half_winner_away) + ", "
    query_update += " `total_home_over_15_data` = " + str(SUM_total_home_over_15) + ", "
    query_update += " `total_home_under_15_data` = " + str(SUM_total_home_under_15) + ", "
    query_update += " `total_home_over_25_data` = " + str(SUM_total_home_over_25) + ", "
    query_update += " `total_home_under_25_data` = " + str(SUM_total_home_under_25) + ", "
    query_update += " `total_home_over_35_data` = " + str(SUM_total_home_over_35) + ", "
    query_update += " `total_home_under_35_data` = " + str(SUM_total_home_under_35) + ", "
    query_update += " `total_home_over_45_data` = " + str(SUM_total_home_over_45) + ", "
    query_update += " `total_home_under_45_data` = " + str(SUM_total_home_under_45) + ", "
    query_update += " `total_home_over_55_data` = " + str(SUM_total_home_over_55) + ", "
    query_update += " `total_home_under_55_data` = " + str(SUM_total_home_under_55) + ", "
    query_update += " `total_home_over_65_data` = " + str(SUM_total_home_over_65) + ", "
    query_update += " `total_home_under_65_data` = " + str(SUM_total_home_under_65) + ", "
    query_update += " `total_away_over_15_data` = " + str(SUM_total_away_over_15) + ", "
    query_update += " `total_away_under_15_data` = " + str(SUM_total_away_under_15) + ", "
    query_update += " `total_away_over_25_data` = " + str(SUM_total_away_over_25) + ", "
    query_update += " `total_away_under_25_data` = " + str(SUM_total_away_under_25) + ", "
    query_update += " `total_away_over_35_data` = " + str(SUM_total_away_over_35) + ", "
    query_update += " `total_away_under_35_data` = " + str(SUM_total_away_under_35) + ", "
    query_update += " `total_away_over_45_data` = " + str(SUM_total_away_over_45) + ", "
    query_update += " `total_away_under_45_data` = " + str(SUM_total_away_under_45) + ", "
    query_update += " `total_away_over_55_data` = " + str(SUM_total_away_over_55) + ", "

    query_update += " `total_away_under_55_data` = " + str(SUM_total_away_under_55) + ", "
    query_update += " `total_away_over_65_data` = " + str(SUM_total_away_over_65) + ", "
    query_update += " `total_away_under_65_data` = " + str(SUM_total_away_under_65) + ", "
    # query_update += " `asian_handicap_first_half_home_min_175_data` = " + str(SUM_asian_handicap_first_half_home_min_175) + ", "
    # query_update += " `asian_handicap_first_half_away_min_175_data` = " + str(SUM_asian_handicap_first_half_away_min_175) + ", "
    query_update += " `asian_handicap_first_half_home_min_15_data` = " + str(SUM_asian_handicap_first_half_home_min_15) + ", "
    query_update += " `asian_handicap_first_half_away_min_15_data` = " + str(SUM_asian_handicap_first_half_away_min_15) + ", "
    # query_update += " `asian_handicap_first_half_home_min_125_data` = " + str(SUM_asian_handicap_first_half_home_min_125) + ", "
    # query_update += " `asian_handicap_first_half_away_min_125_data` = " + str(SUM_asian_handicap_first_half_away_min_125) + ", "
    query_update += " `asian_handicap_first_half_home_min_1_data` = " + str(SUM_asian_handicap_first_half_home_min_1) + ", "
    query_update += " `asian_handicap_first_half_away_min_1_data` = " + str(SUM_asian_handicap_first_half_away_min_1) + ", "
    # query_update += " `asian_handicap_first_half_home_min_075_data` = " + str(SUM_asian_handicap_first_half_home_min_075) + ", "
    # query_update += " `asian_handicap_first_half_away_min_075_data` = " + str(SUM_asian_handicap_first_half_away_min_075) + ", "
    query_update += " `asian_handicap_first_half_home_min_05_data` = " + str(SUM_asian_handicap_first_half_home_min_05) + ", "
    query_update += " `asian_handicap_first_half_away_min_05_data` = " + str(SUM_asian_handicap_first_half_away_min_05) + ", "
    # query_update += " `asian_handicap_first_half_home_min_025_data` = " + str(SUM_asian_handicap_first_half_home_min_025) + ", "
    # query_update += " `asian_handicap_first_half_away_min_025_data` = " + str(SUM_asian_handicap_first_half_away_min_025) + ", "
    query_update += " `asian_handicap_first_half_home_plus_0_data` = " + str(SUM_asian_handicap_first_half_home_plus_0) + ", "
    query_update += " `asian_handicap_first_half_away_plus_0_data` = " + str(SUM_asian_handicap_first_half_away_plus_0) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_025_data` = " + str(SUM_asian_handicap_first_half_home_plus_025) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_025_data` = " + str(SUM_asian_handicap_first_half_away_plus_025) + ", "
    query_update += " `asian_handicap_first_half_home_plus_05_data` = " + str(SUM_asian_handicap_first_half_home_plus_05) + ", "
    query_update += " `asian_handicap_first_half_away_plus_05_data` = " + str(SUM_asian_handicap_first_half_away_plus_05) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_075_data` = " + str(SUM_asian_handicap_first_half_home_plus_075) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_075_data` = " + str(SUM_asian_handicap_first_half_away_plus_075) + ", "
    query_update += " `asian_handicap_first_half_home_plus_1_data` = " + str(SUM_asian_handicap_first_half_home_plus_1) + ", "
    query_update += " `asian_handicap_first_half_away_plus_1_data` = " + str(SUM_asian_handicap_first_half_away_plus_1) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_125_data` = " + str(SUM_asian_handicap_first_half_home_plus_125) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_125_data` = " + str(SUM_asian_handicap_first_half_away_plus_125) + ", "
    query_update += " `asian_handicap_first_half_home_plus_15_data` = " + str(SUM_asian_handicap_first_half_home_plus_15) + ", "
    query_update += " `asian_handicap_first_half_away_plus_15_data` = " + str(SUM_asian_handicap_first_half_away_plus_15) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_175_data` = " + str(SUM_asian_handicap_first_half_home_plus_175) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_175_data` = " + str(SUM_asian_handicap_first_half_away_plus_175) + ", "
    query_update += " `double_chance__first_half_home_draw_data` = " + str(SUM_double_chance__first_half_home_draw) + ", "
    query_update += " `double_chance__first_half_home_away_data` = " + str(SUM_double_chance__first_half_home_away) + ", "
    query_update += " `double_chance__first_half_draw_away_data` = " + str(SUM_double_chance__first_half_draw_away) + ", "
    query_update += " `oddeven_odd_data` = " + str(SUM_oddeven_odd) + ", "
    query_update += " `oddeven_even_data` = " + str(SUM_oddeven_even) + ", "
    query_update += " `results_both_teams_score_home_yes_data` = " + str(SUM_results_both_teams_score_home_yes) + ", "
    query_update += " `results_both_teams_score_draw_yes_data` = " + str(SUM_results_both_teams_score_draw_yes) + ", "
    query_update += " `results_both_teams_score_away_yes_data` = " + str(SUM_results_both_teams_score_away_yes) + ", "
    query_update += " `results_both_teams_score_home_no_data` = " + str(SUM_results_both_teams_score_home_no) + ", "
    query_update += " `results_both_teams_score_draw_no_data` = " + str(SUM_results_both_teams_score_draw_no) + ", "
    query_update += " `results_both_teams_score_away_no_data` = " + str(SUM_results_both_teams_score_away_no) + ", "
    query_update += " `result_total_goals_home_over_35_data` = " + str(SUM_result_total_goals_home_over_35) + ", "
    query_update += " `result_total_goals_draw_over_35_data` = " + str(SUM_result_total_goals_draw_over_35) + ", "
    query_update += " `result_total_goals_away_over_35_data` = " + str(SUM_result_total_goals_away_over_35) + ", "
    query_update += " `result_total_goals_home_under_35_data` = " + str(SUM_result_total_goals_home_under_35) + ", "
    query_update += " `result_total_goals_draw_under_35_data` = " + str(SUM_result_total_goals_draw_under_35) + ", "
    query_update += " `result_total_goals_away_under_35_data` = " + str(SUM_result_total_goals_away_under_35) + ", "
    query_update += " `result_total_goals_home_over_25_data` = " + str(SUM_result_total_goals_home_over_25) + ", "
    query_update += " `result_total_goals_draw_over_25_data` = " + str(SUM_result_total_goals_draw_over_25) + ", "
    query_update += " `result_total_goals_away_over_25_data` = " + str(SUM_result_total_goals_away_over_25) + ", "
    query_update += " `result_total_goals_home_under_25_data` = " + str(SUM_result_total_goals_home_under_25) + ", "
    query_update += " `result_total_goals_draw_under_25_data` = " + str(SUM_result_total_goals_draw_under_25) + ", "
    query_update += " `result_total_goals_away_under_25_data` = " + str(SUM_result_total_goals_away_under_25) + ", "
    query_update += " `goals_overunder__second_half_over_05_data` = " + str(SUM_goals_overunder__second_half_over_05) + ", "
    query_update += " `goals_overunder__second_half_under_05_data` = " + str(SUM_goals_overunder__second_half_under_05) + ", "
    # query_update += " `goals_overunder__second_half_over_075_data` = " + str(SUM_goals_overunder__second_half_over_075) + ", "
    # query_update += " `goals_overunder__second_half_under_075_data` = " + str(SUM_goals_overunder__second_half_under_075) + ", "
    query_update += " `goals_overunder__second_half_over_10_data` = " + str(SUM_goals_overunder__second_half_over_10) + ", "
    query_update += " `goals_overunder__second_half_under_10_data` = " + str(SUM_goals_overunder__second_half_under_10) + ", "
    # query_update += " `goals_overunder__second_half_over_125_data` = " + str(SUM_goals_overunder__second_half_over_125) + ", "
    # query_update += " `goals_overunder__second_half_under_125_data` = " + str(SUM_goals_overunder__second_half_under_125) + ", "
    query_update += " `goals_overunder__second_half_over_15_data` = " + str(SUM_goals_overunder__second_half_over_15) + ", "
    query_update += " `goals_overunder__second_half_under_15_data` = " + str(SUM_goals_overunder__second_half_under_15) + ", "
    # query_update += " `goals_overunder__second_half_over_175_data` = " + str(SUM_goals_overunder__second_half_over_175) + ", "
    # query_update += " `goals_overunder__second_half_under_175_data` = " + str(SUM_goals_overunder__second_half_under_175) + ", "
    query_update += " `goals_overunder__second_half_over_20_data` = " + str(SUM_goals_overunder__second_half_over_20) + ", "
    query_update += " `goals_overunder__second_half_under_20_data` = " + str(SUM_goals_overunder__second_half_under_20) + ", " 
    # query_update += " `goals_overunder__second_half_over_225_data` = " + str(SUM_goals_overunder__second_half_over_225) + ", "
    # query_update += " `goals_overunder__second_half_under_225_data` = " + str(SUM_goals_overunder__second_half_under_225) + ", "
    query_update += " `goals_overunder__second_half_over_25_data` = " + str(SUM_goals_overunder__second_half_over_25) + ", "
    query_update += " `goals_overunder__second_half_under_25_data` = " + str(SUM_goals_overunder__second_half_under_25) + ", "
    # query_update += " `goals_overunder__second_half_over_275_data` = " + str(SUM_goals_overunder__second_half_over_275) + ", "
    # query_update += " `goals_overunder__second_half_under_275_data` = " + str(SUM_goals_overunder__second_half_under_275) + ", "
    query_update += " `goals_overunder__second_half_over_30_data` = " + str(SUM_goals_overunder__second_half_over_30) + ", "
    query_update += " `goals_overunder__second_half_under_30_data` = " + str(SUM_goals_overunder__second_half_under_30) + ", "
    # query_update += " `goals_overunder__second_half_over_325_data` = " + str(SUM_goals_overunder__second_half_over_325) + ", "
    # query_update += " `goals_overunder__second_half_under_325_data` = " + str(SUM_goals_overunder__second_half_under_325) + ", "
    query_update += " `goals_overunder__second_half_over_35_data` = " + str(SUM_goals_overunder__second_half_over_35) + ", "
    query_update += " `goals_overunder__second_half_under_35_data` = " + str(SUM_goals_overunder__second_half_under_35) + ", "
    # query_update += " `goals_overunder__second_half_over_375_data` = " + str(SUM_goals_overunder__second_half_over_375) + ", "
    # query_update += " `goals_overunder__second_half_under_375_data` = " + str(SUM_goals_overunder__second_half_under_375) + ", "
    query_update += " `clean_sheet__home_yes_data` = " + str(SUM_clean_sheet__home_yes) + ", "
    query_update += " `clean_sheet__home_no_data` = " + str(SUM_clean_sheet__home_no) + ", "
    query_update += " `clean_sheet__away_yes_data` = " + str(SUM_clean_sheet__away_yes) + ", "
    query_update += " `clean_sheet__away_no_data` = " + str(SUM_clean_sheet__away_no) + ", "
    query_update += " `win_both_halves_home_data` = " + str(SUM_win_both_halves_home) + ", "
    query_update += " `win_both_halves_away_data` = " + str(SUM_win_both_halves_away) + ", "
    query_update += " `both_teams_score__first_half_yes_data` = " + str(SUM_both_teams_score__first_half_yes) + ", "
    query_update += " `both_teams_score__first_half_no_data` = " + str(SUM_both_teams_score__first_half_no) + ", "
    query_update += " `both_teams_to_score__second_half_yes_data` = " + str(SUM_both_teams_to_score__second_half_yes) + ", "
    query_update += " `both_teams_to_score__second_half_no_data` = " + str(SUM_both_teams_to_score__second_half_no) + ", "
    query_update += " `win_to_nil_home_data` = " + str(SUM_win_to_nil_home) + ", "
    query_update += " `win_to_nil_away_data` = " + str(SUM_win_to_nil_away) + ", "
    query_update += " `exact_goals_number_0_data` = " + str(SUM_exact_goals_number_0) + ", "
    query_update += " `exact_goals_number_1_data` = " + str(SUM_exact_goals_number_1) + ", "
    query_update += " `exact_goals_number_2_data` = " + str(SUM_exact_goals_number_2) + ", "
    query_update += " `exact_goals_number_3_data` = " + str(SUM_exact_goals_number_3) + ", "
    query_update += " `exact_goals_number_4_data` = " + str(SUM_exact_goals_number_4) + ", "
    query_update += " `exact_goals_number_5_data` = " + str(SUM_exact_goals_number_5) + ", "
    query_update += " `exact_goals_number_6_data` = " + str(SUM_exact_goals_number_6) + ", "
    query_update += " `exact_goals_number_more_7_data` = " + str(SUM_exact_goals_number_more_7) + ", "
    query_update += " `to_win_either_half_home_data` = " + str(SUM_to_win_either_half_home) + ", "
    query_update += " `to_win_either_half_away_data` = " + str(SUM_to_win_either_half_away) + ", "
    query_update += " `home_team_exact_goals_number_0_data` = " + str(SUM_home_team_exact_goals_number_0) + ", "
    query_update += " `home_team_exact_goals_number_1_data` = " + str(SUM_home_team_exact_goals_number_1) + ", "
    query_update += " `home_team_exact_goals_number_2_data` = " + str(SUM_home_team_exact_goals_number_2) + ", "
    query_update += " `home_team_exact_goals_number_more_3_data` = " + str(SUM_home_team_exact_goals_number_more_3) + ", "
    query_update += " `away_team_exact_goals_number_0_data` = " + str(SUM_away_team_exact_goals_number_0) + ", "
    query_update += " `away_team_exact_goals_number_1_data` = " + str(SUM_away_team_exact_goals_number_1) + ", "
    query_update += " `away_team_exact_goals_number_2_data` = " + str(SUM_away_team_exact_goals_number_2) + ", "
    query_update += " `away_team_exact_goals_number_more_3_data` = " + str(SUM_away_team_exact_goals_number_more_3) + ", "
    query_update += " `second_half_exact_goals_number_0_data` = " + str(SUM_second_half_exact_goals_number_0) + ", "
    query_update += " `second_half_exact_goals_number_1_data` = " + str(SUM_second_half_exact_goals_number_1) + ", "
    query_update += " `second_half_exact_goals_number_2_data` = " + str(SUM_second_half_exact_goals_number_2) + ", "
    query_update += " `second_half_exact_goals_number_3_data` = " + str(SUM_second_half_exact_goals_number_3) + ", "
    query_update += " `second_half_exact_goals_number_4_data` = " + str(SUM_second_half_exact_goals_number_4) + ", "
    query_update += " `second_half_exact_goals_number_more_5_data` = " + str(SUM_second_half_exact_goals_number_more_5) + ", "
    query_update += " `exact_goals_number__first_half_0_data` = " + str(SUM_exact_goals_number__first_half_0) + ", "
    query_update += " `exact_goals_number__first_half_1_data` = " + str(SUM_exact_goals_number__first_half_1) + ", "
    query_update += " `exact_goals_number__first_half_2_data` = " + str(SUM_exact_goals_number__first_half_2) + ", "
    query_update += " `exact_goals_number__first_half_3_data` = " + str(SUM_exact_goals_number__first_half_3) + ", "
    query_update += " `exact_goals_number__first_half_4_data` = " + str(SUM_exact_goals_number__first_half_4) + ", "
    query_update += " `exact_goals_number__first_half_more_5_data` = " + str(SUM_exact_goals_number__first_half_more_5) + ", "
    query_update += " `to_score_in_both_halves_by_teams_home_data` = " + str(SUM_to_score_in_both_halves_by_teams_home) + ", "
    query_update += " `to_score_in_both_halves_by_teams_away_data` = " + str(SUM_to_score_in_both_halves_by_teams_away) + ", "
    query_update += " `total_goals_both_teams_to_score_over_yes_25_data` = " + str(SUM_total_goals_both_teams_to_score_over_yes_25) + ", "
    query_update += " `total_goals_both_teams_to_score_over_no_25_data` = " + str(SUM_total_goals_both_teams_to_score_over_no_25) + ", "
    query_update += " `total_goals_both_teams_to_score_under_yes_25_data` = " + str(SUM_total_goals_both_teams_to_score_under_yes_25) + ", "
    query_update += " `total_goals_both_teams_to_score_under_no_25_data` = " + str(SUM_total_goals_both_teams_to_score_under_no_25) + ", "
    query_update += " `halftime_result_both_teams_score_home_yes_data` = " + str(SUM_halftime_result_both_teams_score_home_yes) + ", "
    query_update += " `halftime_result_both_teams_score_draw_yes_data` = " + str(SUM_halftime_result_both_teams_score_draw_yes) + ", "
    query_update += " `halftime_result_both_teams_score_away_yes_data` = " + str(SUM_halftime_result_both_teams_score_away_yes) + ", "
    query_update += " `halftime_result_both_teams_score_home_no_data` = " + str(SUM_halftime_result_both_teams_score_home_no) + ", "
    query_update += " `halftime_result_both_teams_score_draw_no_data` = " + str(SUM_halftime_result_both_teams_score_draw_no) + ", "
    query_update += " `halftime_result_both_teams_score_away_no_data` = " + str(SUM_halftime_result_both_teams_score_away_no) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_yes_yes_data` = " + str(SUM_both_teams_to_score_1st_half__2nd_half_yes_yes) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_yes_no_data` = " + str(SUM_both_teams_to_score_1st_half__2nd_half_yes_no) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_no_yes_data` = " + str(SUM_both_teams_to_score_1st_half__2nd_half_no_yes) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_no_no_data` = " + str(SUM_both_teams_to_score_1st_half__2nd_half_no_no) + ", "
    query_update += " `total_goals_under_2_data` = " + str(SUM_total_goals_under_2) + ", "

    query_update += " `total_goals_2_or_3_data` = " + str(SUM_total_goals_2_or_3) + ", "
    query_update += " `total_goals_over_3_data` = " + str(SUM_total_goals_over_3) + ", "
    query_update += " `match_winner_home_perc` = " + str(AVG_match_winner_home) + ", "
    query_update += " `match_winner_draw_perc` = " + str(AVG_match_winner_draw) + ", "
    query_update += " `match_winner_away_perc` = " + str(AVG_match_winner_away) + ", "
    query_update += " `homeaway_home_perc` = " + str(AVG_homeaway_home) + ", "
    query_update += " `homeaway_away_perc` = " + str(AVG_homeaway_away) + ", "
    query_update += " `second_half_winner_home_perc` = " + str(AVG_second_half_winner_home) + ", "
    query_update += " `second_half_winner_draw_perc` = " + str(AVG_second_half_winner_draw) + ", "
    query_update += " `second_half_winner_away_perc` = " + str(AVG_second_half_winner_away) + ", "
    # query_update += " `asian_handicap_home_min_675_perc` = " + str(AVG_asian_handicap_home_min_675) + ", "
    # query_update += " `asian_handicap_away_min_675_perc` = " + str(AVG_asian_handicap_away_min_675) + ", "
    query_update += " `asian_handicap_home_min_65_perc` = " + str(AVG_asian_handicap_home_min_65) + ", "
    query_update += " `asian_handicap_away_min_65_perc` = " + str(AVG_asian_handicap_away_min_65) + ", "
    # query_update += " `asian_handicap_home_min_625_perc` = " + str(AVG_asian_handicap_home_min_625) + ", "
    # query_update += " `asian_handicap_away_min_625_perc` = " + str(AVG_asian_handicap_away_min_625) + ", "
    query_update += " `asian_handicap_home_min_6_perc` = " + str(AVG_asian_handicap_home_min_6) + ", "
    query_update += " `asian_handicap_away_min_6_perc` = " + str(AVG_asian_handicap_away_min_6) + ", "
    # query_update += " `asian_handicap_home_min_575_perc` = " + str(AVG_asian_handicap_home_min_575) + ", "
    # query_update += " `asian_handicap_away_min_575_perc` = " + str(AVG_asian_handicap_away_min_575) + ", "
    query_update += " `asian_handicap_home_min_55_perc` = " + str(AVG_asian_handicap_home_min_55) + ", "
    query_update += " `asian_handicap_away_min_55_perc` = " + str(AVG_asian_handicap_away_min_55) + ", "
    # query_update += " `asian_handicap_home_min_525_perc` = " + str(AVG_asian_handicap_home_min_525) + ", "
    # query_update += " `asian_handicap_away_min_525_perc` = " + str(AVG_asian_handicap_away_min_525) + ", "
    query_update += " `asian_handicap_home_min_5_perc` = " + str(AVG_asian_handicap_home_min_5) + ", "
    query_update += " `asian_handicap_away_min_5_perc` = " + str(AVG_asian_handicap_away_min_5) + ", "
    # query_update += " `asian_handicap_home_min_475_perc` = " + str(AVG_asian_handicap_home_min_475) + ", "
    # query_update += " `asian_handicap_away_min_475_perc` = " + str(AVG_asian_handicap_away_min_475) + ", "
    query_update += " `asian_handicap_home_min_45_perc` = " + str(AVG_asian_handicap_home_min_45) + ", "
    query_update += " `asian_handicap_away_min_45_perc` = " + str(AVG_asian_handicap_away_min_45) + ", "
    # query_update += " `asian_handicap_home_min_425_perc` = " + str(AVG_asian_handicap_home_min_425) + ", "
    # query_update += " `asian_handicap_away_min_425_perc` = " + str(AVG_asian_handicap_away_min_425) + ", "
    query_update += " `asian_handicap_home_min_4_perc` = " + str(AVG_asian_handicap_home_min_4) + ", "
    query_update += " `asian_handicap_away_min_4_perc` = " + str(AVG_asian_handicap_away_min_4) + ", "
    # query_update += " `asian_handicap_home_min_375_perc` = " + str(AVG_asian_handicap_home_min_375) + ", "
    # query_update += " `asian_handicap_away_min_375_perc` = " + str(AVG_asian_handicap_away_min_375) + ", "
    query_update += " `asian_handicap_home_min_35_perc` = " + str(AVG_asian_handicap_home_min_35) + ", "
    query_update += " `asian_handicap_away_min_35_perc` = " + str(AVG_asian_handicap_away_min_35) + ", "
    # query_update += " `asian_handicap_home_min_325_perc` = " + str(AVG_asian_handicap_home_min_325) + ", "
    # query_update += " `asian_handicap_away_min_325_perc` = " + str(AVG_asian_handicap_away_min_325) + ", "
    query_update += " `asian_handicap_home_min_3_perc` = " + str(AVG_asian_handicap_home_min_3) + ", "
    query_update += " `asian_handicap_away_min_3_perc` = " + str(AVG_asian_handicap_away_min_3) + ", "
    # query_update += " `asian_handicap_home_min_275_perc` = " + str(AVG_asian_handicap_home_min_275) + ", "
    # query_update += " `asian_handicap_away_min_275_perc` = " + str(AVG_asian_handicap_away_min_275) + ", "
    query_update += " `asian_handicap_home_min_25_perc` = " + str(AVG_asian_handicap_home_min_25) + ", "
    query_update += " `asian_handicap_away_min_25_perc` = " + str(AVG_asian_handicap_away_min_25) + ", "
    # query_update += " `asian_handicap_home_min_225_perc` = " + str(AVG_asian_handicap_home_min_225) + ", "
    # query_update += " `asian_handicap_away_min_225_perc` = " + str(AVG_asian_handicap_away_min_225) + ", "
    query_update += " `asian_handicap_home_min_2_perc` = " + str(AVG_asian_handicap_home_min_2) + ", "
    query_update += " `asian_handicap_away_min_2_perc` = " + str(AVG_asian_handicap_away_min_2) + ", "
    # query_update += " `asian_handicap_home_min_175_perc` = " + str(AVG_asian_handicap_home_min_175) + ", "
    # query_update += " `asian_handicap_away_min_175_perc` = " + str(AVG_asian_handicap_away_min_175) + ", "
    query_update += " `asian_handicap_home_min_15_perc` = " + str(AVG_asian_handicap_home_min_15) + ", "
    query_update += " `asian_handicap_away_min_15_perc` = " + str(AVG_asian_handicap_away_min_15) + ", "
    # query_update += " `asian_handicap_home_min_125_perc` = " + str(AVG_asian_handicap_home_min_125) + ", "
    # query_update += " `asian_handicap_away_min_125_perc` = " + str(AVG_asian_handicap_away_min_125) + ", "
    query_update += " `asian_handicap_home_min_1_perc` = " + str(AVG_asian_handicap_home_min_1) + ", "
    query_update += " `asian_handicap_away_min_1_perc` = " + str(AVG_asian_handicap_away_min_1) + ", "
    # query_update += " `asian_handicap_home_min_075_perc` = " + str(AVG_asian_handicap_home_min_075) + ", "
    # query_update += " `asian_handicap_away_min_075_perc` = " + str(AVG_asian_handicap_away_min_075) + ", "
    query_update += " `asian_handicap_home_min_05_perc` = " + str(AVG_asian_handicap_home_min_05) + ", "
    query_update += " `asian_handicap_away_min_05_perc` = " + str(AVG_asian_handicap_away_min_05) + ", "
    # query_update += " `asian_handicap_home_min_025_perc` = " + str(AVG_asian_handicap_home_min_025) + ", "
    # query_update += " `asian_handicap_away_min_025_perc` = " + str(AVG_asian_handicap_away_min_025) + ", "
    query_update += " `asian_handicap_home_plus_0_perc` = " + str(AVG_asian_handicap_home_plus_0) + ", "
    query_update += " `asian_handicap_away_plus_0_perc` = " + str(AVG_asian_handicap_away_plus_0) + ", "
    # query_update += " `asian_handicap_home_plus_025_perc` = " + str(AVG_asian_handicap_home_plus_025) + ", "
    # query_update += " `asian_handicap_away_plus_025_perc` = " + str(AVG_asian_handicap_away_plus_025) + ", "
    query_update += " `asian_handicap_home_plus_05_perc` = " + str(AVG_asian_handicap_home_plus_05) + ", "
    query_update += " `asian_handicap_away_plus_05_perc` = " + str(AVG_asian_handicap_away_plus_05) + ", "
    # query_update += " `asian_handicap_home_plus_075_perc` = " + str(AVG_asian_handicap_home_plus_075) + ", "
    # query_update += " `asian_handicap_away_plus_075_perc` = " + str(AVG_asian_handicap_away_plus_075) + ", "
    query_update += " `asian_handicap_home_plus_1_perc` = " + str(AVG_asian_handicap_home_plus_1) + ", "
    query_update += " `asian_handicap_away_plus_1_perc` = " + str(AVG_asian_handicap_away_plus_1) + ", "
    # query_update += " `asian_handicap_home_plus_125_perc` = " + str(AVG_asian_handicap_home_plus_125) + ", "
    # query_update += " `asian_handicap_away_plus_125_perc` = " + str(AVG_asian_handicap_away_plus_125) + ", "
    query_update += " `asian_handicap_home_plus_15_perc` = " + str(AVG_asian_handicap_home_plus_15) + ", "
    query_update += " `asian_handicap_away_plus_15_perc` = " + str(AVG_asian_handicap_away_plus_15) + ", "
    # query_update += " `asian_handicap_home_plus_175_perc` = " + str(AVG_asian_handicap_home_plus_175) + ", "
    # query_update += " `asian_handicap_away_plus_175_perc` = " + str(AVG_asian_handicap_away_plus_175) + ", "
    query_update += " `asian_handicap_home_plus_2_perc` = " + str(AVG_asian_handicap_home_plus_2) + ", "
    query_update += " `asian_handicap_away_plus_2_perc` = " + str(AVG_asian_handicap_away_plus_2) + ", "

    # query_update += " `asian_handicap_home_plus_225_perc` = " + str(AVG_asian_handicap_home_plus_225) + ", "
    # query_update += " `asian_handicap_away_plus_225_perc` = " + str(AVG_asian_handicap_away_plus_225) + ", "
    query_update += " `asian_handicap_home_plus_25_perc` = " + str(AVG_asian_handicap_home_plus_25) + ", "
    query_update += " `asian_handicap_away_plus_25_perc` = " + str(AVG_asian_handicap_away_plus_25) + ", "
    # query_update += " `asian_handicap_home_plus_275_perc` = " + str(AVG_asian_handicap_home_plus_275) + ", "
    # query_update += " `asian_handicap_away_plus_275_perc` = " + str(AVG_asian_handicap_away_plus_275) + ", "
    query_update += " `asian_handicap_home_plus_3_perc` = " + str(AVG_asian_handicap_home_plus_3) + ", "
    query_update += " `asian_handicap_away_plus_3_perc` = " + str(AVG_asian_handicap_away_plus_3) + ", "
    # query_update += " `asian_handicap_home_plus_325_perc` = " + str(AVG_asian_handicap_home_plus_325) + ", "
    # query_update += " `asian_handicap_away_plus_325_perc` = " + str(AVG_asian_handicap_away_plus_325) + ", "
    query_update += " `asian_handicap_home_plus_35_perc` = " + str(AVG_asian_handicap_home_plus_35) + ", "
    query_update += " `asian_handicap_away_plus_35_perc` = " + str(AVG_asian_handicap_away_plus_35) + ", "
    # query_update += " `asian_handicap_home_plus_375_perc` = " + str(AVG_asian_handicap_home_plus_375) + ", "
    # query_update += " `asian_handicap_away_plus_375_perc` = " + str(AVG_asian_handicap_away_plus_375) + ", "
    query_update += " `asian_handicap_home_plus_4_perc` = " + str(AVG_asian_handicap_home_plus_4) + ", "
    query_update += " `asian_handicap_away_plus_4_perc` = " + str(AVG_asian_handicap_away_plus_4) + ", "
    # query_update += " `asian_handicap_home_plus_425_perc` = " + str(AVG_asian_handicap_home_plus_425) + ", "
    # query_update += " `asian_handicap_away_plus_425_perc` = " + str(AVG_asian_handicap_away_plus_425) + ", "
    query_update += " `asian_handicap_home_plus_45_perc` = " + str(AVG_asian_handicap_home_plus_45) + ", "
    query_update += " `asian_handicap_away_plus_45_perc` = " + str(AVG_asian_handicap_away_plus_45) + ", "
    # query_update += " `asian_handicap_home_plus_475_perc` = " + str(AVG_asian_handicap_home_plus_475) + ", "
    # query_update += " `asian_handicap_away_plus_475_perc` = " + str(AVG_asian_handicap_away_plus_475) + ", "
    query_update += " `asian_handicap_home_plus_5_perc` = " + str(AVG_asian_handicap_home_plus_5) + ", "
    query_update += " `asian_handicap_away_plus_5_perc` = " + str(AVG_asian_handicap_away_plus_5) + ", "
    # query_update += " `asian_handicap_home_plus_525_perc` = " + str(AVG_asian_handicap_home_plus_525) + ", "
    # query_update += " `asian_handicap_away_plus_525_perc` = " + str(AVG_asian_handicap_away_plus_525) + ", "
    query_update += " `asian_handicap_home_plus_55_perc` = " + str(AVG_asian_handicap_home_plus_55) + ", "
    query_update += " `asian_handicap_away_plus_55_perc` = " + str(AVG_asian_handicap_away_plus_55) + ", "
    # query_update += " `asian_handicap_home_plus_575_perc` = " + str(AVG_asian_handicap_home_plus_575) + ", "
    # query_update += " `asian_handicap_away_plus_575_perc` = " + str(AVG_asian_handicap_away_plus_575) + ", "
    query_update += " `asian_handicap_home_plus_6_perc` = " + str(AVG_asian_handicap_home_plus_6) + ", "
    query_update += " `asian_handicap_away_plus_6_perc` = " + str(AVG_asian_handicap_away_plus_6) + ", "
    # query_update += " `asian_handicap_home_plus_625_perc` = " + str(AVG_asian_handicap_home_plus_625) + ", "
    # query_update += " `asian_handicap_away_plus_625_perc` = " + str(AVG_asian_handicap_away_plus_625) + ", "
    query_update += " `asian_handicap_home_plus_65_perc` = " + str(AVG_asian_handicap_home_plus_65) + ", "
    query_update += " `asian_handicap_away_plus_65_perc` = " + str(AVG_asian_handicap_away_plus_65) + ", "
    # query_update += " `asian_handicap_home_plus_675_perc` = " + str(AVG_asian_handicap_home_plus_675) + ", "
    # query_update += " `asian_handicap_away_plus_675_perc` = " + str(AVG_asian_handicap_away_plus_675) + ", "
    query_update += " `goals_overunder_over_05_perc` = " + str(AVG_goals_overunder_over_05) + ", "
    query_update += " `goals_overunder_under_05_perc` = " + str(AVG_goals_overunder_under_05) + ", "
    # query_update += " `goals_overunder_over_075_perc` = " + str(AVG_goals_overunder_over_075) + ", "
    # query_update += " `goals_overunder_under_075_perc` = " + str(AVG_goals_overunder_under_075) + ", "
    query_update += " `goals_overunder_over_10_perc` = " + str(AVG_goals_overunder_over_10) + ", "
    query_update += " `goals_overunder_under_10_perc` = " + str(AVG_goals_overunder_under_10) + ", "
    # query_update += " `goals_overunder_over_125_perc` = " + str(AVG_goals_overunder_over_125) + ", "
    # query_update += " `goals_overunder_under_125_perc` = " + str(AVG_goals_overunder_under_125) + ", "
    query_update += " `goals_overunder_over_15_perc` = " + str(AVG_goals_overunder_over_15) + ", "
    query_update += " `goals_overunder_under_15_perc` = " + str(AVG_goals_overunder_under_15) + ", "
    # query_update += " `goals_overunder_over_175_perc` = " + str(AVG_goals_overunder_over_175) + ", "
    # query_update += " `goals_overunder_under_175_perc` = " + str(AVG_goals_overunder_under_175) + ", "
    query_update += " `goals_overunder_over_20_perc` = " + str(AVG_goals_overunder_over_20) + ", "
    query_update += " `goals_overunder_under_20_perc` = " + str(AVG_goals_overunder_under_20) + ", "
    # query_update += " `goals_overunder_over_225_perc` = " + str(AVG_goals_overunder_over_225) + ", "
    # query_update += " `goals_overunder_under_225_perc` = " + str(AVG_goals_overunder_under_225) + ", "
    query_update += " `goals_overunder_over_25_perc` = " + str(AVG_goals_overunder_over_25) + ", "
    query_update += " `goals_overunder_under_25_perc` = " + str(AVG_goals_overunder_under_25) + ", "
    # query_update += " `goals_overunder_over_275_perc` = " + str(AVG_goals_overunder_over_275) + ", "
    # query_update += " `goals_overunder_under_275_perc` = " + str(AVG_goals_overunder_under_275) + ", "
    query_update += " `goals_overunder_over_30_perc` = " + str(AVG_goals_overunder_over_30) + ", "
    query_update += " `goals_overunder_under_30_perc` = " + str(AVG_goals_overunder_under_30) + ", "
    # query_update += " `goals_overunder_over_325_perc` = " + str(AVG_goals_overunder_over_325) + ", "
    # query_update += " `goals_overunder_under_325_perc` = " + str(AVG_goals_overunder_under_325) + ", "
    query_update += " `goals_overunder_over_35_perc` = " + str(AVG_goals_overunder_over_35) + ", "
    query_update += " `goals_overunder_under_35_perc` = " + str(AVG_goals_overunder_under_35) + ", "
    # query_update += " `goals_overunder_over_375_perc` = " + str(AVG_goals_overunder_over_375) + ", "
    # query_update += " `goals_overunder_under_375_perc` = " + str(AVG_goals_overunder_under_375) + ", "
    query_update += " `goals_overunder_over_40_perc` = " + str(AVG_goals_overunder_over_40) + ", "
    query_update += " `goals_overunder_under_40_perc` = " + str(AVG_goals_overunder_under_40) + ", "
    # query_update += " `goals_overunder_over_425_perc` = " + str(AVG_goals_overunder_over_425) + ", "
    # query_update += " `goals_overunder_under_425_perc` = " + str(AVG_goals_overunder_under_425) + ", "
    query_update += " `goals_overunder_over_45_perc` = " + str(AVG_goals_overunder_over_45) + ", "
    query_update += " `goals_overunder_under_45_perc` = " + str(AVG_goals_overunder_under_45) + ", "
    # query_update += " `goals_overunder_over_475_perc` = " + str(AVG_goals_overunder_over_475) + ", "
    # query_update += " `goals_overunder_under_475_perc` = " + str(AVG_goals_overunder_under_475) + ", "
    query_update += " `goals_overunder_over_50_perc` = " + str(AVG_goals_overunder_over_50) + ", "
    query_update += " `goals_overunder_under_50_perc` = " + str(AVG_goals_overunder_under_50) + ", "
    # query_update += " `goals_overunder_over_525_perc` = " + str(AVG_goals_overunder_over_525) + ", "
    # query_update += " `goals_overunder_under_525_perc` = " + str(AVG_goals_overunder_under_525) + ", "
    query_update += " `goals_overunder_over_55_perc` = " + str(AVG_goals_overunder_over_55) + ", "
    query_update += " `goals_overunder_under_55_perc` = " + str(AVG_goals_overunder_under_55) + ", "
    # query_update += " `goals_overunder_over_575_perc` = " + str(AVG_goals_overunder_over_575) + ", "
    # query_update += " `goals_overunder_under_575_perc` = " + str(AVG_goals_overunder_under_575) + ", "

    query_update += " `goals_overunder_over_60_perc` = " + str(AVG_goals_overunder_over_60) + ", "
    query_update += " `goals_overunder_under_60_perc` = " + str(AVG_goals_overunder_under_60) + ", "
    # query_update += " `goals_overunder_over_625_perc` = " + str(AVG_goals_overunder_over_625) + ", "
    # query_update += " `goals_overunder_under_625_perc` = " + str(AVG_goals_overunder_under_625) + ", "
    query_update += " `goals_overunder_over_65_perc` = " + str(AVG_goals_overunder_over_65) + ", "
    query_update += " `goals_overunder_under_65_perc` = " + str(AVG_goals_overunder_under_65) + ", "
    # query_update += " `goals_overunder_over_675_perc` = " + str(AVG_goals_overunder_over_675) + ", "
    # query_update += " `goals_overunder_under_675_perc` = " + str(AVG_goals_overunder_under_675) + ", "
    query_update += " `goals_overunder_over_70_perc` = " + str(AVG_goals_overunder_over_70) + ", "
    query_update += " `goals_overunder_under_70_perc` = " + str(AVG_goals_overunder_under_70) + ", "
    query_update += " `goals_overunder_over_75_perc` = " + str(AVG_goals_overunder_over_75) + ", "
    query_update += " `goals_overunder_under_75_perc` = " + str(AVG_goals_overunder_under_75) + ", "
    query_update += " `goals_overunder_over_85_perc` = " + str(AVG_goals_overunder_over_85) + ", "
    query_update += " `goals_overunder_under_85_perc` = " + str(AVG_goals_overunder_under_85) + ", "
    query_update += " `goals_overunder_over_95_perc` = " + str(AVG_goals_overunder_over_95) + ", "
    query_update += " `goals_overunder_under_95_perc` = " + str(AVG_goals_overunder_under_95) + ", "
    query_update += " `goals_overunder_first_half_over_05_perc` = " + str(AVG_goals_overunder_first_half_over_05) + ", "
    query_update += " `goals_overunder_first_half_under_05_perc` = " + str(AVG_goals_overunder_first_half_under_05) + ", "
    # query_update += " `goals_overunder_first_half_over_075_perc` = " + str(AVG_goals_overunder_first_half_over_075) + ", "
    # query_update += " `goals_overunder_first_half_under_075_perc` = " + str(AVG_goals_overunder_first_half_under_075) + ", "
    query_update += " `goals_overunder_first_half_over_10_perc` = " + str(AVG_goals_overunder_first_half_over_10) + ", "
    query_update += " `goals_overunder_first_half_under_10_perc` = " + str(AVG_goals_overunder_first_half_under_10) + ", "
    # query_update += " `goals_overunder_first_half_over_125_perc` = " + str(AVG_goals_overunder_first_half_over_125) + ", "
    # query_update += " `goals_overunder_first_half_under_125_perc` = " + str(AVG_goals_overunder_first_half_under_125) + ", "
    query_update += " `goals_overunder_first_half_over_15_perc` = " + str(AVG_goals_overunder_first_half_over_15) + ", "
    query_update += " `goals_overunder_first_half_under_15_perc` = " + str(AVG_goals_overunder_first_half_under_15) + ", "
    # query_update += " `goals_overunder_first_half_over_175_perc` = " + str(AVG_goals_overunder_first_half_over_175) + ", "
    # query_update += " `goals_overunder_first_half_under_175_perc` = " + str(AVG_goals_overunder_first_half_under_175) + ", "
    query_update += " `goals_overunder_first_half_over_20_perc` = " + str(AVG_goals_overunder_first_half_over_20) + ", "
    query_update += " `goals_overunder_first_half_under_20_perc` = " + str(AVG_goals_overunder_first_half_under_20) + ", "
    # query_update += " `goals_overunder_first_half_over_225_perc` = " + str(AVG_goals_overunder_first_half_over_225) + ", "
    # query_update += " `goals_overunder_first_half_under_225_perc` = " + str(AVG_goals_overunder_first_half_under_225) + ", "
    query_update += " `goals_overunder_first_half_over_25_perc` = " + str(AVG_goals_overunder_first_half_over_25) + ", "
    query_update += " `goals_overunder_first_half_under_25_perc` = " + str(AVG_goals_overunder_first_half_under_25) + ", "
    # query_update += " `goals_overunder_first_half_over_275_perc` = " + str(AVG_goals_overunder_first_half_over_275) + ", "
    # query_update += " `goals_overunder_first_half_under_275_perc` = " + str(AVG_goals_overunder_first_half_under_275) + ", "
    query_update += " `goals_overunder_first_half_over_30_perc` = " + str(AVG_goals_overunder_first_half_over_30) + ", "
    query_update += " `goals_overunder_first_half_under_30_perc` = " + str(AVG_goals_overunder_first_half_under_30) + ", "
    # query_update += " `goals_overunder_first_half_over_325_perc` = " + str(AVG_goals_overunder_first_half_over_325) + ", "
    # query_update += " `goals_overunder_first_half_under_325_perc` = " + str(AVG_goals_overunder_first_half_under_325) + ", "
    query_update += " `goals_overunder_first_half_over_35_perc` = " + str(AVG_goals_overunder_first_half_over_35) + ", "
    query_update += " `goals_overunder_first_half_under_35_perc` = " + str(AVG_goals_overunder_first_half_under_35) + ", "
    # query_update += " `goals_overunder_first_half_over_375_perc` = " + str(AVG_goals_overunder_first_half_over_375) + ", "
    # query_update += " `goals_overunder_first_half_under_375_perc` = " + str(AVG_goals_overunder_first_half_under_375) + ", "
    query_update += " `htft_double_home_home_perc` = " + str(AVG_htft_double_home_home) + ", "
    query_update += " `htft_double_home_draw_perc` = " + str(AVG_htft_double_home_draw) + ", "
    query_update += " `htft_double_home_away_perc` = " + str(AVG_htft_double_home_away) + ", "
    query_update += " `htft_double_draw_home_perc` = " + str(AVG_htft_double_draw_home) + ", "
    query_update += " `htft_double_draw_draw_perc` = " + str(AVG_htft_double_draw_draw) + ", "
    query_update += " `htft_double_draw_away_perc` = " + str(AVG_htft_double_draw_away) + ", "
    query_update += " `htft_double_away_home_perc` = " + str(AVG_htft_double_away_home) + ", "
    query_update += " `htft_double_away_draw_perc` = " + str(AVG_htft_double_away_draw) + ", "
    query_update += " `htft_double_away_away_perc` = " + str(AVG_htft_double_away_away) + ", "
    query_update += " `both_teams_score_yes_perc` = " + str(AVG_both_teams_score_yes) + ", "
    query_update += " `both_teams_score_no_perc` = " + str(AVG_both_teams_score_no) + ", "
    query_update += " `highest_scoring_half_first_perc` = " + str(AVG_highest_scoring_half_first) + ", "
    query_update += " `highest_scoring_half_draw_perc` = " + str(AVG_highest_scoring_half_draw) + ", "
    query_update += " `highest_scoring_half_second_perc` = " + str(AVG_highest_scoring_half_second) + ", "
    query_update += " `double_chance_home_draw_perc` = " + str(AVG_double_chance_home_draw) + ", "
    query_update += " `double_chance_home_away_perc` = " + str(AVG_double_chance_home_away) + ", "
    query_update += " `double_chance_draw_away_perc` = " + str(AVG_double_chance_draw_away) + ", "
    query_update += " `first_half_winner_home_perc` = " + str(AVG_first_half_winner_home) + ", "
    query_update += " `first_half_winner_draw_perc` = " + str(AVG_first_half_winner_draw) + ", "
    query_update += " `first_half_winner_away_perc` = " + str(AVG_first_half_winner_away) + ", "
    query_update += " `total_home_over_15_perc` = " + str(AVG_total_home_over_15) + ", "
    query_update += " `total_home_under_15_perc` = " + str(AVG_total_home_under_15) + ", "
    query_update += " `total_home_over_25_perc` = " + str(AVG_total_home_over_25) + ", "
    query_update += " `total_home_under_25_perc` = " + str(AVG_total_home_under_25) + ", "
    query_update += " `total_home_over_35_perc` = " + str(AVG_total_home_over_35) + ", "
    query_update += " `total_home_under_35_perc` = " + str(AVG_total_home_under_35) + ", "
    query_update += " `total_home_over_45_perc` = " + str(AVG_total_home_over_45) + ", "
    query_update += " `total_home_under_45_perc` = " + str(AVG_total_home_under_45) + ", "
    query_update += " `total_home_over_55_perc` = " + str(AVG_total_home_over_55) + ", "
    query_update += " `total_home_under_55_perc` = " + str(AVG_total_home_under_55) + ", "
    query_update += " `total_home_over_65_perc` = " + str(AVG_total_home_over_65) + ", "
    query_update += " `total_home_under_65_perc` = " + str(AVG_total_home_under_65) + ", "
    query_update += " `total_away_over_15_perc` = " + str(AVG_total_away_over_15) + ", "
    query_update += " `total_away_under_15_perc` = " + str(AVG_total_away_under_15) + ", "
    query_update += " `total_away_over_25_perc` = " + str(AVG_total_away_over_25) + ", "
    query_update += " `total_away_under_25_perc` = " + str(AVG_total_away_under_25) + ", "
    query_update += " `total_away_over_35_perc` = " + str(AVG_total_away_over_35) + ", "

    query_update += " `total_away_under_35_perc` = " + str(AVG_total_away_under_35) + ", "
    query_update += " `total_away_over_45_perc` = " + str(AVG_total_away_over_45) + ", "
    query_update += " `total_away_under_45_perc` = " + str(AVG_total_away_under_45) + ", "
    query_update += " `total_away_over_55_perc` = " + str(AVG_total_away_over_55) + ", "
    query_update += " `total_away_under_55_perc` = " + str(AVG_total_away_under_55) + ", "
    query_update += " `total_away_over_65_perc` = " + str(AVG_total_away_over_65) + ", "
    query_update += " `total_away_under_65_perc` = " + str(AVG_total_away_under_65) + ", "
    # query_update += " `asian_handicap_first_half_home_min_175_perc` = " + str(AVG_asian_handicap_first_half_home_min_175) + ", "
    # query_update += " `asian_handicap_first_half_away_min_175_perc` = " + str(AVG_asian_handicap_first_half_away_min_175) + ", "
    query_update += " `asian_handicap_first_half_home_min_15_perc` = " + str(AVG_asian_handicap_first_half_home_min_15) + ", "
    query_update += " `asian_handicap_first_half_away_min_15_perc` = " + str(AVG_asian_handicap_first_half_away_min_15) + ", "
    # query_update += " `asian_handicap_first_half_home_min_125_perc` = " + str(AVG_asian_handicap_first_half_home_min_125) + ", "
    # query_update += " `asian_handicap_first_half_away_min_125_perc` = " + str(AVG_asian_handicap_first_half_away_min_125) + ", "
    query_update += " `asian_handicap_first_half_home_min_1_perc` = " + str(AVG_asian_handicap_first_half_home_min_1) + ", "
    query_update += " `asian_handicap_first_half_away_min_1_perc` = " + str(AVG_asian_handicap_first_half_away_min_1) + ", "
    # query_update += " `asian_handicap_first_half_home_min_075_perc` = " + str(AVG_asian_handicap_first_half_home_min_075) + ", "
    # query_update += " `asian_handicap_first_half_away_min_075_perc` = " + str(AVG_asian_handicap_first_half_away_min_075) + ", "
    query_update += " `asian_handicap_first_half_home_min_05_perc` = " + str(AVG_asian_handicap_first_half_home_min_05) + ", "
    query_update += " `asian_handicap_first_half_away_min_05_perc` = " + str(AVG_asian_handicap_first_half_away_min_05) + ", "
    # query_update += " `asian_handicap_first_half_home_min_025_perc` = " + str(AVG_asian_handicap_first_half_home_min_025) + ", "
    # query_update += " `asian_handicap_first_half_away_min_025_perc` = " + str(AVG_asian_handicap_first_half_away_min_025) + ", "
    query_update += " `asian_handicap_first_half_home_plus_0_perc` = " + str(AVG_asian_handicap_first_half_home_plus_0) + ", "
    query_update += " `asian_handicap_first_half_away_plus_0_perc` = " + str(AVG_asian_handicap_first_half_away_plus_0) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_025_perc` = " + str(AVG_asian_handicap_first_half_home_plus_025) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_025_perc` = " + str(AVG_asian_handicap_first_half_away_plus_025) + ", "
    query_update += " `asian_handicap_first_half_home_plus_05_perc` = " + str(AVG_asian_handicap_first_half_home_plus_05) + ", "
    query_update += " `asian_handicap_first_half_away_plus_05_perc` = " + str(AVG_asian_handicap_first_half_away_plus_05) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_075_perc` = " + str(AVG_asian_handicap_first_half_home_plus_075) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_075_perc` = " + str(AVG_asian_handicap_first_half_away_plus_075) + ", "
    query_update += " `asian_handicap_first_half_home_plus_1_perc` = " + str(AVG_asian_handicap_first_half_home_plus_1) + ", "
    query_update += " `asian_handicap_first_half_away_plus_1_perc` = " + str(AVG_asian_handicap_first_half_away_plus_1) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_125_perc` = " + str(AVG_asian_handicap_first_half_home_plus_125) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_125_perc` = " + str(AVG_asian_handicap_first_half_away_plus_125) + ", "
    query_update += " `asian_handicap_first_half_home_plus_15_perc` = " + str(AVG_asian_handicap_first_half_home_plus_15) + ", "
    query_update += " `asian_handicap_first_half_away_plus_15_perc` = " + str(AVG_asian_handicap_first_half_away_plus_15) + ", "
    # query_update += " `asian_handicap_first_half_home_plus_175_perc` = " + str(AVG_asian_handicap_first_half_home_plus_175) + ", "
    # query_update += " `asian_handicap_first_half_away_plus_175_perc` = " + str(AVG_asian_handicap_first_half_away_plus_175) + ", "
    query_update += " `double_chance__first_half_home_draw_perc` = " + str(AVG_double_chance__first_half_home_draw) + ", "
    query_update += " `double_chance__first_half_home_away_perc` = " + str(AVG_double_chance__first_half_home_away) + ", "
    query_update += " `double_chance__first_half_draw_away_perc` = " + str(AVG_double_chance__first_half_draw_away) + ", "
    query_update += " `oddeven_odd_perc` = " + str(AVG_oddeven_odd) + ", "
    query_update += " `oddeven_even_perc` = " + str(AVG_oddeven_even) + ", "
    query_update += " `results_both_teams_score_home_yes_perc` = " + str(AVG_results_both_teams_score_home_yes) + ", "
    query_update += " `results_both_teams_score_draw_yes_perc` = " + str(AVG_results_both_teams_score_draw_yes) + ", "
    query_update += " `results_both_teams_score_away_yes_perc` = " + str(AVG_results_both_teams_score_away_yes) + ", "
    query_update += " `results_both_teams_score_home_no_perc` = " + str(AVG_results_both_teams_score_home_no) + ", "
    query_update += " `results_both_teams_score_draw_no_perc` = " + str(AVG_results_both_teams_score_draw_no) + ", "
    query_update += " `results_both_teams_score_away_no_perc` = " + str(AVG_results_both_teams_score_away_no) + ", "
    query_update += " `result_total_goals_home_over_35_perc` = " + str(AVG_result_total_goals_home_over_35) + ", "
    query_update += " `result_total_goals_draw_over_35_perc` = " + str(AVG_result_total_goals_draw_over_35) + ", "
    query_update += " `result_total_goals_away_over_35_perc` = " + str(AVG_result_total_goals_away_over_35) + ", "
    query_update += " `result_total_goals_home_under_35_perc` = " + str(AVG_result_total_goals_home_under_35) + ", "
    query_update += " `result_total_goals_draw_under_35_perc` = " + str(AVG_result_total_goals_draw_under_35) + ", "
    query_update += " `result_total_goals_away_under_35_perc` = " + str(AVG_result_total_goals_away_under_35) + ", "
    query_update += " `result_total_goals_home_over_25_perc` = " + str(AVG_result_total_goals_home_over_25) + ", "
    query_update += " `result_total_goals_draw_over_25_perc` = " + str(AVG_result_total_goals_draw_over_25) + ", "
    query_update += " `result_total_goals_away_over_25_perc` = " + str(AVG_result_total_goals_away_over_25) + ", "
    query_update += " `result_total_goals_home_under_25_perc` = " + str(AVG_result_total_goals_home_under_25) + ", "
    query_update += " `result_total_goals_draw_under_25_perc` = " + str(AVG_result_total_goals_draw_under_25) + ", "
    query_update += " `result_total_goals_away_under_25_perc` = " + str(AVG_result_total_goals_away_under_25) + ", "
    query_update += " `goals_overunder__second_half_over_05_perc` = " + str(AVG_goals_overunder__second_half_over_05) + ", "
    query_update += " `goals_overunder__second_half_under_05_perc` = " + str(AVG_goals_overunder__second_half_under_05) + ", "
    # query_update += " `goals_overunder__second_half_over_075_perc` = " + str(AVG_goals_overunder__second_half_over_075) + ", "
    # query_update += " `goals_overunder__second_half_under_075_perc` = " + str(AVG_goals_overunder__second_half_under_075) + ", "
    query_update += " `goals_overunder__second_half_over_10_perc` = " + str(AVG_goals_overunder__second_half_over_10) + ", "
    query_update += " `goals_overunder__second_half_under_10_perc` = " + str(AVG_goals_overunder__second_half_under_10) + ", "
    # query_update += " `goals_overunder__second_half_over_125_perc` = " + str(AVG_goals_overunder__second_half_over_125) + ", "
    # query_update += " `goals_overunder__second_half_under_125_perc` = " + str(AVG_goals_overunder__second_half_under_125) + ", "
    query_update += " `goals_overunder__second_half_over_15_perc` = " + str(AVG_goals_overunder__second_half_over_15) + ", "
    query_update += " `goals_overunder__second_half_under_15_perc` = " + str(AVG_goals_overunder__second_half_under_15) + ", "
    # query_update += " `goals_overunder__second_half_over_175_perc` = " + str(AVG_goals_overunder__second_half_over_175) + ", " 
    # query_update += " `goals_overunder__second_half_under_175_perc` = " + str(AVG_goals_overunder__second_half_under_175) + ", "
    query_update += " `goals_overunder__second_half_over_20_perc` = " + str(AVG_goals_overunder__second_half_over_20) + ", "
    query_update += " `goals_overunder__second_half_under_20_perc` = " + str(AVG_goals_overunder__second_half_under_20) + ", "
    # query_update += " `goals_overunder__second_half_over_225_perc` = " + str(AVG_goals_overunder__second_half_over_225) + ", "
    # query_update += " `goals_overunder__second_half_under_225_perc` = " + str(AVG_goals_overunder__second_half_under_225) + ", "
    query_update += " `goals_overunder__second_half_over_25_perc` = " + str(AVG_goals_overunder__second_half_over_25) + ", "
    query_update += " `goals_overunder__second_half_under_25_perc` = " + str(AVG_goals_overunder__second_half_under_25) + ", "
    # query_update += " `goals_overunder__second_half_over_275_perc` = " + str(AVG_goals_overunder__second_half_over_275) + ", "
    # query_update += " `goals_overunder__second_half_under_275_perc` = " + str(AVG_goals_overunder__second_half_under_275) + ", "
    query_update += " `goals_overunder__second_half_over_30_perc` = " + str(AVG_goals_overunder__second_half_over_30) + ", "
    query_update += " `goals_overunder__second_half_under_30_perc` = " + str(AVG_goals_overunder__second_half_under_30) + ", "
    # query_update += " `goals_overunder__second_half_over_325_perc` = " + str(AVG_goals_overunder__second_half_over_325) + ", "
    # query_update += " `goals_overunder__second_half_under_325_perc` = " + str(AVG_goals_overunder__second_half_under_325) + ", "
    query_update += " `goals_overunder__second_half_over_35_perc` = " + str(AVG_goals_overunder__second_half_over_35) + ", "
    query_update += " `goals_overunder__second_half_under_35_perc` = " + str(AVG_goals_overunder__second_half_under_35) + ", "
    # query_update += " `goals_overunder__second_half_over_375_perc` = " + str(AVG_goals_overunder__second_half_over_375) + ", "
    # query_update += " `goals_overunder__second_half_under_375_perc` = " + str(AVG_goals_overunder__second_half_under_375) + ", "
    query_update += " `clean_sheet__home_yes_perc` = " + str(AVG_clean_sheet__home_yes) + ", "
    query_update += " `clean_sheet__home_no_perc` = " + str(AVG_clean_sheet__home_no) + ", "
    query_update += " `clean_sheet__away_yes_perc` = " + str(AVG_clean_sheet__away_yes) + ", "
    query_update += " `clean_sheet__away_no_perc` = " + str(AVG_clean_sheet__away_no) + ", "
    query_update += " `win_both_halves_home_perc` = " + str(AVG_win_both_halves_home) + ", "
    query_update += " `win_both_halves_away_perc` = " + str(AVG_win_both_halves_away) + ", "
    query_update += " `both_teams_score__first_half_yes_perc` = " + str(AVG_both_teams_score__first_half_yes) + ", "
    query_update += " `both_teams_score__first_half_no_perc` = " + str(AVG_both_teams_score__first_half_no) + ", "
    query_update += " `both_teams_to_score__second_half_yes_perc` = " + str(AVG_both_teams_to_score__second_half_yes) + ", "
    query_update += " `both_teams_to_score__second_half_no_perc` = " + str(AVG_both_teams_to_score__second_half_no) + ", "
    query_update += " `win_to_nil_home_perc` = " + str(AVG_win_to_nil_home) + ", "
    query_update += " `win_to_nil_away_perc` = " + str(AVG_win_to_nil_away) + ", "
    query_update += " `exact_goals_number_0_perc` = " + str(AVG_exact_goals_number_0) + ", "
    query_update += " `exact_goals_number_1_perc` = " + str(AVG_exact_goals_number_1) + ", "
    query_update += " `exact_goals_number_2_perc` = " + str(AVG_exact_goals_number_2) + ", "
    query_update += " `exact_goals_number_3_perc` = " + str(AVG_exact_goals_number_3) + ", "
    query_update += " `exact_goals_number_4_perc` = " + str(AVG_exact_goals_number_4) + ", "
    query_update += " `exact_goals_number_5_perc` = " + str(AVG_exact_goals_number_5) + ", "
    query_update += " `exact_goals_number_6_perc` = " + str(AVG_exact_goals_number_6) + ", "
    query_update += " `exact_goals_number_more_7_perc` = " + str(AVG_exact_goals_number_more_7) + ", "
    query_update += " `to_win_either_half_home_perc` = " + str(AVG_to_win_either_half_home) + ", "
    query_update += " `to_win_either_half_away_perc` = " + str(AVG_to_win_either_half_away) + ", "
    query_update += " `home_team_exact_goals_number_0_perc` = " + str(AVG_home_team_exact_goals_number_0) + ", "
    query_update += " `home_team_exact_goals_number_1_perc` = " + str(AVG_home_team_exact_goals_number_1) + ", "
    query_update += " `home_team_exact_goals_number_2_perc` = " + str(AVG_home_team_exact_goals_number_2) + ", "
    query_update += " `home_team_exact_goals_number_more_3_perc` = " + str(AVG_home_team_exact_goals_number_more_3) + ", "
    query_update += " `away_team_exact_goals_number_0_perc` = " + str(AVG_away_team_exact_goals_number_0) + ", "
    query_update += " `away_team_exact_goals_number_1_perc` = " + str(AVG_away_team_exact_goals_number_1) + ", "
    query_update += " `away_team_exact_goals_number_2_perc` = " + str(AVG_away_team_exact_goals_number_2) + ", "
    query_update += " `away_team_exact_goals_number_more_3_perc` = " + str(AVG_away_team_exact_goals_number_more_3) + ", "
    query_update += " `second_half_exact_goals_number_0_perc` = " + str(AVG_second_half_exact_goals_number_0) + ", "
    query_update += " `second_half_exact_goals_number_1_perc` = " + str(AVG_second_half_exact_goals_number_1) + ", "
    query_update += " `second_half_exact_goals_number_2_perc` = " + str(AVG_second_half_exact_goals_number_2) + ", "
    query_update += " `second_half_exact_goals_number_3_perc` = " + str(AVG_second_half_exact_goals_number_3) + ", "
    query_update += " `second_half_exact_goals_number_4_perc` = " + str(AVG_second_half_exact_goals_number_4) + ", "
    query_update += " `second_half_exact_goals_number_more_5_perc` = " + str(AVG_second_half_exact_goals_number_more_5) + ", "
    query_update += " `exact_goals_number__first_half_0_perc` = " + str(AVG_exact_goals_number__first_half_0) + ", "
    query_update += " `exact_goals_number__first_half_1_perc` = " + str(AVG_exact_goals_number__first_half_1) + ", "
    query_update += " `exact_goals_number__first_half_2_perc` = " + str(AVG_exact_goals_number__first_half_2) + ", "
    query_update += " `exact_goals_number__first_half_3_perc` = " + str(AVG_exact_goals_number__first_half_3) + ", "
    query_update += " `exact_goals_number__first_half_4_perc` = " + str(AVG_exact_goals_number__first_half_4) + ", "
    query_update += " `exact_goals_number__first_half_more_5_perc` = " + str(AVG_exact_goals_number__first_half_more_5) + ", "
    query_update += " `to_score_in_both_halves_by_teams_home_perc` = " + str(AVG_to_score_in_both_halves_by_teams_home) + ", "
    query_update += " `to_score_in_both_halves_by_teams_away_perc` = " + str(AVG_to_score_in_both_halves_by_teams_away) + ", "
    query_update += " `total_goals_both_teams_to_score_over_yes_25_perc` = " + str(AVG_total_goals_both_teams_to_score_over_yes_25) + ", "
    query_update += " `total_goals_both_teams_to_score_over_no_25_perc` = " + str(AVG_total_goals_both_teams_to_score_over_no_25) + ", "
    query_update += " `total_goals_both_teams_to_score_under_yes_25_perc` = " + str(AVG_total_goals_both_teams_to_score_under_yes_25) + ", "
    query_update += " `total_goals_both_teams_to_score_under_no_25_perc` = " + str(AVG_total_goals_both_teams_to_score_under_no_25) + ", "
    query_update += " `halftime_result_both_teams_score_home_yes_perc` = " + str(AVG_halftime_result_both_teams_score_home_yes) + ", "
    query_update += " `halftime_result_both_teams_score_draw_yes_perc` = " + str(AVG_halftime_result_both_teams_score_draw_yes) + ", "
    query_update += " `halftime_result_both_teams_score_away_yes_perc` = " + str(AVG_halftime_result_both_teams_score_away_yes) + ", "
    query_update += " `halftime_result_both_teams_score_home_no_perc` = " + str(AVG_halftime_result_both_teams_score_home_no) + ", "
    query_update += " `halftime_result_both_teams_score_draw_no_perc` = " + str(AVG_halftime_result_both_teams_score_draw_no) + ", "
    query_update += " `halftime_result_both_teams_score_away_no_perc` = " + str(AVG_halftime_result_both_teams_score_away_no) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_yes_yes_perc` = " + str(AVG_both_teams_to_score_1st_half__2nd_half_yes_yes) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_yes_no_perc` = " + str(AVG_both_teams_to_score_1st_half__2nd_half_yes_no) + ", "

    query_update += " `both_teams_to_score_1st_half__2nd_half_no_yes_perc` = " + str(AVG_both_teams_to_score_1st_half__2nd_half_no_yes) + ", "
    query_update += " `both_teams_to_score_1st_half__2nd_half_no_no_perc` = " + str(AVG_both_teams_to_score_1st_half__2nd_half_no_no) + ", "
    query_update += " `total_goals_under_2_perc` = " + str(AVG_total_goals_under_2) + ", "
    query_update += " `total_goals_2_or_3_perc` = " + str(AVG_total_goals_2_or_3) + ", "
    query_update += " `total_goals_over_3_perc` = " + str(AVG_total_goals_over_3) + ", "

    query_update += " `total_fixtures` = " + str(PRE_total_rows) + " "
      
    query_update += " WHERE leagueapi_id = " + str(leagueapi_id) + " "  
    query_update += " and `pre_ah_pattern` like '"+str(pre_ah_pattern)+"' "  
    query_update += " and `pre_gou_pattern` like '"+str(pre_gou_pattern)+"' "  
    query_update += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
    query_update += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    if(SUM_match_winner_home is not None and
        SUM_match_winner_draw is not None and
        SUM_match_winner_away is not None 
    ):
        # ------------------------------------------------------ 
        # print(space + query_update, flush=True) 
        # ------------------------------------------------------ 
        mycursor.execute(query_update)
        mydb.commit()    
        # close the cursor and database connection
        mycursor.close()
        mydb.close()
        # ------------------------------------------------------  
        print(space + "query update done", flush=True) 
        # ------------------------------------------------------   
        # ------------------------------------------------------  
        pattern_TABLE = "pattern_"+TABLE
        # ------------------------------------------------------  
        query_update = " UPDATE `football_odds` SET "  
        query_update += " "+pattern_TABLE+" = 1 "   
        query_update += " WHERE leagueapi_id = " + str(leagueapi_id) + " "  
        query_update += " and `pre_ah_pattern` like '"+str(pre_ah_pattern)+"' "  
        query_update += " and `pre_gou_pattern` like '"+str(pre_gou_pattern)+"' "  
        query_update += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query_update += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
        # ------------------------------------------------------  
        print(space + query_update, flush=True) 
        # ------------------------------------------------------  
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------  
        mycursor.execute(query_update)
        mydb.commit()     
        # close the cursor and database connection
        mycursor.close()
        mydb.close()
        # ------------------------------------------------------  
        print(space + pattern_TABLE + " update done", flush=True) 
        # ------------------------------------------------------  
    else: 
        # ------------------------------------------------------  
        print(space + "query CANT update", flush=True) 

