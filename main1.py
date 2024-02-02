import sys
from io import BytesIO
import requests
from PIL import Image
from PyQt5 import uic, Qt  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QCheckBox, QPushButton, QFileDialog

text = ''


# ТАБЛИЦА


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        # self.con = sqlite3.connect('data.db')  # подключение бд
        self.pushButton_1.clicked.connect(self.shema)
        self.pushButton_2.clicked.connect(self.sputnik)
        self.pushButton_2.clicked.connect(self.gibrid)
        self.pushButton.clicked.connect(self.search)

        # self.keyPressEvent()

    def search(self):
        toponim = self.lineEdit.text()
        map_server = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponim,
            "format": "json"
        }
        response = requests.get(map_server, params=params)
        if not response:
            ...
        else:
            json_response = response.json()
            coords = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = coords.split(" ")
            delta = "0.005"
            map_params = {
                "ll": ",".join([lon, lat]),
                "spn": ','.join([delta, delta]),
                "l": "map"
            }
            api_server = ' https://static-maps.yandex.ru/1.x/'
            response = requests.get(api_server, params=map_params)
            pixmap = QPixmap(Image.open(BytesIO(response.content)))
            self.label.setPixmap(pixmap)

        self.lineEdit.setText("")

    def shema(self):
        ...

    def sputnik(self):
        ...

    def gibrid(self):
        ...
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_PageUp:
    #         print('Key_PageUp')
    #     elif event.key() == Qt.Key_PageDown:  # Key_PageUp:
    #         print('PageDown')
    #     elif event.key() == Qt.Key_Up:
    #         print('up')
    #     elif event.key() == Qt.Key_Down:
    #         print('down')
    #     elif event.key() == Qt.Key_Left:
    #         print('left')
    #     elif event.key() == Qt.Key_Right:
    #         print('right')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
