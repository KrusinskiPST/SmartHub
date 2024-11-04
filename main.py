import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from gui.login_gui import MainForm
from logic.authentication import check_login
from gui.main_gui import MainWindow  
from gui.custommsg_box import CustomMessageBox
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_gui = MainForm()
    main_gui = MainWindow()

    def attempt_login(username, password):
        if username == '' and password == '':
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Wprowadź dane logowania.')
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.exec_()
        elif check_login(username,password):
            login_gui.hide()
            main_gui.show()
        else:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Błędne dane do logowania.')
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.exec_()
    def attempt_register(username_register, mail_register, password_register, password2_register):
    
        if not username_register:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Wprowadź login')
            error_dialog.exec_()
        if not mail_register:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Wprowadź adres E-mail')
            error_dialog.exec_()
        if not password_register:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Wprowadź hasło')
            error_dialog.exec_()
        if not password2_register:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Powtórz hasło')
            error_dialog.exec_()
        if password_register != password2_register:
            error_dialog = CustomMessageBox()
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setText('Hasła powinny być jednakowe')
            error_dialog.exec_()


    login_gui.register_attempt.connect(attempt_register)
    login_gui.login_attempt.connect(attempt_login)
    login_gui.show()
    sys.exit(app.exec_())
