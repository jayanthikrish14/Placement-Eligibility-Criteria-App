
# Placement Eligibility Criteria Application

This is a Streamlit application where users can input eligibility criteria for placement. Based on these criteria, the application queries a dataset of student information to display eligible candidates' details. It also has Data Insights page where user can select a meaningful Insight based on which he can take action.

## Installation

To install the project the following packages are needed to be imported(if not already present):

- Os
- Mysql-connector-python
- streamlit

To install packages run command on Windows: 
python -m pip install <Package Name>

To create required tables and fake data run the Main.py file
from windows command prompt run command:
python <path of the file>Main.py


## Environment Variables

To run this project, you will need to add the following environment variables to your OS with the values required to connect to your database:

- DB_HOST - Host name of your database
- DB_NAME - Name of your database
- DB_USER_NAME - User name for your database
- DB_USER_PASSWORD - Password for your database


# Execution / Usage

### 1. Create Students, Programming, Soft_Skills, Placements tables and generate fake data using faker library:
To create required tables and fake data run the Main.py file.

This file first calls a function to create the tables.
Then calls a function to generate and insert fake data taking the number of Students and Programming records required as parameters.
So pass the required numbers
As per the table relationship in this function:
    For every Student record, passed number of Progrmaming
    records is created
    For every Student record, one Soft_Skills and Placements
    record is created

#### To run the file:
From windows command prompt run the command: 
python <path of the file> Main.py

### 2. Streamlit Application:
This App contains two pages:
### 1. Placement Eligibility Criteria:
Lets users to input eligibility criteria rquired and filter student data based on it.
Select the Eligibilty criteria and the numbers required based on which the student data needs to be filtered and the corresponding data is displayed

### 2. Data Insights: 
  Lets user to extract meaningful insights from the data created/available.

  Select the insight based on which user can take actions.

#### To run the application:
Run the streamlit launch page Menu.py
From windows command prompt run the command: 
streamlit run <path of the file> Menu.py

This Menu page has two options Placement Eligibility Criteria and 
Data Insights. Select the required page and select the option required to get filtered data.
