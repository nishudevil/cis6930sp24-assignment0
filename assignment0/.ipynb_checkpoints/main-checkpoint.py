import argparse
import urllib.request
from urllib.request import urlopen,urlretrieve
import ssl
import pypdf
from pypdf import PdfReader

ssl._create_default_https_context = ssl._create_unverified_context

def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    try:
        urlretrieve(url, '../tmp/Incident_Report.pdf')
        print("Downloaded file!")
    except Exception as e:
        print(e)
        
    return data

def extractincidents():
    reader = PdfReader("../tmp/Incident_Report.pdf")
    for page in reader.pages:
        print(page.extract_text())
        print("------New Page------")


def main(url):
    # Download data
    incident_data = fetchincidents(url)

    # Extract data
    extractincidents()
    # Create new database
	
    # Insert data
	
    # Print incident counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)