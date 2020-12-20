import sys 
import os
from PyQt5 import QtWidgets

import design 
import params

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create working directory
        if not os.path.isdir(params.WORK_DIR):
            os.mkdir(params.WORK_DIR)

        # Override the title
        self.setWindowTitle(params.WINDOW_TITLE)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()