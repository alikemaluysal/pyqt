from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # Sürekli fare takibi etkin
        self.cursor_pos = None

    def mouseMoveEvent(self, event):
        self.cursor_pos = event.pos()
        self.update()  # Çizimi güncelle

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.cursor_pos:
            painter.drawEllipse(self.cursor_pos.x() - 5, self.cursor_pos.y() - 5, 10, 10)  # Fare çevresine daire çiz

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.show()
app.exec_()
