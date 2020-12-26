from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot, Qt
import sys

exit_shortcut_conf = "Ctrl+Q"

class App(QWidget):
    # ^ vs Window(QMainWindow)?
    def __init__(self, main_window=False):
        super().__init__()
        # window props
        self.title = "PDF opener"
        self.height = 600
        self.width = 900

        # remember if it is main window
        self.main = main_window

        # Listen for exit shortcut
        self.exit_shortcut = QShortcut(QKeySequence(exit_shortcut_conf), self)
        self.exit_shortcut.activated.connect(self.exit_app)

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

    @pyqtSlot()
    def exit_app(self):
        if self.main:
            # TODO: prevent closing if there are unsaved changes
            pass

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App(True)
    sys.exit(app.exec_())
