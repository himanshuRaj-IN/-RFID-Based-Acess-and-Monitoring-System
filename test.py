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
    mycursor.execute("INSERT INTO entries (`datetime`,Name,location,rfid) VALUES (now(),'Chedi lal','library','dfsf832')")
    con.commit()
    mycursor.execute(f"SELECT * from `entries` e  ")
    meta_data = mycursor.fetchall()
    for x in meta_data:
        print(x)