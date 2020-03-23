import mysql.connector

print("import finished")


cnx = mysql.connector.connect(
    user = 'root',
    password = 'AycheIsCool12!',
    host = '159.89.132.49',
    database = 'phpmyadmin')
cursor = cnx.cursor()

print("Connection made!")

query = 'SELECT COUNT(*) FROM users u WHERE u.stUserName = "streams" AND u.stPassword = "mayonnaise"'

cursor.execute(query)

print(cursor)

cursor.close()
cnx.close()