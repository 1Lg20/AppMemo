import sqlite3
from Config import ConfigSqlite 

class Database():
	def __init__(self):
		self.__database=sqlite3.connect(ConfigSqlite.FileName)
		self.__cursor=self.__database.cursor()
	
	def GetNotes(self):
		self.__cursor.execute("SELECT ID, Title FROM Notes")
		return self.__cursor.fetchall()
