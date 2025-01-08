from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import db_operations
import app_controller


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


if __name__ == '__main__':
    db_operations.init_db()
    app = QApplication([])
  
    window = app_controller.MainWindow()
    window.showMaximized()
    app.exec()




