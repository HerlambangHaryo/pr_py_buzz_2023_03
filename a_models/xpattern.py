# Import
import mysql.connector 
from a_models.xpattern_new import *  
from a_models.xpattern_4_new import *  

def xp_get_fixture_to_xpattern(day1, day2, ROUTES, space):
    # ----------------------------------------------------------   
    # xp_get_fixture_to_xpattern
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "xp_get_fixture_to_xpattern()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " DATE(date), "
    query += " leagueapi_id, "
    query += " (select bookmakersapi_id from football_leagues where football_leagues.leagueapi_id = football_odds.leagueapi_id), "
    query += " season,  "
    query += " fixtureapi_id,  "
    query += " pre_ah_pattern,  "
    query += " pre_gou_pattern  " 
    query += " from football_odds "     
    if(ROUTES == 'odds'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "  
        query += " and fixture_status like 'Match Finished' "

        query += " and deleted_at is null "  
        query += " order by date desc"  
    elif(ROUTES == 'xpattern'):
        # query += " where date <= '"+day2+"' "
        # query += " and date >= '"+day1+"' "  
        query += " where fixture_status like 'Match Finished Ended' "
        
        query += " and deleted_at is null "  
        query += " and end_response = 1 "  
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  
    elif(ROUTES == 'pre_xpattern'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "   
        
        query += " and deleted_at is null "  
        query += " and pre_response != 3 "  
        query += " order by date asc"  
    elif(ROUTES == 'one_xpattern'):
        query += " where one = 1 " 
        query += " and deleted_at is null "  
        query += " order by date desc"  
    elif(ROUTES == 'all_pre_xpattern'):
        query += " where  deleted_at is null "  
        query += " and pre_response != 3 "  
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  
    elif(ROUTES == 'all_end_xpattern'):
        query += " where date <= '"+day2+"' "
        query += " and date >= '"+day1+"' "   
        query += " and  deleted_at is null "  
        query += " and end_response != 3 "  
        query += " and fixture_status like 'Match Finished' "
        query += " order by date, leagueapi_id, fixtureapi_id  desc"  



        
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
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
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
        if(ROUTES == 'pre_xpattern'):  
            xp4N_set_pattern(fixtureapi_id, 'pre_', 4, space)
            xpN_set_pattern(fixtureapi_id, 'pre_', 4, space)


        # if(ROUTES == 'xpattern'): 
        #     # xp_set_pattern(fixtureapi_id, 'end_', 'no', space)
        #     xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
        # elif(ROUTES == 'pre_xpattern'): 
        #     # xp_set_pattern(fixtureapi_id, 'pre_', 'no', space)
        #     xpN_set_pattern(fixtureapi_id, 'pre_', 4, space)
        # elif(ROUTES == 'all_pre_xpattern'): 
        #     # xp_set_pattern(fixtureapi_id, 'pre_', 'no', space)
        #     xpN_set_pattern(fixtureapi_id, 'pre_', 4, space)
        # elif(ROUTES == 'all_end_xpattern'): 
        #     # xp_set_pattern(fixtureapi_id, 'end_', 'no', space)
        #     xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
        # elif(ROUTES == 'one_xpattern'):
        #     # xp_set_pattern(fixtureapi_id, 'pre_', 'yes', space)
        #     # xpN_set_pattern(fixtureapi_id, 'end_', 'no', space) 
        #     xpN_set_pattern(fixtureapi_id, 'end_', 4, space)
    # ----------------------------------------------------------  
 