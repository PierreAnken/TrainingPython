# Source: https://doc.qt.io/qtforpython/tutorials/basictutorial/dialog.html
import sys

from PySide6.QtWidgets import QApplication

from practice.gui.Qt.DialogApplication.Form import Form

if __name__ == '__main__':


    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())