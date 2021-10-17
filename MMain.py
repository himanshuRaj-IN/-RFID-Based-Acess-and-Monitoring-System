import config
import mysql.connector as connector

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
        while True:
            print("For Monitoring -> 1")
            print("    Control    -> 2")
            print("    Exit       -> 0")
            inp = int(input())
            if inp == 0:
                exit()
            elif inp==1:
                print("--------Welcome to Monitoring Section-------")
                while True:
                    print("What you want to Monitor Choose Accordingly :")
                    print("For Library   ----------> 1")
                    print("    Lab103    ----------> 2")
                    print("    Academics   --------> 3")
                    print("    Individual Activity-> 4")
                    print("    Individual Details -> 5")
                    print("    Exit  --------------> 0")
                    inp=int(input())
                    if inp==0:
                        exit()
                    if inp==1:
                        print("---------------------------- Library --------------------------- ")
                        fdate = input("From YYYY-MM-DD HH:MM:SS : ")
                        tdate = input(" TO  YYYY-MM-DD HH:MM:SS : ")
                        try:
                            mycursor.execute(f"SELECT * FROM entries e WHERE (`datetime` BETWEEN '{fdate}' AND '{tdate}')And (location = 'library') ORDER BY `datetime` ;")
                            meta_data = mycursor.fetchall()
                            a=1
                            print("_____________________________________________________________________")
                            print("          Datetime             UID        Location        Name ")
                            print("_____________________________________________________________________")
                            for x in meta_data:
                                print(f"{a}.  {x[0]}    {x[3]}     {x[2]}     {x[1]}")
                                a=a+1
                            print("_____________________________________________________________________")

                        except:
                            print(" An Error occured !!!!!! ")
                            break
                    elif inp==2:
                        print("Lab103")
                        break
                    elif inp == 3:
                        print("Academics")
                        break
                    elif inp == 4:
                        print("individual activity")
                        print("-------------------  Individual Activity  ------------------------ ")
                        uid =   input("         Enter UID       : ")
                        fdate = input("From YYYY-MM-DD HH:MM:SS : ")
                        tdate = input(" TO  YYYY-MM-DD HH:MM:SS : ")
                        try:
                            mycursor.execute(
                                f"SELECT * FROM entries e WHERE (`datetime` BETWEEN '{fdate}' AND '{tdate}')And (uid = '{uid}') ORDER BY `datetime` ;")
                            meta_data = mycursor.fetchall()
                            a = 1
                            print("_____________________________________________________________________")
                            print("          Datetime             UID        Location        Name ")
                            print("_____________________________________________________________________")
                            for x in meta_data:
                                print(f"{a}.  {x[0]}    {x[3]}     {x[2]}     {x[1]}")
                                a = a + 1
                            print("_____________________________________________________________________")

                        except:
                            print(" An Error occured !!!!!! ")
                            break

                    elif inp == 5:
                        print("For Individual Details ")
                        rfid_tag =input("Enter Unique UID : ")

                        mycursor.execute(f"SELECT *from `database` d  WHERE uid ='{rfid_tag}'")
                        meta_data = mycursor.fetchall()
                        meta_data=meta_data[0]

                        print("______________________________________________")
                        print("Name               : ",meta_data[3])
                        print("Contact no.        : ",meta_data[6])
                        print("Email              : ",meta_data[7])
                        print("Card Type          : ",meta_data[1])
                        print("Card Status        : ",meta_data[2])
                        print("RFID Tag ID no     : ",meta_data[0])
                        print("Department         : ",meta_data[4])
                        print("Registration No.   : ",meta_data[5])
                        print("Library Access     : ",meta_data[8])
                        print("Academics Access   : ",meta_data[9])
                        print("S A  Center Access : ",meta_data[10])
                        print("Lab EE121 Access   : ",meta_data[11])
                        print("")
                        print("______________________________________________")
                        break
                    else:
                        print("Not a valid input Try again")

            elif inp == 2:
                print("--------Welcome to Control Section-------")
                while True:
                    print("For   Adding New User ---> 1")
                    print("      Delete User     ---> 2")
                    print("      Edit Permissions --> 3")
                    print("      Back  -------------> 0")
                    inp=input()
                    if inp == 0:
                        break
                    elif inp == 1:
                        print("Enter the detail of user ")
                        name=             input("Name           : ")
                        mobile=           input("Contact NO     : ")
                        email=            input("Email ID       : ")
                        type=             input("Type of User   : ")
                        card_status=      input("Card Status    : ")
                        RFID_tag=         input("RFID Tag ID no : ")
                        department=       input("Depatment      : ")
                        regd_no=          input("Regd No.       : ")
                        Library=          input("Library Access : ")




            else:
                print("Not a valid Input")


    input()
