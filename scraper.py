import requests

def scrapeElection():
    #According to the website, the form takes a POST request.
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

    print response.text

    return

if __name__== "__main__":
    scrapeElection()
