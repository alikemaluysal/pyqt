from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Antialiasing etkin
        pen = QPen(Qt.darkGreen)
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawEllipse(50, 50, 150, 150)  # Kenarları yumuşatılmış daire çiz

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.show()
app.exec_()
