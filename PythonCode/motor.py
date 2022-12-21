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
        self.setWindowTitle("HÜKMEDİCİ")
        self.setWindowIcon(QtGui.QIcon("motor.webp"))
        self.setStyleSheet("background-color: white")
        self.ui.slider_hiz.valueChanged.connect(self.motorControl)
        self.ui.pushButton_sec.clicked.connect(self.connect)
        self.ui.radioButton_baslat.clicked.connect(self.motorControl)
        self.ui.radioButton_durdur.clicked.connect(self.motorControl)
        self.ui.radioButton_saatyon.clicked.connect(self.motorControl)
        self.ui.radioButton_tersyon.clicked.connect(self.motorControl)

    def connect(self): 
        try: 
            comInfo = self.ui.comboBox.currentText()
            self.ui.label_com.setText(comInfo)
            self.serial_connection = serial.Serial(port=self.ui.comboBox.currentText(), baudrate=115200, timeout=.1)
            self.com_flag = True
        except: 
            self.ui.info.setText("COM PORTA BAĞLANILAMIYOR.")

    def motorControl(self): 
        if self.com_flag: 
            info = '\n'
            if self.ui.radioButton_baslat.isChecked(): 
                self.serial_connection.write(bytes('-1', 'utf-8'))
                sleep(0.05)
                d = self.serial_connection.readline()
                info = info + str(d.decode('utf-8')) + '\n'
            if self.ui.radioButton_durdur.isChecked(): 
                self.serial_connection.write(bytes('-2', 'utf-8'))
                sleep(0.05)
                d = self.serial_connection.readline()
                info = info + str(d.decode('utf-8')) + '\n'
            if self.ui.radioButton_saatyon.isChecked(): 
                self.serial_connection.write(bytes('-3', 'utf-8'))
                sleep(0.05)
                d = self.serial_connection.readline()
                info = info + str(d.decode('utf-8')) + '\n'
            if self.ui.radioButton_tersyon.isChecked(): 
                self.serial_connection.write(bytes('-4', 'utf-8'))
                sleep(0.05)
                d = self.serial_connection.readline()
                info = info + str(d.decode('utf-8')) + '\n'
            if self.ui.slider_hiz.value() > 0: 
                self.ui.label_yuzde.setText(str(format(float(self.ui.slider_hiz.value()*100/255), ".3")))
                self.ui.label_gerilim.setText(str(format(float(self.ui.slider_hiz.value()*9/255), ".3")))
                self.serial_connection.write(bytes(str(self.ui.slider_hiz.value()), 'utf-8'))
                # sleep(0.05)
                d = self.serial_connection.readline()
                info = info + str(d.decode('utf-8')) + '\n'

            self.ui.info.setText(info)




def App(): 
    app_ = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app_.exec_())

if __name__ == "__main__":
    App()
