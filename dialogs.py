from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QTabWidget, QDialog, QDialogButtonBox, QLabel, QMessageBox
import db_operations

class UpdatePricesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Prices")

        # Create tab widget to hold Steel and Concrete tabs
        self.tabs = QTabWidget()

       # Tabs for Steel and Concrete
        self.steel_tab = self.create_tab("Steel")
        self.concrete_tab = self.create_tab("Concrete")

        self.tabs.addTab(self.steel_tab, "Steel")
        self.tabs.addTab(self.concrete_tab, "Concrete")

        # Buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.save_changes)
        self.button_box.rejected.connect(self.reject)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(self.button_box)
        self.setLayout(layout)



    def create_tab(self, material):
        data = db_operations.fetch_material_data(material)
        if not data:
            QMessageBox.warning(self, "Error", f"Could not fetch data for {material}")
            return

        tab = QFormLayout()
        tab.data_fields = {}

        labels = [
            "Base Rate", "Maintenance Rate", "Repair Rate", 
            "Demolition Rate", "Environmental Factor", 
            "Social Factor", "Delay Factor"
        ]
        for i, label in enumerate(labels, start=2):
            line_edit = QLineEdit(str(data[i]))
            tab.addRow(QLabel(label), line_edit)
            tab.data_fields[label] = line_edit

        widget = QWidget()
        widget.setLayout(tab)
        widget.material = material
        return widget


    def save_changes(self):
        for i in range(self.tabs.count()):
            tab = self.tabs.widget(i)
            material = tab.material
            data = []
            for field in tab.layout().data_fields.values():
                try:
                    data.append(float(field.text()))
                except ValueError:
                    QMessageBox.warning(self, "Input Error", f"Invalid value for {field}. Please enter numeric values.")
                    return

            if not db_operations.update_material_data(material, data):
                QMessageBox.warning(self, "Error", f"Failed to update data for {material}.")
                return
        
        QMessageBox.information(self, "Success", "Prices updated successfully!")
        self.accept()
