from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import backend


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create QLabel for background image
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("C:/Users/gupta/OneDrive/Desktop/pptx/Picture1.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        # Set the background_label as the parent widget of other widgets
        self.background_layout = QtWidgets.QVBoxLayout(self.background_label)

        # Create the PlainTextEdit widget
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.background_label)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.background_layout.addWidget(self.plainTextEdit)

        # Create the Upload File button
        self.pushButton = QtWidgets.QPushButton(self.background_label)
        self.pushButton.setObjectName("pushButton")
        self.background_layout.addWidget(self.pushButton)

        # Create the Generate PPT button
        self.pushButton_2 = QtWidgets.QPushButton(self.background_label)
        self.pushButton_2.setObjectName("pushButton_2")
        self.background_layout.addWidget(self.pushButton_2)

        # Create other widgets and set their properties (omitted for brevity)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.upload_file)
        self.pushButton_2.clicked.connect(self.generate_ppt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "ADD CONTENT"))
        self.pushButton.setText(_translate("MainWindow", "Upload File"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate PPT"))

    def upload_file(self):
        backend.browse_pdf()

    def generate_ppt(self):
        # Get the content from the PlainTextEdit
        content = self.plainTextEdit.toPlainText()
        backend.create_presentation(content)
