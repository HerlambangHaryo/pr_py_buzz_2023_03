# Import
import mysql.connector  
from a_models.xpattern  import *   
 
def lg_get_leagueapi_id_ARRAY(DICT, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_get_leagueapi_id()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    DICTleagueapi_id = DICT['leagueapi_id']
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------    
    if 'today' in DICT:
        # for update pattern
        DICTtoday = DICT['today']
        query = " Select   "
        query += " tanggal_reset_pre_pattern " 
        query += " , DATEDIFF('"+str(DICTtoday)+"', tanggal_reset_pre_pattern) as diff_reset_pre "  
        query += " , tanggal_reset_end_pattern " 
        query += " , DATEDIFF('"+str(DICTtoday)+"', tanggal_reset_end_pattern) as diff_reset_end "  
        query += " from leagues "  
        query += " where leagueapi_id = '"+str(DICTleagueapi_id)+"' " 
        query += " and leagueapi_id = '"+str(DICTleagueapi_id)+"' " 
    else:
        query = " Select *  "
        query += " from leagues "  
        query += " where leagueapi_id = '"+str(DICTleagueapi_id)+"' " 
    # ----------------------------------------------------------  
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    # ----------------------------------------------------------  
    return result   
    # ----------------------------------------------------------

def lg_check_date_diff_col_for_reset_patternlist(leagueapi_id, date, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_check_date_diff_col_for_reset_patternlist()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select   "
    query += " tanggal_update_patternlists " 
    query += " , DATEDIFF('"+str(date)+"', 'tanggal_update_patternlists') as date_diff " 
    query += " from leagues "   
    query += " where leagueapi_id =  '"+str(leagueapi_id)+"' "  
    query += " and tanggal_reset_end_pattern is not null "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------ 
        tanggal         = x[0]  
        date_diff       = x[1]  
        # ------------------------------------------------------ 
        print(space + "date_diff : " + str(date_diff), flush=True) 

def lg_check_date_diff_col_for_reset_pattern(leagueapi_id, def_col, prep_col, date, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_check_date_diff_col_for_reset_pattern()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query = " Select   "
    query += def_col 
    query += " , DATEDIFF('"+str(date)+"', '"+def_col+"') as date_diff " 
    query += " from leagues "   
    query += " where leagueapi_id =  '"+str(leagueapi_id)+"' "  
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------     
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------ 
        tanggal         = x[0]  
        date_diff       = x[1]  
        # ------------------------------------------------------ 
        print(space + "date_diff : " + str(date_diff), flush=True) 
        # ------------------------------------------------------ 
        if(date_diff is None): 
            xp_get_league_fixture_to_reset(leagueapi_id, date, prep_col, space) 
    # ---------------------------------------------------------- 
    lg_update_reset_pattern(leagueapi_id, def_col, date, space)
    # ---------------------------------------------------------- 

    
def lg_update_reset_pattern(leagueapi_id, def_col, today, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_get_leagueapi_id()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query_commit = "update leagues set "   
    # ----------------------------------------------------------  
    query_commit += " "+str(def_col)+" = '"+str(today)+"' "   
    # ---------------------------------------------------------- 
    query_commit += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # ---------------------------------------------------------- 
    print(space + query_commit, flush=True) 
    # ---------------------------------------------------------- 
    mycursor.execute(query_commit)
    mydb.commit()  
    # ---------------------------------------------------------- 
    print(space + "> leagues reset " + def_col + " UPDATED at " + str(today), flush=True)
    # ---------------------------------------------------------- 