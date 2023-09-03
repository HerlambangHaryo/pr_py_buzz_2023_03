# Import
import mysql.connector 
from a_models.api_fixtures import *   
from a_models.api_standings import *   
from a_models.football_odds import *   


def fS_get_fixture_that_not_update_stats_by_teamapi(leagueapi_id, teams_api_id, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_get_fixture_that_not_update_stats_by_teamapi()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' (SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    # query += " , teams_home " 
    # query += " , teams_away " 
    # query += ' , date '     
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id = "+str(leagueapi_id)+" " 
    query += " and teams_homeapi_id  = "+str(teams_api_id)+" " 
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and shots_on_goal_home is null "
    query += " and shots_on_goal_away is null "
    query += " and season >= 2022) "
    query += ' union (SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    # query += " , teams_home " 
    # query += " , teams_away " 
    # query += ' , date '     
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id = "+str(leagueapi_id)+" " 
    query += " and teams_awayapi_id  = "+str(teams_api_id)+" " 
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and shots_on_goal_home is null "
    query += " and shots_on_goal_away is null "
    query += " and season >= 2022) "
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ---------------------------------------------------------- 
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):
        # ------------------------------------------------------
        for x in result:    
            # --------------------------------------------------
            counter         += 1
            fixtureapi_id   = str(x[0])  
            leagueapi_id    = str(x[1])  
            season          = str(x[2])   
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += "#" + fixtureapi_id 
            word += " #" + leagueapi_id 
            word += " - " + season 
            print(word, flush=True)            
            # --------------------------------------------------
            DICT = {
                "fixtureapi_id" : fixtureapi_id, 
            } 
            af_controll_match_update(DICT, "fixtureapi_id", space)
            # --------------------------------------------------
        # ------------------------------------------------------
    # ----------------------------------------------------------     
    # ----------------------------------------------------------  

def fS_get_fixture_that_not_update_stats_by_league(leagueapi_id, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_get_fixture_that_not_update_stats_by_league()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    # query += " , teams_home " 
    # query += " , teams_away " 
    # query += ' , date '     
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id = "+str(leagueapi_id)+" " 
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and shots_on_goal_home is null "
    query += " and shots_on_goal_away is null "
    query += " and season >= 2022 "
    # query += " order by date desc "
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ---------------------------------------------------------- 
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):
        # ------------------------------------------------------
        for x in result:    
            # --------------------------------------------------
            counter         += 1
            fixtureapi_id   = str(x[0])  
            leagueapi_id    = str(x[1])  
            season          = str(x[2])   
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += "#" + fixtureapi_id 
            word += " #" + leagueapi_id 
            word += " - " + season 
            print(word, flush=True)            
            # --------------------------------------------------
            DICT = {
                "fixtureapi_id" : fixtureapi_id, 
            } 
            af_controll_match_update(DICT, "fixtureapi_id", space)
            # --------------------------------------------------
        # ------------------------------------------------------
    # ----------------------------------------------------------     
    # ----------------------------------------------------------  

