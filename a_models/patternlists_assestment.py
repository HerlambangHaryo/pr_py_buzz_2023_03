# Import
import mysql.connector

def pa_assestment(leagueapi_id, yesterday_ago, space): 
    # ----------------------------------------------------------  
    space += "  "
    print(space + "__pa_assestment__")
    # ----------------------------------------------------------    
    space += "  "
    print(space + "_>pa_check_league_tanggal_update_patternlists__")
    # ----------------------------------------------------------  
    space += "  "
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()  
    # ----------------------------------------------------------  
    query = " Select tanggal_update_patternlists  "
    query += " from leagues "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        tanggal_update_patternlists = x[0]
    # ---------------------------------------------------------- 
    space += "  "
    print(space + "_>pa_get_league_fixtures__")
    # ---------------------------------------------------------- 
    query = ' SELECT  '
    query += ' pre_ah_pattern ' 
    query += ' , pre_ah_pattern_mirror ' 
    query += ' , pre_gou_pattern '  
    query += ' , leagueapi_id ' 
    query += ' , fixtureapi_id '  
    query += ' , date '  
    query += ' , end_ah_pattern ' 
    query += ' , end_ah_pattern_mirror ' 
    query += ' , end_gou_pattern '  
    query += ' , season '   
    query += ' , round '    
    query += ' , teams_home '   
    query += ' , teams_away ' 
    query += ' , league_country ' 
    query += 'FROM football_fixtures'  
    query += " WHERE fixture_status in ('Match Finished', 'Match Finished Ended') "     
    query += " and leagueapi_id = '"+str(leagueapi_id)+"' "    
    # ----------------------------------------------------------   
    if(tanggal_update_patternlists is not None):
        query += " and date <= '"+str(yesterday_ago)+"' " 
        query += " and date >= '"+str(tanggal_update_patternlists)+"' "                 
    elif(tanggal_update_patternlists is None):
        query += " and date <= '"+str(yesterday_ago)+"' "         
    # ---------------------------------------------------------- 
    query += " order by date asc "    
    # ---------------------------------------------------------- 
    mycursor = mydb.cursor() 
    mycursor.execute(query) 
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(myresult)))  
    # ---------------------------------------------------------- 
    counter = 0 
    space += "  "
    # ---------------------------------------------------------- 
    for x in myresult:      
        # ------------------------------------------------------
        print("")
        # ------------------------------------------------------
        counter += 1
        param = "counter : " + str(counter) + " / " +  str(len(myresult))
        print(space + param) 
        # ------------------------------------------------------
        pre_ah_pattern = x[0]
        param = "pre_ah_pattern : " + str(pre_ah_pattern)
        print(space + param) 
        # ------------------------------------------------------
        pre_ah_pattern_mirror = x[1]
        # param = "pre_ah_pattern_mirror : " + str(pre_ah_pattern_mirror)
        # print(space + param) 
        # ------------------------------------------------------        
        pre_gou_pattern = x[2]
        param = "pre_gou_pattern : " + str(pre_gou_pattern)
        print(space + param) 
        # ------------------------------------------------------        
        leagueapi_id = x[3]
        # param = "leagueapi_id : " + str(leagueapi_id)
        # print(space + param) 
        # ------------------------------------------------------        
        fixtureapi_id = x[4]
        # param = "fixtureapi_id : " + str(fixtureapi_id)
        # print(space + param) 
        # ------------------------------------------------------        
        date = x[5]
        # param = "date : " + str(date)
        # print(space + param) 
        # ------------------------------------------------------        
        end_ah_pattern = x[6]
        param = "end_ah_pattern : " + str(end_ah_pattern)
        print(space + param) 
        # ------------------------------------------------------        
        end_ah_pattern_mirror = x[7]
        # param = "end_ah_pattern_mirror : " + str(end_ah_pattern_mirror)
        # print(space + param) 
        # ------------------------------------------------------        
        end_gou_pattern = x[8]
        param = "end_gou_pattern : " + str(end_gou_pattern)
        (space + param) 
        # ------------------------------------------------------        
        season = x[9]
        # param = "season : " + str(season)
        # print(space + param) 
        # ------------------------------------------------------        
        xround = x[10]
        # param = "xround : " + str(xround)
        # print(space + param) 
        # ------------------------------------------------------        
        teams_home = x[11]
        # param = "teams_home : " + str(teams_home)
        # print(space + param) 
        # ------------------------------------------------------        
        teams_away = x[12]
        # param = "teams_away : " + str(teams_away)
        # print(space + param) 
        # ------------------------------------------------------        
        league_country = x[13]
        # param = "league_country : " + str(league_country)
        # print(space + param) 
        # ------------------------------------------------------
        query_1 = " (select " 
        query_1 += " goals_home, " 
        query_1 += " goals_away, " 
        query_1 += " end_ah_pattern, " 
        query_1 += " score_halftime_home, " 
        query_1 += " score_halftime_away  "
        
        query_1 += " from `football_fixtures` " 
        query_1 += " where `pre_ah_pattern` = '"+str(pre_ah_pattern)+"' "
        query_1 += " and `pre_gou_pattern` = '"+str(pre_gou_pattern)+"' "

        query_1 += " and `end_ah_pattern` = '"+str(end_ah_pattern)+"' "
        query_1 += " and `end_gou_pattern` = '"+str(end_gou_pattern)+"' "

        query_1 += " and `goals_home` is not null " 
        query_1 += " and `goals_away` is not null "  

        query_1 += " and `leagueapi_id` = "+str(leagueapi_id)+" "
        query_1 += " and `fixture_status` in ('Match Finished Ended', 'Match Finished') "
        query_1 += " and `football_fixtures`.`deleted_at` is null order by `date` asc) " 
        # ------------------------------------------------------
        mycursor = mydb.cursor() 
        mycursor.execute(query_1) 
        myresult_ff = mycursor.fetchall()
        # ------------------------------------------------------    
        print(space + "Total Row(s) : " + str(len(myresult_ff)))  
        # ------------------------------------------------------ 
        pattern_total_ff = len(myresult_ff)
        # ------------------------------------------------------  
        print(space + "_>pa_check_patternlist__")
        # ------------------------------------------------------ 
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()  
        # ------------------------------------------------------
        query_1 = " select *  "
        query_1 += " from `pattern_lists` " 
        query_1 += " where country = '"+str(league_country)+"' "
        query_1 += " and leagueapi_id = '"+str(leagueapi_id)+"' "
        
        query_1 += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "
        query_1 += " and pre_ah_pattern_mirror = '"+str(pre_ah_pattern_mirror)+"' "
        query_1 += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "
        
        query_1 += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "
        query_1 += " and end_ah_pattern_mirror = '"+str(end_ah_pattern_mirror)+"' "
        query_1 += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "
        # ------------------------------------------------------
        mycursor = mydb.cursor() 
        mycursor.execute(query_1) 
        myresult_pl = mycursor.fetchall()
        # ------------------------------------------------------   
        pattern_total_pl = len(myresult_pl)  
        # ------------------------------------------------------
        if(pattern_total_pl == 0 ): 
            # --------------------------------------------------  
            print(space + "  _>pa_insert_patternlists__")
            # -------------------------------------------------- 
            query = "INSERT INTO `pattern_lists`( "
            query += " `country`, `leagueapi_id`, "
            query += " `pre_ah_pattern`, `pre_ah_pattern_mirror`, "
            query += " `pre_gou_pattern`, `end_ah_pattern`, "
            query += " `end_ah_pattern_mirror`, `end_gou_pattern`) VALUES ( "
            query += " '"+str(league_country)+"', "
            query += " '"+str(leagueapi_id)+"', "
            # -------------------------------------------------- 
            query += " '"+str(pre_ah_pattern)+"', "
            query += " '"+str(pre_ah_pattern_mirror)+"', "
            query += " '"+str(pre_gou_pattern)+"', "
            # -------------------------------------------------- 
            query += " '"+str(end_ah_pattern)+"', "
            query += " '"+str(end_ah_pattern_mirror)+"', "
            query += " '"+str(end_gou_pattern)+"' "
            query += " ) "
            # -------------------------------------------------- 
            mycursor.execute(query)
            mydb.commit() 
            print(space + "    insert commited")
        # ------------------------------------------------------  
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()  
        # ------------------------------------------------------ 
        if(pattern_total_ff < 1):  
            # --------------------------------------------------
            print(space + "  Pattern Total tidak memenuhi syarat ")
        else: 
            # --------------------------------------------------
            print(space + "  Memenuhi syarat ") 
            ## -----------------------------------////////////// betid = 1
            match_winner_home = 0
            match_winner_draw = 0
            match_winner_away = 0
            ## -----------------------------------////////////// betid = 2
            homeaway_home = 0
            homeaway_away = 0
            ## -----------------------------------////////////// betid = 13
            first_half_winner_home = 0
            first_half_winner_draw = 0
            first_half_winner_away = 0 
            ## -----------------------------------////////////// betid = 3
            second_half_winner_home = 0
            second_half_winner_draw = 0
            second_half_winner_away = 0 
            ## -----------------------------------////////////// betid = 4
            asian_handicap_home_plus_0 = 0
            asian_handicap_away_plus_0 = 0

            asian_handicap_home_plus_05 = 0
            asian_handicap_away_plus_05 = 0

            asian_handicap_home_plus_1 = 0
            asian_handicap_away_plus_1 = 0

            asian_handicap_home_plus_15 = 0
            asian_handicap_away_plus_15 = 0

            asian_handicap_home_plus_2 = 0
            asian_handicap_away_plus_2 = 0

            asian_handicap_home_plus_25 = 0
            asian_handicap_away_plus_25 = 0

            asian_handicap_home_plus_3 = 0
            asian_handicap_away_plus_3 = 0

            asian_handicap_home_plus_35 = 0
            asian_handicap_away_plus_35 = 0

            asian_handicap_home_plus_4 = 0
            asian_handicap_away_plus_4 = 0

            asian_handicap_home_plus_45 = 0
            asian_handicap_away_plus_45 = 0

            asian_handicap_home_plus_5 = 0
            asian_handicap_away_plus_5 = 0

            asian_handicap_home_plus_55 = 0
            asian_handicap_away_plus_55 = 0

            asian_handicap_home_plus_6 = 0
            asian_handicap_away_plus_6 = 0

            asian_handicap_home_plus_65 = 0
            asian_handicap_away_plus_65 = 0


            asian_handicap_home_min_05 = 0
            asian_handicap_away_min_05 = 0

            asian_handicap_home_min_1 = 0
            asian_handicap_away_min_1 = 0

            asian_handicap_home_min_15 = 0
            asian_handicap_away_min_15 = 0

            asian_handicap_home_min_2 = 0
            asian_handicap_away_min_2 = 0

            asian_handicap_home_min_25 = 0
            asian_handicap_away_min_25 = 0

            asian_handicap_home_min_3 = 0
            asian_handicap_away_min_3 = 0

            asian_handicap_home_min_35 = 0
            asian_handicap_away_min_35 = 0

            asian_handicap_home_min_4 = 0
            asian_handicap_away_min_4 = 0

            asian_handicap_home_min_45 = 0
            asian_handicap_away_min_45 = 0

            asian_handicap_home_min_5 = 0
            asian_handicap_away_min_5 = 0

            asian_handicap_home_min_55 = 0
            asian_handicap_away_min_55 = 0

            asian_handicap_home_min_6 = 0
            asian_handicap_away_min_6 = 0

            asian_handicap_home_min_65 = 0
            asian_handicap_away_min_65 = 0
            ## -----------------------------------////////////// betid = 19
            asian_handicap_first_half_home_plus_0 = 0
            asian_handicap_first_half_away_plus_0 = 0

            asian_handicap_first_half_home_plus_05 = 0
            asian_handicap_first_half_away_plus_05 = 0

            asian_handicap_first_half_home_plus_1 = 0
            asian_handicap_first_half_away_plus_1 = 0

            asian_handicap_first_half_home_plus_15 = 0
            asian_handicap_first_half_away_plus_15 = 0 


            asian_handicap_first_half_home_min_05 = 0
            asian_handicap_first_half_away_min_05 = 0

            asian_handicap_first_half_home_min_1 = 0
            asian_handicap_first_half_away_min_1 = 0

            asian_handicap_first_half_home_min_15 = 0
            asian_handicap_first_half_away_min_15 = 0
            ## -----------------------------------////////////// betid = 5 
            goals_overunder_over_05  = 0
            goals_overunder_under_05 = 0

            goals_overunder_over_15  = 0
            goals_overunder_under_15 = 0

            goals_overunder_over_25  = 0
            goals_overunder_under_25 = 0

            goals_overunder_over_35  = 0
            goals_overunder_under_35 = 0

            goals_overunder_over_45  = 0
            goals_overunder_under_45 = 0

            goals_overunder_over_55  = 0
            goals_overunder_under_55 = 0 
            ## -----------------------------------////////////// betid = 6 
            goals_overunder_first_half_over_05  = 0
            goals_overunder_first_half_under_05 = 0

            goals_overunder_first_half_over_15  = 0
            goals_overunder_first_half_under_15 = 0

            goals_overunder_first_half_over_25  = 0
            goals_overunder_first_half_under_25 = 0

            goals_overunder_first_half_over_35  = 0
            goals_overunder_first_half_under_35 = 0 
            ## -----------------------------------////////////// betid = 26 
            goals_overunder__second_half_over_05  = 0
            goals_overunder__second_half_under_05 = 0

            goals_overunder__second_half_over_15  = 0
            goals_overunder__second_half_under_15 = 0

            goals_overunder__second_half_over_25  = 0
            goals_overunder__second_half_under_25 = 0

            goals_overunder__second_half_over_35  = 0
            goals_overunder__second_half_under_35 = 0 
            ## -----------------------------------////////////// betid = 12 
            double_chance_home_draw = 0
            double_chance_home_away = 0
            double_chance_draw_away = 0 
            ## -----------------------------------////////////// betid = 8 
            both_teams_score_yes = 0
            both_teams_score_no  = 0 
            ## -----------------------------------////////////// betid = 34 
            both_teams_score__first_half_yes = 0
            both_teams_score__first_half_no  = 0 
            ## -----------------------------------////////////// betid = 35 
            both_teams_to_score__second_half_yes = 0
            both_teams_to_score__second_half_no  = 0 
            ## -----------------------------------////////////// betid = 24
            results_both_teams_score_home_yes = 0
            results_both_teams_score_draw_yes = 0
            results_both_teams_score_away_yes = 0

            results_both_teams_score_home_no = 0
            results_both_teams_score_draw_no = 0
            results_both_teams_score_away_no = 0 
            ## -----------------------------------////////////// betid = 49
            total_goals_both_teams_to_score_over_yes_25  = 0
            total_goals_both_teams_to_score_over_no_25   = 0
            total_goals_both_teams_to_score_under_yes_25 = 0
            total_goals_both_teams_to_score_under_no_25  = 0 
            ## -----------------------------------////////////// betid = 73
            both_teams_to_score_1st_half__2nd_half_yes_yes = 0
            both_teams_to_score_1st_half__2nd_half_yes_no = 0
            both_teams_to_score_1st_half__2nd_half_no_yes = 0
            both_teams_to_score_1st_half__2nd_half_no_no = 0 
            ## -----------------------------------////////////// betid = 27
            clean_sheet__home_yes = 0
            clean_sheet__home_no  = 0 
            ## -----------------------------------////////////// betid = 28
            clean_sheet__away_yes = 0
            clean_sheet__away_no  = 0 
            ## -----------------------------------////////////// betid = 48 
            ## -----------------------------------////////////// betid = 21 
            oddeven_odd  = 0
            oddeven_even = 0 
            ## -----------------------------------////////////// betid = 38 
            exact_goals_number_0 = 0
            exact_goals_number_1 = 0
            exact_goals_number_2 = 0
            exact_goals_number_3 = 0
            exact_goals_number_4 = 0
            exact_goals_number_5 = 0
            exact_goals_number_6 = 0
            exact_goals_number_more_7 = 0  
            ## -----------------------------------////////////// betid = 46 
            exact_goals_number__first_half_0 = 0
            exact_goals_number__first_half_1 = 0
            exact_goals_number__first_half_2 = 0
            exact_goals_number__first_half_3 = 0
            exact_goals_number__first_half_4 = 0
            exact_goals_number__first_half_more_5 = 0   
            ## -----------------------------------////////////// betid = 48 
            second_half_exact_goals_number_0 = 0
            second_half_exact_goals_number_1 = 0
            second_half_exact_goals_number_2 = 0
            second_half_exact_goals_number_3 = 0
            second_half_exact_goals_number_4 = 0
            second_half_exact_goals_number_more_5 = 0   
            ## -----------------------------------////////////// betid = 40 
            home_team_exact_goals_number_0 = 0
            home_team_exact_goals_number_1 = 0
            home_team_exact_goals_number_2 = 0
            home_team_exact_goals_number_more_3 = 0 
            ## -----------------------------------////////////// betid = 41 
            away_team_exact_goals_number_0 = 0
            away_team_exact_goals_number_1 = 0
            away_team_exact_goals_number_2 = 0
            away_team_exact_goals_number_more_3 = 0 
            ## -----------------------------------////////////// betid = 36 
            win_to_nil_home = 0
            win_to_nil_away = 0 
            ## -----------------------------------////////////// betid = 39
            to_win_either_half_home = 0
            to_win_either_half_away = 0 
            ## -----------------------------------////////////// betid = 32
            win_both_halves_home = 0
            win_both_halves_away = 0 
            ## -----------------------------------////////////// betid = 48
            to_score_in_both_halves_by_teams_home = 0
            to_score_in_both_halves_by_teams_away = 0  
            ## -----------------------------------////////////// betid = 11    
            highest_scoring_half_first  = 0
            highest_scoring_half_draw   = 0
            highest_scoring_half_second = 0 
            ## -----------------------------------////////////// betid = 7 
            htft_double_home_draw = 0
            htft_double_home_away = 0
            htft_double_draw_away = 0
            htft_double_draw_draw = 0
            htft_double_home_home = 0
            htft_double_draw_home = 0
            htft_double_away_home = 0
            htft_double_away_draw = 0
            htft_double_away_away = 0 
            ## -----------------------------------////////////// betid = 20 
            double_chance__first_half_home_draw = 0
            double_chance__first_half_home_away = 0
            double_chance__first_half_draw_away = 0 
            ## -----------------------------------////////////// betid = 25 
            result_total_goals_home_over_35 = 0
            result_total_goals_draw_over_35 = 0
            result_total_goals_away_over_35 = 0

            result_total_goals_home_under_35 = 0
            result_total_goals_draw_under_35 = 0
            result_total_goals_away_under_35 = 0

            result_total_goals_home_over_25 = 0
            result_total_goals_draw_over_25 = 0
            result_total_goals_away_over_25 = 0

            result_total_goals_home_under_25 = 0
            result_total_goals_draw_under_25 = 0
            result_total_goals_away_under_25 = 0 
            ## -----------------------------------////////////// betid = 52 
            halftime_result_both_teams_score_home_yes = 0
            halftime_result_both_teams_score_draw_yes = 0
            halftime_result_both_teams_score_away_yes = 0

            halftime_result_both_teams_score_home_no = 0
            halftime_result_both_teams_score_draw_no = 0
            halftime_result_both_teams_score_away_no = 0 
            # -------------------------------------------------- 
            for x in myresult_ff: 
                # ---------------------------------------------- 
                btts_sts = 'no'
                btts_first_sts = 'no'
                btts_second_sts = 'no'
                # ----------------------------------------------
                goals_home = x[0]
                goals_away = x[1]
                # ----------------------------------------------
                score_halftime_home = x[3]
                score_halftime_away = x[4]
                # ---------------------------------------------- 
                # print(space + "goals_home: " + str(goals_home) )
                # print(space + "goals_away: " + str(goals_away) )
                # ---------------------------------------------- 
                # print(space + "score_halftime_home: " + str(score_halftime_home) )
                # print(space + "score_halftime_away: " + str(score_halftime_away) )
                # ----------------------------------------------
                total_goals = goals_home + goals_away
                # ---------------------------------------------- 
                if(score_halftime_home is not None):
                    score_secondtime_home = abs(goals_home - score_halftime_home)
                    score_secondtime_away = abs(goals_away - score_halftime_away)
                    total_goals_half = score_halftime_home + score_halftime_away
                    total_goals_second = score_secondtime_home + score_secondtime_away 
                ## --------------------------------------------- betid = 1  
                if(goals_home > goals_away):
                    match_winner_home += 1 
                elif(goals_home == goals_away):
                    match_winner_draw += 1
                elif(goals_home < goals_away):
                    match_winner_away += 1
                ## --------------------------------------------- betid = 2
                if(goals_home > goals_away):
                    homeaway_home += 1  
                elif(goals_home < goals_away):
                    homeaway_away += 1
                ## --------------------------------------------- betid = 4   
                if(goals_home > goals_away):
                    asian_handicap_home_plus_0 += 1
                if(goals_home < goals_away):
                    asian_handicap_away_plus_0 += 1
                ## ---------------------------------------------
                if(goals_home + 0.5 > goals_away):
                    asian_handicap_home_plus_05 += 1
                if(goals_home + 0.5 < goals_away):
                    asian_handicap_away_min_05 += 1
                ## ---------------------------------------------
                if(goals_home + 1 > goals_away):
                    asian_handicap_home_plus_1 += 1
                if(goals_home + 1 < goals_away):
                    asian_handicap_away_min_1 += 1
                ## ---------------------------------------------
                if(goals_home + 1.5 > goals_away):
                    asian_handicap_home_plus_15 += 1
                if(goals_home + 1.5 < goals_away):
                    asian_handicap_away_min_15 += 1
                ## ---------------------------------------------
                if(goals_home + 2 > goals_away):
                    asian_handicap_home_plus_2 += 1
                if(goals_home + 2 < goals_away):
                    asian_handicap_away_min_2 += 1
                ## ---------------------------------------------
                if(goals_home + 2.5 > goals_away):
                    asian_handicap_home_plus_25 += 1
                if(goals_home + 2.5 < goals_away):
                    asian_handicap_away_min_25 += 1
                ## ---------------------------------------------
                if(goals_home + 3 > goals_away):
                    asian_handicap_home_plus_3 += 1
                if(goals_home + 3 < goals_away):
                    asian_handicap_away_min_3 += 1
                ## ---------------------------------------------
                if(goals_home + 3.5 > goals_away):
                    asian_handicap_home_plus_35 += 1
                if(goals_home + 3.5 < goals_away):
                    asian_handicap_away_min_35 += 1
                ## ---------------------------------------------
                if(goals_home + 4 > goals_away):
                    asian_handicap_home_plus_4 += 1
                if(goals_home + 4 < goals_away):
                    asian_handicap_away_min_4 += 1
                ## ---------------------------------------------
                if(goals_home + 4.5 > goals_away):
                    asian_handicap_home_plus_45 += 1
                if(goals_home + 4.5 < goals_away):
                    asian_handicap_away_min_45 += 1
                ## ---------------------------------------------
                if(goals_home + 5 > goals_away):
                    asian_handicap_home_plus_5 += 1
                if(goals_home + 5 < goals_away):
                    asian_handicap_away_min_5 += 1
                ## ---------------------------------------------
                if(goals_home + 5.5 > goals_away):
                    asian_handicap_home_plus_55 += 1
                if(goals_home + 5.5 < goals_away):
                    asian_handicap_away_min_55 += 1
                ## ---------------------------------------------
                if(goals_home + 6 > goals_away):
                    asian_handicap_home_plus_6 += 1
                if(goals_home + 6 < goals_away):
                    asian_handicap_away_min_6 += 1
                ## ---------------------------------------------
                if(goals_home + 6.5 > goals_away):
                    asian_handicap_home_plus_65 += 1
                if(goals_home + 6.5 < goals_away):
                    asian_handicap_away_min_65 += 1
                ## ---------------------------------------------
                if(goals_home - 0.5 > goals_away):
                    asian_handicap_home_min_05 += 1
                if(goals_home - 0.5 < goals_away):
                    asian_handicap_away_plus_05 += 1
                ## ---------------------------------------------
                if(goals_home - 1 > goals_away):
                    asian_handicap_home_min_1 += 1
                if(goals_home - 1 < goals_away):
                    asian_handicap_away_plus_1 += 1
                ## ---------------------------------------------
                if(goals_home - 1.5 > goals_away):
                    asian_handicap_home_min_15 += 1
                if(goals_home - 1.5 < goals_away):
                    asian_handicap_away_plus_15 += 1
                ## ---------------------------------------------
                if(goals_home - 2 > goals_away):
                    asian_handicap_home_min_2 += 1
                if(goals_home - 2 < goals_away):
                    asian_handicap_away_plus_2 += 1
                ## ---------------------------------------------
                if(goals_home - 2.5 > goals_away):
                    asian_handicap_home_min_25 += 1
                if(goals_home - 2.5 < goals_away):
                    asian_handicap_away_plus_25 += 1
                ## ---------------------------------------------
                if(goals_home - 3 > goals_away):
                    asian_handicap_home_min_3 += 1
                if(goals_home - 3 < goals_away):
                    asian_handicap_away_plus_3 += 1
                ## ---------------------------------------------
                if(goals_home - 3.5 > goals_away):
                    asian_handicap_home_min_35 += 1
                if(goals_home - 3.5 < goals_away):
                    asian_handicap_away_plus_35 += 1
                ## ---------------------------------------------
                if(goals_home - 4 > goals_away):
                    asian_handicap_home_min_4 += 1
                if(goals_home - 4 < goals_away):
                    asian_handicap_away_plus_4 += 1
                ## ---------------------------------------------
                if(goals_home - 4.5 > goals_away):
                    asian_handicap_home_min_45 += 1
                if(goals_home - 4.5 < goals_away):
                    asian_handicap_away_plus_45 += 1
                ## ---------------------------------------------
                if(goals_home - 5 > goals_away):
                    asian_handicap_home_min_5 += 1
                if(goals_home - 5 < goals_away):
                    asian_handicap_away_plus_5 += 1
                ## ---------------------------------------------
                if(goals_home - 5.5 > goals_away):
                    asian_handicap_home_min_55 += 1
                if(goals_home - 5.5 < goals_away):
                    asian_handicap_away_plus_55 += 1
                ## ---------------------------------------------
                if(goals_home - 6 > goals_away):
                    asian_handicap_home_min_6 += 1
                if(goals_home - 6 < goals_away):
                    asian_handicap_away_plus_6 += 1
                ## ---------------------------------------------
                if(goals_home - 6.5 > goals_away):
                    asian_handicap_home_min_65 += 1
                if(goals_home - 6.5 < goals_away):
                    asian_handicap_away_plus_65 += 1 
                ## --------------------------------------------- betid = 5 
                if(total_goals > 0):
                    goals_overunder_over_05  += 1
                if(total_goals < 1):
                    goals_overunder_under_05 += 1
                ## ---------------------------------------------
                if(total_goals > 1):
                    goals_overunder_over_15  += 1
                if(total_goals < 2):
                    goals_overunder_under_15 += 1
                ## ---------------------------------------------
                if(total_goals > 2):
                    goals_overunder_over_25  += 1
                if(total_goals < 3):
                    goals_overunder_under_25 += 1
                ## ---------------------------------------------
                if(total_goals > 3):
                    goals_overunder_over_35  += 1
                if(total_goals < 4):
                    goals_overunder_under_35 += 1
                ## ---------------------------------------------
                if(total_goals > 4):
                    goals_overunder_over_45  += 1
                if(total_goals < 5):
                    goals_overunder_under_45 += 1
                ## ---------------------------------------------
                if(total_goals > 5):
                    goals_overunder_over_55  += 1
                if(total_goals < 6):
                    goals_overunder_under_55 += 1 
                ## --------------------------------------------- betid = 8
                if( (goals_home > 0) and (goals_away > 0) ):
                    both_teams_score_yes += 1
                    btts_sts = 'yes'
                else:
                    both_teams_score_no  += 1
                ## --------------------------------------------- betid = 12
                if(goals_home >= goals_away):
                    double_chance_home_draw += 1 
                elif(goals_home != goals_away):
                    double_chance_home_away += 1
                elif(goals_home <= goals_away):
                    double_chance_draw_away += 1 
                ## --------------------------------------------- betid = 21
                if( (total_goals % 2) == 0):
                    oddeven_even  += 1
                else:
                    oddeven_odd += 1
                ## --------------------------------------------- betid = 8
                if(btts_sts == 'yes'): 
                    if(goals_home > goals_away):
                        results_both_teams_score_home_yes += 1 
                    elif(goals_home == goals_away):
                        results_both_teams_score_draw_yes += 1
                    elif(goals_home < goals_away):
                        results_both_teams_score_away_yes += 1
                elif(btts_sts == 'no'): 
                    if(goals_home > goals_away):
                        results_both_teams_score_home_no += 1 
                    elif(goals_home == goals_away):
                        results_both_teams_score_draw_no += 1
                    elif(goals_home < goals_away):
                        results_both_teams_score_away_no += 1
                ## --------------------------------------------- betid = 49
                if(btts_sts == 'yes'):
                    if(total_goals > 2):
                        total_goals_both_teams_to_score_over_yes_25  += 1
                    elif(total_goals < 3):
                        total_goals_both_teams_to_score_under_yes_25 += 1 
                elif(btts_sts == 'no'):
                    if(total_goals > 2):
                        total_goals_both_teams_to_score_over_no_25   += 1
                    elif(total_goals < 3):
                        total_goals_both_teams_to_score_under_no_25  += 1 
                ## --------------------------------------------- betid = 27
                if(goals_home == 0):
                    clean_sheet__away_yes += 1 
                else:
                    clean_sheet__away_no += 1 
                ## --------------------------------------------- betid = 28
                if(goals_away == 0):
                    clean_sheet__home_yes += 1 
                else:
                    clean_sheet__home_no += 1  
                ## --------------------------------------------- betid = 38 
                if(total_goals == 0):
                    exact_goals_number_0 += 1
                elif(total_goals == 1):
                    exact_goals_number_1 += 1
                elif(total_goals == 2):
                    exact_goals_number_2 += 1
                elif(total_goals == 3):
                    exact_goals_number_3 += 1
                elif(total_goals == 4):
                    exact_goals_number_4 += 1
                elif(total_goals == 5):
                    exact_goals_number_5 += 1
                elif(total_goals == 6):
                    exact_goals_number_6 += 1
                elif(total_goals >= 7):
                    exact_goals_number_more_7 += 1 
                ## --------------------------------------------- betid = 40 
                if(goals_home == 0):
                    home_team_exact_goals_number_0 += 1
                elif(goals_home == 1):
                    home_team_exact_goals_number_1 += 1
                elif(goals_home == 2):
                    home_team_exact_goals_number_2 += 1
                elif(goals_home >= 3):
                    home_team_exact_goals_number_more_3 += 1   
                ## --------------------------------------------- betid = 41 
                if(goals_away == 0):
                    away_team_exact_goals_number_0 += 1
                elif(goals_away == 1):
                    away_team_exact_goals_number_1 += 1
                elif(goals_away == 2):
                    away_team_exact_goals_number_2 += 1
                elif(goals_away >= 3):
                    away_team_exact_goals_number_more_3 += 1    
                ## --------------------------------------------- betid = 36 
                if(goals_home > goals_away and goals_away == 0):
                    win_to_nil_home += 1  
                elif(goals_home < goals_away and goals_home == 0):
                    win_to_nil_away += 1 
                ## --------------------------------------------- betid = 25 
                if(goals_home > goals_away): 
                    if(total_goals > 2):
                        result_total_goals_home_over_25 += 1
                    if(total_goals > 3):
                        result_total_goals_home_over_35 += 1
                    if(total_goals < 4): 
                        result_total_goals_home_under_35 += 1
                    if(total_goals < 3): 
                        result_total_goals_home_under_25 += 1
                elif(goals_home == goals_away): 
                    if(total_goals > 2):
                        result_total_goals_draw_over_25 += 1
                    if(total_goals > 3):
                        result_total_goals_draw_over_35 += 1
                    if(total_goals < 4): 
                        result_total_goals_draw_under_35 += 1
                    if(total_goals < 3): 
                        result_total_goals_draw_under_25 += 1
                elif(goals_home < goals_away): 
                    if(total_goals > 2):
                        result_total_goals_away_over_25 += 1
                    if(total_goals > 3):
                        result_total_goals_away_over_35 += 1
                    if(total_goals < 4): 
                        result_total_goals_away_under_35 += 1
                    if(total_goals < 3): 
                        result_total_goals_away_under_25 += 1 
                
                # ---------------------------------------------
                # --------------------------------------------- 
                # --------------------------------------------- 
                if(score_halftime_home is not None):
                    ## --------------------------------------------- betid = 52 
                    if(score_halftime_home > score_halftime_away): 
                        if(btts_first_sts == 'yes'): 
                            halftime_result_both_teams_score_home_yes += 1
                        elif(btts_first_sts == 'no'): 
                            halftime_result_both_teams_score_home_no += 1
                    elif(score_halftime_home == score_halftime_away): 
                        if(btts_first_sts == 'yes'): 
                            halftime_result_both_teams_score_draw_yes += 1
                        elif(btts_first_sts == 'no'): 
                            halftime_result_both_teams_score_draw_no += 1
                    elif(score_halftime_home < score_halftime_away): 
                        if(btts_first_sts == 'yes'): 
                            halftime_result_both_teams_score_away_yes += 1
                        elif(btts_first_sts == 'no'):  
                            halftime_result_both_teams_score_away_no += 1
                    ## ---------------------------------------- betid = 39
                    if(score_halftime_home > score_halftime_away and 
                       score_secondtime_home <= score_secondtime_away) :
                        to_win_either_half_home += 1
                    elif(score_halftime_home <= score_halftime_away and 
                         score_secondtime_home > score_secondtime_away) :
                        to_win_either_half_home += 1
                    elif(score_halftime_home < score_halftime_away and 
                         score_secondtime_home >= score_secondtime_away) :
                        to_win_either_half_away += 1
                    elif(score_halftime_home >= score_halftime_away and 
                         score_secondtime_home < score_secondtime_away) :
                        to_win_either_half_away += 1
                    ## ---------------------------------------- betid = 32
                    if(score_halftime_home > score_halftime_away and 
                       score_secondtime_home > score_secondtime_away) :
                        win_both_halves_home += 1
                    if(score_halftime_home < score_halftime_away and 
                       score_secondtime_home < score_secondtime_away) :
                        win_both_halves_away += 1
                    ## ---------------------------------------- betid = 48
                    if(score_halftime_home > 0 and score_secondtime_home > 0):
                        to_score_in_both_halves_by_teams_home = 0
                    if(score_halftime_away > 0 and score_secondtime_away > 0):
                        to_score_in_both_halves_by_teams_away = 0 
                    ## ---------------------------------------- betid = 11   
                    if(total_goals_half > total_goals_second):
                        highest_scoring_half_first  += 1
                    elif(total_goals_half == total_goals_second):
                        highest_scoring_half_draw   += 1
                    elif(total_goals_half < total_goals_second):
                        highest_scoring_half_second += 1
                    ## ---------------------------------------- betid = 7 
                    if(score_halftime_home > score_halftime_away and 
                       score_secondtime_home == score_secondtime_away):
                        htft_double_home_draw += 1
                    elif(score_halftime_home > score_halftime_away and 
                         score_secondtime_home < score_secondtime_away):
                        htft_double_home_away += 1
                    # -----------------------------------------
                    elif(score_halftime_home == score_halftime_away and 
                         score_secondtime_home < score_secondtime_away):
                        htft_double_draw_away += 1
                    elif(score_halftime_home == score_halftime_away and 
                         score_secondtime_home == score_secondtime_away):
                        htft_double_draw_draw += 1
                    # -----------------------------------------
                    elif(score_halftime_home > score_halftime_away and 
                         score_secondtime_home > score_secondtime_away):
                        htft_double_home_home += 1
                    elif(score_halftime_home == score_halftime_away and 
                         score_secondtime_home > score_secondtime_away):
                        htft_double_draw_home += 1
                    # -----------------------------------------
                    elif(score_halftime_home < score_halftime_away and 
                         score_secondtime_home > score_secondtime_away):
                        htft_double_away_home += 1
                    elif(score_halftime_home < score_halftime_away and 
                         score_secondtime_home == score_secondtime_away):
                        htft_double_away_draw += 1
                    elif(score_halftime_home < score_halftime_away and 
                         score_secondtime_home < score_secondtime_away):
                        htft_double_away_away += 1
                    ## ---------------------------------------- betid = 20 
                    if(score_halftime_home >= score_halftime_away):
                        double_chance__first_half_home_draw += 1 
                    elif(score_halftime_home != score_halftime_away):
                        double_chance__first_half_home_away += 1
                    elif(score_halftime_home <= score_halftime_away):
                        double_chance__first_half_draw_away += 1
                    ## ---------------------------------------- betid = 46 
                    if(total_goals_half == 0):
                        exact_goals_number__first_half_0 += 1
                    elif(total_goals_half == 1):
                        exact_goals_number__first_half_1 += 1
                    elif(total_goals_half == 2):
                        exact_goals_number__first_half_2 += 1
                    elif(total_goals_half == 3):
                        exact_goals_number__first_half_3 += 1
                    elif(total_goals_half == 4):
                        exact_goals_number__first_half_4 += 1
                    elif(total_goals_half >= 5):
                        exact_goals_number__first_half_more_5 += 1  
                    ## ---------------------------------------- betid = 42
                    if(total_goals_second == 0):
                        second_half_exact_goals_number_0 += 1
                    elif(total_goals_second == 1):
                        second_half_exact_goals_number_1 += 1
                    elif(total_goals_second == 2):
                        second_half_exact_goals_number_2 += 1
                    elif(total_goals_second == 3):
                        second_half_exact_goals_number_3 += 1
                    elif(total_goals_second == 4):
                        second_half_exact_goals_number_4 += 1
                    elif(total_goals_second >= 5):
                        second_half_exact_goals_number_more_5 += 1  
                    ## ---------------------------------------- betid = 73
                    if(btts_first_sts == 'yes' and btts_second_sts == 'yes'):
                        both_teams_to_score_1st_half__2nd_half_yes_yes += 1
                    elif(btts_first_sts == 'yes' and btts_second_sts == 'no'):
                        both_teams_to_score_1st_half__2nd_half_yes_no += 1
                    elif(btts_first_sts == 'no' and btts_second_sts == 'yes'):
                        both_teams_to_score_1st_half__2nd_half_no_yes += 1
                    elif(btts_first_sts == 'no' and btts_second_sts == 'no'):
                        both_teams_to_score_1st_half__2nd_half_no_no += 1
                    ## ---------------------------------------- betid = 13
                    if(score_halftime_home > score_halftime_away):
                        first_half_winner_home += 1  
                    elif(score_halftime_home == score_halftime_away):
                        first_half_winner_draw += 1
                    elif(score_halftime_home < score_halftime_away):
                        first_half_winner_away += 1
                    ## ---------------------------------------- betid = 3
                    if(score_secondtime_home > score_secondtime_away):
                        second_half_winner_home += 1  
                    elif(score_secondtime_home == score_secondtime_away):
                        second_half_winner_draw += 1
                    elif(score_secondtime_home < score_secondtime_away):
                        second_half_winner_away += 1
                    ## ---------------------------------------- betid = 19
                    if(score_halftime_home > score_halftime_away):
                        asian_handicap_first_half_home_plus_0 = 0 
                    if(score_halftime_home < score_halftime_away):
                        asian_handicap_first_half_away_plus_0 = 0
                    ## ----------------------------------------
                    if(score_halftime_home + 0.5 > score_halftime_away):
                        asian_handicap_first_half_home_plus_05 = 0
                    if(score_halftime_home + 0.5 < score_halftime_away):
                        asian_handicap_first_half_away_min_05 = 0
                    ## ----------------------------------------
                    if(score_halftime_home + 1  > score_halftime_away):
                        asian_handicap_first_half_home_plus_1 = 0
                    if(score_halftime_home + 1  < score_halftime_away):
                        asian_handicap_first_half_away_min_1 = 0
                    ## ----------------------------------------
                    if(score_halftime_home + 1.5 > score_halftime_away):
                        asian_handicap_first_half_home_plus_15 = 0
                    if(score_halftime_home + 1.5 < score_halftime_away):
                        asian_handicap_first_half_away_min_15 = 0 
                    ## ----------------------------------------
                    if(score_halftime_home - 0.5 > score_halftime_away):
                        asian_handicap_first_half_home_min_05 = 0
                    if(score_halftime_home - 0.5 < score_halftime_away):
                        asian_handicap_first_half_away_plus_05 = 0
                    ## ----------------------------------------
                    if(score_halftime_home - 1 > score_halftime_away):
                        asian_handicap_first_half_home_min_1 = 0
                    if(score_halftime_home - 1 < score_halftime_away):
                        asian_handicap_first_half_away_plus_1 = 0
                    ## ----------------------------------------
                    if(score_halftime_home - 1.5 > score_halftime_away):
                        asian_handicap_first_half_home_min_15 = 0
                    if(score_halftime_home - 1.5 < score_halftime_away):
                        asian_handicap_first_half_away_plus_15 = 0
                    ## ---------------------------------------- betid = 6
                    if(total_goals_half > 0):
                        goals_overunder_first_half_over_05  += 1
                    if(total_goals_half < 1):
                        goals_overunder_first_half_under_05 += 1
                    ## ----------------------------------------
                    if(total_goals_half > 1):
                        goals_overunder_first_half_over_15  += 1
                    if(total_goals_half < 2):
                        goals_overunder_first_half_under_15 += 1
                    ## ----------------------------------------
                    if(total_goals_half > 2):
                        goals_overunder_first_half_over_25  += 1
                    if(total_goals_half < 3):
                        goals_overunder_first_half_under_25 += 1
                    ## ----------------------------------------
                    if(total_goals_half > 3):
                        goals_overunder_first_half_over_35  += 1
                    if(total_goals_half < 4):
                        goals_overunder_first_half_under_35 += 1 
                    ## ---------------------------------------- betid = 13
                    if(score_halftime_home > score_halftime_away):
                        first_half_winner_home += 1  
                    elif(score_halftime_home == score_halftime_away):
                        first_half_winner_draw += 1
                    elif(score_halftime_home < score_halftime_away):
                        first_half_winner_away += 1
                    ## ---------------------------------------- betid = 3
                    if(score_secondtime_home > score_secondtime_away):
                        second_half_winner_home += 1  
                    elif(score_secondtime_home == score_secondtime_away):
                        second_half_winner_draw += 1
                    elif(score_secondtime_home < score_secondtime_away):
                        second_half_winner_away += 1 
                # ----------------------------------------------
            # --------------------------------------------------
            # --------------------------------------------------
            query = " UPDATE `pattern_lists` SET "

            # 1 	Match Winner
            # 2 	Home/Away
            # 3 	Second Half Winner
            # 4 	Asian Handicap
            # 5 	Goals Over/Under
            # 6 	Goals Over/Under First Half
            # 7 	HT/FT Double
            # 8 	Both Teams Score
            # 11 	Highest Scoring Half
            # 12 	Double Chance
            # 13 	First Half Winner
            # 19 	Asian Handicap First Half
            # 20 	Double Chance - First Half
            # 21 	Odd/Even
            # 24 	Results/Both Teams Score
            # 25 	Result/Total Goals
            # 26 	Goals Over/Under - Second Half
            # 27 	Clean Sheet - Home
            # 28 	Clean Sheet - Away
            # 32 	Win Both Halves
            # 34 	Both Teams Score - First Half
            # 35 	Both Teams To Score - Second Half
            # 36 	Win To Nil
            # 38 	Exact Goals Number
            # 39 	To Win Either Half
            # 40 	Home Team Exact Goals Number
            # 41 	Away Team Exact Goals Number
            # 42 	Second Half Exact Goals Number
            # 46 	Exact Goals Number - First Half
            # 48 	To Score In Both Halves By Teams
            # 49 	Total Goals/Both Teams To Score
            # 52 	Halftime Result/Both Teams Score
            # 55 	Corners 1x2
            # 73 	Both Teams to Score 1st Half - 2nd Half
            # 74 	10 Over/Under
            # 79 	Cards European Handicap
            # 86 	RCARD
            # -------------------------------------------------- 
            query += " `halftime_result_both_teams_score_away_yes_data`='"+str(halftime_result_both_teams_score_away_yes)+"', "
            query += " `halftime_result_both_teams_score_away_no_data`='"+str(halftime_result_both_teams_score_away_no)+"', " 
            # --------------------------------------------------
            query += " `halftime_result_both_teams_score_away_yes_perc`='"+str(halftime_result_both_teams_score_away_yes / pattern_total_ff * 100)+"', "
            query += " `halftime_result_both_teams_score_away_no_perc`='"+str(halftime_result_both_teams_score_away_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `halftime_result_both_teams_score_draw_yes_data`='"+str(halftime_result_both_teams_score_draw_yes)+"', "
            query += " `halftime_result_both_teams_score_draw_no_data`='"+str(halftime_result_both_teams_score_draw_no)+"', " 
            # --------------------------------------------------
            query += " `halftime_result_both_teams_score_draw_yes_perc`='"+str(halftime_result_both_teams_score_draw_yes / pattern_total_ff * 100)+"', "
            query += " `halftime_result_both_teams_score_draw_no_perc`='"+str(halftime_result_both_teams_score_draw_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `halftime_result_both_teams_score_home_yes_data`='"+str(halftime_result_both_teams_score_home_yes)+"', "
            query += " `halftime_result_both_teams_score_home_no_data`='"+str(halftime_result_both_teams_score_home_no)+"', " 
            # --------------------------------------------------
            query += " `halftime_result_both_teams_score_home_yes_perc`='"+str(halftime_result_both_teams_score_home_yes / pattern_total_ff * 100)+"', "
            query += " `halftime_result_both_teams_score_home_no_perc`='"+str(halftime_result_both_teams_score_home_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `result_total_goals_draw_over_25_data`='"+str(result_total_goals_draw_over_25)+"', "
            query += " `result_total_goals_draw_over_35_data`='"+str(result_total_goals_draw_over_35)+"', " 
            query += " `result_total_goals_draw_under_35_data`='"+str(result_total_goals_draw_under_35)+"', " 
            query += " `result_total_goals_draw_under_25_data`='"+str(result_total_goals_draw_under_25)+"', " 
            # --------------------------------------------------
            query += " `result_total_goals_draw_over_25_perc`='"+str(result_total_goals_draw_over_25 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_draw_over_35_perc`='"+str(result_total_goals_draw_over_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_draw_under_35_perc`='"+str(result_total_goals_draw_under_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_draw_under_25_perc`='"+str(result_total_goals_draw_under_25 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `result_total_goals_away_over_25_data`='"+str(result_total_goals_away_over_25)+"', "
            query += " `result_total_goals_away_over_35_data`='"+str(result_total_goals_away_over_35)+"', " 
            query += " `result_total_goals_away_under_35_data`='"+str(result_total_goals_away_under_35)+"', " 
            query += " `result_total_goals_away_under_25_data`='"+str(result_total_goals_away_under_25)+"', " 
            # --------------------------------------------------
            query += " `result_total_goals_away_over_25_perc`='"+str(result_total_goals_away_over_25 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_away_over_35_perc`='"+str(result_total_goals_away_over_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_away_under_35_perc`='"+str(result_total_goals_away_under_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_away_under_25_perc`='"+str(result_total_goals_away_under_25 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `result_total_goals_home_over_25_data`='"+str(result_total_goals_home_over_25)+"', "
            query += " `result_total_goals_home_over_35_data`='"+str(result_total_goals_home_over_35)+"', " 
            query += " `result_total_goals_home_under_35_data`='"+str(result_total_goals_home_under_35)+"', " 
            query += " `result_total_goals_home_under_25_data`='"+str(result_total_goals_home_under_25)+"', " 
            # --------------------------------------------------
            query += " `result_total_goals_home_over_25_perc`='"+str(result_total_goals_home_over_25 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_home_over_35_perc`='"+str(result_total_goals_home_over_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_home_under_35_perc`='"+str(result_total_goals_home_under_35 / pattern_total_ff * 100)+"', "
            query += " `result_total_goals_home_under_25_perc`='"+str(result_total_goals_home_under_25 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `double_chance__first_half_home_draw_data`='"+str(double_chance__first_half_home_draw)+"', "
            query += " `double_chance__first_half_home_away_data`='"+str(double_chance__first_half_home_away)+"', " 
            query += " `double_chance__first_half_draw_away_data`='"+str(double_chance__first_half_draw_away)+"', " 
            # --------------------------------------------------
            query += " `double_chance__first_half_home_draw_perc`='"+str(double_chance__first_half_home_draw / pattern_total_ff * 100)+"', "
            query += " `double_chance__first_half_home_away_perc`='"+str(double_chance__first_half_home_away / pattern_total_ff * 100)+"', "
            query += " `double_chance__first_half_draw_away_perc`='"+str(double_chance__first_half_draw_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `htft_double_home_draw_data`='"+str(htft_double_home_draw)+"', "
            query += " `htft_double_home_away_data`='"+str(htft_double_home_away)+"', "
            # --------------------------------------------------
            query += " `htft_double_draw_away_data`='"+str(htft_double_draw_away)+"', " 
            query += " `htft_double_draw_draw_data`='"+str(htft_double_draw_draw)+"', " 
            # --------------------------------------------------
            query += " `htft_double_home_home_data`='"+str(htft_double_home_home)+"', " 
            query += " `htft_double_draw_home_data`='"+str(htft_double_draw_home)+"', " 
            # --------------------------------------------------
            query += " `htft_double_away_home_data`='"+str(htft_double_away_home)+"', " 
            query += " `htft_double_away_draw_data`='"+str(htft_double_away_draw)+"', " 
            query += " `htft_double_away_away_data`='"+str(htft_double_away_away)+"', " 
            # --------------------------------------------------
            query += " `htft_double_home_draw_perc`='"+str(htft_double_home_draw / pattern_total_ff * 100)+"', "
            query += " `htft_double_home_away_perc`='"+str(htft_double_home_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `htft_double_draw_away_perc`='"+str(htft_double_draw_away / pattern_total_ff * 100)+"', "
            query += " `htft_double_draw_draw_perc`='"+str(htft_double_draw_draw / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `htft_double_home_home_perc`='"+str(htft_double_home_home / pattern_total_ff * 100)+"', "
            query += " `htft_double_draw_home_perc`='"+str(htft_double_draw_home / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `htft_double_away_home_perc`='"+str(htft_double_away_home / pattern_total_ff * 100)+"', "
            query += " `htft_double_away_draw_perc`='"+str(htft_double_away_draw / pattern_total_ff * 100)+"', "
            query += " `htft_double_away_away_perc`='"+str(htft_double_away_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `highest_scoring_half_first_data`='"+str(highest_scoring_half_first)+"', "
            query += " `highest_scoring_half_draw_data`='"+str(highest_scoring_half_draw)+"', " 
            query += " `highest_scoring_half_second_data`='"+str(highest_scoring_half_second)+"', " 
            # --------------------------------------------------
            query += " `highest_scoring_half_first_perc`='"+str(highest_scoring_half_first / pattern_total_ff * 100)+"', "
            query += " `highest_scoring_half_draw_perc`='"+str(highest_scoring_half_draw / pattern_total_ff * 100)+"', "
            query += " `highest_scoring_half_second_perc`='"+str(highest_scoring_half_second / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `to_score_in_both_halves_by_teams_home_data`='"+str(to_score_in_both_halves_by_teams_home)+"', "
            query += " `to_score_in_both_halves_by_teams_away_data`='"+str(to_score_in_both_halves_by_teams_away)+"', " 
            # --------------------------------------------------
            query += " `to_score_in_both_halves_by_teams_home_perc`='"+str(to_score_in_both_halves_by_teams_home / pattern_total_ff * 100)+"', "
            query += " `to_score_in_both_halves_by_teams_away_perc`='"+str(to_score_in_both_halves_by_teams_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `win_both_halves_home_data`='"+str(win_both_halves_home)+"', "
            query += " `win_both_halves_away_data`='"+str(win_both_halves_away)+"', " 
            # --------------------------------------------------
            query += " `win_both_halves_home_perc`='"+str(win_both_halves_home / pattern_total_ff * 100)+"', "
            query += " `win_both_halves_away_perc`='"+str(win_both_halves_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `to_win_either_half_home_data`='"+str(to_win_either_half_home)+"', "
            query += " `to_win_either_half_away_data`='"+str(to_win_either_half_away)+"', " 
            # --------------------------------------------------
            query += " `to_win_either_half_home_perc`='"+str(to_win_either_half_home / pattern_total_ff * 100)+"', "
            query += " `to_win_either_half_away_perc`='"+str(to_win_either_half_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `win_to_nil_home_data`='"+str(win_to_nil_home)+"', "
            query += " `win_to_nil_away_data`='"+str(win_to_nil_away)+"', " 
            # --------------------------------------------------
            query += " `win_to_nil_home_perc`='"+str(win_to_nil_home / pattern_total_ff * 100)+"', "
            query += " `win_to_nil_away_perc`='"+str(win_to_nil_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `away_team_exact_goals_number_0_data`='"+str(away_team_exact_goals_number_0)+"', "
            query += " `away_team_exact_goals_number_1_data`='"+str(away_team_exact_goals_number_1)+"', " 
            query += " `away_team_exact_goals_number_2_data`='"+str(away_team_exact_goals_number_2)+"', " 
            query += " `away_team_exact_goals_number_more_3_data`='"+str(away_team_exact_goals_number_more_3)+"', " 
            # --------------------------------------------------
            query += " `away_team_exact_goals_number_0_perc`='"+str(away_team_exact_goals_number_0 / pattern_total_ff * 100)+"', "
            query += " `away_team_exact_goals_number_1_perc`='"+str(away_team_exact_goals_number_1 / pattern_total_ff * 100)+"', "
            query += " `away_team_exact_goals_number_2_perc`='"+str(away_team_exact_goals_number_2 / pattern_total_ff * 100)+"', "
            query += " `away_team_exact_goals_number_more_3_perc`='"+str(away_team_exact_goals_number_more_3 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `home_team_exact_goals_number_0_data`='"+str(home_team_exact_goals_number_0)+"', "
            query += " `home_team_exact_goals_number_1_data`='"+str(home_team_exact_goals_number_1)+"', " 
            query += " `home_team_exact_goals_number_2_data`='"+str(home_team_exact_goals_number_2)+"', " 
            query += " `home_team_exact_goals_number_more_3_data`='"+str(home_team_exact_goals_number_more_3)+"', " 
            # --------------------------------------------------
            query += " `home_team_exact_goals_number_0_perc`='"+str(home_team_exact_goals_number_0 / pattern_total_ff * 100)+"', "
            query += " `home_team_exact_goals_number_1_perc`='"+str(home_team_exact_goals_number_1 / pattern_total_ff * 100)+"', "
            query += " `home_team_exact_goals_number_2_perc`='"+str(home_team_exact_goals_number_2 / pattern_total_ff * 100)+"', "
            query += " `home_team_exact_goals_number_more_3_perc`='"+str(home_team_exact_goals_number_more_3 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `second_half_exact_goals_number_0_data`='"+str(second_half_exact_goals_number_0)+"', "
            query += " `second_half_exact_goals_number_1_data`='"+str(second_half_exact_goals_number_1)+"', " 
            query += " `second_half_exact_goals_number_2_data`='"+str(second_half_exact_goals_number_2)+"', " 
            query += " `second_half_exact_goals_number_3_data`='"+str(second_half_exact_goals_number_3)+"', " 
            query += " `second_half_exact_goals_number_4_data`='"+str(second_half_exact_goals_number_4)+"', " 
            query += " `second_half_exact_goals_number_more_5_data`='"+str(second_half_exact_goals_number_more_5)+"', " 
            # --------------------------------------------------
            query += " `second_half_exact_goals_number_0_perc`='"+str(second_half_exact_goals_number_0 / pattern_total_ff * 100)+"', "
            query += " `second_half_exact_goals_number_1_perc`='"+str(second_half_exact_goals_number_1 / pattern_total_ff * 100)+"', "
            query += " `second_half_exact_goals_number_2_perc`='"+str(second_half_exact_goals_number_2 / pattern_total_ff * 100)+"', "
            query += " `second_half_exact_goals_number_3_perc`='"+str(second_half_exact_goals_number_3 / pattern_total_ff * 100)+"', "
            query += " `second_half_exact_goals_number_4_perc`='"+str(second_half_exact_goals_number_4 / pattern_total_ff * 100)+"', "
            query += " `second_half_exact_goals_number_more_5_perc`='"+str(second_half_exact_goals_number_more_5 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `exact_goals_number__first_half_0_data`='"+str(exact_goals_number__first_half_0)+"', "
            query += " `exact_goals_number__first_half_1_data`='"+str(exact_goals_number__first_half_1)+"', " 
            query += " `exact_goals_number__first_half_2_data`='"+str(exact_goals_number__first_half_2)+"', " 
            query += " `exact_goals_number__first_half_3_data`='"+str(exact_goals_number__first_half_3)+"', " 
            query += " `exact_goals_number__first_half_4_data`='"+str(exact_goals_number__first_half_4)+"', " 
            query += " `exact_goals_number__first_half_more_5_data`='"+str(exact_goals_number__first_half_more_5)+"', " 
            # --------------------------------------------------
            query += " `exact_goals_number__first_half_0_perc`='"+str(exact_goals_number__first_half_0 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number__first_half_1_perc`='"+str(exact_goals_number__first_half_1 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number__first_half_2_perc`='"+str(exact_goals_number__first_half_2 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number__first_half_3_perc`='"+str(exact_goals_number__first_half_3 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number__first_half_4_perc`='"+str(exact_goals_number__first_half_4 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number__first_half_more_5_perc`='"+str(exact_goals_number__first_half_more_5 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `exact_goals_number_0_data`='"+str(exact_goals_number_0)+"', "
            query += " `exact_goals_number_1_data`='"+str(exact_goals_number_1)+"', " 
            query += " `exact_goals_number_2_data`='"+str(exact_goals_number_2)+"', " 
            query += " `exact_goals_number_3_data`='"+str(exact_goals_number_3)+"', " 
            query += " `exact_goals_number_4_data`='"+str(exact_goals_number_4)+"', " 
            query += " `exact_goals_number_5_data`='"+str(exact_goals_number_5)+"', " 
            query += " `exact_goals_number_6_data`='"+str(exact_goals_number_6)+"', " 
            query += " `exact_goals_number_more_7_data`='"+str(exact_goals_number_more_7)+"', " 
            # --------------------------------------------------
            query += " `exact_goals_number_0_perc`='"+str(exact_goals_number_0 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_1_perc`='"+str(exact_goals_number_1 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_2_perc`='"+str(exact_goals_number_2 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_3_perc`='"+str(exact_goals_number_3 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_4_perc`='"+str(exact_goals_number_4 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_5_perc`='"+str(exact_goals_number_5 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_6_perc`='"+str(exact_goals_number_6 / pattern_total_ff * 100)+"', "
            query += " `exact_goals_number_more_7_perc`='"+str(exact_goals_number_more_7 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `clean_sheet__home_yes_data`='"+str(clean_sheet__home_yes)+"', "
            query += " `clean_sheet__home_no_data`='"+str(clean_sheet__home_no)+"', " 
            # --------------------------------------------------
            query += " `clean_sheet__home_yes_perc`='"+str(clean_sheet__home_yes / pattern_total_ff * 100)+"', "
            query += " `clean_sheet__home_no_perc`='"+str(clean_sheet__home_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `clean_sheet__away_yes_data`='"+str(clean_sheet__away_yes)+"', "
            query += " `clean_sheet__away_no_data`='"+str(clean_sheet__away_no)+"', " 
            # --------------------------------------------------
            query += " `clean_sheet__away_yes_perc`='"+str(clean_sheet__away_yes / pattern_total_ff * 100)+"', "
            query += " `clean_sheet__away_no_perc`='"+str(clean_sheet__away_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `both_teams_to_score_1st_half__2nd_half_no_yes_data`='"+str(both_teams_to_score_1st_half__2nd_half_no_yes)+"', "
            query += " `both_teams_to_score_1st_half__2nd_half_no_no_data`='"+str(both_teams_to_score_1st_half__2nd_half_no_no)+"', "
            # --------------------------------------------------
            query += " `both_teams_to_score_1st_half__2nd_half_no_yes_perc`='"+str(both_teams_to_score_1st_half__2nd_half_no_yes / pattern_total_ff * 100)+"', "
            query += " `both_teams_to_score_1st_half__2nd_half_no_no_perc`='"+str(both_teams_to_score_1st_half__2nd_half_no_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `both_teams_to_score_1st_half__2nd_half_yes_yes_data`='"+str(both_teams_to_score_1st_half__2nd_half_yes_yes)+"', "
            query += " `both_teams_to_score_1st_half__2nd_half_yes_no_data`='"+str(both_teams_to_score_1st_half__2nd_half_yes_no)+"', "
            # --------------------------------------------------
            query += " `both_teams_to_score_1st_half__2nd_half_yes_yes_perc`='"+str(both_teams_to_score_1st_half__2nd_half_yes_yes / pattern_total_ff * 100)+"', "
            query += " `both_teams_to_score_1st_half__2nd_half_yes_no_perc`='"+str(both_teams_to_score_1st_half__2nd_half_yes_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `total_goals_both_teams_to_score_over_no_25_data`='"+str(total_goals_both_teams_to_score_over_no_25)+"', "
            query += " `total_goals_both_teams_to_score_under_no_25_data`='"+str(total_goals_both_teams_to_score_under_no_25)+"', " 
            # --------------------------------------------------
            query += " `total_goals_both_teams_to_score_over_no_25_perc`='"+str(total_goals_both_teams_to_score_over_no_25 / pattern_total_ff * 100)+"', "
            query += " `total_goals_both_teams_to_score_under_no_25_perc`='"+str(total_goals_both_teams_to_score_under_no_25 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `total_goals_both_teams_to_score_over_yes_25_data`='"+str(total_goals_both_teams_to_score_over_yes_25)+"', "
            query += " `total_goals_both_teams_to_score_under_yes_25_data`='"+str(total_goals_both_teams_to_score_under_yes_25)+"', " 
            # --------------------------------------------------
            query += " `total_goals_both_teams_to_score_over_yes_25_perc`='"+str(total_goals_both_teams_to_score_over_yes_25 / pattern_total_ff * 100)+"', "
            query += " `total_goals_both_teams_to_score_under_yes_25_perc`='"+str(total_goals_both_teams_to_score_under_yes_25 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_05_data`='"+str(goals_overunder_first_half_over_05)+"', "
            query += " `goals_overunder_first_half_under_05_data`='"+str(goals_overunder_first_half_under_05)+"', " 
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_05_perc`='"+str(goals_overunder_first_half_over_05 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_first_half_under_05_perc`='"+str(goals_overunder_first_half_under_05 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_15_data`='"+str(goals_overunder_first_half_over_15)+"', "
            query += " `goals_overunder_first_half_under_15_data`='"+str(goals_overunder_first_half_under_15)+"', " 
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_15_perc`='"+str(goals_overunder_first_half_over_15 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_first_half_under_15_perc`='"+str(goals_overunder_first_half_under_15 / pattern_total_ff * 100)+"', "  
            # -------------------------------------------------- 
            query += " `goals_overunder_first_half_over_25_data`='"+str(goals_overunder_first_half_over_25)+"', "
            query += " `goals_overunder_first_half_under_25_data`='"+str(goals_overunder_first_half_under_25)+"', " 
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_25_perc`='"+str(goals_overunder_first_half_over_25 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_first_half_under_25_perc`='"+str(goals_overunder_first_half_under_25 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_35_data`='"+str(goals_overunder_first_half_over_35)+"', "
            query += " `goals_overunder_first_half_under_35_data`='"+str(goals_overunder_first_half_under_35)+"', " 
            # --------------------------------------------------
            query += " `goals_overunder_first_half_over_35_perc`='"+str(goals_overunder_first_half_over_35 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_first_half_under_35_perc`='"+str(goals_overunder_first_half_under_35 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_min_15_data`='"+str(asian_handicap_first_half_home_min_15)+"', "
            query += " `asian_handicap_first_half_away_min_15_data`='"+str(asian_handicap_first_half_away_min_15)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_min_15_perc`='"+str(asian_handicap_first_half_home_min_15 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_min_15_perc`='"+str(asian_handicap_first_half_away_min_15 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------   
            query += " `asian_handicap_first_half_home_plus_15_data`='"+str(asian_handicap_first_half_home_plus_15)+"', "
            query += " `asian_handicap_first_half_away_plus_15_data`='"+str(asian_handicap_first_half_away_plus_15)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_15_perc`='"+str(asian_handicap_first_half_home_plus_15 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_plus_15_perc`='"+str(asian_handicap_first_half_away_plus_15 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_05_data`='"+str(asian_handicap_first_half_home_plus_05)+"', "
            query += " `asian_handicap_first_half_away_plus_05_data`='"+str(asian_handicap_first_half_away_plus_05)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_05_perc`='"+str(asian_handicap_first_half_home_plus_05 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_plus_05_perc`='"+str(asian_handicap_first_half_away_plus_05 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_min_1_data`='"+str(asian_handicap_first_half_home_min_1)+"', "
            query += " `asian_handicap_first_half_away_min_1_data`='"+str(asian_handicap_first_half_away_min_1)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_min_1_perc`='"+str(asian_handicap_first_half_home_min_1 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_min_1_perc`='"+str(asian_handicap_first_half_away_min_1 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------   
            query += " `asian_handicap_first_half_home_plus_1_data`='"+str(asian_handicap_first_half_home_plus_1)+"', "
            query += " `asian_handicap_first_half_away_plus_1_data`='"+str(asian_handicap_first_half_away_plus_1)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_1_perc`='"+str(asian_handicap_first_half_home_plus_1 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_plus_1_perc`='"+str(asian_handicap_first_half_away_plus_1 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_0_data`='"+str(asian_handicap_first_half_home_plus_0)+"', "
            query += " `asian_handicap_first_half_away_plus_0_data`='"+str(asian_handicap_first_half_away_plus_0)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_first_half_home_plus_0_perc`='"+str(asian_handicap_first_half_home_plus_0 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_first_half_away_plus_0_perc`='"+str(asian_handicap_first_half_away_plus_0 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `second_half_winner_home_data`='"+str(second_half_winner_home)+"', "
            query += " `second_half_winner_draw_data`='"+str(second_half_winner_draw)+"', "
            query += " `second_half_winner_away_data`='"+str(second_half_winner_away)+"', "
            # --------------------------------------------------
            query += " `second_half_winner_home_perc`='"+str(second_half_winner_home / pattern_total_ff * 100)+"', "
            query += " `second_half_winner_draw_perc`='"+str(second_half_winner_draw / pattern_total_ff * 100)+"', "
            query += " `second_half_winner_away_perc`='"+str(second_half_winner_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `first_half_winner_home_data`='"+str(first_half_winner_home)+"', "
            query += " `first_half_winner_draw_data`='"+str(first_half_winner_draw)+"', "
            query += " `first_half_winner_away_data`='"+str(first_half_winner_away)+"', "
            # --------------------------------------------------
            query += " `first_half_winner_home_perc`='"+str(first_half_winner_home / pattern_total_ff * 100)+"', "
            query += " `first_half_winner_draw_perc`='"+str(first_half_winner_draw / pattern_total_ff * 100)+"', "
            query += " `first_half_winner_away_perc`='"+str(first_half_winner_away / pattern_total_ff * 100)+"', "
            # -------------------------------------------------- 
            query += " `oddeven_even_data`='"+str(oddeven_even)+"', "
            query += " `oddeven_odd_data`='"+str(oddeven_odd)+"', " 
            # --------------------------------------------------
            query += " `oddeven_even_perc`='"+str(oddeven_even / pattern_total_ff * 100)+"', "
            query += " `oddeven_odd_perc`='"+str(oddeven_odd / pattern_total_ff * 100)+"', "  
            # -------------------------------------------------- 
            query += " `match_winner_home_data`='"+str(match_winner_home)+"', "
            query += " `match_winner_draw_data`='"+str(match_winner_draw)+"', "
            query += " `match_winner_away_data`='"+str(match_winner_away)+"', "
            # --------------------------------------------------
            query += " `match_winner_home_perc`='"+str(match_winner_home / pattern_total_ff * 100)+"', "
            query += " `match_winner_draw_perc`='"+str(match_winner_draw / pattern_total_ff * 100)+"', "
            query += " `match_winner_away_perc`='"+str(match_winner_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `goals_overunder_over_05_data`='"+str(goals_overunder_over_05)+"', "
            query += " `goals_overunder_under_05_data`='"+str(goals_overunder_under_05)+"', " 
            query += " `goals_overunder_over_15_data`='"+str(goals_overunder_over_15)+"', "
            query += " `goals_overunder_under_15_data`='"+str(goals_overunder_under_15)+"', " 
            query += " `goals_overunder_over_25_data`='"+str(goals_overunder_over_25)+"', "
            query += " `goals_overunder_under_25_data`='"+str(goals_overunder_under_25)+"', " 
            query += " `goals_overunder_over_35_data`='"+str(goals_overunder_over_35)+"', "
            query += " `goals_overunder_under_35_data`='"+str(goals_overunder_under_35)+"', " 
            query += " `goals_overunder_over_45_data`='"+str(goals_overunder_over_45)+"', "
            query += " `goals_overunder_under_45_data`='"+str(goals_overunder_under_45)+"', " 
            query += " `goals_overunder_over_55_data`='"+str(goals_overunder_over_55)+"', "
            query += " `goals_overunder_under_55_data`='"+str(goals_overunder_under_55)+"', "
            # --------------------------------------------------
            query += " `goals_overunder_over_05_perc`='"+str(goals_overunder_over_05 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_05_perc`='"+str(goals_overunder_under_05 / pattern_total_ff * 100)+"', " 
            query += " `goals_overunder_over_15_perc`='"+str(goals_overunder_over_15 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_15_perc`='"+str(goals_overunder_under_15 / pattern_total_ff * 100)+"', " 
            query += " `goals_overunder_over_25_perc`='"+str(goals_overunder_over_25 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_25_perc`='"+str(goals_overunder_under_25 / pattern_total_ff * 100)+"', " 
            query += " `goals_overunder_over_35_perc`='"+str(goals_overunder_over_35 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_35_perc`='"+str(goals_overunder_under_35 / pattern_total_ff * 100)+"', " 
            query += " `goals_overunder_over_45_perc`='"+str(goals_overunder_over_45 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_45_perc`='"+str(goals_overunder_under_45 / pattern_total_ff * 100)+"', " 
            query += " `goals_overunder_over_55_perc`='"+str(goals_overunder_over_55 / pattern_total_ff * 100)+"', "
            query += " `goals_overunder_under_55_perc`='"+str(goals_overunder_under_55 / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `both_teams_score_yes_data`='"+str(both_teams_score_yes)+"', "
            query += " `both_teams_score_no_data`='"+str(both_teams_score_no)+"', "
            # --------------------------------------------------
            query += " `both_teams_score_yes_perc`='"+str(both_teams_score_yes / pattern_total_ff * 100)+"', "
            query += " `both_teams_score_no_perc`='"+str(both_teams_score_no / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `double_chance_home_draw_data`='"+str(double_chance_home_draw)+"', "
            query += " `double_chance_home_away_data`='"+str(double_chance_home_away)+"', "
            query += " `double_chance_draw_away_data`='"+str(double_chance_draw_away)+"', "
            # --------------------------------------------------
            query += " `double_chance_home_draw_perc`='"+str(double_chance_home_draw / pattern_total_ff * 100)+"', "
            query += " `double_chance_home_away_perc`='"+str(double_chance_home_away / pattern_total_ff * 100)+"', "
            query += " `double_chance_draw_away_perc`='"+str(double_chance_draw_away / pattern_total_ff * 100)+"', "
            # --------------------------------------------------
            query += " `homeaway_home_data`='"+str(homeaway_home)+"', "
            query += " `homeaway_away_data`='"+str(homeaway_away)+"', " 
            # --------------------------------------------------
            query += " `homeaway_home_perc`='"+str(homeaway_home / pattern_total_ff * 100)+"', "
            query += " `homeaway_away_perc`='"+str(homeaway_away / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_0_data`='"+str(asian_handicap_home_plus_0)+"', "
            query += " `asian_handicap_away_plus_0_data`='"+str(asian_handicap_away_plus_0)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_0_perc`='"+str(asian_handicap_home_plus_0 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_0_perc`='"+str(asian_handicap_away_plus_0 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_1_data`='"+str(asian_handicap_home_plus_1)+"', "
            query += " `asian_handicap_away_plus_1_data`='"+str(asian_handicap_away_plus_1)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_1_perc`='"+str(asian_handicap_home_plus_1 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_1_perc`='"+str(asian_handicap_away_plus_1 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_2_data`='"+str(asian_handicap_home_plus_2)+"', "
            query += " `asian_handicap_away_plus_2_data`='"+str(asian_handicap_away_plus_2)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_2_perc`='"+str(asian_handicap_home_plus_2 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_2_perc`='"+str(asian_handicap_away_plus_2 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_3_data`='"+str(asian_handicap_home_plus_3)+"', "
            query += " `asian_handicap_away_plus_3_data`='"+str(asian_handicap_away_plus_3)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_3_perc`='"+str(asian_handicap_home_plus_3 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_3_perc`='"+str(asian_handicap_away_plus_3 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_4_data`='"+str(asian_handicap_home_plus_4)+"', "
            query += " `asian_handicap_away_plus_4_data`='"+str(asian_handicap_away_plus_4)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_4_perc`='"+str(asian_handicap_home_plus_4 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_4_perc`='"+str(asian_handicap_away_plus_4 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_5_data`='"+str(asian_handicap_home_plus_5)+"', "
            query += " `asian_handicap_away_plus_5_data`='"+str(asian_handicap_away_plus_5)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_5_perc`='"+str(asian_handicap_home_plus_5 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_5_perc`='"+str(asian_handicap_away_plus_5 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_6_data`='"+str(asian_handicap_home_plus_6)+"', "
            query += " `asian_handicap_away_plus_6_data`='"+str(asian_handicap_away_plus_6)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_6_perc`='"+str(asian_handicap_home_plus_6 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_6_perc`='"+str(asian_handicap_away_plus_6 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_1_data`='"+str(asian_handicap_home_min_1)+"', "
            query += " `asian_handicap_away_min_1_data`='"+str(asian_handicap_away_min_1)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_1_perc`='"+str(asian_handicap_home_min_1 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_1_perc`='"+str(asian_handicap_away_min_1 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_2_data`='"+str(asian_handicap_home_min_2)+"', "
            query += " `asian_handicap_away_min_2_data`='"+str(asian_handicap_away_min_2)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_2_perc`='"+str(asian_handicap_home_min_2 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_2_perc`='"+str(asian_handicap_away_min_2 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_3_data`='"+str(asian_handicap_home_min_3)+"', "
            query += " `asian_handicap_away_min_3_data`='"+str(asian_handicap_away_min_3)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_3_perc`='"+str(asian_handicap_home_min_3 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_3_perc`='"+str(asian_handicap_away_min_3 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_4_data`='"+str(asian_handicap_home_min_4)+"', "
            query += " `asian_handicap_away_min_4_data`='"+str(asian_handicap_away_min_4)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_4_perc`='"+str(asian_handicap_home_min_4 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_4_perc`='"+str(asian_handicap_away_min_4 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_5_data`='"+str(asian_handicap_home_min_5)+"', "
            query += " `asian_handicap_away_min_5_data`='"+str(asian_handicap_away_min_5)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_5_perc`='"+str(asian_handicap_home_min_5 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_5_perc`='"+str(asian_handicap_away_min_5 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_6_data`='"+str(asian_handicap_home_min_6)+"', "
            query += " `asian_handicap_away_min_6_data`='"+str(asian_handicap_away_min_6)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_6_perc`='"+str(asian_handicap_home_min_6 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_6_perc`='"+str(asian_handicap_away_min_6 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_05_data`='"+str(asian_handicap_home_plus_05)+"', "
            query += " `asian_handicap_away_plus_05_data`='"+str(asian_handicap_away_plus_05)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_05_perc`='"+str(asian_handicap_home_plus_05 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_05_perc`='"+str(asian_handicap_away_plus_05 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_15_data`='"+str(asian_handicap_home_plus_15)+"', "
            query += " `asian_handicap_away_plus_15_data`='"+str(asian_handicap_away_plus_15)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_15_perc`='"+str(asian_handicap_home_plus_15 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_15_perc`='"+str(asian_handicap_away_plus_15 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_25_data`='"+str(asian_handicap_home_plus_25)+"', "
            query += " `asian_handicap_away_plus_25_data`='"+str(asian_handicap_away_plus_25)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_25_perc`='"+str(asian_handicap_home_plus_25 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_25_perc`='"+str(asian_handicap_away_plus_25 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_35_data`='"+str(asian_handicap_home_plus_35)+"', "
            query += " `asian_handicap_away_plus_35_data`='"+str(asian_handicap_away_plus_35)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_35_perc`='"+str(asian_handicap_home_plus_35 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_35_perc`='"+str(asian_handicap_away_plus_35 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_45_data`='"+str(asian_handicap_home_plus_45)+"', "
            query += " `asian_handicap_away_plus_45_data`='"+str(asian_handicap_away_plus_45)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_45_perc`='"+str(asian_handicap_home_plus_45 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_45_perc`='"+str(asian_handicap_away_plus_45 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_55_data`='"+str(asian_handicap_home_plus_55)+"', "
            query += " `asian_handicap_away_plus_55_data`='"+str(asian_handicap_away_plus_55)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_55_perc`='"+str(asian_handicap_home_plus_55 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_55_perc`='"+str(asian_handicap_away_plus_55 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_65_data`='"+str(asian_handicap_home_plus_65)+"', "
            query += " `asian_handicap_away_plus_65_data`='"+str(asian_handicap_away_plus_65)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_plus_65_perc`='"+str(asian_handicap_home_plus_65 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_plus_65_perc`='"+str(asian_handicap_away_plus_65 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_15_data`='"+str(asian_handicap_home_min_15)+"', "
            query += " `asian_handicap_away_min_15_data`='"+str(asian_handicap_away_min_15)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_15_perc`='"+str(asian_handicap_home_min_15 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_15_perc`='"+str(asian_handicap_away_min_15 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_25_data`='"+str(asian_handicap_home_min_25)+"', "
            query += " `asian_handicap_away_min_25_data`='"+str(asian_handicap_away_min_25)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_25_perc`='"+str(asian_handicap_home_min_25 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_25_perc`='"+str(asian_handicap_away_min_25 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_35_data`='"+str(asian_handicap_home_min_35)+"', "
            query += " `asian_handicap_away_min_35_data`='"+str(asian_handicap_away_min_35)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_35_perc`='"+str(asian_handicap_home_min_35 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_35_perc`='"+str(asian_handicap_away_min_35 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_45_data`='"+str(asian_handicap_home_min_45)+"', "
            query += " `asian_handicap_away_min_45_data`='"+str(asian_handicap_away_min_45)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_45_perc`='"+str(asian_handicap_home_min_45 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_45_perc`='"+str(asian_handicap_away_min_45 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_55_data`='"+str(asian_handicap_home_min_55)+"', "
            query += " `asian_handicap_away_min_55_data`='"+str(asian_handicap_away_min_55)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_55_perc`='"+str(asian_handicap_home_min_55 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_55_perc`='"+str(asian_handicap_away_min_55 / pattern_total_ff * 100)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_65_data`='"+str(asian_handicap_home_min_65)+"', "
            query += " `asian_handicap_away_min_65_data`='"+str(asian_handicap_away_min_65)+"', " 
            # --------------------------------------------------
            query += " `asian_handicap_home_min_65_perc`='"+str(asian_handicap_home_min_65 / pattern_total_ff * 100)+"', "
            query += " `asian_handicap_away_min_65_perc`='"+str(asian_handicap_away_min_65 / pattern_total_ff * 100)+"', "  
            # --------------------------------------------------
            query += " `total_fixtures`='"+str(pattern_total_ff)+"' "
            # --------------------------------------------------
            query += " where `leagueapi_id` = '"+str(leagueapi_id)+"' "
            # --------------------------------------------------
            query += " and `pre_ah_pattern` = '"+str(pre_ah_pattern)+"' "
            query += " and `pre_gou_pattern` = '"+str(pre_gou_pattern)+"' "
            # --------------------------------------------------
            query += " and `end_ah_pattern` = '"+str(end_ah_pattern)+"' "
            query += " and `end_gou_pattern` = '"+str(end_gou_pattern)+"' "
            # --------------------------------------------------
            # print(space + query)
            mycursor.execute(query)
            mydb.commit()     
            # --------------------------------------------------
            print(space + "    patternlists updated")
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    print(space + "  _>pa_update_tanggal_update_patternlists__")
    # ----------------------------------------------------------
    query = " UPDATE `leagues` SET "
    query += " tanggal_update_patternlists = '"+str(yesterday_ago)+"' "
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    # ----------------------------------------------------------
    mycursor.execute(query)
    mydb.commit()     
    # ----------------------------------------------------------
    print(space + "    leagues updated")
    # ----------------------------------------------------------