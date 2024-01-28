# cis6930sp24-assignment0
Data Engineering Assignment 0

# Project Description
Extracting data from an online source, reformatting the data and stroring useful information is SQL DB

# Install Steps
pip install pipenv
pipenv install pypdf
pipenv shell
pip install .

# How to run
pipenv run python assignment0/main.py --incidents <url>

# How tor run test
pipenv run python test/<test_fileName>.py

# extractincidents() and populatedb():
Reads the pdf row wise and formats the data in proepr format by removing all noisy data
Returns a list of tuples as each row of pdf which is then inserted into DB using populatedb() 