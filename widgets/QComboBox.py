from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QComboBox Örneği")
    window.setGeometry(100, 100, 300, 200)

    combo = QComboBox(window)
    combo.addItems(["Seçenek 1", "Seçenek 2", "Seçenek 3"])
    combo.move(100, 80)

    combo.currentTextChanged.connect(lambda text: print(f"Seçilen: {text}"))

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
