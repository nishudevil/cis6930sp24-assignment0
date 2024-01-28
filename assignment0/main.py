import argparse
import urllib.request
from urllib.request import urlopen,urlretrieve
import pypdf
from pypdf import PdfReader
import sqlite3
from sqlite3 import Error
import re

#establish connection to sqlite and create incidents table if not present
def createdb():
    conn = None
    try:
        conn = sqlite3.connect('../resources/normanpd.db')
        cur=conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
                    incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)''')
    except Error as e:
        print(e)
    finally:
        return conn

#insert formatted pdf data into DB
def populatedb(conn,incidents):
    cur=conn.cursor()
    cur.execute('delete from incidents')
    cur.executemany('insert into incidents (incident_time, incident_number, incident_location, nature, incident_ori) values (?,?,?,?,?)',incidents)
    conn.commit()

#Print Nature|Count(*)
def status(conn):
    cur=conn.cursor()
    cur.execute('select nature, count(*) as events from incidents group by nature order by events desc, nature asc')
    rows = cur.fetchall()
    for row in rows:
        print(row[0]+"|"+str(row[1]))

#Download incidents pdf from url
def downloadPDF(url):
    try:
        urlretrieve(url, '../tmp/Incident_Report.pdf')
    except Exception as e:
        print(e)

# Regular expression to find the last capital letter
def extract_last_capital_onwards(s):
    match = re.search(r'[A-Z][a-z]*$', s)

    if match:
        return match.group()
    else:
        return ""

#Split pdf string data by newline and then format each row of pdf to get the required values
def extractincidents():
    reader = PdfReader("../tmp/Incident_Report.pdf")
    dataList=[]
    rowList=[]
    for page in reader.pages:
        rowList+=(page.extract_text().replace("NORMAN","").replace("POLICE","").replace("DEPARTMENT","").split('\n'))

    #remove last row with date only
    rowList.pop()
    for i in range(len(rowList)):
        spaceSplit=rowList[i].strip().split(' ')
        temp=[]
        n=len(spaceSplit)
        if i==0 or spaceSplit[0]=="Daily":
            continue
        if n<5:
            #check if it is an incomplete entry, then we ignore that rw
            if(re.match(r".*?/.*?/.*?",spaceSplit[0])):
                continue
            dataList.pop()
            #if one row data is pushed to a new row, split location from nature by keeping the substring from the last capital letter onwards
            tempIncNature=rowList[i].strip().split(' ')
            for j in range(len(tempIncNature)):
                if(tempIncNature[j].isupper()):
                    tempIncNature[j]=""
                else:
                    tempIncNature[j]=extract_last_capital_onwards(tempIncNature[j])
                    break
            
            spaceSplit=rowList[i-1].strip().split(' ')+tempIncNature
            n=len(spaceSplit)

        incTime=spaceSplit[0]+' '+spaceSplit[1]
        incNum=spaceSplit[2]
        incORI=spaceSplit[n-1]
        temp.append(incTime)
        temp.append(incNum)
        incLoc=spaceSplit[3]+' '
        incNat=""
        #forming incidents location and nature by some formatting and handling special cases
        for j,space in enumerate(spaceSplit):
            if j==n-1:
                continue
            
            if j>=4:
                if space.isdigit():
                    if space=="911":
                        incNat+=space+' '
                    else:
                        incLoc+=space+' '
                        
                elif ( space in ["MVA","COP","DDACTS","EMS"] or not space.isupper() ) and space not in ["1/2",'/']:
                    incNat+=space+' '
                else:
                    incLoc+=space+' '

        temp.append(incLoc.strip())
        temp.append(incNat.strip())
        temp.append(incORI)
        dataList.append(temp)

    
    dataListTuples = [tuple(l) for l in dataList]
    return dataListTuples

def main(url):
    # Download data
    downloadPDF(url)
    
    # Extract data
    incidents = extractincidents()
    #print(incidents)
    
    # Create new database
    conn=createdb()
    
    # Insert data
    populatedb(conn, incidents)
    
    # Print incident counts
    status(conn)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)