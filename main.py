import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication
from design import Ui_MainWindow
from parcing import result, save_in_json


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.request = {}
        self.work_edit.setPlaceholderText('Введите должность')
        self.payment_edit.setPlaceholderText('Введите зарплату(в формате *мин*-*макс*)')
        self.city_edit.setPlaceholderText('Введите город')
        self.age_edit.setPlaceholderText('Введите возраст')
        self.sex_edit.setPlaceholderText('Введите пол(М или Ж)')
        self.find_workers_btn.clicked.connect(self.find_characters)
        self.json_btn.clicked.connect(save_in_json)

    def find_characters(self):
        self.request['Название'] = self.work_edit.text()
        self.request['Зарплата'] = self.payment_edit.text()
        self.request['Возраст'] = self.age_edit.text()
        self.request['Пол'] = self.sex_edit.text()
        self.request['Город'] = self.city_edit.text()
        res = result(self.request)
        if res:
            self.label_10.setText(self.request['Название'])
            self.label_9.setText(res['Зарплата'])
            self.label_8.setText(res['Город'])
            self.label_7.setText(res['Возраст'])
            self.label_6.setText(res['Пол'])
            self.url_label.setText(res['Ссылка'])
        else:
            self.label_10.setText('Нету такого работника')
            self.label_9.setText('')
            self.label_8.setText('')
            self.label_7.setText('')
            self.label_6.setText('')
            self.url_label.setText('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
