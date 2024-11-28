from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QLabel Örneği")
    window.setGeometry(100, 100, 300, 200)

    label = QLabel("Merhaba, PyQt5!", window)
    label.move(100, 80)  # Ekranda pozisyon

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
