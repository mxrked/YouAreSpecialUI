

from PyQt5 import QtCore, QtGui, QtWidgets
from resources.qrc import vault_boy, terminal_bg
from resources.files import functions
from resources.files import backupFiles

import StatsWindow

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):

        ''' Functions '''
        def enterStatsWindow():

            self.ui = StatsWindow.Ui_StatsWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding Start window
            StartWindow.hide()

            print("Routing to Stats window")

        StartWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(800, 800)
        StartWindow.setMinimumSize(QtCore.QSize(800, 800))
        StartWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startWindow_TerminalBGFrame = QtWidgets.QFrame(self.centralwidget)
        self.startWindow_TerminalBGFrame.setStyleSheet("border-image: url(:/newPrefix/imgs/terminal-bg.png);")
        self.startWindow_TerminalBGFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.startWindow_TerminalBGFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.startWindow_TerminalBGFrame.setObjectName("startWindow_TerminalBGFrame")
        self.startWindow_SubHeadingLabel = QtWidgets.QLabel(self.startWindow_TerminalBGFrame)
        self.startWindow_SubHeadingLabel.setGeometry(QtCore.QRect(0, 80, 791, 81))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(22)
        self.startWindow_SubHeadingLabel.setFont(font)
        self.startWindow_SubHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_SubHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_SubHeadingLabel.setObjectName("startWindow_SubHeadingLabel")
        self.startWindow_MainHeadingLabel = QtWidgets.QLabel(self.startWindow_TerminalBGFrame)
        self.startWindow_MainHeadingLabel.setGeometry(QtCore.QRect(0, 120, 791, 111))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(26)
        self.startWindow_MainHeadingLabel.setFont(font)
        self.startWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_MainHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_MainHeadingLabel.setObjectName("startWindow_MainHeadingLabel")
        self.startWindow_VaultBoyLabel = QtWidgets.QLabel(self.startWindow_TerminalBGFrame)
        self.startWindow_VaultBoyLabel.setGeometry(QtCore.QRect(280, 260, 241, 231))
        self.startWindow_VaultBoyLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"}")
        self.startWindow_VaultBoyLabel.setText("")
        self.startWindow_VaultBoyLabel.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/vault_boy.png"))
        self.startWindow_VaultBoyLabel.setScaledContents(True)
        self.startWindow_VaultBoyLabel.setObjectName("startWindow_VaultBoyLabel")
        self.startWindow_ExitBtn = QtWidgets.QPushButton(self.startWindow_TerminalBGFrame)
        self.startWindow_ExitBtn.clicked.connect(functions.exitApp)
        self.startWindow_ExitBtn.setGeometry(QtCore.QRect(429, 580, 90, 50))
        self.startWindow_ExitBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.startWindow_ExitBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(14)
        self.startWindow_ExitBtn.setFont(font)
        self.startWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_ExitBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.startWindow_ExitBtn.setObjectName("startWindow_ExitBtn")
        self.startWindow_BeginBtn = QtWidgets.QPushButton(self.startWindow_TerminalBGFrame)
        self.startWindow_BeginBtn.clicked.connect(enterStatsWindow)
        self.startWindow_BeginBtn.setGeometry(QtCore.QRect(270, 580, 105, 50))
        self.startWindow_BeginBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.startWindow_BeginBtn.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(14)
        self.startWindow_BeginBtn.setFont(font)
        self.startWindow_BeginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_BeginBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.startWindow_BeginBtn.setObjectName("startWindow_BeginBtn")
        self.startWindow_MadeWithLabel = QtWidgets.QLabel(self.startWindow_TerminalBGFrame)
        self.startWindow_MadeWithLabel.setGeometry(QtCore.QRect(10, 735, 781, 61))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(11)
        self.startWindow_MadeWithLabel.setFont(font)
        self.startWindow_MadeWithLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgba(225, 225, 225, 165);\n"
"}")
        self.startWindow_MadeWithLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_MadeWithLabel.setObjectName("startWindow_MadeWithLabel")
        self.verticalLayout.addWidget(self.startWindow_TerminalBGFrame)
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "YouAreSpecialUI - Start Window"))
        self.startWindow_SubHeadingLabel.setText(_translate("StartWindow", "YOU ARE"))
        self.startWindow_MainHeadingLabel.setText(_translate("StartWindow", "S.P.E.C.I.A.L"))
        self.startWindow_ExitBtn.setText(_translate("StartWindow", "EXIT"))
        self.startWindow_BeginBtn.setText(_translate("StartWindow", "BEGIN"))
        self.startWindow_MadeWithLabel.setText(_translate("StartWindow", "Made with PyQt5"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()

    # Backing up the current files (Uncomment to create backup files)
    backupFiles.backupAllFiles()

    sys.exit(app.exec_())
