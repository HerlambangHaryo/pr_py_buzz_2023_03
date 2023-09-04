# Import
import mysql.connector  
from a_models.api_fixtures_new_2 import *   

def fxs_check_fixture_statistics_updated_at(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fxs_check_fixture_statistics_updated_at()", flush=True)
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
    query += " , season  "  
    query += " , fixtureapi_id  " 
    query += " from football_fixtures " 
    query += " where fixture_status in ('Match Finished', 'Match Finished Ended') "  
    query += " and fixture_statistics_updated_at is null " 
    query += " and leagueapi_id IN (SELECT leagueapi_id FROM `football_leagues` WHERE `detail_stats` = 1 order by star desc, leagueapi_id asc) "
    # query += " and fixtureapi_id = '1035046' " 
    query += " order by date desc "  
    # query += " limit 500 "  
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------   
    space += "__"
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
        # ------------------------------------------------------
        leagueapi_id   = str(x[0])  
        season         = str(x[1])    
        fixtureapi_id  = str(x[2])  
        # ------------------------------------------------------
        word = "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season 
        word += " -> " + fixtureapi_id 
        print(space + word, flush=True)    
        # ------------------------------------------------------
        update_or_insert = fxs_check_fixture_statistics(leagueapi_id, season, fixtureapi_id, space)
        # ------------------------------------------------------
        if(update_or_insert == 0):
            # --------------------------------------------------
            word = "__INSERT_"
            # --------------------------------------------------
            print(space + word, flush=True)     
            # --------------------------------------------------
            ROUTES = 'fixtureapi_id'
            word = space + " ROUTES: " + ROUTES  
            print(word, flush=True)      
            # --------------------------------------------------
            DICT = {
                'fixtureapi_id' :fixtureapi_id,  
            }
            # --------------------------------------------------
            afN2_controll_match_update(DICT, ROUTES, space) 
            # --------------------------------------------------
        # ------------------------------------------------------
        elif(update_or_insert == 1):
            # --------------------------------------------------
            word = "________UPDATED_"
            # --------------------------------------------------
            print(space + word, flush=True)    
            # --------------------------------------------------
            # fxs_update_data(leagueapi_id, season, fixtureapi_id, space + "________")
            
            # --------------------------------------------------
            ROUTES = 'fixtureapi_id'
            word = space + " ROUTES: " + ROUTES  
            print(word, flush=True)      
            # --------------------------------------------------
            DICT = {
                'fixtureapi_id' :fixtureapi_id,  
            }
            # --------------------------------------------------
            afN2_controll_match_update(DICT, ROUTES, space) 
        # ------------------------------------------------------
        print(space, flush=True)    
    # ---------------------------------------------------------- 
 
def fxs_check_fixture_statistics(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fxs_check_fixture_statistics()", flush=True)
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
    query += " *  " 
    query += " from football_statistics " 
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
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "total_rows: " + str(total_rows), flush=True)
    # ----------------------------------------------------------
    return total_rows     
    # ----------------------------------------------------------  
 
def fxs_update_data(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fxs_update_data()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query_commit = "UPDATE `football_fixtures` SET " 
    # ------------------------------------------------------
    query_commit += " `fixture_statistics_updated_at` = now() "
    # ------------------------------------------------------
    query_commit += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    query_commit += " and season = '"+str(season)+"' "
    query_commit += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + "football_fixtures UPDATED", flush=True)
    # ----------------------------------------------------------   
    mycursor.execute(query_commit)
    mydb.commit()      
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------  

    