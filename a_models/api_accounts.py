# Import
import mysql.connector  

def aa_check_acccount(requested, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "aa_check_acccount()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select *  "
    query += " from apiaccounts "  
    query += " where active = 1 "  
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        APIaccount = x[2]
        APIkey     = x[4]
        counterAPI = x[6]  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    if(requested == "APIkey"):
        print(space + "API " + APIaccount + " counter is " + str(counterAPI), flush=True )  
        print(space + "APIkey: " + APIkey, flush=True)
    # ---------------------------------------------------------- 
    if(requested == "counterAPI"):
        return counterAPI
    if(requested == "APIkey"):
        return APIkey
    # ---------------------------------------------------------- 

def aa_update_counter(space):   
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "aa_update_counter()", flush=True) 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor() 
    # ----------------------------------------------------------
    query = " update apiaccounts "   
    query += " set counter = (counter - 1), "   
    query += " updated_at = now() "   
    query += " where active = 1 "  
    # ----------------------------------------------------------
    mycursor.execute(query)
    mydb.commit()    
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------
    # print(space + "API counter's updated")
    # ----------------------------------------------------------
