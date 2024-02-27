import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QFile, QTextStream


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.num_inserts = 8  # Количество вставок с текстом и полем для ввода данных
        self.data_file = 'data.txt'
        self.initUI()
        self.load_data()

    def initUI(self):
        vbox = QVBoxLayout()
        s = ['Ширина', 'Высота', 'Цвет яблока', 'Цвет змейки', 'Цвет фона', 'Цвет текста', 'Скорость змейки',
             'Постоянно меняющиеся цвет змейки?(да/нет)']
        self.inserts = []
        for i in range(self.num_inserts):
            hbox = QHBoxLayout()

            text_label = QLabel(s[i])
            hbox.addWidget(text_label)

            text_field = QLineEdit()
            hbox.addWidget(text_field)

            self.inserts.append(text_field)

            vbox.addLayout(hbox)

        save_button = QPushButton('Сохранить данные')
        save_button.clicked.connect(self.save_data)
        vbox.addWidget(save_button)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Приложение с вставками для ввода данных')
        self.show()

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf8') as file:
            for insert in self.inserts:
                data = insert.text()
                file.write(data + '\n')

    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf8') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i < len(self.inserts):
                        self.inserts[i].setText(line.strip())
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
