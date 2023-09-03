# Import
import mysql.connector 

def ffp_get_fixtures_today(date_0, date_1, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ffp_get_fixtures_today()", flush=True)
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
    query += " date " 
    query += " , fixtureapi_id "   

    query += " , pre_ah_pattern " 
    query += " , pre_ah_pattern_mirror " 
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern " 
    query += " , end_ah_pattern_mirror " 
    query += " , end_gou_pattern "  

    query += " , leagueapi_id "  
    query += " , season "  
 
    query += " from football_odds " 

    query += " where date >= DATE('"+str(date_0)+"') " 
    query += " and date <= DATE('"+str(date_1)+"') " 

    query += " and fixture_status not in ('Match Finished', 'Match Finished Ended') "  
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
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter             += 1
        # ------------------------------------------------------
        date      = str(x[0]) 
        fixtureapi_id     = str(x[1])   
        # ------------------------------------------------------ 
        pre_ah_pattern          = str(x[2])   
        pre_ah_pattern_mirror   = str(x[3])   
        pre_gou_pattern         = str(x[4])   
        # ------------------------------------------------------ 
        end_ah_pattern          = str(x[5])   
        end_ah_pattern_mirror   = str(x[6])   
        end_gou_pattern         = str(x[7])   
        # ------------------------------------------------------ 
        leagueapi_id            = str(x[8])   
        season                  = str(x[9])   
        # ------------------------------------------------------ 
        word = space + "[" + str(counter) + "/" + str(total_rows) + "] "  
        word += fixtureapi_id  
        word += " -> " + date     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + "          " + pre_ah_pattern     
        word += " / " + pre_ah_pattern_mirror   
        word += " / " + pre_gou_pattern     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + "          " + end_ah_pattern     
        word += " / " + end_ah_pattern_mirror   
        word += " / " + end_gou_pattern     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = "  "        
        print(word, flush=True)   
        # ------------------------------------------------------ League 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------ Country 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------ World 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------  
    # ----------------------------------------------------------  


def ffp_get_fixtures_by_league(leagueapi_id, season, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ffp_get_fixtures_by_league()", flush=True)
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
    query += " date " 
    query += " , fixtureapi_id "   

    query += " , pre_ah_pattern " 
    query += " , pre_ah_pattern_mirror " 
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern " 
    query += " , end_ah_pattern_mirror " 
    query += " , end_gou_pattern "  
 
    query += " from football_odds " 

    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' " 

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "  
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
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter             += 1
        # ------------------------------------------------------
        date      = str(x[0]) 
        fixtureapi_id     = str(x[1])   
        # ------------------------------------------------------ 
        pre_ah_pattern          = str(x[2])   
        pre_ah_pattern_mirror   = str(x[3])   
        pre_gou_pattern         = str(x[4])   
        # ------------------------------------------------------ 
        end_ah_pattern          = str(x[5])   
        end_ah_pattern_mirror   = str(x[6])   
        end_gou_pattern         = str(x[7])   
        # ------------------------------------------------------ 
        word = space + "[" + str(counter) + "/" + str(total_rows) + "] "  
        word += fixtureapi_id  
        word += " -> " + date     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + "          " + pre_ah_pattern     
        word += " / " + pre_ah_pattern_mirror   
        word += " / " + pre_gou_pattern     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = space + "          " + end_ah_pattern     
        word += " / " + end_ah_pattern_mirror   
        word += " / " + end_gou_pattern     
        print(word, flush=True)   
        # ------------------------------------------------------  
        word = "  "        
        print(word, flush=True)   
        # ------------------------------------------------------ League 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------ Country 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "country_blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------ World 
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_blank", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_blank_pre", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_pre_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_pre_blank_mirror", space)
        # ------------------------------------------------------  
        ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, 
                          pre_ah_pattern, pre_gou_pattern, 
                          end_ah_pattern, end_gou_pattern, 
                          "world_blank_pre_mirror", space)
        # ------------------------------------------------------  
        # ------------------------------------------------------  
    # ----------------------------------------------------------   

    
def ffp_check_pattern(leagueapi_id, season, fixtureapi_id, date, pre_ah, pre_gou, end_ah, end_gou, pattern_status, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "ffp_check_pattern()", flush=True)
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
    query += " date " 
    query += " , fixtureapi_id "   

    query += " , pre_ah_pattern " 
    query += " , pre_ah_pattern_mirror " 
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern " 
    query += " , end_ah_pattern_mirror " 
    query += " , end_gou_pattern "  
 
    query += " from football_odds " 

    # query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # query += " and season = '"+str(season)+"' " 
    
    # ---------------------------------------------------------- League  
    if(pattern_status == "pre_pre"): 
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 

    elif(pattern_status == "pre_blank"):
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

    elif(pattern_status == "blank_pre"): 
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and end_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
 
    elif(pattern_status == "pre_pre_mirror"):
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern_mirror = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 
 
    elif(pattern_status == "pre_blank_mirror"):
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' "  
 
    elif(pattern_status == "blank_pre_mirror"):  
        query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
        # query += " and season = '"+str(season)+"' " 

        query += " and end_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
    # ----------------------------------------------------------   
    # ---------------------------------------------------------- Country  
    elif(pattern_status == "country_pre_pre"): 
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 

    elif(pattern_status == "country_pre_blank"):
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

    elif(pattern_status == "country_blank_pre"): 
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and end_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
 
    elif(pattern_status == "country_pre_pre_mirror"):
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern_mirror = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 
 
    elif(pattern_status == "country_pre_blank_mirror"):
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' "  
 
    elif(pattern_status == "country_blank_pre_mirror"):  
        query += " where leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE  `country_name` like (SELECT country_name FROM `football_leagues` WHERE `leagueapi_id` = '"+str(leagueapi_id)+"')) " 
        # query += " and season = '"+str(season)+"' " 

        query += " and end_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- World  
    elif(pattern_status == "world_pre_pre"):  
        query += " where pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 

    elif(pattern_status == "world_pre_blank"): 
        query += " where pre_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

    elif(pattern_status == "world_blank_pre"):  
        query += " where end_ah_pattern = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
 
    elif(pattern_status == "world_pre_pre_mirror"): 
        query += " where pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

        query += " and end_ah_pattern_mirror = '"+str(end_ah)+"' " 
        query += " and end_gou_pattern = '"+str(end_gou)+"' " 
 
    elif(pattern_status == "world_pre_blank_mirror"): 
        query += " where pre_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and pre_gou_pattern = '"+str(pre_gou)+"' "  
 
    elif(pattern_status == "world_blank_pre_mirror"):   
        query += " where end_ah_pattern_mirror = '"+str(pre_ah)+"' " 
        query += " and end_gou_pattern = '"+str(pre_gou)+"' " 
    # ---------------------------------------------------------- 

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "  
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
    # close the cursor and database connection
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------
    if(total_rows > 2):
        # ------------------------------------------------------
        total_ffp = ffp_check(leagueapi_id, season, fixtureapi_id, space) 
        # ------------------------------------------------------
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------
        if(total_ffp > 0):
            # --------------------------------------------------
            query_commit = "update football_forecast_pattern set "  
            # --------------------------------------------------  
            query_commit += " forecast_"+pattern_status+" = '"+str(total_rows)+"', " 
            query_commit += " updated_at = current_timestamp "  
            # --------------------------------------------------
            query_commit += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
            query_commit += " and season = '"+str(season)+"' "  
            query_commit += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
            # --------------------------------------------------
            mycursor.execute(query_commit)
            mydb.commit()  
            # --------------------------------------------------
            print(space + "football_forecast_pattern UPDATED", flush=True) 
            # --------------------------------------------------
        elif(total_ffp == 0):
            # --------------------------------------------------
            query_commit = "INSERT INTO `football_forecast_pattern`( "
            # --------------------------------------------------
            query_commit += " `date`, " 
            query_commit += " `leagueapi_id`, "
            query_commit += " `season`, "
            query_commit += " `fixtureapi_id`, "
            query_commit += " `forecast_"+pattern_status+"`, "
            # --------------------------------------------------
            query_commit += " `created_at` "   
            # --------------------------------------------------
            query_commit += " ) VALUES ( "
            # --------------------------------------------------
            query_commit += " '" + str(date) + "', "  
            query_commit += " '" + str(leagueapi_id) + "', " 
            query_commit += " '" + str(season) + "', " 
            query_commit += " '" + str(fixtureapi_id) + "', " 
            query_commit += " '" + str(total_rows) + "', " 
            # --------------------------------------------------
            query_commit += " current_timestamp "    
            # --------------------------------------------------
            query_commit += " ) "
            # --------------------------------------------------
            mycursor.execute(query_commit)
            mydb.commit()   
            # --------------------------------------------------
            print(space + "football_forecast_pattern INSERTED", flush=True) 
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
        mycursor.close()
        mydb.close() 
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------


def ffp_check(leagueapi_id, season, fixtureapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "ffp_check()", flush=True) 
    # ----------------------------------------------------------   
    print(space + "leagueapi_id : " + str(leagueapi_id), flush=True)  
    print(space + "season : " + str(season), flush=True)  
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
    query += " from football_forecast_pattern "    
    query += " where leagueapi_id = "+str(leagueapi_id)+" "   
    query += " and season = "+str(season)+" "  
    query += " and fixtureapi_id = "+str(fixtureapi_id)+" "   
    # ----------------------------------------------------------    
    # print(space + query, flush=True)
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