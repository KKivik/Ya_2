import io
import os
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Crypto import Decoder, No_Flash_Drive, No_Key_On_Flash

class Cryptographer_window(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('consts/Main_window.ui', self)  # Загружаем дизайн
        self.select_folder.clicked.connect(self.selecting_folder)
        self.encode_button.clicked.connect(self.encoding_select)
        self.fname = ''

    def selecting_folder(self):
        self.fname = QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if self.fname != '' and self.status.text() != '':
            self.status.setText('')

    def encoding_select(self):
        if self.fname == '':
            self.status.setText('Выберите файл!')
            self.status.setStyleSheet("font: 15pt Comic Sans MS")
        else:
            try:
                self.Encryptor = Decoder(self.fname, True)
            except No_Flash_Drive:
                self.status.setText('Вставьте флешку')
                self.status.setStyleSheet("font: 15pt Comic Sans MS")
            except No_Key_On_Flash:
                self.status.setText('На флешке отсутствует ключ')
                self.status.setStyleSheet("font: 15pt Comic Sans MS")
            else:
                self.status.setText('Успешно')
                self.status.setStyleSheet("font: 15pt Comic Sans MS")

    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cryptographer_window()
    ex.show()
    sys.exit(app.exec())

