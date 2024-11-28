from PyQt5.QtWidgets import QApplication, QProgressBar, QMainWindow
from PyQt5.QtCore import QTimer

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QProgressBar Örneği")
    window.setGeometry(100, 100, 300, 200)

    progress = QProgressBar(window)
    progress.setGeometry(50, 80, 200, 30)

    timer = QTimer()
    timer.timeout.connect(lambda: progress.setValue(progress.value() + 10))
    timer.start(1000)

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
