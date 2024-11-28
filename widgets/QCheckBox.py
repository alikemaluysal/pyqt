from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QCheckBox Örneği")
    window.setGeometry(100, 100, 300, 200)

    checkbox = QCheckBox("Seçenek", window)
    checkbox.move(100, 80)

    checkbox.stateChanged.connect(
        lambda state: print("Seçildi" if state else "Seçilmedi")
    )

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
