from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit



#! App Settings ----
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Calculator')
main_win.resize(250, 500)


#! Objects ----
screen = QLineEdit()
clear = QPushButton('C')
delete = QPushButton('<=')

#! Design ----
master_layout = QVBoxLayout()
master_layout.addWidget(screen)
col1 = QGridLayout()

bottom_row = QHBoxLayout()
bottom_row.addWidget(clear)
bottom_row.addWidget(delete)

calc_row = QHBoxLayout()
calc_row.addLayout(col1)

master_layout.addLayout(calc_row)
master_layout.addLayout(bottom_row)


main_win.setLayout(master_layout)

#! Functionality ----
def buttonHandler(text):
    screen.setText(screen.text() + text)

def buttonCreator(layout, text, row, col):
    button = QPushButton(text)
    button.clicked.connect(lambda:buttonHandler(text))
    layout.addWidget(button, row, col)

clear.clicked.connect(lambda:screen.setText(''))
# [:-1] removes the last character
delete.clicked.connect(lambda:screen.setText(screen.text()[:-1]))

row = 3
col = 0
for i in range(10):
    
    buttonCreator(col1, str(i), row, col)
    
    col+=1
    if i % 3 == 0:
        row -= 1
        col=0
    

for index, value  in enumerate(['/','*','+','-']):
    buttonCreator(col1, value, index, 4)

#! Show/Run the App ----
main_win.show()
app.exec_()