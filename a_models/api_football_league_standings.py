# Import
import mysql.connector 
 
def aFLS_update_or_insert(leagueapi_id, season, teamapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "aFLS_update_or_insert()", flush=True) 
    # ----------------------------------------------------------   
    print(space + "leagueapi_id : " + str(leagueapi_id), flush=True) 
    print(space + "season : " + str(season), flush=True) 
    print(space + "teamapi_id : " + str(teamapi_id), flush=True) 
    # ----------------------------------------------------------  
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select  * " 
    query += " from api_football_league_standings "    
    query += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query += " and season = "+str(season)+" "     
    query += " and teamapi_id = "+str(teamapi_id)+" "      
    # ----------------------------------------------------------    
    print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------    
    total_rows = len(result)
    # ----------------------------------------------------------
    print(space + "total_rows: " + str(total_rows), flush=True)
    # ----------------------------------------------------------
    return total_rows     
    # ----------------------------------------------------------  
