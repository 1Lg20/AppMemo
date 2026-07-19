from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QScrollArea
import BlockHome
import SqliteConnector

from Config import ConfigFinestra, ConfigBlock

class MainWindow(QMainWindow):

	__ListBLock=[]

	def __init__(self):
		super().__init__()

		# set window
		self.setWindowTitle(ConfigFinestra.NomeFinestra)
		self.setWindowIcon(QIcon(ConfigFinestra.Icon))
		self.setMinimumSize(QSize(ConfigFinestra.MinHeight, ConfigFinestra.MinWidth))

		# creo container
		self.container=QWidget()
		self.containerLayout=QHBoxLayout()
		self.container.setLayout(self.containerLayout)
		self.setCentralWidget(self.container)

		#creo scrollarea per Box
		self.CreaListBox()
		

		print("Blocchi creati: ", len(self.__ListBLock))

	
	#create block
	def CreaListBox(self):
		# crea il contenitore dei block
		ListBlockW = QWidget()
		ListBlockL = QVBoxLayout()
		ListBlockW.setLayout(ListBlockL)

		# Creo la scroll Area e inserisco il contenitore dei block al suo interno
		self.__scroll_area = QScrollArea()
		self.__scroll_area.setWidgetResizable(True)
		self.__scroll_area.setWidget(ListBlockW)	

		# Scarico i dati dal Database
		database=SqliteConnector.Database()
		NotesList=database.GetNotes()
		database.Close()

		# Creo tanti block quenti sono gli elementi del databse e li inserisco nel contenitore
		for i in range(len(NotesList)):
			Block= BlockHome.BlockHome(NotesList[i][1], NotesList[i][0], self)
			self.__ListBLock.append(Block)
			ListBlockL.addWidget(Block)
		
		self.containerLayout.addWidget(self.__scroll_area)

	# cancello tutti i widget nel layout main
	def clear_layout(self):
		if self.containerLayout is not None:
			while self.containerLayout.count():
				child = self.containerLayout.takeAt(0)
				if child.widget() is not None:
					child.widget().deleteLater()
				elif child.layout() is not None:
					clear_layout(child.layout())

	# riporto la finestra allo stato originario
	def resetWindows(self):
		self.clear_layout()
		self.setWindowTitle(ConfigFinestra.NomeFinestra)
		self.CreaListBox()   
