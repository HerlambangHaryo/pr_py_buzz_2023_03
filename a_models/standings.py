# Import
import mysql.connector  
from a_models.api_fixtures import *  


def st_get_team_rank(leagueapi_id, season, today, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "st_get_team_rank()")
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = "Select   "   
    query += " teamapi_id " 
    query += " , name " 
    query += " , points " 
    query += " , goals_substract " 
    query += " from standings " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' "   
    query += " order by points DESC, goals_substract DESC  "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)), flush=True) 
    total_rows = len(result)
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------    
    for x in result:     
        # ------------------------------------------------------
        counter        += 1
        teamapi_id   = str(x[0])  
        name   = str(x[1])  
        points   = str(x[2])  
        goals_substract   = str(x[3])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + teamapi_id + " - "
        word += name + " - "
        word += points + "pts - "
        word += goals_substract + "gs "
        print(word, flush=True)   
        # ------------------------------------------------------  
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------ 
        # ------------------------------------------------------   
        update = " UPDATE `standings` SET  "
        # ------------------------------------------------------  
        update += " `rank` = '"+str(counter)+"', "
        update += " `updated_data_at` = current_timestamp "
        # ------------------------------------------------------
        update += " WHERE teamapi_id = '"+str(teamapi_id)+"' " 
        # ------------------------------------------------------  
        update += " AND leagueapi_id = '"+str(leagueapi_id)+"' "    
        update += " AND season = '"+str(season)+"' "   
        # ------------------------------------------------------  
        # print(space + update)
        mycursor.execute(update)
        mydb.commit()      
        print(space + "> standing rank UPDATED")   
    # ----------------------------------------------------------    

def st_get_team_barely_updated(leagueapi_id, season, today, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "st_get_team_barely_updated()")
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = "Select teamapi_id, name, Date(updated_data_at) "   
    query += " from standings " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' "  
    query += " and DATE(updated_data_at) != '"+str(today)+"' "   
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)), flush=True) 
    total_rows = len(result)
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------    
    for x in result:     
        # ------------------------------------------------------
        counter        += 1
        teams_id   = str(x[0])  
        name   = str(x[1])  
        updated_data_at   = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + teams_id + " - "
        word += updated_data_at
        print(word, flush=True)   
        # ------------------------------------------------------
        st_update_standing(leagueapi_id, season, teams_id, name, space)
    # ----------------------------------------------------------    


def st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teamapi_id, status_match, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "st_get_team_update_stats()")
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

    query += " goals_avg_per_match, " 
    query += " goals_for_ratio, " 
    query += " goals_againts_ratio, " 
    
    query += " form_win_streak_counter, "   
    query += " form_unbeatable_counter, "  
    query += " form_defeatable_counter, "  

    query += " form_win_streak, "   
    query += " form_unbeatable, "  
    query += " form_defeatable, "  

    query += " rank "  

    query += " from standings " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' "  
    query += " and teamapi_id = '"+str(teamapi_id)+"' "   
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)), flush=True) 
    total_rows = len(result)
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    if(total_rows > 0):
        # ------------------------------------------------------
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            goals_avg_per_match   = str(x[0]) 
            goals_for_ratio    = str(x[1]) 
            goals_againts_ratio = str(x[2])  

            form_win_streak_counter         = x[3]  
            form_unbeatable_counter         = x[4] 
            form_defeatable_counter         = x[5] 

            form_win_streak         = x[6]  
            form_unbeatable         = x[7] 
            form_defeatable         = x[8] 

            rank         = x[9] 
            # -------------------------------------------------- 
        # ------------------------------------------------------    
        if(form_win_streak_counter is not None and form_win_streak_counter > 1 ): 
            fx_status = form_win_streak
        elif(form_unbeatable_counter is not None and form_unbeatable_counter > 2 ): 
            fx_status = form_unbeatable
        elif(form_defeatable_counter is not None and form_defeatable_counter > 2 ): 
            fx_status = form_defeatable
        else:
            fx_status = ''
        # ------------------------------------------------------  
                
        update = " UPDATE `football_fixtures` SET  " 
        # ------------------------------------------------------  
        if(status_match == 'home'): 
            update += " `goals_avg_per_match_home` = '"+str(goals_avg_per_match)+"', "
            update += " `goals_for_home_ratio` = '"+str(goals_for_ratio)+"', "
            update += " `goals_againts_home_ratio` = '"+str(goals_againts_ratio)+"', "
            update += " `rank_home` = '"+str(rank)+"', "
            update += " `home_fx_status` = '"+str(fx_status)+"' " 
            
            update += " WHERE teams_home_id = '"+str(teamapi_id)+"' " 
        elif(status_match == 'away'):
            update += " `goals_avg_per_match_away` = '"+str(goals_avg_per_match)+"', "
            update += " `goals_for_away_ratio` = '"+str(goals_for_ratio)+"', "
            update += " `goals_againts_away_ratio` = '"+str(goals_againts_ratio)+"', "
            update += " `rank_away` = '"+str(rank)+"', "
            update += " `away_fx_status` = '"+str(fx_status)+"' "

            update += " WHERE teams_away_id = '"+str(teamapi_id)+"' " 
        # ------------------------------------------------------  
        update += " AND leagueapi_id = '"+str(leagueapi_id)+"' "    
        update += " AND season = '"+str(season)+"' "  
        update += " AND fixtureapi_id = '"+str(fixtureapi_id)+"' "  
        # ------------------------------------------------------  
        print(space + update)
        mycursor.execute(update)
        mydb.commit()      
        print(space + "> football_fixture STATS UPDATED")
    # ---------------------------------------------------------- 

