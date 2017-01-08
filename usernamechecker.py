import bs4
import urllib
import requests
import string
from bs4 import BeautifulSoup
import sys

img = '''
  _            _ _       _            _               _
 | |          (_) |     | |          | |             | |
 | |___      ___| |_ ___| |__     ___| |__   ___  ___| | _____ _ __
 | __\ \ /\ / / | __/ __| '_ \   / __| '_ \ / _ \/ __| |/ / _ \ '__|
 | |_ \ V  V /| | || (__| | | | | (__| | | |  __/ (__|   <  __/ |
  \__| \_/\_/ |_|\__\___|_| |_|  \___|_| |_|\___|\___|_|\_\___|_|
github.com/threebarber/
                      '''

print img
twitchurl = 'https://www.twitch.tv/'

filename = raw_input("[+]Enter the filename containing the usernames to check (IE userlist.txt): ")
try:
    twitchlist = open(filename,'r')
except IOError:
    sys.exit("[-]Invalid username filename!")

savefilename = raw_input("[+]Enter filename to save available usernames to: ")
try:
    savelist = open(savefilename,'w')
except IOError:
        sys.exit("[+]Invalid save file")

for line in twitchlist.readlines():
    username = line.strip('\n')
    page = requests.get(twitchurl + username)
    if "404 Not Found" in str(page.headers):
        print "[+]Username " +username+ " available"
        savelist.write(username+ "\n")
    else:
        print "[-]Username " +username+ " unavailable"
    #print page.headers

print "[+]Done!"
