from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()