from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QPushButton, QGroupBox, QRadioButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from random import shuffle, randint

class Question():
    def __init__(self, quest, r_ans, w1, w2, w3):
        self.quest=quest
        self.r_ans=r_ans
        self.w1=w1
        self.w2=w2
        self.w3=w3

Questions=[]
Questions.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Польский'))
Questions.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Алеуты', 'Чулымцы'))
Questions.append(Question('Какое слово обозначает вид традиционной меховой обуви у народов Сибири и Дальнего Востока?', 'Торбаса', 'Кухлянка', 'Малица', 'Билярцы'))
Questions.append(Question('Как на Севере называют сани, в которые запрягают собак или оленей?', 'Нарты', 'Кибитка', 'Бричка', 'Чуканка'))
Questions.append(Question('Когда расселялись славяне в VI-VIII веках они разделились на несколько ветвей. Определите, какой ветви не было?','Северные','Восточные','Западные','Южные'))
Questions.append(Question('Определите, какое основное занятие у восточных славян', 'Земледелие', 'Скотоводство', 'Рыболовство', 'Охота'))
Questions.append(Question('Определите, какое основное занятие у восточных славян', 'В Ростовской области', 'В Самарской области', 'В Ленинградской области', 'В Московской области'))
Questions.append(Question('Какой народ России считается самым северным?', 'Нганасаны', 'Алтайцы', 'Башкиры', 'Чулымцы'))
Questions.append(Question('Каково количество народов на территории России?', 'Более 190', 'Более 100', 'Более 250', 'Более 150'))
Questions.append(Question('На каком языке разговаривают Мордва?', 'На мокшанском', 'На русском', 'На горномарийском', 'На украинском'))
Questions.append(Question('Какае количество казахов в России?', '647 тыс человек', '821 тыс человек', '1 млн человек', 'Более 1 млн человек'))
Questions.append(Question('Какое место украинцы занимают по численности их постоянного населения на территории России?', '3-е место', '4-е место', '2-е место', '5-е место'))


app=QApplication([])
main_w=QWidget()
main_w.resize(600,300)
main_w.setWindowTitle('Memory Card')
question=QLabel('Какой национальности не существует?')
bts_answer1=QRadioButton('Энцы')
bts_answer2=QRadioButton('Смурфы')
bts_answer3=QRadioButton('Алеуты')
bts_answer4=QRadioButton('Чулымцы')
but=QButtonGroup()
but.addButton(bts_answer1)
but.addButton(bts_answer2)
but.addButton(bts_answer3)
but.addButton(bts_answer4)
enter=QPushButton('Ответить')
Rad=QGroupBox('Варианты ответов')
answer=[bts_answer1,bts_answer2,bts_answer3,bts_answer4]

true=QGroupBox('Результат теста')
trueornot=QLabel('Правильно/Неправильно')
ortrue=QLabel('Правильный ответ')
true.hide()

def show_question():
    enter.setText('Ответить')
    but.setExclusive(False)
    bts_answer1.setChecked(False)
    bts_answer2.setChecked(False)
    bts_answer3.setChecked(False)
    bts_answer4.setChecked(False)
    but.setExclusive(True)
    true.hide()
    Rad.show()

def ask(q1:Questions):
    question.setText(q1.quest)
    shuffle(answer)
    ortrue.setText('Правильный ответ:'+q1.r_ans)
    answer[0].setText(q1.r_ans)
    answer[1].setText(q1.w1)
    answer[2].setText(q1.w2)
    answer[3].setText(q1.w3)
    show_question()

def show_correct(res):
    trueornot.setText(res)

def check_answer():
    Rad.hide()
    true.show()
    enter.setText('Следующий вопрос')
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_w.scr+=1
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неправильно!')
    else:
        show_correct('Ни один ответ не выбран!')
    print('--Статистика--')
    print('-Всего вопросов:', main_w.total)
    print('-Правильных ответов:',main_w.scr)
    print('--Рейтинг:', (main_w.scr/main_w.total)*100,'%')

def next_quest():
    cur_quest=randint(1,len(Questions)-1)
    ask(Questions[cur_quest])
    main_w.total+=1

def Click_OK():
    if enter.text()=='Ответить':
        check_answer()
    else:
        next_quest()

h_line_1=QHBoxLayout()
h_line_2=QHBoxLayout()
v_line_2=QVBoxLayout()
v_line_3=QVBoxLayout()
h_line_3=QHBoxLayout()
h_line_4=QHBoxLayout()
v_line_3.addWidget(bts_answer1,alignment=Qt.AlignCenter)
v_line_3.addWidget(bts_answer2,alignment=Qt.AlignCenter)
v_line_2.addWidget(bts_answer3,alignment=Qt.AlignCenter)
v_line_2.addWidget(bts_answer4,alignment=Qt.AlignCenter)
h_line_2.addLayout(v_line_3)
h_line_2.addLayout(v_line_2)
Rad.setLayout(h_line_2)
h_line_1.addWidget(question,alignment=Qt.AlignHCenter)
h_line_4.addWidget(Rad,alignment=Qt.AlignHCenter)
h_line_3.addStretch(1)
h_line_3.addWidget(enter, stretch=3)
h_line_3.addStretch(1)
v_line=QVBoxLayout()
v_line.addStretch(1)
v_line.addLayout(h_line_1,stretch=1)
v_line.addStretch(1)
v_line.addLayout(h_line_4,stretch=8)
v_line.addStretch(1)
v_line.addLayout(h_line_3,stretch=2)
v_line_true=QVBoxLayout()
v_line_true.addWidget(trueornot,alignment=(Qt.AlignTop|Qt.AlignLeft))
v_line_true.addWidget(ortrue,alignment=Qt.AlignCenter)
true.setLayout(v_line_true)
h_line_4.addWidget(true,alignment=Qt.AlignHCenter)

main_w.scr=0
main_w.total=0
next_quest()
enter.clicked.connect(Click_OK)

main_w.setLayout(v_line)
main_w.show()
app.exec_()