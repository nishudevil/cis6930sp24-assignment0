import argparse
import urllib.request
from urllib.request import urlopen,urlretrieve
import ssl
import pypdf
from pypdf import PdfReader
import sqlite3
from sqlite3 import Error
import re

ssl._create_default_https_context = ssl._create_unverified_context

def createdb():
    conn = None
    try:
        conn = sqlite3.connect('../resources/normanpd.db')
        cur=conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
                    incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)''')
        #print("Incidents Table created!!!")
    except Error as e:
        print(e)
    finally:
        return conn


def populatedb(conn,incidents):
    cur=conn.cursor()
    cur.executemany('insert into incidents (incident_time, incident_number, incident_location, nature, incident_ori) values (?,?,?,?,?)',incidents)
    #conn.commit()
    #print("Inserted into DB!!!!!")

def status(conn):
    cur=conn.cursor()
    cur.execute('select nature, count(*) as events from incidents group by nature order by events desc, nature asc')
    rows = cur.fetchall()
    for row in rows:
        print(row[0]+"|"+str(row[1]))
    # cur.execute('select * from incidents where nature ="Public Assist 14005"')
    # row2 = cur.fetchall()
    # print(row2)

def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    try:
        urlretrieve(url, '../tmp/Incident_Report.pdf')
        #print("Downloaded file!")
    except Exception as e:
        print(e)
        
    return data

def extract_last_capital_onwards(s):
    # Regular expression to find the last capital letter
    match = re.search(r'[A-Z][a-z]*$', s)

    if match:
        return match.group()
    else:
        return ""

def extractincidents():
    reader = PdfReader("../tmp/Incident_Report.pdf")
    dataList=[]
    rowList=[]
    for page in reader.pages:
        rowList+=(page.extract_text().replace("NORMAN","").replace("POLICE","").replace("DEPARTMENT","").split('\n'))

    rowList.pop()
    for i in range(len(rowList)):
        spaceSplit=rowList[i].strip().split(' ')
        temp=[]
        n=len(spaceSplit)
        if i==0 or spaceSplit[0]=="Daily":
            continue
        if n<5:
            #check if it is an incomplete entry
            if(re.match(r".*?/.*?/.*?",spaceSplit[0])):
                continue
            dataList.pop()
            #split location from nature by keeping the substring from the last capital letter onwards
            tempIncNature=rowList[i].strip().split(' ')
            tempIncNature[0]=extract_last_capital_onwards(tempIncNature[0])
            spaceSplit=rowList[i-1].strip().split(' ')+tempIncNature
            n=len(spaceSplit)

        #print(spaceSplit)
        incTime=spaceSplit[0]+' '+spaceSplit[1]
        incNum=spaceSplit[2]
        incORI=spaceSplit[n-1]
        temp.append(incTime)
        temp.append(incNum)
        incLoc=spaceSplit[3]+' '
        incNat=""
        
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
    incident_data = fetchincidents(url)
    
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