# Import
import mysql.connector 
 
def tr_delete_duplicate(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "tr_delete_duplicate()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query_commit = "DELETE t1 FROM api_football_team_reports  t1 "
    query_commit += "INNER JOIN api_football_team_reports  t2 "
    query_commit += "WHERE t1.id < t2.id " 
    # ----------------------------------------------------------   
    query_commit += "AND t1.leagueapi_id = t2.leagueapi_id "
    query_commit += "AND t1.season = t2.season "
    query_commit += "AND t1.fixtureapi_id = t2.fixtureapi_id "
    query_commit += "AND t1.teamapi_id  = t2.teamapi_id  "
    # ----------------------------------------------------------   
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------   
    mycursor.execute(query_commit)
    mydb.commit()   
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------    
    # ----------------------------------------------------------  


def tr_league_group_league_standings(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "tr_league_group_league_standings()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = "Select "
    query += " leagueapi_id "  
    query += " , DATE(league_standing_updated_at) "  
    query += " from football_leagues " 
    query += " where DATE(league_standing_updated_at) >= DATE('"+day1+"') "
    query += " and DATE(league_standing_updated_at) <= DATE('"+day2+"') "  
    query += " order by leagueapi_id asc  "  
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
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        leagueapi_id    = str(x[0])  
        date            = str(x[1])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " __ " + date  
        print(word, flush=True)    
        # ------------------------------------------------------
        tr_football_fixture(day1, day2, leagueapi_id, space)
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  

def tr_football_fixture(day1, day2, leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "tr_football_fixture()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = "Select "
    query += " leagueapi_id "   
    query += " , season "    
    query += " , fixtureapi_id "   
    query += " , date "  
    query += " , teams_homeapi_id "  
    query += " , teams_awayapi_id "  
    query += " from football_fixtures " 
    query += " where DATE(date) >= DATE('"+day1+"') "
    query += " and DATE(date) <= DATE('"+day2+"') "  
    query += " and leagueapi_id = '"+leagueapi_id+"' "  
    query += " order by leagueapi_id asc  "  
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
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        leagueapi_id    = str(x[0])  
        season          = str(x[1])    
        # ------------------------------------------------------
        fixtureapi_id   = str(x[2])  
        date            = str(x[3])    
        # ------------------------------------------------------
        teams_homeapi_id    = str(x[4])  
        teams_awayapi_id    = str(x[5])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        word += " __ " + fixtureapi_id  
        word += " __ " + date
        word += " __ " + teams_homeapi_id
        word += " __ " + teams_awayapi_id
        print(word, flush=True)    
        # ------------------------------------------------------
        tr_league_standings(leagueapi_id, season, fixtureapi_id, date, teams_homeapi_id, space)
        # ------------------------------------------------------
        tr_league_standings(leagueapi_id, season, fixtureapi_id, date, teams_awayapi_id, space)
        # ------------------------------------------------------
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
 
def tr_league_standings(leagueapi_id, season, fixtureapi_id, date, teamapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "tr_league_standings()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = "Select "
    # ----------------------------------------------------------
    query += " rank " 
    query += " , points "
    query += " , goals_diff "
    query += " , group_status "
    query += " , form "
    query += " , long_form "
    query += " , status "
    query += " , description "
    # ----------------------------------------------------------
    query += " , played "
    query += " , win "
    query += " , draw "
    query += " , lose "
    # ----------------------------------------------------------
    query += " , goals_for "
    query += " , goals_againts "
    # ----------------------------------------------------------
    query += " , home_played "
    query += " , home_win "
    query += " , home_draw "
    query += " , home_lose "
    query += " , home_goals_for "
    query += " , home_goals_againts "
    # ----------------------------------------------------------
    query += " , away_played "
    query += " , away_win "
    query += " , away_draw "
    query += " , away_lose "
    query += " , away_goals_for "
    query += " , away_goals_againts "
    # ----------------------------------------------------------
    query += " , home_goals_for_average "
    query += " , away_goals_for_average "
    # ----------------------------------------------------------
    query += " , goals_for_average "
    query += " , home_goals_for_minute_0_15_total "
    query += " , home_goals_for_minute_0_15_percentage "
    query += " , home_goals_for_minute_16_30_total "
    query += " , home_goals_for_minute_16_30_percentage "
    query += " , home_goals_for_minute_31_45_total "
    query += " , home_goals_for_minute_31_45_percentage "
    query += " , home_goals_for_minute_46_60_total "
    query += " , home_goals_for_minute_46_60_percentage "
    query += " , home_goals_for_minute_61_75_total "
    query += " , home_goals_for_minute_61_75_percentage "
    query += " , home_goals_for_minute_76_90_total "
    query += " , home_goals_for_minute_76_90_percentage "
    query += " , home_goals_for_minute_91_105_total "
    query += " , home_goals_for_minute_91_105_percentage "
    query += " , home_goals_for_minute_106_120_total "
    query += " , home_goals_for_minute_106_120_percentage "
    # ----------------------------------------------------------
    query += " , away_goals_for_minute_0_15_total "
    query += " , away_goals_for_minute_0_15_percentage "
    query += " , away_goals_for_minute_16_30_total "
    query += " , away_goals_for_minute_16_30_percentage "
    query += " , away_goals_for_minute_31_45_total "
    query += " , away_goals_for_minute_31_45_percentage "
    query += " , away_goals_for_minute_46_60_total "
    query += " , away_goals_for_minute_46_60_percentage "
    query += " , away_goals_for_minute_61_75_total "
    query += " , away_goals_for_minute_61_75_percentage "
    query += " , away_goals_for_minute_76_90_total "
    query += " , away_goals_for_minute_76_90_percentage "
    query += " , away_goals_for_minute_91_105_total "
    query += " , away_goals_for_minute_91_105_percentage "
    query += " , away_goals_for_minute_106_120_total "
    query += " , away_goals_for_minute_106_120_percentage "
    # ----------------------------------------------------------
    query += " , home_goals_against_average "
    query += " , away_goals_against_average "
    # ----------------------------------------------------------
    query += " , goals_against_average "
    query += " , home_goals_against_minute_0_15_total "
    query += " , home_goals_against_minute_0_15_percentage "
    query += " , home_goals_against_minute_16_30_total "
    query += " , home_goals_against_minute_16_30_percentage "
    query += " , home_goals_against_minute_31_45_total "
    query += " , home_goals_against_minute_31_45_percentage "
    query += " , home_goals_against_minute_46_60_total "
    query += " , home_goals_against_minute_46_60_percentage "
    query += " , home_goals_against_minute_61_75_total "
    query += " , home_goals_against_minute_61_75_percentage "
    query += " , home_goals_against_minute_76_90_total "
    query += " , home_goals_against_minute_76_90_percentage "
    query += " , home_goals_against_minute_91_105_total "
    query += " , home_goals_against_minute_91_105_percentage "
    query += " , home_goals_against_minute_106_120_total "
    query += " , home_goals_against_minute_106_120_percentage "
    query += " , away_goals_against_minute_0_15_total "
    query += " , away_goals_against_minute_0_15_percentage "
    query += " , away_goals_against_minute_16_30_total "
    query += " , away_goals_against_minute_16_30_percentage "
    query += " , away_goals_against_minute_31_45_total "
    query += " , away_goals_against_minute_31_45_percentage "
    query += " , away_goals_against_minute_46_60_total "
    query += " , away_goals_against_minute_46_60_percentage "
    query += " , away_goals_against_minute_61_75_total "
    query += " , away_goals_against_minute_61_75_percentage "
    query += " , away_goals_against_minute_76_90_total "
    query += " , away_goals_against_minute_76_90_percentage "
    query += " , away_goals_against_minute_91_105_total "
    query += " , away_goals_against_minute_91_105_percentage "
    query += " , away_goals_against_minute_106_120_total "
    query += " , away_goals_against_minute_106_120_percentage "
    # ----------------------------------------------------------
    query += " , biggest_streak_wins "
    query += " , biggest_streak_draws "
    query += " , biggest_streak_loses "
    # ----------------------------------------------------------
    query += " , biggest_wins_home "
    query += " , biggest_wins_away "
    # ----------------------------------------------------------
    query += " , biggest_loses_home "
    query += " , biggest_loses_away "
    # ----------------------------------------------------------
    query += " , biggest_goals_for_home "
    query += " , biggest_goals_for_away "
    # ----------------------------------------------------------
    query += " , biggest_goals_against_home "
    query += " , biggest_goals_against_away "
    # ----------------------------------------------------------
    query += " , clean_sheet_home "
    query += " , clean_sheet_away "
    query += " , clean_sheet_total "
    # ----------------------------------------------------------
    query += " , failed_to_score_home "
    query += " , failed_to_score_away "
    query += " , failed_to_score_total "
    # ----------------------------------------------------------
    query += " , penalty_scored_total "
    query += " , penalty_scored_percentage "
    query += " , penalty_missed_total "
    query += " , penalty_missed_percentage "
    query += " , penalty_total "
    # ----------------------------------------------------------
    query += " , cards_yellow_0_15_total "
    query += " , cards_yellow_0_15_percentage "
    query += " , cards_yellow_16_30_total "
    query += " , cards_yellow_16_30_percentage "
    query += " , cards_yellow_31_45_total "
    query += " , cards_yellow_31_45_percentage "
    query += " , cards_yellow_46_60_total "
    query += " , cards_yellow_46_60_percentage "
    query += " , cards_yellow_61_75_total "
    query += " , cards_yellow_61_75_percentage "
    query += " , cards_yellow_76_90_total "
    query += " , cards_yellow_76_90_percentage "
    query += " , cards_yellow_91_105_total "
    query += " , cards_yellow_91_105_percentage "
    query += " , cards_yellow_106_120_total "
    query += " , cards_yellow_106_120_percentage "
    # ----------------------------------------------------------
    query += " , cards_red_0_15_total "
    query += " , cards_red_0_15_percentage "
    query += " , cards_red_16_30_total "
    query += " , cards_red_16_30_percentage "
    query += " , cards_red_31_45_total "
    query += " , cards_red_31_45_percentage "
    query += " , cards_red_46_60_total "
    query += " , cards_red_46_60_percentage "
    query += " , cards_red_61_75_total "
    query += " , cards_red_61_75_percentage "
    query += " , cards_red_76_90_total "
    query += " , cards_red_76_90_percentage "
    query += " , cards_red_91_105_total "
    query += " , cards_red_91_105_percentage "
    query += " , cards_red_106_120_total "
    query += " , cards_red_106_120_percentage "
    # ----------------------------------------------------------
    query += " from api_football_league_standings "  
    # ----------------------------------------------------------
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "   
    query += " and teamapi_id = '"+str(teamapi_id)+"' "    
    # ----------------------------------------------------------
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ---------------------------------------------------------- 
    counter = 0
    counter_col = 0
    # ----------------------------------------------------------   
    for rs1 in result:     
        # ------------------------------------------------------
        counter_col = 0
        rank = rs1[counter_col] 

        counter_col += 1   
        points = rs1[counter_col] 

        counter_col += 1  
        goals_diff = rs1[counter_col] 

        counter_col += 1  
        group_status = rs1[counter_col] 

        counter_col += 1  
        form = rs1[counter_col] 

        counter_col += 1  
        long_form = rs1[counter_col] 

        counter_col += 1  
        status = rs1[counter_col] 

        counter_col += 1  
        description = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        played = rs1[counter_col] 

        counter_col += 1  
        win = rs1[counter_col] 

        counter_col += 1  
        draw = rs1[counter_col] 

        counter_col += 1  
        lose = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        goals_for = rs1[counter_col] 

        counter_col += 1  
        goals_againts = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        home_played = rs1[counter_col] 

        counter_col += 1  
        home_win = rs1[counter_col] 

        counter_col += 1  
        home_draw = rs1[counter_col] 

        counter_col += 1  
        home_lose = rs1[counter_col] 

        counter_col += 1  
        home_goals_for = rs1[counter_col] 

        counter_col += 1  
        home_goals_againts = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        away_played = rs1[counter_col] 

        counter_col += 1  
        away_win = rs1[counter_col] 

        counter_col += 1  
        away_draw = rs1[counter_col] 

        counter_col += 1  
        away_lose = rs1[counter_col] 

        counter_col += 1  
        away_goals_for = rs1[counter_col] 

        counter_col += 1  
        away_goals_againts = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        home_goals_for_average = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_average = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        goals_for_average = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_0_15_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_16_30_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_31_45_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_46_60_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_61_75_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_76_90_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_91_105_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_106_120_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_for_minute_106_120_percentage = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        away_goals_for_minute_0_15_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_16_30_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_31_45_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_46_60_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_61_75_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_76_90_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_91_105_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_106_120_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_for_minute_106_120_percentage = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        home_goals_against_average = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_average = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        goals_against_average = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_0_15_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_16_30_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_31_45_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_46_60_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_61_75_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_76_90_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_91_105_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_106_120_total = rs1[counter_col] 

        counter_col += 1  
        home_goals_against_minute_106_120_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_0_15_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_16_30_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_31_45_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_46_60_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_61_75_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_76_90_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_91_105_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_106_120_total = rs1[counter_col] 

        counter_col += 1  
        away_goals_against_minute_106_120_percentage = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        biggest_streak_wins = rs1[counter_col] 

        counter_col += 1  
        biggest_streak_draws = rs1[counter_col] 

        counter_col += 1  
        biggest_streak_loses = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        biggest_wins_home = rs1[counter_col] 

        counter_col += 1  
        biggest_wins_away = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        biggest_loses_home = rs1[counter_col] 

        counter_col += 1  
        biggest_loses_away = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        biggest_goals_for_home = rs1[counter_col] 

        counter_col += 1  
        biggest_goals_for_away = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        biggest_goals_against_home = rs1[counter_col] 

        counter_col += 1  
        biggest_goals_against_away = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        clean_sheet_home = rs1[counter_col] 

        counter_col += 1  
        clean_sheet_away = rs1[counter_col] 

        counter_col += 1  
        clean_sheet_total = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        failed_to_score_home = rs1[counter_col] 

        counter_col += 1  
        failed_to_score_away = rs1[counter_col] 

        counter_col += 1  
        failed_to_score_total = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        penalty_scored_total = rs1[counter_col] 

        counter_col += 1  
        penalty_scored_percentage = rs1[counter_col] 

        counter_col += 1  
        penalty_missed_total = rs1[counter_col] 

        counter_col += 1  
        penalty_missed_percentage = rs1[counter_col] 

        counter_col += 1  
        penalty_total = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        cards_yellow_0_15_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_16_30_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_31_45_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_46_60_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_61_75_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_76_90_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_91_105_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_106_120_total = rs1[counter_col] 

        counter_col += 1  
        cards_yellow_106_120_percentage = rs1[counter_col] 

        counter_col += 1  
        # ------------------------------------------------------
        cards_red_0_15_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_0_15_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_16_30_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_16_30_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_31_45_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_31_45_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_46_60_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_46_60_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_61_75_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_61_75_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_76_90_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_76_90_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_91_105_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_91_105_percentage = rs1[counter_col] 

        counter_col += 1  
        cards_red_106_120_total = rs1[counter_col] 

        counter_col += 1  
        cards_red_106_120_percentage = rs1[counter_col]  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        word += " __ " + fixtureapi_id  
        word += " __ " + date
        word += " __ " + teamapi_id 
        # ------------------------------------------------------
        print(space + word, flush=True)    
        # ------------------------------------------------------
        update_or_insert = tr_update_or_insert(leagueapi_id, season, fixtureapi_id, teamapi_id, space)
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        print(space + str(update_or_insert), flush=True)    
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------ 
        if(update_or_insert == 1):
            # ---------------------------------- 
            query_commit = "UPDATE `api_football_team_reports` SET "
            # ----------------------------------   
            query_commit += " fixtureapi_id = '"+str(fixtureapi_id)+"', "   
            query_commit += " date = '"+str(date)+"', " 
            # ----------------------------------   
            query_commit += " rank = '"+str(rank)+"', "   
            query_commit += " points = '"+str(points)+"', " 
            query_commit += " goals_diff = '"+str(goals_diff)+"', " 
            query_commit += " group_status = '"+str(group_status)+"', " 
            query_commit += " form = '"+str(form)+"', " 
            query_commit += " long_form = '"+str(long_form)+"', " 
            query_commit += " status = '"+str(status)+"', " 
            query_commit += " description = '"+str(description)+"', " 
            # ----------------------------------
            query_commit += " played = '"+str(played)+"', " 
            query_commit += " win = '"+str(win)+"', " 
            query_commit += " draw = '"+str(draw)+"', " 
            query_commit += " lose = '"+str(lose)+"', " 
            # ----------------------------------
            query_commit += " goals_for = '"+str(goals_for)+"', " 
            query_commit += " goals_againts = '"+str(goals_againts)+"', " 
            # ----------------------------------
            query_commit += " home_played = '"+str(home_played)+"', " 
            query_commit += " home_win = '"+str(home_win)+"', " 
            query_commit += " home_draw = '"+str(home_draw)+"', " 
            query_commit += " home_lose = '"+str(home_lose)+"', " 
            query_commit += " home_goals_for = '"+str(home_goals_for)+"', " 
            query_commit += " home_goals_againts = '"+str(home_goals_againts)+"', " 
            # ----------------------------------
            query_commit += " away_played = '"+str(away_played)+"', " 
            query_commit += " away_win = '"+str(away_win)+"', " 
            query_commit += " away_draw = '"+str(away_draw)+"', " 
            query_commit += " away_lose = '"+str(away_lose)+"', " 
            query_commit += " away_goals_for = '"+str(away_goals_for)+"', " 
            query_commit += " away_goals_againts = '"+str(away_goals_againts)+"', " 
            # ----------------------------------
            query_commit += " home_goals_for_average = '"+str(home_goals_for_average)+"', " 
            query_commit += " away_goals_for_average = '"+str(away_goals_for_average)+"', " 
            # ----------------------------------
            query_commit += " goals_for_average = '"+str(goals_for_average)+"', " 
            query_commit += " home_goals_for_minute_0_15_total = '"+str(home_goals_for_minute_0_15_total)+"', " 
            query_commit += " home_goals_for_minute_0_15_percentage = '"+str(home_goals_for_minute_0_15_percentage)+"', " 
            query_commit += " home_goals_for_minute_16_30_total = '"+str(home_goals_for_minute_16_30_total)+"', " 
            query_commit += " home_goals_for_minute_16_30_percentage = '"+str(home_goals_for_minute_16_30_percentage)+"', " 
            query_commit += " home_goals_for_minute_31_45_total = '"+str(home_goals_for_minute_31_45_total)+"', " 
            query_commit += " home_goals_for_minute_31_45_percentage = '"+str(home_goals_for_minute_31_45_percentage)+"', " 
            query_commit += " home_goals_for_minute_46_60_total = '"+str(home_goals_for_minute_46_60_total)+"', " 
            query_commit += " home_goals_for_minute_46_60_percentage = '"+str(home_goals_for_minute_46_60_percentage)+"', " 
            query_commit += " home_goals_for_minute_61_75_total = '"+str(home_goals_for_minute_61_75_total)+"', " 
            query_commit += " home_goals_for_minute_61_75_percentage = '"+str(home_goals_for_minute_61_75_percentage)+"', " 
            query_commit += " home_goals_for_minute_76_90_total = '"+str(home_goals_for_minute_76_90_total)+"', " 
            query_commit += " home_goals_for_minute_76_90_percentage = '"+str(home_goals_for_minute_76_90_percentage)+"', " 
            query_commit += " home_goals_for_minute_91_105_total = '"+str(home_goals_for_minute_91_105_total)+"', " 
            query_commit += " home_goals_for_minute_91_105_percentage = '"+str(home_goals_for_minute_91_105_percentage)+"', " 
            query_commit += " home_goals_for_minute_106_120_total = '"+str(home_goals_for_minute_106_120_total)+"', " 
            query_commit += " home_goals_for_minute_106_120_percentage = '"+str(home_goals_for_minute_106_120_percentage)+"', " 
            # ----------------------------------
            query_commit += " away_goals_for_minute_0_15_total = '"+str(away_goals_for_minute_0_15_total)+"', " 
            query_commit += " away_goals_for_minute_0_15_percentage = '"+str(away_goals_for_minute_0_15_percentage)+"', " 
            query_commit += " away_goals_for_minute_16_30_total = '"+str(away_goals_for_minute_16_30_total)+"', " 
            query_commit += " away_goals_for_minute_16_30_percentage = '"+str(away_goals_for_minute_16_30_percentage)+"', " 
            query_commit += " away_goals_for_minute_31_45_total = '"+str(away_goals_for_minute_31_45_total)+"', " 
            query_commit += " away_goals_for_minute_31_45_percentage = '"+str(away_goals_for_minute_31_45_percentage)+"', " 
            query_commit += " away_goals_for_minute_46_60_total = '"+str(away_goals_for_minute_46_60_total)+"', " 
            query_commit += " away_goals_for_minute_46_60_percentage = '"+str(away_goals_for_minute_46_60_percentage)+"', " 
            query_commit += " away_goals_for_minute_61_75_total = '"+str(away_goals_for_minute_61_75_total)+"', " 
            query_commit += " away_goals_for_minute_61_75_percentage = '"+str(away_goals_for_minute_61_75_percentage)+"', " 
            query_commit += " away_goals_for_minute_76_90_total = '"+str(away_goals_for_minute_76_90_total)+"', " 
            query_commit += " away_goals_for_minute_76_90_percentage = '"+str(away_goals_for_minute_76_90_percentage)+"', " 
            query_commit += " away_goals_for_minute_91_105_total = '"+str(away_goals_for_minute_91_105_total)+"', " 
            query_commit += " away_goals_for_minute_91_105_percentage = '"+str(away_goals_for_minute_91_105_percentage)+"', " 
            query_commit += " away_goals_for_minute_106_120_total = '"+str(away_goals_for_minute_106_120_total)+"', " 
            query_commit += " away_goals_for_minute_106_120_percentage = '"+str(away_goals_for_minute_106_120_percentage)+"', " 
            # ----------------------------------
            query_commit += " home_goals_against_average = '"+str(home_goals_against_average)+"', " 
            query_commit += " away_goals_against_average = '"+str(away_goals_against_average)+"', " 
            # ----------------------------------
            query_commit += " goals_against_average = '"+str(goals_against_average)+"', " 
            query_commit += " home_goals_against_minute_0_15_total = '"+str(home_goals_against_minute_0_15_total)+"', " 
            query_commit += " home_goals_against_minute_0_15_percentage = '"+str(home_goals_against_minute_0_15_percentage)+"', " 
            query_commit += " home_goals_against_minute_16_30_total = '"+str(home_goals_against_minute_16_30_total)+"', " 
            query_commit += " home_goals_against_minute_16_30_percentage = '"+str(home_goals_against_minute_16_30_percentage)+"', " 
            query_commit += " home_goals_against_minute_31_45_total = '"+str(home_goals_against_minute_31_45_total)+"', " 
            query_commit += " home_goals_against_minute_31_45_percentage = '"+str(home_goals_against_minute_31_45_percentage)+"', " 
            query_commit += " home_goals_against_minute_46_60_total = '"+str(home_goals_against_minute_46_60_total)+"', " 
            query_commit += " home_goals_against_minute_46_60_percentage = '"+str(home_goals_against_minute_46_60_percentage)+"', " 
            query_commit += " home_goals_against_minute_61_75_total = '"+str(home_goals_against_minute_61_75_total)+"', " 
            query_commit += " home_goals_against_minute_61_75_percentage = '"+str(home_goals_against_minute_61_75_percentage)+"', " 
            query_commit += " home_goals_against_minute_76_90_total = '"+str(home_goals_against_minute_76_90_total)+"', " 
            query_commit += " home_goals_against_minute_76_90_percentage = '"+str(home_goals_against_minute_76_90_percentage)+"', " 
            query_commit += " home_goals_against_minute_91_105_total = '"+str(home_goals_against_minute_91_105_total)+"', " 
            query_commit += " home_goals_against_minute_91_105_percentage = '"+str(home_goals_against_minute_91_105_percentage)+"', " 
            query_commit += " home_goals_against_minute_106_120_total = '"+str(home_goals_against_minute_106_120_total)+"', " 
            query_commit += " home_goals_against_minute_106_120_percentage = '"+str(home_goals_against_minute_106_120_percentage)+"', " 
            query_commit += " away_goals_against_minute_0_15_total = '"+str(away_goals_against_minute_0_15_total)+"', " 
            query_commit += " away_goals_against_minute_0_15_percentage = '"+str(away_goals_against_minute_0_15_percentage)+"', " 
            query_commit += " away_goals_against_minute_16_30_total = '"+str(away_goals_against_minute_16_30_total)+"', " 
            query_commit += " away_goals_against_minute_16_30_percentage = '"+str(away_goals_against_minute_16_30_percentage)+"', " 
            query_commit += " away_goals_against_minute_31_45_total = '"+str(away_goals_against_minute_31_45_total)+"', " 
            query_commit += " away_goals_against_minute_31_45_percentage = '"+str(away_goals_against_minute_31_45_percentage)+"', " 
            query_commit += " away_goals_against_minute_46_60_total = '"+str(away_goals_against_minute_46_60_total)+"', " 
            query_commit += " away_goals_against_minute_46_60_percentage = '"+str(away_goals_against_minute_46_60_percentage)+"', " 
            query_commit += " away_goals_against_minute_61_75_total = '"+str(away_goals_against_minute_61_75_total)+"', " 
            query_commit += " away_goals_against_minute_61_75_percentage = '"+str(away_goals_against_minute_61_75_percentage)+"', " 
            query_commit += " away_goals_against_minute_76_90_total = '"+str(away_goals_against_minute_76_90_total)+"', " 
            query_commit += " away_goals_against_minute_76_90_percentage = '"+str(away_goals_against_minute_76_90_percentage)+"', " 
            query_commit += " away_goals_against_minute_91_105_total = '"+str(away_goals_against_minute_91_105_total)+"', " 
            query_commit += " away_goals_against_minute_91_105_percentage = '"+str(away_goals_against_minute_91_105_percentage)+"', " 
            query_commit += " away_goals_against_minute_106_120_total = '"+str(away_goals_against_minute_106_120_total)+"', " 
            query_commit += " away_goals_against_minute_106_120_percentage = '"+str(away_goals_against_minute_106_120_percentage)+"', " 
            # ----------------------------------
            query_commit += " biggest_streak_wins = '"+str(biggest_streak_wins)+"', " 
            query_commit += " biggest_streak_draws = '"+str(biggest_streak_draws)+"', " 
            query_commit += " biggest_streak_loses = '"+str(biggest_streak_loses)+"', " 
            # ----------------------------------
            query_commit += " biggest_wins_home = '"+str(biggest_wins_home)+"', " 
            query_commit += " biggest_wins_away = '"+str(biggest_wins_away)+"', " 
            # ----------------------------------
            query_commit += " biggest_loses_home = '"+str(biggest_loses_home)+"', " 
            query_commit += " biggest_loses_away = '"+str(biggest_loses_away)+"', " 
            # ----------------------------------
            query_commit += " biggest_goals_for_home = '"+str(biggest_goals_for_home)+"', " 
            query_commit += " biggest_goals_for_away = '"+str(biggest_goals_for_away)+"', " 
            # ----------------------------------
            query_commit += " biggest_goals_against_home = '"+str(biggest_goals_against_home)+"', " 
            query_commit += " biggest_goals_against_away = '"+str(biggest_goals_against_away)+"', " 
            # ----------------------------------
            query_commit += " clean_sheet_home = '"+str(clean_sheet_home)+"', " 
            query_commit += " clean_sheet_away = '"+str(clean_sheet_away)+"', " 
            query_commit += " clean_sheet_total = '"+str(clean_sheet_total)+"', " 
            # ----------------------------------
            query_commit += " failed_to_score_home = '"+str(failed_to_score_home)+"', " 
            query_commit += " failed_to_score_away = '"+str(failed_to_score_away)+"', " 
            query_commit += " failed_to_score_total = '"+str(failed_to_score_total)+"', " 
            # ----------------------------------
            query_commit += " penalty_scored_total = '"+str(penalty_scored_total)+"', " 
            query_commit += " penalty_scored_percentage = '"+str(penalty_scored_percentage)+"', " 
            query_commit += " penalty_missed_total = '"+str(penalty_missed_total)+"', " 
            query_commit += " penalty_missed_percentage = '"+str(penalty_missed_percentage)+"', " 
            query_commit += " penalty_total = '"+str(penalty_total)+"', " 
            # ----------------------------------
            query_commit += " cards_yellow_0_15_total = '"+str(cards_yellow_0_15_total)+"', " 
            query_commit += " cards_yellow_0_15_percentage = '"+str(cards_yellow_0_15_percentage)+"', " 
            query_commit += " cards_yellow_16_30_total = '"+str(cards_yellow_16_30_total)+"', " 
            query_commit += " cards_yellow_16_30_percentage = '"+str(cards_yellow_16_30_percentage)+"', " 
            query_commit += " cards_yellow_31_45_total = '"+str(cards_yellow_31_45_total)+"', " 
            query_commit += " cards_yellow_31_45_percentage = '"+str(cards_yellow_31_45_percentage)+"', " 
            query_commit += " cards_yellow_46_60_total = '"+str(cards_yellow_46_60_total)+"', " 
            query_commit += " cards_yellow_46_60_percentage = '"+str(cards_yellow_46_60_percentage)+"', " 
            query_commit += " cards_yellow_61_75_total = '"+str(cards_yellow_61_75_total)+"', " 
            query_commit += " cards_yellow_61_75_percentage = '"+str(cards_yellow_61_75_percentage)+"', " 
            query_commit += " cards_yellow_76_90_total = '"+str(cards_yellow_76_90_total)+"', " 
            query_commit += " cards_yellow_76_90_percentage = '"+str(cards_yellow_76_90_percentage)+"', " 
            query_commit += " cards_yellow_91_105_total = '"+str(cards_yellow_91_105_total)+"', " 
            query_commit += " cards_yellow_91_105_percentage = '"+str(cards_yellow_91_105_percentage)+"', " 
            query_commit += " cards_yellow_106_120_total = '"+str(cards_yellow_106_120_total)+"', " 
            query_commit += " cards_yellow_106_120_percentage = '"+str(cards_yellow_106_120_percentage)+"', " 
            # ----------------------------------
            query_commit += " cards_red_0_15_total = '"+str(cards_red_0_15_total)+"', " 
            query_commit += " cards_red_0_15_percentage = '"+str(cards_red_0_15_percentage)+"', " 
            query_commit += " cards_red_16_30_total = '"+str(cards_red_16_30_total)+"', " 
            query_commit += " cards_red_16_30_percentage = '"+str(cards_red_16_30_percentage)+"', " 
            query_commit += " cards_red_31_45_total = '"+str(cards_red_31_45_total)+"', " 
            query_commit += " cards_red_31_45_percentage = '"+str(cards_red_31_45_percentage)+"', " 
            query_commit += " cards_red_46_60_total = '"+str(cards_red_46_60_total)+"', " 
            query_commit += " cards_red_46_60_percentage = '"+str(cards_red_46_60_percentage)+"', " 
            query_commit += " cards_red_61_75_total = '"+str(cards_red_61_75_total)+"', " 
            query_commit += " cards_red_61_75_percentage = '"+str(cards_red_61_75_percentage)+"', " 
            query_commit += " cards_red_76_90_total = '"+str(cards_red_76_90_total)+"', " 
            query_commit += " cards_red_76_90_percentage = '"+str(cards_red_76_90_percentage)+"', " 
            query_commit += " cards_red_91_105_total = '"+str(cards_red_91_105_total)+"', " 
            query_commit += " cards_red_91_105_percentage = '"+str(cards_red_91_105_percentage)+"', " 
            query_commit += " cards_red_106_120_total = '"+str(cards_red_106_120_total)+"', " 
            query_commit += " cards_red_106_120_percentage = '"+str(cards_red_106_120_percentage)+"' " 
            # ----------------------------------
            query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
            query_commit += " and season = "+str(season)+" "     
            query_commit += " and teamapi_id = "+str(teamapi_id)+" "     
            # ----------------------------------
            print(space + "api_football_team_reports UPDATED", flush=True)  
            # ----------------------------------
            # ----------------------------------
            # ----------------------------------
            # ----------------------------------
            # ----------------------------------
        # --------------------------------------
        elif(update_or_insert == 0):
            # ----------------------------------
            query_commit = "INSERT INTO `api_football_team_reports`( "
            # ----------------------------------   
            query_commit += " `leagueapi_id`, " 
            query_commit += " `season`, "  
            query_commit += " `teamapi_id`, "  
            query_commit += " `fixtureapi_id`, "  
            query_commit += " `date`, "  
            # ----------------------------------
            query_commit += " `rank`, " 
            query_commit += " `points`, " 
            query_commit += " `goals_diff`, " 
            query_commit += " `group_status`, " 
            query_commit += " `form`, " 
            query_commit += " `long_form`, " 
            query_commit += " `status`, " 
            query_commit += " `description`, "
            # ----------------------------------
            query_commit += " `played`, " 
            query_commit += " `win`, " 
            query_commit += " `draw`, " 
            query_commit += " `lose`, "
            # ----------------------------------
            query_commit += " `goals_for`, " 
            query_commit += " `goals_againts`, "
            # ----------------------------------
            query_commit += " `home_played`, " 
            query_commit += " `home_win`, " 
            query_commit += " `home_draw`, " 
            query_commit += " `home_lose`, " 
            query_commit += " `home_goals_for`, " 
            query_commit += " `home_goals_againts`, "
            # ----------------------------------
            query_commit += " `away_played`, " 
            query_commit += " `away_win`, " 
            query_commit += " `away_draw`, " 
            query_commit += " `away_lose`, " 
            query_commit += " `away_goals_for`, " 
            query_commit += " `away_goals_againts`, "
            # ----------------------------------
            query_commit += " `home_goals_for_average`, " 
            query_commit += " `away_goals_for_average`, "
            # ----------------------------------
            query_commit += " `goals_for_average`, " 
            query_commit += " `home_goals_for_minute_0_15_total`, " 
            query_commit += " `home_goals_for_minute_0_15_percentage`, " 
            query_commit += " `home_goals_for_minute_16_30_total`, " 
            query_commit += " `home_goals_for_minute_16_30_percentage`, " 
            query_commit += " `home_goals_for_minute_31_45_total`, " 
            query_commit += " `home_goals_for_minute_31_45_percentage`, " 
            query_commit += " `home_goals_for_minute_46_60_total`, " 
            query_commit += " `home_goals_for_minute_46_60_percentage`, " 
            query_commit += " `home_goals_for_minute_61_75_total`, " 
            query_commit += " `home_goals_for_minute_61_75_percentage`, " 
            query_commit += " `home_goals_for_minute_76_90_total`, " 
            query_commit += " `home_goals_for_minute_76_90_percentage`, " 
            query_commit += " `home_goals_for_minute_91_105_total`, " 
            query_commit += " `home_goals_for_minute_91_105_percentage`, " 
            query_commit += " `home_goals_for_minute_106_120_total`, " 
            query_commit += " `home_goals_for_minute_106_120_percentage`, "
            # ----------------------------------
            query_commit += " `away_goals_for_minute_0_15_total`, " 
            query_commit += " `away_goals_for_minute_0_15_percentage`, " 
            query_commit += " `away_goals_for_minute_16_30_total`, " 
            query_commit += " `away_goals_for_minute_16_30_percentage`, " 
            query_commit += " `away_goals_for_minute_31_45_total`, " 
            query_commit += " `away_goals_for_minute_31_45_percentage`, " 
            query_commit += " `away_goals_for_minute_46_60_total`, " 
            query_commit += " `away_goals_for_minute_46_60_percentage`, " 
            query_commit += " `away_goals_for_minute_61_75_total`, " 
            query_commit += " `away_goals_for_minute_61_75_percentage`, " 
            query_commit += " `away_goals_for_minute_76_90_total`, " 
            query_commit += " `away_goals_for_minute_76_90_percentage`, " 
            query_commit += " `away_goals_for_minute_91_105_total`, " 
            query_commit += " `away_goals_for_minute_91_105_percentage`, " 
            query_commit += " `away_goals_for_minute_106_120_total`, " 
            query_commit += " `away_goals_for_minute_106_120_percentage`, "
            # ----------------------------------
            query_commit += " `home_goals_against_average`, " 
            query_commit += " `away_goals_against_average`, "
            # ----------------------------------
            query_commit += " `goals_against_average`, " 
            query_commit += " `home_goals_against_minute_0_15_total`, " 
            query_commit += " `home_goals_against_minute_0_15_percentage`, " 
            query_commit += " `home_goals_against_minute_16_30_total`, " 
            query_commit += " `home_goals_against_minute_16_30_percentage`, " 
            query_commit += " `home_goals_against_minute_31_45_total`, " 
            query_commit += " `home_goals_against_minute_31_45_percentage`, " 
            query_commit += " `home_goals_against_minute_46_60_total`, " 
            query_commit += " `home_goals_against_minute_46_60_percentage`, " 
            query_commit += " `home_goals_against_minute_61_75_total`, " 
            query_commit += " `home_goals_against_minute_61_75_percentage`, " 
            query_commit += " `home_goals_against_minute_76_90_total`, " 
            query_commit += " `home_goals_against_minute_76_90_percentage`, " 
            query_commit += " `home_goals_against_minute_91_105_total`, " 
            query_commit += " `home_goals_against_minute_91_105_percentage`, " 
            query_commit += " `home_goals_against_minute_106_120_total`, " 
            query_commit += " `home_goals_against_minute_106_120_percentage`, " 
            query_commit += " `away_goals_against_minute_0_15_total`, " 
            query_commit += " `away_goals_against_minute_0_15_percentage`, " 
            query_commit += " `away_goals_against_minute_16_30_total`, " 
            query_commit += " `away_goals_against_minute_16_30_percentage`, " 
            query_commit += " `away_goals_against_minute_31_45_total`, " 
            query_commit += " `away_goals_against_minute_31_45_percentage`, " 
            query_commit += " `away_goals_against_minute_46_60_total`, " 
            query_commit += " `away_goals_against_minute_46_60_percentage`, " 
            query_commit += " `away_goals_against_minute_61_75_total`, " 
            query_commit += " `away_goals_against_minute_61_75_percentage`, " 
            query_commit += " `away_goals_against_minute_76_90_total`, " 
            query_commit += " `away_goals_against_minute_76_90_percentage`, " 
            query_commit += " `away_goals_against_minute_91_105_total`, " 
            query_commit += " `away_goals_against_minute_91_105_percentage`, " 
            query_commit += " `away_goals_against_minute_106_120_total`, " 
            query_commit += " `away_goals_against_minute_106_120_percentage`, "
            # ----------------------------------
            query_commit += " `biggest_streak_wins`, " 
            query_commit += " `biggest_streak_draws`, " 
            query_commit += " `biggest_streak_loses`, "
            # ----------------------------------
            query_commit += " `biggest_wins_home`, " 
            query_commit += " `biggest_wins_away`, "
            # ----------------------------------
            query_commit += " `biggest_loses_home`, " 
            query_commit += " `biggest_loses_away`, "
            # ----------------------------------
            query_commit += " `biggest_goals_for_home`, " 
            query_commit += " `biggest_goals_for_away`, "
            # ----------------------------------
            query_commit += " `biggest_goals_against_home`, " 
            query_commit += " `biggest_goals_against_away`, "
            # ----------------------------------
            query_commit += " `clean_sheet_home`, " 
            query_commit += " `clean_sheet_away`, " 
            query_commit += " `clean_sheet_total`, "
            # ----------------------------------
            query_commit += " `failed_to_score_home`, " 
            query_commit += " `failed_to_score_away`, " 
            query_commit += " `failed_to_score_total`, "
            # ----------------------------------
            query_commit += " `penalty_scored_total`, " 
            query_commit += " `penalty_scored_percentage`, " 
            query_commit += " `penalty_missed_total`, " 
            query_commit += " `penalty_missed_percentage`, " 
            query_commit += " `penalty_total`, "
            # ----------------------------------
            query_commit += " `cards_yellow_0_15_total`, " 
            query_commit += " `cards_yellow_0_15_percentage`, " 
            query_commit += " `cards_yellow_16_30_total`, " 
            query_commit += " `cards_yellow_16_30_percentage`, " 
            query_commit += " `cards_yellow_31_45_total`, " 
            query_commit += " `cards_yellow_31_45_percentage`, " 
            query_commit += " `cards_yellow_46_60_total`, " 
            query_commit += " `cards_yellow_46_60_percentage`, " 
            query_commit += " `cards_yellow_61_75_total`, " 
            query_commit += " `cards_yellow_61_75_percentage`, " 
            query_commit += " `cards_yellow_76_90_total`, " 
            query_commit += " `cards_yellow_76_90_percentage`, " 
            query_commit += " `cards_yellow_91_105_total`, " 
            query_commit += " `cards_yellow_91_105_percentage`, " 
            query_commit += " `cards_yellow_106_120_total`, " 
            query_commit += " `cards_yellow_106_120_percentage`, "
            # ----------------------------------
            query_commit += " `cards_red_0_15_total`, " 
            query_commit += " `cards_red_0_15_percentage`, " 
            query_commit += " `cards_red_16_30_total`, " 
            query_commit += " `cards_red_16_30_percentage`, " 
            query_commit += " `cards_red_31_45_total`, " 
            query_commit += " `cards_red_31_45_percentage`, " 
            query_commit += " `cards_red_46_60_total`, " 
            query_commit += " `cards_red_46_60_percentage`, " 
            query_commit += " `cards_red_61_75_total`, " 
            query_commit += " `cards_red_61_75_percentage`, " 
            query_commit += " `cards_red_76_90_total`, " 
            query_commit += " `cards_red_76_90_percentage`, " 
            query_commit += " `cards_red_91_105_total`, " 
            query_commit += " `cards_red_91_105_percentage`, " 
            query_commit += " `cards_red_106_120_total`, " 
            query_commit += " `cards_red_106_120_percentage`, " 
            # ----------------------------------
            # ---------------------------------- 
            query_commit += " `created_at` "
            # ----------------------------------
            query_commit += " ) VALUES ( " 
            # ----------------------------------
            query_commit += " '" + str(leagueapi_id) + "', " 
            query_commit += " '" + str(season) + "', " 
            query_commit += " '" + str(teamapi_id) + "', " 
            query_commit += " '" + str(fixtureapi_id) + "', " 
            query_commit += " '" + str(date) + "', " 
            # ----------------------------------
            query_commit += " '" + str(rank) + "', " 
            query_commit += " '" + str(points) + "', " 
            query_commit += " '" + str(goals_diff) + "', " 
            query_commit += " '" + str(group_status) + "', " 
            query_commit += " '" + str(form) + "', " 
            query_commit += " '" + str(long_form) + "', " 
            query_commit += " '" + str(status) + "', " 
            query_commit += " '" + str(description) + "', "
            # ----------------------------------
            query_commit += " '" + str(played) + "', " 
            query_commit += " '" + str(win) + "', " 
            query_commit += " '" + str(draw) + "', " 
            query_commit += " '" + str(lose) + "', "
            # -----------------------------------
            query_commit += " '" + str(goals_for) + "', " 
            query_commit += " '" + str(goals_againts) + "', "
            # -----------------------------------
            query_commit += " '" + str(home_played) + "', " 
            query_commit += " '" + str(home_win) + "', " 
            query_commit += " '" + str(home_draw) + "', " 
            query_commit += " '" + str(home_lose) + "', " 
            query_commit += " '" + str(home_goals_for) + "', " 
            query_commit += " '" + str(home_goals_againts) + "', "
            # -----------------------------------
            query_commit += " '" + str(away_played) + "', " 
            query_commit += " '" + str(away_win) + "', " 
            query_commit += " '" + str(away_draw) + "', " 
            query_commit += " '" + str(away_lose) + "', " 
            query_commit += " '" + str(away_goals_for) + "', " 
            query_commit += " '" + str(away_goals_againts) + "', "
            # -----------------------------------
            query_commit += " '" + str(home_goals_for_average) + "', " 
            query_commit += " '" + str(away_goals_for_average) + "', "
            # -----------------------------------
            query_commit += " '" + str(goals_for_average) + "', " 
            query_commit += " '" + str(home_goals_for_minute_0_15_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_0_15_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_16_30_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_16_30_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_31_45_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_31_45_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_46_60_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_46_60_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_61_75_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_61_75_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_76_90_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_76_90_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_91_105_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_91_105_percentage) + "', " 
            query_commit += " '" + str(home_goals_for_minute_106_120_total) + "', " 
            query_commit += " '" + str(home_goals_for_minute_106_120_percentage) + "', "
            # -----------------------------------
            query_commit += " '" + str(away_goals_for_minute_0_15_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_0_15_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_16_30_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_16_30_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_31_45_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_31_45_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_46_60_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_46_60_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_61_75_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_61_75_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_76_90_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_76_90_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_91_105_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_91_105_percentage) + "', " 
            query_commit += " '" + str(away_goals_for_minute_106_120_total) + "', " 
            query_commit += " '" + str(away_goals_for_minute_106_120_percentage) + "', "
            # -----------------------------------
            query_commit += " '" + str(home_goals_against_average) + "', " 
            query_commit += " '" + str(away_goals_against_average) + "', "
            # -----------------------------------
            query_commit += " '" + str(goals_against_average) + "', " 
            query_commit += " '" + str(home_goals_against_minute_0_15_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_0_15_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_16_30_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_16_30_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_31_45_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_31_45_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_46_60_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_46_60_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_61_75_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_61_75_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_76_90_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_76_90_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_91_105_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_91_105_percentage) + "', " 
            query_commit += " '" + str(home_goals_against_minute_106_120_total) + "', " 
            query_commit += " '" + str(home_goals_against_minute_106_120_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_0_15_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_0_15_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_16_30_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_16_30_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_31_45_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_31_45_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_46_60_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_46_60_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_61_75_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_61_75_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_76_90_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_76_90_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_91_105_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_91_105_percentage) + "', " 
            query_commit += " '" + str(away_goals_against_minute_106_120_total) + "', " 
            query_commit += " '" + str(away_goals_against_minute_106_120_percentage) + "', "
            # -----------------------------------
            query_commit += " '" + str(biggest_streak_wins) + "', " 
            query_commit += " '" + str(biggest_streak_draws) + "', " 
            query_commit += " '" + str(biggest_streak_loses) + "', "
            # -----------------------------------
            query_commit += " '" + str(biggest_wins_home) + "', " 
            query_commit += " '" + str(biggest_wins_away) + "', "
            # -----------------------------------
            query_commit += " '" + str(biggest_loses_home) + "', " 
            query_commit += " '" + str(biggest_loses_away) + "', "
            # -----------------------------------
            query_commit += " '" + str(biggest_goals_for_home) + "', " 
            query_commit += " '" + str(biggest_goals_for_away) + "', "
            # -----------------------------------
            query_commit += " '" + str(biggest_goals_against_home) + "', " 
            query_commit += " '" + str(biggest_goals_against_away) + "', "
            # -----------------------------------
            query_commit += " '" + str(clean_sheet_home) + "', " 
            query_commit += " '" + str(clean_sheet_away) + "', " 
            query_commit += " '" + str(clean_sheet_total) + "', "
            # -----------------------------------
            query_commit += " '" + str(failed_to_score_home) + "', " 
            query_commit += " '" + str(failed_to_score_away) + "', " 
            query_commit += " '" + str(failed_to_score_total) + "', "
            # -----------------------------------
            query_commit += " '" + str(penalty_scored_total) + "', " 
            query_commit += " '" + str(penalty_scored_percentage) + "', " 
            query_commit += " '" + str(penalty_missed_total) + "', " 
            query_commit += " '" + str(penalty_missed_percentage) + "', " 
            query_commit += " '" + str(penalty_total) + "', "
            # -----------------------------------
            query_commit += " '" + str(cards_yellow_0_15_total) + "', " 
            query_commit += " '" + str(cards_yellow_0_15_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_16_30_total) + "', " 
            query_commit += " '" + str(cards_yellow_16_30_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_31_45_total) + "', " 
            query_commit += " '" + str(cards_yellow_31_45_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_46_60_total) + "', " 
            query_commit += " '" + str(cards_yellow_46_60_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_61_75_total) + "', " 
            query_commit += " '" + str(cards_yellow_61_75_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_76_90_total) + "', " 
            query_commit += " '" + str(cards_yellow_76_90_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_91_105_total) + "', " 
            query_commit += " '" + str(cards_yellow_91_105_percentage) + "', " 
            query_commit += " '" + str(cards_yellow_106_120_total) + "', " 
            query_commit += " '" + str(cards_yellow_106_120_percentage) + "', "
            # -----------------------------------
            query_commit += " '" + str(cards_red_0_15_total) + "', " 
            query_commit += " '" + str(cards_red_0_15_percentage) + "', " 
            query_commit += " '" + str(cards_red_16_30_total) + "', " 
            query_commit += " '" + str(cards_red_16_30_percentage) + "', " 
            query_commit += " '" + str(cards_red_31_45_total) + "', " 
            query_commit += " '" + str(cards_red_31_45_percentage) + "', " 
            query_commit += " '" + str(cards_red_46_60_total) + "', " 
            query_commit += " '" + str(cards_red_46_60_percentage) + "', " 
            query_commit += " '" + str(cards_red_61_75_total) + "', " 
            query_commit += " '" + str(cards_red_61_75_percentage) + "', " 
            query_commit += " '" + str(cards_red_76_90_total) + "', " 
            query_commit += " '" + str(cards_red_76_90_percentage) + "', " 
            query_commit += " '" + str(cards_red_91_105_total) + "', " 
            query_commit += " '" + str(cards_red_91_105_percentage) + "', " 
            query_commit += " '" + str(cards_red_106_120_total) + "', " 
            query_commit += " '" + str(cards_red_106_120_percentage) + "', " 
            # ----------------------------------
            # ----------------------------------
            query_commit += " now() ) "    
            # ----------------------------------
            print(space + "api_football_team_reports INSERTED", flush=True)
            # ----------------------------------
        # --------------------------------------
        mycursor.execute(query_commit)
        mydb.commit()   
        # --------------------------------------
        mycursor.close()
        mydb.close() 
        # --------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------

def tr_update_or_insert(leagueapi_id, season, fixtureapi_id, teamapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "tr_update_or_insert()", flush=True) 
    # ----------------------------------------------------------   
    print(space + "leagueapi_id : " + str(leagueapi_id), flush=True) 
    print(space + "season : " + str(season), flush=True) 
    print(space + "teamapi_id : " + str(teamapi_id), flush=True) 
    # ----------------------------------------------------------  
    print(space + "fixtureapi_id : " + str(fixtureapi_id), flush=True)  
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select  * " 
    query += " from api_football_team_reports "    
    query += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query += " and season = "+str(season)+" "     
    query += " and teamapi_id = "+str(teamapi_id)+" "      
    query += " and fixtureapi_id = "+str(fixtureapi_id)+" "      
    # ----------------------------------------------------------    
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------
    print(space + "total_rows: " + str(total_rows), flush=True)
    # ----------------------------------------------------------
    return total_rows     
    # ----------------------------------------------------------  
