#Author D4RKSH4DOWS
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

import requests as r
import os,time,random,threading
from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup as bs

os.system('clear')
print ('''%s
____   _____  __  __  _____    __  __
  //  ((   )) ||\\ ||  ||==     ||==||
 //__  \\\_//  || \||  ||___    ||  ||
%sAuthor : D4RKSH4D0WS
'''%(G1,W0))
att=raw_input("\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mAttacker: ")
if att == '':
	exit('[!] Bye goblok')
def zh(sites):
	try:
		agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
		acak = random.choice(agent)
		site=r.post('http://zone-h.org/notify/single',headers={'cache-control': 'max-age=0','upgrade-insecure-requests': '1','save-data': 'on','user-agent': '{acak}','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','referer': 'http://zone-h.org/notify/single','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data={'defacer':att,'domain1':sites,'hackmode':'30','reason':'1'}).text
		prs=bs(site,'html.parser')
		pind=prs.find_all('li')[17]
		if 'OK' in pind.text:
			print ('%s[ %sOK %s] %s'%(W0,G0,W0,sites))
		else:
			print ('%s[ %sERROR %s] %s'%(W0,R0,W0,sites))
	except r.exceptions.ConnectionError:
		exit('[!] Koneksi internet tidak ada')

try:
	print ('%s[%s!%s] %sWeb harus pakai http atau https'%(W1,R1,W1,W0))
	sitelist=raw_input("\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mInput file: ")
	if sitelist == '':
		exit('[!] Bye goblok')
	sites = open(sitelist,"r").read().splitlines()
	pp = Pool(5) #gk usah di tambahin dah 5 aja !
	pr = pp.map(zh, sites)
except IOError:
	exit('[!] File tidak ada')
