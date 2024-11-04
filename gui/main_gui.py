from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLineEdit, QListWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadStyleSheet('main.qss')
        self.active_button = None
    def initUI(self):
        self.setWindowTitle('Smart Hub')
        self.resize(1200, 800)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.main_panel = QFrame()
        self.main_panel.setObjectName("content")
        self.main_panel.setFrameShape(QFrame.StyledPanel)
        main_layout.addWidget(self.main_panel, 5)

        self.main_panel_layout = QVBoxLayout(self.main_panel)
        self.main_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel('Jesteś zalogowany!', self.main_panel)
        self.label.setAlignment(Qt.AlignCenter)
        self.main_panel_layout.addWidget(self.label)


        iconPanel = QFrame(self)
        iconPanel.setObjectName("iconPanel")

        tiles_layout = QVBoxLayout(iconPanel)
        tiles_layout.setContentsMargins(0, 0, 0, 0)
        tiles_layout.setSpacing(0)
        tiles_layout.addStretch(0)

        button_width = 110
        iconPanel.setFixedWidth(button_width)  # Ustaw szerokość z marginesami


        icon_dir = os.path.join(os.path.dirname(__file__), '..', 'resources', 'img')
        icon_names = [
            ("home.ico","Home", self.home), 
            ("plus.ico","Add device", self.add), 
            ("list.ico","Device list", self.device_list), 
            ("user.ico","User", self.user_profile), 
            ("settings.ico","Settings", self.settings)
            ]

        for icon_name, label_text, function in icon_names:
            icon_path = os.path.join(icon_dir, icon_name)
            button = QPushButton()
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(64, 64))
            button.setFixedWidth(button_width)
            button.clicked.connect(function)
            
            # Stworzenie layoutu dla przycisku i etykiety
            button_layout = QVBoxLayout()
            button_layout.addWidget(button)
            
            # Dodanie etykiety pod przyciskiem
            button_label = QLabel(label_text)
            button_label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie etykiety
            button_layout.addWidget(button_label)
            button_label.setObjectName("Label")
            # Dodanie całego layoutu z przyciskiem i etykietą do głównego layoutu
            tiles_layout.addLayout(button_layout)
            tiles_layout.addStretch(0)

        main_layout.addWidget(iconPanel, 1)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                elif item.layout() is not None:
                    self.clear_layout(item.layout())

    def update_icon_color(self, new_active_button):
        if self.active_button:
            self.active_button.setStyleSheet("")  # Resetuj styl dla poprzedniego aktywnego przycisku
        new_active_button.setStyleSheet("QPushButton { background-color: rgba(124, 124, 124, 133);border-radius: 0px;padding-left: 20px;padding-right: 20px; }")  # Ustaw kolor dla nowego przycisku
        self.active_button = new_active_button  # Zaktualizuj referencję do nowego przycisku


    def home(self):
        self.clear_layout(self.main_panel_layout)

        central_widget = QWidget()
        central_widget.setObjectName("home")
        self.main_panel_layout.addWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(central_widget)
        
        # Add a centered QPushButton with fixed width
        add_button = QLabel("Submit")
        add_button.setFixedWidth(150)
        layout.addWidget(add_button, alignment=Qt.AlignCenter)

        # Update icon color
        self.update_icon_color(self.sender())

    def add(self):
        self.clear_layout(self.main_panel_layout)

        central_widget = QWidget()
        central_widget.setObjectName("add_panel")
        self.main_panel_layout.addWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(central_widget)
        
        # Create QLineEdit widgets directly and set fixed width
        self.client_id = QLineEdit()
        self.client_id.setPlaceholderText("Wprowadź CLIENT_ID")
        self.client_id.setFixedWidth(300)
        layout.addWidget(self.client_id, alignment=Qt.AlignCenter)
        self.client_id.setObjectName("add_input")

        self.secret_key = QLineEdit()
        self.secret_key.setPlaceholderText("Wprowadź SECRET_KEY")
        self.secret_key.setFixedWidth(300)
        layout.addWidget(self.secret_key, alignment=Qt.AlignCenter)
        self.secret_key.setObjectName("add_input")

        self.local_key = QLineEdit()
        self.local_key.setPlaceholderText("Wprowadź LOCAL_KEY")
        self.local_key.setFixedWidth(300)
        layout.addWidget(self.local_key, alignment=Qt.AlignCenter)
        self.local_key.setObjectName("add_input")

        # Add a centered QPushButton with fixed width
        add_button = QPushButton("Submit")
        add_button.clicked.connect(self.submit_data)
        add_button.setFixedWidth(150)
        layout.addWidget(add_button, alignment=Qt.AlignCenter)
        add_button.setObjectName("add_button")

        # Update icon color
        self.update_icon_color(self.sender())

    def submit_data(self):
        # This method handles data submission
        client_id = self.client_id.text()
        secret_key = self.secret_key.text()
        local_key = self.local_key.text()
        print(f"CLIENT_ID: {client_id}, SECRET_KEY: {secret_key}, LOCAL_KEY: {local_key}")

    def device_list(self):
        self.clear_layout(self.main_panel_layout)
        list_widget = QListWidget()
        # Tutaj możesz dodać elementy do list_widget, np. z bazy danych
        self.main_panel_layout.addWidget(list_widget)
        list_widget.setObjectName("list")
        self.update_icon_color(self.sender())  # Przekazanie klikniętego przycisku

    def user_profile(self):
        self.clear_layout(self.main_panel_layout)
        user_widget = QListWidget()
        # Tutaj możesz dodać elementy do list_widget, np. z bazy danych
        self.main_panel_layout.addWidget(user_widget)
        user_widget.setObjectName("user")
        self.update_icon_color(self.sender())  # Przekazanie klikniętego przycisku

    def settings(self):
        self.clear_layout(self.main_panel_layout)
        settings_widget = QListWidget()
        # Tutaj możesz dodać elementy do list_widget, np. z bazy danych
        self.main_panel_layout.addWidget(settings_widget)
        settings_widget.setObjectName("settings")
        self.update_icon_color(self.sender())  # Przekazanie klikniętego przycisku
        
    def loadStyleSheet(self, sheetName):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path_to_file = os.path.join(current_dir, '..', 'resources', 'qss', sheetName)
        with open(path_to_file, 'r') as file:
            self.setStyleSheet(file.read())

   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

