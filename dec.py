from PyQt5 import QtCore, QtGui, QtWidgets
import cryptocode

class Ui_dec(object):
    def decode(self):
        text = self.dectext.toPlainText()
        password = self.decpass.toPlainText()
        decoded = cryptocode.decrypt(text, password)
        if decoded == False:
            self.decoutput.setText("wrong password or text")
        else:
            self.decoutput.setText(decoded)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        MainWindow.setMaximumSize(QtCore.QSize(450, 550))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.a3 = QtWidgets.QLabel(self.centralwidget)
        self.a3.setGeometry(QtCore.QRect(100, 400, 261, 71))
        self.a3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.a3.setStyleSheet("font: 8pt \"Acme\";")
        self.a3.setObjectName("a3")
        self.dec = QtWidgets.QLabel(self.centralwidget)
        self.dec.setGeometry(QtCore.QRect(100, 10, 261, 71))
        self.dec.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dec.setStyleSheet("font: 8pt \"Acme\";")
        self.dec.setObjectName("dec")
        self.decpass = QtWidgets.QTextEdit(self.centralwidget)
        self.decpass.setGeometry(QtCore.QRect(40, 220, 371, 41))
        self.decpass.setObjectName("decpass")
        self.a2 = QtWidgets.QLabel(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(100, 160, 261, 71))
        self.a2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.a2.setStyleSheet("font: 8pt \"Acme\";")
        self.a2.setObjectName("a2")
        self.dectext = QtWidgets.QTextEdit(self.centralwidget)
        self.dectext.setGeometry(QtCore.QRect(40, 110, 371, 41))
        self.dectext.setObjectName("dectext")
        self.a1 = QtWidgets.QLabel(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(90, 60, 281, 71))
        self.a1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.a1.setStyleSheet("font: 8pt \"Acme\";")
        self.a1.setObjectName("a1")
        self.decoutput = QtWidgets.QTextEdit(self.centralwidget)
        self.decoutput.setGeometry(QtCore.QRect(40, 450, 371, 41))
        self.decoutput.setObjectName("decoutput")
        self.deccon = QtWidgets.QPushButton(self.centralwidget)
        self.deccon.setGeometry(QtCore.QRect(150, 310, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(20)
        self.deccon.setFont(font)
        self.deccon.setObjectName("deccon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.deccon.clicked.connect(self.decode)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Decrypt"))
        self.a3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">OUTPUT</span></p></body></html>"))
        self.dec.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">DECRYPT</span></p></body></html>"))
        self.a2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">PASSWORD</span></p></body></html>"))
        self.a1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">ENCRYPTED TEXT</span></p></body></html>"))
        self.deccon.setText(_translate("MainWindow", "DECRYPT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dec()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
