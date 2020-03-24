from sshtunnel import SSHTunnelForwarder
import mysql.connector

server = SSHTunnelForwarder(
    '159.89.132.49',
    ssh_username='root',
    ssh_password='AycheisCool12!',
    remote_bind_address=('127.0.0.1', 8080)
)
server.start()

print("ssh complete!\nStarting connection to db")

cnx = mysql.connector.connect(
    user = 'root',
    passwd = 'AycheIsCool12!',
    host = '127.0.0.1',
    database = 'phpmyadmin'
    )

# cursor = cnx.cursor()

print("Connection made!")

# query = 'SELECT COUNT(*) FROM users u WHERE u.stUserName = "streams" AND u.stPassword = "mayonnaise"'

# cursor.execute(query)

# print(cursor)

# cursor.close()
# cnx.close()