import requests
import csv
from bs4 import BeautifulSoup

def getPayload(elec_code, D3, t):
    return None

def scrapeElection():
    #According to the website, the form takes a POST request to GET data. WutFace
    payload = {
        'VTI-GROUP': 0,
        'D3':        'President, U.S.',
        'flag':      1,
        'B1':        'View The Results'
    }
    url = "http://www.chicagoelections.com/en/"
    action = "wdlevel3.asp?elec_code=" + "5" #6 = 2016 Primary Republican
    #test
    url = url + action
    response = requests.post(url, data=payload)

    return response.text

def getElectionCodes():
    #Could scrape, but instead, need to manually get
    pass
    return    

def convertHTMLToCSV(html):
    """
    Given HTML document as a string, write to a CSV file with the name of the
    table as the CSV file's name.
    """
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find("table").find_all("tr")

    ward_table = False 
    #ward tables have 1 less row of padding both top and bot, for use later
    first = True
    f = open('test.csv','w')
    w = csv.writer(f,delimiter=';')
    for row in rows[3:]:
        columns = row.find_all("td")
        row = []
        string = ""
        for column in columns:
            #print column.get_text("|", strip=True), "|"
            #print column.string, ";",
            row.append(column.get_text())
            string = string + column.get_text() + ";"
        #print "\n--------------------------------"
        w.writerow(row)
        print string
    return

if __name__ == "__main__":
    testText = scrapeElection()
    convertHTMLToCSV(testText)
