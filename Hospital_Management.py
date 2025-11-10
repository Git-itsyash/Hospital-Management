
print("""                             
                                                                          ██████╗██╗      █████╗ ███████╗███████╗     ██╗██████╗ 
                                                                          ██╔════╝██║     ██╔══██╗██╔════╝██╔════╝    ███║╚════██╗
                                                                          ██║     ██║     ███████║███████╗███████╗    ╚██║ █████╔╝
                                                                          ██║     ██║     ██╔══██║╚════██║╚════██║     ██║██╔═══╝ 
                                                                          ╚██████╗███████╗██║  ██║███████║███████║     ██║███████╗
                                                                           ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═╝╚══════╝

                                                        """)


a=("""      
              ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗     ███████╗ ██████╗██╗███████╗███╗   ██╗ ██████╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
             ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝████╗  ██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
             ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝    ███████╗██║     ██║█████╗  ██╔██╗ ██║██║     █████╗      ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
             ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗    ╚════██║██║     ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝      ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
             ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║    ███████║╚██████╗██║███████╗██║ ╚████║╚██████╗███████╗    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
              ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                                                                                                                                                             
                                                                                                                                                                    
                                                                                                                                                                                             """)

print(a)
def topic():
    print("""
               -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              |      _    _  ____   _____ _____ _____ _______       _        __  __          _   _          _____ ______ __  __ ______ _   _ _______    _______     _______ _______ ______ __  __       |
              |     | |  | |/ __ \ / ____|  __ \_   _|__   __|/\   | |      |  \/  |   /\   | \ | |   /\   / ____|  ____|  \/  |  ____| \ | |__   __|  / ____\ \   / / ____|__   __|  ____|  \/  |      |
              |     | |__| | |  | | (___ | |__) || |    | |  /  \  | |      | \  / |  /  \  |  \| |  /  \ | |  __| |__  | \  / | |__  |  \| |  | |    | (___  \ \_/ / (___    | |  | |__  | \  / |      |
              |     |  __  | |  | |\___ \|  ___/ | |    | | / /\ \ | |      | |\/| | / /\ \ | . ` | / /\ \| | |_ |  __| | |\/| |  __| | . ` |  | |     \___ \  \   / \___ \   | |  |  __| | |\/| |      |
              |     | |  | | |__| |____) | |    _| |_   | |/ ____ \| |____  | |  | |/ ____ \| |\  |/ ____ \ |__| | |____| |  | | |____| |\  |  | |     ____) |  | |  ____) |  | |  | |____| |  | |      |
              |     |_|  |_|\____/|_____/|_|   |_____|  |_/_/    \_\______| |_|  |_/_/    \_\_| \_/_/    \_\_____|______|_|  |_|______|_| \_|  |_|    |_____/   |_| |_____/   |_|  |______|_|  |_|      |
              |                                                                                                                                                                                         |
              |                                                                                                                                                                                         |
               -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
      
 """)  
topic()                                                                                                                                                                        
            
credits = """
                                                                            *************************************************
                                                                           *          PYTHON AND MYSQL PROJECT                *
                                                                           *                  BY->                            *
                                                                           *                       YASH GUPTA                 *
                                                                           *                       ADITYA MALL                *
                                                                           *                       PARV SINGH                 *
                                                                           *                       RAVI                       *
                                                                           *                       AISHWARYA SINGH            *
                                                                           **************************************************
 """
print(credits)

import mysql.connector as a
import os
from tabulate import tabulate
from pwinput import pwinput
con = a.connect(host="localhost",user="root",passwd="itsyash",database="hospital_management")
c = con.cursor()

def topic():
    print("""
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  |      _    _  ____   _____ _____ _____ _______       _        __  __          _   _          _____ ______ __  __ ______ _   _ _______    _______     _______ _______ ______ __  __       |
  |     | |  | |/ __ \ / ____|  __ \_   _|__   __|/\   | |      |  \/  |   /\   | \ | |   /\   / ____|  ____|  \/  |  ____| \ | |__   __|  / ____\ \   / / ____|__   __|  ____|  \/  |      |
  |     | |__| | |  | | (___ | |__) || |    | |  /  \  | |      | \  / |  /  \  |  \| |  /  \ | |  __| |__  | \  / | |__  |  \| |  | |    | (___  \ \_/ / (___    | |  | |__  | \  / |      |
  |     |  __  | |  | |\___ \|  ___/ | |    | | / /\ \ | |      | |\/| | / /\ \ | . ` | / /\ \| | |_ |  __| | |\/| |  __| | . ` |  | |     \___ \  \   / \___ \   | |  |  __| | |\/| |      |
  |     | |  | | |__| |____) | |    _| |_   | |/ ____ \| |____  | |  | |/ ____ \| |\  |/ ____ \ |__| | |____| |  | | |____| |\  |  | |     ____) |  | |  ____) |  | |  | |____| |  | |      |
  |     |_|  |_|\____/|_____/|_|   |_____|  |_/_/    \_\______| |_|  |_/_/    \_\_| \_/_/    \_\_____|______|_|  |_|______|_| \_|  |_|    |_____/   |_| |_____/   |_|  |______|_|  |_|      |
  |                                                                                                                                                                                         |
  |                                                                                                                                                                                         |
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
         """)
