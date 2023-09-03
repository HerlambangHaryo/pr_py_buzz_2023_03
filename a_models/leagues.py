# Import
import mysql.connector  
from a_models.xpattern  import *   
from a_models.api_odds import *  
 
def lg_get_league_for_predates(leagueapi_id, season, page, date, date_raw, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_get_league_for_predates()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ----------------------------------------------------------   
    query = " Select "
    query += " bookmakersapi_id "  
    query += " , bookmakers_name "  
    query += " from football_leagues "  
    query += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # ----------------------------------------------------------
    for x in myresult:   
        bookmakersapi_id = x[0]
        bookmakersname   = x[1]
    # ----------------------------------------------------------
    print(space + "bookmakersapi_id : " + str(bookmakersapi_id) , flush=True)
    print(space + "bookmakersname : " + str(bookmakersname) , flush=True)
    # ----------------------------------------------------------- 
    if(bookmakersapi_id == 8 or bookmakersapi_id == 11): 
        # -------------------------------------------------------         
        DICT = {
            'date' : date,
            'page' : page,
            'league' : leagueapi_id,
            'season' : season,
            'bookmaker' : bookmakersapi_id,
            'date_raw' : date_raw,
        }
        # ------------------------------------------------------- 
        PREP_ = "preleague_"
        # -------------------------------------------------------
        ao_controll_match_update(DICT, PREP_, space)
        # -------------------------------------------------------
    # ----------------------------------------------------------

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
        query += " from football_leagues "  
        query += " where leagueapi_id = '"+str(DICTleagueapi_id)+"' " 
        query += " and leagueapi_id = '"+str(DICTleagueapi_id)+"' " 
    else:
        query = " Select *  "
        query += " from football_leagues "  
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
    query += " from football_leagues "   
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
    query += " from football_leagues "   
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
    query_commit = "update football_leagues set "   
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
    print(space + "> football_leagues reset " + def_col + " UPDATED at " + str(today), flush=True)
    # ---------------------------------------------------------- 

       
def lg_update_tanggal(leagueapi_id, def_col, today, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_update_tanggal()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query_commit = "update football_leagues set "   
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
    print(space + "> football_leagues : " + def_col + " UPDATED at " + str(today), flush=True)
    # ---------------------------------------------------------- 

def lg_update_total_pattern(leagueapi_id, def_col, total, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_update_total_pattern()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_mmbuzz_2022_06"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    mycursor = mydb.cursor()
    # ---------------------------------------------------------- 
    query_commit = "update football_leagues set "   
    # ----------------------------------------------------------  
    query_commit += " "+str(def_col)+" = '"+str(total)+"' "   
    # ---------------------------------------------------------- 
    query_commit += " where leagueapi_id = '"+str(leagueapi_id)+"' " 
    # ---------------------------------------------------------- 
    print(space + query_commit, flush=True) 
    # ---------------------------------------------------------- 
    mycursor.execute(query_commit)
    mydb.commit()  
    # ---------------------------------------------------------- 
    print(space + "> football_leagues : " + def_col + " UPDATED ", flush=True)
    # ---------------------------------------------------------- 
 
def lg_related_pattern_id(leagueapi_id, space):
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "lg_related_pattern_id()", flush=True) 
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # France - National 2 
    france = [ 67, 68, 69 ]  

    # Germany - Regionalliga
    regionalliga = [ 83, 84, 85, 86, 87 ]

    # Germany - Oberliga
    oberliga = [ 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755 ]

    # Portugal - Campeonato de Portugal Prio
    campeonato = [ 457, 458, 459, 460 ]  

    # Poland - III Liga
    iii_liga = [ 780, 781, 782, 783 ]  

    # Sweden - Ettan
    ettan = [ 563, 564 ]  
 
    # Sweden - Division 2
    division_2 = [ 592, 593, 594, 595, 596, 597 ]  
 
    # Finland - Kakkonen
    fin_kakkonen = [ 247, 248, 249 ] 

    # Spain  Segunda División RFEF
    spain_segunda_rfef = [ 875, 876, 877, 878, 879, ] 
 
    # Norway - 2. Division
    norway_div = [ 473, 474 ]   

    # Spain - Primera División RFEF
    spain_pri = [ 435, 436 ]  

    # Spain - Tercera División RFEF
    spain_ter = [ 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456 ]  

    # Czech-Republic -  3. liga
    Czech_3liga = [ 348, 349, 685, ]  

    # Australia -  NPL
    au_npl = [ 192, 194, 196, ]  

    # Australia - NPL 365
    au_npl_365 = [ 195, 481, 482 ]  

    # Austria - Regionalliga
    austria_regionalliga = [ 221, 222, 223, 688 ]  

    # Turkey - 3. Lig
    turkey_3Lig = [ 552, 553, 554 ]  

    # Italy - Campionato 
    italy_campionato = [705, 706]

    # Italy - Serie C 
    italy_serie_c = [942, 943, 976]

    # Egypt - Second League 
    egypt_second_league = [887, 888, 889]

    # # England - 1xbet 
    # england_1xbet = [887, 888, 889]

    # Registered 
    registered = [ 
        #england
        39, 40, 41, 42, 43, 44, 47, 
        #france
        61, 62, 64, 
        #brazil
        71, 72, 521, 
        #germany
        78, 79, 80, 82, 488,
        #netherland
        88, 89, 90, 91, 492,
        #portugal
        94, 95, 865,
        #Japan
        98, 99, 100, 101, 
        #Poland
        106, 107, 109, 
        #Sweden
        113, 114, 549, 
        #Belarus
        116,
        #Denmark
        119, 120, 122, 862, 
        #Argentina
        128, 129, 131, 132, 133, 134, 
        #Italy
        135, 139, 137, 
        #Spain
        140, 141, 143,
        #Belgium
        144, 145, 146, 147, 487, 518,
        #Costa-Rica
        162, 
        #Iceland
        164, 165, 166, 
        #China
        169, 170,
        #Bulgaria
        172, 173, 174, 
        #Australia
        188, 189, 
        #Greece
        197, 199, 494, 
        #Turkey
        203, 204, 205, 206, 
        #Switzerland
        207, 208, 209, 510, 
        #Croatia
        210, 210, 211, 212, 
        #Austria
        218, 219, 484,
        #Egypt
        233, 
        #Russia
        235, 236, 
        #Colombia
        239, 240, 
        #Ecuador
        242, 243, 917, 
        #Paraguay
        250, 252,
        #USA
        253, 254, 255, 256, 489, 257,
        #Mexico
        262, 263, 673, 
        #Chile
        265, 266, 711,
        #Uruguay
        268, 269, 
        #Hungary
        271, 272, 273,
        #Canada
        479,
        #Norway
        103, 104, 105,
        #Hungary
        417,
        #Azerbaidjan
        419,
        #Israel
        382, 383, 384, 496,
        #Ivory-Coast
        386,
        #Slovenia
        373, 374, 375,
        #Uzbekistan
        369, 
        #Singapore
        368, 
        #Lithuania
        361, 362,
        #Latvia
        365,
        #Czech-Republic
        345, 346, 347,
        #bolivia
        344,
        #Ukraine
        333, 334, 
        #Estonia
        328, 329, 657,
        #Kuwait
        330, 720,
        #Georgia
        326, 327,
        #Cyprus
        318,
        #venezuela
        299,
        #United-Arab-Emirates
        301, 303,
        #South-Korea
        292, 293, 294, 295,
        #Romania
        283, 284, 285,
        #Serbia
        286, 287, 732,
        #Peru
        281,
        #Malaysia
        278, 279, 499,
        #World
        11, 12, 13, 490, 
        #Scotland
        179, 180, 
        #Finland
        244, 245, 246, 
        #Slovakia
        332, 506, 680, 
        #South-Africa
        288, 
        #Bangladesh
        398, 
        #Saudi-Arabia
        307, 308, 
        #Jamaica
        322, 
        #Oman
        406, 726, 
        #Iran
        290, 291,
        #Vietnam
        340, 
        #Ethiopia
        363, 
    ]  

    if(int(leagueapi_id) in france):
        print(space + "--- Related", flush=True)
        return 67
    elif(int(leagueapi_id) in regionalliga):
        print(space + "--- Related", flush=True)
        return 83
    elif(int(leagueapi_id) in oberliga):
        print(space + "--- Related", flush=True)
        return 744
    elif(int(leagueapi_id) in campeonato):
        print(space + "--- Related", flush=True)
        return 457
    elif(int(leagueapi_id) in iii_liga):
        print(space + "--- Related", flush=True)
        return 780
    elif(int(leagueapi_id) in ettan):
        print(space + "--- Related", flush=True)
        return 563
    elif(int(leagueapi_id) in division_2):
        print(space + "--- Related", flush=True)
        return 592
    elif(int(leagueapi_id) in au_npl):
        print(space + "--- Related", flush=True)
        return 192
    elif(int(leagueapi_id) in fin_kakkonen):
        print(space + "--- Related", flush=True)
        return 247
    elif(int(leagueapi_id) in norway_div):
        print(space + "--- Related", flush=True)
        return 473
    elif(int(leagueapi_id) in spain_pri):
        print(space + "--- Related", flush=True)
        return 435
    elif(int(leagueapi_id) in spain_ter):
        print(space + "--- Related", flush=True)
        return 439
    elif(int(leagueapi_id) in Czech_3liga):
        print(space + "--- Related", flush=True)
        return 348
    elif(int(leagueapi_id) in spain_segunda_rfef):
        print(space + "--- Related", flush=True)
        return 875 
    elif(int(leagueapi_id) in au_npl_365):
        print(space + "--- Related", flush=True)
        return 195 
    elif(int(leagueapi_id) in austria_regionalliga):
        print(space + "--- Related", flush=True)
        return 221 
    elif(int(leagueapi_id) in turkey_3Lig):
        print(space + "--- Related", flush=True)
        return 552 
    elif(int(leagueapi_id) in italy_campionato):
        print(space + "--- Related", flush=True)
        return 702 
    elif(int(leagueapi_id) in egypt_second_league):
        print(space + "--- Related", flush=True)
        return 887 
    elif(int(leagueapi_id) in italy_serie_c):
        print(space + "--- Related", flush=True)
        return 942 

        

        
    elif(int(leagueapi_id) in registered):
        print(space + "--- Registered", flush=True)
        return leagueapi_id 
    else:
        return 0
        print(space + "______________________________________________________NotRegistered", flush=True)

    # ----------------------------------------------------------