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
		# print(type(body.value))
		# body_new = body.value.replace("\'", "\"")
		# content = json.loads(rf"{body_new}")
		content = self.get_dict_from_body(body.value)
		print("_____________________________________________________________________")
		print(content)
		query = f"""INSERT INTO offers_list (price, price_for_m, area, rooms_amount,title, offer, city, href, image) VALUES (
		'{content["price"]}','{content["price_for_m"]}', '{content["area"]}',
		'{content["rooms_amount"]}', '{content["title"]}', '{content["offer"]}', 
		'{content["short_description"]}', '{content["href"]}', '{content["image"]}');"""
		print(query)
		self.cursor.execute(query)
		self.db.commit()

	def get_dict_from_body(self, body):
		print(body)
		dicto = {}

		for item in body.split(","):
			print(item)
			# key = item.split("\': \'")[0].replace(" ", "").replace("\'", "").replace("{", "").replace("}", "")
			# value = item.split("\': \'")[1].replace(" ", "").replace("\'", "").replace("{", "").replace("}", "")
		return {item.split("\': \'")[0].replace("\'", "").replace("{", "").replace("}", ""): item.split(":")[1].replace(" ", "").replace("\'", "").replace("{", "").replace("}", "")
			for item in body.replace(r"\'", "").split(",")}

	def establish_connection(self):
		"""
		establishes connection between service and database
		:return:
		"""
		self.db = mysql.connector.connect(
				user='root', password='root', host='mysql', port=3306, database="offers"
			)
		self.cursor = self.db.cursor()
		print("Db connected")

	def close_connection(self):
		self.client.close()

	def create_database(self):
		print("+"*100)
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS offers")
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS offers_list (id INT NOT NULL AUTO_INCREMENT primary key, price varchar(30), price_for_m varchar(30), area varchar(30),
							   rooms_amount INT, title varchar(30), offer varchar(255), city varchar(255), href varchar(255), image varchar(255));""")