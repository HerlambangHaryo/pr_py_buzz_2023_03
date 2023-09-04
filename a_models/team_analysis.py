# Import
import mysql.connector  
from a_models.date import *  
  

def ta_analyze_roundx(leagueapi_id, season, roundx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ta_analyze_roundx()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------   
    query = "Select "
    query += " fixtureapi_id "   
    query += " ,  leagueapi_id "   
    query += " ,  season "   
    query += " ,  date "   
    query += " ,  teams_homeapi_id "   
    query += " ,  teams_awayapi_id "   
    query += " ,  round "   
    query += " from football_fixtures " 
    query += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query += " and season = "+str(season)+" "       
    query += " and round = '"+str(roundx)+"' "      
    # ----------------------------------------------------------   
    space += "__" 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        fixtureapi_id   = str(x[0])   
        leagueapi_id    = str(x[1])   
        season          = str(x[2])   
        date            = str(x[3])   
        # ------------------------------------------------------
        teams_homeapi_id    = str(x[4])   
        teams_awayapi_id    = str(x[5])   
        # ------------------------------------------------------
        roundx          = str(x[6])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " __ " + season  
        word += " __ " + fixtureapi_id  
        word += " __ " + date  
        word += " __ " + roundx  
        print(word, flush=True)    
        # ------------------------------------------------------
        ta_analyze_details(date, leagueapi_id, season, fixtureapi_id, teams_homeapi_id, "home", space)
        ta_analyze_details(date, leagueapi_id, season, fixtureapi_id, teams_awayapi_id, "away", space)
    # ----------------------------------------------------------  

def ta_analyze_today(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ta_analyze_today()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    pre_query = "Select leagueapi_id from football_leagues where team_statistics = 1 "
    # ----------------------------------------------------------   
    query = "Select "
    query += " fixtureapi_id "   
    query += " ,  leagueapi_id "   
    query += " ,  season "   
    query += " ,  date "   
    query += " ,  teams_homeapi_id "   
    query += " ,  teams_awayapi_id "   
    query += " ,  round "   
    query += " from football_fixtures " 
    query += " where DATE(date) >= DATE('"+day1+"') "
    query += " and DATE(date) <= DATE('"+day2+"') "
    query += " and leagueapi_id IN ("+pre_query+") "    
    # ----------------------------------------------------------   
    space += "__" 
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        fixtureapi_id   = str(x[0])   
        leagueapi_id    = str(x[1])   
        season          = str(x[2])   
        date            = str(x[3])   
        # ------------------------------------------------------
        teams_homeapi_id    = str(x[4])   
        teams_awayapi_id    = str(x[5])   
        # ------------------------------------------------------
        roundx          = str(x[6])   
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " __ " + season  
        word += " __ " + fixtureapi_id  
        word += " __ " + date  
        word += " __ " + roundx  
        print(word, flush=True)    
        # ------------------------------------------------------
        ta_analyze_details(date, leagueapi_id, season, fixtureapi_id, teams_homeapi_id, "home", space)
        ta_analyze_details(date, leagueapi_id, season, fixtureapi_id, teams_awayapi_id, "away", space)
    # ----------------------------------------------------------  
 
def ta_analyze_details(date, leagueapi_id, season, fixtureapi_id, teamapi_id, statusx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ta_analyze_details()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------     
    query = "SELECT "
    # ----------------------------------------------------------    
    query += " SUM(corner) "
    query += " , AVG(corner) "  
    # ----------------------------------------------------------    
    query += " , SUM(total_shots) "
    query += " , AVG(total_shots) "  
    # ----------------------------------------------------------    
    query += " , SUM(shots_on_goal) "
    query += " , AVG(shots_on_goal) "  
    # ----------------------------------------------------------    
    query += " , SUM(fouls) "
    query += " , AVG(fouls) "  
    # ----------------------------------------------------------    
    query += " , SUM(offsides) "
    query += " , AVG(offsides) "  
    # ----------------------------------------------------------    
    query += " , MAX(corner) "
    query += " , MIN(corner) "  
    # ----------------------------------------------------------    
    query += " , MAX(total_shots) "
    query += " , MIN(total_shots) "  
    # ----------------------------------------------------------    
    query += " , MAX(shots_on_goal) "
    query += " , MIN(shots_on_goal) "  
    # ----------------------------------------------------------    
    query += " , MAX(fouls) "
    query += " , MIN(fouls) "  
    # ----------------------------------------------------------    
    query += " , MAX(offsides) "
    query += " , MIN(offsides) "  
    # ----------------------------------------------------------   
    query += " FROM " 
    # ----------------------------------------------------------    
    query += " ( "
    query += " ( "
    query += " Select "
    query += " fixtureapi_id "   
    query += " ,  leagueapi_id "   
    query += " ,  season "   
    query += " ,  date "   
    query += " ,  'Home' as statusx "   
    # ----------------------------------------------------------  
    query += " ,  corner_kicks_home as corner "   
    query += " ,  total_shots_home as total_shots " 
    query += " ,  shots_on_goal_home as shots_on_goal " 
    query += " ,  fouls_home as fouls " 
    query += " ,  offsides_home as offsides " 
    # ----------------------------------------------------------  
    query += " from football_statistics " 
    query += " where  DATE(date) <= DATE('"+date+"') "
    query += " and leagueapi_id = "+leagueapi_id+" "    
    query += " and season = "+season+" "       
    query += " and teams_homeapi_id = "+teamapi_id+" "    
    query += " ) union ( "    
    query += " Select "
    query += " fixtureapi_id "   
    query += " ,  leagueapi_id "   
    query += " ,  season "   
    query += " ,  date "   
    query += " ,  'Away' as statusx "   
    # ----------------------------------------------------------  
    query += " ,  corner_kicks_away as corner "   
    query += " ,  total_shots_away as total_shots " 
    query += " ,  shots_on_goal_away as shots_on_goal " 
    query += " ,  fouls_away as fouls " 
    query += " ,  offsides_away as offsides " 
    # ----------------------------------------------------------  
    query += " from football_statistics " 
    query += " where  DATE(date) <= DATE('"+date+"') "
    query += " and leagueapi_id = "+leagueapi_id+" "    
    query += " and season = "+season+" "       
    query += " and teams_awayapi_id = "+teamapi_id+" "   
    query += " )"    
    query += " ) as CORNERS;"    
    # ----------------------------------------------------------   
    space += "__" 
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    # ----------------------------------------------------------   
    result_check = mycursor.fetchone()
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------   
    corner_kicks_total   = result_check[0]
    corner_kicks_avg     = result_check[1]
    # ----------------------------------------------------------  
    word = "corners: " + str(corner_kicks_total)      
    word += " __ avg: " + str(corner_kicks_avg)      
    print(space + word, flush=True)
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   
    total_shots_total   = result_check[2]
    total_shots_avg     = result_check[3]
    # ----------------------------------------------------------  
    word = "total_shots: " + str(total_shots_total)      
    word += " __ avg: " + str(total_shots_avg)      
    print(space + word, flush=True)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------   
    shots_on_goal_total   = result_check[4]
    shots_on_goal_avg     = result_check[5]
    # ----------------------------------------------------------  
    word = "shots_on_goal: " + str(shots_on_goal_total)      
    word += " __ avg: " + str(shots_on_goal_avg)      
    print(space + word, flush=True)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------   
    fouls_total   = result_check[6]
    fouls_avg     = result_check[7]
    # ----------------------------------------------------------  
    word = "fouls: " + str(fouls_total)      
    word += " __ avg: " + str(fouls_avg)      
    print(space + word, flush=True)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------   
    offsides_total   = result_check[8]
    offsides_avg     = result_check[9]
    # ----------------------------------------------------------  
    word = "offsides: " + str(offsides_total)      
    word += " __ avg: " + str(offsides_avg)      
    print(space + word, flush=True) 
    # ----------------------------------------------------------   
    corner_kicks_max    = result_check[10]
    corner_kicks_min    = result_check[11]
    # ----------------------------------------------------------   
    total_shots_max    = result_check[12]
    total_shots_min    = result_check[13]
    # ----------------------------------------------------------   
    shots_on_goal_max    = result_check[14]
    shots_on_goal_min    = result_check[15]
    # ----------------------------------------------------------   
    fouls_max    = result_check[16]
    fouls_min    = result_check[17]
    # ----------------------------------------------------------   
    offsides_max    = result_check[18]
    offsides_min    = result_check[19] 
    # ----------------------------------------------------------     
    # ----------------------------------------------------------  
    print("", flush=True) 
    # ----------------------------------------------------------  
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
    query_commit = "UPDATE `api_football_league_standings` SET "
    # ----------------------------------------------------------  
    query_commit += " `corner_kicks_total` = "+str(corner_kicks_total)+", "
    query_commit += " `corner_kicks_avg` = "+str(corner_kicks_avg)+", "
    query_commit += " `corner_kicks_max` = "+str(corner_kicks_max)+", "
    query_commit += " `corner_kicks_min` = "+str(corner_kicks_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `total_shots_total` = "+str(total_shots_total)+", "
    query_commit += " `total_shots_avg` = "+str(total_shots_avg)+", "
    query_commit += " `total_shots_max` = "+str(total_shots_max)+", "
    query_commit += " `total_shots_min` = "+str(total_shots_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `shots_on_goal_total` = "+str(shots_on_goal_total)+", "
    query_commit += " `shots_on_goal_avg` = "+str(shots_on_goal_avg)+", "
    query_commit += " `shots_on_goal_max` = "+str(shots_on_goal_max)+", "
    query_commit += " `shots_on_goal_min` = "+str(shots_on_goal_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `fouls_total` = "+str(fouls_total)+", "
    query_commit += " `fouls_avg` = "+str(fouls_avg)+", "
    query_commit += " `fouls_max` = "+str(fouls_max)+", "
    query_commit += " `fouls_min` = "+str(fouls_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `offsides_total` = "+str(offsides_total)+", "
    query_commit += " `offsides_avg` = "+str(offsides_avg)+", " 
    query_commit += " `offsides_max` = "+str(offsides_max)+", "
    query_commit += " `offsides_min` = "+str(offsides_min)+", " 
    # ----------------------------------------------------------   
    query_commit += " `updated_at` = now() "
    # ----------------------------------------------------------  
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query_commit += " and season = "+str(season)+" "   
    query_commit += " and teamapi_id = "+str(teamapi_id)+" "    
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
    # ----------------------------------------------------------  


    
    # ----------------------------------------------------------  
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
    query_commit = "UPDATE `football_statistics` SET "
    # ----------------------------------------------------------  
    query_commit += " `corner_kicks_total_"+statusx+"` = "+str(corner_kicks_total)+", "
    query_commit += " `corner_kicks_avg_"+statusx+"` = "+str(corner_kicks_avg)+", "
    query_commit += " `corner_kicks_max_"+statusx+"` = "+str(corner_kicks_max)+", "
    query_commit += " `corner_kicks_min_"+statusx+"` = "+str(corner_kicks_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `total_shots_total_"+statusx+"` = "+str(total_shots_total)+", "
    query_commit += " `total_shots_avg_"+statusx+"` = "+str(total_shots_avg)+", "
    query_commit += " `total_shots_max_"+statusx+"` = "+str(total_shots_max)+", "
    query_commit += " `total_shots_min_"+statusx+"` = "+str(total_shots_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `shots_on_goal_total_"+statusx+"` = "+str(shots_on_goal_total)+", "
    query_commit += " `shots_on_goal_avg_"+statusx+"` = "+str(shots_on_goal_avg)+", "
    query_commit += " `shots_on_goal_max_"+statusx+"` = "+str(shots_on_goal_max)+", "
    query_commit += " `shots_on_goal_min_"+statusx+"` = "+str(shots_on_goal_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `fouls_total_"+statusx+"` = "+str(fouls_total)+", "
    query_commit += " `fouls_avg_"+statusx+"` = "+str(fouls_avg)+", "
    query_commit += " `fouls_max_"+statusx+"` = "+str(fouls_max)+", "
    query_commit += " `fouls_min_"+statusx+"` = "+str(fouls_min)+", "
    # ----------------------------------------------------------  
    query_commit += " `offsides_total_"+statusx+"` = "+str(offsides_total)+", "
    query_commit += " `offsides_avg_"+statusx+"` = "+str(offsides_avg)+", " 
    query_commit += " `offsides_max_"+statusx+"` = "+str(offsides_max)+", "
    query_commit += " `offsides_min_"+statusx+"` = "+str(offsides_min)+", " 
    # ----------------------------------------------------------   
    query_commit += " `updated_at` = now() "
    # ----------------------------------------------------------  
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query_commit += " and season = "+str(season)+" "   
    query_commit += " and fixtureapi_id = "+str(fixtureapi_id)+" "    
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
    # ----------------------------------------------------------  

     