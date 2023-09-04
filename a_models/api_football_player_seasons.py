# Import
import mysql.connector 
 
def aFPS_update_or_insert(leagueapi_id, season, teamapi_id, playerapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "aFPS_update_or_insert()", flush=True) 
    # ----------------------------------------------------------   
    print(space + "leagueapi_id : " + str(leagueapi_id), flush=True) 
    print(space + "season : " + str(season), flush=True) 
    print(space + "teamapi_id : " + str(teamapi_id), flush=True) 
    print(space + "playerapi_id : " + str(playerapi_id), flush=True) 
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
    query += " from api_football_player_seasons "    
    query += " where leagueapi_id = "+str(leagueapi_id)+" "    
    query += " and season = "+str(season)+" "     
    query += " and teamapi_id = "+str(teamapi_id)+" "  
    query += " and playerapi_id = "+str(playerapi_id)+" "      
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
