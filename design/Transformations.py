from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.translate(self.width() / 2, self.height() / 2)  # Orijin merkezde
        painter.rotate(45)  # 45 derece döndür
        painter.drawRect(-50, -50, 100, 100)  # Döndürülmüş dikdörtgen

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.resize(400, 300)
window.show()
app.exec_()
