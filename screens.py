import os

print(os.curdir)

os.chdir('.')

import requests
from secrets import ID, PASSWORD

LOGIN_URL = r'http://www.aaii.com/stockideas?a=menubarHome'

# all screens
PERFORMANCE_ROOT    = r'http://www.aaii.com/stockideas/performance'
PERFORMANCE_MONTHLY = r'http://www.aaii.com/files/spreadsheets/stockideas/monthlyperformance.xlsx'
PERFORMANCE_ANUAL   = r'http://www.aaii.com/files/spreadsheets/stockideas/annualperformance.xlsx'

# individual screens
r'http://www.aaii.com/stockideas/screendata/CashRichFirms'
r'http://www.aaii.com/files/spreadsheets/stockideas/passingcompanies/CashRichFirms.xlsx'

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': ID,
    'inUserPass': PASSWORD,
}

url = LOGIN_URL

##################################

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
    r = s.get(PERFORMANCE_MONTHLY)
    #print (r.text)
        # etc...