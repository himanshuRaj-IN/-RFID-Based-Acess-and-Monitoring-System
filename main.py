# @ Himanshu Raj
#
import mysql.connector as connector
import config
from datetime import datetime

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
    mycursor.execute("SELECT *FROM entries")
    meta_data=mycursor.fetchall()
    for data in meta_data:
        print(data)
    dat=datetime.now()
    dat = dat.replace(microsecond=0)
    print(dat)


