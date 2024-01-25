import argparse
import urllib.request
from urllib.request import urlopen,urlretrieve
import ssl
import pypdf
from pypdf import PdfReader
import sqlite3
from sqlite3 import Error

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
    cur.execute('select * from incidents where incident_number="2024-00004434W"')
    row2=cur.fetchall()
    print(row2)

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

def extractincidents():
    reader = PdfReader("../tmp/Incident_Report.pdf")
    dataList=[]
    pageList=[]
    for page in reader.pages:
        pageList+=(page.extract_text().split('\n'))

    for i,page in enumerate(pageList):
        spaceSplit=page.split(' ')
        temp=[]
        size=len(spaceSplit)
        if size<5 or i==0:
            continue
        
        incTime=spaceSplit[0]+' '+spaceSplit[1]
        incNum=spaceSplit[2]
        incORI=spaceSplit[size-1]
        temp.append(incTime)
        temp.append(incNum)
        incLoc=spaceSplit[3]+' '
        incNat=""
        
        for j,space in enumerate(spaceSplit):
            if j==size-1:
                continue
            
            if j>=4:
                if ( space=="MVA" or not space.isupper() or space=="911" ) and not space=='/' and not space=='9':
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