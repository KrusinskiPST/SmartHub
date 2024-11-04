from PyQt5.QtWidgets import QMessageBox
class CustomMessageBox(QMessageBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        # Ustawienie białego tła i innych stylów specyficznych dla QMessageBox
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QPushButton {
                width: 80px;
                height: 24px;
                background-color: #0078D7;
                color: white;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0053a4;
            }
        """)