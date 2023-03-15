# Import
import mysql.connector
import datetime 

def its_start(): 
    # -------------------------------------------------- 
    datenow = datetime.datetime.now()
    datenow_onlydate = datenow.strftime("%Y-%m-%d %H:%M:%S")  
    # --------------------------------------------------   
    word = "# -------------------------------------------------- Start at "
    start_notification = word + str(datenow_onlydate)
    # --------------------------------------------------   
    print(start_notification)  
    # --------------------------------------------------   
     
def its_end(): 
    # -------------------------------------------------- 
    datenow = datetime.datetime.now()
    datenow_onlydate = datenow.strftime("%Y-%m-%d %H:%M:%S")  
    # --------------------------------------------------   
    word = "# -------------------------------------------------- End at "
    start_notification = word + str(datenow_onlydate)
    # --------------------------------------------------   
    print(start_notification)  
    # --------------------------------------------------   
             
def its_api_empty(): 
    # --------------------------------------------------   
    word = "# ------------- API COUNTER EMPTY ------------- #"
    print(word)   
    # --------------------------------------------------   
    
    
    