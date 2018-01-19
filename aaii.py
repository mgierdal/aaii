import os

print(os.curdir)

os.chdir('.')

import urllib2
import sys
import requests
from secrets import ID, PASSWORD
import shutil
import re

STOCK_IDEAS_URL = r'http://www.aaii.com/stockideas?a=menubarHome'

# all screens
PERFORMANCE_ROOT    = r'http://www.aaii.com/stockideas/performance' # also redirected from 
PERFORMANCE_MONTHLY = r'http://www.aaii.com/files/spreadsheets/stockideas/monthlyperformance.xlsx'
PERFORMANCE_ANNUALLY   = r'http://www.aaii.com/files/spreadsheets/stockideas/annualperformance.xlsx'

AAII_BASE_URL = r'http://www.aaii.com'
screens_main_url = r'http://www.aaii.com/stock-screens'
screens_mmenubarhome_url = r'http://www.aaii.com/stock-screens?a=menubarHome'
performance_history_url = r'http://www.aaii.com/stock-screens/performance'

# search for http://www.aaii.com/stock-screens/screendata/CANSLIMRev

# individual screens
r'http://www.aaii.com/stockideas/screendata/CashRichFirms'
r'http://www.aaii.com/files/spreadsheets/stockideas/passingcompanies/CashRichFirms.xlsx'

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': ID,
    'inUserPass': PASSWORD,
}

#url = LOGIN_URL


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
def find_xlsx_href(s):
    from re import findall
    ptrn = r'(href.+?xlsx)'
    return findall(ptrn, s)
##################################
def get_aaii_screen_performance_page(url = PERFORMANCE_ROOT):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(url)
    page = response.read()
    return page
def save_aaii_screen_performance_page(html):
    with open('performance.html', 'w') as f:
        f.writelines(html)
##################################

if __name__=='__main__':
    page = get_aaii_screen_performance_page(performance_history_url)
    save_aaii_screen_performance_page(page) # stock_screens.html
    performance_pages = [r''.join([AAII_BASE_URL, re.sub(r'href.*?"','',x)]) for x in find_xlsx_href(page)]
    print performance_pages
    for sheets in performance_pages[:]:
        source_url =  sheets
        performance_file = sheets.split(r'/')[-1]
        print source_url, performance_file
        _, msg = urllib.urlretrieve(source_url, performance_file)
    sys.exit()

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
