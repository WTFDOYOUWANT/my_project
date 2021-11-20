import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        if self.do_paint:
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        size = randint(0, 200)
        qp.drawEllipse(50, 70, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
