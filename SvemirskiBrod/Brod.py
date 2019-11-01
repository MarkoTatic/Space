from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys, random



class Brod(QMainWindow):

    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        self.mover = Mover(centralWidget)
        self.mover.setFocus()
        self.initUI()

    def initUI(self):
        """initiates application UI"""
       # self.InitSpaceS(170, 140)
        self.resize(400, 400)
        self.center()
        self.setWindowTitle('Svemirski brod')

        self.show()



    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def InitSpaceS(self, val, val2):
        label = QLabel(self)
        pixmap = QPixmap('rocketship.png')
        label.setPixmap(pixmap)
        label.setGeometry(val, val2, 100, 100)


class Mover(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(170, 140, 100, 100)
        self.setPixmap(QtGui.QPixmap('rocketship.png'))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.move(self.x(), self.y() - 5)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(self.x(), self.y() + 5)
        elif event.key() == QtCore.Qt.Key_Left:
            self.move(self.x() - 5, self.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(self.x() + 5, self.y())
        else:
            QtWidgets.QLabel.keyPressEvent(self, event)


if __name__ == '__main__':
    app = QApplication([])
    brod = Brod()
    sys.exit(app.exec_())