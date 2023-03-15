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

    query += " from football_fixtures " 
    if(ROUTES == 'one'):
        query += " where one = 1 " 
    elif(ROUTES == 'fixture'):
        query += " where date >= '"+str(day0)+"' " 
        query += " and date <= '"+str(day1)+"' " 
        query += " and fixture_status like 'Not Started' " 
    query += " and deleted_at is null "   
    query += " order by date asc  "   
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
        # ------------------------------------------------------ 
        if(good_to_go == 1):
            # ---------------------------------------------- 
            star = '<i class="fas fa-star text-yellow"></i>'
            # ---------------------------------------------- 
            query_commit = "update football_fixtures set "   
            # ---------------------------------------------- 
            if(ROUTES == 'one'):
                PREP_COL = "end" 
            elif(ROUTES == 'fixture'):
                PREP_COL = "pre" 
            query_commit += " on_"+PREP_COL+"define = '"+isi+"', " 
            query_commit += " star = '"+star+"' "  
            query_commit += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
            # ---------------------------------------------- 
            mycursor.execute(query_commit)
            mydb.commit()  
        # ------------------------------------------------------ 
        print("")
    # ----------------------------------------------------------  