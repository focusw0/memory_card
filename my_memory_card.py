from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

app = QApplication([])
mw = QWidget()
mw.setWindowTitle("Memory Card")

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("2 + 2 = ?", "4", "22", "2", "10"))
question_list.append(Question("Летело три воробья. Сколько?", "3", "4", "2", "1"))
question_list.append(Question("Выбери ответ", "Ответ", "Вопрос", "Ок", "X"))
question_list.append(Question("Самая большая страна в мире", "Россия", "Сша", "Канада", "Китай"))
question_list.append(Question("Начало второй мировой войны", "1939", "1941", "1945", "1914"))

#вопросы.

btn_ok = QPushButton('Ответить')
lbl_question = QLabel("Какой национальности не существует?")    

RadioGroupBox = QGroupBox('Варианты ответов')
btn_ans1 = QRadioButton('Энцы')
btn_ans2 = QRadioButton('Чулымцы')
btn_ans3 = QRadioButton('Смурфы')
btn_ans4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
line_h1 = QHBoxLayout()

line_v1.addWidget(btn_ans1)
line_v1.addWidget(btn_ans3)
line_v2.addWidget(btn_ans2)
line_v2.addWidget(btn_ans4)

line_h1.addLayout(line_v1)
line_h1.addLayout(line_v2)

RadioGroupBox.setLayout(line_h1)

#результаты.

AnsGroupBox = QGroupBox('Результаты теста')
lbl_res = QLabel('Прав ты или нет?')
lbl_correct = QLabel('Ответ')

line_res = QVBoxLayout()
line_res.addWidget(lbl_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
line_res.addWidget(lbl_correct, alignment=Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(line_res)

line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h4 = QHBoxLayout()

line_h2.addWidget(lbl_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line_h3.addWidget(RadioGroupBox)
line_h3.addWidget(AnsGroupBox)

#RadioGroupBox.hide()
AnsGroupBox.hide()

line_h4.addStretch(1)
line_h4.addWidget(btn_ok, stretch = 2)
line_h4.addStretch(1)

m_line = QVBoxLayout()

m_line.addLayout(line_h2, stretch = 2)
m_line.addLayout(line_h3, stretch = 8)
m_line.addStretch(1)
m_line.addLayout(line_h4, stretch = 1)
m_line.addStretch(1)
m_line.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Продолжить")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lbl_res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        mw.score += 1
        show_correct("Правильно")
        print("Статистика\nВсего вопросов: ", mw.total, "\nПравильных ответов: ", mw.score)
        print("Рейтинг: ", (mw.score/mw.total)*100, "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно")
            print("Рейтинг: ", (mw.score/mw.total)*100, "%")

def next_question():
    mw.total += 1
    print("Статистика\nВсего вопросов: ", mw.total, "\nПравильных ответов: ", mw.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)   

def click_ok():
    if btn_ok.text() == "Ответить":
        check_answer()
    else:
        next_question()

#q = 
btn_ok.clicked.connect(click_ok)

mw.total = 0
mw.score = 0
next_question()
mw.resize(600, 500)
mw.setLayout(m_line)
mw.show()
app.exec_()