def fS_get_fixture_that_not_update_stats_all_league(space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_get_fixture_that_not_update_stats_all_league()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    # query += " , teams_home " 
    # query += " , teams_away " 
    # query += ' , date '     
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id IN (select leagueapi_id from football_leagues where detail_stats = 1) " 
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and lineups_coach_homeapi_id  is null "
    query += " and lineups_coach_awayapi_id  is null "
    # query += " and season >= 2022 "
    query += " order by date desc "
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter         += 1
        fixtureapi_id   = str(x[0])  
        leagueapi_id    = str(x[1])  
        season          = str(x[2])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += "#" + fixtureapi_id 
        word += " #" + leagueapi_id 
        word += " - " + season 
        print(word, flush=True)            
        # ------------------------------------------------------ 
        DICT = {
            "fixtureapi_id" : fixtureapi_id, 
        } 
        af_controll_match_update(DICT, "fixtureapi_id", space)
    # ----------------------------------------------------------     
    # ----------------------------------------------------------   

def fS_check_date_is_null(leagueapi_id_PARAM, season_PARAM, space):
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_check_date_is_null()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    query += " , teams_homeapi_id " 
    query += " , teams_awayapi_id " 
    query += ' , date '     
    query += 'FROM football_statistics' 

    if(season_PARAM == 'fixtureapi_id' ):
        query += " WHERE fixtureapi_id = '"+leagueapi_id_PARAM+"' " 
    else:
        query += " WHERE leagueapi_id = '"+leagueapi_id_PARAM+"' " 
        query += " and season = '"+season_PARAM+"' "   
        query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and date is null " 
    query += " order by fixtureapi_id asc " 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    if(total_rows != 0):
        counter = 0
        # ------------------------------------------------------   
        for x in result:    
            # --------------------------------------------------
            counter         += 1
            fixtureapi_id   = str(x[0])  
            leagueapi_id    = str(x[1])  
            season          = str(x[2])   

            teams_homeapi_id   = str(x[3])  
            teams_awayapi_id    = str(x[4])  
            date          = str(x[5])   
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += "#" + fixtureapi_id 
            word += " #" + leagueapi_id 
            word += " - " + season 
            print(word, flush=True)             
            # --------------------------------------------------
            fO_import_date(fixtureapi_id, leagueapi_id_PARAM, season_PARAM, space)
        # ------------------------------------------------------  
        # ------------------------------------------------------  
    # ----------------------------------------------------------  
    fS_get_match_finished_for_ultimate_assessment(leagueapi_id_PARAM, season_PARAM, space)
    # ----------------------------------------------------------   
     
def fS_get_match_finished_for_ultimate_assessment(leagueapi_id_PARAM, season_PARAM, space):
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_get_match_finished_for_ultimate_assessment()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    query += " , teams_homeapi_id " 
    query += " , teams_awayapi_id " 
    query += ' , date '     
    query += 'FROM football_statistics' 
    
    if(season_PARAM == 'fixtureapi_id' ):
        query += " WHERE fixtureapi_id = '"+leagueapi_id_PARAM+"' " 
    else:
        query += " WHERE leagueapi_id = '"+leagueapi_id_PARAM+"' " 
        query += " and season = '"+season_PARAM+"' "   
        query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   

    query += " order by date asc " 
    # query += "  limit 20, 20 " 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter         += 1
        fixtureapi_id   = str(x[0])  
        leagueapi_id    = str(x[1])  
        season          = str(x[2])   

        teams_homeapi_id   = str(x[3])  
        teams_awayapi_id    = str(x[4])  
        date          = str(x[5])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " " + date 
        word += " #" + fixtureapi_id 
        word += "  " + leagueapi_id 
        word += " - " + season 
        word +=  " [" + teams_homeapi_id + " vs " + teams_awayapi_id + "] " 
        print(word, flush=True)            
        # ------------------------------------------------------ 
        fS_get_match_finished_for_ultimate_assessment_TEAM_DETAILS(fixtureapi_id, leagueapi_id, season, date, teams_homeapi_id, 'home', space)
        fS_get_match_finished_for_ultimate_assessment_TEAM_DETAILS(fixtureapi_id, leagueapi_id, season, date, teams_awayapi_id, 'away', space)
        print("")
    # ----------------------------------------------------------  

def fS_get_match_finished_for_ultimate_assessment_TEAM_DETAILS(fixtureapi_id_PARAM, leagueapi_id_PARAM, season_PARAM, date, teams_api_id, team_status, space):
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "fS_get_match_finished_for_ultimate_assessment_TEAM_DETAILS()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    query += " , teams_homeapi_id as team "  
    query += ' , date '     
    # -------------------------------------------
    query += ' , goals_home as goals '    
    query += ' , score_halftime_home as score_halftime'     
    query += ' , score_secondtime_home as score_secondtime '  
    # -------------------------------------------
    query += ' , corner_kicks_home as corner_kicks '   
    query += ' , yellow_cards_home as yellow_cards  '   
    query += ' , red_cards_home as red_cards '   
    # -------------------------------------------
    # -------------------------------------------
    query += ' , goals_away  as goals_against '   
    query += ' , score_halftime_away  as score_halftime_against'     
    query += ' , score_secondtime_away  as score_secondtime_against '  
    # -------------------------------------------
    query += ' , corner_kicks_away  as corner_kicks_against '   
    query += ' , yellow_cards_away  as yellow_cards_against  '   
    query += ' , red_cards_away  as red_cards_against '   
    # -------------------------------------------
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id = '"+leagueapi_id_PARAM+"' " 
    query += " and season = '"+season_PARAM+"' "   
    query += " and date < '"+date+"' "   
    query += " and teams_homeapi_id = '"+teams_api_id+"' "   
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended')  "   
    query += "  order by date asc "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result_as_home =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows_as_home = len(result_as_home)
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' fixtureapi_id ' 
    query += ' , leagueapi_id '  
    query += ' , season '  
    query += " , teams_awayapi_id as team "  
    query += ' , date '     
    # -------------------------------------------
    query += ' , goals_away  as goals '   
    query += ' , score_halftime_away  as score_halftime'     
    query += ' , score_secondtime_away  as score_secondtime '  
    # -------------------------------------------
    query += ' , corner_kicks_away  as corner_kicks '   
    query += ' , yellow_cards_away  as yellow_cards  '   
    query += ' , red_cards_away  as red_cards '   
    # -------------------------------------------
    # -------------------------------------------
    query += ' , goals_home as goals_against '    
    query += ' , score_halftime_home as score_halftime_against '     
    query += ' , score_secondtime_home as score_secondtime_against '  
    # -------------------------------------------
    query += ' , corner_kicks_home as corner_kicks_against '   
    query += ' , yellow_cards_home as yellow_cards_against  '   
    query += ' , red_cards_home as red_cards_against '   
    # -------------------------------------------
    query += 'FROM football_statistics' 
    query += " WHERE leagueapi_id = '"+leagueapi_id_PARAM+"' " 
    query += " and season = '"+season_PARAM+"' "   
    query += " and date < '"+date+"' "   
    query += " and teams_awayapi_id = '"+teams_api_id+"' "   
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended')  "     
    query += "  order by date asc " 
    # ----------------------------------------------------------    
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result_as_away =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows_as_away = len(result_as_away)
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 





    # ----------------------------------------------------------  
    counter_as_home = 0
    counter_as_away = 0
    total_rows = total_rows_as_home + total_rows_as_away
    # ----------------------------------------------------------   
    if(total_rows != 0):
        # ------------------------------------------------ Goals
        goals_total = 0
        goals_avg = 0
        # ------------------------------------------------- Half
        halfs_total = 0
        halfs_avg = 0
        # ----------------------------------------------- Second
        seconds_total = 0
        seconds_avg = 0
        # ---------------------------------------------- Corners
        corners_total = 0
        corners_avg = 0
        # ---------------------------------------------- Yellows
        yellows_total = 0
        yellows_avg = 0
        # ------------------------------------------------ Cards
        cards_total = 0
        cards_avg = 0
        # ------------------------------------------------------
        for x in result_as_home:    
            # --------------------------------------------------
            counter_as_home         += 1
            # --------------------------------------------------
            fixtureapi_id   = str(x[0])  
            leagueapi_id    = str(x[1])  
            season          = str(x[2])   
            # --------------------------------------------------
            team            = str(x[3])   
            date            = str(x[4])   
            # --------------------------------------------------
            goals                   = x[5]   
            score_halftime          = x[6]   
            score_secondtime        = x[7]   
            # -------------------------------------------------- 
            corner_kicks               = 0
            if(x[8] is not None):
                corner_kicks           = x[8]   

            yellow_cards               = 0
            if(x[9] is not None):
                yellow_cards           = x[9]   

            red_cards               = 0
            if(x[10] is not None):
                red_cards           = x[10]   
            # --------------------------------------------------
            goals_against           = x[11]
            # --------------------------------------------------
            word = space + "[" + str(counter_as_home) + "/" +str(total_rows_as_home) + "] " 
            word += " " + date 
            word += " #" + fixtureapi_id 
            word += "  " + leagueapi_id 
            word += " - " + season 
            word +=  " [" + team + "] " 
            word +=  " goals: " + str(goals)
            print(word, flush=True)            
            # --------------------------------------------------
            goals_total += goals 
            # --------------------------------------------------
        # ------------------------------------------------------ 
        # ------------------------------------------------------
        for x in result_as_away:    
            # --------------------------------------------------
            counter_as_away         += 1
            # --------------------------------------------------
            fixtureapi_id   = str(x[0])  
            leagueapi_id    = str(x[1])  
            season          = str(x[2])   
            # --------------------------------------------------
            team            = str(x[3])   
            date            = str(x[4])   
            # --------------------------------------------------
            goals                   = x[5]   
            score_halftime          = x[6]   
            score_secondtime        = x[7]   
            # -------------------------------------------------- 
            corner_kicks               = 0
            if(x[8] is not None):
                corner_kicks           = x[8]   

            yellow_cards               = 0
            if(x[9] is not None):
                yellow_cards           = x[9]   

            red_cards               = 0
            if(x[10] is not None):
                red_cards           = x[10]   
            # --------------------------------------------------
            goals_against           = x[11]
            # --------------------------------------------------
            word = space + "[" + str(counter_as_away) + "/" +str(total_rows_as_away) + "] " 
            word += " " + date 
            word += " #" + fixtureapi_id 
            word += "  " + leagueapi_id 
            word += " - " + season 
            word +=  " [" + team + "] " 
            word +=  " goals: " + str(goals)
            print(word, flush=True)            
            # ---------------------------------------------- for
            # -------------------------------------------- goals
            goals_total += goals 
            # ------------------------------------------ against
            # -------------------------------------------- goals
            goals_total_against += goals_against 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        match_played = counter_as_home + counter_as_away
        # ------------------------------------------------------ 
        # ------------------------------------------------ goals 
        goals_ratio     = (goals_total / total_rows)
        halfs_ratio     = (halfs_total / total_rows)
        seconds_ratio   = (seconds_total / total_rows)
        # ------------------------------------------------------ 
        corners_ratio   = (corners_total / total_rows)
        yellows_ratio   = (yellows_total / total_rows)
        cards_ratio     = (cards_total / total_rows)
        # ------------------------------------------------------ 
        space += "____"
        # ------------------------------------------------------ 
        print(space + "Total Rows: " + str(total_rows), flush=True)
        print(space + "Match Played: " + str(match_played), flush=True)
        # ------------------------------------------------------ 
        print("", flush=True)
        # ------------------------------------------------------ 
        goals_for_home
        goals_for_home_ratio

        goals_against_home
        goals_against_home_ratio
        # print(space + "Match Played as Home : " + str(counter_as_home), flush=True)
        # print(space + "goals ratio: " + str(goals_ratio), flush=True)
        # print(space + "half ratio: " + str(halfs_ratio), flush=True)
        # print(space + "second ratio: " + str(seconds_ratio), flush=True)
        # ------------------------------------------------------ 
        print("", flush=True)
        # ------------------------------------------------------ 
        goals_for_away
        goals_for_away_ratio
        
        goals_against_away
        goals_against_away_ratio
        # print(space + "Match Played as Away : " + str(counter_as_away), flush=True)
        # print(space + "corners ratio: " + str(corners_ratio), flush=True)
        # print(space + "yellows ratio: " + str(yellows_ratio), flush=True)
        # print(space + "cards ratio: " + str(cards_ratio), flush=True)
        # ------------------------------------------------------ 
        print("", flush=True)
        # ------------------------------------------------------ 
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ----------------------------------------------------------    
        query = "UPDATE `football_statistics` SET  "
        query += " goals_"+team_status+"_ratio = '"+str(goals_ratio)+"', " 
        query += " halfs_"+team_status+"_ratio = '"+str(halfs_ratio)+"', " 
        query += " seconds_"+team_status+"_ratio = '"+str(seconds_ratio)+"', " 
        # ----------------------------------------------------------    

        query += " corners_"+team_status+"_ratio = '"+str(corners_ratio)+"', " 
        query += " yellows_"+team_status+"_ratio = '"+str(yellows_ratio)+"', " 
        query += " cards_"+team_status+"_ratio = '"+str(cards_ratio)+"' " 

        query += " where fixtureapi_id = '"+str(fixtureapi_id_PARAM)+"' " 
        query += " and leagueapi_id = '"+str(leagueapi_id_PARAM)+"' " 
        query += " and season = '"+str(season_PARAM)+"' " 
        # ----------------------------------------------------------    
        # mycursor.execute(query)
        # mydb.commit()      
        # # ----------------------------------------------------------      
        # # close the cursor and database connection
        # mycursor.close()
        # mydb.close() 
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ----------------------------------------------------------    
        query = "UPDATE `football_odds` SET  "
        query += " goals_"+team_status+"_ratio = '"+str(goals_ratio)+"', " 
        query += " halfs_"+team_status+"_ratio = '"+str(halfs_ratio)+"', " 
        query += " seconds_"+team_status+"_ratio = '"+str(seconds_ratio)+"', " 
        # ----------------------------------------------------------    

        query += " corners_"+team_status+"_ratio = '"+str(corners_ratio)+"', " 
        query += " yellows_"+team_status+"_ratio = '"+str(yellows_ratio)+"', " 
        query += " cards_"+team_status+"_ratio = '"+str(cards_ratio)+"' " 

        query += " where fixtureapi_id = '"+str(fixtureapi_id_PARAM)+"' " 
        query += " and leagueapi_id = '"+str(leagueapi_id_PARAM)+"' " 
        query += " and season = '"+str(season_PARAM)+"' " 
        # ----------------------------------------------------------    
        # mycursor.execute(query)
        # mydb.commit()      
        # # ----------------------------------------------------------      
        # # close the cursor and database connection
        # mycursor.close()
        # mydb.close()  
    # ----------------------------------------------------------

    
def fS_get_league_group_for_api_standings(day1, day2, space):
    # ----------------------------------------------------------   
    # 1a. Match Update
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fS_get_league_group_for_api_standings()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select "
    query += " leagueapi_id " 
    query += " , season  "
    query += " from football_odds " 
    query += " where date <= Date('"+day2+"') "
    query += " and date >= Date('"+day1+"') "
    query += " and deleted_at is null "  
    query += " group by leagueapi_id, season "
    query += " order by date, leagueapi_id asc  "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season
        print(word, flush=True)    
        # ------------------------------------------------------
        DICT = {
            'leagueapi_id' :leagueapi_id,
            'season' :season, 
        }
        # # ------------------------------------------------------  
        as_controll_match_update(DICT, "Null", space)
        # # ------------------------------------------------------ 
        print("  ___________________________________________________", flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------  