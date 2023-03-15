# Import
import mysql.connector
from a_model.apiaccounts import *  
 
def lg_get_league_for_predates(leagueapi_id, season, page, space):
    # ----------------------------------------------------------  
    space += "  "
    print(space + "__lg_get_league_for_predates__")
    # ----------------------------------------------------------  
    space += "  "
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select *  "
    query += " from leagues "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        bookmakersapi_id = x[6]
        bookmakersname   = x[7]
    # ----------------------------------------------------------
    print(space + "bookmakersapi_id : " + str(bookmakersapi_id) )
    print(space + "bookmakersname : " + str(bookmakersname) )
    # ----------------------------------------------------------
    if(bookmakersapi_id == 8 or bookmakersapi_id == 11):
        aa_get_active_API_account_for_predates_from_leagues(leagueapi_id, season, bookmakersapi_id, page, space) 
    # ----------------------------------------------------------
        
def lg_get_league_for_end_dates(leagueapi_id, season, space):
    # ----------------------------------------------------------  
    space += "  "
    print(space + "__lg_get_league_for_end_dates__")
    # ----------------------------------------------------------  
    space += "  "
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select *  "
    query += " from leagues "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        bookmakersapi_id = x[6]
        bookmakersname   = x[7]
    # ----------------------------------------------------------
    print(space + "bookmakersapi_id : " + str(bookmakersapi_id) )
    print(space + "bookmakersname : " + str(bookmakersname) )
    # ----------------------------------------------------------
    if(bookmakersapi_id == 8 or bookmakersapi_id == 11):
        aa_get_active_API_account_for_end_dates_from_leagues(leagueapi_id, season, bookmakersapi_id, space) 
    # ----------------------------------------------------------
        
        
        