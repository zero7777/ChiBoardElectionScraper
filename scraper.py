import requests
import csv
from bs4 import BeautifulSoup

def scrapeElection():
    #According to the website, the form takes a POST request to GET data. WutFace
    payload = {
        'VTI-GROUP': 0,
        'D3':        'U.S. Representative, 1st District',
        'flag':      1,
        'B1':        'View The Results'
    }
    url = "http://www.chicagoelections.com/en/"
    action = "wdlevel3.asp?elec_code=" + "6" #6 = 2016 Primary Republican
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
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")
    print "no spaces after this", "lol"

    ward_table = False 
    #ward tables have 1 less row of padding both top and bot, for use later

    for row in rows[2:-3]:
        #print row.get_text()
        columns = row.find_all("td")
        for column in columns:
            print column.get_text(),
        print "\n--------"

    return

if __name__ == "__main__":
    testText = scrapeElection()
    convertHTMLToCSV(testText)
