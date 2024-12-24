from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication

import db_operations
import app_controller



if __name__ == '__main__':
    db_operations.init_db()
    app = QApplication([])
    window = app_controller.MainWindow()
    window.show()
    app.exec()




