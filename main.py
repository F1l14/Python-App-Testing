from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

#! App Settings ----
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Test App')
main_win.resize(400, 400)


#! Objects ----
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')

#! Design ----
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(button1, alignment=Qt.AlignLeft)
row2.addWidget(button2, alignment=Qt.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignRight)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_win.setLayout(master_layout)

#! Show/Run the App ----
main_win.show()
app.exec_()