import requests
import csv
from bs4 import BeautifulSoup

def getPayload(elec_code, D3, t):
    return None

def scrapeWardElection(elec_code, ward, race_number):

    url = "http://www.chicagoelections.com/en/pctlevel3.asp?Ward=" + str(ward) + "&elec_code=" + str(elec_code) + "&race_number=" + str(race_number)

    response = requests.get(url) #todo check dis function to be safe

    if response.status_code != 200:
        print "Failed to scrape from " + url
    #print response.text
    return response.text

def scrapeElectionURL(url):
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print "Failed to scrape from " + url
    return response.text

def scrapeElection(elec_code,contest):
    #According to the website, the form takes a POST request to GET data. WutFace
    payload = {
        'VTI-GROUP': 0,
        'D3':        contest,
        'flag':      1,
        'B1':        'View The Results'
    }
    url = "http://www.chicagoelections.com/en/wdlevel3.asp?elec_code=" + str(elec_code) #6 = 2016 Primary Republican
    #test
    url = url
    response = requests.post(url, data=payload)
    return response.text

def getElectionCodes():
    #Could scrape, but instead, need to manually get
    pass
    return    

def writeCSVRows(rows,file_name):
    f = open(file_name,'w')
    w = csv.writer(f,delimiter=',')
    count = 0
    for row in rows:
        w.writerow(row)
        count += 1
    f.close()
    print "Wrote ", count, " rows to ", file_name
    return

def convertHTMLToCSV(html,file_name):
    """
    Given HTML document as a string, write to a CSV file with the name of the
    table as the CSV file's name.
    """
    soup = BeautifulSoup(html, "html.parser")
    html_rows = soup.find("table").find_all("tr")
    #MOTHER FUCKING LIST COMPREHENSION WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    rows = [[c.get_text() for c in r.find_all("td")] for r in html_rows]

    #this will break if there are less than 4 rows in the table lol
    writeCSVRows(rows[3:-2],file_name)
    return

if __name__ == "__main__":
    testText = scrapeElection("5","President, U.S.")
    convertHTMLToCSV(testText, "election.csv")
    getText = scrapeWardElection(5,1,10)
    convertHTMLToCSV(getText,"ward.csv")
