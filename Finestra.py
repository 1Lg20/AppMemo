from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QScrollArea
import BlockHome

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

		#creo scrollarea per Box
		self.__CreaListBox()
		self.containerLayout.addWidget(self.scroll_area)
		self.setCentralWidget(self.container)
		

		print("Blocchi creati: ", len(self.__ListBLock))

	
	#create block
	def __CreaListBox(self):
		self.ListBlockW = QWidget()
		self.ListBlockL = QVBoxLayout()
		self.ListBlockW.setLayout(self.ListBlockL)

		self.scroll_area = QScrollArea()
		self.scroll_area.setWidgetResizable(True)
		self.scroll_area.setWidget(self.ListBlockW)	

		element = [
			{"name": "titolo1", "id": 0},
			{"name": "titolo2", "id": 1},
			{"name": "titolo3", "id": 2},
			{"name": "titolo4", "id": 3},
			{"name": "titolo5", "id": 4},
			{"name": "titolo6", "id": 5},
			{"name": "titolo7", "id": 6},
			{"name": "titolo8", "id": 7},
			{"name": "titolo9", "id": 8},
			{"name": "titolo10", "id": 9},
		]

		for i in range(len(element)):
			Block= BlockHome.BlockHome(element[i]["name"], element[i]["id"])
			self.__ListBLock.append(Block)
			self.ListBlockL.addWidget(Block)
