# Steel vs. Concrete Bridge Cost Comparison Software

## About The Project

![Screenshot (165)](https://github.com/user-attachments/assets/cbf9d4a0-48f7-4ed0-aa1f-7f861cf8212b)

The primary objective of this project was to develop a desktop application to compare the life cycle costs of steel and concrete bridges. This application leverages SQLite to store cost-related data and PyQt5 for the graphical user interface (GUI). The software aims to facilitate informed decision-making by providing users with clear cost breakdowns and visual comparisons.


## Prerequisites
1. Ensure Python is installed on your system.
2. Ensure pip is installed and accessible by running the following command
  ```
pip --version
``` 
3. Install the required dependencies by running the following command.
```
pip install matplotlib==3.10.0 numpy==2.2.1 PyQt5==5.15.11 PyQt5_sip==12.16.1
```  
4. If problems arise during installation, try installing an older version of python(Python 3.9.7), and then try again.



## Installation
1. Clone the Repo
```
git clone https://github.com/zetabug/Bridge-Cost-Comparison.git
```
2. Change directory
```
cd Bridge-Cost-Comparison
```
3. Run the main file
```
python main.py
```

## Usage
1. Provide input for all the fields in the Input Panel. --Mandatory--
2. Click on the Calculate Costs button.
3. To export the Bar plot and the Table, click on the Export Plot/Export Table button as suitable.
4. Prices stored in the SQLite database can be updated using the Update Database button.




