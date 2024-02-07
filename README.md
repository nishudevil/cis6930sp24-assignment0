# 🔰 Introduction to Data Engineering Assignment 0 -> cis6930sp24-assignment0

### 🕵️ Name
- Nishant Routray
- UFID: 36194433
- nishant.routray@ufl.edu

## 💻 Project Description
We are given an Incident pdf which has data regarding all incidents captured on that day from location to the nature of it. We are required to read the pdf for each page and store the entire properly formatted data in SQLLite DB. Then we need to display the count of incidents grouped by the nature of it in the terminal.

## 🛡️ Directories to be present
`/assignment0` contains the main.py <br/>
`/tmp` stores the incidentPdf that is downloaded <br/>
`/resources` stores the sql DB (normanpd.db) that is created <br/>
`/test` contains the test files

## 🐧 Install Steps
```bash
#Pre-requisites to setup the environment before running the main program, first step may not be required
pip install pipenv
pipenv install .
```
## 💡 How to run
```bash
pipenv run python assignment0/main.py --incidents <incidents_url>
```

## 💡 How tor run test
```bash
#Running DB connectivity test and data validity test that is being inserted into SQL
pipenv run python -m pytest -v
```

## ⚙️ downloadPDF() and createDB():
- Downloads the incident pdf from the url into /tmp directory
- Establishes the connection with sqllite and creates the DB in /resources dir
- Creates table `incidents` if it does not exist within the DB 

## ⚙️ extractincidents() and populatedb():
- Read the pdf downloaded page wise and split the data by new line to get a list of all rows.
- Splits each row of string by space to get each element for the row.
- Uses regex and special conditions to match string patterns to determine each column value like data, incident number.
- Properly determine location and nature for each row, by using regex and understanding the patterns in the pdf.
- Handle incomplete data and append if same row data is continued to next line.
- Returns a list of tuples, which in turn is given as a parameter to `populatedb()` to insert the list into DB.

## ⚙️ status()
- Groups by nature field in DB and orders by count in descending followed by nature in ascending to print the data in terminal.
- For null nature, it is handled over here to display such data at the end. e.g "|3"

## 🔑 Video Demo

https://github.com/nishudevil/cis6930sp24-assignment0/assets/33056648/44bd7232-1256-45d0-b1f0-35e04eb55b6d

## 🧱 Database
- DB is created everytime if not present with proper table schema in the appropriate directory structure
- All the data is committed and cleared properly before re-inserting new data

## ❗ Assumptions
- We consider location will always be in upper case to act as a delimiter from nature field.
- The exceptions include `["MVA", "EMS", "COP", "DDACTS"]` which will be added to nature even if its in upper case, analyzed after going through all the existing pdfs.
- All digits shall belong to location except `911`
- For rows where location is continued into a new line, we extract nature from the last capital onwards e.g. HWYMotorist -> Motorist

## 🔥 Test Cases
- DB Connection Test, to make sure sqllite conenction is properly setup
- Checks whether DB file and incidentPdf are created successfully in their respective directories
- Checks the validity of data that is being inserted to DB; like data inserted should not be null, all columns must have a valid value


