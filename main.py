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

        self.stateCheckBox.stateChanged.connect(self.changeState)
        self.dayTempSlider.valueChanged.connect(self.changeDayValue)


        self.updateUI()
    
    def updateUI(self):
        # Set values from settings
        self.dayTempSlider.setValue(self.manager.getDayTempValue())
        self.stateCheckBox.setChecked(self.manager.checkIfEnabled())
        
        self.dayTempLabel.setText(str(self.manager.getDayTempValue()))

    def changeState(self, state):

        if state == Qt.Checked:
            self.manager.update()
        else:
            self.manager.stop()


    def changeDayValue(self, value):
        print("value changed " + str(value))
        self.manager.setDayTempValue(value)

        self.dayTempLabel.setText(str(self.manager.getDayTempValue()))

        if self.stateCheckBox.isChecked():
            self.manager.update()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()
