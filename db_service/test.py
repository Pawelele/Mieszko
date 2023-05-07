"""hjkhjkhjk"""
import mysql.connector


db = mysql.connector.connect(
			user='root', password='root', host='mysql', port=3306, database="offers"
		)
print("Db connected")
