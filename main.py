import sys 
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import design 
import params
import manager


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create working directory
        if not os.path.isdir(params.WORK_DIR):
            os.mkdir(params.WORK_DIR)

        # Override the title
        self.setWindowTitle(params.WINDOW_TITLE)

        self.manager = manager.ColorTempManager()

        # Update ui on start
        self.dayTempSlider.setMinimum(params.TEMP_MIN_VALUE)
        self.dayTempSlider.setMaximum(params.TEMP_MAX_VALUE)

        self.nightTempSlider.setMinimum(params.TEMP_MIN_VALUE)
        self.nightTempSlider.setMaximum(params.TEMP_MAX_VALUE)

        self.stateCheckBox.stateChanged.connect(self.changeState)

        self.updateUI()
    
    def updateUI(self):
        # Set values from settings
        self.dayTempSlider.setValue(self.manager.getDayTempValue())
        self.nightTempSlider.setValue(self.manager.getNightTempValue())
        self.stateCheckBox.setChecked(self.manager.checkIfEnabled())
        
        self.dayTempLabel.setText(str(self.manager.getDayTempValue()))
        self.nightTempLabel.setText(str(self.manager.getNightTempValue()))


    def changeState(self, state):

        if state == Qt.Checked:
            self.manager.start()
        else:
            self.manager.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()
