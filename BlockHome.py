from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout
from Config import ConfigBlock

class BlockHome(QWidget):
	def __init__(self, Titolo, ID):
		super().__init__()
		self.label = QLabel(Titolo)
		self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.ID=ID
		
		layout = QVBoxLayout()
		layout.addWidget(self.label)

		self.setStyleSheet(ConfigBlock.StyleBlock)
		self.setFixedSize(ConfigBlock.BlockDimensionW, ConfigBlock.BlockDimensionH)
		self.setLayout(layout)

	# Override metodo mousePressEvent
	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.LeftButton:
			print("Il mio id è:"+str(self.ID))
	
	# cambio cursore quando hover
	def enterEvent(self, event):
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

	# reset cursore quando non hover
	def leaveEvent(self, event):
		self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))



		