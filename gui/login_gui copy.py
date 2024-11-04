from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QDesktopWidget, QMessageBox, QStackedWidget
from PyQt5.QtCore import pyqtSignal
import os
class MainForm(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Inicjalizacja obu okien
        self.login_window = LoginWindow()
        self.register_window = RegisterWindow()

        # Dodawanie okien do stosu
        self.addWidget(self.login_window)
        self.addWidget(self.register_window)

        # Połączenie sygnału z odpowiednią funkcją
        self.login_window.register_widget.connect(self.show_register_window)

    def show_register_window(self):
        # Ustawienie okna rejestracji jako aktywnego
        self.setCurrentWidget(self.login_window)

class RegisterWindow(QWidget):
    register_attempt = pyqtSignal(str, str, str, str)
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);")
        self.loadStyleSheet('login.qss')
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle('Login')
        self.resize(1200, 800)
        self.center()
        
        
        # Główny layout, który będzie zawierał input_container z paddingami po bokach
        main_layout = QVBoxLayout(self)

        # Dodanie spacerów w pionie (góra i dół)
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # Dodanie spacerów w poziomie (lewa i prawa strona)
        horizontal_layout = QHBoxLayout()
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding)
        spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding)
        horizontal_layout.addItem(spacer_left)

        # Kontener na inputy
        input_container = QWidget()
        input_layout = QVBoxLayout(input_container)
        username_label = QLabel('Login:')
        self.username_input = QLineEdit()
        password_label = QLabel('Hasło:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton('Zaloguj się')
        register = QLabel('<a href="register_acc">Utwórz konto</a>')
        register.setOpenExternalLinks(False)
        register.linkActivated.connect(self.check_register)

        input_layout.addWidget(username_label)
        input_layout.addWidget(self.username_input)
        input_layout.addWidget(password_label)
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(login_button)
        input_layout.addWidget(register)
        horizontal_layout.addWidget(input_container)

        horizontal_layout.addItem(spacer_right)
        main_layout.addLayout(horizontal_layout)
        main_layout.addItem(spacer_bottom)

        login_button.clicked.connect(self.check_login)

        # Object name 
        input_container.setObjectName("form")
    def check_register(self):
        username_register = self.username_register.text()
        mail_register = self.mail_register.text()
        password_register = self.password_register.text()
        password2_register = self.password2_register.text()
        self.register_attempt.emit(username_register, mail_register, password_register, password2_register)
class LoginWindow(QWidget):
    login_attempt = pyqtSignal(str, str)  # Sygnał wysyłany z loginem i hasłem
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);")
        self.loadStyleSheet('login.qss')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        self.resize(1200, 800)
        self.center()
        
        # Główny layout, który będzie zawierał input_container z paddingami po bokach
        main_layout = QVBoxLayout(self)

        # Dodanie spacerów w pionie (góra i dół)
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # Dodanie spacerów w poziomie (lewa i prawa strona)
        horizontal_layout = QHBoxLayout()
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding)
        spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding)
        horizontal_layout.addItem(spacer_left)

        # Kontener na inputy
        input_container = QWidget()
        input_layout = QVBoxLayout(input_container)
        username_label = QLabel('Login:')
        self.username_input = QLineEdit()
        password_label = QLabel('Hasło:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton('Zaloguj się')
        register = QLabel('<a href="register_acc">Utwórz konto</a>')
        register.setOpenExternalLinks(False)
        register.linkActivated.connect(self.register_widget)

        input_layout.addWidget(username_label)
        input_layout.addWidget(self.username_input)
        input_layout.addWidget(password_label)
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(login_button)
        input_layout.addWidget(register)
        horizontal_layout.addWidget(input_container)

        horizontal_layout.addItem(spacer_right)
        main_layout.addLayout(horizontal_layout)
        main_layout.addItem(spacer_bottom)

        login_button.clicked.connect(self.check_login)

        # Object name 
        input_container.setObjectName("form")

    def check_login(self):
        # Załóżmy, że check_login jest zdefiniowane gdzie indziej
        username = self.username_input.text()
        password = self.password_input.text()
        self.login_attempt.emit(username, password)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def register_widget(self):
        self.setCur(self.RegisterWindow)
    def loadStyleSheet(self, sheetName):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path_to_file = os.path.join(current_dir, '..', 'resources', 'qss', sheetName)
        with open(path_to_file, 'r') as file:
            self.setStyleSheet(file.read())