import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '$07Imtsms77$'
	)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE nastech")

print ("Good to go!")