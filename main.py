from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

window_size = 400

def resize_window(option, label):
    global window_size
    if(option == "bigger"):
        window_size += 100
       
    if(option == "smaller"):
        window_size -= 100
    main_win.resize(window_size, window_size)
    label.setText(f'Window size: {main_win.size().width()} x {main_win.size().height()}')

#! App Settings ----
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Test App')
main_win.resize(window_size, window_size)


#! Objects ----

title = QLabel('Window size: 400 x 400')
plusButton = QPushButton('+')
plusButton.clicked.connect(lambda:resize_window("bigger", title))
minusButton = QPushButton('-')
minusButton.clicked.connect(lambda:resize_window("smaller", title))
#! Design ----
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()


row1.addWidget(title, alignment=Qt.AlignCenter)
row2.addWidget(minusButton, alignment=Qt.AlignLeft)
row2.addWidget(plusButton, alignment=Qt.AlignRight)

master_layout.addLayout(row1)
master_layout.addLayout(row2)


main_win.setLayout(master_layout)

#! Show/Run the App ----
main_win.show()
app.exec_()