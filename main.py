from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QPainter
import math
import sys


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('turning a point.ui', self)
        self.pushButton.clicked.connect(self.click)
        self.start = False

        self.pixmap = QPixmap('krug.jpg').scaled(301, 301)
        self.label.setPixmap(self.pixmap)
        self.poworot = 360

    def paintEvent(self, event):
        if self.start:
            self.label.clear()
            self.pixmap = QPixmap('krug.jpg').scaled(301, 301)
            painter = QPainter(self.pixmap)
            painter.setPen(QtCore.Qt.red)
            painter.drawLine(150, 150, abs(int(math.cos(math.radians(self.poworot)) * 135 + 150)),
                             abs(int(math.sin(math.radians(self.poworot)) * 135 - 150)))
            self.label.setPixmap(self.pixmap)
            painter.end()
        self.start = False

    def click(self):
        try:
            self.lineEdit.setStyleSheet("color: black;")
            self.poworot = int(eval(self.lineEdit.text()))
            if len(str(self.poworot)) > 100 * 100:
                print('124')
                raise OverflowError
            self.lineEdit.setText(str(self.poworot))
            self.start = True
            if self.comboBox.currentIndex() == 1:
                self.poworot = math.degrees(self.poworot)
            self.label_2.setText(f'sin: {str(round(math.sin(math.radians(self.poworot)), 3))}')
            self.label_3.setText(f'cos: {str(round(math.cos(math.radians(self.poworot)), 3))}')
            if round(math.sin(math.radians(self.poworot)), 3) == 0.0:
                self.label_4.setText(
                    f'tg: {str(round(math.sin(math.radians(self.poworot)) / math.cos(math.radians(self.poworot)), 3))}')
                self.label_5.setText('ctg: -')
            elif round(math.cos(math.radians(self.poworot)), 3) == 0.0:
                self.label_5.setText(
                    f'ctg: {str(round(math.cos(math.radians(self.poworot)) / math.sin(math.radians(self.poworot)), 3))}')
                self.label_4.setText('tg: -')
            else:
                self.label_4.setText(
                    f'tg: {str(round(math.sin(math.radians(self.poworot)) / math.cos(math.radians(self.poworot)), 3))}')
                self.label_5.setText(
                    f'ctg: {str(round(math.cos(math.radians(self.poworot)) / math.sin(math.radians(self.poworot)), 3))}')
            self.label_6.setText(
                f'coords: ({str(round(math.cos(math.radians(self.poworot)), 3))}; \
{str(round(math.sin(math.radians(self.poworot)), 3))})')
            self.update()
        except SyntaxError:
            self.lineEdit.setStyleSheet("color: red;")
            self.lineEdit.setText('Неправильный ввод')
        except NameError:
            self.lineEdit.setStyleSheet("color: red;")
            self.lineEdit.setText('Неправильный ввод')
        except OverflowError:
            self.lineEdit.setStyleSheet("color: red;")
            self.poworot = 0
            self.lineEdit.setText('Слишком большое значение')
        except ValueError:
            self.lineEdit.setStyleSheet("color: red;")
            self.lineEdit.setText('Неправильный ввод')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = DBSample()
    ex.show()

    sys.exit(app.exec_())