opd_table = """
CREATE TABLE IF NOT EXISTS  opd (patient_name VARCHAR(255),patient_id INT(10),doctor_name VARCHAR(255),disease VARCHAR(255),treatment VARCHAR(255),father_name VARCHAR(255),address VARCHAR(255),nationality VARCHAR(255),mobile_no VARCHAR(20),ayushman_card_number VARCHAR(20),gender VARCHAR(10),aadhar_number VARCHAR(20)
)
"""
general_room = """
CREATE TABLE IF NOT EXISTS  general_room (patient_name VARCHAR(255),patient_id INT(10),doctor_name VARCHAR(255),disease VARCHAR(255),treatment VARCHAR(255),father_name VARCHAR(255),address VARCHAR(255),nationality VARCHAR(255),mobile_no VARCHAR(20),ayushman_card_number VARCHAR(20),gender VARCHAR(10),aadhar_number VARCHAR(20)
)
"""
ac_room= """
CREATE TABLE IF NOT EXISTS  ac_room (patient_name VARCHAR(255),patient_id INT(10),doctor_name VARCHAR(255),disease VARCHAR(255),treatment VARCHAR(255),father_name VARCHAR(255),address VARCHAR(255),nationality VARCHAR(255),mobile_no VARCHAR(20),ayushman_card_number VARCHAR(20),gender VARCHAR(10),aadhar_number VARCHAR(20)
)
"""
deluxe_room = """
CREATE TABLE IF NOT EXISTS  deluxe_room (patient_name VARCHAR(255),patient_id INT(10),doctor_name VARCHAR(255),disease VARCHAR(255),treatment VARCHAR(255),father_name VARCHAR(255),address VARCHAR(255),nationality VARCHAR(255),mobile_no VARCHAR(20),ayushman_card_number VARCHAR(20),gender VARCHAR(10),aadhar_number VARCHAR(20)
)
"""
signup = """CREATE TABLE IF NOT EXISTS signup_user_data (user_name VARCHAR(50),user_id INT(10))"""
signin = """CREATE TABLE IF NOT EXISTS signin_user_data (user_name VARCHAR(50),user_id INT(10))"""
c.execute(opd_table)
c.execute(general_room)
c.execute(ac_room)
c.execute(deluxe_room)
c.execute(signup)
c.execute(signin)
c.close()
def choose_task():
     print("""
                            
                      _____  _    _   ____    ____    _____  ______   _______          _____  _  __
                     / ____|| |  | | / __ \  / __ \  / ____||  ____| |__   __| /\     / ____|| |/ /
                    | |     | |__| || |  | || |  | || (___  | |__       | |   /  \   | (___  | ' / 
                    | |     |  __  || |  | || |  | | \___ \ |  __|      | |  / /\ \   \___ \ |  <  
                    | |____ | |  | || |__| || |__| | ____) || |____     | | / ____ \  ____) || . \ 
                     \_____||_|  |_| \____/  \____/ |_____/ |______|    |_|/_/    \_\|_____/ |_|\_\
                                                                                                    
                                                                                
""")
    




def signup():
    print("""
            =======================================================================-
                                   <<<<<PLEASE SIGN UP>>>>>
            =======================================================================
          """)
    z = input("ENTER THE USERNAME:")
    x = pwinput("ENTER THE PASSWORD:")
    data = (z, x)
    sql = 'INSERT INTO signup_user_data (user_name, user_id) VALUES (%s, %s)'
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    print("""
              ===================================================================-
                                  <<<<< SIGN UP SUCCESSFULLY>>>>>
              ===================================================================
          """)
    print(">------------------------------------------------------------------------------------<")
    signin()

