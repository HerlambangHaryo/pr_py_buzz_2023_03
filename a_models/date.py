# Import
import mysql.connector 
import datetime 

def get_today_adds(date_diff, space): 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    print(space + "get_today_adds()") 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    param = "adds date_diff : " + str(date_diff)
    print(space + param, flush=True)
    # ----------------------------------------------------------
    today = datetime.datetime.now()
    DD = datetime.timedelta(days=date_diff)
    today_raw = today + DD
    # ---------------------------------------------------------- 
    param = "today_raw : " + str(today_raw)
    print(space + param, flush=True)
    # ---------------------------------------------------------- 
    return today_raw
    # ---------------------------------------------------------- 

def get_today_subs(date_diff, space): 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    print(space + "get_today_subs()") 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    param = "subs date_diff : " + str(date_diff)
    print(space + param, flush=True)
    # ----------------------------------------------------------
    today = datetime.datetime.now()
    DD = datetime.timedelta(days=date_diff)
    today_raw = today - DD
    # ---------------------------------------------------------- 
    param = "today_raw : " + str(today_raw)
    print(space + param, flush=True)
    # ---------------------------------------------------------- 
    return today_raw
    # ---------------------------------------------------------- 

def get_hour_subs(date_diff, space): 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    print(space + "get_hour_subs()") 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    param = "subs date_diff : " + str(date_diff)
    print(space + param, flush=True)
    # ----------------------------------------------------------
    today = datetime.datetime.now()
    DD = datetime.timedelta(hours=date_diff)
    today_raw = today - DD
    # ---------------------------------------------------------- 
    param = "today_raw : " + str(today_raw)
    print(space + param, flush=True)
    # ---------------------------------------------------------- 
    return today_raw
    # ---------------------------------------------------------- 

def get_hour_adds(date_diff, space): 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    print(space + "get_hour_adds()") 
    # ---------------------------------------------------------- 
    space += "__" 
    # ---------------------------------------------------------- 
    param = "adds date_diff : " + str(date_diff)
    print(space + param, flush=True)
    # ----------------------------------------------------------
    today = datetime.datetime.now()
    DD = datetime.timedelta(hours=date_diff)
    today_raw = today + DD
    # ---------------------------------------------------------- 
    param = "today_raw : " + str(today_raw)
    print(space + param, flush=True)
    # ---------------------------------------------------------- 
    return today_raw
    # ---------------------------------------------------------- 