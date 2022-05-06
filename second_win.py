from PyQt5.QtWidgets import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        line_name = QLineEdit('Ф.И.О.')
        name_lable = QLabel('Ведите Ф.И.О.')
        age_lable = QLabel('Полных лет:')
        line_age = QLineEdit('0')
        inster1_lable = Qlable('Лягте на спин и замерьте пульс за 15 секунд. Нажмите кнопку"Начать первый тест", чтобы запустить таймер. Результат запешите в соответствующее поле.') 
        
        self.h_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.btn1)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw.FinalWin()