# Import
import mysql.connector 

def roags_ultimate(today, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_ultimate()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "SELECT "
    query += " leagueapi_id " 
    query += " , season  " 
    query += " , fixtureapi_id  "
    query += "FROM `football_odds` "
    query += "where  pre_anytime_goal_scorer is not null "
    query += "and end_anytime_goal_scorer is not null "
    query += "and leagueapi_id not in "
    query += "(SELECT `leagueapi_id` "
    query += "FROM `football_leagues` "
    query += "where `research_on_anytime_goal_scorers_updated_at` is not null) "
    query += "group by leagueapi_id " 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query, flush=True)
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
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        fixtureapi_id      = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " __ " + fixtureapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        roags_get(leagueapi_id, today, space) 
        # ------------------------------------------------------
        roags_league_update(leagueapi_id, space) 
    # ---------------------------------------------------------- 

def roags_today(day0, day1, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_today()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id " 
    query += " , season  " 
    query += " , fixtureapi_id  "
    query += " from football_fixtures " 
    query += " where Date(date) >= Date('"+str(day0)+"')  "
    query += " and Date(date) <= Date('"+str(day1)+"') " 
    query += " and research_on_anytime_goal_scorers_updated_at is null " 
    query += " order by date desc " 
    # query += " limit 10 " 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query, flush=True)
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
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        fixtureapi_id      = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " __ " + fixtureapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        roags_odds(leagueapi_id, season, fixtureapi_id, space)
    # ---------------------------------------------------------- 

def roags_get(leagueapi_id, today, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_get()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id " 
    query += " , season  " 
    query += " , fixtureapi_id  "
    query += " from football_fixtures " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and Date(date) <= Date('"+str(today)+"') " 
    query += " and research_on_anytime_goal_scorers_updated_at is null " 
    query += " order by date desc " 
    # query += " limit 10 " 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query, flush=True)
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
        leagueapi_id   = str(x[0])  
        season         = str(x[1])  
        fixtureapi_id      = str(x[2])  
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " __ " + fixtureapi_id 
        print(word, flush=True)    
        # ------------------------------------------------------
        roags_odds(leagueapi_id, season, fixtureapi_id, space)
    # ---------------------------------------------------------- 
 
def roags_odds(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_odds()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id " 
    query += " , season  " 
    query += " , fixtureapi_id  "
    query += " , pre_anytime_goal_scorer  "
    query += " , end_anytime_goal_scorer  "
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "  
    query += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query, flush=True)
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
        leagueapi_id    = str(x[0])  
        season          = str(x[1])  
        fixtureapi_id   = str(x[2])  
        # ------------------------------------------------------
        pre_anytime_goal_scorer     = str(x[3])  
        end_anytime_goal_scorer     = str(x[4])  
        # ------------------------------------------------------
        # word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        # word += " #" + leagueapi_id 
        # word += " - " + season 
        # word += " __ " + fixtureapi_id 
        # print(word, flush=True)    
        # ------------------------------------------------------ 
        array_pre_anytime_goal_scorer = pre_anytime_goal_scorer.split(";")
        roags_array(array_pre_anytime_goal_scorer, 'pre', leagueapi_id, season, fixtureapi_id, space)        
        # ------------------------------------------------------  
        array_end_anytime_goal_scorer = end_anytime_goal_scorer.split(";")
        roags_array(array_end_anytime_goal_scorer, 'end', leagueapi_id, season, fixtureapi_id, space)
        # ------------------------------------------------------  

        # ------------------------------------------------------   
        if(x[4] is not None):
            # --------------------------------------------------    
            host="localhost"
            user="root" 
            database="pr_mmbuzz_2022_06"
            mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
            mycursor = mydb.cursor()
            # --------------------------------------------------     
            query_commit = "UPDATE `football_fixtures` SET "
            # --------------------------------------------------    
            query_commit += " `research_on_anytime_goal_scorers_updated_at` = now() "
            # --------------------------------------------------    
            query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
            query_commit += " and season = "+str(season)+" "   
            query_commit += " and fixtureapi_id = "+str(fixtureapi_id)+" "    
            # --------------------------------------------------    
            print(space + query_commit, flush=True) 
            # --------------------------------------------------    
            mycursor.execute(query_commit)
            mydb.commit()     
            # --------------------------------------------------     
            mycursor.close()
            mydb.close()
            # --------------------------------------------------    
        # ------------------------------------------------------    
    # ---------------------------------------------------------- 
 
def roags_array(array_AGS, prep, leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_array()", flush=True)
    # ----------------------------------------------------------  
    for row in array_AGS:
        # ------------------------------------------------------ 
        value_and_odd   = row.split(":")
        # ------------------------------------------------------ 
        # print(space + str(len(value_and_odd)), flush=True)
        # ------------------------------------------------------ 
        if(len(value_and_odd) == 2): 
            # -------------------------------------------------- 
            value           = value_and_odd[0]
            odd             = value_and_odd[1]
            # -------------------------------------------------- 
            if(float(odd) <= 2.20):
                # ---------------------------------------------- 
                word = value + " - " + str(odd)
                print(space + word, flush=True)
                # ---------------------------------------------- 
                roags_insert_or_update(leagueapi_id, season,
                            fixtureapi_id,
                            value,
                            odd,
                            prep,
                            space)
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
 
def roags_insert_or_update(leagueapi_id, season,
                            fixtureapi_id,
                            value,
                            odd,
                            prep,
                            space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_insert_or_update()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select  * " 
    query += " from research_on_anytime_goal_scorers "    
    query += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query += " and season = "+str(season)+" "    
    query += " and fixtureapi_id = "+str(fixtureapi_id)+" "    
    query += " and value = '"+str(value).replace("'", "\\'") +"' "    
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------   
    # 
    # 
    # ----------------------------------------------------------    
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # ------------------------------------------------------ 
        query_commit = "INSERT INTO `research_on_anytime_goal_scorers`( "
        # ------------------------------------------  
        query_commit += " `leagueapi_id`, "
        query_commit += " `season`, "
        query_commit += " `fixtureapi_id`, "  
        query_commit += " `value`, " 

        if(prep == "pre"): 
            query_commit += " `pre_odd`, " 
        elif(prep == "end"): 
            query_commit += " `end_odd`, " 
 
        # ------------------------------------------------------  
        query_commit += " `created_at` "   
        # ------------------------------------------------------  
        query_commit += " ) VALUES ( "
        # ------------------------------------------------------ 
        query_commit += " " + str(leagueapi_id) + ", " 
        query_commit += " '" + str(season) + "', " 
        query_commit += " '" + str(fixtureapi_id) + "', "  
        query_commit += " '" + str(value).replace("'", "\\'") + "', "    
        query_commit += " '" + str(odd) + "', "   
        query_commit += " current_timestamp ) "     
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True)
        # ------------------------------------------------------  
        mycursor.execute(query_commit)
        mydb.commit()     
        # ------------------------------------------------------  
    # ----------------------------------------------------------  
    elif(total_rows == 1): 
        # ------------------------------------------------------  
        query_commit = "UPDATE `research_on_anytime_goal_scorers` SET "
        # ------------------------------------------------------    
        if(prep == "pre"): 
            query_commit += " `pre_odd` = '"+str(odd)+"', "
        elif(prep == "end"): 
            query_commit += " `end_odd` = '"+str(odd)+"', " 
        # ------------------------------------------------------
        query_commit += " `updated_at` = now() "
        # ------------------------------------------------------
        query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
        query_commit += " and season = "+str(season)+" "   
        query_commit += " and fixtureapi_id = "+str(fixtureapi_id)+" "   
        query_commit += " and value = '"+str(value).replace("'", "\\'")+"' "   
        # ------------------------------------------------------ 
        print(space + query_commit, flush=True) 
        # ------------------------------------------------------  
        mycursor.execute(query_commit)
        mydb.commit()     
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------       

def roags_league_update(leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "roags_league_update()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------     
    query_commit = "UPDATE `football_leagues` SET "
    # ----------------------------------------------------------    
    query_commit += " `research_on_anytime_goal_scorers_updated_at` = now() "
    # ----------------------------------------------------------   
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "      
    # ----------------------------------------------------------   
    print(space + query_commit, flush=True) 
    # ----------------------------------------------------------   
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------       