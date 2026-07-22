import sqlite3
from Config import ConfigSqlite 

class Database():
	def __init__(self):
		self.__database=sqlite3.connect(ConfigSqlite.FileName)
		self.__cursor=self.__database.cursor()
	
	def GetNotes(self):
		self.__cursor.execute("SELECT ID, Title FROM Notes")
		return self.__cursor.fetchall()

	def GetNoteByID(self, id):
		self.__cursor.execute("SELECT Title, Context FROM Notes WHERE ID="+str(id))
		return self.__cursor.fetchall()
	
	def SalvaText(self, id, testo):
		Query="UPDATE Notes SET Context= ? WHERE ID= ?"
		
		self.__cursor.execute(Query, (testo, id))
		
		self.__database.commit()
	
	def Close(self):
		self.__database.close()
