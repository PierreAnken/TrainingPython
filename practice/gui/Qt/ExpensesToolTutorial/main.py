import sys

from PySide6.QtWidgets import QApplication

from practice.gui.Qt.ExpensesToolTutorial.MainWindow import MainWindow
from practice.gui.Qt.ExpensesToolTutorial.Widget import Widget

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()

    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())