def signin():
    print("""
            =======================================================================
                                   <<<<<PLEASE SIGN IN>>>>>
            =======================================================================
          """)
    while True:
        q = input("ENTER THE USERNAME:")
        w = pwinput("ENTER PASSWORD:")
        # Check if the entered username and password are valid
        sql = 'SELECT * FROM signup_user_data WHERE user_name = %s AND user_id = %s'
        cur = con.cursor()
        cur.execute(sql, (q, w))
        user = cur.fetchone()  # Fetch the first matching row
        if user:
            print("""
                  =================================================================
                                     {{SIGN IN SUCCESSFULLY}}
                  =================================================================
              """)
            
            os.system("cls")
            print(">-------------------------------------------------------------------------------------<")
            topic()
            choose_task()
            main()
            break  # Exit the loop if the login is successful
        else:
            print("Wrong username or password. Please try again.")
            signin()


  # Perform user registration
  # Perform user sign-in

def opd():      
    n = input("PATIENT NAME: ")
    c = input("PATIENT ID:")
    t = input("DOCTOR NAME: ")
    o = input("DISEASE:")
    u = "BED REST"
    r = input("FATHER NAME: ")
    a = input("ADDRESS: ")
    p = input("NATIONALITY: ")
    q = input("MOBILE NO: ")
        
        # Prompt the user for Ayushman card input based on the 'w' value
    w = input("AYUSHMAN CARD YES OR NO: ")
    if w.lower() == 'yes':
         ayushman_card_number = input("AYUSHMAN CARD NUMBER: ")
    else:
         ayushman_card_number = None
        
    e = input("GENDER: ")
    y = input("AADHAR NUMBER: ")
    data = (n, c, t, o, u, r, a, p, q, ayushman_card_number, e, y)  # Use ayushman_card_number here
    sql = 'insert into opd values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    con.close
    print("DOCTOR_ADVICE = EAT HEALTHY FOOD AND TAKE MEDICINES ON TIME PRESCRIBED BY THE DOCTOR")
    print("DATA ENTERED SUCCESSFULLY")
    main()
    print(">---------------------------------------------------------------------------<")
    choose_task()
    main()

def genr():
    query = "SELECT COUNT(PATIENT_NAME) 'PATIENT_NAME' FROM general_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()
    cur.close()
    if int(index[0]) <= 30:
        print("No of patients in general room are", index[0], "\n")
        n = input("PATIENT NAME: ")
        c = input("PATIENT ID: ")
        t = input("DOCTOR NAME: ")
        o = input("DISEASE:")
        u = "BED REST"
        r = input("FATHER NAME: ")
        a = input("ADDRESS: ")
        p = input("NATIONALITY: ")
        q = input("MOBILE NO: ")
        
        # Prompt the user for Ayushman card input based on the 'w' value
        w = input("AYUSHMAN CARD YES OR NO: ")
        if w.lower() == 'yes':
            ayushman_card_number = input("AYUSHMAN CARD NUMBER: ")
        else:
            ayushman_card_number = None
        
        e = input("GENDER: ")
        y = input("AADHAR NUMBER: ")
        data = (n, c, t, o, u, r, a, p, q, ayushman_card_number, e, y)  # Use ayushman_card_number here
        sql = 'insert into general_room values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cur = con.cursor()
        cur.execute(sql, data)
        con.commit()
        print("DOCTOR_ADVICE = EAT HEALTHY FOOD AND TAKE MEDICINES ON TIME PRESCRIBED BY THE DOCTOR")
        print("DATA ENTERED SUCCESSFULLY")
        print(">---------------------------------------------------------------------------<")
        choose_task()     
        main()
    else:
        print("MAXIMUM PATIENT ADMITED!!")
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
def acr():
    query = "SELECT COUNT(PATIENT_NAME) 'PATIENT_NAME' FROM ac_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()[0]
    cur.close()
    if index <= 30:
        print("No of patients in ac room are", index[0], "\n")
        n = input("PATIENT NAME: ")
        z = input("PATIENT ID: ")
        t = input("DOCTOR NAME: ")
        o = input("DISEASE:")
        u = "BED REST"
        r = input("FATHER NAME: ")
        a = input("ADDRESS: ")
        p = input("NATIONALITY: ")
        q = input("MOBILE NO: ") 
        # Prompt the user for Ayushman card input based on the 'w' value
        w = input("AYUSHMAN CARD YES OR NO: ")
        if w.lower() == 'yes':
            ayushman_card_number = input("AYUSHMAN CARD NUMBER: ")
        else:
            ayushman_card_number = None
        e = input("GENDER: ")
        y = input("AADHAR NUMBER: ")
        data = (n, z, t, o, u,  r, a, p, q, ayushman_card_number, e, y)  # Use ayushman_card_number here
        sql = 'insert into ac_room values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        
        cur.execute(sql, data)
        con.commit()
        cur.close()
        print("DOCTOR_ADVICE = EAT HEALTHY FOOD AND TAKE MEDICINES ON TIME PRESCRIBED BY THE DOCTOR")
        print("DATA ENTERED SUCCESSFULLY")      
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
    else:
        print("Maximum paitent admited !!")
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
   
