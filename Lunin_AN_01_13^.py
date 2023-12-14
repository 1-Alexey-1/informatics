#задание 13 Написать программу редактор текстовых файлов с графическим интерфейсом. Обязательно: Кнопка сохранить,
#кнопка выхода. Необязательно, но приветствуется: возможность открытия файла и отображения текста в окне, изменение цвета и размера текста,
#упаковка программы, изменение цвета кнопок принаведении мыши и др.
import os
import sys
from PyQt5 import QtWidgets
import design 
from PyQt5.QtWidgets import *


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_bth.clicked.connect(self.save_file)
        self.ext_btn.clicked.connect(self.exit)
        self.dif=os.getcwd()

    def save_file(self):
        self.my_text = self.edt_text.toPlainText()
        QFileDialog.getSaveFileName()
        with open(self.dir + '/somefile.txt', 'a') as f:
            f.write(self.my_text)
        self.edt_text.clear()
    def exit(self):
        exit()


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp() 
    window.show() 
    app.exec_() 

if __name__ == '__main__':  
    main() 