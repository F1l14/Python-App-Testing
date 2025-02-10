from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        #! App Settings ----
        super().__init__()
        self.setWindowTitle('Calculator')
        self.resize(250, 500)


        #! Properties ----
        self.screen = QLineEdit()
        self.clear = QPushButton('C')
        self.delete = QPushButton('<=')

        self.clear.clicked.connect(self.buttonHandler)
        self.delete.clicked.connect(self.buttonHandler)
        #! Design ----
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.screen)
        col1 = QGridLayout()

        bottom_row = QHBoxLayout()
        bottom_row.addWidget(self.clear)
        bottom_row.addWidget(self.delete)

        calc_row = QHBoxLayout()
        calc_row.addLayout(col1)

        master_layout.addLayout(calc_row)
        master_layout.addLayout(bottom_row)


        self.setLayout(master_layout)

            
        row = 3
        col = 0
        for i in range(10):
            
            self.buttonCreator(col1, str(i), row, col)
            
            col+=1
            if i % 3 == 0:
                row -= 1
                col=0
    

        for index, value  in enumerate(['/','*','+','-','=']):
            self.buttonCreator(col1, value, index, 4)

    #! Functionality ----
    def buttonHandler(self):
        current = self.sender()
        text = current.text()

        match text:
            case "=":
                try:
                    self.screen.setText(str(eval(self.screen.text())))
                except Exception as e:
                    print("error: ", e)
                    self.screen.setText("Error")
            case "C":
                self.screen.setText("")
            case "<=":
                self.screen.setText(self.screen.text()[:-1])
            case _:
                self.screen.setText(self.screen.text()+text)



    def buttonCreator(self, layout, text, row, col):
        button = QPushButton(text)
        button.clicked.connect(self.buttonHandler)
        layout.addWidget(button, row, col)



if __name__ == "__main__":
    app = QApplication([])
    main_window = Calculator()
    main_window.show()
    app.exec_()