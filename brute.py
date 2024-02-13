#__________________IMPORT____________#

import os,sys,rich,bs4,json,re,random,requests,time,datetime

try:

	from time import sleep

	from bs4 import BeautifulSoup as sop

	from concurrent.futures import ThreadPoolExecutor as tred 

except ModuleNotFoundError:

	print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')

	os.system('pip install rich')

	os.system('pip install requests')

	os.system('pip install bs4')

#__________________ COLOR __________________#

A = '\x1b[1;97m' 

R = '\x1b[38;5;196m'

Y = '\033[1;33m'

G = '\x1b[38;5;48m'

B = '\x1b[38;5;8m'

G1 = '\x1b[38;5;46m'

G2 = '\x1b[38;5;47m'

G3 = '\x1b[38;5;48m'

G4 = '\x1b[38;5;49m'

G5 = '\x1b[38;5;50m'

X = '\33[1;34m'

X1 = '\x1b[38;5;14m'

X2 = '\x1b[38;5;123m'

X3 = '\x1b[38;5;122m'

X4 = '\x1b[38;5;86m'

X5 = '\x1b[38;5;121m'

S = '\x1b[1;96m'

M = '\x1b[38;5;205m'

#__________________ LOOP __________________

pwpluss,pwnya,dump,id,id2,tokenku,method,loop,oks,cps=[],[],[],[],[],[],[],0,0,0

rc = random.choice

rr = random.randint

#__________________ LINE __________________#

def linex():

    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def clear():

	os.system(f'clear')

	print(logo)

#__________________ SAVE OK CP __________________#

bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

tanggal = datetime.datetime.now().day

bulan = bulane[(str(datetime.datet
