"""Module contains mocked data to check correctness of working the db_service"""
import unittest

import mysql.connector

from db_service.db_actions import Database


class TestDatabaseMethods(unittest.TestCase):

	def test_singleton(self):
		db_connection = Database()
		second_connection = Database()

		self.assertIs(db_connection, second_connection)

	def test_connection(self):
		connection = mysql.connector.connect(
			user='root', password='root', host='sql_server', port=3306, database="offers"
		)
		print("Db connected")
