# Import
import mysql.connector
from a_models.patternlists_assestment_new import *  

def plN_check_patternlist_only_ends(
        countrows,
        leagueapi_id,   

        end_ah_pattern,  
        end_gou_pattern, 
        space):
    # ----------------------------------------------------------   
    space += "__"    
    # ----------------------------------------------------------  
    print(space + "plN_check_patternlist_only_ends()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select * " 
    query += " from football_pattern_only "     
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "    

    query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "  
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
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # -------------------------------------------------- 
        space += "__"
        # -------------------------------------------------- 
        query = "INSERT INTO `football_pattern_only`( " 
        # -------------------------------------------------- 
        query += " `total_fixtures`, " 
        query += " `leagueapi_id`, " 
        query += " `end_ah_pattern`, " 
        query += " `end_gou_pattern`"
        # -------------------------------------------------- 
        query += " ) VALUES ( " 
        # -------------------------------------------------- 
        query += " '"+str(countrows)+"', "  
        query += " '"+str(leagueapi_id)+"', " 
        # -------------------------------------------------- 
        query += " '"+str(end_ah_pattern)+"', " 
        query += " '"+str(end_gou_pattern)+"' "
        query += " ) "
        # -------------------------------------------------- 
        mycursor.execute(query)
        mydb.commit() 
        print(space + "__insert commited", flush=True)
    elif(total_rows != 0): 
        print(space + "__Already Data", flush=True)
    # ----------------------------------------------------------  
    paN_get_fixtures_only_ends(
            leagueapi_id,  
            "only_ends", 
            "only_ends", 
            end_ah_pattern,  
            end_gou_pattern, 
            "football_pattern_only", 
            space) 
    # ----------------------------------------------------------        
    
def plN_check_patternlist_pre_ends(
        countrows,
        leagueapi_id,   

        pre_ah_pattern,  
        pre_gou_pattern, 

        end_ah_pattern,  
        end_gou_pattern, 
        space):
    # ----------------------------------------------------------   
    space += "__"    
    # ----------------------------------------------------------  
    print(space + "plN_check_patternlist_pre_ends()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select * " 
    query += " from football_pattern_from "     
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "    

    query += " and pre_ah_pattern = '"+str(pre_ah_pattern)+"' "   
    query += " and pre_gou_pattern = '"+str(pre_gou_pattern)+"' "  

    query += " and end_ah_pattern = '"+str(end_ah_pattern)+"' "   
    query += " and end_gou_pattern = '"+str(end_gou_pattern)+"' "  
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
    # ----------------------------------------------------------  
    if(total_rows == 0): 
        # -------------------------------------------------- 
        space += "__"
        # -------------------------------------------------- 
        query = "INSERT INTO `football_pattern_from`( " 
        # -------------------------------------------------- 
        query += " `total_fixtures`, " 
        query += " `leagueapi_id`, " 

        query += " `pre_ah_pattern`, " 
        query += " `pre_gou_pattern`, "

        query += " `end_ah_pattern`, " 
        query += " `end_gou_pattern` "
        # -------------------------------------------------- 
        query += " ) VALUES ( " 
        # -------------------------------------------------- 
        query += " '"+str(countrows)+"', "  
        query += " '"+str(leagueapi_id)+"', " 
        # -------------------------------------------------- 
        query += " '"+str(pre_ah_pattern)+"', " 
        query += " '"+str(pre_gou_pattern)+"', "
        # -------------------------------------------------- 
        query += " '"+str(end_ah_pattern)+"', " 
        query += " '"+str(end_gou_pattern)+"' "
        query += " ) "
        # -------------------------------------------------- 
        # print(space + query, flush=True)
        mycursor.execute(query)
        mydb.commit() 
        print(space + "__insert commited", flush=True)
    elif(total_rows != 0): 
        print(space + "__Already Data", flush=True)
    # ----------------------------------------------------------  
    paN_get_fixtures_pre_ends(
            leagueapi_id,  

            pre_ah_pattern,  
            pre_gou_pattern, 

            end_ah_pattern,  
            end_gou_pattern, 

            "football_pattern_from", 
            space) 
    # ----------------------------------------------------------   
 