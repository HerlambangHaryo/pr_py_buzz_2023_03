# Import
import mysql.connector 
from a_models.football_ultimate_assessment import *   
from a_models.football_odds import *   
from a_models.football_pattern_assessment import *   
 
 
def fp_group_by_league_season_to_update_pattern(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_group_by_league_season_to_update_pattern()", flush=True)
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
    query += " leagueapi_id  "   
    query += " , season  "
    query += " from football_odds " 
    query += " where DATE(date) >= '"+str(day1)+"' " 
    query += " and DATE(date) <= '"+str(day2)+"' " 
    query += " group by leagueapi_id , season "  
    # query += " limit 1 "  
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
        counter             += 1
        # ------------------------------------------------------
        leagueapi_id        = str(x[0])   
        season              = str(x[1])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " - " + season    
        print(word, flush=True)      
        # ------------------------------------------------------
        fo_delete_football_pattern(leagueapi_id, space) 
        # ------------------------------------------------------
        fo_group_pattern(leagueapi_id, space)
    # ----------------------------------------------------------  

def fp_group_by_league_season(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fo_controll_predates()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " leagueapi_id  "   
    query += " , season  "
    query += " from football_odds " 
    query += " where DATE(date) >= '"+str(day1)+"' " 
    query += " and DATE(date) <= '"+str(day2)+"' " 
    query += " group by leagueapi_id , season "  
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
        leagueapi_id        = str(x[0])   
        season              = str(x[1])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " - " + season    
        print(word, flush=True)     
        # ------------------------------------------------------
        fp_not_started_goto(leagueapi_id, season, space)
    # ----------------------------------------------------------  
 
def fp_not_started_goto(leagueapi_id, season, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_not_started_goto()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " fixtureapi_id  "   

    query += " , pre_ah_pattern  "
    query += " , pre_gou_pattern  "
    query += " , pre_ah_pattern_mirror  "

    query += " , pre_ah_pattern_4  "
    query += " , pre_gou_pattern_4  "
    query += " , pre_ah_pattern_mirror_4  "
    
    query += " , date  "

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    query += " and season = '"+str(season)+"' " 
    query += " and fixture_status  = 'Not Started Goto' " 
    query += " and pre_response >= 2 "  
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
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    counter = 0
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1
        # ------------------------------------------------------
        fixtureapi_id           = str(x[0])   
        # ------------------------------------------------------
        pre_ah_pattern          = str(x[1])    
        pre_gou_pattern         = str(x[2])    
        pre_ah_pattern_mirror   = str(x[3])     
        # ------------------------------------------------------
        date                    = str(x[7])     
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fixtureapi_id  
        word += " __ " + pre_ah_pattern    
        word += " __ " + pre_gou_pattern     
        print(word, flush=True)     
        # ------------------------------------------------------
        original    = fp_check_all_around(leagueapi_id, pre_ah_pattern, pre_gou_pattern, "league", 'preend', space)
        mirror      = fp_check_all_around(leagueapi_id, pre_ah_pattern_mirror, pre_gou_pattern, "league mirror", 'preend', space)
        # ------------------------------------------------------ 
        total_DATA  = original + mirror
        # ------------------------------------------------------ 
        if(total_DATA > 2) :
            # -------------------------------------------------- 
            fua_update_or_insert(leagueapi_id, 
                        season, 
                        fixtureapi_id, 
                        date, 
                        "total_pattern_form_pre_end_league", 
                        total_DATA, 
                        space)
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
        else :
            # -------------------------------------------------- 
            print(space + "total_DATA under 2", flush=True)
            # -------------------------------------------------- 
        # ------------------------------------------------------  
        print("", flush=True)     
    # ----------------------------------------------------------  

def fp_check_all_around(leagueapi_id, pre_ah, pre_gou, STATUS, TYPE, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_check_all_around() " + STATUS, flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " count(*)  "   

    query += " , pre_ah_pattern  "
    query += " , pre_gou_pattern  "
    query += " , pre_ah_pattern_mirror  " 

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 

    query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
    query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

    query += " and end_ah_pattern = '"+str(pre_ah)+"' " 
    query += " and end_gou_pattern = '"+str(pre_gou)+"' " 

    query += " and fixture_status  like '%Match Finished%' "  

    query += " group by pre_ah_pattern, pre_gou_pattern "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    result = mycursor.fetchone()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    if result is not None:
        # ------------------------------------------------------   
        return result[0]
    # ----------------------------------------------------------   
    elif result is None:
        # ------------------------------------------------------   
        return 0
        # ------------------------------------------------------    
        # ------------------------------------------------------   
        # ------------------------------------------------------   
    # ---------------------------------------------------------- 
 
def fp_all_leagues(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_all_leagues()", flush=True)
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
    query += " leagueapi_id  "   

    query += " , pre_ah_pattern "  
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern "  
    query += " , end_gou_pattern "  

    query += " , pre_ah_pattern_mirror "  
    query += " , end_ah_pattern_mirror "  

    query += " , count(*) as counter "  

    query += " , pre_response "  
    query += " , end_response "  

    query += " from football_odds " 

    query += " where football_pattern_from_only_updated_at is null "  
    query += " and fixture_status IN ('Match Finished','Match Finished Ended') "  
    
    query += " and pre_ah_pattern != 'H' "  
    query += " and pre_gou_pattern != 'G' "  

    query += " and end_ah_pattern != 'H' "  
    query += " and end_gou_pattern != 'G' "  
 
    query += " and pre_response = 3 "  
    query += " and end_response = 3 "  

    query += " group by "  
    query += " leagueapi_id  "   

    query += " , pre_ah_pattern "  
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern "  
    query += " , end_gou_pattern "  

    query += " , pre_ah_pattern_mirror "  
    query += " , end_ah_pattern_mirror "  
    
    query += " , pre_response "  
    query += " , end_response "  

    query += " HAVING COUNT(*) > 2 "  
    query += " ORDER BY COUNT(*)  DESC "  
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
        leagueapi_id        = str(x[0])    
        # ------------------------------------------------------
        pre_ah_pattern          = str(x[1])   
        pre_gou_pattern         = str(x[2])    
        # ------------------------------------------------------
        end_ah_pattern          = str(x[3])   
        end_gou_pattern         = str(x[4])    
        # ------------------------------------------------------
        pre_ah_pattern_mirror       = str(x[5])   
        end_ah_pattern_mirror       = str(x[6])    
        # ------------------------------------------------------
        counter_rows       = str(x[7])    
        # ------------------------------------------------------
        pre_response       = str(x[8])   
        end_response       = str(x[9])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " >" + counter_rows   
        word += " #" + leagueapi_id   

        word += " __ " + pre_ah_pattern   
        word += " __ " + pre_gou_pattern   

        word += " __ " + end_ah_pattern   
        word += " __ " + end_gou_pattern   

        word += " __ " + pre_ah_pattern_mirror   
        word += " __ " + end_ah_pattern_mirror   

        word += " __ " + pre_response   
        word += " __ " + end_response  

        print(word, flush=True)    
        # ------------------------------------------------------
        fp_ask_fixtureapi_id(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   


def fp_ask_fixtureapi_id(leagueapi_id, pre_ah, pre_gou, end_ah, end_gou, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_ask_fixtureapi_id() ", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " fixtureapi_id  "    

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 

    query += " and pre_ah_pattern = '"+str(pre_ah)+"' " 
    query += " and pre_gou_pattern = '"+str(pre_gou)+"' " 

    query += " and end_ah_pattern = '"+str(end_ah)+"' " 
    query += " and end_gou_pattern = '"+str(end_gou)+"' " 
    query += " LIMIT 1 " 
    
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    result = mycursor.fetchone()
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    if result is not None:
        # ------------------------------------------------------    
        fp_fixtureapi_id(result[0], space)
        # ------------------------------------------------------   
    # ---------------------------------------------------------- 
    

def fp_fixtureapi_id(fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fp_fixtureapi_id()", flush=True)
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
    query += " leagueapi_id  "  
    query += " , season  "  
    query += " , fixtureapi_id  "  

    query += " , pre_ah_pattern "  
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern "  
    query += " , end_gou_pattern "  

    query += " , pre_ah_pattern_mirror "  
    query += " , end_ah_pattern_mirror "  

    query += " from football_odds " 
    query += " where fixtureapi_id = '"+str(fixtureapi_id)+"' "  
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
        leagueapi_id        = str(x[0])   
        season              = str(x[1])   
        fixtureapi_id       = str(x[2])    
        # ------------------------------------------------------
        pre_ah_pattern          = str(x[3])   
        pre_gou_pattern         = str(x[4])    
        # ------------------------------------------------------
        end_ah_pattern          = str(x[5])   
        end_gou_pattern         = str(x[6])    
        # ------------------------------------------------------
        pre_ah_pattern_mirror       = str(x[7])   
        end_ah_pattern_mirror       = str(x[8])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " - " + season  
        word += " __ " + fixtureapi_id   

        word += " __ " + pre_ah_pattern   
        word += " __ " + pre_gou_pattern   

        word += " __ " + end_ah_pattern   
        word += " __ " + end_gou_pattern   

        word += " __ " + pre_ah_pattern_mirror   
        word += " __ " + end_ah_pattern_mirror   

        print(word, flush=True)    
        # ---------------------------------------------- Pre-Pre 
        fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, pre_ah_pattern, pre_gou_pattern, space)
        fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern_mirror, pre_gou_pattern, pre_ah_pattern_mirror, pre_gou_pattern, space)
        # ---------------------------------------------- Pre-End 
        fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
        fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern_mirror, pre_gou_pattern, end_ah_pattern_mirror, end_gou_pattern, space)
        # --------------------------------------------- Only-Pre 
        fP_DELETE_football_pattern_only(leagueapi_id, pre_ah_pattern, pre_gou_pattern, space)
        fP_DELETE_football_pattern_only(leagueapi_id, pre_ah_pattern_mirror, pre_gou_pattern, space)
        # --------------------------------------------- Only-End 
        fP_DELETE_football_pattern_only(leagueapi_id, end_ah_pattern, end_gou_pattern, space)
        fP_DELETE_football_pattern_only(leagueapi_id, end_ah_pattern_mirror, end_gou_pattern, space)
        # ------------------------------------------------------
        fpa_group_pattern_to_assess(leagueapi_id, 
                                pre_ah_pattern, pre_gou_pattern, 
                                end_ah_pattern, end_gou_pattern,  
                                pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                'Pre-Pre', 'football_pattern_from', 1,
                                space)
        # ------------------------------------------------------
        fpa_group_pattern_to_assess(leagueapi_id, 
                                pre_ah_pattern, pre_gou_pattern, 
                                end_ah_pattern, end_gou_pattern,  
                                pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                'Pre-End', 'football_pattern_from', 1,
                                space)
        fpa_group_pattern_to_assess(leagueapi_id, 
                                pre_ah_pattern, pre_gou_pattern, 
                                end_ah_pattern, end_gou_pattern,  
                                pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                'Only-Pre', 'football_pattern_only', 1,
                                space)
        # ------------------------------------------------------
        fpa_group_pattern_to_assess(leagueapi_id, 
                                pre_ah_pattern, pre_gou_pattern, 
                                end_ah_pattern, end_gou_pattern,  
                                pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                'Only-End', 'football_pattern_only', 1,
                                space)
    # ----------------------------------------------------------
    

def fP_DELETE_football_pattern_only(leagueapi_id, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fP_DELETE_football_pattern_only()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query_commit = "DELETE FROM `football_pattern_only`  "
    # ----------------------------------------------------------    
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query_commit += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query_commit += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "football_pattern_only's DELETED")
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  

     
def fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fP_DELETE_football_pattern_from()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query_commit = "DELETE FROM `football_pattern_from`  "
    # ----------------------------------------------------------    
    query_commit += " where leagueapi_id = "+str(leagueapi_id)+" "    

    query_commit += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "   
    query_commit += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   

    query_commit += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query_commit += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "football_pattern_from's DELETED")
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  
 
def fP_DELETE_football_pattern_from_country(country, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fP_DELETE_football_pattern_from_country()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query_commit = "DELETE FROM `football_pattern_from_country`  "
    # ----------------------------------------------------------    
    query_commit += " where country = '"+str(country)+"' "    

    query_commit += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "   
    query_commit += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   

    query_commit += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query_commit += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "football_pattern_from_country's DELETED")
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  
 
def fP_DELETE_football_pattern_from_world(world, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fP_DELETE_football_pattern_from_world()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    query_commit = "DELETE FROM `football_pattern_from_world`  "
    # ----------------------------------------------------------     

    query_commit += " where pre_ah_pattern = '"+str(pre_ah_pattern)+"' "   
    query_commit += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "   

    query_commit += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query_commit += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "   
    # ----------------------------------------------------------    
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "football_pattern_from_world's DELETED")
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  
   