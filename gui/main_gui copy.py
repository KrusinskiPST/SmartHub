import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class SemiTransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Częściowo Przezroczyste Okno')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowOpacity(0.5)  # Ustaw całkowity poziom przezroczystości okna

        # Styl dla tła okna (tło lekko przezroczyste)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 10);")

def main():
    app = QApplication(sys.argv)
    ex = SemiTransparentWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
