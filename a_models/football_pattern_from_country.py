# Import
import mysql.connector  

def fpfc_QUERY_all_league_by_country(country, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fpfc_all_league_by_country()", flush=True)
    # ----------------------------------------------------------      
    query = "Select "  
    query += " leagueapi_id "  
    query += " from football_leagues " 
    query += " where country_name = '"+str(country)+"' "   
    query += " and deleted_at is null "        
    # ----------------------------------------------------------    
    return query
    # ---------------------------------------------------------- 
 
def fpfc_by_country(country, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fpfc_by_country()", flush=True)
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------  
    array_league = fpfc_QUERY_all_league_by_country(country, space)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = "Select "
    query += " pre_ah_pattern " 
    query += " , pre_gou_pattern "  

    query += " , end_ah_pattern " 
    query += " , end_gou_pattern "  

    query += " , count(*) "  

    query += " from football_odds " 
    query += " where leagueapi_id IN ("+str(array_league)+") " 
    query += " and fixture_status in ('Match Finished', 'Match Finished Ended') " 

    query += " and pre_ah_pattern is not null " 
    query += " and pre_gou_pattern is not null " 
    
    query += " and end_ah_pattern is not null " 
    query += " and end_gou_pattern is not null " 

    query += " and pre_ah_pattern != 'H' " 
    query += " and pre_gou_pattern != 'G' " 

    query += " and end_ah_pattern != 'H' " 
    query += " and end_gou_pattern != 'G' " 
    
    query += " and pre_response = 3 " 
    query += " and end_response = 3 "  

    query += " group by "
    query += " pre_ah_pattern " 
    query += " , pre_gou_pattern "  
    query += " , end_ah_pattern " 
    query += " , end_gou_pattern "  

    query += " HAVING COUNT(*) > 2 " 


    query += " order by count(*) desc " 
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
    # lg_update_total_pattern(leagueapi_id, "total_pattern_pre_ends", total_rows, space)
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter             += 1
        # ------------------------------------------------------
        pre_ah_pattern      = str(x[0]) 
        pre_gou_pattern     = str(x[1])  

        end_ah_pattern      = str(x[2]) 
        end_gou_pattern     = str(x[3])  

        countrows           = str(x[4])  
        # ------------------------------------------------------ 
        word = space + "[" + str(counter) + "/" + str(total_rows) + "] " + countrows + ". "
        word += pre_ah_pattern  
        word += " // " + pre_gou_pattern   
        word += " >> " + end_ah_pattern  
        word += " // " + end_gou_pattern   
        print(word, flush=True)   
        # ------------------------------------------------------  
        # fpfc_controll_pattern_ROUTE('from', country, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space) 
    # ----------------------------------------------------------  

    
def fpfc_controll_pattern_ROUTE(TABLE, country, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space):
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fpfc_controll_pattern_ROUTE()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " select "  
    query += " fixtureapi_id  "  
    query += " from `football_odds` "  
    query += " where `country` = "+str(country)+" "  

    if(TABLE == "from"):
        query += " and `pre_ah_pattern` like '"+str(pre_ah_pattern)+"' "  
        query += " and `pre_gou_pattern` like '"+str(pre_gou_pattern)+"' "  
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
        
    elif(TABLE == "only"): 
        query += " and `end_ah_pattern` like '"+str(end_ah_pattern)+"' "  
        query += " and `end_gou_pattern` like '"+str(end_gou_pattern)+"' " 
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    # space += "__"
    # ----------------------------------------------------------
    total_rows = len(result)    
    # ----------------------------------------------------------
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------
    aP_check_patternlist(TABLE, leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
    aP_final_assestment(query, TABLE, total_rows,
        leagueapi_id, pre_ah_pattern, pre_gou_pattern, end_ah_pattern, end_gou_pattern, space)
    # ----------------------------------------------------------