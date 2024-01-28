## 🔰 Introduction

# 🌲 cis6930sp24-assignment0
Data Engineering Assignment 0

# 💻 Project Description
We extract data as a PDF from an online source -> Reformatting the data -> Storing useful information in SQL DB

# 🛡️ Directories to be present
`/assignment0` contains the main.py <br/>
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
pipenv run python -m unittest -v test/<test_fileName>.py
```

# 👉👈 extractincidents() and populatedb():
Reads the pdf row wise and formats the data in proper format by removing all noisy data
Returns a list of tuples as each row of pdf which is then inserted into DB using populatedb() 

# 🔑 Video Demo


https://github.com/nishudevil/cis6930sp24-assignment0/assets/33056648/4d1dc49c-4155-4202-bd48-818678aaf73d

