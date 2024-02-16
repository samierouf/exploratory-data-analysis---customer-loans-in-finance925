# Exploratory Data Analysis- Customer Loans in Finance

The aim of this project is to practice exploratory data analysis on a customer loan dataset based in AWS using data visulisation and other methods to clean the data and preform statistical analyisis on the data set to then be able to preform querries to get an insight of the data.

## Prerequisites
- AWS account
- Python 3.11
- Java 8
- Download versions from the 'requirements.txt' file
- YAML file containg information about the database 'credentials.yaml'
  
## Installation
```bash
pip install -r requirements.txt
```

## Clonening the repo
using the folwing clone the repo
```bash
git clone https://github.com/samierouf/exploratory-data-analysis---customer-loans-in-finance925.git
```

## Usage
To run this code or recreate something similar, install the prerequisites. Once everything is downloaded/installed, create an environment, a local repository, and clone the repo. Run the main.py file to automatically extract, clean, and upload data from various sources to the sales_data database on your localhost.

## Project information
  - ### data_transformation.py
  - ### dataframe_transformation.py
  - ### db_utils.py
  - ### information.py
  - ### plotter.py
  - ### data_visualisation.ipynb
  - ### main.ipynb

## Project information
### data_transformation.py
Contains code to change the data in the dataframe.

### dataframe_transformation.py
contaibs code that is used to alter the dataframe.

### db_utils.py
Contains the code to connect to the data base.

### information.py
Contains code that extracts information from the data.

### plotter.py
Contains code used to visualise the data.

### data_visualisation.ipynb
Notebook containg the data visualisations that are used to determin the best methods to deal with the data.

### main.ipynb
Contains the code and visuals for EDA of the data.

## Project steps

### Milestone 1
This milestone is about setting up the python environment and creating the YAML file that are going to hold the credentials for dowloading databases.

### Milestone 2
Is the the milestone where the data is extracted from AWS and saved as a csv for easier access.

### Milestone 3
In this milestone we are going to preform Exploratory data analysis on the data so that we can gain an insight and understanding of the data and fix any issues it has such as dealing with nulls, dealing with skewnesss or observing patterns or relations that may be present in the data. In this milestone the data visulisations that are in the `data_visualisation.ipynb` are used to help make the dicissisons on what was method was used to replace the nulls, what transformation was used to normalise the data that have a skew amd to help identify outliers.

### Milestone 4
In this milestone we are going to look at what information can now be extracted from the dataframe and visualise them to better present our findings.

## Learning
### Statistical and visual analysis.
  - Improved statistical analysis
  - Practiced using both Visua and statistical analysis
### Presenting data
  - what visuals may be useful for presenting data
### Handeling Nulls
  - Different ways to handel null or missing data
  - Using information from data set  to fill in null instead of droping a variable even if it exceds the threshold of dropping
### Python
  -  Using jupyter notebooks
  -  practicing coding

## Reflecting on Real-World Application
  -  Using data exploration in decision making
  -  Using EDA to improve data quality
  -  Using Visualisation for communications

## Troubleshooting
 - Ensure that all files are in the same location.
 - All packages are installed in the environment.
 - correct info in YAML file








