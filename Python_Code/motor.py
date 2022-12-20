import sys
from PyQt5 import QtWidgets, QtGui
from motor_ui import Ui_MainWindow
import serial
from time import sleep

class MyApp(QtWidgets.QMainWindow): 
    def __init__(self): 
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.slider_hiz.setRange(0,255)
        self.com_flag = False
        self.serial_connection = serial.Serial()
        self.setWindowTitle("MOTOR KONTROL UYGULAMASI")
        self.setWindowIcon(QtGui.QIcon("motor.webp"))
        self.setStyleSheet("background-color: turquoise")
        self.ui.slider_hiz.valueChanged.connect(self.motorControl)
        self.ui.pushButton_sec.clicked.connect(self.connect)
        self.ui.radioButton_baslat.clicked.connect(self.motorControl)
        self.ui.radioButton_durdur.clicked.connect(self.motorControl)
        self.ui.radioButton_saatyon.clicked.connect(self.motorControl)
        self.ui.radioButton_tersyon.clicked.connect(self.motorControl)

    def connect(self): 
        comInfo = self.ui.comboBox.currentText()
        print(comInfo)
        self.ui.label_com.setText(comInfo)
        self.serial_connection = serial.Serial(self.ui.comboBox.currentText(), 9600)
        self.com_flag = True

    def motorControl(self): 
        if self.com_flag: 
            val = self.ui.slider_hiz.value()
            if not(val >= 250): 
                bytmessage = bytes(str(val+5), encoding='ascii')
            else: 
                bytmessage = bytes(str(val),encoding="ascii")
                
            self.serial_connection.write(bytmessage)
            pre = int((val)*100/255)
            self.ui.label_yuzde.setText("%: "+ str(pre))
            self.ui.label_gerilim.setText(f"{9*pre/100} V")
            
            print(bytmessage)
            if self.ui.radioButton_baslat.isChecked(): 
                self.serial_connection.write(b'1')
            if self.ui.radioButton_durdur.isChecked(): 
                self.serial_connection.write(b'2')
            if self.ui.radioButton_saatyon.isChecked(): 
                self.serial_connection.write(b'3')
            if self.ui.radioButton_tersyon.isChecked(): 
                self.serial_connection.write(b'4')





def App(): 
    app_ = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app_.exec_())

if __name__ == "__main__":
    App()