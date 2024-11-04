from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QSpacerItem, QSizePolicy, QApplication
from PyQt5.QtCore import pyqtSignal
import os

class RegisterWindow(QWidget):
    register_attempt = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);")
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rejestracja')
        self.resize(1200, 800)
        self.center()

        main_layout = QVBoxLayout(self)

        input_container = QWidget()
        input_layout = QVBoxLayout(input_container)

        # Pola formularza i etykiety błędów
        self.username_input = QLineEdit()
        self.username_error_label = QLabel()
        self.username_error_label.setStyleSheet("color: red")

        self.mail_input = QLineEdit()
        self.mail_error_label = QLabel()
        self.mail_error_label.setStyleSheet("color: red")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_error_label = QLabel()
        self.password_error_label.setStyleSheet("color: red")

        self.password2_input = QLineEdit()
        self.password2_input.setEchoMode(QLineEdit.Password)
        self.password2_error_label = QLabel()
        self.password2_error_label.setStyleSheet("color: red")

        register_button = QPushButton('Zarejestruj się')
        register_button.clicked.connect(self.check_register)

        # Dodawanie widgetów do layoutu
        input_layout.addWidget(QLabel('Login:'))
        input_layout.addWidget(self.username_input)
        input_layout.addWidget(self.username_error_label)

        input_layout.addWidget(QLabel('Email:'))
        input_layout.addWidget(self.mail_input)
        input_layout.addWidget(self.mail_error_label)

        input_layout.addWidget(QLabel('Hasło:'))
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(self.password_error_label)

        input_layout.addWidget(QLabel('Powtórz hasło:'))
        input_layout.addWidget(self.password2_input)
        input_layout.addWidget(self.password2_error_label)

        input_layout.addWidget(register_button)

        main_layout.addWidget(input_container)

    def check_register(self):
        # Resetowanie komunikatów o błędach
        self.username_error_label.setText('')
        self.mail_error_label.setText('')
        self.password_error_label.setText('')
        self.password2_error_label.setText('')

        # Sprawdzanie, czy pola są puste
        if not self.username_input.text():
            self.username_error_label.setText('Pole nie może być puste.')
        if not self.mail_input.text():
            self.mail_error_label.setText('Pole nie może być puste.')
        if not self.password_input.text():
            self.password_error_label.setText('Pole nie może być puste.')
        if not self.password2_input.text():
            self.password2_error_label.setText('Pole nie może być puste.')

        # Wysłanie danych, jeśli wszystkie pola są poprawnie wypełnione
        if not any([self.username_error_label.text(), self.mail_error_label.text(), self.password_error_label.text(), self.password2_error_label.text()]):
            self.register_attempt.emit(self.username_input.text(), self.mail_input.text(), self.password_input.text(), self.password2_input.text())

    def center(self):
        qr = self.frameGeometry()
        cp = RegisterWindow().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationDisplayName("Transparent Application")
    window = RegisterWindow()
    window.show()
    window.setWindowOpacity(0.8)  # Ustawienie przezroczystości okna
    app.exec_()