def st_update_standing(leagueapi_id, season, teams_id, name, space):
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------   
    print(space + "st_update_standing()")
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " ( "
    query += " Select "  
    query += " teams_home_id as team_id, "  
    query += " teams_home as name, "  
    query += " 'home' as status, "  
    query += " goals_home, "  
    query += " goals_away, "  
    query += " date, "  
    # ----------------------------------------------------------  
    query += " score_halftime_home, "
    query += " score_halftime_away, "

    query += " score_fulltime_home, "
    query += " score_fulltime_away, "

    query += " score_extratime_home, "
    query += " score_extratime_away, "

    query += " score_penalty_home, "
    query += " score_penalty_away, "

    query += " lineups_coach_home_name, "
    query += " lineups_coach_away_name, "

    query += " lineups_coach_home_photo, "
    query += " lineups_coach_away_photo, "

    query += " lineups_formation_home, "
    query += " lineups_formation_away, "

    query += " shots_on_goal_home, "
    query += " shots_on_goal_away, "

    query += " shots_off_goal_home, "
    query += " shots_off_goal_away, "

    query += " total_shots_home, "
    query += " total_shots_away, "

    query += " blocked_shots_home, "
    query += " blocked_shots_away, "

    query += " shots_inside_box_home, "
    query += " shots_inside_box_away, "

    query += " shots_outside_box_home, "
    query += " shots_outside_box_away, "

    query += " fouls_home, "
    query += " fouls_away, "

    query += " corner_kicks_home, "
    query += " corner_kicks_away, "

    query += " offsides_home, "
    query += " offsides_away, "

    query += " ball_possession_home, "
    query += " ball_possession_away, "

    query += " yellow_cards_home, "
    query += " yellow_cards_away, "

    query += " red_cards_home, "
    query += " red_cards_away, "

    query += " goalkeeper_saves_home, "
    query += " goalkeeper_saves_away, "

    query += " total_passess_home, "
    query += " total_passess_away, "

    query += " passess_accurate_home, "
    query += " passess_accurate_away, "

    query += " passess_home, "
    query += " passess_away, "
    # ----------------------------------------------------------  
    query += " fixtureapi_id "   
    
    query += " from football_fixtures "  

    if(int(leagueapi_id) in [2, 3, 848]):
        query += " where leagueapi_id IN (2, 3, 848) "   
    else:
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  

    query += " and season = '"+str(season)+"' "  
    query += " and teams_home_id = '"+str(teams_id)+"' "  
    query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') "  
    query += " ) "  

    query += " union all "  

    query += " ( "  
    query += " Select "  
    query += " teams_away_id as team_id, "  
    query += " teams_away as name, "  
    query += " 'away' as status, "  
    query += " goals_home, "  
    query += " goals_away, "   
    query += " date, "  
    # ----------------------------------------------------------  
    query += " score_halftime_home, "
    query += " score_halftime_away, "

    query += " score_fulltime_home, "
    query += " score_fulltime_away, "

    query += " score_extratime_home, "
    query += " score_extratime_away, "

    query += " score_penalty_home, "
    query += " score_penalty_away, "

    query += " lineups_coach_home_name, "
    query += " lineups_coach_away_name, "

    query += " lineups_coach_home_photo, "
    query += " lineups_coach_away_photo, "

    query += " lineups_formation_home, "
    query += " lineups_formation_away, "

    query += " shots_on_goal_home, "
    query += " shots_on_goal_away, "

    query += " shots_off_goal_home, "
    query += " shots_off_goal_away, "

    query += " total_shots_home, "
    query += " total_shots_away, "

    query += " blocked_shots_home, "
    query += " blocked_shots_away, "

    query += " shots_inside_box_home, "
    query += " shots_inside_box_away, "

    query += " shots_outside_box_home, "
    query += " shots_outside_box_away, "

    query += " fouls_home, "
    query += " fouls_away, "

    query += " corner_kicks_home, "
    query += " corner_kicks_away, "

    query += " offsides_home, "
    query += " offsides_away, "

    query += " ball_possession_home, "
    query += " ball_possession_away, "

    query += " yellow_cards_home, "
    query += " yellow_cards_away, "

    query += " red_cards_home, "
    query += " red_cards_away, "

    query += " goalkeeper_saves_home, "
    query += " goalkeeper_saves_away, "

    query += " total_passess_home, "
    query += " total_passess_away, "

    query += " passess_accurate_home, "
    query += " passess_accurate_away, "

    query += " passess_home, "
    query += " passess_away, "
    # ----------------------------------------------------------  
    query += " fixtureapi_id " 
    
    query += " from football_fixtures "  

    if(int(leagueapi_id) in [2,3,848]):
        query += " where leagueapi_id IN (2,3,848) "   
    else:
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  

    query += " and season = '"+str(season)+"' "  
    query += " and teams_away_id = '"+str(teams_id)+"' " 
    query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') " 
    query += " ) "      
    query += " order by date asc "
    # ----------------------------------------------------------    
    # print(space + query)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    counter = 0
    # ----------------------------------------------------------
    response_length = len(myresult) 
    # ----------------------------------------------------------
    print(space + "> Total Row(s) : " + str(response_length) ) 
    # ----------------------------------------------------------
    # ------------------------------------------------------   
    if(response_length > 0):
        match_played = 0
        match_played_home = 0
        match_played_away = 0
        goals_total = 0
        win = 0
        draw = 0 
        lose = 0
        points = 0
        # ------------------------------------------------------  
        goals_for = 0
        goals_againts = 0
        goals_substract = 0
        # ------------------------------------------------------  
        form_total = ''
        form_win_streak = ''
        form_unbeatable = ''
        form_defeatable = ''
        # ------------------------------------------------------  
        form_win_streak_counter = 0
        form_unbeatable_counter = 0
        form_defeatable_counter = 0
        # ------------------------------------------------------  
        form_total_home = ''
        form_total_away = '' 
        # ------------------------------------------------------  
        form_win_streak_home = ''
        form_win_streak_home_counter = 0
        form_unbeatable_home = ''
        form_unbeatable_home_counter = 0
        form_defeatable_home = ''
        form_defeatable_home_counter = 0
        # ------------------------------------------------------  
        form_win_streak_away = ''
        form_win_streak_away_counter = 0
        form_unbeatable_away = ''
        form_unbeatable_away_counter = 0
        form_defeatable_away = ''
        form_defeatable_away_counter = 0
        # ------------------------------------------------------  
        goals_for_home = 0
        goals_for_away = 0
        goals_againts_home = 0
        goals_againts_away = 0 
        # ------------------------------------------------------
        counter_col = 0
        # ------------------------------------------------------   
        for x in myresult:   
            # --------------------------------------------------
            teamapi_id   = x[counter_col]

            counter_col += 1
            name         = x[counter_col] 

            counter_col += 1
            status       = x[counter_col] 
            
            counter_col += 1
            goals_home   = x[counter_col] 
            
            counter_col += 1
            goals_away   = x[counter_col] 
            
            counter_col += 1
            date   = x[counter_col] 
             
            counter_col += 1
            score_halftime_home = x[counter_col]

            counter_col += 1
            score_halftime_away = x[counter_col]

            counter_col += 1
            score_fulltime_home = x[counter_col]

            counter_col += 1
            score_fulltime_away = x[counter_col]

            counter_col += 1
            score_extratime_home = x[counter_col]

            counter_col += 1
            score_extratime_away = x[counter_col]

            counter_col += 1
            score_penalty_home = x[counter_col]

            counter_col += 1
            score_penalty_away = x[counter_col]

            counter_col += 1
            lineups_coach_home_name = x[counter_col]

            counter_col += 1
            lineups_coach_away_name = x[counter_col]

            counter_col += 1
            lineups_coach_home_photo = x[counter_col]

            counter_col += 1
            lineups_coach_away_photo = x[counter_col]

            counter_col += 1
            lineups_formation_home = x[counter_col]

            counter_col += 1
            lineups_formation_away = x[counter_col]

            counter_col += 1
            shots_on_goal_home = x[counter_col]

            counter_col += 1
            shots_on_goal_away = x[counter_col]

            counter_col += 1
            shots_off_goal_home = x[counter_col]

            counter_col += 1
            shots_off_goal_away = x[counter_col]

            counter_col += 1
            total_shots_home = x[counter_col]

            counter_col += 1
            total_shots_away = x[counter_col]

            counter_col += 1
            blocked_shots_home = x[counter_col]

            counter_col += 1
            blocked_shots_away = x[counter_col]

            counter_col += 1
            shots_inside_box_home = x[counter_col]

            counter_col += 1
            shots_inside_box_away = x[counter_col]

            counter_col += 1
            shots_outside_box_home = x[counter_col]

            counter_col += 1
            shots_outside_box_away = x[counter_col]

            counter_col += 1
            fouls_home = x[counter_col]

            counter_col += 1
            fouls_away = x[counter_col]

            counter_col += 1
            corner_kicks_home = x[counter_col]

            counter_col += 1
            corner_kicks_away = x[counter_col]

            counter_col += 1
            offsides_home = x[counter_col]

            counter_col += 1
            offsides_away = x[counter_col]

            counter_col += 1
            ball_possession_home = x[counter_col]

            counter_col += 1
            ball_possession_away = x[counter_col]

            counter_col += 1
            yellow_cards_home = x[counter_col]

            counter_col += 1
            yellow_cards_away = x[counter_col]

            counter_col += 1
            red_cards_home = x[counter_col]

            counter_col += 1
            red_cards_away = x[counter_col]

            counter_col += 1
            goalkeeper_saves_home = x[counter_col]

            counter_col += 1
            goalkeeper_saves_away = x[counter_col]

            counter_col += 1
            total_passess_home = x[counter_col]

            counter_col += 1
            total_passess_away = x[counter_col]

            counter_col += 1
            passess_accurate_home = x[counter_col]

            counter_col += 1
            passess_accurate_away = x[counter_col]

            counter_col += 1
            passess_home = x[counter_col] 

            counter_col += 1
            passess_away = x[counter_col]

            counter_col += 1
            fixtureapi_id   = x[counter_col] 
            # --------------------------------------------------
            word = space + "#" + str(fixtureapi_id) 
            print(word)
            # --------------------------------------------------
            if(goals_home is None):
                # af_get_active_API_account_single_fixture(fixtureapi_id, space)
                DICT = {
                    "fixtureapi_id" : fixtureapi_id
                }
                af_controll_match_update(DICT, 'fixtureapi_id', space)
                print(space + "RE_STATED") 
                st_update_standing(leagueapi_id, season, teams_id, name, space)
            elif(goals_home is not None):
                # --------------------------------------------------
                goals_total += goals_home + goals_away
                # --------------------------------------------------
                # --------------------------------------------------
                match_played += 1
                # --------------------------------------------------
                if(status == 'home'): 
                    # ----------------------------------------------
                    if(goals_home > goals_away):
                        # ------------------------------------------
                        win += 1
                        points += 3
                        form_total = '<i class="fa-solid fa-house text-success"></i> ' + form_total 
                        form_total_home = '<i class="fa-solid fa-house text-success"></i> ' + form_total_home 
                        # ------------------------------------------
                        form_win_streak = '<i class="fa-solid fa-house text-success"></i> ' + form_win_streak
                        form_win_streak_counter += 1
                        form_win_streak_home = '<i class="fa-solid fa-house text-success"></i> ' + form_win_streak_home
                        form_win_streak_home_counter += 1
                        # ------------------------------------------
                        form_unbeatable = '<i class="fa-solid fa-house text-success"></i> ' + form_unbeatable
                        form_unbeatable_counter += 1
                        form_unbeatable_home = '<i class="fa-solid fa-house text-success"></i> ' + form_unbeatable_home
                        form_unbeatable_home_counter += 1
                        # ------------------------------------------
                        form_defeatable = ''
                        form_defeatable_counter = 0
                        form_defeatable_home = '' 
                        form_defeatable_home_counter = 0
                        # ------------------------------------------
                    # ----------------------------------------------
                    elif(goals_home == goals_away): 
                        # ------------------------------------------
                        draw += 1
                        points += 1
                        form_total = '<i class="fa-solid fa-house text-secondary"></i> ' + form_total 
                        form_total_home = '<i class="fa-solid fa-house text-secondary"></i> ' + form_total_home
                        # ------------------------------------------
                        form_win_streak = ''
                        form_win_streak_counter = 0
                        form_win_streak_home = ''
                        form_win_streak_home_counter = 0
                        # ------------------------------------------
                        form_unbeatable = '<i class="fa-solid fa-house text-secondary"></i> ' + form_unbeatable
                        form_unbeatable_counter += 1
                        form_unbeatable_home = '<i class="fa-solid fa-house text-secondary"></i> ' + form_unbeatable_home
                        form_unbeatable_home_counter += 1
                        # ------------------------------------------
                        form_defeatable = '<i class="fa-solid fa-house text-secondary"></i> ' + form_defeatable
                        form_defeatable_counter = 1
                        form_defeatable_home = '<i class="fa-solid fa-house text-secondary"></i> ' + form_defeatable_home
                        form_defeatable_home_counter += 1 
                        # ------------------------------------------
                    # ----------------------------------------------
                    elif(goals_home < goals_away):
                        # ------------------------------------------
                        lose += 1
                        form_total = '<i class="fa-solid fa-house text-danger"></i> ' + form_total 
                        form_total_home = '<i class="fa-solid fa-house text-danger"></i> ' + form_total_home
                        # ------------------------------------------
                        form_win_streak = ''
                        form_win_streak_counter = 0
                        form_win_streak_home = ''
                        form_win_streak_home_counter = 0
                        # ------------------------------------------
                        form_unbeatable = ''
                        form_unbeatable_counter = 0
                        form_unbeatable_home = '' 
                        form_unbeatable_home_counter = 0
                        # ------------------------------------------
                        form_defeatable = '<i class="fa-solid fa-house text-danger"></i> ' + form_defeatable
                        form_defeatable_counter += 1
                        form_defeatable_home = '<i class="fa-solid fa-house text-danger"></i> ' + form_defeatable_home
                        form_defeatable_home_counter += 1
                        # ------------------------------------------
                    # ---------------------------------------------- 
                    goals_for += goals_home
                    goals_againts += goals_away
                    goals_for_home = goals_home + goals_for_home
                    goals_againts_home = goals_away + goals_againts_home
                    match_played_home += 1 
                    # ----------------------------------------------
                # --------------------------------------------------
                elif(status == 'away'):
                    # ---------------------------------------------- 
                    if(goals_home < goals_away):
                        # ------------------------------------------ 
                        win += 1
                        points += 3
                        form_total = '<i class="fas fa-flag text-success"></i> ' + form_total 
                        form_total_away = '<i class="fas fa-flag text-success"></i> ' + form_total_away 
                        # ------------------------------------------ 
                        form_win_streak = '<i class="fas fa-flag text-success"></i> ' + form_win_streak
                        form_win_streak_counter += 1
                        form_win_streak_away = '<i class="fas fa-flag text-success"></i> ' + form_win_streak_away
                        form_win_streak_away_counter += 1
                        # ------------------------------------------ 
                        form_unbeatable = '<i class="fas fa-flag text-success"></i> ' + form_unbeatable
                        form_unbeatable_counter += 1  
                        form_unbeatable_away = '<i class="fas fa-flag text-success"></i> ' + form_unbeatable_away
                        form_unbeatable_away_counter += 1
                        # ------------------------------------------ 
                        form_defeatable = ''
                        form_defeatable_counter = 0
                        form_defeatable_away = '' 
                        form_defeatable_away_counter = 0
                        # ------------------------------------------
                    # ----------------------------------------------  
                    elif(goals_home == goals_away): 
                        # ------------------------------------------ 
                        draw += 1
                        points += 1
                        form_total = '<i class="fas fa-flag text-secondary"></i> ' + form_total 
                        form_total_away = '<i class="fas fa-flag text-secondary"></i> ' + form_total_away
                        # ------------------------------------------ 
                        form_win_streak = ''
                        form_win_streak_counter = 0
                        form_win_streak_away = ''
                        form_win_streak_away_counter = 0
                        # ------------------------------------------ 
                        form_unbeatable = '<i class="fas fa-flag text-secondary"></i> ' + form_unbeatable
                        form_unbeatable_counter += 1
                        form_unbeatable_away = '<i class="fas fa-flag text-secondary"></i> ' + form_unbeatable_away
                        form_unbeatable_away_counter += 1
                        # ------------------------------------------ 
                        form_defeatable = '<i class="fas fa-flag text-secondary"></i> ' + form_defeatable
                        form_defeatable_counter = 1
                        form_defeatable_away = '<i class="fas fa-flag text-secondary"></i> ' + form_defeatable_away
                        form_defeatable_away_counter += 1
                        # ------------------------------------------ 
                    # ---------------------------------------------- 
                    elif(goals_home > goals_away):
                        # ------------------------------------------ 
                        lose += 1
                        form_total = '<i class="fas fa-flag text-danger"></i> ' + form_total 
                        form_total_away = '<i class="fas fa-flag text-danger"></i> ' + form_total_away
                        # ------------------------------------------ 
                        form_win_streak = ''
                        form_win_streak_counter = 0
                        form_win_streak_away = ''
                        form_win_streak_away_counter = 0
                        # ------------------------------------------ 
                        form_unbeatable = ''
                        form_unbeatable_counter = 0
                        form_unbeatable_away = '' 
                        form_unbeatable_away_counter = 0
                        # ------------------------------------------ 
                        form_defeatable = '<i class="fas fa-flag text-danger"></i> ' + form_defeatable
                        form_defeatable_counter += 1
                        form_defeatable_away = '<i class="fas fa-flag text-danger"></i> ' + form_defeatable_away
                        form_defeatable_away_counter += 1
                        # ------------------------------------------ 
                    # ---------------------------------------------- 
                    goals_againts += goals_home
                    goals_for += goals_away
                    goals_for_away = goals_away + goals_for_away
                    goals_againts_away = goals_home + goals_againts_away
                    match_played_away += 1
                    # ---------------------------------------------- 
                # --------------------------------------------------
            # --------------------------------------------------
            # if(score_halftime_home is not None): 
            #     score_secondtime
            #     if(status == 'home'): 
            #     elif(status == 'away'): 
        # ------------------------------------------------------  
        goals_substract = goals_for - goals_againts
        # ------------------------------------------------------   
        # ------------------------------------------------------ 
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------ 
        # ------------------------------------------------------   
        update = " UPDATE `standings` SET  "
        # ------------------------------------------------------  
        update += " `match_played` = '"+str(match_played)+"', "
        # ------------------------------------------------------  
        update += " `win` = '"+str(win)+"', "
        update += " `draw` = '"+str(draw)+"', "
        update += " `lose` = '"+str(lose)+"', "
        # ------------------------------------------------------  
        update += " `points` = '"+str(points)+"', "
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------  
        update += " `goals_for` = '"+str(goals_for)+"', "
        if(match_played != 0):
            update += " `goals_for_ratio` = '"+str(goals_for / match_played)+"', "
        # ------------------------------------------------------
        update += " `goals_for_home` = '"+str(goals_for_home)+"', "
        goals_for_home_ratio = 0
        if(match_played_home != 0):
            goals_for_home_ratio = goals_for_home / match_played_home
            update += " `goals_for_home_ratio` = '"+str(goals_for_home_ratio)+"', "
        # ------------------------------------------------------
        update += " `goals_for_away` = '"+str(goals_for_away)+"', "
        goals_for_away_ratio = 0
        if(match_played_away != 0):
            goals_for_away_ratio = goals_for_away / match_played_away
            update += " `goals_for_away_ratio` = '"+str(goals_for_away_ratio)+"', " 
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------
        update += " `goals_againts` = '"+str(goals_againts)+"', "
        if(match_played != 0):
            update += " `goals_againts_ratio` = '"+str(goals_againts / match_played)+"', " 
        # ------------------------------------------------------
        update += " `goals_againts_home` = '"+str(goals_againts_home)+"', "
        goals_againts_home_ratio = 0
        if(match_played_home != 0):
            goals_againts_home_ratio = goals_againts_home / match_played_home
            update += " `goals_againts_home_ratio` = '"+str(goals_againts_home_ratio)+"', "
        # ------------------------------------------------------
        update += " `goals_againts_away` = '"+str(goals_againts_away)+"', "
        goals_againts_away_ratio = 0
        if(match_played_away != 0):
            goals_againts_away_ratio = goals_againts_away / match_played_away
            update += " `goals_againts_away_ratio` = '"+str(goals_againts_away_ratio)+"', "
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------
        update += " `goals_substract` = '"+str(goals_substract)+"', " 
        # ------------------------------------------------------
        goals_avg_per_match = 0
        if(match_played != 0):
            goals_avg_per_match = goals_total / match_played
            update += " `goals_avg_per_match` = '"+str(goals_avg_per_match)+"', "
        # ------------------------------------------------------
        # ------------------------------------------------------
        update += " `form_total` = '"+str(form_total)+"', " 
        update += " `form_total_home` = '"+str(form_total_home)+"', " 
        update += " `form_total_away` = '"+str(form_total_away)+"', " 
        # ------------------------------------------------------
        update += " `form_win_streak` = '"+str(form_win_streak)+"', "
        update += " `form_win_streak_counter` = '"+str(form_win_streak_counter)+"', "
        # ------------------------------------------------------
        update += " `form_win_streak_home` = '"+str(form_win_streak_home)+"', "
        update += " `form_win_streak_home_counter` = '"+str(form_win_streak_home_counter)+"', "
        # ------------------------------------------------------
        update += " `form_win_streak_away` = '"+str(form_win_streak_away)+"', "
        update += " `form_win_streak_away_counter` = '"+str(form_win_streak_away_counter)+"', "
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------
        update += " `form_unbeatable` = '"+str(form_unbeatable)+"', "
        update += " `form_unbeatable_counter` = '"+str(form_unbeatable_counter)+"', "
        # ------------------------------------------------------
        update += " `form_unbeatable_home` = '"+str(form_unbeatable_home)+"', "
        update += " `form_unbeatable_home_counter` = '"+str(form_unbeatable_home_counter)+"', "
        # ------------------------------------------------------
        update += " `form_unbeatable_away` = '"+str(form_unbeatable_away)+"', "
        update += " `form_unbeatable_away_counter` = '"+str(form_unbeatable_away_counter)+"', "
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------
        update += " `form_defeatable` = '"+str(form_defeatable)+"', "
        update += " `form_defeatable_counter` = '"+str(form_defeatable_counter)+"', "
        # ------------------------------------------------------
        update += " `form_defeatable_home` = '"+str(form_defeatable_home)+"', "
        update += " `form_defeatable_home_counter` = '"+str(form_defeatable_home_counter)+"', "
        # ------------------------------------------------------
        update += " `form_defeatable_away` = '"+str(form_defeatable_away)+"', "
        update += " `form_defeatable_away_counter` = '"+str(form_defeatable_away_counter)+"', "
        # ------------------------------------------------------
        #  
        # 
        # 
        # 
        #  
        # ------------------------------------------------------
        update += " `form_total_home` = '"+str(form_total_home)+"', " 
        # ------------------------------------------------------
        update += " `form_total_away` = '"+str(form_total_away)+"', " 
        # ------------------------------------------------------
        update += " `updated_data_at` = now() "  
        # ------------------------------------------------------
        update += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
        update += " and season = '"+str(season)+"' "  
        update += " and teamapi_id  = '"+str(teams_id)+"' " 
        # ------------------------------------------------------
        # print(space +  update) 
        mycursor.execute(update)
        mydb.commit()      
        print(space + "> standings UPDATED")
        # ------------------------------------------------------
        # print("") 
        # if(status_match == 'home'):
        #     goals_for_ratio = goals_for_home_ratio
        #     goals_againts_ratio = goals_againts_home_ratio  
        # elif(status_match == 'away'):
        #     goals_for_ratio = goals_for_away_ratio
        #     goals_againts_ratio = goals_againts_away_ratio 
        # ------------------------------------------------------
        if(form_win_streak_counter > 1 ): 
            fx_status = form_win_streak
        elif(form_unbeatable_counter > 2 ): 
            fx_status = form_unbeatable
        elif(form_defeatable_counter > 2 ): 
            fx_status = form_defeatable
        else:
            fx_status = ''

        # ------------------------------------------------------
        # print(space + "day1: " + day1)
        # if(day1 != 'Enddate'):
        #     st_get_team_update_stats(leagueapi_id, season, teams_id, day1, day2, status_match, goals_for_ratio, goals_againts_ratio, goals_avg_per_match, fx_status, space + "  ")
        # ------------------------------------------------------ 
    elif(response_length == 0):
        # ------------------------------------------------------
        print(space + "No Match")
    # ----------------------------------------------------------


