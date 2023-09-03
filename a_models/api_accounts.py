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
    query = " Select "
    query += " account  "  
    query += " , apikey   "  
    query += " , counter  "  
    query += " from apiaccounts "  
    query += " where active = 1 "  
    # ----------------------------------------------------------  
    # print(space + query, flush=True)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        APIaccount = x[0]
        APIkey     = x[1]
        counterAPI = x[2]  
    # ----------------------------------------------------------   
    if(counterAPI == 0):
        # ------------------------------------------------------  
        query_update_to_nil = "UPDATE `apiaccounts` SET  `active` = 4 where `active` = 1"
        mycursor.execute(query_update_to_nil)
        mydb.commit()   
        # ------------------------------------------------------  
        host="localhost"
        user="root" 
        database="pr_mmbuzz_2022_06"
        mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
        mycursor = mydb.cursor()
        # ------------------------------------------------------   
        query1 = " Select "
        query1 += " account  "  
        query1 += " , apikey   "  
        query1 += " , counter  "  
        query1 += " , id  "  
        query1 += " from apiaccounts "  
        query1 += " where counter != 0 "  
        query1 += " limit 1 "  
        # ------------------------------------------------------ 
        mycursor = mydb.cursor()
        mycursor.execute(query1)
        myresult1 = mycursor.fetchall()
        # ------------------------------------------------------ 
        for x1 in myresult1:   
            APIaccount  = x1[0]
            APIkey      = x1[1]
            counterAPI  = x1[2]  
            x1_id       = x1[3]  
        # ------------------------------------------------------ 
        query_update_to_one = "UPDATE `apiaccounts` SET  `active` = 1 where `id` = " + str(x1_id)
        mycursor.execute(query_update_to_one)
        mydb.commit()   
        # ------------------------------------------------------  
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
