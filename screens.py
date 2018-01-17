import os

print(os.curdir)

os.chdir('.')

import requests
from secrets import ID, PASSWORD
import shutil

STOCK_IDEAS_URL = r'http://www.aaii.com/stockideas?a=menubarHome'

# all screens
PERFORMANCE_ROOT    = r'http://www.aaii.com/stockideas/performance'
PERFORMANCE_MONTHLY = r'http://www.aaii.com/files/spreadsheets/stockideas/monthlyperformance.xlsx'
PERFORMANCE_ANNUALLY   = r'http://www.aaii.com/files/spreadsheets/stockideas/annualperformance.xlsx'

# individual screens
r'http://www.aaii.com/stockideas/screendata/CashRichFirms'
r'http://www.aaii.com/files/spreadsheets/stockideas/passingcompanies/CashRichFirms.xlsx'

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': ID,
    'inUserPass': PASSWORD,
}

url = LOGIN_URL

def download_file(url):
    """
    from https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    """
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    return local_filename

##################################

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    stock_ideas = s.post(STOCK_IDEAS_URL, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print (p.text)

    performance = s.post(PERFORMANCE_ROOT, data=payload)

    # An authorised request.
    #r = s.get(PERFORMANCE_MONTHLY)
    #print (r.text)
    
    download_file(PERFORMANCE_MONTHLY)
    download_file(PERFORMANCE_ANNUALLY)
