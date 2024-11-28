from PyQt5.QtWidgets import QApplication, QSlider, QLabel, QMainWindow
from PyQt5.QtCore import Qt

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QSlider Örneği")
    window.setGeometry(100, 100, 300, 200)

    slider = QSlider(Qt.Horizontal, window)
    slider.setGeometry(50, 80, 200, 30)
    slider.setMinimum(0)
    slider.setMaximum(100)

    label = QLabel("Değer: 0", window)
    label.move(100, 120)

    slider.valueChanged.connect(lambda value: label.setText(f"Değer: {value}"))

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
