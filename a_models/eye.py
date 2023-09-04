# Import
import mysql.connector 
from a_models.api_odds_new import *    
from a_models.football_pattern import *    
 
def EYE_on_eye(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "EYE_on_eye()", flush=True)
    # ----------------------------------------------------------  
    EYE_delete_duplicate(space) 
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

    query += " from football_set_eyes " 
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
        EYE_check_odds(leagueapi_id, season, fixtureapi_id, space) 
    # ----------------------------------------------------------   


def EYE_check_odds(leagueapi_id, season, fixtureapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "EYE_check_odds()", flush=True)
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
    query += " from football_odds " 
    
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' "
    query += " and season = '"+str(season)+"' "
    query += " and fixtureapi_id = '"+str(fixtureapi_id)+"' "  
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
    # ---------------------------------------------------------- 
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ---------------------------------------------------------- 
    if(total_rows == 0):  
        # ------------------------------------------------------  
        date_raw        = get_today_adds(0, space) 
        bookmaker       = EYE_check_bookm(leagueapi_id, space)
        # ------------------------------------------------------     
        DICT = {
            'fixture' : fixtureapi_id,
            'bookmaker' : bookmaker,
            'date_raw' : date_raw, 
        } 
        # ------------------------------------------------------  
        PREP_ = "preone_"
        # ------------------------------------------------------
        aoN_controll_match_update(DICT, PREP_, space)
    else: 
        # ------------------------------------------------------
        fp_fixtureapi_id(fixtureapi_id, space)
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
     

def EYE_check_bookm(leagueapi_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "EYE_check_bookm()", flush=True)
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
    query += " bookmakersapi_id "  

    query += " from football_leagues " 
    
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
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
    # ---------------------------------------------------------- 
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    for x in result:     
        # ------------------------------------------------------
        bookmakersapi_id        = str(x[0])   
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    return bookmakersapi_id
    # ----------------------------------------------------------  

def EYE_delete_duplicate(space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "EYE_delete_duplicate()", flush=True)
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    query_commit = "DELETE t1 FROM football_set_eyes t1 "
    query_commit += "INNER JOIN football_set_eyes t2 "
    query_commit += "WHERE t1.id < t2.id " 
    # ----------------------------------------------------------   
    query_commit += "AND t1.leagueapi_id = t2.leagueapi_id "
    query_commit += "AND t1.season = t2.season "
    query_commit += "AND t1.fixtureapi_id = t2.fixtureapi_id "
    # ----------------------------------------------------------   
    print(space + query_commit, flush=True)
    # ----------------------------------------------------------   
    mycursor.execute(query_commit)
    mydb.commit()   
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()  
    # ----------------------------------------------------------    
    # ----------------------------------------------------------   