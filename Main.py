import sys
import Finestra
from PyQt6.QtWidgets import QApplication


def Main():
    app = QApplication(sys.argv)

    window = Finestra.MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__":
    Main()