def dlxr():
    query = "SELECT COUNT(PATIENT_NAME) 'PATIENT_NAME' FROM deluxe_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()
    if int(index[0]) <= 1:
        print("No of patients in deluxe room are", index[0], "\n")
        n = input("PATIENT NAME: ")
        c = input("PATIENT ID: ")
        t = input("DOCTOR NAME: ")
        o = input("DISEASE:")
        u = "BED REST"
        r = input("FATHER NAME: ")
        a = input("ADDRESS: ")
        p = input("NATIONALITY: ")
        q = input("MOBILE NO: ") 
        # Prompt the user for Ayushman card input based on the 'w' value
        w = input("AYUSHMAN CARD YES OR NO: ")
        if w.lower() == 'yes':
            ayushman_card_number = input("AYUSHMAN CARD NUMBER: ")
        else:
            ayushman_card_number = None
        e = input("GENDER: ")
        y = input("AADHAR NUMBER: ")
        data = (n, c, t, o, u,  r, a, p, q, ayushman_card_number, e, y)  # Use ayushman_card_number here
        sql = 'insert into deluxe_room values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cur = con.cursor()
        cur.execute(sql, data)
        con.commit()
        print("DOCTOR_ADVICE = EAT HEALTHY FOOD AND TAKE MEDICINES ON TIME PRESCRIBED BY THE DOCTOR")
        print("DATA ENTERED SUCCESSFULLY")      
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
    else:
        print("Maximum paitent admited !!")
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
# r = romove
def rgenr():
    c=input("PATIENT NAME:")
    r=input("PATIENT ID:")
    data = (c,r)
    sql = 'delete from general_room where patient_name = %s and patient_id = %s'
    cur = con.cursor()
    cur.execute(sql,data)
    con.commit()
    print("DATA UPDATED")
    print(">-------------------------------------------------------------------------<")
    choose_task()
    main()
    
def racr():
    c=input("PATIENT NAME:")
    r=input("PATIENT ID:")
    data = (c,r)
    sql = 'delete from ac_room where patient_name = %s and patient_id = %s'
    cur = con.cursor()
    cur.execute(sql,data)
    con.commit()
    print("DATA UPDATED")
    print(">--------------------------------------------------------------------------<")
    choose_task()
    main()

def rdlxr():
    c=input("PATIENT NAME:")
    r=input("PATIENT ID:")
    data = (c,r)
    sql = 'delete from deluxe_room where patient_name = %s and patient_id = %s'
    cur = con.cursor()
    cur.execute(sql,data)
    con.commit()
    print("DATA UPDATED")
    print(">-----------------------------------------------------------------------------<")
    choose_task()
    main()
#d = data of ....
def dopd():
    cl = input("patient id:")
    data = (cl,)
    sql = "select * from opd where patient_id = %s"
    cur = con.cursor()
    cur.execute(sql,data)
    d = cur.fetchall()
    for i in d:    
        table1 = [["PATIENT NAME",i[0]],["PATIENT ID",i[1]],["DOCTOR NAME",i[2]],["DISEASE NAME",i[3]],["DOCTOR ADVICE",i[4]],["FATHER NAME",i[5]],["ADDRESS",i[6]],["NATIONALITY",i[7]],["MOBILE NO.",i[8]],["AYUSHMAN CARD",i[9]],["GENDER",i[10]],["AADHAR CARD NO.",i[11]]]
        print(tabulate(table1,tablefmt="grid"))
        print("DONE")
        print(">---------------------------------------------------------------------------<")
        choose_task()
        main()
# p = patient
def dgenrp():
    cl = input("patient id:")
    data = (cl,)
    sql = "select * from general_room where patient_id = %s"
    cur = con.cursor()
    cur.execute(sql,data)
    d = cur.fetchall()
    for i in d:    
        table1 = [["PATIENT NAME",i[0]],["PATIENT ID",i[1]],["DOCTOR NAME",i[2]],["DISEASE",i[3]],["DOCTOR ADVICE",i[4]],["FATHER NAME",i[5]],["ADDRESS",i[6]],["NATIONALITY",i[7]],["MOBILE NO.",i[8]],["AYUSHMAN CARD",i[9]],["GENDER",i[10]],["AADHAR CARD NO.",i[11]]]
        print(tabulate(table1,tablefmt="grid"))
        print("DONE")
        print(">-------------------------------------------------------------------------------------------<")
        choose_task()
    main()

