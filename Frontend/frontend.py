import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(119, 99, 371, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Set the background image using QPalette
        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("E:/Games/Frontend/sky.jpg")
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        MainWindow.setPalette(palette)

        self.BrowsePDF = QtWidgets.QPushButton(self.frame)
        self.BrowsePDF.setGeometry(QtCore.QRect(230, 30, 75, 23))
        self.BrowsePDF.setObjectName("BrowsePDF")
        self.Submit = QtWidgets.QPushButton(self.frame)
        self.Submit.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.Submit.setObjectName("Submit")
        self.FontSize = QtWidgets.QLabel(self.frame)
        self.FontSize.setGeometry(QtCore.QRect(100, 70, 51, 31))
        self.FontSize.setSizeIncrement(QtCore.QSize(2, 2))
        self.FontSize.setObjectName("FontSize")
        self.FontColour = QtWidgets.QLabel(self.frame)
        self.FontColour.setGeometry(QtCore.QRect(100, 100, 61, 31))
        self.FontColour.setObjectName("FontColour")
        self.TitleFontSize = QtWidgets.QLabel(self.frame)
        self.TitleFontSize.setGeometry(QtCore.QRect(100, 140, 71, 21))
        self.TitleFontSize.setObjectName("TitleFontSize")
        self.TitleFontColour = QtWidgets.QLabel(self.frame)
        self.TitleFontColour.setGeometry(QtCore.QRect(100, 170, 81, 16))
        self.TitleFontColour.setObjectName("TitleFontColour")
        self.FontSizenNo = QtWidgets.QComboBox(self.frame)  # Replace with QComboBox
        self.FontSizenNo.setGeometry(QtCore.QRect(200, 70, 71, 21))
        self.FontSizenNo.setObjectName("FontSizenNo")
        self.FontSizenNo.addItems(["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30"])
        self.TitleFontColourNo = QtWidgets.QComboBox(self.frame)  # Replace with QComboBox
        self.TitleFontColourNo.setGeometry(QtCore.QRect(200, 170, 71, 21))
        self.TitleFontColourNo.setObjectName("TitleFontColourNo")
        self.TitleFontColourNo.addItems(["Red", "Blue", "Black", "Green", "Yellow", "White"])
        self.TitleFontSizeNo = QtWidgets.QComboBox(self.frame)  # Replace with QComboBox
        self.TitleFontSizeNo.setGeometry(QtCore.QRect(200, 130, 71, 21))
        self.TitleFontSizeNo.setObjectName("TitleFontSizeNo")
        self.TitleFontSizeNo.addItems(["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30"])
        self.FontColourNo = QtWidgets.QComboBox(self.frame)  # Replace with QComboBox
        self.FontColourNo.setGeometry(QtCore.QRect(200, 100, 71, 21))
        self.FontColourNo.setObjectName("FontColourNo")
        self.FontColourNo.addItems(["Red", "Blue", "Black", "Green", "Yellow", "White"])
        self.FileName = QtWidgets.QLineEdit(self.frame)
        self.FileName.setGeometry(QtCore.QRect(70, 30, 151, 21))
        self.FileName.setObjectName("FileName")
        self.FileName.setReadOnly(True)  # Set the QLineEdit as read-only
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BrowsePDF.clicked.connect(self.browse_pdf)  # Connect the button click event to a custom method

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowsePDF.setText(_translate("MainWindow", "Browse PDF"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.FontSize.setText(_translate("MainWindow", "Font Size\n"
""))
        self.FontColour.setText(_translate("MainWindow", "Font Colour\n"
""))
        self.TitleFontSize.setText(_translate("MainWindow", "Title Font Size\n"
""))
        self.TitleFontColour.setText(_translate("MainWindow", "Title Font Colour"))

    def browse_pdf(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                file_name = QtCore.QFileInfo(selected_file).fileName()  # Extract the file name
                self.FileName.setText(file_name)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create an instance of the generated UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())