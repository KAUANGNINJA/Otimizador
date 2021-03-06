# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 403)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowrame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(56, 58, 89);\n"
"}")
        self.dropShadowrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.droprame.setObjectName("dropShadowrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowrame)
        self.label_title.setGeometry(QtCore.QRect(-30, 10, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(215, 157, 255);")
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_descriao = QtWidgets.QLabel(self.dropShadowrame)
        self.label_descriao.setGeometry(QtCore.QRect(-30, 70, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_descriao.setFont(font)
        self.label_descriao.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_descriao.setTextFormat(QtCore.Qt.AutoText)
        self.label_descriao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descriao.setObjectName("label_descriao")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowrame)
        self.progressBar.setGeometry(QtCore.QRect(30, 260, 531, 21))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"Shadow
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:0.988636, y2:0.517, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowrame)
        self.label_loading.setGeometry(QtCore.QRect(-20, 290, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_loading.setTextFormat(QtCore.Qt.AutoText)
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_copright = QtWidgets.QLabel(self.dropShadowrame)
        self.label_copright.setGeometry(QtCore.QRect(0, 340, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_copright.setFont(font)
        self.label_copright.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_copright.setTextFormat(QtCore.Qt.AutoText)
        self.label_copright.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copright.setObjectName("label_copright")
        self.pushButton = QtWidgets.QPushButton(self.dropShadowrame)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 211, 51))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:0.988636, y2:0.517, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.dropShadowrame)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 120, 211, 51))
        self.pushButton_2.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:0.988636, y2:0.517, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.dropShadowrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Otimizador"))
        self.label_title.setText(_translate("MainWindow", "<strong>OTIMIZADOR</strong> DE COMPUTADOR"))
        self.label_descriao.setText(_translate("MainWindow", "<strong>PARA</strong> WINDOWS"))
        self.label_loading.setText(_translate("MainWindow", "loading....."))
        self.label_copright.setText(_translate("MainWindow", "<strong>COPRIGHT</strong> ByKauan"))
        self.pushButton.setText(_translate("MainWindow", "Otimizar"))
        self.pushButton_2.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
