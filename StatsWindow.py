

from PyQt5 import QtCore, QtGui, QtWidgets
from resources.qrc import vault_boy, terminal_bg
from resources.files import functions
from resources.files import arrays_and_variables

import StartWindow, PerksWindow

class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):

        ''' Functions '''
        def enterStartWindow():

            self.window = QtWidgets.QMainWindow()
            self.ui = StartWindow.Ui_StartWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            StatsWindow.hide()
            print("Routing to Start window")
        def enterPerksWindow():

            self.window = QtWidgets.QMainWindow()
            self.ui = PerksWindow.Ui_PerksWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            StatsWindow.hide()
            print("Routing to Perks window")

        def addSSpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_SSpinBox.lineEdit().text() != 0 and self.statsWindow_SSpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.sPoints[0] != 0 and arrays_and_variables.sPoints[0] != 10:
                                        newPoint = arrays_and_variables.sPoints[0] + 1

                                        arrays_and_variables.sPoints.clear()
                                        arrays_and_variables.sPoints.append(newPoint)

                                        self.statsWindow_SSpinBox.lineEdit().setText(str(arrays_and_variables.sPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusSSpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_SSpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.sPoints[0] != 1:

                                newPoint = arrays_and_variables.sPoints[0] - 1

                                arrays_and_variables.sPoints.clear()
                                arrays_and_variables.sPoints.append(newPoint)

                                self.statsWindow_SSpinBox.lineEdit().setText(str(arrays_and_variables.sPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addPSpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_PSpinBox.lineEdit().text() != 0 and self.statsWindow_PSpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.pPoints[0] != 0 and arrays_and_variables.pPoints[0] != 10:
                                        newPoint = arrays_and_variables.pPoints[0] + 1

                                        arrays_and_variables.pPoints.clear()
                                        arrays_and_variables.pPoints.append(newPoint)

                                        self.statsWindow_PSpinBox.lineEdit().setText(str(arrays_and_variables.pPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusPSpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_PSpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.pPoints[0] != 1:

                                newPoint = arrays_and_variables.pPoints[0] - 1

                                arrays_and_variables.pPoints.clear()
                                arrays_and_variables.pPoints.append(newPoint)

                                self.statsWindow_PSpinBox.lineEdit().setText(str(arrays_and_variables.pPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addESpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_ESpinBox.lineEdit().text() != 0 and self.statsWindow_ESpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.ePoints[0] != 0 and arrays_and_variables.ePoints[0] != 10:
                                        newPoint = arrays_and_variables.ePoints[0] + 1

                                        arrays_and_variables.ePoints.clear()
                                        arrays_and_variables.ePoints.append(newPoint)

                                        self.statsWindow_ESpinBox.lineEdit().setText(str(arrays_and_variables.ePoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusESpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_ESpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.ePoints[0] != 1:

                                newPoint = arrays_and_variables.ePoints[0] - 1

                                arrays_and_variables.ePoints.clear()
                                arrays_and_variables.ePoints.append(newPoint)

                                self.statsWindow_ESpinBox.lineEdit().setText(str(arrays_and_variables.ePoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addCSpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_CSpinBox.lineEdit().text() != 0 and self.statsWindow_CSpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.cPoints[0] != 0 and arrays_and_variables.cPoints[0] != 10:
                                        newPoint = arrays_and_variables.cPoints[0] + 1

                                        arrays_and_variables.cPoints.clear()
                                        arrays_and_variables.cPoints.append(newPoint)

                                        self.statsWindow_CSpinBox.lineEdit().setText(str(arrays_and_variables.cPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusCSpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_CSpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.cPoints[0] != 1:

                                newPoint = arrays_and_variables.cPoints[0] - 1

                                arrays_and_variables.cPoints.clear()
                                arrays_and_variables.cPoints.append(newPoint)

                                self.statsWindow_CSpinBox.lineEdit().setText(str(arrays_and_variables.cPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addISpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_ISpinBox.lineEdit().text() != 0 and self.statsWindow_ISpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.iPoints[0] != 0 and arrays_and_variables.iPoints[0] != 10:
                                        newPoint = arrays_and_variables.iPoints[0] + 1

                                        arrays_and_variables.iPoints.clear()
                                        arrays_and_variables.iPoints.append(newPoint)

                                        self.statsWindow_ISpinBox.lineEdit().setText(str(arrays_and_variables.iPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusISpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_ISpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.iPoints[0] != 1:

                                newPoint = arrays_and_variables.iPoints[0] - 1

                                arrays_and_variables.iPoints.clear()
                                arrays_and_variables.iPoints.append(newPoint)

                                self.statsWindow_ISpinBox.lineEdit().setText(str(arrays_and_variables.iPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addASpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_ASpinBox.lineEdit().text() != 0 and self.statsWindow_ASpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.aPoints[0] != 0 and arrays_and_variables.aPoints[0] != 10:
                                        newPoint = arrays_and_variables.aPoints[0] + 1

                                        arrays_and_variables.aPoints.clear()
                                        arrays_and_variables.aPoints.append(newPoint)

                                        self.statsWindow_ASpinBox.lineEdit().setText(str(arrays_and_variables.aPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusASpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_ASpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.aPoints[0] != 1:

                                newPoint = arrays_and_variables.aPoints[0] - 1

                                arrays_and_variables.aPoints.clear()
                                arrays_and_variables.aPoints.append(newPoint)

                                self.statsWindow_ASpinBox.lineEdit().setText(str(arrays_and_variables.aPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def addLSpinBoxValue():

                if self.statsWindow_CurrentSkillPointsLabel.text() != "0":

                        # Making sure that value doesnt go below 1 or above 10
                        if self.statsWindow_LSpinBox.lineEdit().text() != 0 and self.statsWindow_LSpinBox.lineEdit().text() != 11:


                                # Making sure that value doesnt go below 1 or above 10
                                if arrays_and_variables.lPoints[0] != 0 and arrays_and_variables.lPoints[0] != 10:
                                        newPoint = arrays_and_variables.lPoints[0] + 1

                                        arrays_and_variables.lPoints.clear()
                                        arrays_and_variables.lPoints.append(newPoint)

                                        self.statsWindow_LSpinBox.lineEdit().setText(str(arrays_and_variables.lPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))
        def minusLSpinBoxValue():

                # Making sure that the value isnt below 1
                if self.statsWindow_LSpinBox.lineEdit().text() != 1:

                        # Making sure that the value isnt below 1
                        if arrays_and_variables.lPoints[0] != 1:

                                newPoint = arrays_and_variables.lPoints[0] - 1

                                arrays_and_variables.lPoints.clear()
                                arrays_and_variables.lPoints.append(newPoint)

                                self.statsWindow_LSpinBox.lineEdit().setText(str(arrays_and_variables.lPoints[0]))



                # Calculating and returning the remaining points
                remainingSkillPoints = functions.getRemainingSkillPoints()
                self.statsWindow_CurrentSkillPointsLabel.setText(str(remainingSkillPoints))




        StatsWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        StatsWindow.setObjectName("StatsWindow")
        StatsWindow.resize(800, 1200)
        StatsWindow.setMinimumSize(QtCore.QSize(800, 1200))
        StatsWindow.setMaximumSize(QtCore.QSize(800, 1200))
        self.centralwidget = QtWidgets.QWidget(StatsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statsWindow_TerminalBGFrame = QtWidgets.QFrame(self.centralwidget)
        self.statsWindow_TerminalBGFrame.setStyleSheet("border-image: url(:/newPrefix/imgs/terminal-bg.png);")
        self.statsWindow_TerminalBGFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statsWindow_TerminalBGFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statsWindow_TerminalBGFrame.setObjectName("statsWindow_TerminalBGFrame")
        self.statsWindow_MainHeadingLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_MainHeadingLabel.setGeometry(QtCore.QRect(10, 120, 781, 91))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_MainHeadingLabel.setFont(font)
        self.statsWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    border-image: none;\n"
"}")
        self.statsWindow_MainHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_MainHeadingLabel.setObjectName("statsWindow_MainHeadingLabel")
        self.statsWindow_Text2Label = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_Text2Label.setGeometry(QtCore.QRect(110, 260, 581, 91))
        self.statsWindow_Text2Label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(10)
        self.statsWindow_Text2Label.setFont(font)
        self.statsWindow_Text2Label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    border-image: none;\n"
"}")
        self.statsWindow_Text2Label.setTextFormat(QtCore.Qt.AutoText)
        self.statsWindow_Text2Label.setScaledContents(False)
        self.statsWindow_Text2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_Text2Label.setWordWrap(True)
        self.statsWindow_Text2Label.setObjectName("statsWindow_Text2Label")
        self.statsWindow_Text1Label = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_Text1Label.setGeometry(QtCore.QRect(110, 201, 581, 81))
        self.statsWindow_Text1Label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(10)
        self.statsWindow_Text1Label.setFont(font)
        self.statsWindow_Text1Label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    border-image: none;\n"
"}")
        self.statsWindow_Text1Label.setTextFormat(QtCore.Qt.AutoText)
        self.statsWindow_Text1Label.setScaledContents(False)
        self.statsWindow_Text1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_Text1Label.setWordWrap(True)
        self.statsWindow_Text1Label.setObjectName("statsWindow_Text1Label")
        self.statsWindow_PerksBtn = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_PerksBtn.clicked.connect(enterPerksWindow)
        self.statsWindow_PerksBtn.setGeometry(QtCore.QRect(140, 20, 100, 50))
        self.statsWindow_PerksBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.statsWindow_PerksBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(14)
        self.statsWindow_PerksBtn.setFont(font)
        self.statsWindow_PerksBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_PerksBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_PerksBtn.setObjectName("statsWindow_PerksBtn")
        self.statsWindow_StartBtn = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_StartBtn.setGeometry(QtCore.QRect(23, 20, 100, 50))
        self.statsWindow_StartBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.statsWindow_StartBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(14)
        self.statsWindow_StartBtn.setFont(font)
        self.statsWindow_StartBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_StartBtn.clicked.connect(enterStartWindow)
        self.statsWindow_StartBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_StartBtn.setObjectName("statsWindow_StartBtn")
        self.statsWindow_SkillPointsRemainingLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_SkillPointsRemainingLabel.setGeometry(QtCore.QRect(6, 370, 791, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(14)
        self.statsWindow_SkillPointsRemainingLabel.setFont(font)
        self.statsWindow_SkillPointsRemainingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_SkillPointsRemainingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_SkillPointsRemainingLabel.setObjectName("statsWindow_SkillPointsRemainingLabel")
        self.statsWindow_CurrentSkillPointsLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_CurrentSkillPointsLabel.setGeometry(QtCore.QRect(6, 410, 791, 61))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(20)
        self.statsWindow_CurrentSkillPointsLabel.setFont(font)
        self.statsWindow_CurrentSkillPointsLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_CurrentSkillPointsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_CurrentSkillPointsLabel.setObjectName("statsWindow_CurrentSkillPointsLabel")
        self.statsWindow_SLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_SLabel.setGeometry(QtCore.QRect(10, 540, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_SLabel.setFont(font)
        self.statsWindow_SLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_SLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_SLabel.setObjectName("statsWindow_SLabel")
        self.statsWindow_PLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_PLabel.setGeometry(QtCore.QRect(10, 610, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_PLabel.setFont(font)
        self.statsWindow_PLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_PLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_PLabel.setObjectName("statsWindow_PLabel")
        self.statsWindow_SSpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_SSpinBox.setGeometry(QtCore.QRect(260, 541, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_SSpinBox.setFont(font)
        self.statsWindow_SSpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_SSpinBox.setReadOnly(False)
        self.statsWindow_SSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_SSpinBox.setKeyboardTracking(False)
        self.statsWindow_SSpinBox.setDisabled(True)
        self.statsWindow_SSpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_SSpinBox.setMinimum(1)
        self.statsWindow_SSpinBox.setMaximum(10)
        self.statsWindow_SSpinBox.setObjectName("statsWindow_SSpinBox")
        self.statsWindow_PSpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_PSpinBox.setGeometry(QtCore.QRect(260, 610, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_PSpinBox.setFont(font)
        self.statsWindow_PSpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_PSpinBox.setReadOnly(False)
        self.statsWindow_PSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_PSpinBox.setKeyboardTracking(False)
        self.statsWindow_PSpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_PSpinBox.setDisabled(True)
        self.statsWindow_PSpinBox.setMinimum(1)
        self.statsWindow_PSpinBox.setMaximum(10)
        self.statsWindow_PSpinBox.setObjectName("statsWindow_PSpinBox")
        self.statsWindow_ESpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ESpinBox.setGeometry(QtCore.QRect(260, 680, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_ESpinBox.setFont(font)
        self.statsWindow_ESpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_ESpinBox.setReadOnly(False)
        self.statsWindow_ESpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_ESpinBox.setKeyboardTracking(False)
        self.statsWindow_ESpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_ESpinBox.setDisabled(True)
        self.statsWindow_ESpinBox.setMinimum(1)
        self.statsWindow_ESpinBox.setMaximum(10)
        self.statsWindow_ESpinBox.setObjectName("statsWindow_ESpinBox")
        self.statsWindow_ELabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ELabel.setGeometry(QtCore.QRect(10, 680, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_ELabel.setFont(font)
        self.statsWindow_ELabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_ELabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_ELabel.setObjectName("statsWindow_ELabel")
        self.statsWindow_CLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_CLabel.setGeometry(QtCore.QRect(10, 750, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_CLabel.setFont(font)
        self.statsWindow_CLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_CLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_CLabel.setObjectName("statsWindow_CLabel")
        self.statsWindow_CSpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_CSpinBox.setGeometry(QtCore.QRect(260, 750, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_CSpinBox.setFont(font)
        self.statsWindow_CSpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_CSpinBox.setReadOnly(False)
        self.statsWindow_CSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_CSpinBox.setKeyboardTracking(False)
        self.statsWindow_CSpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_CSpinBox.setDisabled(True)
        self.statsWindow_CSpinBox.setMinimum(1)
        self.statsWindow_CSpinBox.setMaximum(10)
        self.statsWindow_CSpinBox.setObjectName("statsWindow_CSpinBox")
        self.statsWindow_ILabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ILabel.setGeometry(QtCore.QRect(10, 820, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_ILabel.setFont(font)
        self.statsWindow_ILabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_ILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_ILabel.setObjectName("statsWindow_ILabel")
        self.statsWindow_ISpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ISpinBox.setGeometry(QtCore.QRect(260, 820, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_ISpinBox.setFont(font)
        self.statsWindow_ISpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_ISpinBox.setReadOnly(False)
        self.statsWindow_ISpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_ISpinBox.setKeyboardTracking(False)
        self.statsWindow_ISpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_ISpinBox.setDisabled(True)
        self.statsWindow_ISpinBox.setMinimum(1)
        self.statsWindow_ISpinBox.setMaximum(10)
        self.statsWindow_ISpinBox.setObjectName("statsWindow_ISpinBox")
        self.statsWindow_ALabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ALabel.setGeometry(QtCore.QRect(10, 890, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_ALabel.setFont(font)
        self.statsWindow_ALabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_ALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_ALabel.setObjectName("statsWindow_ALabel")
        self.statsWindow_ASpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_ASpinBox.setGeometry(QtCore.QRect(260, 890, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_ASpinBox.setFont(font)
        self.statsWindow_ASpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_ASpinBox.setReadOnly(False)
        self.statsWindow_ASpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_ASpinBox.setKeyboardTracking(False)
        self.statsWindow_ASpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_ASpinBox.setDisabled(True)
        self.statsWindow_ASpinBox.setMinimum(1)
        self.statsWindow_ASpinBox.setMaximum(10)
        self.statsWindow_ASpinBox.setObjectName("statsWindow_ASpinBox")
        self.statsWindow_LLabel = QtWidgets.QLabel(self.statsWindow_TerminalBGFrame)
        self.statsWindow_LLabel.setGeometry(QtCore.QRect(10, 960, 251, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(24)
        self.statsWindow_LLabel.setFont(font)
        self.statsWindow_LLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.statsWindow_LLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWindow_LLabel.setObjectName("statsWindow_LLabel")
        self.statsWindow_LSpinBox = QtWidgets.QSpinBox(self.statsWindow_TerminalBGFrame)
        self.statsWindow_LSpinBox.setGeometry(QtCore.QRect(260, 960, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(-1)
        self.statsWindow_LSpinBox.setFont(font)
        self.statsWindow_LSpinBox.setStyleSheet("QSpinBox {\n"
"    border-image: none;\n"
"    background-color: rgb(0, 58, 0);\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 30px;\n"
"    text-align: right;\n"
"    color: white;\n"
"}")
        self.statsWindow_LSpinBox.setReadOnly(False)
        self.statsWindow_LSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.statsWindow_LSpinBox.setKeyboardTracking(False)
        self.statsWindow_LSpinBox.lineEdit().setReadOnly(True)
        self.statsWindow_LSpinBox.setDisabled(True)
        self.statsWindow_LSpinBox.setMinimum(1)
        self.statsWindow_LSpinBox.setMaximum(10)
        self.statsWindow_LSpinBox.setObjectName("statsWindow_LSpinBox")
        self.statsWindow_SPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_SPlus.setGeometry(QtCore.QRect(600, 550, 35, 35))
        self.statsWindow_SPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_SPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_SPlus.setFont(font)
        self.statsWindow_SPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_SPlus.clicked.connect(addSSpinBoxValue)
        self.statsWindow_SPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_SPlus.setObjectName("statsWindow_SPlus")
        self.statsWindow_SMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_SMinus.setGeometry(QtCore.QRect(650, 550, 35, 35))
        self.statsWindow_SMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_SMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_SMinus.setFont(font)
        self.statsWindow_SMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_SMinus.clicked.connect(minusSSpinBoxValue)
        self.statsWindow_SMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_SMinus.setObjectName("statsWindow_SMinus")
        self.statsWindow_PMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_PMinus.setGeometry(QtCore.QRect(650, 620, 35, 35))
        self.statsWindow_PMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_PMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_PMinus.setFont(font)
        self.statsWindow_PMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_PMinus.clicked.connect(minusPSpinBoxValue)
        self.statsWindow_PMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_PMinus.setObjectName("statsWindow_PMinus")
        self.statsWindow_PPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_PPlus.setGeometry(QtCore.QRect(600, 620, 35, 35))
        self.statsWindow_PPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_PPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_PPlus.setFont(font)
        self.statsWindow_PPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_PPlus.clicked.connect(addPSpinBoxValue)
        self.statsWindow_PPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_PPlus.setObjectName("statsWindow_PPlus")
        self.statsWindow_EMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_EMinus.setGeometry(QtCore.QRect(650, 690, 35, 35))
        self.statsWindow_EMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_EMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_EMinus.setFont(font)
        self.statsWindow_EMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_EMinus.clicked.connect(minusESpinBoxValue)
        self.statsWindow_EMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_EMinus.setObjectName("statsWindow_EMinus")
        self.statsWindow_EPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_EPlus.setGeometry(QtCore.QRect(600, 690, 35, 35))
        self.statsWindow_EPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_EPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_EPlus.setFont(font)
        self.statsWindow_EPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_EPlus.clicked.connect(addESpinBoxValue)
        self.statsWindow_EPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_EPlus.setObjectName("statsWindow_EPlus")
        self.statsWindow_CMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_CMinus.setGeometry(QtCore.QRect(650, 760, 35, 35))
        self.statsWindow_CMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_CMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_CMinus.setFont(font)
        self.statsWindow_CMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_CMinus.clicked.connect(minusCSpinBoxValue)
        self.statsWindow_CMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_CMinus.setObjectName("statsWindow_CMinus")
        self.statsWindow_CPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_CPlus.setGeometry(QtCore.QRect(600, 760, 35, 35))
        self.statsWindow_CPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_CPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_CPlus.setFont(font)
        self.statsWindow_CPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_CPlus.clicked.connect(addCSpinBoxValue)
        self.statsWindow_CPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_CPlus.setObjectName("statsWindow_CPlus")
        self.statsWindow_IMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_IMinus.setGeometry(QtCore.QRect(650, 830, 35, 35))
        self.statsWindow_IMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_IMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_IMinus.setFont(font)
        self.statsWindow_IMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_IMinus.clicked.connect(minusISpinBoxValue)
        self.statsWindow_IMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_IMinus.setObjectName("statsWindow_IMinus")
        self.statsWindow_IPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_IPlus.setGeometry(QtCore.QRect(600, 830, 35, 35))
        self.statsWindow_IPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_IPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_IPlus.setFont(font)
        self.statsWindow_IPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_IPlus.clicked.connect(addISpinBoxValue)
        self.statsWindow_IPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_IPlus.setObjectName("statsWindow_IPlus")
        self.statsWindow_AMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_AMinus.setGeometry(QtCore.QRect(650, 900, 35, 35))
        self.statsWindow_AMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_AMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_AMinus.setFont(font)
        self.statsWindow_AMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_AMinus.clicked.connect(minusASpinBoxValue)
        self.statsWindow_AMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_AMinus.setObjectName("statsWindow_AMinus")
        self.statsWindow_APlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_APlus.setGeometry(QtCore.QRect(600, 900, 35, 35))
        self.statsWindow_APlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_APlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_APlus.setFont(font)
        self.statsWindow_APlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_APlus.clicked.connect(addASpinBoxValue)
        self.statsWindow_APlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_APlus.setObjectName("statsWindow_APlus")
        self.statsWindow_LMinus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_LMinus.setGeometry(QtCore.QRect(650, 970, 35, 35))
        self.statsWindow_LMinus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_LMinus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_LMinus.setFont(font)
        self.statsWindow_LMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_LMinus.clicked.connect(minusLSpinBoxValue)
        self.statsWindow_LMinus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_LMinus.setObjectName("statsWindow_LMinus")
        self.statsWindow_LPlus = QtWidgets.QPushButton(self.statsWindow_TerminalBGFrame)
        self.statsWindow_LPlus.setGeometry(QtCore.QRect(600, 970, 35, 35))
        self.statsWindow_LPlus.setMinimumSize(QtCore.QSize(35, 35))
        self.statsWindow_LPlus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("OCR-A BT")
        font.setPointSize(16)
        self.statsWindow_LPlus.setFont(font)
        self.statsWindow_LPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statsWindow_LPlus.clicked.connect(addLSpinBoxValue)
        self.statsWindow_LPlus.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.statsWindow_LPlus.setObjectName("statsWindow_LPlus")
        self.verticalLayout.addWidget(self.statsWindow_TerminalBGFrame)
        StatsWindow.setCentralWidget(self.centralwidget)

        # This prevent the value of the spinboxes from resetting
        self.statsWindow_SSpinBox.setValue(arrays_and_variables.sPoints[0])
        self.statsWindow_PSpinBox.setValue(arrays_and_variables.pPoints[0])
        self.statsWindow_ESpinBox.setValue(arrays_and_variables.ePoints[0])
        self.statsWindow_CSpinBox.setValue(arrays_and_variables.cPoints[0])
        self.statsWindow_ISpinBox.setValue(arrays_and_variables.iPoints[0])
        self.statsWindow_ASpinBox.setValue(arrays_and_variables.aPoints[0])
        self.statsWindow_LSpinBox.setValue(arrays_and_variables.lPoints[0])


        self.retranslateUi(StatsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatsWindow)

    def retranslateUi(self, StatsWindow):

        remainingSkillPoints = functions.getRemainingSkillPoints()

        _translate = QtCore.QCoreApplication.translate
        StatsWindow.setWindowTitle(_translate("StatsWindow", "YouAreSpecialUI - Stats Window"))
        self.statsWindow_MainHeadingLabel.setText(_translate("StatsWindow", "Stats Window"))
        self.statsWindow_Text2Label.setText(_translate("StatsWindow", "Once you have used all of your skill points, you can proceed to the Perks window to check what kind of perks you are allowed to use based on its respected attribute skill points total."))
        self.statsWindow_Text1Label.setText(_translate("StatsWindow", "This is the Stats window. Here you will input your 21 skill points into each of the follow 7 attributes: Strength, Perception, Endurance, Charisma, Intelligence, Agility and Luck."))
        self.statsWindow_PerksBtn.setText(_translate("StatsWindow", "PERKS"))
        self.statsWindow_StartBtn.setText(_translate("StatsWindow", "START"))
        self.statsWindow_SkillPointsRemainingLabel.setText(_translate("StatsWindow", "Skill Points Remaining"))
        self.statsWindow_CurrentSkillPointsLabel.setText(_translate("StatsWindow", str(remainingSkillPoints))) # Adding the current remaining points. This is to keep up with the current amount
        self.statsWindow_SLabel.setText(_translate("StatsWindow", "S"))
        self.statsWindow_PLabel.setText(_translate("StatsWindow", "P"))
        self.statsWindow_ELabel.setText(_translate("StatsWindow", "E"))
        self.statsWindow_CLabel.setText(_translate("StatsWindow", "C"))
        self.statsWindow_ILabel.setText(_translate("StatsWindow", "I"))
        self.statsWindow_ALabel.setText(_translate("StatsWindow", "A"))
        self.statsWindow_LLabel.setText(_translate("StatsWindow", "L"))
        self.statsWindow_SPlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_SMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_PMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_PPlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_EMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_EPlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_CMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_CPlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_IMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_IPlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_AMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_APlus.setText(_translate("StatsWindow", "+"))
        self.statsWindow_LMinus.setText(_translate("StatsWindow", "-"))
        self.statsWindow_LPlus.setText(_translate("StatsWindow", "+"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsWindow = QtWidgets.QMainWindow()
    ui = Ui_StatsWindow()
    ui.setupUi(StatsWindow)
    print("RUN StartWindow.py to start the program!")
    sys.exit()
