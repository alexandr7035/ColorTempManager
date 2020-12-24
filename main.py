import sys 
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import design 
import params
import client


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
    
        self.client = client.Client()

        self.setupUi(self)

        # Create working directory
        if not os.path.isdir(params.WORK_DIR):
            os.mkdir(params.WORK_DIR)

        # Override the title
        self.setWindowTitle(params.WINDOW_TITLE)

        # Update ui on start
        self.dayTempSlider.setMinimum(params.TEMP_MIN_VALUE)
        self.dayTempSlider.setMaximum(params.TEMP_MAX_VALUE)

        self.stateCheckBox.stateChanged.connect(self.changeState)
        self.dayTempSlider.valueChanged.connect(self.changeDayValue)


        self.updateUI()
    
    def updateUI(self):
        # Set values from settings

        day_value = self.client.get_day_temp_value()
        self.dayTempSlider.setValue(day_value)
        self.dayTempLabel.setText(str(day_value))

        self.stateCheckBox.setChecked(self.client.check_if_enabled())


    def changeState(self, state):

        if state == Qt.Checked:
            #self.manager.update()
            pass
        else:
            #self.manager.stop()
            pass


    def changeDayValue(self, value):
        print("value changed " + str(value))
        #self.manager.setDayTempValue(value)
        pass

        #self.dayTempLabel.setText(str(self.manager.getDayTempValue()))

        if self.stateCheckBox.isChecked():
            pass




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()
