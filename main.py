from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

#! App Settings ----
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Test App')
main_win.resize(400, 400)




#! -----------------


#! Show/Run the App
main_win.show()
app.exec_()