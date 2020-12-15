from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt
import sys


class App(QWidget):
    # ^ vs Window(QMainWindow)?
    def __init__(self):
        super().__init__()
        # window props
        self.title = "PDF opener"
        self.height = 600
        self.width = 900

        # window init
        self.initUI()

    def initUI(self):
        # apply window settings
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        # widgets
        vbox = QVBoxLayout()
        self.selected_file_label = QLabel("File not selected")
        self.selected_file_label.setAlignment(Qt.AlignTop)
        vbox.addWidget(self.selected_file_label)

        button = QPushButton('Choose PDF', self)
        button.move(50, 30)
        button.clicked.connect(self.select_pdf)
        vbox.addWidget(button)
        self.setLayout(vbox)

        self.show()

    @pyqtSlot()
    def select_pdf(self):
        qfd = QFileDialog()
        path = "C:\\"
        f = QFileDialog.getOpenFileName(qfd, 'Select PDF', "C:\\", "PDF files (*.pdf)") #
        # f = (file_path, filter), where filter = "PDF files..."     ^

        self.selected_file_label.setText(f"Selected file: {f[0]}")

        return f[0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
