from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QListWidget, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
class Editor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Editor")
        self.resize(900, 900)

         #* Properties -------------------------------
        self.folderB = QPushButton("Select Folder")
        self.fileList = QListWidget()
        self.comboB = QComboBox()
        self.leftB = QPushButton("Left")
        self.rightB = QPushButton("Right")
        self.mirrorB = QPushButton("Mirror")
        self.sharpB = QPushButton("Sharpness")
        self.bwB = QPushButton("B/W")
        self.colorB = QPushButton("Color")
        self.contrastB = QPushButton("Contrast")
        self.blurB = QPushButton("Blur")
        col1_widgets = [self.folderB, self.fileList, self.comboB, self.leftB, self.rightB, self.mirrorB, self.sharpB, self.bwB, self.colorB, self.contrastB, self.blurB]
        
         #* Combo -------------------------------
        combo_items = ["Original", "Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"]
        
        for item in combo_items:
            self.comboB.addItem(item)



        self.pictureView = QLabel("Picture View")
        
        #* Design -------------------------------
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        for widget in col1_widgets:
            self.col1.addWidget(widget)
        
        self.col2.addWidget(self.pictureView)

        #Adjusting "Stretch", 20%
        self.master_layout.addLayout(self.col1, 20)
        self.master_layout.addLayout(self.col2, 80)
        self.setLayout(self.master_layout)




if __name__=="__main__":
    app = QApplication([])
    main_window = Editor()
    main_window.show()
    app.exec_()

