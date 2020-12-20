import sys 
from PyQt5 import QtWidgets

import design 
import params

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Override the title
        self.setWindowTitle(params.WINDOW_TITLE)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()