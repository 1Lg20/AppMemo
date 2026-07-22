from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton, QSizePolicy, QHBoxLayout
import SqliteConnector

class EditorBlock(QWidget):
	def __init__(self, id, main):
		super().__init__()

		self.__main = main	

		# connetto al DB e scarico i dati della nota
		database=SqliteConnector.Database()
		dato=database.GetNoteByID(id)
		database.Close()
		self.ID=id

		# edito il titolo della finestra con il titolo della nota e aggiungo il testo
		self.__main.setWindowTitle(dato[0][0])
		self.Text = QTextEdit()
		self.Text.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.Text.setPlainText(dato[0][1])

		layout = QVBoxLayout()
		layout.addWidget(self.Text)	

		rigaButton=QWidget()
		rigaButtonLayout= QHBoxLayout()
		rigaButton.setLayout(rigaButtonLayout)

		# creo il pulsante per uscire
		buttonExit = QPushButton('Esci', self)
		buttonExit.clicked.connect(self.Esci)
		rigaButtonLayout.addWidget(buttonExit)	

		# creo il pulsante per uscire
		buttonSalva = QPushButton('Salva', self)
		buttonSalva.clicked.connect(self.Salva)
		rigaButtonLayout.addWidget(buttonSalva)

		layout.addWidget(rigaButton)	
		self.setLayout(layout)

	def Esci(self):
		print("Exit!")
		self.__main.resetWindows()

	def Salva(self):
		print("Salva")
		Testo=self.Text.toPlainText()
		database=SqliteConnector.Database()
		database.SalvaText(self.ID, Testo)
		database.Close()
		