# Import
import mysql.connector 
import pandas as pd
from a_models.football_pattern_assessment import *   
  
def fo_group_pattern(leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fo_group_pattern()", flush=True)
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

    query += " , pre_ah_pattern  "
    query += " , pre_gou_pattern  "

    query += " , end_ah_pattern  "
    query += " , end_gou_pattern  "

    query += " , pre_ah_pattern_mirror  "
    query += " , end_ah_pattern_mirror  "

    query += " , count(*)  as total_fixtures "
    query += " from football_odds " 
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and fixture_status IN ('Match Finished', 'Match Finished Ended') "  

    query += " and pre_ah_pattern != 'H' "  
    query += " and end_ah_pattern != 'H' "  

    query += " and pre_gou_pattern != 'G' "  
    query += " and end_gou_pattern != 'G' "  

    query += " and football_pattern_from_updated_at is  null "  

    query += " group by   "  
    query += " pre_ah_pattern  "
    query += " , pre_gou_pattern  "
    query += " , end_ah_pattern  "
    query += " , end_gou_pattern  "   
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
        # ------------------------------------------------------
        pre_ah_pattern      = str(x[1])    
        pre_gou_pattern     = str(x[2])    
        end_ah_pattern      = str(x[3])    
        end_gou_pattern     = str(x[4])    
        # ------------------------------------------------------
        countrows           = str(x[5])    
        # ------------------------------------------------------
        pre_ah_pattern_mirror      = str(x[6])    
        end_ah_pattern_mirror      = str(x[7])    
        # ------------------------------------------------------
        word = space + "[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + leagueapi_id  
        word += " __ " + countrows  
        word += " __ " + pre_ah_pattern   
        word += " __ " + pre_gou_pattern  
        word += " __ " + end_ah_pattern  
        word += " __ " + end_gou_pattern   
        print(word, flush=True)      
        # ------------------------------------------------------
        fpa_group_pattern_to_assess(leagueapi_id, 
                                    pre_ah_pattern, pre_gou_pattern, 
                                    end_ah_pattern, end_gou_pattern, 
                                    pre_ah_pattern_mirror, end_ah_pattern_mirror,
                                    space) 
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  

def fo_delete_football_pattern(leagueapi_id, space):   
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "fo_delete_football_pattern()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------
    query = " delete FROM football_pattern_from "    
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "   
    # ----------------------------------------------------------
    mycursor.execute(query)
    mydb.commit()    
    # ----------------------------------------------------------
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    print(space + "football_pattern_from's DELETED")
    # ----------------------------------------------------------

def fo_controll_predates(day1, day2, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "fo_controll_predates()", flush=True)
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
    query += " DATE(date) as date_FX "  
    query += " , DATE(pre_odd_updated_at) as date_pre  "  
    query += " , count(*) as counter  "  
    query += " , fixture_status  "  
    query += " from football_odds " 
    query += " where DATE(date) >= '"+str(day1)+"' " 
    query += " and DATE(date) <= '"+str(day2)+"' " 
    query += " group by DATE(pre_odd_updated_at), fixture_status " 
    query += " order by DATE(date) desc "  
    # ----------------------------------------------------------   
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor.execute(query)   
    rows    = mycursor.fetchall() 
    df      = pd.DataFrame(rows, columns=[i[0] for i in mycursor.description]) 
    # ---------------------------------------------------------- 
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 120)
    # ---------------------------------------------------------- 
    total_rows = len(rows)
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # close the cursor and database connection
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    print("", flush=True)
    print(df, flush=True)
    print("", flush=True) 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

    