def dacrp():
    cl = input("patient id:")
    data = (cl,)
    sql = "select * from ac_room where patient_id = %s"
    cur = con.cursor()
    cur.execute(sql,data)
    d = cur.fetchall()
    for i in d:    
        table1 = [["PATIENT NAME",i[0]],["PATIENT ID",i[1]],["DOCTOR NAME",i[2]],["DISEASE",i[3]],["DOCTOR ADVICE",i[4]],["FATHER NAME",i[5]],["ADDRESS",i[6]],["NATIONALITY",i[7]],["MOBILE NO.",i[8]],["AYUSHMAN CARD",i[9]],["GENDER",i[10]],["AADHAR CARD NO.",i[11]]]
        print(tabulate(table1,tablefmt="grid"))
        print("DONE")
        print(">----------------------------------------------------------------------------------------------<")
        choose_task()
    main()

def ddlxrp():
    cl = input("patient id:")
    data = (cl,)
    sql = "select * from deluxe_room where patient_id = %s"
    cur = con.cursor()
    cur.execute(sql,data)
    d = cur.fetchall()
    for i in d:    
        table1 = [["PATIENT NAME",i[0]],["PATIENT ID",i[1]],["DOCTOR NAME",i[2]],["DISEASE",i[3]],["DOCTOR ADVICE",i[4]],["FATHER NAME",i[5]],["ADDRESS",i[6]],["NATIONALITY",i[7]],["MOBILE NO.",i[8]],["AYUSHMAN CARD",i[9]],["GENDER",i[10]],["AADHAR CARD NO.",i[11]]]
        print(tabulate(table1,tablefmt="grid"))
        print("DONE")
        print(">----------------------------------------------------------------------------------------------------<")
        choose_task()
    main()

def ac_count():
    query = " select count(PATIENT_NAME) 'PATIENT_NAME' from ac_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()
    if index[0] <= 30:
        print("No of patients are ",index[0])
    else:
        print("Maximum limit is reached!!")
        choose_task()
    main()

def gen_count():
    query = " select count(PATIENT_NAME) 'PATIENT_NAME' from general_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()
    if index[0] <= 30:
        print("No of patients are ",index[0])
    else:
        print("Maximum limit is reached")
        choose_task()
    main()

def delu_count():
    query = " select count(PATIENT_NAME) 'PATIENT_NAME' from deluxe_room;"
    cur = con.cursor()
    cur.execute(query)
    index = cur.fetchone()
    if index[0] <= 30:
        print("No of patients are ",index[0])
    else:
        print("Maximum limit is reached")
        choose_task()
    main()
def main():
    print("""
    *****************************************************************************************************************************
    *1.OPD PATIENT       ADMIT PATIENT->        DISCHARGE PATIENT->      SHOW PATIENT->                  NUMBER OF PATIENT IN-> *
    *                    2.GENERAL ROOM         5.GENERAL ROOM           8.OPD PATIENT                   12.GENERAL ROOM        *
    *                    3.AC ROOM              6.AC ROOM                9.GENERAL ROOM ADMIT PATIENT    13.AC ROOM             *
    *                    4.AC DELUXE ROOM       7.AC DELUXE ROOM        10.AC ROOM ADMIT PATIENT         14.DELUXE ROOM         *
    *                                                                   11.AC DELUXE ROOM PATIENT                               *
    *                                                                                                                           *
    *                                                      15.Exit                                                              *
    *****************************************************************************************************************************
    """)
    print("CHOOSE TASK")
    choice = input("enter task no.")
    print(">--------------------------------------<")
    if(choice=='1'):
        opd()
    elif(choice=='2'):
        genr()
    elif(choice=='3'):
        acr()
    elif(choice=='4'):
        dlxr()
    elif(choice=='5'):
        rgenr()
    elif(choice=='6'):
        racr()
    elif(choice=='7'):
        rdlxr()
    elif(choice=='8'):
        dopd()
    elif(choice=='9'):
        dgenrp()
    elif(choice=='10'):
        dacrp()
    elif(choice=='11'):
        ddlxrp()
    elif choice=="12":
        gen_count()
    elif choice=="13":
        ac_count()
    elif(choice=="14"):
        delu_count()
    elif(choice=="15"):
        exit()
    else:
        print("wrong choice")
        main()
def pswd():
    p = pwinput("ENTER THE DATABASE PASSWORD:",'*')
    if p == "root":
        
        print(">--------------------------------------------------------------------------------<")
        signup()
    else:
        print("wrong password")
        pswd()
pswd()


