# Import
import mysql.connector 

def pd_get_fixtures_next_match(day0, day1, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pd_get_fixtures_next_match()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------   
    if(ROUTES == 'one'):
        PREP_COL = "end_" 
    elif(ROUTES == 'fixture'):
        PREP_COL = "pre_" 
    elif(ROUTES == 'research_pre'):
        PREP_COL = "pre_" 
    elif(ROUTES == 'research_end'):
        PREP_COL = "end_" 
    elif(ROUTES == 'preleague'):
        PREP_COL = "pre_" 
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
    query += " fixtureapi_id, " 

    query += " teams_home, " 
    query += " teams_away, " 
    query += " date " 

    query += " , "+PREP_COL+"both_teams_score_yes " 
    query += " , "+PREP_COL+"both_teams_score_no " 

    query += " , "+PREP_COL+"rcard_yes " 
    query += " , "+PREP_COL+"rcard_no " 

    query += " , "+PREP_COL+"first_half_winner_home " 
    query += " , "+PREP_COL+"first_half_winner_draw " 
    query += " , "+PREP_COL+"first_half_winner_away " 

    query += " , "+PREP_COL+"second_half_winner_home " 
    query += " , "+PREP_COL+"second_half_winner_draw " 
    query += " , "+PREP_COL+"second_half_winner_away " 

    query += " , "+PREP_COL+"htft_double_home_home "
    query += " , "+PREP_COL+"htft_double_home_draw "
    query += " , "+PREP_COL+"htft_double_home_away "
    query += " , "+PREP_COL+"htft_double_draw_home "
    query += " , "+PREP_COL+"htft_double_draw_draw "
    query += " , "+PREP_COL+"htft_double_draw_away "
    query += " , "+PREP_COL+"htft_double_away_home "
    query += " , "+PREP_COL+"htft_double_away_draw "
    query += " , "+PREP_COL+"htft_double_away_away " 

    query += " , "+PREP_COL+"both_teams_score__first_half_yes " 
    query += " , "+PREP_COL+"both_teams_score__first_half_no " 

    query += " , "+PREP_COL+"both_teams_to_score__second_half_yes " 
    query += " , "+PREP_COL+"both_teams_to_score__second_half_no " 

    query += " , "+PREP_COL+"results_both_teams_score_home_yes "
    query += " , "+PREP_COL+"results_both_teams_score_draw_yes "
    query += " , "+PREP_COL+"results_both_teams_score_away_yes "
    query += " , "+PREP_COL+"results_both_teams_score_home_no "
    query += " , "+PREP_COL+"results_both_teams_score_draw_no "
    query += " , "+PREP_COL+"results_both_teams_score_away_no " 
    
    # ------------------------------------------------------
    query += " , "+PREP_COL+"to_score_in_both_halves_by_teams_home"
    query += " , "+PREP_COL+"to_score_in_both_halves_by_teams_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"total_goals_both_teams_to_score_over_yes_25"
    query += " , "+PREP_COL+"total_goals_both_teams_to_score_over_no_25"
    query += " , "+PREP_COL+"total_goals_both_teams_to_score_under_yes_25"
    query += " , "+PREP_COL+"total_goals_both_teams_to_score_under_no_25"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"both_teams_to_score_1st_half__2nd_half_yes_yes"
    query += " , "+PREP_COL+"both_teams_to_score_1st_half__2nd_half_yes_no"
    query += " , "+PREP_COL+"both_teams_to_score_1st_half__2nd_half_no_yes"
    query += " , "+PREP_COL+"both_teams_to_score_1st_half__2nd_half_no_no"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"highest_scoring_half_first"
    query += " , "+PREP_COL+"highest_scoring_half_draw"
    query += " , "+PREP_COL+"highest_scoring_half_second"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"double_chance_home_draw"
    query += " , "+PREP_COL+"double_chance_home_away"
    query += " , "+PREP_COL+"double_chance_draw_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"double_chance__first_half_home_draw"
    query += " , "+PREP_COL+"double_chance__first_half_home_away"
    query += " , "+PREP_COL+"double_chance__first_half_draw_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"oddeven_odd"
    query += " , "+PREP_COL+"oddeven_even"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"result_total_goals_home_over_35"
    query += " , "+PREP_COL+"result_total_goals_draw_over_35"
    query += " , "+PREP_COL+"result_total_goals_away_over_35"
    query += " , "+PREP_COL+"result_total_goals_home_under_35"
    query += " , "+PREP_COL+"result_total_goals_draw_under_35"
    query += " , "+PREP_COL+"result_total_goals_away_under_35"
    query += " , "+PREP_COL+"result_total_goals_home_over_25"
    query += " , "+PREP_COL+"result_total_goals_draw_over_25"
    query += " , "+PREP_COL+"result_total_goals_away_over_25"
    query += " , "+PREP_COL+"result_total_goals_home_under_25"
    query += " , "+PREP_COL+"result_total_goals_draw_under_25"
    query += " , "+PREP_COL+"result_total_goals_away_under_25"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"clean_sheet__home_yes"
    query += " , "+PREP_COL+"clean_sheet__home_no"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"clean_sheet__away_yes"
    query += " , "+PREP_COL+"clean_sheet__away_no"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"win_both_halves_home"
    query += " , "+PREP_COL+"win_both_halves_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"win_to_nil_home"
    query += " , "+PREP_COL+"win_to_nil_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"to_win_either_half_home"
    query += " , "+PREP_COL+"to_win_either_half_away"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"halftime_result_both_teams_score_home_yes"
    query += " , "+PREP_COL+"halftime_result_both_teams_score_draw_yes"
    query += " , "+PREP_COL+"halftime_result_both_teams_score_away_yes"
    query += " , "+PREP_COL+"halftime_result_both_teams_score_home_no"
    query += " , "+PREP_COL+"halftime_result_both_teams_score_draw_no"
    query += " , "+PREP_COL+"halftime_result_both_teams_score_away_no"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"exact_goals_number__first_half_0"
    query += " , "+PREP_COL+"exact_goals_number__first_half_1"
    query += " , "+PREP_COL+"exact_goals_number__first_half_2"
    query += " , "+PREP_COL+"exact_goals_number__first_half_3"
    query += " , "+PREP_COL+"exact_goals_number__first_half_4"
    query += " , "+PREP_COL+"exact_goals_number__first_half_more_5"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"second_half_exact_goals_number_0"
    query += " , "+PREP_COL+"second_half_exact_goals_number_1"
    query += " , "+PREP_COL+"second_half_exact_goals_number_2"
    query += " , "+PREP_COL+"second_half_exact_goals_number_3"
    query += " , "+PREP_COL+"second_half_exact_goals_number_4"
    query += " , "+PREP_COL+"second_half_exact_goals_number_more_5"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"home_team_exact_goals_number_0"
    query += " , "+PREP_COL+"home_team_exact_goals_number_1"
    query += " , "+PREP_COL+"home_team_exact_goals_number_2"
    query += " , "+PREP_COL+"home_team_exact_goals_number_more_3"
    # ------------------------------------------------------
    query += " , "+PREP_COL+"away_team_exact_goals_number_0"
    query += " , "+PREP_COL+"away_team_exact_goals_number_1"
    query += " , "+PREP_COL+"away_team_exact_goals_number_2"
    query += " , "+PREP_COL+"away_team_exact_goals_number_more_3"
    # ------------------------------------------------------ 
    query += " , "+PREP_COL+"asian_handicap_home_min_675"
    query += " , "+PREP_COL+"asian_handicap_away_min_675"
    query += " , "+PREP_COL+"asian_handicap_home_min_65"
    query += " , "+PREP_COL+"asian_handicap_away_min_65"
    query += " , "+PREP_COL+"asian_handicap_home_min_625"
    query += " , "+PREP_COL+"asian_handicap_away_min_625"
    query += " , "+PREP_COL+"asian_handicap_home_min_6"
    query += " , "+PREP_COL+"asian_handicap_away_min_6"
    query += " , "+PREP_COL+"asian_handicap_home_min_575"
    query += " , "+PREP_COL+"asian_handicap_away_min_575"
    query += " , "+PREP_COL+"asian_handicap_home_min_55"
    query += " , "+PREP_COL+"asian_handicap_away_min_55"
    query += " , "+PREP_COL+"asian_handicap_home_min_525"
    query += " , "+PREP_COL+"asian_handicap_away_min_525"
    query += " , "+PREP_COL+"asian_handicap_home_min_5"
    query += " , "+PREP_COL+"asian_handicap_away_min_5"
    query += " , "+PREP_COL+"asian_handicap_home_min_475"
    query += " , "+PREP_COL+"asian_handicap_away_min_475"
    query += " , "+PREP_COL+"asian_handicap_home_min_45"
    query += " , "+PREP_COL+"asian_handicap_away_min_45"
    query += " , "+PREP_COL+"asian_handicap_home_min_425"
    query += " , "+PREP_COL+"asian_handicap_away_min_425"
    query += " , "+PREP_COL+"asian_handicap_home_min_4"
    query += " , "+PREP_COL+"asian_handicap_away_min_4"
    query += " , "+PREP_COL+"asian_handicap_home_min_375"
    query += " , "+PREP_COL+"asian_handicap_away_min_375"
    query += " , "+PREP_COL+"asian_handicap_home_min_35"
    query += " , "+PREP_COL+"asian_handicap_away_min_35"
    query += " , "+PREP_COL+"asian_handicap_home_min_325"
    query += " , "+PREP_COL+"asian_handicap_away_min_325"
    query += " , "+PREP_COL+"asian_handicap_home_min_3"
    query += " , "+PREP_COL+"asian_handicap_away_min_3"
    query += " , "+PREP_COL+"asian_handicap_home_min_275"
    query += " , "+PREP_COL+"asian_handicap_away_min_275"
    query += " , "+PREP_COL+"asian_handicap_home_min_25"
    query += " , "+PREP_COL+"asian_handicap_away_min_25"
    query += " , "+PREP_COL+"asian_handicap_home_min_225"
    query += " , "+PREP_COL+"asian_handicap_away_min_225"
    query += " , "+PREP_COL+"asian_handicap_home_min_2"
    query += " , "+PREP_COL+"asian_handicap_away_min_2"
    query += " , "+PREP_COL+"asian_handicap_home_min_175"
    query += " , "+PREP_COL+"asian_handicap_away_min_175"
    query += " , "+PREP_COL+"asian_handicap_home_min_15"
    query += " , "+PREP_COL+"asian_handicap_away_min_15"
    query += " , "+PREP_COL+"asian_handicap_home_min_125"
    query += " , "+PREP_COL+"asian_handicap_away_min_125"
    query += " , "+PREP_COL+"asian_handicap_home_min_1"
    query += " , "+PREP_COL+"asian_handicap_away_min_1"
    query += " , "+PREP_COL+"asian_handicap_home_min_075"
    query += " , "+PREP_COL+"asian_handicap_away_min_075"
    query += " , "+PREP_COL+"asian_handicap_home_min_05"
    query += " , "+PREP_COL+"asian_handicap_away_min_05"
    query += " , "+PREP_COL+"asian_handicap_home_min_025"
    query += " , "+PREP_COL+"asian_handicap_away_min_025"
    query += " , "+PREP_COL+"asian_handicap_home_plus_0"
    query += " , "+PREP_COL+"asian_handicap_away_plus_0"
    query += " , "+PREP_COL+"asian_handicap_home_plus_025"
    query += " , "+PREP_COL+"asian_handicap_away_plus_025"
    query += " , "+PREP_COL+"asian_handicap_home_plus_05"
    query += " , "+PREP_COL+"asian_handicap_away_plus_05"
    query += " , "+PREP_COL+"asian_handicap_home_plus_075"
    query += " , "+PREP_COL+"asian_handicap_away_plus_075"
    query += " , "+PREP_COL+"asian_handicap_home_plus_1"
    query += " , "+PREP_COL+"asian_handicap_away_plus_1"
    query += " , "+PREP_COL+"asian_handicap_home_plus_125"
    query += " , "+PREP_COL+"asian_handicap_away_plus_125"
    query += " , "+PREP_COL+"asian_handicap_home_plus_15"
    query += " , "+PREP_COL+"asian_handicap_away_plus_15"
    query += " , "+PREP_COL+"asian_handicap_home_plus_175"
    query += " , "+PREP_COL+"asian_handicap_away_plus_175"
    query += " , "+PREP_COL+"asian_handicap_home_plus_2"
    query += " , "+PREP_COL+"asian_handicap_away_plus_2"
    query += " , "+PREP_COL+"asian_handicap_home_plus_225"
    query += " , "+PREP_COL+"asian_handicap_away_plus_225"
    query += " , "+PREP_COL+"asian_handicap_home_plus_25"
    query += " , "+PREP_COL+"asian_handicap_away_plus_25"
    query += " , "+PREP_COL+"asian_handicap_home_plus_275"
    query += " , "+PREP_COL+"asian_handicap_away_plus_275"
    query += " , "+PREP_COL+"asian_handicap_home_plus_3"
    query += " , "+PREP_COL+"asian_handicap_away_plus_3"
    query += " , "+PREP_COL+"asian_handicap_home_plus_325"
    query += " , "+PREP_COL+"asian_handicap_away_plus_325"
    query += " , "+PREP_COL+"asian_handicap_home_plus_35"
    query += " , "+PREP_COL+"asian_handicap_away_plus_35"
    query += " , "+PREP_COL+"asian_handicap_home_plus_375"
    query += " , "+PREP_COL+"asian_handicap_away_plus_375"
    query += " , "+PREP_COL+"asian_handicap_home_plus_4"
    query += " , "+PREP_COL+"asian_handicap_away_plus_4"
    query += " , "+PREP_COL+"asian_handicap_home_plus_425"
    query += " , "+PREP_COL+"asian_handicap_away_plus_425"
    query += " , "+PREP_COL+"asian_handicap_home_plus_45"
    query += " , "+PREP_COL+"asian_handicap_away_plus_45"
    query += " , "+PREP_COL+"asian_handicap_home_plus_475"
    query += " , "+PREP_COL+"asian_handicap_away_plus_475"
    query += " , "+PREP_COL+"asian_handicap_home_plus_5"
    query += " , "+PREP_COL+"asian_handicap_away_plus_5"
    query += " , "+PREP_COL+"asian_handicap_home_plus_525"
    query += " , "+PREP_COL+"asian_handicap_away_plus_525"
    query += " , "+PREP_COL+"asian_handicap_home_plus_55"
    query += " , "+PREP_COL+"asian_handicap_away_plus_55"
    query += " , "+PREP_COL+"asian_handicap_home_plus_575"
    query += " , "+PREP_COL+"asian_handicap_away_plus_575"
    query += " , "+PREP_COL+"asian_handicap_home_plus_6"
    query += " , "+PREP_COL+"asian_handicap_away_plus_6"
    query += " , "+PREP_COL+"asian_handicap_home_plus_625"
    query += " , "+PREP_COL+"asian_handicap_away_plus_625"
    query += " , "+PREP_COL+"asian_handicap_home_plus_65"
    query += " , "+PREP_COL+"asian_handicap_away_plus_65"
    query += " , "+PREP_COL+"asian_handicap_home_plus_675"
    query += " , "+PREP_COL+"asian_handicap_away_plus_675" 
    query += " , "+PREP_COL+"goals_overunder_over_05"
    query += " , "+PREP_COL+"goals_overunder_under_05"
    query += " , "+PREP_COL+"goals_overunder_over_075"
    query += " , "+PREP_COL+"goals_overunder_under_075"
    query += " , "+PREP_COL+"goals_overunder_over_10"
    query += " , "+PREP_COL+"goals_overunder_under_10"
    query += " , "+PREP_COL+"goals_overunder_over_125"
    query += " , "+PREP_COL+"goals_overunder_under_125"
    query += " , "+PREP_COL+"goals_overunder_over_15"
    query += " , "+PREP_COL+"goals_overunder_under_15"
    query += " , "+PREP_COL+"goals_overunder_over_175"
    query += " , "+PREP_COL+"goals_overunder_under_175"
    query += " , "+PREP_COL+"goals_overunder_over_20"
    query += " , "+PREP_COL+"goals_overunder_under_20"
    query += " , "+PREP_COL+"goals_overunder_over_225"
    query += " , "+PREP_COL+"goals_overunder_under_225"
    query += " , "+PREP_COL+"goals_overunder_over_25"
    query += " , "+PREP_COL+"goals_overunder_under_25"
    query += " , "+PREP_COL+"goals_overunder_over_275"
    query += " , "+PREP_COL+"goals_overunder_under_275"
    query += " , "+PREP_COL+"goals_overunder_over_30"
    query += " , "+PREP_COL+"goals_overunder_under_30"
    query += " , "+PREP_COL+"goals_overunder_over_325"
    query += " , "+PREP_COL+"goals_overunder_under_325"
    query += " , "+PREP_COL+"goals_overunder_over_35"
    query += " , "+PREP_COL+"goals_overunder_under_35"
    query += " , "+PREP_COL+"goals_overunder_over_375"
    query += " , "+PREP_COL+"goals_overunder_under_375"
    query += " , "+PREP_COL+"goals_overunder_over_40"
    query += " , "+PREP_COL+"goals_overunder_under_40"
    query += " , "+PREP_COL+"goals_overunder_over_425"
    query += " , "+PREP_COL+"goals_overunder_under_425"
    query += " , "+PREP_COL+"goals_overunder_over_45"
    query += " , "+PREP_COL+"goals_overunder_under_45"
    query += " , "+PREP_COL+"goals_overunder_over_475"
    query += " , "+PREP_COL+"goals_overunder_under_475"
    query += " , "+PREP_COL+"goals_overunder_over_50"
    query += " , "+PREP_COL+"goals_overunder_under_50"
    query += " , "+PREP_COL+"goals_overunder_over_525"
    query += " , "+PREP_COL+"goals_overunder_under_525"
    query += " , "+PREP_COL+"goals_overunder_over_55"
    query += " , "+PREP_COL+"goals_overunder_under_55"
    query += " , "+PREP_COL+"goals_overunder_over_575"
    query += " , "+PREP_COL+"goals_overunder_under_575"
    query += " , "+PREP_COL+"goals_overunder_over_60"
    query += " , "+PREP_COL+"goals_overunder_under_60"
    query += " , "+PREP_COL+"goals_overunder_over_625"
    query += " , "+PREP_COL+"goals_overunder_under_625"
    query += " , "+PREP_COL+"goals_overunder_over_65"
    query += " , "+PREP_COL+"goals_overunder_under_65"
    query += " , "+PREP_COL+"goals_overunder_over_675"
    query += " , "+PREP_COL+"goals_overunder_under_675"
    query += " , "+PREP_COL+"goals_overunder_over_70"
    query += " , "+PREP_COL+"goals_overunder_under_70"
    query += " , "+PREP_COL+"goals_overunder_over_75"
    query += " , "+PREP_COL+"goals_overunder_under_75"
    query += " , "+PREP_COL+"goals_overunder_over_85"
    query += " , "+PREP_COL+"goals_overunder_under_85"
    query += " , "+PREP_COL+"goals_overunder_over_95"
    query += " , "+PREP_COL+"goals_overunder_under_95" 
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_175"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_175"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_15"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_15"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_125"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_125"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_1"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_1"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_075"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_075"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_05"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_05"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_min_025"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_min_025"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_0"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_0"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_025"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_025"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_05"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_05"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_075"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_075"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_1"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_1"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_125"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_125"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_15"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_15"
    query += " , "+PREP_COL+"asian_handicap_first_half_home_plus_175"
    query += " , "+PREP_COL+"asian_handicap_first_half_away_plus_175" 
    query += " , "+PREP_COL+"goals_overunder_first_half_over_05"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_05"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_075"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_075"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_10"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_10"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_125"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_125"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_15"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_15"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_175"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_175"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_20"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_20"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_225"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_225"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_25"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_25"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_275"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_275"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_30"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_30"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_325"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_325"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_35"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_35"
    query += " , "+PREP_COL+"goals_overunder_first_half_over_375"
    query += " , "+PREP_COL+"goals_overunder_first_half_under_375" 
    query += " , "+PREP_COL+"goals_overunder__second_half_over_05"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_05"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_075"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_075"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_10"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_10"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_125"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_125"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_15"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_15"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_175"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_175"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_20"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_20"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_225"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_225"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_25"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_25"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_275"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_275"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_30"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_30"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_325"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_325"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_35"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_35"
    query += " , "+PREP_COL+"goals_overunder__second_half_over_375"
    query += " , "+PREP_COL+"goals_overunder__second_half_under_375" 

    query += " from football_fixturesx " 
    if(ROUTES == 'one'):
        query += " where one = 1 " 
    elif(ROUTES == 'fixture'):
        query += " where date >= '"+str(day0)+"' " 
        query += " and date <= '"+str(day1)+"' " 
        query += " and fixture_status like 'Not Started' " 
    elif(ROUTES == 'research_pre'):
        query += " where leagueapi_id = '"+str(day0)+"' " 
        query += " and season = '"+str(day1)+"' " 
        query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') " 
    elif(ROUTES == 'research_end'):
        query += " where leagueapi_id = '"+str(day0)+"' " 
        query += " and season = '"+str(day1)+"' " 
        query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') " 
    elif(ROUTES == 'preleague'):
        query += " where leagueapi_id = '"+str(day0)+"' " 
        query += " and season = '"+str(day1)+"' " 
        query += " and fixture_status like 'Not Started' " 


    query += " and deleted_at is null "   
    query += " order by date asc  "   
    # ----------------------------------------------------------   
    # print(space + query)
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
        teams_home_id   = str(x[0]) 
        teams_away_id   = str(x[1]) 
        # ------------------------------------------------------
        leagueapi_id    = str(x[2])  
        season          = str(x[3])  
        # ------------------------------------------------------
        fixtureapi_id   = str(x[4])  
        # ------------------------------------------------------
        teams_home      = str(x[5])  
        teams_away      = str(x[6])  
        date            = str(x[7]) 
        # ------------------------------------------------------
        count_col = 7
        # ------------------------------------------------------
        count_col += 1
        pre_both_teams_score_yes        = x[count_col] 
        count_col += 1
        pre_both_teams_score_no         = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_rcard_yes = x[count_col]
        count_col += 1
        pre_rcard_no = x[count_col] 
        # ------------------------------------------------------
        count_col += 1
        pre_first_half_winner_home = x[count_col]
        count_col += 1
        pre_first_half_winner_draw = x[count_col]
        count_col += 1
        pre_first_half_winner_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_second_half_winner_home = x[count_col]
        count_col += 1
        pre_second_half_winner_draw = x[count_col]
        count_col += 1
        pre_second_half_winner_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_htft_double_home_home = x[count_col]
        count_col += 1
        pre_htft_double_home_draw = x[count_col]
        count_col += 1
        pre_htft_double_home_away = x[count_col] 

        count_col += 1
        pre_htft_double_draw_home = x[count_col]
        count_col += 1
        pre_htft_double_draw_draw = x[count_col]
        count_col += 1
        pre_htft_double_draw_away = x[count_col]
        
        count_col += 1
        pre_htft_double_away_home = x[count_col]
        count_col += 1
        pre_htft_double_away_draw = x[count_col]
        count_col += 1
        pre_htft_double_away_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_both_teams_score__first_half_yes        = x[count_col] 
        count_col += 1
        pre_both_teams_score__first_half_no         = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_both_teams_to_score__second_half_yes        = x[count_col] 
        count_col += 1
        pre_both_teams_to_score__second_half_no         = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_results_both_teams_score_home_yes = x[count_col]
        count_col += 1
        pre_results_both_teams_score_draw_yes = x[count_col]
        count_col += 1
        pre_results_both_teams_score_away_yes = x[count_col]
        
        count_col += 1
        pre_results_both_teams_score_home_no = x[count_col]
        count_col += 1
        pre_results_both_teams_score_draw_no = x[count_col]
        count_col += 1
        pre_results_both_teams_score_away_no = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_to_score_in_both_halves_by_teams_home = x[count_col]

        count_col += 1
        pre_to_score_in_both_halves_by_teams_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_total_goals_both_teams_to_score_over_yes_25 = x[count_col]

        count_col += 1
        pre_total_goals_both_teams_to_score_over_no_25 = x[count_col]

        count_col += 1
        pre_total_goals_both_teams_to_score_under_yes_25 = x[count_col]

        count_col += 1
        pre_total_goals_both_teams_to_score_under_no_25 = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_both_teams_to_score_1st_half__2nd_half_yes_yes = x[count_col]

        count_col += 1
        pre_both_teams_to_score_1st_half__2nd_half_yes_no = x[count_col]

        count_col += 1
        pre_both_teams_to_score_1st_half__2nd_half_no_yes = x[count_col]

        count_col += 1
        pre_both_teams_to_score_1st_half__2nd_half_no_no = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_highest_scoring_half_first = x[count_col]

        count_col += 1
        pre_highest_scoring_half_draw = x[count_col]

        count_col += 1
        pre_highest_scoring_half_second = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_double_chance_home_draw = x[count_col]

        count_col += 1
        pre_double_chance_home_away = x[count_col]

        count_col += 1
        pre_double_chance_draw_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_double_chance__first_half_home_draw = x[count_col]

        count_col += 1
        pre_double_chance__first_half_home_away = x[count_col]

        count_col += 1
        pre_double_chance__first_half_draw_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_oddeven_odd = x[count_col]

        count_col += 1
        pre_oddeven_even = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_result_total_goals_home_over_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_draw_over_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_away_over_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_home_under_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_draw_under_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_away_under_35 = x[count_col]

        count_col += 1
        pre_result_total_goals_home_over_25 = x[count_col]

        count_col += 1
        pre_result_total_goals_draw_over_25 = x[count_col]

        count_col += 1
        pre_result_total_goals_away_over_25 = x[count_col]

        count_col += 1
        pre_result_total_goals_home_under_25 = x[count_col]

        count_col += 1
        pre_result_total_goals_draw_under_25 = x[count_col]

        count_col += 1
        pre_result_total_goals_away_under_25 = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_clean_sheet__home_yes = x[count_col]

        count_col += 1
        pre_clean_sheet__home_no = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_clean_sheet__away_yes = x[count_col]

        count_col += 1
        pre_clean_sheet__away_no = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_win_both_halves_home = x[count_col]

        count_col += 1
        pre_win_both_halves_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_win_to_nil_home = x[count_col]

        count_col += 1
        pre_win_to_nil_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_to_win_either_half_home = x[count_col]

        count_col += 1
        pre_to_win_either_half_away = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_halftime_result_both_teams_score_home_yes = x[count_col]

        count_col += 1
        pre_halftime_result_both_teams_score_draw_yes = x[count_col]

        count_col += 1
        pre_halftime_result_both_teams_score_away_yes = x[count_col]

        count_col += 1
        pre_halftime_result_both_teams_score_home_no = x[count_col]

        count_col += 1
        pre_halftime_result_both_teams_score_draw_no = x[count_col]

        count_col += 1
        pre_halftime_result_both_teams_score_away_no = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_exact_goals_number__first_half_0 = x[count_col]

        count_col += 1
        pre_exact_goals_number__first_half_1 = x[count_col]

        count_col += 1
        pre_exact_goals_number__first_half_2 = x[count_col]

        count_col += 1
        pre_exact_goals_number__first_half_3 = x[count_col]

        count_col += 1
        pre_exact_goals_number__first_half_4 = x[count_col]

        count_col += 1
        pre_exact_goals_number__first_half_more_5 = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_second_half_exact_goals_number_0 = x[count_col]

        count_col += 1
        pre_second_half_exact_goals_number_1 = x[count_col]

        count_col += 1
        pre_second_half_exact_goals_number_2 = x[count_col]

        count_col += 1
        pre_second_half_exact_goals_number_3 = x[count_col]

        count_col += 1
        pre_second_half_exact_goals_number_4 = x[count_col]

        count_col += 1
        pre_second_half_exact_goals_number_more_5 = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_home_team_exact_goals_number_0 = x[count_col]

        count_col += 1
        pre_home_team_exact_goals_number_1 = x[count_col]

        count_col += 1
        pre_home_team_exact_goals_number_2 = x[count_col]

        count_col += 1
        pre_home_team_exact_goals_number_more_3 = x[count_col]
        # ------------------------------------------------------
        count_col += 1
        pre_away_team_exact_goals_number_0 = x[count_col]

        count_col += 1
        pre_away_team_exact_goals_number_1 = x[count_col]

        count_col += 1
        pre_away_team_exact_goals_number_2 = x[count_col]

        count_col += 1
        pre_away_team_exact_goals_number_more_3 = x[count_col]
        # ------------------------------------------------------ 
        count_col += 1
        pre_asian_handicap_home_min_675 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_675 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_65 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_65 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_625 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_625 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_6 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_6 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_575 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_575 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_55 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_55 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_525 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_525 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_5 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_5 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_475 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_475 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_45 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_45 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_425 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_425 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_4 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_4 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_375 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_375 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_35 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_35 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_325 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_325 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_3 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_3 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_275 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_275 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_25 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_25 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_225 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_225 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_2 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_2 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_min_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_min_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_0 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_0 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_2 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_2 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_225 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_225 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_25 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_25 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_275 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_275 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_3 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_3 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_325 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_325 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_35 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_35 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_375 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_375 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_4 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_4 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_425 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_425 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_45 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_45 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_475 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_475 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_5 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_5 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_525 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_525 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_55 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_55 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_575 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_575 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_6 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_6 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_625 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_625 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_65 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_65 = x[count_col]
        count_col += 1
        pre_asian_handicap_home_plus_675 = x[count_col]
        count_col += 1
        pre_asian_handicap_away_plus_675 = x[count_col] 
        count_col += 1
        pre_goals_overunder_over_05 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_05 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_075 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_075 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_10 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_10 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_125 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_125 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_15 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_15 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_175 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_175 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_20 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_20 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_225 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_225 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_25 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_25 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_275 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_275 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_30 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_30 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_325 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_325 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_35 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_35 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_375 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_375 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_40 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_40 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_425 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_425 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_45 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_45 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_475 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_475 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_50 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_50 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_525 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_525 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_55 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_55 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_575 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_575 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_60 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_60 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_625 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_625 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_65 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_65 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_675 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_675 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_70 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_70 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_75 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_75 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_85 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_85 = x[count_col]
        count_col += 1
        pre_goals_overunder_over_95 = x[count_col]
        count_col += 1
        pre_goals_overunder_under_95 = x[count_col] 
        count_col += 1
        pre_asian_handicap_first_half_home_min_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_min_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_min_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_0 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_0 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_025 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_05 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_075 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_1 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_125 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_15 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_home_plus_175 = x[count_col]
        count_col += 1
        pre_asian_handicap_first_half_away_plus_175 = x[count_col] 
        count_col += 1
        pre_goals_overunder_first_half_over_05 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_05 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_075 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_075 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_10 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_10 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_125 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_125 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_15 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_15 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_175 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_175 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_20 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_20 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_225 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_225 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_25 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_25 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_275 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_275 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_30 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_30 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_325 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_325 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_35 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_35 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_over_375 = x[count_col]
        count_col += 1
        pre_goals_overunder_first_half_under_375 = x[count_col] 
        count_col += 1
        pre_goals_overunder__second_half_over_05 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_05 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_075 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_075 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_10 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_10 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_125 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_125 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_15 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_15 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_175 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_175 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_20 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_20 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_225 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_225 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_25 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_25 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_275 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_275 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_30 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_30 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_325 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_325 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_35 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_35 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_over_375 = x[count_col]
        count_col += 1
        pre_goals_overunder__second_half_under_375 = x[count_col] 

        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
        word += " - " + season
        word += " -----#" + teams_home + " " + teams_home_id 
        word += " - " + teams_away + " "+ teams_away_id
        word += " - " + date
        print(word, flush=True)   
        # ------------------------------------------------------ 
        good_to_go = 0
        isi = ''
        # ------------------------------------------------------  
        route = "http://localhost/pr_laravel_8_buzz_2022_12/Oddsreader/status/"

        # ------------------------------------------------------ 
        if(pre_first_half_winner_home is not None and pre_first_half_winner_home <= 2):
            print(space + "__" + "pre_first_half_winner_home:" + str(pre_first_half_winner_home), flush=True)
            good_to_go = 1
 
            isi += '<a href="'+route+'1stHwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'

            if(pre_first_half_winner_home == 1.95): 
                isi += '<h6>'

            isi += ' 1stHwin '+ str(pre_first_half_winner_home)

            if(pre_first_half_winner_home == 1.95): 
                isi += '</h6>'

            isi += ' </a> '

        if(pre_first_half_winner_draw is not None and pre_first_half_winner_draw <= 2):
            print(space + "__" + "pre_first_half_winner_draw:" + str(pre_first_half_winner_draw), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'1stXdraw" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'

            if(pre_first_half_winner_draw == 1.95): 
                isi += '<h6>'

            isi += ' 1stXdraw '+ str(pre_first_half_winner_draw)

            if(pre_first_half_winner_draw == 1.95): 
                isi += '</h6>'

            isi += ' </a> '
        if(pre_first_half_winner_away is not None and pre_first_half_winner_away <= 2):
            print(space + "__" + "pre_first_half_winner_away:" + str(pre_first_half_winner_away), flush=True)
            good_to_go = 1

            isi += '<a href="'+route+'1stAwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'

            if(pre_first_half_winner_away == 1.95): 
                isi += '<h6>'

            isi += ' 1stAwin '+ str(pre_first_half_winner_away)

            if(pre_first_half_winner_away == 1.95): 
                isi += '</h6>'

            isi += ' </a> ' 
        # ------------------------------------------------------ 
        if(pre_second_half_winner_home is not None and pre_second_half_winner_home <= 2):
            print(space + "__" + "pre_second_half_winner_home:" + str(pre_second_half_winner_home), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'2ndHwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' 2ndHwin '+ str(pre_second_half_winner_home)
            isi += ' </a> '
        if(pre_second_half_winner_draw is not None and pre_second_half_winner_draw <= 2):
            print(space + "__" + "pre_second_half_winner_draw:" + str(pre_second_half_winner_draw), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'2ndXdraw" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' 2ndXdraw '+ str(pre_second_half_winner_draw)
            isi += ' </a> '
        if(pre_second_half_winner_away is not None and pre_second_half_winner_away <= 2):
            print(space + "__" + "pre_second_half_winner_away:" + str(pre_second_half_winner_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'2ndAwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' 2ndAwin '+ str(pre_second_half_winner_away)
            isi += ' </a> ' 
        # ------------------------------------------------------  
        if(pre_total_goals_both_teams_to_score_over_yes_25 is not None and pre_total_goals_both_teams_to_score_over_yes_25 <= 2):
            print(space + "__" + "pre_total_goals_both_teams_to_score_over_yes_25:" + str(pre_total_goals_both_teams_to_score_over_yes_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'Bty-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-success me-1 mt-2">'

            if(pre_total_goals_both_teams_to_score_over_yes_25 <= 1.8): 
                isi += '<h6>'

            isi += ' Bty-o25 '+ str(pre_total_goals_both_teams_to_score_over_yes_25)

            if(pre_total_goals_both_teams_to_score_over_yes_25 <= 1.8): 
                isi += '</h6>'

            isi += ' </a> '

            #---------------------------------------------------------------------- Based on Research 
            if(pre_total_goals_both_teams_to_score_over_yes_25 < 1.5):  
                isi += '<a href="'+route+'o25" '
                isi += ' target="_blank" '
                isi += ' class="badge badge  bg-gradient-success me-1 mt-2">'
                isi += '<h6>'
                isi += ' >>>>>o25<<<<< ' 
                isi += '</h6>'
                isi += ' </a> '
            elif(pre_total_goals_both_teams_to_score_over_yes_25 < 1.5):  
                isi += '<a href="'+route+'o25" '
                isi += ' target="_blank" '
                isi += ' class="badge badge  bg-gradient-success me-1 mt-2">'
                isi += '<h6>'
                isi += ' >>>>>o25<<<<< ' 
                isi += '</h6>'
                isi += ' </a> '

        if(pre_total_goals_both_teams_to_score_over_no_25 is not None and pre_total_goals_both_teams_to_score_over_no_25 <= 2):
            print(space + "__" + "pre_total_goals_both_teams_to_score_over_no_25:" + str(pre_total_goals_both_teams_to_score_over_no_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'Btn-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-success me-1 mt-2">'
            isi += ' Btn-o25 '+ str(pre_total_goals_both_teams_to_score_over_no_25)
            isi += ' </a> '

        if(pre_total_goals_both_teams_to_score_under_yes_25 is not None and pre_total_goals_both_teams_to_score_under_yes_25 <= 2):
            print(space + "__" + "pre_total_goals_both_teams_to_score_under_yes_25:" + str(pre_total_goals_both_teams_to_score_under_yes_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'Bty-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-danger me-1 mt-2">'
            isi += ' Bty-u25 '+ str(pre_total_goals_both_teams_to_score_under_yes_25)
            isi += ' </a> '

        if(pre_total_goals_both_teams_to_score_under_no_25 is not None and pre_total_goals_both_teams_to_score_under_no_25 <= 2):
            print(space + "__" + "pre_total_goals_both_teams_to_score_under_no_25:" + str(pre_total_goals_both_teams_to_score_under_no_25), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'Btn-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-danger me-1 mt-2">'

            if(pre_total_goals_both_teams_to_score_under_no_25 <= 1.83): 
                isi += '<h6>'

            isi += ' Btn-u25 '+ str(pre_total_goals_both_teams_to_score_under_no_25)

            if(pre_total_goals_both_teams_to_score_under_no_25 <= 1.83): 
                isi += '</h6>'

            isi += ' </a> '
        # ------------------------------------------------------ 
        if(pre_to_win_either_half_home is not None and pre_to_win_either_half_home < 1.3):
            print(space + "__" + "pre_to_win_either_half_home:" + str(pre_to_win_either_half_home), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-eithr '+ str(pre_to_win_either_half_home)
            isi += ' </a> '
        if(pre_to_win_either_half_away is not None and pre_to_win_either_half_away < 1.3):
            print(space + "__" + "pre_to_win_either_half_away:" + str(pre_to_win_either_half_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'A-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-eithr '+ str(pre_to_win_either_half_away)
            isi += ' </a> '
        # ------------------------------------------------------      
        if(pre_win_both_halves_home is not None and pre_win_both_halves_home <= 2):
            print(space + "__" + "pre_win_both_halves_home:" + str(pre_win_both_halves_home), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-both" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-both '+ str(pre_win_both_halves_home)
            isi += ' </a> '

        if(pre_win_both_halves_away is not None and pre_win_both_halves_away <= 2):
            print(space + "__" + "pre_win_both_halves_away:" + str(pre_win_both_halves_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'A-both" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-both '+ str(pre_win_both_halves_away)
            isi += ' </a> '
        # ------------------------------------------------------ 
        if(pre_win_to_nil_home is not None and pre_win_to_nil_home <= 2):
            print(space + "__" + "pre_win_to_nil_home:" + str(pre_win_to_nil_home), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-nil" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-nil '+ str(pre_win_to_nil_home)
            isi += ' </a> '

            
            if(pre_win_to_nil_home == 1.91): 
                isi += '<a href="'+route+'Btn" '
                isi += ' target="_blank" '
                isi += ' class="badge badge  bg-gradient-custom-pink me-1 mt-2">'
                isi += '<h6>'
                isi += ' >>Btn<< ' 
                isi += '</h6>'
                isi += ' </a> '

        if(pre_win_to_nil_away is not None and pre_win_to_nil_away <= 2):
            print(space + "__" + "pre_win_to_nil_away:" + str(pre_win_to_nil_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'A-nil" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-nil '+ str(pre_win_to_nil_away)
            isi += ' </a> ' 

            
            if(pre_win_to_nil_away == 1.91): 
                isi += '<a href="'+route+'Btn" '
                isi += ' target="_blank" '
                isi += ' class="badge badge  bg-gradient-custom-pink me-1 mt-2">'
                isi += '<h6>'
                isi += ' >>Btn<< ' 
                isi += '</h6>'
                isi += ' </a> '
        # ------------------------------------------------------ 
        if(pre_result_total_goals_home_over_35 is not None and pre_result_total_goals_home_over_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_home_over_35:" + str(pre_result_total_goals_home_over_35), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-o35 '+ str(pre_result_total_goals_home_over_35)
            isi += ' </a> ' 

        if(pre_result_total_goals_draw_over_35 is not None and pre_result_total_goals_draw_over_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_draw_over_35:" + str(pre_result_total_goals_draw_over_35), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'X-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' X-o35 '+ str(pre_result_total_goals_draw_over_35)
            isi += ' </a> '  
        
        if(pre_result_total_goals_away_over_35 is not None and pre_result_total_goals_away_over_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_away_over_35:" + str(pre_result_total_goals_away_over_35), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'A-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-o35 '+ str(pre_result_total_goals_away_over_35)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_home_under_35 is not None and pre_result_total_goals_home_under_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_home_under_35:" + str(pre_result_total_goals_home_under_35), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-u35 '+ str(pre_result_total_goals_home_under_35)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_draw_under_35 is not None and pre_result_total_goals_draw_under_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_draw_under_35:" + str(pre_result_total_goals_draw_under_35), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'X-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' X-u35 '+ str(pre_result_total_goals_draw_under_35)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_away_under_35 is not None and pre_result_total_goals_away_under_35 <= 2.2):
            print(space + "__" + "pre_result_total_goals_away_under_35:" + str(pre_result_total_goals_away_under_35), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'A-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-u35 '+ str(pre_result_total_goals_away_under_35)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_home_over_25 is not None and pre_result_total_goals_home_over_25 <= 2.2): 
            print(space + "__" + "pre_result_total_goals_home_over_25:" + str(pre_result_total_goals_home_over_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'

            if(pre_result_total_goals_home_over_25 <= 1.83): 
                isi += '<h6>'

            isi += ' H-o25 '+ str(pre_result_total_goals_home_over_25)

            if(pre_result_total_goals_home_over_25 <= 1.83): 
                isi += '</h6>'

            isi += ' </a> ' 
        
        if(pre_result_total_goals_draw_over_25 is not None and pre_result_total_goals_draw_over_25 <= 2.2):
            print(space + "__" + "pre_result_total_goals_draw_over_25:" + str(pre_result_total_goals_draw_over_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'X-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' X-o25 '+ str(pre_result_total_goals_draw_over_25)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_away_over_25 is not None and pre_result_total_goals_away_over_25 <= 2.2):
            print(space + "__" + "pre_result_total_goals_away_over_25:" + str(pre_result_total_goals_away_over_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'A-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'

            if(pre_result_total_goals_away_over_25 <= 1.83): 
                isi += '<h6>'

            isi += ' A-o25 '+ str(pre_result_total_goals_away_over_25)

            if(pre_result_total_goals_away_over_25 <= 1.83): 
                isi += '</h6>'

            isi += ' </a> ' 
        
        if(pre_result_total_goals_home_under_25 is not None and pre_result_total_goals_home_under_25 <= 2.2): 
            print(space + "__" + "pre_result_total_goals_home_under_25:" + str(pre_result_total_goals_home_under_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-primary me-1 mt-2">'
            isi += ' H-u25 '+ str(pre_result_total_goals_home_under_25)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_draw_under_25 is not None and pre_result_total_goals_draw_under_25 <= 2.2):
            print(space + "__" + "pre_result_total_goals_draw_under_25:" + str(pre_result_total_goals_draw_under_25), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'X-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' X-u25 '+ str(pre_result_total_goals_draw_under_25)
            isi += ' </a> ' 
        
        if(pre_result_total_goals_away_under_25 is not None and pre_result_total_goals_away_under_25 <= 2.2):
            print(space + "__" + "pre_result_total_goals_away_under_25:" + str(pre_result_total_goals_away_under_25), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'A-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-warning me-1 mt-2">'
            isi += ' A-u25 '+ str(pre_result_total_goals_away_under_25)
            isi += ' </a> ' 
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        # ------------------------------------------------------  
        
        # ------------------------------------------------------ BTTS
        if(pre_both_teams_score_yes is not None and pre_both_teams_score_yes >= 2.5):
            print(space + "__" + "pre_both_teams_score_yes:" + str(pre_both_teams_score_yes), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'Bty" '
            isi += ' target="_blank" '
            isi += ' class="badge badge bg-gradient-dark me-1 mt-2">'
            isi += ' Bty '+ str(pre_both_teams_score_yes)
            isi += ' </a> '  

        if(pre_both_teams_score_no is not None and pre_both_teams_score_no >= 2.5):
            print(space + "__" + "pre_both_teams_score_no:" + str(pre_both_teams_score_no), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'Btn" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' Btn '+ str(pre_both_teams_score_no)
            isi += ' </a> '
        # ------------------------------------------------------  
        if(pre_double_chance_home_draw is not None and pre_double_chance_home_draw >= 3):
            print(space + "__" + "pre_double_chance_home_draw:" + str(pre_double_chance_home_draw), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'1x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' 1x '+ str(pre_double_chance_home_draw)
            isi += ' </a> '

        if(pre_double_chance_home_away is not None and pre_double_chance_home_away >= 3):
            print(space + "__" + "pre_double_chance_home_away:" + str(pre_double_chance_home_away), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'12" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' 12 '+ str(pre_double_chance_home_away)
            isi += ' </a> '

        if(pre_double_chance_draw_away is not None and pre_double_chance_draw_away >= 3):
            print(space + "__" + "pre_double_chance_draw_away:" + str(pre_double_chance_draw_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'2x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' 2x '+ str(pre_double_chance_draw_away)
            isi += ' </a> '
        # ------------------------------------------------------  
        if(pre_clean_sheet__away_yes is not None and pre_clean_sheet__away_yes >= 7):
            print(space + "__" + "pre_clean_sheet__away_yes:" + str(pre_clean_sheet__away_yes), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'CSy-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' CSy-A '+ str(pre_clean_sheet__away_yes)
            isi += ' </a> '

        if(pre_clean_sheet__home_yes is not None and pre_clean_sheet__home_yes >= 7):
            print(space + "__" + "pre_clean_sheet__home_yes:" + str(pre_clean_sheet__home_yes), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'CSy-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' CSy-H '+ str(pre_clean_sheet__home_yes)
            isi += ' </a> '
        # ------------------------------------------------------ 

        if(pre_to_win_either_half_home is not None and pre_to_win_either_half_home >= 4):
            print(space + "__" + "pre_to_win_either_half_home:" + str(pre_to_win_either_half_home), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'H-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' H-eithr '+ str(pre_to_win_either_half_home)
            isi += ' </a> '

        if(pre_to_win_either_half_away is not None and pre_to_win_either_half_away >= 4):
            print(space + "__" + "pre_to_win_either_half_away:" + str(pre_to_win_either_half_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'A-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' A-eithr '+ str(pre_to_win_either_half_away)
            isi += ' </a> '

            
        # ------------------------------------------------------      
        if(pre_win_both_halves_home is not None and pre_win_both_halves_home >= 101):
            print(space + "__" + "pre_win_both_halves_home:" + str(pre_win_both_halves_home), flush=True) 
            good_to_go = 1
            isi += '<a href="'+route+'CSn-A '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' <h6> '
            isi += ' >>CSn-A<< '+ str(pre_clean_sheet__away_no ) + ' / ' + str(pre_win_both_halves_home )
            isi += ' </h6> '
            isi += ' </a> '

        if(pre_win_both_halves_away is not None and pre_win_both_halves_away >= 101):
            print(space + "__" + "pre_win_both_halves_away:" + str(pre_win_both_halves_away), flush=True)
            good_to_go = 1
            isi += '<a href="'+route+'CSn-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-dark me-1 mt-2">'
            isi += ' <h6> '
            isi += ' >>CSn-H<< '+ str(pre_clean_sheet__home_no ) + ' / ' + str(pre_win_both_halves_away )
            isi += ' </h6> '
            isi += ' </a> '
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # if(ROUTES == 'one'):
        #     PREP_COL = "end_" 
        # elif(ROUTES == 'fixture'):
        #     PREP_COL = "pre_" 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_htft_double_home_home:" + str(pre_htft_double_home_home), flush=True)
        # print(space + "__" + "pre_htft_double_home_draw:" + str(pre_htft_double_home_draw), flush=True)
        # print(space + "__" + "pre_htft_double_home_away:" + str(pre_htft_double_home_away), flush=True)
        # print("")
        # print(space + "__" + "pre_htft_double_draw_home:" + str(pre_htft_double_draw_home), flush=True)
        # print(space + "__" + "pre_htft_double_draw_draw:" + str(pre_htft_double_draw_draw), flush=True)
        # print(space + "__" + "pre_htft_double_draw_away:" + str(pre_htft_double_draw_away), flush=True)
        # print("")
        # print(space + "__" + "pre_htft_double_away_home:" + str(pre_htft_double_away_home), flush=True)
        # print(space + "__" + "pre_htft_double_away_draw:" + str(pre_htft_double_away_draw), flush=True)
        # print(space + "__" + "pre_htft_double_away_away:" + str(pre_htft_double_away_away), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_both_teams_score__first_half_yes:" + str(pre_both_teams_score__first_half_yes), flush=True)
        # print(space + "__" + "pre_both_teams_score__first_half_no:" + str(pre_both_teams_score__first_half_no), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_both_teams_to_score__second_half_yes:" + str(pre_both_teams_to_score__second_half_yes), flush=True)
        # print(space + "__" + "pre_both_teams_to_score__second_half_no:" + str(pre_both_teams_to_score__second_half_no), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_results_both_teams_score_home_yes:" + str(pre_results_both_teams_score_home_yes), flush=True)
        # print(space + "__" + "pre_results_both_teams_score_draw_yes:" + str(pre_results_both_teams_score_draw_yes), flush=True)
        # print(space + "__" + "pre_results_both_teams_score_away_yes:" + str(pre_results_both_teams_score_away_yes), flush=True)
        # print("")
        # print(space + "__" + "pre_results_both_teams_score_home_no:" + str(pre_results_both_teams_score_home_no), flush=True)
        # print(space + "__" + "pre_results_both_teams_score_draw_no:" + str(pre_results_both_teams_score_draw_no), flush=True)
        # print(space + "__" + "pre_results_both_teams_score_away_no:" + str(pre_results_both_teams_score_away_no), flush=True)
        # # ------------------------------------------------------  
        # print("")
        # print(space + "__" + "pre_to_score_in_both_halves_by_teams_home:" + str(pre_to_score_in_both_halves_by_teams_home), flush=True) 
        # print(space + "__" + "pre_to_score_in_both_halves_by_teams_away:" + str(pre_to_score_in_both_halves_by_teams_away), flush=True)
        # # ------------------------------------------------------ 
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_both_teams_to_score_1st_half__2nd_half_yes_yes:" + str(pre_both_teams_to_score_1st_half__2nd_half_yes_yes), flush=True) 
        # print(space + "__" + "pre_both_teams_to_score_1st_half__2nd_half_yes_no:" + str(pre_both_teams_to_score_1st_half__2nd_half_yes_no), flush=True) 
        # print(space + "__" + "pre_both_teams_to_score_1st_half__2nd_half_no_yes:" + str(pre_both_teams_to_score_1st_half__2nd_half_no_yes), flush=True) 
        # print(space + "__" + "pre_both_teams_to_score_1st_half__2nd_half_no_no:" + str(pre_both_teams_to_score_1st_half__2nd_half_no_no), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_highest_scoring_half_first:" + str(pre_highest_scoring_half_first), flush=True) 
        # print(space + "__" + "pre_highest_scoring_half_draw:" + str(pre_highest_scoring_half_draw), flush=True) 
        # print(space + "__" + "pre_highest_scoring_half_second:" + str(pre_highest_scoring_half_second), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_double_chance__first_half_home_draw:" + str(pre_double_chance__first_half_home_draw), flush=True) 
        # print(space + "__" + "pre_double_chance__first_half_home_away:" + str(pre_double_chance__first_half_home_away), flush=True) 
        # print(space + "__" + "pre_double_chance__first_half_draw_away:" + str(pre_double_chance__first_half_draw_away), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_oddeven_odd:" + str(pre_oddeven_odd), flush=True) 
        # print(space + "__" + "pre_oddeven_even:" + str(pre_oddeven_even), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_clean_sheet__home_yes:" + str(pre_clean_sheet__home_yes), flush=True) 
        # print(space + "__" + "pre_clean_sheet__home_no:" + str(pre_clean_sheet__home_no), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_halftime_result_both_teams_score_home_yes:" + str(pre_halftime_result_both_teams_score_home_yes), flush=True) 
        # print(space + "__" + "pre_halftime_result_both_teams_score_draw_yes:" + str(pre_halftime_result_both_teams_score_draw_yes), flush=True) 
        # print(space + "__" + "pre_halftime_result_both_teams_score_away_yes:" + str(pre_halftime_result_both_teams_score_away_yes), flush=True) 
        # print("")
        # print(space + "__" + "pre_halftime_result_both_teams_score_home_no:" + str(pre_halftime_result_both_teams_score_home_no), flush=True) 
        # print(space + "__" + "pre_halftime_result_both_teams_score_draw_no:" + str(pre_halftime_result_both_teams_score_draw_no), flush=True) 
        # print(space + "__" + "pre_halftime_result_both_teams_score_away_no:" + str(pre_halftime_result_both_teams_score_away_no), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_exact_goals_number__first_half_0:" + str(pre_exact_goals_number__first_half_0), flush=True) 
        # print(space + "__" + "pre_exact_goals_number__first_half_1:" + str(pre_exact_goals_number__first_half_1), flush=True) 
        # print(space + "__" + "pre_exact_goals_number__first_half_2:" + str(pre_exact_goals_number__first_half_2), flush=True) 
        # print(space + "__" + "pre_exact_goals_number__first_half_3:" + str(pre_exact_goals_number__first_half_3), flush=True) 
        # print(space + "__" + "pre_exact_goals_number__first_half_4:" + str(pre_exact_goals_number__first_half_4), flush=True) 
        # print(space + "__" + "pre_exact_goals_number__first_half_more_5:" + str(pre_exact_goals_number__first_half_more_5), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_second_half_exact_goals_number_0:" + str(pre_second_half_exact_goals_number_0), flush=True) 
        # print(space + "__" + "pre_second_half_exact_goals_number_1:" + str(pre_second_half_exact_goals_number_1), flush=True) 
        # print(space + "__" + "pre_second_half_exact_goals_number_2:" + str(pre_second_half_exact_goals_number_2), flush=True) 
        # print(space + "__" + "pre_second_half_exact_goals_number_3:" + str(pre_second_half_exact_goals_number_3), flush=True) 
        # print(space + "__" + "pre_second_half_exact_goals_number_4:" + str(pre_second_half_exact_goals_number_4), flush=True) 
        # print(space + "__" + "pre_second_half_exact_goals_number_more_5:" + str(pre_second_half_exact_goals_number_more_5), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_home_team_exact_goals_number_0:" + str(pre_home_team_exact_goals_number_0), flush=True) 
        # print(space + "__" + "pre_home_team_exact_goals_number_1:" + str(pre_home_team_exact_goals_number_1), flush=True) 
        # print(space + "__" + "pre_home_team_exact_goals_number_2:" + str(pre_home_team_exact_goals_number_2), flush=True) 
        # print(space + "__" + "pre_home_team_exact_goals_number_more_3:" + str(pre_home_team_exact_goals_number_more_3), flush=True)
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_away_team_exact_goals_number_0:" + str(pre_away_team_exact_goals_number_0), flush=True) 
        # print(space + "__" + "pre_away_team_exact_goals_number_1:" + str(pre_away_team_exact_goals_number_1), flush=True) 
        # print(space + "__" + "pre_away_team_exact_goals_number_2:" + str(pre_away_team_exact_goals_number_2), flush=True) 
        # print(space + "__" + "pre_away_team_exact_goals_number_more_3:" + str(pre_away_team_exact_goals_number_more_3), flush=True)
        # # ------------------------------------------------------
        # # ------------------------------------------------------ 
        # print("")
        # print(space + "__" + "pre_rcard_yes:" + str(pre_rcard_yes), flush=True) 
        # print(space + "__" + "pre_rcard_no:" + str(pre_rcard_no), flush=True) 

        good_to_go2 = 0
        isi += "<hr/>"

        # ---------------------------------------------------------------------------------------------- -6     
        if(pre_asian_handicap_home_min_675 is not None and pre_asian_handicap_home_min_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_65 is not None and pre_asian_handicap_home_min_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-65 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_625 is not None and pre_asian_handicap_home_min_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_6 is not None and pre_asian_handicap_home_min_6 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-6" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-6' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -5     
        if(pre_asian_handicap_home_min_575 is not None and pre_asian_handicap_home_min_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_55 is not None and pre_asian_handicap_home_min_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-55 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_525 is not None and pre_asian_handicap_home_min_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_5 is not None and pre_asian_handicap_home_min_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-5' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -4     
        if(pre_asian_handicap_home_min_475 is not None and pre_asian_handicap_home_min_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_45 is not None and pre_asian_handicap_home_min_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-45 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_425 is not None and pre_asian_handicap_home_min_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_4 is not None and pre_asian_handicap_home_min_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-4' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -3     
        if(pre_asian_handicap_home_min_375 is not None and pre_asian_handicap_home_min_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_35 is not None and pre_asian_handicap_home_min_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_325 is not None and pre_asian_handicap_home_min_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_3 is not None and pre_asian_handicap_home_min_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-3' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -2     
        if(pre_asian_handicap_home_min_275 is not None and pre_asian_handicap_home_min_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_25 is not None and pre_asian_handicap_home_min_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_225 is not None and pre_asian_handicap_home_min_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_2 is not None and pre_asian_handicap_home_min_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-2' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -1     
        if(pre_asian_handicap_home_min_175 is not None and pre_asian_handicap_home_min_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_15 is not None and pre_asian_handicap_home_min_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_125 is not None and pre_asian_handicap_home_min_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_1 is not None and pre_asian_handicap_home_min_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -0     
        if(pre_asian_handicap_home_min_075 is not None and pre_asian_handicap_home_min_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_05 is not None and pre_asian_handicap_home_min_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_min_025 is not None and pre_asian_handicap_home_min_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H-025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H-025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -6     
        if(pre_asian_handicap_away_min_675 is not None and pre_asian_handicap_away_min_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_65 is not None and pre_asian_handicap_away_min_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+65 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_625 is not None and pre_asian_handicap_away_min_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_6 is not None and pre_asian_handicap_away_min_6 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+6" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+6' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -5     
        if(pre_asian_handicap_away_min_575 is not None and pre_asian_handicap_away_min_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_55 is not None and pre_asian_handicap_away_min_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+55 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_525 is not None and pre_asian_handicap_away_min_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_5 is not None and pre_asian_handicap_away_min_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+5' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -4     
        if(pre_asian_handicap_away_min_475 is not None and pre_asian_handicap_away_min_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_45 is not None and pre_asian_handicap_away_min_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+45 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_425 is not None and pre_asian_handicap_away_min_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_4 is not None and pre_asian_handicap_away_min_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+4' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -3     
        if(pre_asian_handicap_away_min_375 is not None and pre_asian_handicap_away_min_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_35 is not None and pre_asian_handicap_away_min_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_325 is not None and pre_asian_handicap_away_min_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_3 is not None and pre_asian_handicap_away_min_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+3' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -2     
        if(pre_asian_handicap_away_min_275 is not None and pre_asian_handicap_away_min_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_25 is not None and pre_asian_handicap_away_min_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_225 is not None and pre_asian_handicap_away_min_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_2 is not None and pre_asian_handicap_away_min_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+2' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- -1     
        if(pre_asian_handicap_away_min_175 is not None and pre_asian_handicap_away_min_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_15 is not None and pre_asian_handicap_away_min_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_125 is not None and pre_asian_handicap_away_min_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_1 is not None and pre_asian_handicap_away_min_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -0     
        if(pre_asian_handicap_away_min_075 is not None and pre_asian_handicap_away_min_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_05 is not None and pre_asian_handicap_away_min_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_min_025 is not None and pre_asian_handicap_away_min_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A+025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A+025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -0 
        if(pre_asian_handicap_home_plus_0 is not None and pre_asian_handicap_home_plus_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+0' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_025 is not None and pre_asian_handicap_home_plus_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_05 is not None and pre_asian_handicap_home_plus_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+05 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_075 is not None and pre_asian_handicap_home_plus_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -1 
        if(pre_asian_handicap_home_plus_1 is not None and pre_asian_handicap_home_plus_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_125 is not None and pre_asian_handicap_home_plus_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_15 is not None and pre_asian_handicap_home_plus_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+15 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_175 is not None and pre_asian_handicap_home_plus_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -2 
        if(pre_asian_handicap_home_plus_2 is not None and pre_asian_handicap_home_plus_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+2' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_225 is not None and pre_asian_handicap_home_plus_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_25 is not None and pre_asian_handicap_home_plus_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+25 ' + ' 1.98'
            isi += ' </h6> '     
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_275 is not None and pre_asian_handicap_home_plus_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -3 
        if(pre_asian_handicap_home_plus_3 is not None and pre_asian_handicap_home_plus_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+3' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_325 is not None and pre_asian_handicap_home_plus_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_35 is not None and pre_asian_handicap_home_plus_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+35 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_375 is not None and pre_asian_handicap_home_plus_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -4 
        if(pre_asian_handicap_home_plus_4 is not None and pre_asian_handicap_home_plus_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+4' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_425 is not None and pre_asian_handicap_home_plus_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_45 is not None and pre_asian_handicap_home_plus_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+45 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_475 is not None and pre_asian_handicap_home_plus_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -5 
        if(pre_asian_handicap_home_plus_5 is not None and pre_asian_handicap_home_plus_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+5' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_525 is not None and pre_asian_handicap_home_plus_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_55 is not None and pre_asian_handicap_home_plus_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+55 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_575 is not None and pre_asian_handicap_home_plus_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -6 
        if(pre_asian_handicap_home_plus_6 is not None and pre_asian_handicap_home_plus_6 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+6" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+6' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_625 is not None and pre_asian_handicap_home_plus_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_home_plus_65 is not None and pre_asian_handicap_home_plus_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+65 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_home_plus_675 is not None and pre_asian_handicap_home_plus_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah H+675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah H+675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- -0 
        if(pre_asian_handicap_away_plus_0 is not None and pre_asian_handicap_away_plus_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-0' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_025 is not None and pre_asian_handicap_away_plus_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_05 is not None and pre_asian_handicap_away_plus_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-05 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_075 is not None and pre_asian_handicap_away_plus_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -1 
        if(pre_asian_handicap_away_plus_1 is not None and pre_asian_handicap_away_plus_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_125 is not None and pre_asian_handicap_away_plus_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_15 is not None and pre_asian_handicap_away_plus_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-15 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_175 is not None and pre_asian_handicap_away_plus_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -2 
        if(pre_asian_handicap_away_plus_2 is not None and pre_asian_handicap_away_plus_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-2' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_225 is not None and pre_asian_handicap_away_plus_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_25 is not None and pre_asian_handicap_away_plus_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-25 ' + ' 1.98'
            isi += ' </h6> '    
            isi += ' </a> '  
        if(pre_asian_handicap_away_plus_275 is not None and pre_asian_handicap_away_plus_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -3 
        if(pre_asian_handicap_away_plus_3 is not None and pre_asian_handicap_away_plus_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-3' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_325 is not None and pre_asian_handicap_away_plus_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_35 is not None and pre_asian_handicap_away_plus_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-35 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_375 is not None and pre_asian_handicap_away_plus_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -4 
        if(pre_asian_handicap_away_plus_4 is not None and pre_asian_handicap_away_plus_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-4' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_425 is not None and pre_asian_handicap_away_plus_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_45 is not None and pre_asian_handicap_away_plus_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-45 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_475 is not None and pre_asian_handicap_away_plus_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -5 
        if(pre_asian_handicap_away_plus_5 is not None and pre_asian_handicap_away_plus_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-5' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_525 is not None and pre_asian_handicap_away_plus_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_55 is not None and pre_asian_handicap_away_plus_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-55 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_575 is not None and pre_asian_handicap_away_plus_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- -6 
        if(pre_asian_handicap_away_plus_6 is not None and pre_asian_handicap_away_plus_6 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-6" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-6' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_625 is not None and pre_asian_handicap_away_plus_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_away_plus_65 is not None and pre_asian_handicap_away_plus_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-65 ' + ' 1.98'
            isi += ' </h6> '     
        if(pre_asian_handicap_away_plus_675 is not None and pre_asian_handicap_away_plus_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Ah A-675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Ah A-675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_over_05 is not None and pre_goals_overunder_over_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_075 is not None and pre_goals_overunder_over_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_over_10 is not None and pre_goals_overunder_over_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_125 is not None and pre_goals_overunder_over_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_15 is not None and pre_goals_overunder_over_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_175 is not None and pre_goals_overunder_over_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder_over_20 is not None and pre_goals_overunder_over_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_225 is not None and pre_goals_overunder_over_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_25 is not None and pre_goals_overunder_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_275 is not None and pre_goals_overunder_over_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder_over_30 is not None and pre_goals_overunder_over_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_325 is not None and pre_goals_overunder_over_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_35 is not None and pre_goals_overunder_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_375 is not None and pre_goals_overunder_over_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o4
        if(pre_goals_overunder_over_40 is not None and pre_goals_overunder_over_40 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o40" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o40 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_425 is not None and pre_goals_overunder_over_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_45 is not None and pre_goals_overunder_over_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o45 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_475 is not None and pre_goals_overunder_over_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o5
        if(pre_goals_overunder_over_50 is not None and pre_goals_overunder_over_50 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o50" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o50 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_525 is not None and pre_goals_overunder_over_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_55 is not None and pre_goals_overunder_over_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o55 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_575 is not None and pre_goals_overunder_over_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o6
        if(pre_goals_overunder_over_60 is not None and pre_goals_overunder_over_60 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o60" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o60 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_625 is not None and pre_goals_overunder_over_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_65 is not None and pre_goals_overunder_over_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o65 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_over_675 is not None and pre_goals_overunder_over_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o7
        if(pre_goals_overunder_over_70 is not None and pre_goals_overunder_over_70 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o70" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o70 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_goals_overunder_over_75 is not None and pre_goals_overunder_over_75 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o75" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o75 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        # ---------------------------------------------------------------------------------------------- o8 
        if(pre_goals_overunder_over_85 is not None and pre_goals_overunder_over_85 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o85" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o85 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        # ---------------------------------------------------------------------------------------------- o9 
        if(pre_goals_overunder_over_95 is not None and pre_goals_overunder_over_95 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'o95" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' o95 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   


        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_under_05 is not None and pre_goals_overunder_under_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_075 is not None and pre_goals_overunder_under_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_under_10 is not None and pre_goals_overunder_under_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_125 is not None and pre_goals_overunder_under_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_15 is not None and pre_goals_overunder_under_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_175 is not None and pre_goals_overunder_under_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder_under_20 is not None and pre_goals_overunder_under_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_225 is not None and pre_goals_overunder_under_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_25 is not None and pre_goals_overunder_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_275 is not None and pre_goals_overunder_under_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder_under_30 is not None and pre_goals_overunder_under_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_325 is not None and pre_goals_overunder_under_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_35 is not None and pre_goals_overunder_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_375 is not None and pre_goals_overunder_under_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o4
        if(pre_goals_overunder_under_40 is not None and pre_goals_overunder_under_40 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u40" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u40 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_425 is not None and pre_goals_overunder_under_425 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u425" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u425 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_45 is not None and pre_goals_overunder_under_45 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u45" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u45 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_475 is not None and pre_goals_overunder_under_475 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u475" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u475 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o5
        if(pre_goals_overunder_under_50 is not None and pre_goals_overunder_under_50 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u50" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u50 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_525 is not None and pre_goals_overunder_under_525 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u525" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u525 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_55 is not None and pre_goals_overunder_under_55 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u55" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u55 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_575 is not None and pre_goals_overunder_under_575 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u575" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u575 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o6
        if(pre_goals_overunder_under_60 is not None and pre_goals_overunder_under_60 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u60" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u60 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_625 is not None and pre_goals_overunder_under_625 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u625" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u625 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_65 is not None and pre_goals_overunder_under_65 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u65" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u65 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_under_675 is not None and pre_goals_overunder_under_675 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u675" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u675 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o7
        if(pre_goals_overunder_under_70 is not None and pre_goals_overunder_under_70 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u70" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u70 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_goals_overunder_under_75 is not None and pre_goals_overunder_under_75 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u75" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u75 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        # ---------------------------------------------------------------------------------------------- o8 
        if(pre_goals_overunder_under_85 is not None and pre_goals_overunder_under_85 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u85" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u85 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        # ---------------------------------------------------------------------------------------------- o9 
        if(pre_goals_overunder_under_95 is not None and pre_goals_overunder_under_95 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'u95" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' u95 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   


        # ---------------------------------------------------------------------------------------------- 1st -1     
        if(pre_asian_handicap_first_half_home_min_175 is not None and pre_asian_handicap_first_half_home_min_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_min_15 is not None and pre_asian_handicap_first_half_home_min_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_min_125 is not None and pre_asian_handicap_first_half_home_min_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_min_1 is not None and pre_asian_handicap_first_half_home_min_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- 1st -1     
        if(pre_asian_handicap_first_half_home_min_075 is not None and pre_asian_handicap_first_half_home_min_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_min_05 is not None and pre_asian_handicap_first_half_home_min_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_min_025 is not None and pre_asian_handicap_first_half_home_min_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H-025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H-025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

            
        # ---------------------------------------------------------------------------------------------- 1st -1     
        if(pre_asian_handicap_first_half_away_min_175 is not None and pre_asian_handicap_first_half_away_min_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_min_15 is not None and pre_asian_handicap_first_half_away_min_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_min_125 is not None and pre_asian_handicap_first_half_away_min_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_min_1 is not None and pre_asian_handicap_first_half_away_min_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- 1st -1     
        if(pre_asian_handicap_first_half_away_min_075 is not None and pre_asian_handicap_first_half_away_min_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_min_05 is not None and pre_asian_handicap_first_half_away_min_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_min_025 is not None and pre_asian_handicap_first_half_away_min_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A+025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A+025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

            

        # ---------------------------------------------------------------------------------------------- 1st +1   
        if(pre_asian_handicap_first_half_home_plus_0 is not None and pre_asian_handicap_first_half_home_plus_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+0' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_asian_handicap_first_half_home_plus_025 is not None and pre_asian_handicap_first_half_home_plus_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_plus_05 is not None and pre_asian_handicap_first_half_home_plus_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_asian_handicap_first_half_home_plus_075 is not None and pre_asian_handicap_first_half_home_plus_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
            

        # ---------------------------------------------------------------------------------------------- 1st +1   
        if(pre_asian_handicap_first_half_home_plus_1 is not None and pre_asian_handicap_first_half_home_plus_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_asian_handicap_first_half_home_plus_125 is not None and pre_asian_handicap_first_half_home_plus_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_home_plus_15 is not None and pre_asian_handicap_first_half_home_plus_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_asian_handicap_first_half_home_plus_175 is not None and pre_asian_handicap_first_half_home_plus_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah H+175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah H+175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        # ---------------------------------------------------------------------------------------------- 1st +1   
        if(pre_asian_handicap_first_half_away_plus_0 is not None and pre_asian_handicap_first_half_away_plus_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-0' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_asian_handicap_first_half_away_plus_025 is not None and pre_asian_handicap_first_half_away_plus_025 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-025" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-025 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_plus_05 is not None and pre_asian_handicap_first_half_away_plus_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_asian_handicap_first_half_away_plus_075 is not None and pre_asian_handicap_first_half_away_plus_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
            

        # ---------------------------------------------------------------------------------------------- 1st +1   
        if(pre_asian_handicap_first_half_away_plus_1 is not None and pre_asian_handicap_first_half_away_plus_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-1' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_asian_handicap_first_half_away_plus_125 is not None and pre_asian_handicap_first_half_away_plus_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_asian_handicap_first_half_away_plus_15 is not None and pre_asian_handicap_first_half_away_plus_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '   
        if(pre_asian_handicap_first_half_away_plus_175 is not None and pre_asian_handicap_first_half_away_plus_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Ah A-175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Ah A-175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

            
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_first_half_over_05 is not None and pre_goals_overunder_first_half_over_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_075 is not None and pre_goals_overunder_first_half_over_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_first_half_over_10 is not None and pre_goals_overunder_first_half_over_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_125 is not None and pre_goals_overunder_first_half_over_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_15 is not None and pre_goals_overunder_first_half_over_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_175 is not None and pre_goals_overunder_first_half_over_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder_first_half_over_20 is not None and pre_goals_overunder_first_half_over_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_225 is not None and pre_goals_overunder_first_half_over_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_25 is not None and pre_goals_overunder_first_half_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_275 is not None and pre_goals_overunder_first_half_over_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder_first_half_over_30 is not None and pre_goals_overunder_first_half_over_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_325 is not None and pre_goals_overunder_first_half_over_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_35 is not None and pre_goals_overunder_first_half_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_over_375 is not None and pre_goals_overunder_first_half_over_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-o375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-o375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_first_half_under_05 is not None and pre_goals_overunder_first_half_under_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_075 is not None and pre_goals_overunder_first_half_under_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder_first_half_under_10 is not None and pre_goals_overunder_first_half_under_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_125 is not None and pre_goals_overunder_first_half_under_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_15 is not None and pre_goals_overunder_first_half_under_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_175 is not None and pre_goals_overunder_first_half_under_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder_first_half_under_20 is not None and pre_goals_overunder_first_half_under_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_225 is not None and pre_goals_overunder_first_half_under_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_25 is not None and pre_goals_overunder_first_half_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_275 is not None and pre_goals_overunder_first_half_under_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder_first_half_under_30 is not None and pre_goals_overunder_first_half_under_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_325 is not None and pre_goals_overunder_first_half_under_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_35 is not None and pre_goals_overunder_first_half_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder_first_half_under_375 is not None and pre_goals_overunder_first_half_under_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-u375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-u375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
            
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder__second_half_over_05 is not None and pre_goals_overunder__second_half_over_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_075 is not None and pre_goals_overunder__second_half_over_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder__second_half_over_10 is not None and pre_goals_overunder__second_half_over_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_125 is not None and pre_goals_overunder__second_half_over_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_15 is not None and pre_goals_overunder__second_half_over_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_175 is not None and pre_goals_overunder__second_half_over_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder__second_half_over_20 is not None and pre_goals_overunder__second_half_over_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_225 is not None and pre_goals_overunder__second_half_over_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_25 is not None and pre_goals_overunder__second_half_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_275 is not None and pre_goals_overunder__second_half_over_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder__second_half_over_30 is not None and pre_goals_overunder__second_half_over_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_325 is not None and pre_goals_overunder__second_half_over_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_35 is not None and pre_goals_overunder__second_half_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_over_375 is not None and pre_goals_overunder__second_half_over_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-o375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-o375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  

        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder__second_half_under_05 is not None and pre_goals_overunder__second_half_under_05 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u05" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u05 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_075 is not None and pre_goals_overunder__second_half_under_075 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u075" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u075 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o1
        if(pre_goals_overunder__second_half_under_10 is not None and pre_goals_overunder__second_half_under_10 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u10" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u10 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_125 is not None and pre_goals_overunder__second_half_under_125 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u125" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u125 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_15 is not None and pre_goals_overunder__second_half_under_15 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u15" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u15 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_175 is not None and pre_goals_overunder__second_half_under_175 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u175" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u175 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o2
        if(pre_goals_overunder__second_half_under_20 is not None and pre_goals_overunder__second_half_under_20 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u20" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u20 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_225 is not None and pre_goals_overunder__second_half_under_225 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u225" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u225 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_25 is not None and pre_goals_overunder__second_half_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_275 is not None and pre_goals_overunder__second_half_under_275 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u275" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u275 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        # ---------------------------------------------------------------------------------------------- o3
        if(pre_goals_overunder__second_half_under_30 is not None and pre_goals_overunder__second_half_under_30 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u30" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u30 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_325 is not None and pre_goals_overunder__second_half_under_325 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u325" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u325 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_35 is not None and pre_goals_overunder__second_half_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_goals_overunder__second_half_under_375 is not None and pre_goals_overunder__second_half_under_375 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-u375" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-u375 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> '  
        if(pre_both_teams_score_no is not None and pre_both_teams_score_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_rcard_yes is not None and pre_rcard_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Red-y" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Red-y ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_rcard_no is not None and pre_rcard_no  == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Red-n" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Red-n ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_first_half_winner_home is not None and pre_first_half_winner_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1stHwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1stHwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_first_half_winner_draw is not None and pre_first_half_winner_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1stXwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1stXwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_first_half_winner_away is not None and pre_first_half_winner_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1stAwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1stAwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_second_half_winner_home is not None and pre_second_half_winner_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2ndHwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2ndHwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_winner_draw is not None and pre_second_half_winner_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2ndXwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2ndXwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_winner_away is not None and pre_second_half_winner_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2ndAwin" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2ndAwin ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_htft_double_home_home is not None and pre_htft_double_home_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-HH" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-HH ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_home_draw is not None and pre_htft_double_home_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-HX" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-HX ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_home_away is not None and pre_htft_double_home_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-HA" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-HA ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        if(pre_htft_double_draw_home is not None and pre_htft_double_draw_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-XH" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-XH ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_draw_draw is not None and pre_htft_double_draw_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-XX" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-XX ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_draw_away is not None and pre_htft_double_draw_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-XA" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-XA ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 

        if(pre_htft_double_away_home is not None and pre_htft_double_away_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-AH" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-AH ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_away_draw is not None and pre_htft_double_away_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-AX" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-AX ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_htft_double_away_away is not None and pre_htft_double_away_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'htft-AA" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' htft-AA ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_both_teams_score__first_half_yes is not None and pre_both_teams_score__first_half_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1stBty" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1stBty ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_both_teams_score__first_half_no is not None and pre_both_teams_score__first_half_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1stBtn" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1stBtn ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_both_teams_to_score__second_half_yes is not None and pre_both_teams_to_score__second_half_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2ndBty" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2ndBty ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_both_teams_to_score__second_half_no is not None and pre_both_teams_to_score__second_half_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2ndBtn" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2ndBtn ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_results_both_teams_score_home_yes is not None and pre_results_both_teams_score_home_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Bty-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Bty-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_results_both_teams_score_draw_yes is not None and pre_results_both_teams_score_draw_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Bty-X" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Bty-X ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_results_both_teams_score_away_yes is not None and pre_results_both_teams_score_away_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Bty-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Bty-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_results_both_teams_score_home_no is not None and pre_results_both_teams_score_home_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_results_both_teams_score_draw_no is not None and pre_results_both_teams_score_draw_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn-X" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn-X ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_results_both_teams_score_away_no is not None and pre_results_both_teams_score_away_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_to_score_in_both_halves_by_teams_home is not None and pre_to_score_in_both_halves_by_teams_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-sc-Halv" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-sc-Halv ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_to_score_in_both_halves_by_teams_away is not None and pre_to_score_in_both_halves_by_teams_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-sc-Halv" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-sc-Halv ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_total_goals_both_teams_to_score_over_yes_25 is not None and pre_total_goals_both_teams_to_score_over_yes_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Bty-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Bty-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_total_goals_both_teams_to_score_over_no_25 is not None and pre_total_goals_both_teams_to_score_over_no_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_total_goals_both_teams_to_score_under_yes_25 is not None and pre_total_goals_both_teams_to_score_under_yes_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Bty-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Bty-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_total_goals_both_teams_to_score_under_no_25 is not None and pre_total_goals_both_teams_to_score_under_no_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'Btn-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' Btn-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_both_teams_to_score_1st_half__2nd_half_yes_yes is not None and pre_both_teams_to_score_1st_half__2nd_half_yes_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-y-2nd-y" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-y-2nd-y ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_both_teams_to_score_1st_half__2nd_half_yes_no is not None and pre_both_teams_to_score_1st_half__2nd_half_yes_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-y-2nd-n" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-y-2nd-n ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_both_teams_to_score_1st_half__2nd_half_no_yes is not None and pre_both_teams_to_score_1st_half__2nd_half_no_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-n-2nd-y" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-n-2nd-y ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_both_teams_to_score_1st_half__2nd_half_no_no is not None and pre_both_teams_to_score_1st_half__2nd_half_no_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-n-2nd-n" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-n-2nd-n ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_highest_scoring_half_first is not None and pre_highest_scoring_half_first == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'High-1st" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' High-1st ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_highest_scoring_half_draw is not None and pre_highest_scoring_half_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'High-X" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' High-X ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_highest_scoring_half_second is not None and pre_highest_scoring_half_second == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'High-2nd" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' High-2nd ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_double_chance_home_draw is not None and pre_double_chance_home_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1x ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_double_chance_home_away is not None and pre_double_chance_home_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'12" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 12 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_double_chance_draw_away is not None and pre_double_chance_draw_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2x ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_double_chance__first_half_home_draw is not None and pre_double_chance__first_half_home_draw == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-1x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-1x ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_double_chance__first_half_home_away is not None and pre_double_chance__first_half_home_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-12" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-12 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_double_chance__first_half_draw_away is not None and pre_double_chance__first_half_draw_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-2x" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-2x ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_oddeven_odd is not None and pre_oddeven_odd == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'odd" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' odd ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_oddeven_even is not None and pre_oddeven_even == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'even" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' even ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_result_total_goals_home_over_35 is not None and pre_result_total_goals_home_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_draw_over_35 is not None and pre_result_total_goals_draw_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'X-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' X-o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_away_over_35 is not None and pre_result_total_goals_away_over_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-o35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-o35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_home_under_35 is not None and pre_result_total_goals_home_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_draw_under_35 is not None and pre_result_total_goals_draw_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'X-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' X-u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_away_under_35 is not None and pre_result_total_goals_away_under_35 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-u35" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-u35 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_home_over_25 is not None and pre_result_total_goals_home_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_draw_over_25 is not None and pre_result_total_goals_draw_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'X-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' X-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_away_over_25 is not None and pre_result_total_goals_away_over_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-o25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-o25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_home_under_25 is not None and pre_result_total_goals_home_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_draw_under_25 is not None and pre_result_total_goals_draw_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'X-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' X-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_result_total_goals_away_under_25 is not None and pre_result_total_goals_away_under_25 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-u25" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-u25 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_clean_sheet__home_yes is not None and pre_clean_sheet__home_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'CSy-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' CSy-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_clean_sheet__home_no is not None and pre_clean_sheet__home_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'CSn-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' CSn-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_clean_sheet__away_yes is not None and pre_clean_sheet__away_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'CSy-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' CSy-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_clean_sheet__away_no is not None and pre_clean_sheet__away_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'CSn-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' CSn-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_win_both_halves_home is not None and pre_win_both_halves_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-both" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-both ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_win_both_halves_away is not None and pre_win_both_halves_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-both" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-both ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_win_to_nil_home is not None and pre_win_to_nil_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-nil" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-nil ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_win_to_nil_away is not None and pre_win_to_nil_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-nil" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-nil ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_to_win_either_half_home is not None and pre_to_win_either_half_home == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-eithr ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_to_win_either_half_away is not None and pre_to_win_either_half_away == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-eithr" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-eithr ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_halftime_result_both_teams_score_home_yes is not None and pre_halftime_result_both_teams_score_home_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Bty-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Bty-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_halftime_result_both_teams_score_draw_yes is not None and pre_halftime_result_both_teams_score_draw_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Bty-X" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Bty-X ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_halftime_result_both_teams_score_away_yes is not None and pre_halftime_result_both_teams_score_away_yes == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Bty-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Bty-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_halftime_result_both_teams_score_home_no is not None and pre_halftime_result_both_teams_score_home_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Btn-H" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Btn-H ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_halftime_result_both_teams_score_draw_no is not None and pre_halftime_result_both_teams_score_draw_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Btn-X" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Btn-X ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_halftime_result_both_teams_score_away_no is not None and pre_halftime_result_both_teams_score_away_no == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-Btn-A" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-Btn-A ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_exact_goals_number__first_half_0 is not None and pre_exact_goals_number__first_half_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG-0 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_exact_goals_number__first_half_1 is not None and pre_exact_goals_number__first_half_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG-1 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_exact_goals_number__first_half_2 is not None and pre_exact_goals_number__first_half_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG-2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG-2 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_exact_goals_number__first_half_3 is not None and pre_exact_goals_number__first_half_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG-3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG-3 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_exact_goals_number__first_half_4 is not None and pre_exact_goals_number__first_half_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG-4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG-4 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_exact_goals_number__first_half_more_5 is not None and pre_exact_goals_number__first_half_more_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'1st-exG->5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 1st-exG->5 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_second_half_exact_goals_number_0 is not None and pre_second_half_exact_goals_number_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG-0 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_exact_goals_number_1 is not None and pre_second_half_exact_goals_number_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG-1 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_exact_goals_number_2 is not None and pre_second_half_exact_goals_number_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG-2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG-2 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_exact_goals_number_3 is not None and pre_second_half_exact_goals_number_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG-3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG-3 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_exact_goals_number_4 is not None and pre_second_half_exact_goals_number_4 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG-4" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG-4 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_second_half_exact_goals_number_more_5 is not None and pre_second_half_exact_goals_number_more_5 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'2nd-exG->5" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' 2nd-exG->5 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_home_team_exact_goals_number_0 is not None and pre_home_team_exact_goals_number_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-exG-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-exG-0 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_home_team_exact_goals_number_1 is not None and pre_home_team_exact_goals_number_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-exG-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-exG-1 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_home_team_exact_goals_number_2 is not None and pre_home_team_exact_goals_number_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-exG-2" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-exG-2 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_home_team_exact_goals_number_more_3 is not None and pre_home_team_exact_goals_number_more_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'H-exG->3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' H-exG->3 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        # ------------------------------------------------------
        if(pre_away_team_exact_goals_number_0 is not None and pre_away_team_exact_goals_number_0 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-exG-0" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-exG-0 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_away_team_exact_goals_number_1 is not None and pre_away_team_exact_goals_number_1 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-exG-1" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-exG-1 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_away_team_exact_goals_number_2 is not None and pre_away_team_exact_goals_number_2 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-exG-3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> '
            isi += ' A-exG-3 ' + ' 1.98'
            isi += ' </h6> ' 
            isi += ' </a> ' 
        if(pre_away_team_exact_goals_number_more_3 is not None and pre_away_team_exact_goals_number_more_3 == 1.98):
            good_to_go = 1
            good_to_go2 = 1
            isi += '<a href="'+route+'A-exG->3" '
            isi += ' target="_blank" '
            isi += ' class="badge badge  bg-gradient-gradient-gray-600 me-1 mt-2">'
            isi += ' <h6> ' 
            isi += ' A-exG->3 ' + ' 1.98' 
            isi += ' </a> ' 
        # ------------------------------------------------------

        print(space + "good_to_go: " + str(good_to_go), flush=True)

        on_eye = 'Null'
        if(good_to_go2 == 1):
            pre_on_eye = '<i class="fa-solid fa-eye text-primary"></i>'
            on_eye = "'" + pre_on_eye + "'"


        if(good_to_go == 1):
            # ---------------------------------------------- 
            star = '<i class="fas fa-star text-yellow"></i>'
            # ---------------------------------------------- 
            query_commit = "update football_fixturesx set "   
            # ----------------------------------------------  
            # ---------------------------------------------- 
            if(ROUTES == 'one'):
                PREP_COL = "end" 
            elif(ROUTES == 'fixture'):
                PREP_COL = "pre" 
            elif(ROUTES == 'research_pre'):
                PREP_COL = "pre" 
            elif(ROUTES == 'research_end'):
                PREP_COL = "end" 
            elif(ROUTES == 'preleague'):
                PREP_COL = "pre" 
            query_commit += " on_"+PREP_COL+"define = '"+isi+"', " 
            query_commit += " on_eye = "+on_eye+", "  
            query_commit += " star = '"+star+"' "  
            query_commit += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
            # ---------------------------------------------- 
            # print(space + query_commit, flush=True)
            # ---------------------------------------------- 
            mycursor.execute(query_commit)
            mydb.commit()   
        # ------------------------------------------------------ 
        print("")
    # ----------------------------------------------------------  