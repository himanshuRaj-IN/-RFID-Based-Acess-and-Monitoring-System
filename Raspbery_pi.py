import config
import mysql.connector as connector

def library():
    inp = input("Enter the Value of RFID :  ")
    mycursor.execute(f"SELECT card_status,card_type,library,name,uid from `database` d  WHERE uid = '{inp}'")
    meta_data = mycursor.fetchall()

    try:
        meta_data = meta_data[0]
        if meta_data[0] == 1:
            if meta_data[2] == 1:
                print("---------------------------------------------")
                print(f"Welcome to Central Library {meta_data[3]} !!")
                mycursor.execute(f"INSERT INTO entries (`datetime`,Name,location,uid) VALUES (now(),'{meta_data[3]}','library','{meta_data[4]}')")
                con.commit()
                print("---- Your Entry Added into The Database  ----")
                print("---------------------------------------------")
            else:
                print(f"- Sorry {meta_data[3]} !! Access Denied !! -")
        else:
            print(f"- Sorry {meta_data[3]} !! Card Blocked / Dead !! -")
    except:
        print("--------  Not Found In Our Database  --------")
def academics():
    inp = input("Enter the Value of RFID :  ")
    mycursor.execute(f"SELECT card_status,card_type,academics,name,uid from `database` d  WHERE uid = '{inp}'")
    meta_data = mycursor.fetchall()

    try:
        meta_data = meta_data[0]
        if meta_data[0] == 1:
            if meta_data[2] == 1:
                print("-----------------------------------------------")
                print(f"Welcome to Academics Section {meta_data[3]} !!")
                mycursor.execute(
                    f"INSERT INTO entries (`datetime`,Name,location,uid) VALUES (now(),'{meta_data[3]}','academics','{meta_data[4]}')")
                con.commit()
                print("---- Your Entry Added into The Database  ----")
                print("---------------------------------------------")
            else:
                print(f"- Sorry {meta_data[3]} !! Access Denied !! -")
        else:
            print(f"- Sorry {meta_data[3]} !! Card Blocked / Dead !! -")
    except:
        print("--------  Not Found In Our Database  --------")
def student_activity_center ():
    inp = input("Enter the Value of RFID :  ")
    mycursor.execute(f"SELECT card_status,card_type,sac,name,uid from `database` d  WHERE uid = '{inp}'")
    meta_data = mycursor.fetchall()

    try:
        meta_data = meta_data[0]
        if meta_data[0] == 1:
            if meta_data[2] == 1:
                print("-----------------------------------------------")
                print(f"Welcome to Student Activity Center  {meta_data[3]} !!")
                mycursor.execute(
                    f"INSERT INTO entries (`datetime`,Name,location,uid) VALUES (now(),'{meta_data[3]}','sac','{meta_data[4]}')")
                con.commit()
                print("---- Your Entry Added into The Database  ----")
                print("---------------------------------------------")
            else:
                print(f"- Sorry {meta_data[3]} !! Access Denied !! -")
        else:
            print(f"- Sorry {meta_data[3]} !! Card Blocked / Dead !! -")

    except:
        print("--------  Not Found In Our Database  --------")
def auditorium():
    inp = input("Enter the Value of RFID :  ")
    mycursor.execute(f"SELECT card_status,card_type,auditorium,name,uid from `database` d  WHERE uid = '{inp}'")
    meta_data = mycursor.fetchall()

    try:
        meta_data = meta_data[0]
        if meta_data[0] == 1:
            if meta_data[2] == 1:
                print("-----------------------------------------------")
                print(f"Welcome to Main Auditorium   {meta_data[3]} !!")
                mycursor.execute(
                    f"INSERT INTO entries (`datetime`,Name,location,uid) VALUES (now(),'{meta_data[3]}','auditorium','{meta_data[4]}')")
                con.commit()
                print("---- Your Entry Added into The Database  ----")
                print("---------------------------------------------")
            else:
                print(f"- Sorry {meta_data[3]} !! Access Denied !! -")
        else:
            print(f"- Sorry {meta_data[3]} !! Card Blocked / Dead !! -")

    except:
        print("--------  Not Found In Our Database  --------")

if __name__ == '__main__':

    host = config.host
    user = config.user
    password = config.password
    database_name = config.database_name
    port = config.port
    con = connector.connect(host=host, user=user, passwd=password, database=database_name, port=port)
    if con.is_connected():
        print("connected to database")
        print(con.get_server_info())
    else:
        print("Error is connection ")
    mycursor = con.cursor()


    while True:
        auditorium()

        # Select azvove define function according to need !!