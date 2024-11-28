from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QRegion
from PyQt5.QtCore import Qt, QRect  # QRect artık QtCore'dan alınır

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        clip_region = QRegion(QRect(50, 50, 100, 100))  # Kesme bölgesi
        painter.setClipRegion(clip_region)
        painter.setBrush(Qt.blue)
        painter.drawRect(0, 0, 200, 200)  # Sadece kesme bölgesinde görünecek

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(MyWidget())
window.show()
app.exec_()
