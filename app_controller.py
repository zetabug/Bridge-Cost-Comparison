from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox, QFileDialog
from layout import Ui_MainWindow

import csv
import dialogs
import visualization

import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
 
        self.ui.setupUi(self)

        self.ui.calcCosts_btn.clicked.connect(self.displayAll)
        self.ui.updateDB_btn.clicked.connect(self.openUpdateDialog)
        self.ui.exportPlot_btn.clicked.connect(lambda :  visualization.export_chart(self)) 
        self.ui.exportTable_btn.clicked.connect(self.export_to_CSV) 


    def calcCosts(self):
        # Validate user inputs
        try:
            span_length = float(self.ui.span_input.text().strip())
            width = float(self.ui.width_input.text().strip())
            traffic_volume = float(self.ui.traffic_input.text().strip())
            design_life = float(self.ui.life_input.text().strip())

            # Ensure the values are positive
            if ((not span_length) or (not width) or (not traffic_volume)) :
                raise ValueError

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please check your Input.")
            return

        #fetching costs from database
        conn  = sqlite3.connect('sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM costTable")
        DBcosts = cursor.fetchall()

        # defining user inputs
        span_length = float(self.ui.span_input.text())
        width = float(self.ui.width_input.text())
        traffic_volume = float(self.ui.traffic_input.text())
        design_life = float(self.ui.life_input.text())

        # to store calculated costs
        results = []
        
        for row in DBcosts:
            base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor = row[2:]
        
            # Calculate costs
            construction_cost = span_length * width * base_rate
            maintenance_cost = span_length * width * maintenance_rate * design_life
            repair_cost = span_length * width * repair_rate
            demolition_cost = span_length * width * demolition_rate
            environmental_cost = span_length * width * environmental_factor
            social_cost = traffic_volume * social_factor * design_life
            user_cost = traffic_volume * delay_factor * design_life
            total_cost = (
                construction_cost + maintenance_cost + repair_cost +
                demolition_cost + environmental_cost + social_cost + user_cost
            )

            results.append((construction_cost, maintenance_cost, repair_cost,
                            demolition_cost, environmental_cost, social_cost, user_cost, total_cost))
            
        return results
        

    def displayAll(self):
        res = self.calcCosts()
        if(not res):
            return None

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


        steel_costs = res[0]
        concrete_costs = res[1]

        cost_components = [
            "Construction Cost", "Maintenance Cost", "Repair Cost",
            "Demolition Cost", "Environmental Cost", "Social Cost",
            "User Cost", "Total Cost"
        ]
        
        #======================================================
        # Display table
        #======================================================
        self.ui.tableWidget.verticalHeader().setVisible(False)

        # populate table
        for row, component in enumerate(cost_components):
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(component))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(f"{float(steel_costs[row]):,.2f}"))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"{float(concrete_costs[row]):,.2f}"))
            
            
        #======================================================       
        # Calling the function to dispay bar chart 
        # =====================================================
        visualization.create_plot(self,cost_components, steel_costs, concrete_costs)


    def openUpdateDialog(self):
        dialog = dialogs.UpdatePricesDialog() 
        dialog.exec()
    
    def export_to_CSV(self):
        try : 
            # checking if the table is empty or not
            if self.ui.tableWidget.rowCount()==0 or self.ui.tableWidget.columnCount()==0:
                raise ValueError
            
            else:
                # Open a file dialog to choose a save location
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;All Files (*)", options=options)
                
                if file_path:
                    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
                        writer = csv.writer(file)
                        
                        # Write headers
                        headers = [self.ui.tableWidget.horizontalHeaderItem(col).text() for col in range(self.ui.tableWidget.columnCount())]
                        writer.writerow(headers)
                        
                        # Write table data
                        for row in range(self.ui.tableWidget.rowCount()):
                            row_data = []
                            for col in range(self.ui.tableWidget.columnCount()):
                                item = self.ui.tableWidget.item(row, col)
                                row_data.append(item.text() if item else "")  # Handle empty cells
                            writer.writerow(row_data)

                    print(f"Table exported successfully to {file_path}")
            
        except ValueError:
            QMessageBox.warning(self, "Error", "No data available.")
            return
            
                
        

   