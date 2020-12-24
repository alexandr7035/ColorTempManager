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
        print("ui ok")



        # Override the title
        self.setWindowTitle(params.WINDOW_TITLE)

        # Update ui on start
        self.dayTempSlider.setMinimum(params.TEMP_MIN_VALUE)
        self.dayTempSlider.setMaximum(params.TEMP_MAX_VALUE)

        self.stateCheckBox.stateChanged.connect(self.changeState)

        self.dayTempSlider.sliderReleased.connect(self.updateDayTempValue)
        self.dayTempSlider.valueChanged.connect(self.dayTempSliderMoved)


        self.updateUI()
    
    def updateUI(self):

        # Set values from settings
        day_value = self.client.get_day_temp_value()
        
        self.dayTempSlider.setValue(day_value)
        self.dayTempLabel.setText(str(day_value))
        self.stateCheckBox.setChecked(self.client.check_if_enabled())


    def changeState(self, state):

        if state == Qt.Checked:
            self.client.set_enabled(True)
            
        else:
            self.client.set_enabled(False)
           

    # Called when slider value changed
    def dayTempSliderMoved(self, value):
        self.dayTempLabel.setText(str(value))


    # Called only when mouse released
    def updateDayTempValue(self):
        value = self.dayTempSlider.value()
        print("value changed " + str(value))
        self.client.set_day_temp_value(value)







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    app.exec_()
