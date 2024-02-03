## 🔰 Introduction

# 🌲 cis6930sp24-assignment0
Data Engineering Assignment 0

# 💻 Project Description
We are given an Incident pdf which has data regarding all incidents captured on that day from location to the nature of it. We are required to read the pdf for each page and store the entire properly formatted data in SQLLite DB. Then we need to display the count of incidents grouped by the nature of it in the terminal.

# 🛡️ Directories to be present
`/assignment0` contains the main.py <br/>
`/tmp` stores the incidentPdf that is downloaded <br/>
`/resources` stores the sql DB that is created <br/>
`/test` contains the test files

# 🐧 Install Steps
```bash
#Pre-requisites to setup the environment before running the main program, first two steps are not required since Pipfile is included
pip install pipenv 
pipenv install pypdf pytest
pip install .
```
# 💡 How to run
```bash
pipenv run python assignment0/main.py --incidents <incidents_url>
```

# 💡 How tor run test
```bash
#Running DB connectivity test and data validity test that is being inserted into SQL
pipenv run python -m pytest -v
```

# 👉👈 downloadPDF() and createDB():
- Downloads the incident pdf into /tmp directory
- Establishes the connection with sqllite and creates the DB in /resources dir
- Creates table `incidents` if it does not exist within the DB 

# 👉👈 extractincidents() and populatedb():
- Read the pdf page wise and split the data by new line to get a list of all rows.
- Splits each row of string by space to get each element for the row.
- Uses regex and special conditions to match string patterns to determine each column value like data, incident number.
- Properly determine location and nature for each row.
- Handle incomplete data and append if same row data is continued to next line.
- Returns a list of tuples, which in turn is given as a parameter to `populatedb()` to insert the list into DB.

# 👉👈 status()
- Groups by nature field in DB and orders by count in descending followed by nature in ascending to print the data in terminal.

# 🔑 Video Demo

https://github.com/nishudevil/cis6930sp24-assignment0/assets/33056648/53c49328-b237-4e31-99b7-17eea33e297e

# ❗ Assumptions
We consider location will always be in upper case to act as a delimiter from nature field.
The exceptions include ["MVA","EMS","COP","DDACTS"] which will be added to nature, analyzed after going through all the existing pdfs.

# 🔥 Test Cases
- DB Connection Test
- Checks whether DB file and incidentPdf are created successfully
- Checks the validity of data that is being inserted to DB


