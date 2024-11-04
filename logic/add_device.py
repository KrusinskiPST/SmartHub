from PyQt5.QtCore import QThread
from tinytuya.wizard import wizard
class WizardThread(QThread):
    def run(self):
        wizard()  # Funkcja, która może blokować

def run_tinytuya_wizard(self):
    self.wizard_thread = WizardThread()
    self.wizard_thread.start()
