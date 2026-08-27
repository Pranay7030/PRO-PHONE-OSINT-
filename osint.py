import socket,requests,phonenumbers
from phonenumbers import carrier,geocoder
R="\033[91m";G="\033[92m";Y="\033[93m";C="\033[96m";W="\033[97m"

print(R+r"""
 ____ _ _ _ ____ _ __
| __ )| | | | / \ / ___| |/ /
| _ \| |_| | / _ \ | | | ' /
| |_) | _ |/ ___ \| |___|. \
|____/|_| |_/_/ \_\____|_|\_\
  BHACKSH V9 FINAL - PRANAY
  SOLO GHOST // BHANDARA // V9 COMBO
"""+W)

def phone():
 n=input(Y+"Phone +91: "+W).strip()
 try:
  p=phonenumbers.parse(n)
  print(G+f"Operator: {carrier.name_for_number(p,'en')}"+W)
  print(G+f"Location: {geocoder.description_for_number(p,'en')}"+W)
 except:
  print(R+"Galat Number"+W)

def email():
 e=input(Y+"Email: "+W).strip()
 print(C+f"Check: https://haveibeenpwned.com/account/{e}"+W)

def ip():
 i=input(Y+"IP: "+W).strip()
 try:
  h=socket.gethostbyaddr(i)[0]
 except:
  h="No Host"
 print(G+f"IP:{i} Host:{h}"+W)
 try:
  r=requests.get(f"https://ipapi.co/{i}/json/",timeout=15).json()
  lat=r.get('latitude'); lon=r.get('longitude')
  m=f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
  print(G+f"City: {r.get('city')} ISP: {r.get('org')}"+W)
  print(C+f"MAP: {m}"+W)
  q=input(Y+"QR y/n: "+W)
  if q.lower()=='y':
   import qrcode
   qrcode.make(m).save(f"{i}_map.png")
   print(G+f"Saved {i}_map.png"+W)
 except Exception as ex:
  print(R+str(ex)+W)

def insta():
 u=input(Y+"Insta: "+W).replace("@","").strip()
 print(C+f"https://instagram.com/{u}"+W)

while True:
 c=input(Y+"\n[1]Phone [2]Email [3]IP [4]Insta [5]Exit: "+W)
 if c=='1': phone()
 elif c=='2': email()
 elif c=='3': ip()
 elif c=='4': insta()
 elif c=='5': break
