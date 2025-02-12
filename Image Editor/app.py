from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QListWidget, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from os import listdir, path
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
        self.saveB = QPushButton("Save")
        self.saveB.setDisabled(True)
        
        self.dirPath = None
        
         #* Combo -------------------------------
        combo_items = ["Original", "Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"]
        
        for item in combo_items:
            self.comboB.addItem(item)



        self.pictureView = QLabel("Picture View")
        self.pictureView.setAlignment(Qt.AlignCenter)

        #* Functionality------------------------
        self.folderB.clicked.connect(self.openFolder)
        self.fileList.itemSelectionChanged.connect(self.showImage)
        
        #* Design -------------------------------
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        col1_widgets = [self.folderB, self.fileList, self.comboB, self.leftB, self.rightB, self.mirrorB, self.sharpB, self.bwB, self.colorB, self.contrastB, self.blurB, self.saveB]
        for widget in col1_widgets:
            self.col1.addWidget(widget)
        
        self.col2.addWidget(self.pictureView)

        #Adjusting "Stretch", 20% - 80%, of the window view
        self.master_layout.addLayout(self.col1, 20)
        self.master_layout.addLayout(self.col2, 80)
        self.setLayout(self.master_layout)

    #opens system dialog to choose folder , get all file names , filters and keeps the images, adds them to the list
    def openFolder(self):
        self.dirPath = QFileDialog.getExistingDirectory(None, "Select a Folder", "")
        if self.dirPath !="":
            files = listdir(self.dirPath)
            for file in files:
                if file.endswith((".jpg", ".png")):
                    self.fileList.addItem(file)

    # forms the full image path, hides the initial label, creates the image with the correct dimensions, shows the image
    def showImage(self):
        imagePath = path.join(self.dirPath, self.fileList.currentItem().text())
        self.pictureView.hide()
        image = QPixmap(imagePath).scaled(self.pictureView.width(), self.pictureView.height(), Qt.KeepAspectRatio)
        
        self.pictureView.setPixmap(image)
        self.pictureView.show()

        self.saveB.setDisabled(False)

if __name__=="__main__":
    app = QApplication([])
    main_window = Editor()
    main_window.show()
    app.exec_()

