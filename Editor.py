from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
import SqliteConnector

class EditorBlock(QWidget):
	def __init__(self, id, main):
		super().__init__()

		self.__main = main	

		# connetto al DB e scarico i dati della nota
		database=SqliteConnector.Database()
		dato=database.GetNoteByID(id)
		database.Close()

		# edito il titolo della finestra con il titolo della nota e aggiungo il testo
		self.__main.setWindowTitle(dato[0][0])
		self.label = QLabel(dato[0][1])
		layout = QVBoxLayout()
		layout.addWidget(self.label)
		self.setLayout(layout)

		# creo il pulsante per uscire
		button = QPushButton('exit', self)
		button.clicked.connect(self.on_click)

	def on_click(self):
		print("Exit!")
		self.__main.resetWindows()

		