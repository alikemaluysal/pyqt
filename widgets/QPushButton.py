from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("QPushButton Example")
    window.setGeometry(100, 100, 300, 200)

    button = QPushButton("Click!", window)
    button.move(100, 80)

    # Tıklama olayı
    button.clicked.connect(click)

    window.show()
    sys.exit(app.exec_())

def click():
    print("Clicked!")  # Uygulama kapanmaz, yalnızca bu mesaj yazdırılır.

if __name__ == "__main__":
    main()
