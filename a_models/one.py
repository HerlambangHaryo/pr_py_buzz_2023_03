# Import
import mysql.connector 
from a_models.football_pattern import *  
 
def one_on_one_for_advices(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_one_for_advices()", flush=True) 
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
    query += " from football_set_ones " 
    query += " where status = 1 "   
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
        fixtureapi_id       = str(x[2])     
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " __ " + season  
        word += " __ " + fixtureapi_id    
        print(word, flush=True)      
        # ------------------------------------------------------
        one_on_football_odds(leagueapi_id, season, fixtureapi_id, space)
    # ----------------------------------------------------------
    
def one_on_football_odds(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_football_odds()", flush=True) 
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

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    query += " and season = '"+str(season)+"' "   
    query += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "   
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
        fixtureapi_id       = str(x[2])     
        # ------------------------------------------------------
        pre_ah_pattern          = str(x[3])   
        pre_ah_pattern_mirror   = str(x[4])    
        pre_gou_pattern         = str(x[5])     
        # ------------------------------------------------------
        end_ah_pattern          = str(x[6])   
        end_ah_pattern_mirror   = str(x[7])    
        end_gou_pattern         = str(x[8])     
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " __ " + season  
        word += " __ " + fixtureapi_id    
        print(word, flush=True)      
        # ------------------------------------------------------
        league_count = one_on_count_league_football_odds(leagueapi_id, 
                                            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern,
                                            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern,
                                            space) 
        
        if(league_count > 2): 
            # -------------------------------------------------- 
            one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, 1, space)
            # ------------------------------------------ Pre-End  
            fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
            # --------------------------------------------------
            fpa_group_pattern_to_assess(leagueapi_id, 
                                    pre_ah_pattern, pre_gou_pattern, 
                                    end_ah_pattern, end_gou_pattern,  
                                    pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                    'Pre-End', 'football_pattern_from', 1,
                                    space)
            # -------------------------------------------------- 
        else:
            # -------------------------------------------------- 
            one_update_zero(leagueapi_id, season, fixtureapi_id, space)
            # -------------------------------------------------- 

            # if(league_count > 2): 
            #     # --------------------------------------------------
            #     one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, 1, space)
            #     # ------------------------------------------ Pre-End  
            #     # fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
            #     # # --------------------------------------------------
            #     # fpa_group_pattern_to_assess(leagueapi_id, 
            #     #                         pre_ah_pattern, pre_gou_pattern, 
            #     #                         end_ah_pattern, end_gou_pattern,  
            #     #                         pre_ah_pattern_mirror, end_ah_pattern_mirror,
            #     #                         'Pre-End', 'football_pattern_from', 1,
            #     #                         space)
            #     # --------------------------------------------------
            #     # --------------------------------------------------
            # else:
            #     one_update_zero(leagueapi_id, season, fixtureapi_id, space)
            
        #     if(country_count <= 1): 
        #         # world_count = one_on_count_world_football_odds(leagueapi_id, 
        #         #                                 pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern,
        #         #                                 end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern,
        #         #                                 space) 

        #         # if(world_count == 0): 
        #         one_update_zero(leagueapi_id, season, fixtureapi_id, space)
        #         # else: 
        #         #     # ----------------------------------------------
        #         #     one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, 3, space)
        #         #     # ----------------------------------------------
        #         #     # ---------------------------------- Pre-End 
        #         #     fP_DELETE_football_pattern_from_world('None', pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
        #         #     # ------------------------------------------
        #         #     fpa_group_pattern_to_assess(leagueapi_id, 
        #         #                             pre_ah_pattern, pre_gou_pattern, 
        #         #                             end_ah_pattern, end_gou_pattern,  
        #         #                             pre_ah_pattern_mirror, end_ah_pattern_mirror,
        #         #                             'Pre-End', 'football_pattern_from_world', 3,
        #         #                             space)
        #             # ------------------------------------------
        #         # ----------------------------------------------
        #     elif(country_count >= 2): 
        #         # ----------------------------------------------
        #         one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, 2, space)
        #         # ----------------------------------------------
        #         # -------------------------------------- Pre-End 
        #         if(country_count > 2):
        #             fP_DELETE_football_pattern_from_country(country_name, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
        #             # ----------------------------------------------
        #             fpa_group_pattern_to_assess(country_name, 
        #                                     pre_ah_pattern, pre_gou_pattern, 
        #                                     end_ah_pattern, end_gou_pattern,  
        #                                     pre_ah_pattern_mirror, end_ah_pattern_mirror,
        #                                     'Pre-End', 'football_pattern_from_country', 2,
        #                                     space)
        #         # ----------------------------------------------
        #     # --------------------------------------------------
        # elif(league_count >= 2): 
        #     # --------------------------------------------------
        #     one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, 1, space)
        #     # ------------------------------------------ Pre-End 
        #     if(league_count > 2):
        #         fP_DELETE_football_pattern_from(leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
        #         # --------------------------------------------------
        #         fpa_group_pattern_to_assess(leagueapi_id, 
        #                                 pre_ah_pattern, pre_gou_pattern, 
        #                                 end_ah_pattern, end_gou_pattern,  
        #                                 pre_ah_pattern_mirror, end_ah_pattern_mirror,
        #                                 'Pre-End', 'football_pattern_from', 1,
        #                                 space)
        #         # --------------------------------------------------
    # ----------------------------------------------------------      
  
def one_update_type_of_pattern(leagueapi_id, season, fixtureapi_id, type_of_pattern, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_update_type_of_pattern()", flush=True)
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
    query_commit += " `type_of_pattern` = '"+str(type_of_pattern)+"' "
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

def one_update_zero(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_update_zero()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query_commit = "UPDATE `football_set_ones` SET " 
    # ------------------------------------------------------
    query_commit += " `status` = 0 "
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

def one_on_football_league(leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_football_league()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select "
    query += " country_name  "    
    query += " from football_leagues " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "    
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    # ----------------------------------------------------------   
    result_check = mycursor.fetchone()
    total_rows = result_check[0]
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------       
    return total_rows
    # ----------------------------------------------------------      

def one_on_count_league_football_odds(leagueapi_id, 
                                            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern,
                                            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern,
                                            space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_count_league_football_odds()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "( "
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "     

    query += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "    
    # ----------------------------------------------------------   
    query += " ) union ( "
    # ----------------------------------------------------------  
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "     

    query += " and pre_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern_mirror)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " )  "
    # ----------------------------------------------------------   
    # print(space + query)
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
    print(space + "Total league Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------      
    return total_rows
    # ----------------------------------------------------------      
 
def one_on_count_country_football_odds(country_name, 
                                            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern,
                                            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern,
                                            space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_count_country_football_odds()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query_league = "SELECT leagueapi_id " 
    query_league += "FROM `football_leagues` " 
    query_league += "where country_name = '"+str(country_name)+"' "
    # ----------------------------------------------------------  
    query = "( "
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds " 
    query += " where leagueapi_id IN ("+query_league+") "    

    query += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "    
    # ----------------------------------------------------------   
    query += " ) union ( "
    # ----------------------------------------------------------  
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds " 
    query += " where leagueapi_id IN ("+query_league+") "     

    query += " and pre_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern_mirror)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " )  "
    # ----------------------------------------------------------   
    # print(space + query)
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
    print(space + "Total country Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------   
    return total_rows
    # ----------------------------------------------------------         
 
def one_on_count_world_football_odds(leagueapi_id, 
                                            pre_ah_pattern, pre_ah_pattern_mirror, pre_gou_pattern,
                                            end_ah_pattern, end_ah_pattern_mirror, end_gou_pattern,
                                            space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "one_on_count_world_football_odds()", flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "( "
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds "  

    query += " where pre_ah_pattern = '"+str(pre_ah_pattern)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "    
    # ----------------------------------------------------------   
    query += " ) union ( "
    # ----------------------------------------------------------  
    query += " Select "
    query += " leagueapi_id  "    
    query += " , season  "      
    query += " , fixtureapi_id  "   

    query += " , pre_ah_pattern  "   
    query += " , pre_ah_pattern_mirror  "   
    query += " , pre_gou_pattern  "   

    query += " , end_ah_pattern  "   
    query += " , end_ah_pattern_mirror  "   
    query += " , end_gou_pattern  "   

    query += " from football_odds "  

    query += " where pre_ah_pattern = '"+str(pre_ah_pattern_mirror)+"' "    
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "    
    
    query += " and end_ah_pattern = '"+str(end_ah_pattern_mirror)+"' "    
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "    

    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') "   
    query += " )  "
    # ----------------------------------------------------------   
    # print(space + query)
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
    print(space + "Total world Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------     
    return total_rows
    # ----------------------------------------------------------       