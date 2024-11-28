from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QLineEdit Örneği")
    window.setGeometry(100, 100, 300, 200)

    line_edit = QLineEdit(window)
    line_edit.move(100, 80)
    line_edit.setPlaceholderText("Metin girin...")  # İpucu metni

    line_edit.textChanged.connect(lambda text: print(f"Girilen metin: {text}"))

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
