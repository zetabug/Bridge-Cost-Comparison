# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # frame 1 - input form
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_1.setStyleSheet("")
        self.frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_1.setObjectName("frame_1")
        
        self.frame_1_layout = QtWidgets.QVBoxLayout(self.frame_1)
        self.frame_1_layout.setObjectName("frame_1_layout")
        
        
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_1)
        # self.formLayoutWidget.setGeometry(QtCore.QRect(15, 30, 235, 361))
        self.formLayoutWidget.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(45)

        self.formLayout.setObjectName("formLayout")
        self.span_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.span_label.setFont(font)
        self.span_label.setAlignment(QtCore.Qt.AlignCenter)
        self.span_label.setObjectName("span_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.span_label)
        self.span_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.span_input.setMinimumSize(QtCore.QSize(0, 25))
        self.span_input.setBaseSize(QtCore.QSize(0, 0))
        self.span_input.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.span_input.setObjectName("span_input")
        self.span_input.setValidator(QIntValidator(0,9999999))
    

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.span_input)
        self.width_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.width_label.setFont(font)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)
        self.width_label.setObjectName("width_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.width_label)
        self.width_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.width_input.setValidator(QIntValidator(0,9999999))

        self.width_input.setMinimumSize(QtCore.QSize(0, 25))
        self.width_input.setObjectName("width_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.width_input)
        self.traffic_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.traffic_label.setMinimumSize(QtCore.QSize(0, 58))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.traffic_label.setFont(font)
        self.traffic_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.traffic_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.traffic_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.traffic_label.setObjectName("traffic_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.traffic_label)
        self.traffic_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.traffic_input.setValidator(QIntValidator(0,9999999))

        self.traffic_input.setMinimumSize(QtCore.QSize(0, 25))
        self.traffic_input.setObjectName("traffic_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.traffic_input)
        self.life_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.life_label.setFont(font)
        self.life_label.setAlignment(QtCore.Qt.AlignCenter)
        self.life_label.setObjectName("life_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.life_label)
        self.life_input = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.life_input.setEnabled(True)
        self.life_input.setMaximum(500)
        self.life_input.setMinimumSize(QtCore.QSize(0, 25))
        self.life_input.setStyleSheet("font-size: 12px;")
        self.life_input.setObjectName("life_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.life_input)
        
        # Add formLayoutWidget to the vertical layout
        self.frame_1_layout.addWidget(self.formLayoutWidget)
        

        self.calcCosts_btn = QtWidgets.QPushButton(self.frame_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calcCosts_btn.setFont(font)

        self.calcCosts_btn.setStyleSheet("color:#fff;\n"
"background-color:rgb(0, 0, 0)")
        self.calcCosts_btn.setObjectName("calcCosts_btn")
        
        self.frame_1_layout.addWidget(self.calcCosts_btn)

        self.updateDB_btn = QtWidgets.QPushButton(self.frame_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateDB_btn.setFont(font)
        self.updateDB_btn.setStyleSheet("color:#fff;\n"
"background-color:rgb(0, 0, 0)")
        self.updateDB_btn.setObjectName("updateDB_btn")
        
        self.frame_1_layout.addWidget(self.updateDB_btn)
        
        self.horizontalLayout.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.frame_3_layout = QtWidgets.QVBoxLayout(self.frame_3)
        self.frame_3_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_3_layout.addWidget(self.tableWidget)

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        # Style the headers
        self.tableWidget.setStyleSheet("""
        QHeaderView::section {
                background-color: black; 
                color: white;
                font-size: 12px; 
                font-weight: bold;
                border: 1px solid gray;
                outline: none;
        }
        """)

        # Enable stretching for columns to fit the available space
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Adjust the default section size (optional)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)


        # Add Export Table button
        self.exportTable_btn = QtWidgets.QPushButton(self.frame_3)
        self.exportTable_btn.setFixedSize(250, 50)  # Fixed size, no stretching
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.exportTable_btn.setFont(font)
        self.exportTable_btn.setStyleSheet("""background-color:rgb(0, 0, 255);
        color:#fff;""")
        self.exportTable_btn.setObjectName("exportTable_btn")

        self.frame_3_layout.addWidget(self.exportTable_btn, alignment=QtCore.Qt.AlignCenter)

        # Add Export Plot button
        self.exportPlot_btn = QtWidgets.QPushButton(self.frame_3)
        self.exportPlot_btn.setFixedSize(250, 50)  # Fixed size, no stretching
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.exportPlot_btn.setFont(font)
        self.exportPlot_btn.setStyleSheet("""background-color:rgb(0, 0, 255);
        color:#fff;""")
        self.exportPlot_btn.setObjectName("exportPlot_btn")

        self.frame_3_layout.addWidget(self.exportPlot_btn, alignment=QtCore.Qt.AlignCenter)
        


        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 12)
        self.horizontalLayout.setStretch(1, 30)
        self.horizontalLayout.setStretch(2, 18)
        
        self.frame_3_layout.setStretch(0,76)
        self.frame_3_layout.setStretch(1,12)
        self.frame_3_layout.setStretch(3,12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Bridge Cost Comparison", "Bridge Cost Comparison"))
        self.span_label.setText(_translate("MainWindow", "Span Length (m) :"))
        self.width_label.setText(_translate("MainWindow", "Width (m) :"))
        self.traffic_label.setText(_translate("MainWindow", "<html><head/><body><p><span >Traffic Volume :</span></p><p><span >(Average Daily Traffic </span></p><p><span>in vehicles/day)</span></p></body></html>"))
        self.life_label.setText(_translate("MainWindow", "Design Life (years) :"))
        self.updateDB_btn.setText(_translate("MainWindow", "Update Database"))
        self.calcCosts_btn.setText(_translate("MainWindow", "Calculate Costs"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cost Component"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Steel Bridge (₹)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Concrete Bridge (₹)"))
        self.exportPlot_btn.setText(_translate("MainWindow", "Export Plot"))
        self.exportTable_btn.setText(_translate("MainWindow", "Export Table"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.showMaximized()
#     sys.exit(app.exec_())
