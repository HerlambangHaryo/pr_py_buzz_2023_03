# Import
import mysql.connector 
from a_models.api_odds_new import *   
 
def pd_gak_sempet_predates(day1, day2, today, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pd_gak_sempet_predates()", flush=True)
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
    query += " , season" 
    query += " from football_fixtures " 
    query += " where date >= '"+str(day1)+"' "  
    query += " and date <= '"+str(day2)+"' "  
    query += " and deleted_at is null "       
    query += " and fixture_status IN ('Not Started', 'Not Started Goto', 'Not Started One') "       
 
    query += " group by leagueapi_id, season "
    query += " order by leagueapi_id asc  "   
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
    print(space + "Total Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------  
        counter         += 1
        leagueapi_id    = str(x[0])  
        season          = str(x[1])    
        # ------------------------------------------------------  
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
        word += " #" + leagueapi_id 
        word += " - " + season  
        print(word, flush=True)   
        # ------------------------------------------------------  
        pd_detail_fixtures(day1, day2, leagueapi_id, season, today, space)
    # ----------------------------------------------------------  

def pd_detail_fixtures(day1, day2, leagueapi_id, season, today, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pd_detail_fixtures()", flush=True)
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
    query += " , season" 
    query += " , fixtureapi_id" 
    query += " from football_fixtures " 
    query += " where date >= '"+str(day1)+"' "  
    query += " and date <= '"+str(day2)+"' "  

    query += " and leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "  
    query += " and fixture_status IN ('Not Started', 'Not Started Goto', 'Not Started One') "  

    query += " and deleted_at is null "         
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
    total_row_fixtures = total_rows
    # ----------------------------------------------------------    
    print(space + "Total Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    word_fixtures = ""
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------  
        counter         += 1
        leagueapi_id    = str(x[0])  
        season          = str(x[1])    
        # ------------------------------------------------------  
        fixtureapi_id   = str(x[2])    
        # ------------------------------------------------------  
        word = space + "[" + str(counter) + "/" +str(len(result)) + "] " 
        word += " #" + fixtureapi_id  
        print(word, flush=True)   
        # ------------------------------------------------------
        word_fixtures += fixtureapi_id
        # ------------------------------------------------------ 
        if(counter != total_rows):
            word_fixtures += ", "
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    if(total_rows != 0 ):
        # ------------------------------------------------------
        pd_check_odds(day1, day2, leagueapi_id, season, word_fixtures, total_row_fixtures, today, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    print(space, flush=True)
    # ----------------------------------------------------------  
 
def pd_check_odds(day1, day2, leagueapi_id, season, word_fixtures, total_row_fixtures, today, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pd_check_odds()", flush=True)
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
    query += " , season" 
    query += " , fixtureapi_id" 
    query += " from football_odds " 
    query += " where date >= '"+str(day1)+"' "  
    query += " and date <= '"+str(day2)+"' "  

    query += " and leagueapi_id = '"+str(leagueapi_id)+"' "  
    query += " and season = '"+str(season)+"' "  

    query += " and fixtureapi_id IN ("+ word_fixtures +")   "  

    query += " and deleted_at is null "         
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
    print(space + "Total Row(s) : " + str(total_rows), flush=True)  
    # ----------------------------------------------------------  
    counter = 0
    # ----------------------------------------------------------  
    space += "__" 
    # ----------------------------------------------------------  
    if(total_rows == 0):
        # ------------------------------------------------------ 
        bookmakersapi_id = pd_league(leagueapi_id, space)
        # ------------------------------------------------------ 
        if(total_row_fixtures == 1):
            # --------------------------------------------------  
            print(space + "SINGLE FIXTURE: bm: " + str(bookmakersapi_id), flush=True)  
            print(space + "today: " + str(today), flush=True)  
            # -------------------------------------------------- 
            DICT = {
                'date' : "NONE",
                'date_raw' : today,
                'fixture' : word_fixtures, 
                'bookmaker' : bookmakersapi_id, 
            } 
            # --------------------------------------------------  
            PREP_ = "preone_"
            # -------------------------------------------------- 
            aoN_controll_match_update(DICT, PREP_, space)
            # --------------------------------------------------  
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        elif(total_row_fixtures > 1):
            # -------------------------------------------------- 
            print(space + "LEAGUE GROUP: bm: " + str(bookmakersapi_id), flush=True)  
            print(space + "today: " + str(today), flush=True)  
            # --------------------------------------------------  
            DICT = {
                'date' : "NONE",
                'date_raw' : today,
                'league' : leagueapi_id,
                'season' : season,
                'bookmaker' : bookmakersapi_id,
                'page' : 1,
                'counter_loop' : 0,
                'date_diff' : 0, 
            } 
            # --------------------------------------------------  
            PREP_ = "preleague_"
            # -------------------------------------------------- 
            aoN_controll_match_update(DICT, PREP_, space)
            # --------------------------------------------------  
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
 
def pd_league(leagueapi_id, space): 
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pd_league()", flush=True)
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

    query += " and deleted_at is null "         
    # ----------------------------------------------------------   
    print(space + query, flush=True)  
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
 