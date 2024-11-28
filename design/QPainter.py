from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.red)
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawRect(50, 50, 100, 100)  # Kırmızı bir dikdörtgen çiz

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.show()
app.exec_()
