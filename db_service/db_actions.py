import mysql.connector
from pymongo import MongoClient

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

	@staticmethod
	def process(body):
		#MS TODO: PROCESS INCOMING DATA
		pass

	@classmethod
	def __call__(cls):
		if not hasattr(cls, "instance"):
			cls.instance = super.__new__(cls)
		return cls.instance

	def __init__(self):
		#MS TODO: sprawdzenie, czy baza istnieje, jeśli nie istnieje - utworzyć
		self.client = None
		self.db = None
		self.check_if_db_exists()
		self.establish_connection()

	def establish_connection(self):
		"""
		establishes connection between service and database
		:return:
		"""
		self.db = mysql.connector.connect(
			user='root', password='root', host='sql_server:3306', database="offers"
		)
		print("Db connected")

	def close_connection(self):
		self.client.close()

	def check_if_db_exists(self):
		pass

	def create_database(self):
		self.db.cursor.execute("CREATE DATABASE offers")
		pass


