from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 538)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 541, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.timeLcdNumber.setMinimumSize(QtCore.QSize(0, 40))
        self.timeLcdNumber.setMaximumSize(QtCore.QSize(197, 16777215))
        self.timeLcdNumber.setObjectName("timeLcdNumber")
        self.horizontalLayout.addWidget(self.timeLcdNumber, 0, QtCore.Qt.AlignLeft)
        self.bestTime = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.bestTime.setObjectName("bestTime")
        self.bestTime.setText("Лучшее время:")
        self.horizontalLayout.addWidget(self.bestTime, 0, QtCore.Qt.AlignLeft)
        self.newGamePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.newGamePushButton.setObjectName("newGamePushButton")
        self.horizontalLayout.addWidget(self.newGamePushButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.InfoPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.InfoPushButton.setObjectName("InfoPushButton")
        self.horizontalLayout.addWidget(self.InfoPushButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gameFieldTableView = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        # self.gameFieldTableView.setStyleSheet("QTableView { gridline-color: black; }")
        self.gameFieldTableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameFieldTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.gameFieldTableView.setObjectName("gameFieldTableView")
        self.gameFieldTableView.horizontalHeader().setVisible(False)
        self.gameFieldTableView.horizontalHeader().setDefaultSectionSize(80)
        self.gameFieldTableView.verticalHeader().setVisible(False)
        self.gameFieldTableView.verticalHeader().setDefaultSectionSize(80)
        self.verticalLayout_2.addWidget(self.gameFieldTableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu = self.menubar.addMenu("&amp; menu")
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_1.triggered.connect(self.whiteTheme)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.blackTheme)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.exit)
        self.menu.addAction(self.action_1)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.editMenu = QtWidgets.QMenu(self.menubar)
        self.editMenu = self.menubar.addMenu("&amp; Edit")
        self.state_1 = QtWidgets.QAction(MainWindow)
        self.state_1.setObjectName("state_1")
        self.state_2 = QtWidgets.QAction(MainWindow)
        self.state_2.setObjectName("state_2")
        self.state_3 = QtWidgets.QAction(MainWindow)
        self.state_3.setObjectName("state_3")
        self.state_4 = QtWidgets.QAction(MainWindow)
        self.state_4.setObjectName("state_4")
        self.state_5 = QtWidgets.QAction(MainWindow)
        self.state_5.setObjectName("state_5")
        self.editMenu.addAction(self.state_1)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.state_2)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.state_3)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.state_4)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.state_5)
        self.menubar.addAction(self.editMenu.menuAction())
        self.rangeMenu = QtWidgets.QMenu(self.menubar)
        self.rangeMenu = self.menubar.addMenu("&amp; Range")
        self.range_1 = QtWidgets.QAction(MainWindow)
        self.range_1.setObjectName("range_1")
        self.range_2 = QtWidgets.QAction(MainWindow)
        self.range_2.setObjectName("range_2")
        self.rangeMenu.addAction(self.range_1)
        self.rangeMenu.addSeparator()
        self.rangeMenu.addAction(self.range_2)
        self.menubar.addAction(self.rangeMenu.menuAction())
        self.whiteTheme()

        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(MainWindow):
        MainWindow.close()

    def blackTheme(MainWindow):
        MainWindow.centralwidget.setStyleSheet("color: #282828;background-color: #282828;")
        MainWindow.newGamePushButton.setStyleSheet("color: #b1b1b1;background-color: QLinearGradient( x1: 0, y1: 0, "
                                                   "x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, "
                                                   "stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, "
                                                   "stop: 1 #464646);border-width: 1px;border-color: "
                                                   "#1e1e1e;border-style: solid;border-radius: 6;padding: "
                                                   "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")
        MainWindow.InfoPushButton.setStyleSheet("color: #b1b1b1;background-color: QLinearGradient( x1: 0, y1: 0, "
                                                "x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, "
                                                "stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, "
                                                "stop: 1 #464646);border-width: 1px;border-color: "
                                                "#1e1e1e;border-style: solid;border-radius: 6;padding: "
                                                "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")

    def whiteTheme(MainWindow):
        MainWindow.centralwidget.setStyleSheet("background: #FFF8DC;")
        MainWindow.newGamePushButton.setStyleSheet("color: black;background-color: QLinearGradient( x1: 0, y1: 0, "
                                                   "x2: 0, y2: 1, stop: 0 white, stop: 0.1 white, "
                                                   "stop: 0.5 white, stop: 0.9 white, "
                                                   "stop: 1 white);border-width: 1px;border-color: "
                                                   "#BC8F8F;border-style: solid;border-radius: 6;padding: "
                                                   "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")
        MainWindow.InfoPushButton.setStyleSheet("color: black;background-color: QLinearGradient( x1: 0, y1: 0, "
                                                "x2: 0, y2: 1, stop: 0 white, stop: 0.1 white, "
                                                "stop: 0.5 white, stop: 0.9 white, "
                                                "stop: 1 white);border-width: 1px;border-color: "
                                                "#BC8F8F;border-style: solid;border-radius: 6;padding: "
                                                "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кубик Рубика"))
        self.newGamePushButton.setText(_translate("MainWindow", "Новая Игра"))
        self.InfoPushButton.setText(_translate("MainWindow", "Информация об игре"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_1.setText(_translate("MainWindow", "&Светлая тема"))
        self.action_2.setText(_translate("MainWindow", "&Темная тема"))
        self.action_3.setText(_translate("MainWindow", "&Выход"))
        self.editMenu.setTitle(_translate("MainWindow", "&Настройка цвета"))
        self.state_1.setText(_translate("MainWindow", "&Синий+красный"))
        self.state_2.setText(_translate("MainWindow", "&Зеленый+желтый"))
        self.state_3.setText(_translate("MainWindow", "&Салатовый+фиолетовый"))
        self.state_4.setText(_translate("MainWindow", "&Бирюзовый+темно-синий"))
        self.state_5.setText(_translate("MainWindow", "&Случайное сочетание"))
        self.rangeMenu.setTitle(_translate("MainWindow", "&Настройка размера кубика"))
        self.range_1.setText(_translate("MainWindow", "3*3"))
        self.range_2.setText(_translate("MainWindow", "5*5"))


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.setStyleSheet("background: #DDA0DD; color: black")
        self.setFixedSize(550, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info2 = QtWidgets.QLabel(self)
        self.info2.setObjectName("Info2")
        self.info2.setGeometry(QtCore.QRect(10, 0, 500, 100))
        self.info2.setText("Игра была разработана студенткой 2 курса ФКН Лариной Марией.\nЦель игры - сложить все "
                           "квадратики одного цвета на одной стороне. Удачи!")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.pushButton.setStyleSheet("color: black;background-color: QLinearGradient( x1: 0, y1: 0, "
                                      "x2: 0, y2: 1, stop: 0 white, stop: 0.1 white, "
                                      "stop: 0.5 white, stop: 0.9 white, "
                                      "stop: 1 white);border-width: 1px;border-color: "
                                      "#BC8F8F;border-style: solid;border-radius: 6;padding: "
                                      "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Information")
        self.pushButton.setText("Понятно")

    def btnClosed(self):
        self.close()


class WinStatus(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WinStatus, self).__init__(parent)

        self.setStyleSheet("background: #DDA0DD;")
        self.setFixedSize(350, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(self)
        self.text.setObjectName("Info")
        self.text.setGeometry(QtCore.QRect(10, 0, 350, 100))
        self.text.setText("Вы выиграли!!! Поздравляю!!!")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closeB)
        self.pushButton.setStyleSheet("color: black;background-color: QLinearGradient( x1: 0, y1: 0, "
                                      "x2: 0, y2: 1, stop: 0 white, stop: 0.1 white, "
                                      "stop: 0.5 white, stop: 0.9 white, "
                                      "stop: 1 white);border-width: 1px;border-color: "
                                      "#BC8F8F;border-style: solid;border-radius: 6;padding: "
                                      "3px;font-size: 15px;padding-left: 5px;padding-right: 5px;")
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Победа")
        self.pushButton.setText("Спасибо")

    def closeB(self):
        self.close()
