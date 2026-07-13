from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel

from Config import ConfigFinestra, ConfigBlock

class MainWindow(QMainWindow):

    __ListBLock=[]

    def __init__(self):
        super().__init__()

        # set windows
        self.setWindowTitle(ConfigFinestra.NomeFinestra)
        self.setWindowIcon(QIcon(ConfigFinestra.Icon))
        self.setMinimumSize(QSize(ConfigFinestra.MinHeight, ConfigFinestra.MinWidth))

        #create block
        self.__ListBLock.append(self.__creaBlock())
        print("Blocchi creati: ", len(self.__ListBLock))
       
    # method to create block
    def __creaBlock(self):
        Block= QLabel("Blocco")
        Block.setFixedSize(ConfigBlock.BlockDimensionH, ConfigBlock.BlockDimensionW)
        Block.setStyleSheet(ConfigBlock.Style)
        self.setCentralWidget(Block)
        return Block