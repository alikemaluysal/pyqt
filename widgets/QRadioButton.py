from PyQt5.QtWidgets import QApplication, QRadioButton, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QRadioButton Örneği")
    window.setGeometry(100, 100, 300, 200)

    radio1 = QRadioButton("Seçenek 1", window)
    radio1.move(100, 60)
    radio2 = QRadioButton("Seçenek 2", window)
    radio2.move(100, 100)

    radio1.toggled.connect(lambda: print("Seçenek 1 seçildi" if radio1.isChecked() else ""))
    radio2.toggled.connect(lambda: print("Seçenek 2 seçildi" if radio2.isChecked() else ""))

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
