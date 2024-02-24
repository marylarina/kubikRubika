import os
import random

from KubikRubikaGame import *
from MainWindowUI import Ui_MainWindow as MainWindowUI, ClssDialog, WinStatus

from PyQt5 import QtSvg, QtCore
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt, QTimer


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.index = 1
        self.row_count = 3
        self.k = 'b1'
        self.t = 'r1'

        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        self._images = {
            os.path.splitext(f)[0]: QtSvg.QSvgRenderer(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }

        self._game = KubikRubikaGame(self.row_count, self.row_count, self.index)
        self.game_resize(self._game)
        if self._game.state == GameState.WIN:
            win = WinStatus(self)
            win.exec_()

        self.bestScore = 1234567890
        self.time = 0
        self.time2 = self.time

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeCheck)
        self.timer.setInterval(100)
        self.on_new_game()

        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                painter.restore()

        self.gameFieldTableView.setItemDelegate(MyDelegate(self))

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.gameFieldTableView.indexAt(e.pos())
            self.on_item_clicked(idx, e)

        self.gameFieldTableView.mousePressEvent = new_mouse_press_event
        self.newGamePushButton.clicked.connect(self.on_new_game)
        self.InfoPushButton.clicked.connect(self.openDialog)
        self.state_1.triggered.connect(self.redBlue)
        self.state_2.triggered.connect(self.yelGreen)
        self.state_3.triggered.connect(self.lgPurp)
        self.state_4.triggered.connect(self.dbCyan)
        self.state_5.triggered.connect(self.rand)
        self.range_1.triggered.connect(self.three)
        self.range_2.triggered.connect(self.five)

    def openDialog(self):
        dialog = ClssDialog(self)
        dialog.exec_()

    def timeCheck(self):
        self.time2 += 0.1
        self.timeLcdNumber.display(self.time2)

    def winStatus(self):
        win = WinStatus(self)
        win.exec_()

    def game_resize(self, game: KubikRubikaGame) -> None:
        model = QStandardItemModel(game.row_count, game.col_count)
        self.gameFieldTableView.setModel(model)
        self.update_view()

    def update_view(self):
        self.gameFieldTableView.viewport().update()

    def on_new_game(self):
        self._game = KubikRubikaGame(self.row_count, self.row_count, self.index)
        self.game_resize(self._game)
        self.update_view()
        self.time2 = self.time
        self.timer.start()

    def three(self):
        self.row_count = 3
        self.on_new_game()

    def five(self):
        self.row_count = 5
        self.on_new_game()

    def redBlue(self):
        self.index = 1
        self.on_new_game()

    def yelGreen(self):
        self.index = 2
        self.on_new_game()

    def lgPurp(self):
        self.index = 3
        self.on_new_game()

    def dbCyan(self):
        self.index = 4
        self.on_new_game()

    def rand(self):
        self.index = 5
        listImg = ['b1', 'c1', 'db', 'g1', 'lg', 'p1', 'r1', 'y1']
        self.k = random.choice(listImg)
        self.t = random.choice(listImg)
        while self.k == self.t:
            self.t = random.choice(listImg)
        self.on_new_game()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        item = self._game[e.row(), e.column()]
        if self.index == 1:
            if item.color == Color.FIRST:
                img = self._images['b1']
            elif item.color == Color.SECOND:
                img = self._images['r1']
            else:
                img = self._images['r1']
            self.update_view()
        elif self.index == 2:
            if item.color == Color.FIRST:
                img = self._images['g1']
            elif item.color == Color.SECOND:
                img = self._images['y1']
            else:
                img = self._images['y1']
            self.update_view()
        elif self.index == 3:
            if item.color == Color.FIRST:
                img = self._images['lg']
            elif item.color == Color.SECOND:
                img = self._images['p1']
            else:
                img = self._images['p1']
            self.update_view()
        elif self.index == 4:
            if item.color == Color.FIRST:
                img = self._images['db']
            elif item.color == Color.SECOND:
                img = self._images['c1']
            else:
                img = self._images['c1']
            self.update_view()
        elif self.index == 5:
            if item.color == Color.FIRST:
                img = self._images[self.k]
            elif item.color == Color.SECOND:
                img = self._images[self.t]
            else:
                img = self._images[self.k]
        else:
            if item.color == Color.FIRST:
                img = self._images['b1']
            elif item.color == Color.SECOND:
                img = self._images['r1']
            else:
                img = self._images['r1']
        img.render(painter, QRectF(option.rect))

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self._game.left_mouse_click(e.row(), e.column(), self.row_count)
            if self._game.state == GameState.WIN:
                self.timer.stop()
                score = self.time2
                if score < self.bestScore:
                    self.bestTime.setText("Лучшее время: " + str(score))
                self.winStatus()
                self.on_new_game()
        elif me.button() == Qt.RightButton:
            self._game.right_mouse_click(e.row(), e.column(), self.row_count)
            if self._game.state == GameState.WIN:
                self.timer.stop()
                score = self.time2
                if score < self.bestScore:
                    self.bestTime.setText("Лучшее время: " + str(score))
                self.winStatus()
                self.on_new_game()
        self.update_view()
