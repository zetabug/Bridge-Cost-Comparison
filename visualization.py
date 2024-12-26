from PyQt5.QtWidgets import QVBoxLayout, QFileDialog,QMessageBox
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import ticker
from PyQt5 import QtWidgets



def create_plot(self , categories , steel_values, concrete_values ):
    
        categories.reverse()
        steel_values = steel_values[::-1]
        concrete_values = concrete_values[::-1]
        
        # Check if the canvas already exists in frame2's layout
        layout = self.ui.frame_2.layout()
        if layout is None or layout.count() == 0:
            # If no existing canvas, create it and add to layout
            figure = Figure(figsize=(5, 4), dpi=100)
            canvas = FigureCanvas(figure)
            axes = figure.add_subplot(111)

            # Add the canvas to the frame2 layout
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            self.ui.frame_2.setLayout(layout)
        else:
            # Access existing canvas and axes
            canvas = layout.itemAt(0).widget()
            axes = canvas.figure.get_axes()[0]

        # Clear existing axes
        axes.clear()

        # Create the double bar chart
        index = np.arange(len(categories))

        bar_width = 0.35
        # Plot the bars for each dataset
        axes.barh(index , concrete_values, bar_width, label='Concrete', color='#F08080')
        axes.barh(index + bar_width, steel_values, bar_width, label='Steel', color='#87CEEB')

        # Set the y-ticks to the center of the bars
        axes.set_yticks(index + bar_width / 2)
        axes.set_yticklabels(categories)

        def format_large_numbers(x, pos):
            if x >= 1_000_000:
                return f'{x*1e-6:.1f}M'
            elif x >= 1_000:
                return f'{x*1e-3:.0f}K'
            else:
                return f'{x:.0f}'

        axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_large_numbers))

        # Add a legend
        axes.legend()

         # Limit the width of the plot by adjusting its position
        axes.set_position([0.25, 0.1, 0.7, 0.85])  # [left, bottom, width, height]

         # Enable dynamic resizing
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()
        canvas.draw()


def export_chart(self):
        layout = self.ui.frame_2.layout()
    
        try:    
            if layout is None or layout.count() == 0:
                print("No data available")
                raise ValueError
            else:
                # Open a file dialog to select the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save Chart", "", "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")

                if file_path:
                    # Save the chart using savefig
                    self.canvas.figure.savefig(file_path)
                    print(f"Chart saved to {file_path}")
        
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please check your Input.")
            return