from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)  # Kenar siyah
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))  # Dolgu kırmızı
        painter.drawRect(50, 50, 100, 100)  # Kırmızı dolgulu dikdörtgen

        painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))  # Çapraz desen
        painter.drawEllipse(200, 50, 100, 100)  # Mavi dolgulu daire

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.show()
app.exec_()
