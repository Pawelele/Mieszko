import json

import mysql.connector


def singleton(cls):
	instances = {}
	def getinstance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return getinstance

@singleton
class Database:
	"""	Class to access the database """

	@classmethod
	def __call__(cls):
		if not hasattr(cls, "instance"):
			cls.instance = super.__new__(cls)
		return cls.instance

	def __init__(self):
		#MS TODO: sprawdzenie, czy baza istnieje, jeśli nie istnieje - utworzyć
		self.client = None
		self.db = None

		self.establish_connection()
		self.create_database()

	def process(self, body):
		self.fill_database_with_scraped_content(body)

	def fill_database_with_scraped_content(self, body):
		content = json.loads(body)
		self.db.cursor.execute(f"""INSERT INTO offers_list VALUES (
		{content["price"]},{content["price_for_m"]}, {content["area"]},
		{content["rooms_amount"]}, {content["title"]}, {content["offer"]}, 
		{content["short_description"]}, {content["href"]}, {content["image"]});""")

	def establish_connection(self):
		"""
		establishes connection between service and database
		:return:
		"""
		self.db = mysql.connector.connect(
				user='root', password='root', host='127.0.0.1', port=3306, database="offers"
			)
		print("Db connected")

	def close_connection(self):
		self.client.close()


	def create_database(self):
		pass
		# self.db.cursor.execute("CREATE DATABASE [IF NOT EXISTS] offers; CREATE TABLE offers_list (ID INT NOT NULL AUTO_INCREMENT, price varchar(30), price_for_m varchar(30), area varchar(30),"
		# 					   "rooms_amount INT, title varchar(30), offer varchar(30), short_description varchar(max), href varchar(max), image varchar(max));")
		# self.db.cursor.commit()


