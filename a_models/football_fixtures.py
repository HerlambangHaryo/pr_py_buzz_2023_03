# Import
import mysql.connector 
from a_models.api_fixtures import *   
from a_models.api_odds import *   
from a_models.xpattern import *   
from a_models.standings import *   
from a_models.leagues import *   
from a_models.patternlists_assestment import *  


def ff_get_fixtures_for_reset_pattern(leagueapi_id, season, day0, prep_col, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixtures_for_reset_pattern()", flush=True)
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
    query += " leagueapi_id " 
    query += " , season " 
    query += " , fixtureapi_id " 

    query += " , date " 
    query += " , teams_home " 
    query += " , teams_away " 
    query += " , fixture_status " 

    query += " from football_fixtures " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # query += " and season = '"+str(season)+"' "
    
    query += " and date <= '"+str(day0)+"' " 

    if(prep_col == 'pre_'):
        query += " and pre_ah_pattern is not null " 
        query += " and pre_gou_pattern is not null " 
    elif(prep_col == 'end_'):
        query += " and end_ah_pattern is not null " 
        query += " and end_gou_pattern is not null " 

    
    query += " and deleted_at is null "   
    query += " order by league_country, leagueapi_id asc  "   
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id_row  = str(x[0]) 
        season            = str(x[1])  
        fixtureapi_id     = str(x[2])  
    
        date     = str(x[3])  
        teams_home     = str(x[4])  
        teams_away     = str(x[5])  
        fixture_status     = str(x[6])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id_row
        word += " - " + season 
        word += " | " + teams_home 
        word += " vs " + teams_away 
        word += " | " + date 
        word += " | " + fixture_status 
        print(word, flush=True)   
        # ------------------------------------------------------
        xp_set_pattern(fixtureapi_id, prep_col, 'no', space)
    # ---------------------------------------------------------- 
    lg_update_reset_pattern(leagueapi_id, prep_col, day0, space)
    # ----------------------------------------------------------

def ff_get_fixture_today_xpattern_advices(day1, day2, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_today_xpattern_advices()", flush=True)
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
    query += " date,  "
    query += " fixtureapi_id,  "

    query += " league_country,  "
    query += " league_name,  "
    query += " season,  "

    query += " teams_home,  "
    query += " teams_away  "

    query += " from football_fixtures "    
    query += " where DATE(date) >= '"+str(day1)+"' "
    query += " and DATE(date) <= '"+str(day2)+"' "
    # query += " and pre_match_winner_home is not null "
    # query += " and pre_ah_pattern is null "
    query += " order by date asc "
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall() 
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    count_rows = 0
    # ----------------------------------------------------------  
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------  
        date = rs1[0]
        fixtureapi_id = rs1[1]

        league_country = rs1[2]
        league_name  = rs1[3] 
        season  = rs1[4]

        teams_home  = rs1[5]
        teams_away  = rs1[6]
        # ------------------------------------------------------  
        word = space + "[" +str(count_rows) + "/" + str(total_rows) + "] " + str(date)
        print(word, flush=True)  
        # ------------------------------------------------------  
        word = space + str(league_country) + " - "
        word += str(league_name) + " "
        word += str(season)  
        print(word, flush=True)   
        # ------------------------------------------------------   
        word = "#" + str(fixtureapi_id)+ "  "
        word += str(teams_home) + " vs "
        word += str(teams_away) 
        print(word, flush=True)   
        # ------------------------------------------------------  
        if(ROUTES == 'xpattern'):
            xp_set_pattern(fixtureapi_id, 'pre_', 'yes', space)
    # ----------------------------------------------------------  

def ff_get_fixture_status_match_finished_for_daily_update_patternlist(day1, day2, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_status_match_finished_for_daily_update_patternlist()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select  "
    query += " fixtureapi_id  " 
    query += " , teams_home  " 
    query += " , teams_away " 

    query += " , leagueapi_id " 

    query += " , pre_ah_pattern " 
    query += " , pre_gou_pattern " 
    query += " , end_ah_pattern " 
    query += " , end_gou_pattern " 

    query += " , season " 
    query += " , pre_ah_pattern_mirror " 
    query += " , end_ah_pattern_mirror " 
    query += " , league_country " 
    
    query += " , end_odd_updated_at " 
    query += " , fixture_status " 

    query += " from football_fixtures "    
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    query += " and end_odd_updated_at is not null "  
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') " 
    # ----------------------------------------------------------  
    print(space + query, flush=True) 
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall() 
    # ----------------------------------------------------------     
    space += "__"
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    count_rows = 0
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------    
    counter = 0
    # ----------------------------------------------------------    
    for x in result: 
        # ------------------------------------------------------   
        counter += 1
        # ------------------------------------------------------  
        fixtureapi_id = x[0]
        teams_home = x[1]
        teams_away = x[2]

        leagueapi_id = x[3]

        pre_ah_pattern      = x[4]
        pre_gou_pattern     = x[5]
        end_ah_pattern      = x[6]
        end_gou_pattern     = x[7]

        season     = x[8]

        pre_ah_pattern_mirror      = x[9]
        end_ah_pattern_mirror      = x[10]

        league_country     = x[11]

        end_odd_updated_at     = x[12]
        fixture_status     = x[13]
        # ------------------------------------------------------    
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " + "#" + str(fixtureapi_id) + " "
        word += "#" + str(league_country) + " " + str(leagueapi_id) + "-" + str(season) + " / "
        word += str(teams_home) + " vs "
        word += str(teams_away)  
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + "pre-ah:" + str(pre_ah_pattern) + " -- "
        word += "pre-gou:" + str(pre_gou_pattern) + " -/- "
        word += "end-ah:" + str(end_ah_pattern) + " -- "
        word += "end-gou:" + str(end_gou_pattern)  
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + str(fixture_status) + " -- "
        word += "end_odd_updated_at:" + str(end_odd_updated_at)  
        print(word, flush=True)   
        # ------------------------------------------------------   
        print("", flush=True)
        # ------------------------------------------------------  
        pl_check_patternlist(leagueapi_id, league_country, 
            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern, 
            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern, 
            space)
        print("", flush=True)
        pa_assestment_daily_update(leagueapi_id, league_country, 
            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern, 
            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern, 
            space)
        print("", flush=True)
        # ------------------------------------------------------   

def ff_get_fixture_status_match_finished(day1, day2, ROUTES, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_status_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select DATE(date), leagueapi_id, "
    query += " (select bookmakersapi_id from leagues "
    query += "  where leagues.leagueapi_id = football_fixtures.leagueapi_id), "
    query += " season,  "
    query += " fixtureapi_id,  "
    query += " pre_ah_pattern,  "
    query += " pre_gou_pattern  "
    query += " from football_fixtures "    
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    if(ROUTES == 'odds'):
        query += " and fixture_status like 'Match Finished' "
    elif(ROUTES == 'xpattern'):
        query += " and fixture_status like 'Match Finished Ended' "
    query += " and deleted_at is null "  
    query += " order by leagueapi_id "  
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall() 
    # ----------------------------------------------------------     
    space += "__"
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    count_rows = 0
    # ----------------------------------------------------------  
    for rs1 in result: 
        # ------------------------------------------------------  
        count_rows += 1
        # ------------------------------------------------------  
        date = rs1[0]
        league = rs1[1]
        bookmaker = rs1[2]
        season  = rs1[3]

        fixtureapi_id  = rs1[4]
        pre_ah_pattern  = rs1[5]
        pre_gou_pattern  = rs1[6]
        # ------------------------------------------------------  
        words_001 = space + str(count_rows) + ". "
        words_001 += str(date) + " // "
        words_001 += str(league) + " // "
        words_001 += str(bookmaker) + " // "
        words_001 += str(season)+ " // "
        words_001 += str(fixtureapi_id)+ " // "
        words_001 += str(pre_ah_pattern)+ " // "
        words_001 += str(pre_gou_pattern)
        # ------------------------------------------------------  
        words =  words_001
        print(words, flush=True)  
        # ------------------------------------------------------  
        if(ROUTES == 'xpattern'):
            xp_set_pattern(fixtureapi_id, 'end_', 'no', space)
    # ----------------------------------------------------------  

def ff_get_group_league_status_match_finished(day1, day2, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_group_league_status_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    #
    # always double check to ff_get_fixture_status_match_finished
    # same query
    # 
    query = "Select DATE(date), leagueapi_id, "
    query += " (select bookmakersapi_id from leagues "
    query += "  where leagues.leagueapi_id = football_fixtures.leagueapi_id), "
    query += " season  "
    query += " from football_fixtures "    
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "  
    query += " and fixture_status like 'Match Finished' "
    query += " and deleted_at is null " 
    query += " and end_odd_updated_at is null " 
    query += " group by DATE(date), leagueapi_id, season "
    query += " order by leagueapi_id "  
    # query += " limit 0,2 "  
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall() 
    # ----------------------------------------------------------    
    space += "__"
    total_rows = len(result)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------    
    count_rows = 0  
    # ---------------------------------------------------------- 
    ff_get_fixture_status_match_finished(day1, day2, 'odds', space)
    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):
        # ------------------------------------------------------
        space += "__"
        # ------------------------------------------------------
        for rs1 in result: 
            # --------------------------------------------------  
            count_rows += 1
            # -------------------------------------------------- 
            date = rs1[0]
            league = rs1[1]
            bookmaker = rs1[2]
            season  = rs1[3]
            # --------------------------------------------------
            words_001 = space + str(count_rows) + ". "
            words_001 += str(date) + " // "
            words_001 += str(league) + " // "
            words_001 += str(bookmaker) + " // "
            words_001 += str(season)
            # -------------------------------------------------- 
            words =  words_001
            print(words, flush=True) 
            # --------------------------------------------------  
            DICT = {
                "date" : date,
                "bookmaker" : bookmaker,
                "season" : season,
                "league" : league,
                "page" : 1,
            }
            # ao_controll_match_update(date, bookmaker, season, league, 1, space) 
            ao_controll_match_update(DICT, 'end_', space) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  

# def ff_get_team_list_next_match(leagueapi_id, season, space):
#     # ----------------------------------------------------------   
#     space += "__"
#     # ---------------------------------------------------------- 
#     print(space + "ff_get_team_list_next_match()", flush=True)
#     # ----------------------------------------------------------   
#     space += "__"
#     # ----------------------------------------------------------    
#     host="localhost"
#     user="root" 
#     database="pr_mmbuzz_2022_06"
#     mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
#     mycursor = mydb.cursor()  
#     # ----------------------------------------------------------  
#     query = "( Select leagueapi_id, season, teams_home_id as team_id, teams_home as name  "
#     query += " from football_fixtures " 
#     query += " where leagueapi_id = '"+leagueapi_id+"' " 
#     query += " and season = '"+season+"' " 
#     query += " and deleted_at is null "  
#     query += " group by leagueapi_id, season, teams_home_id, teams_home ) " 
#     query += " union all "  
#     query = "( Select leagueapi_id, season, teams_away_id as team_id, teams_away as name  "
#     query += " from football_fixtures " 
#     query += " where leagueapi_id = '"+leagueapi_id+"' " 
#     query += " and season = '"+season+"' " 
#     query += " and deleted_at is null "  
#     query += " group by leagueapi_id, season, teams_away_id, teams_away ) " 
#     query += " order by team_id asc " 
#     # ----------------------------------------------------------  
#     # print(space + query)
#     # ----------------------------------------------------------   
#     mycursor = mydb.cursor()
#     mycursor.execute(query)
#     result =  mycursor.fetchall()
#     # ----------------------------------------------------------    
#     print(space + "Total Row(s) : " + str(len(result)), flush=True) 
#     # ----------------------------------------------------------    
#     counter = 0
#     # ----------------------------------------------------------   
#     space += "__"
#     # ----------------------------------------------------------  
#     for x in result:    
#         # ------------------------------------------------------
#         counter        += 1

#         leagueapi_id   = str(x[0]) 
#         season         = str(x[1]) 

#         team_id        = x[2] 
#         name           = str(x[3])  
#         # ------------------------------------------------------
#         word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
#         word += " - " + season
#         word += " -----#" + str(team_id) 
#         word += " - " + name
#         print(word, flush=True)   
#         # ------------------------------------------------------
#         if(team_id is None):
#             print(space + "NONEONOENEOENOENOEONEOEO")
#             print(space + "RESTART")
#         # ------------------------------------------------------
#         if(team_id is not None):
#             st_check_standing(leagueapi_id, season, team_id, name, space)
#             st_update_standing(leagueapi_id, season, team_id, name, space)
#         # ------------------------------------------------------

def ff_get_teams_from_fixtures(fixtureapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_teams_from_fixtures()", flush=True)
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
    query += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
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
        teams_home_id   = x[0] 
        teams_away_id   = x[1] 

        leagueapi_id    = str(x[2])  
        season          = str(x[3])   
        fixtureapi_id   = str(x[4])  
 
        # ------------------------------------------------------ 
        st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_home_id, 'home', space)
        st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_away_id, 'away', space)
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  

def ff_get_fixtures_next_match(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixtures_next_match()", flush=True)
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
    query += " fixtureapi_id, " 

    query += " teams_home, " 
    query += " teams_away, " 
    query += " date " 
    
    query += " from football_fixtures " 
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
        teams_home_id   = x[0] 
        teams_away_id   = x[1] 

        leagueapi_id    = str(x[2])  
        season          = str(x[3])   
        fixtureapi_id   = str(x[4])  

        teams_home      = str(x[5])  
        teams_away      = str(x[6])  
        date            = str(x[7]) 
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id + " - " + season
        print(word, flush=True)   
        # ------------------------------------------------------ 
        word = space + date + " fx:" + fixtureapi_id
        print(word, flush=True)   
        # ------------------------------------------------------ 
        word = space + teams_home + " [" + str(teams_home_id) + "] "
        word += " vs " + teams_away + " [" + str(teams_away_id) + "] "
        print(word, flush=True)   
        # ------------------------------------------------------ 
        if(teams_home_id is None):
            print(space + "home NONE")
        # ------------------------------------------------------ 
        if(teams_away_id is None):
            # -------------------------------------------------- 
            print(space + "away NONE")
            # -------------------------------------------------- 
            DICT = {
                'fixtureapi_id': fixtureapi_id
            } 
            # -------------------------------------------------- 
            af_controll_match_update(DICT, 'fixtureapi_id', space)
        # ------------------------------------------------------ 
        ff_get_teams_from_fixtures(fixtureapi_id, space)
        # ------------------------------------------------------ 
        print("")
    # ---------------------------------------------------------- 

def ff_get_fixt_next_match(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixt_next_match()", flush=True)
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
    query += " fixtureapi_id, " 

    query += " teams_home, " 
    query += " teams_away, " 
    query += " date " 
    
    query += " from football_fixtures " 
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
        teams_home_id   = x[0] 
        teams_away_id   = x[1] 

        leagueapi_id    = str(x[2])  
        season          = str(x[3])   
        fixtureapi_id   = str(x[4])  

        teams_home      = str(x[5])  
        teams_away      = str(x[6])  
        date            = str(x[7]) 
        # ------------------------------------------------------  
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
        print(word, flush=True)    
        # ------------------------------------------------------  
        word = space + "__Home: #" + teams_home_id 
        print(word, flush=True)     
        st_check_standing_rows(leagueapi_id, season, teams_home_id, teams_home, space)
        st_update_standing(leagueapi_id, season, teams_home_id, teams_home, space)
        st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_home_id, 'home', space)
        # ------------------------------------------------------  
        word = space + "__Away: #" + teams_away_id 
        print(word, flush=True)    
        st_check_standing_rows(leagueapi_id, season, teams_away_id, teams_away, space)
        st_update_standing(leagueapi_id, season, teams_away_id, teams_away, space)
        st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_away_id, 'away', space)

        
        # st_check_standings(leagueapi_id, season, space)
        # st_get_team_barely_updated(leagueapi_id, season, day0, space)
        # st_get_team_rank(leagueapi_id, season, day0, space)
    # ---------------------------------------------------------- 

def ff_get_fixtures_not_started_yet(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixtures_not_started_yet()", flush=True)
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
    query += " fixtureapi_id, " 

    query += " teams_home, " 
    query += " teams_away, " 
    query += " date " 
    
    query += " from football_fixtures " 
    query += " where date >= '"+str(day0)+"' " 
    query += " and date <= '"+str(day1)+"' " 
    query += " and fixture_status like 'Not Started Yet' " 
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

        leagueapi_id    = str(x[2])  
        season          = str(x[3])  

        fixtureapi_id   = str(x[4])  

        teams_home      = str(x[5])  
        teams_away      = str(x[6])  
        date            = str(x[7]) 
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
        word += " - " + season
        word += " -----#" + teams_home + " " + teams_home_id 
        word += " - " + teams_away + " "+ teams_away_id
        word += " - " + date
        print(word, flush=True)   
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    counter = 0 
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'): 
        # ------------------------------------------------------    
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            teams_home_id   = str(x[0]) 
            teams_away_id   = str(x[1]) 

            leagueapi_id    = str(x[2])  
            season          = str(x[3])  

            fixtureapi_id   = str(x[4])  
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
            word += " - " + season
            word += " -----#" + teams_home_id 
            word += " - " + teams_away_id
            print(word, flush=True)   
            # --------------------------------------------------
            ROUTES = "fixtureapi_id"
            DICT = {
                "fixtureapi_id" : fixtureapi_id
            }
            af_controll_match_update(DICT, ROUTES, space)
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  

"""
def ff_get_fixtures_next_match(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixtures_next_match()", flush=True)
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
    query += " fixtureapi_id, " 

    query += " teams_home, " 
    query += " teams_away, " 
    query += " date " 
    
    query += " from football_fixtures " 
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

        leagueapi_id    = str(x[2])  
        season          = str(x[3])  

        fixtureapi_id   = str(x[4])  

        teams_home      = str(x[5])  
        teams_away      = str(x[6])  
        date            = str(x[7]) 
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
        word += " - " + season
        word += " -----#" + teams_home + " " + teams_home_id 
        word += " - " + teams_away + " "+ teams_away_id
        word += " - " + date
        print(word, flush=True)   
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'): 
        # ------------------------------------------------------    
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            teams_home_id   = str(x[0]) 
            teams_away_id   = str(x[1]) 

            leagueapi_id    = str(x[2])  
            season          = str(x[3])  

            fixtureapi_id   = str(x[4])  
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + leagueapi_id
            word += " - " + season
            word += " -----#" + teams_home_id 
            word += " - " + teams_away_id
            print(word, flush=True)   
            # --------------------------------------------------
            st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_home_id, 'home', space)
            st_get_team_update_stats(fixtureapi_id, leagueapi_id, season, teams_away_id, 'away', space)
        # ------------------------------------------------------   
    # ----------------------------------------------------------   
"""

def ff_get_league_group_next_match_ARRAY(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_league_group_next_match_ARRAY()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select leagueapi_id, league_name, league_country, season  "
    query += " from football_fixtures " 
    query += " where date >= '"+str(day0)+"' " 
    query += " and date <= '"+str(day1)+"' " 
    query += " and deleted_at is null "   
    query += " group by leagueapi_id, league_name, league_country, season "
    query += " order by league_country, leagueapi_id asc  "   
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    return result 
    # ----------------------------------------------------------   
    
def ff_league_check_end_odd_update(leagueapi_id, season, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_league_check_end_odd_update()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select end_odd_updated_at "
    query += " from football_fixtures " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "  
    query += " and deleted_at is null "  
    query += " and end_odd_updated_at is not null "     
    query += " order by end_odd_updated_at desc  "   
    query += " limit 0,1 "   
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        end_odd_updated_at   = str(x[0])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + end_odd_updated_at 
        print(word, flush=True)  
        # ------------------------------------------------------
        lg_check_date_diff_col_for_reset_pattern(leagueapi_id, 'tanggal_reset_pre_pattern', 'pre_', end_odd_updated_at, space) 
        lg_check_date_diff_col_for_reset_pattern(leagueapi_id, 'tanggal_reset_end_pattern', 'end_', end_odd_updated_at, space) 
    # ----------------------------------------------------------   


def ff_gak_sempet_predates(day0, date_raw, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_gak_sempet_predates()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select leagueapi_id, league_name, league_country, season, DATE(date),  "
    query += " (select bookmakersapi_id from leagues "
    query += "  where leagues.leagueapi_id = football_fixtures.leagueapi_id) "
    query += " from football_fixtures " 
    query += " where date = '"+day0+"' "  
    query += " and deleted_at is null "  
    query += " and pre_odd_updated_at is null "    
    query += " group by leagueapi_id, league_name, league_country, season, DATE(date) "
    query += " order by league_country, leagueapi_id asc  "   
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------    

    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        league   = str(x[0]) 
        league_name    = str(x[1]) 
        league_country = str(x[2])  
        season         = str(x[3])   
        date            = str(x[4])   
        bookmaker            = str(x[5])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + league_country
        word += " - " + league_name
        word += " -----#" + league 
        word += " - " + season 
        word += " - " + date 
        word += " - " + bookmaker 
        print(word, flush=True)   
        # ------------------------------------------------------  

    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        for x in result:    
            # ------------------------------------------------------
            counter        += 1
            league   = str(x[0]) 
            league_name    = str(x[1]) 
            league_country = str(x[2])  
            season         = str(x[3])   
            date            = str(x[4])   
            bookmaker            = str(x[5])   
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + league_country
            word += " - " + league_name
            word += " -----#" + league 
            word += " - " + season 
            word += " - " + date 
            word += " - " + bookmaker 
            print(word, flush=True)   
            # ------------------------------------------------------
            DICT = {
                "date" : date,
                "date_raw" : date_raw,
                "bookmaker" : bookmaker,
                "season" : season,
                "league" : league,
                "page" : 1,
            }
            # ao_controll_match_update(date, bookmaker, season, league, 1, space) 
            ao_controll_match_update(DICT, 'preleague_', space) 
            #------------------------------------------------------

def ff_get_league_group_next_match(day0, day1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_league_group_next_match()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select leagueapi_id, league_name, league_country, season  "
    query += " from football_fixtures " 
    query += " where date >= '"+day0+"' " 
    query += " and date <= '"+day1+"' " 
    query += " and deleted_at is null "  
    # #603 
    # query += " where leagueapi_id in (2, 39) "  
    query += " group by leagueapi_id, league_name, league_country, season "
    query += " order by league_country, leagueapi_id asc  "  
    # query += " limit 0,3  "  
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(len(result)), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0]) 
        league_name    = str(x[1]) 
        league_country = str(x[2])  
        season         = str(x[3])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " + league_country
        word += " - " + league_name
        word += " -----#" + leagueapi_id 
        word += " - " + season
        print(word, flush=True)   
        # ------------------------------------------------------
        # ff_get_team_list_next_match(leagueapi_id, season, space)
        st_check_standings(leagueapi_id, season, space)
        st_get_team_barely_updated(leagueapi_id, season, day0, space)
        st_get_team_rank(leagueapi_id, season, day0, space)
    # ----------------------------------------------------------   

def ff_get_fixture_that_fixture_status_not_in_match_finished(day1, day2, today, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_that_fixture_status_not_in_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select leagueapi_id "
    query += " , league_name "
    query += " , league_country "
    query += " , season  "
    query += " , teams_home " 
    query += " , teams_away " 
    query += " , fixture_status " 
    query += " , DATE(updated_at) " 
    query += " , date " 
    query += " from football_fixtures " 
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' " 
    query += " ) "
    query += " and deleted_at is null "
    query += " and DATE(updated_at) != '"+str(today)+"' " 
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
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0]) 
        league_name    = str(x[1]) 
        league_country = str(x[2])  
        season         = str(x[3])  

        teams_home      = str(x[4]) 
        teams_away      = str(x[5])  
        fixture_status  = str(x[6])  

        updated_at  = str(x[7])  
        date  = str(x[8])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " + leagueapi_id 
        word += " - " + season
        word += " / " + teams_home
        word += " vs " + teams_away
        word += " / " + fixture_status
        word += " / " + updated_at
        word += " / " + date
        print(word, flush=True)    
        # ------------------------------------------------------
    # ----------------------------------------------------------

def ff_get_league_group_fixture_status_not_in_match_finished(day1, day2, today, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_league_group_fixture_status_not_in_match_finished()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select leagueapi_id, league_name, league_country, season  "
    query += " from football_fixtures " 
    query += " where date <= '"+day2+"' "
    query += " and date >= '"+day1+"' "
    query += " and deleted_at is null "
    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended' " 
    query += " ) "
    query += " and deleted_at is null "
    query += " and DATE(updated_at) != '"+str(today)+"' "
    query += " group by leagueapi_id, league_name, league_country, season "
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
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0]) 
        league_name    = str(x[1]) 
        league_country = str(x[2])  
        season         = str(x[3])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " + league_country
        word += " - " + league_name
        word += " -----#" + leagueapi_id 
        word += " - " + season
        print(word, flush=True)    
    # ----------------------------------------------------------   
    ff_get_fixture_that_fixture_status_not_in_match_finished(day1, day2, today, space) 
    # ----------------------------------------------------------   
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        # ------------------------------------------------------  
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            leagueapi_id   = str(x[0]) 
            league_name    = str(x[1]) 
            league_country = str(x[2])  
            season         = str(x[3])  
            # --------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " + league_country
            word += " - " + league_name
            word += " -----#" + leagueapi_id 
            word += " - " + season
            print(word, flush=True)   
            # ---------------------------------------------------
            # --------------------------------------------------- 
            DICT = {
                'leagueapi_id' :leagueapi_id,
                'season' :season,
                'day1' :day1,
                'day2' :day2,
            }
            # --------------------------------------------------- 
            ROUTES = 'leagueapi_id'
            af_controll_match_update(DICT, ROUTES, space)
            # --------------------------------------------------- 
            print("  ___________________________________________________", flush=True)
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------   
        
   
def ff_get_fixture_that_not_update_stats(leagueapi_id, season, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_that_not_update_stats()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' leagueapi_id '  
    query += ' , season '  
    query += " , teams_home " 
    query += " , teams_away " 
    query += ' , date '   
    query += 'FROM football_fixtures' 
    query += " WHERE leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and shots_on_goal_home is null "
    query += " and shots_on_goal_away is null "
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
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  

        teams_home         = str(x[2])  
        teams_away         = str(x[3])  

        date         = str(x[4])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += "#" + leagueapi_id 
        word += " - " + season
        word += " - " + teams_home
        word += " vs " + teams_away
        print(word, flush=True)            

        
def ff_get_fixture_that_not_update_stats(leagueapi_id, season, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_that_not_update_stats()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = ' SELECT  '
    query += ' leagueapi_id '  
    query += ' , season '  
    query += " , teams_home " 
    query += " , teams_away " 
    query += ' , date '   
    query += 'FROM football_fixtures' 
    query += " WHERE leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " and shots_on_goal_home is null "
    query += " and shots_on_goal_away is null "
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
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  

        teams_home         = str(x[2])  
        teams_away         = str(x[3])  

        date         = str(x[4])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += "#" + leagueapi_id 
        word += " - " + season
        word += " - " + teams_home
        word += " vs " + teams_away
        print(word, flush=True)    
    # ----------------------------------------------------------     
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        # ------------------------------------------------------  
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            leagueapi_id   = str(x[0])  
            season         = str(x[1])  

            teams_home         = str(x[2])  
            teams_away         = str(x[3])  

            date         = str(x[4])  
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += "#" + leagueapi_id 
            word += " - " + season
            word += " - " + teams_home
            word += " vs " + teams_away
            print(word, flush=True)    
            # --------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------   
        
def ff_get_fixture_that_not_update_stats_with_team(teamapi_id, leagueapi_id, season, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ff_get_fixture_that_not_update_stats_with_team()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query1 = ' SELECT  '
    query1 += ' leagueapi_id '  
    query1 += ' , season '  
    query1 += " , teams_home " 
    query1 += " , teams_away " 
    query1 += ' , date '   
    query1 += 'FROM football_fixtures' 
    query1 += " WHERE leagueapi_id = '"+str(leagueapi_id)+"' "
    query1 += " and season = '"+str(season)+"' "
    query1 += " and teams_home_id = '"+str(teamapi_id)+"' "
    query1 += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query1 += " and shots_on_goal_home is null "
    query1 += " and shots_on_goal_away is null "

    
    query2 = ' SELECT  '
    query2 += ' leagueapi_id '  
    query2 += ' , season '  
    query2 += " , teams_home " 
    query2 += " , teams_away " 
    query2 += ' , date '   
    query2 += 'FROM football_fixtures' 
    query2 += " WHERE leagueapi_id = '"+str(leagueapi_id)+"' "
    query2 += " and season = '"+str(season)+"' "
    query2 += " and teams_away_id = '"+str(teamapi_id)+"' "
    query2 += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query2 += " and shots_on_goal_home is null "
    query2 += " and shots_on_goal_away is null "

    query = "(" + query1 + ") union (" + query2 + ") order by date asc"


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
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  

        teams_home         = str(x[2])  
        teams_away         = str(x[3])  

        date         = str(x[4])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += "#" + leagueapi_id 
        word += " - " + season
        word += " - " + teams_home
        word += " vs " + teams_away
        print(word, flush=True)    
    # ----------------------------------------------------------     
    continue_ = input(space + "Are you sure want to continue? :  ")
    # ----------------------------------------------------------   
    counter = 0
    # ----------------------------------------------------------  
    if(total_rows > 0 and continue_ == 'yes'):   
        # ------------------------------------------------------  
        for x in result:    
            # --------------------------------------------------
            counter        += 1
            leagueapi_id   = str(x[0])  
            season         = str(x[1])  

            teams_home         = str(x[2])  
            teams_away         = str(x[3])  

            date         = str(x[4])  
            # ------------------------------------------------------
            word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
            word += "#" + leagueapi_id 
            word += " - " + season
            word += " - " + teams_home
            word += " vs " + teams_away
            print(word, flush=True)    
            # --------------------------------------------------- 