def st_check_standings(leagueapi_id, season, space):
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------   
    print(space + "st_check_standings()")
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = " Select * "  
    query += " from standings "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "   
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True)  
    # ---------------------------------------------------------- 
    if(total_rows == 0):
        # ------------------------------------------------------  
        space += "__"
        # ------------------------------------------------------  
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------  
        query = " (Select teams_home_id as teams_id,  "  
        query += " teams_home as name "  
        query += " from football_fixtures "  
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
        query += " and season = '"+str(season)+"'  "  
        query += " group by teams_home_id ) "  
        query += " union all  "  
        query += " ( Select teams_away_id as teams_id, "  
        query += " teams_away as name "  
        query += " from football_fixtures "  
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
        query += " and season = '"+str(season)+"' " 
        query += " group by teams_away_id )  "     
        # ------------------------------------------------------  
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        # ------------------------------------------------------  
        total_rows = len(result)
        print(space + "Total Row(s) : " + str(total_rows), flush=True) 
        # ------------------------------------------------------  
        counter = 0
        # ------------------------------------------------------   
        for x in result:    
            # --------------------------------------------------  
            counter        += 1
            # --------------------------------------------------  
            teams_id    = str(x[0]) 
            name        = str(x[1])  
            # --------------------------------------------------  
            st_check_standing_rows(leagueapi_id, season, teams_id, name, space)
            # --------------------------------------------------   
        # ------------------------------------------------------   
    # ---------------------------------------------------------- 

def st_check_standing_rows(leagueapi_id, season, teamapi_id, name, space):
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------   
    print(space + "st_check_standing_rows()")
    # ----------------------------------------------------------  
    space += "__"
    # ---------------------------------------------------------- 
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query = " Select * "  
    query += " from standings "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "  
    query += " and teamapi_id  = '"+str(teamapi_id)+"' "  
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ---------------------------------------------------------- 
    if(len(myresult) == 0):
        ## insert
        insert = " INSERT INTO `standings`( "
        insert += " `leagueapi_id`, "
        insert += "  `season`, "
        insert += "  `teamapi_id`, "
        insert += "  `name`  "
        insert += " ) VALUES ( "
        insert += "  '"+str(leagueapi_id)+"', "
        insert += "  '"+str(season)+"', "
        insert += "  '"+str(teamapi_id)+"', "
        insert += "  '"+str(name.replace("'", "\\'"))+"' ) "
        mycursor.execute(insert)
        mydb.commit()      
        print(space +  "row_inserted")
    elif(len(myresult) > 0):
        print(space +  "Already-data") 
    # ---------------------------------------------------------- 