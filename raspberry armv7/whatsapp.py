## Configuration



target = "" ## Name of the target user whom you want to send the message
## target name should be as it appears on the Whatsapp Web


from pkgutil import ImpImporter
import requests
from time import sleep
import sys
sys.stdout.flush()
sleep(0.5)
print("Checking Internet ", end=".")
while True:
    sys.stdout.flush()
    sleep(0.5)
    try:
        resp = requests.get('https://www.google.com/', timeout=2).status_code
        if str(resp).strip() == "200":
            print("\nConnected to Internet")
            break
        else:
            print(resp)
    except:
        print(".", end="")
        # print(".")
        sleep(5)
        pass




import rpa as r
# print("Settings")
# r.debug(on_off=True)
# r.error(True)
# r.setup()
# r.load('/home/pi/.tagui/src/tagui').replace('"google-chrome"', '"chromium-browser"').replace('python', 'python3')
# r.dump(r.load('/home/pi/.tagui/src/tagui').replace('python', 'python3').replace('"google-chrome"', '"chromium-browser"'), '/home/pi/.tagui/src/tagui')
# r.init(chrome_browser = True)
r.dump(r.load('/home/pi/.tagui/src/tagui').replace('"google-chrome"', '"chromium-browser"'), '/home/pi/.tagui/src/tagui')
print("Init")
r.init()
print("URL")
r.url("https://web.whatsapp.com/")




def getRaspberryPi_ip():
    import os

    ipv4 = {}
    cmd = "/usr/sbin/ifconfig | grep \"inet \" | grep -v 127.0.0.1 | awk '{print $2}'|awk '{split($0,a,\"/\"); print a[1]}'"
    output = os.popen(cmd).readlines()
    for each in output:
        x0 = str(each).strip()
        if x0.startswith("192"):
            ipv4["wlan0"] = str(x0)
            print("wlan0 : " + str(x0))
        elif x0.startswith("169"):
            ipv4["eth0"] = str(x0)
            print("eth0 : " + str(x0))
        else:
            print("Unknown IP detected")
    
    return ipv4

n = 0
count = 0
login = ""
menu_loaded = ""
while n == 0:
    count = count + 1
    print("Loading Whatsapp : " +str(count))
    try:
        menu_loaded = r.read('//*[@title="' + str(target) + '"]')
    except Exception as e:
        pass
    try:
        login = r.read('//*[@class="landing-title _3-XoE"]')
        # print(login)
    except Exception as e:
        pass

    if login == "To use WhatsApp on your computer:":
        print("We need to Login")
        x0 = input("Sign in .....\nPress ENTER to continue ...")
        # quit()
    if menu_loaded == str(target).strip():
        n = 1
        print("Whatsapp Loaded !")
    elif count >= 10:
        n = 1
        print("Error : Unable to Load Whatsapp")
    else:
        n = 0


    if count >= 10:
        print("Too many attempts, check if something is wrong")
        n = 1




ipv4 = getRaspberryPi_ip()

# wiki/docs (wiki.techgence.com)
print(" ## wiki.techgence.com --------")
try:
    wlan0 = ipv4["wlan0"]
    raw_wiki_techgence_wlan = str(wlan0) + ":3000"
    print("WLAN : " + raw_wiki_techgence_wlan)
except Exception as e:
    wlan0 = None
    pass
try:
    eth0 = ipv4["eth0"]
    raw_wiki_techgence_lan = str(eth0) + ":3000"
    print("eth0 : " + raw_wiki_techgence_lan)
except Exception as e:
    eth0 = None
    pass
wiki_techgence = "wiki.techgence.com\n      "
if wlan0 != None:
    wiki_techgence = wiki_techgence + "wlan0 : " + str(raw_wiki_techgence_wlan) + "\n      "
if eth0 != None:
    wiki_techgence = wiki_techgence + "eth0 : " + str(raw_wiki_techgence_lan)

# Nextcloud
wiki_techgence = wiki_techgence + "\n\n" + "Nextcloud\n"
if wlan0 != None:
    wiki_techgence = wiki_techgence + "     wlan0 : " + str(wlan0) + "/nextcloud\n      "
if eth0 != None:
    wiki_techgence = wiki_techgence + "eth0 : " + str(eth0) + "/nextcloud"

## Wireless Printers
wiki_techgence = wiki_techgence + "\n\n" + "Wireless Printers\n"
if wlan0 != None:
    wiki_techgence = wiki_techgence + "     wlan0 : " + str(wlan0) + ":631/jobs\n      "
if eth0 != None:
    wiki_techgence = wiki_techgence + "eth0 : " + str(eth0) + ":631/jobs"


msgContent = str(wiki_techgence).strip()
r.type('//div[@class="_13NKt copyable-text selectable-text"]', target)
r.click(target)
r.type("Type a message", str(msgContent) + "[enter]")
r.click('//*[@data-icon="send"]')
sleep(10)


r.close()
