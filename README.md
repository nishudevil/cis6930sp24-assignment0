## 🔰 Introduction

# 🌲 cis6930sp24-assignment0
Data Engineering Assignment 0

# 💻 Project Description
Extracting data from an online source, reformatting the data and stroring useful information is SQL DB

# 🛡️ Directories to be present
`/assignment0` contain the main.py <br/>
`/tmp` stores the incidentPdf that ois downloaded <br/>
`/resources` stores the sql DB that is created <br/>
`/test` contains the test files

# 🐧 Install Steps
```bash
#Pre-requisites to setup the environment before running the main program
pip install pipenv 
pipenv install pypdf 
pipenv shell
pip install .
```
# 💡 How to run
```bash
pipenv run python assignment0/main.py --incidents <incidents_url>
```

# 💡 How tor run test
```bash
#Running test cases present in /test dir
pipenv run python test/<test_fileName>.py
```

# 👉👈 extractincidents() and populatedb():
Reads the pdf row wise and formats the data in proepr format by removing all noisy data
Returns a list of tuples as each row of pdf which is then inserted into DB using populatedb() 

# 🔑 Video Demo