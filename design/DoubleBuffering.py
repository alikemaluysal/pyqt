from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.buffer = QPixmap(400, 300)
        self.buffer.fill(Qt.white)
        self.painter = QPainter(self.buffer)
        self.painter.setPen(Qt.black)

    def mouseMoveEvent(self, event):
        self.painter.drawEllipse(event.pos().x() - 5, event.pos().y() - 5, 10, 10)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.buffer)

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.resize(400, 300)
window.show()
app.exec_()
