# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl

#TINGGAL PAKE AJA LOGIN QR DULU
#CREATOR BY 🐲 รєใғв๏ҭ вұ: ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱ 🐲 

botStart = time.time()
mulai = time.time()
#untuk membatasi assist tambahkan tanda pagar sebelum nama assist
print  ("Welcome login self")  
boy = LineClient()
#boy = LineClient(authToken="Token Luu")
channel = LineChannel(boy,boy.server.CHANNEL_ID['LINE_TIMELINE'])
boy.log("Auth Token : " + str(boy.authToken))
print ("Welcome login k1")  
k1 = LineClient()
#k1 = LineClient(authToken="Token Luu")
channel = LineChannel(k1,k1.server.CHANNEL_ID['LINE_TIMELINE'])
k1.log("Auth Token : " + str(k1.authToken))
print ("Welcome login k2")  
k2 = LineClient()
#k2 = LineClient(authToken="Token Luu")
channel = LineChannel(k2,k2.server.CHANNEL_ID['LINE_TIMELINE'])
k2.log("Auth Token : " + str(k2.authToken))
print ("Welcome login k3")  
k3 = LineClient()
#k3 = LineClient(authToken="Token Luu")
channel = LineChannel(k3,k3.server.CHANNEL_ID['LINE_TIMELINE'])
k3.log("Auth Token : " + str(k3.authToken))
print ("Welcome login k4")  
k4 = LineClient()
#k4 = LineClient(authToken="Token Luu")
channel = LineChannel(k4,k4.server.CHANNEL_ID['LINE_TIMELINE'])
k4.log("Auth Token : " + str(k4.authToken))
print ("Welcome login k5")  
k5 = LineClient()
#k5 = LineClient(authToken="Token Luu")
channel = LineChannel(k5,k5.server.CHANNEL_ID['LINE_TIMELINE'])
k5.log("Auth Token : " + str(k5.authToken))
print ("Welcome login k6")  
k6 = LineClient()
#k6 = LineClient(authToken="Token Luu")
channel = LineChannel(k6,k6.server.CHANNEL_ID['LINE_TIMELINE'])
k6.log("Auth Token : " + str(k6.authToken))
print ("Welcome login k7")  
k7 = LineClient()
#k7 = LineClient(authToken="Token Luu")
channel = LineChannel(k7,k7.server.CHANNEL_ID['LINE_TIMELINE'])
k7.log("Auth Token : " + str(k7.authToken))
print ("Welcome login k8")  
k8 = LineClient()
#k8 = LineClient(authToken="Token Luu")
channel = LineChannel(k8,k8.server.CHANNEL_ID['LINE_TIMELINE'])
k8.log("Auth Token : " + str(k8.authToken))
print ("Welcome login k9")  
k9 = LineClient()
#k9 = LineClient(authToken="Token Luu")
channel = LineChannel(k9,k9.server.CHANNEL_ID['LINE_TIMELINE'])
k9.log("Auth Token : " + str(k9.authToken))
print ("Welcome k10")  
k10 = LineClient()
#k10 = LineClient(authToken="Token Luu")
channel = LineChannel(k10,k10.server.CHANNEL_ID['LINE_TIMELINE'])
k10.log("Auth Token : " + str(k10.authToken))
print ("Welcome login ghost")  
sw = LineClient()
#sw = LineClient(authToken="Token Luu")
channel = LineChannel(sw,sw.server.CHANNEL_ID['LINE_TIMELINE'])
sw.log("Auth Token : " + str(sw.authToken))

print ("รєใғв๏ҭ вұ: ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱")

#ubah mid di dalem admin,owner,creator.json dengan mid kalian
poll = LinePoll(boy)
call = boy
creator = ["Mid Luu"]
owner = ["Mid Luu"]
admin = ["Mid Luu"]
staff = ["Mid Luu"]
mid = boy.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Imid = k9.getProfile().mid
Jmid = k10.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [boy,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,sw]
ABC = [boy,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
Boy = admin + staff + creator

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

boyProfile = boy.getProfile()
myProfile["displayName"] = boyProfile.displayName
myProfile["statusMessage"] = boyProfile.statusMessage
myProfile["pictureStatus"] = boyProfile.pictureStatus

responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
responsename = sw.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.01)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(0,1)
        restartBot()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "ҭ๏ҭคใ рєกงђมกī гม๓คђ「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Pesan Sider Luu\n\n╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Welcome Message Luu\n\n╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\n๔ī งг๏มр "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12842273","STKPKGID":"1318245","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Leave Message Luu\n\n╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\n๔คгī งг๏มр "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12690685","STKPKGID":"1314362","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,10,7)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = boy.getAllContactIds()
        gid = boy.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"❂͜͡☬➣ ♩ค๓ : "+datetime.strftime(timeNow,'%H:%M:%S')+" ฬīв\n❂͜͡☬➣ งг๏มр : "+str(len(gid))+"\n❂͜͡☬➣ ҭє๓คก : "+str(len(teman))+"\n❂͜͡☬➣ єхрīгє๔ : In "+hari+"\n❂͜͡☬➣ ⅴєгรī๏ก : рұҭђ๏ก3\n❂͜͡☬➣ ҭค๓งงคใ : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n❂͜͡☬➣ гมกҭī๓є : \n • "+bot
        boy.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═══════════════════════╗" + "\n" + \
                  "      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►" + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·๓єกม·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Help\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 2\n" + \
                  "╠❂͜͡☬➣ " + key + "Help bot\n" + \
                  "╠❂͜͡☬➣ " + key + "Meme\n" + \
                  "╠❂͜͡☬➣ " + key + "Me\n" + \
                  "╠❂͜͡☬➣ " + key + "Mymid\n" + \
                  "╠❂͜͡☬➣ " + key + "Mid「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Info 「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "K 「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mb\n" + \
                  "╠❂͜͡☬➣ " + key + "Stat\n" + \
                  "╠❂͜͡☬➣ " + key + "Penyewa\n" + \
                  "╠❂͜͡☬➣ " + key + "Abo\n" + \
                  "╠❂͜͡☬➣ " + key + "Poin\n" + \
                  "╠❂͜͡☬➣ " + key + "Run\n" + \
                  "╠❂͜͡☬➣ " + key + "Creat\n" + \
                  "╠❂͜͡☬➣ " + key + "Bro\n" + \
                  "╠❂͜͡☬➣ " + key + "Speed/Sp\n" + \
                  "╠❂͜͡☬➣ " + key + "Sr\n" + \
                  "╠❂͜͡☬➣ " + key + "Tag/ 😆\n" + \
                  "╠❂͜͡☬➣ " + key + "sob\n" + \
                  "╠❂͜͡☬➣ " + key + "lur\n" + \
                  "╠❂͜͡☬➣ " + key + "Gi\n" + \
                  "╠❂͜͡☬➣ " + key + "Op\n" + \
                  "╠❂͜͡☬➣ " + key + "Cl\n" + \
                  "╠❂͜͡☬➣ " + key + "Url\n" + \
                  "╠❂͜͡☬➣ " + key + "Rjt\n" + \
                  "╠❂͜͡☬➣ " + key + "Gl\n" + \
                  "╠❂͜͡☬➣ " + key + "Igp「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ime「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lu「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lu\n" + \
                  "╠❂͜͡☬➣ " + key + "S「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ufoto\n" + \
                  "╠❂͜͡☬➣ " + key + "Ugr\n" + \
                  "╠❂͜͡☬➣ " + key + "Ubot\n" + \
                  "╠❂͜͡☬➣ " + key + "Bc:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ђīвมгคก·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Musik:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Musik2:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Playlist「Nama Penyanyi」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ytmp4:「Judul Video\n" + \
                  "╠❂͜͡☬➣ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "╠❂͜͡☬➣ " + key + "1cak\n" + \
                  "╠❂͜͡☬➣ " + key + "Profilesmule:「ID Smule」\n" + \
                  "╠❂͜͡☬➣ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "╠❂͜͡☬➣ " + key + "Gimage:「Keyword」\n" + \
                  "╠❂͜͡☬➣ " + key + "Img food:「Nama Makanan」\n" + \
                  "╠❂͜͡☬➣ " + key + "Cekig:「ID IG」\n" + \
                  "╠❂͜͡☬➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠❂͜͡☬➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamtag「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╔═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·рг๏ҭєςҭ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Nt「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Dp「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Pu「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Pj「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Pk「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Pc「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Pi「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "As「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Dg「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Tl「on/off」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·รєҭҭīกงร·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Un「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Jointicket「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Str「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Re「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Rg「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Contact「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autojoin「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoadd「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Wl「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Simi「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoleave「on/off」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ค๔๓īก·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Admin:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Admin:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Staff:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Staff:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Adm「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Admd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Owa「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Owd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Botadd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Botdell「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Fresh\n" + \
                  "╠❂͜͡☬➣ " + key + "Lb\n" + \
                  "╠❂͜͡☬➣ " + key + "La\n" + \
                  "╠❂͜͡☬➣ " + key + "Lp\n" + \
                  "╠❂͜͡☬➣ кєҭīк「 ғгєรђ」♩īкค รม๔คђ\n╠❂͜͡☬➣ ๓єกงงมกคкคก ς๏๓๓คก๔ ๔ī คҭค๔\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►" + "\n" + \
                  "╚═══════════════════════╝" 
    return helpMessage2
    boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
    
  
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔═══════════════════════╗" + "\n" + \
                  "     ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣ " + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·в๏ҭ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Mytoken\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek sider\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek spam\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek pesan\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek respon\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek welcome\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek leave\n" + \
                  "╠❂͜͡☬➣ " + key + "Set si:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set spam:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set pesan:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set re:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set wl:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set leave:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mme:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "1na:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "2na:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "1up「Kirim fotonya」\n" + \
                  "╠❂͜͡☬➣ " + key + "2up「Kirim fotonya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠❂͜͡☬➣ " + key + "St:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "St「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Sc:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Sc\n" + \
				  "╠❂͜͡☬➣ " + key + "Ufoto\n" + \
                  "╠❂͜͡☬➣ " + key + "Ugrup\n" + \
                  "╠❂͜͡☬➣ " + key + "Ubot\n" + \
                  "╠❂͜͡☬➣ " + key + "Bc:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
				  "╠❂͜͡☬➣ " + key + "Self「on/off」\n" + \
				  "╠❂͜͡☬➣ " + key + "Hc\n" + \
                  "╠❂͜͡☬➣ " + key + "Rc\n" + \
				  "╠❂͜͡☬➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·вใคςкใīรҭ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Blc\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Banlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkbanlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Cb\n" + \
                  "╠❂͜͡☬➣ " + key + "Fresh\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage3
    boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
    
def infomeme():
    helpMessage4 = """
╔═══════════════════════╗
       ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►
╚═══════════════════════╝
╔═══════════════════════╗
    ◄]·✪·ใīรҭ ๓є๓є·✪·[►
╠═══════════════════════╝
╠❂͜͡☬➣ Buzz
╠❂͜͡☬➣ Spongebob
╠❂͜͡☬➣ Patrick
╠❂͜͡☬➣ Doge
╠❂͜͡☬➣ Joker
╠❂͜͡☬➣ Xzibit
╠❂͜͡☬➣ You_tried
╠❂͜͡☬➣ cb
╠❂͜͡☬➣ blb
╠❂͜͡☬➣ wonka
╠❂͜͡☬➣ keanu
╠❂͜͡☬➣ cryingfloor
╠❂͜͡☬➣ disastergirl
╠❂͜͡☬➣ facepalm
╠❂͜͡☬➣ fwp
╠❂͜͡☬➣ grumpycat
╠❂͜͡☬➣ captain
╠❂͜͡☬➣ mmm
╠❂͜͡☬➣ rollsafe
╠❂͜͡☬➣ sad-obama
╠❂͜͡☬➣ sad-clinton
╠❂͜͡☬➣ aag
╠❂͜͡☬➣ sarcasticbear
╠❂͜͡☬➣ sk
╠❂͜͡☬➣ sparta
╠❂͜͡☬➣ sad
╠❂͜͡☬➣ contoh:
╠❂͜͡☬➣ Meme@buzz@lu tau?@gatau
╠═══════════════════════╗
      ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣·[►
╚═══════════════════════╝
"""
    return helpMessage4
    boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if boy.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            boy.reissueGroupTicket(op.param1)
                            X = boy.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = boy.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            boy.updateGroup(X)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = k1.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                k1.updateGroup(X)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    k2.updateGroup(X)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = k3.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        k3.updateGroup(X)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = k4.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            k4.updateGroup(X)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = k5.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                k5.updateGroup(X)
                                    except:
                                        pass

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if k6.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            k6.reissueGroupTicket(op.param1)
                            X = k6.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = k6.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            k6.updateGroup(X)
                except:
                    try:
                        if k7.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k7.reissueGroupTicket(op.param1)
                                X = k7.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = k7.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                k7.updateGroup(X)
                    except:
                        try:
                            if k8.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k8.reissueGroupTicket(op.param1)
                                    X = k8.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = k8.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    k8.updateGroup(X)
                        except:
                            try:
                                if k9.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k9.reissueGroupTicket(op.param1)
                                        X = k9.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = k9.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        k9.updateGroup(X)
                            except:
                                try:
                                    if k10.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k10.reissueGroupTicket(op.param1)
                                            X = k10.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            k10.updateGroup(X)
                                except:
                                    try:
                                        if randon.choice(ABC).getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                random.choice(ABC).reissueGroupTicket(op.param1)
                                                X = random.choice(ABC).getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).updateGroup(X)
                                    except:
                                        pass

        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1)
                k3.leaveRoom(op.param1)
                k4.leaveRoom(op.param1)  
                k5.leaveRoom(op.param1)
                k6.leaveRoom(op.param1)
                k7.leaveRoom(op.param1)
                k8.leaveRoom(op.param1)
                k9.leaveRoom(op.param1)
                k10.leaveRoom(op.param1)   
        if op.type == 24:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1)
                k3.leaveRoom(op.param1)
                k4.leaveRoom(op.param1)  
                k5.leaveRoom(op.param1)
                k6.leaveRoom(op.param1)
                k7.leaveRoom(op.param1)
                k8.leaveRoom(op.param1)
                k9.leaveRoom(op.param1)
                k10.leaveRoom(op.param1)        
                
        if op.type == 5:
              if wait["autoAdd"] == True:
                  boy.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "ђคīī ", ", ҭєгī๓ค кครīђ รม๔คђ ค๔๔ รคұค")
                  boy.sendText(op.param1, wait["message"])
                  boy.sendContact(op.param1,"uf6b78cccb67849b1f543d1f838752049")
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"รєใค๓คҭҭīกงงคใ\n Group " +str(ginfo.name))
                        boy.leaveGroup(op.param1)
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Hai " + str(ginfo.name))
                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.acceptGroupInvitation(op.param1)                     
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k5.leaveGroup(op.param1)
                    else:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k6.leaveGroup(op.param1)
                    else:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k7.leaveGroup(op.param1)
                    else:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                        k8.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                        k8.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k9.leaveGroup(op.param1)
                    else:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k10.leaveGroup(op.param1)
                    else:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = boy.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            boy.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k1.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k4.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k4.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k5.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k5.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k6.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k6.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k7.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k7.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k8.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k8.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k9.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k9.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k10.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k10.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k1.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k1.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
#+++++++++++++++++Bot Backup +++++++++++++++++++++++++#
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        boy.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.findAndAddContactsByMid(op.param3)
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            boy.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.findAndAddContactsByMid(op.param3)
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                boy.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.findAndAddContactsByMid(op.param3)
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    boy.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.findAndAddContactsByMid(op.param3)
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        boy.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                    	pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.findAndAddContactsByMid(op.param3)
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        boy.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.findAndAddContactsByMid(op.param3)
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            boy.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.findAndAddContactsByMid(op.param3)
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                boy.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k9.findAndAddContactsByMid(op.param3)
                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                    boy.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.findAndAddContactsByMid(op.param3)
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        boy.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                    	pass
                return
#_________________________^^^^^^^^__________________________________
            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.findAndAddContactsByMid(op.param3)
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.findAndAddContactsByMid(op.param3)
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.findAndAddContactsByMid(op.param3)
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.findAndAddContactsByMid(op.param3)
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.findAndAddContactsByMid(op.param3)
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.findAndAddContactsByMid(op.param3)
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.findAndAddContactsByMid(op.param3)
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k9.findAndAddContactsByMid(op.param3)
                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.findAndAddContactsByMid(op.param3)
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.findAndAddContactsByMid(op.param3)
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
#________________________(^_^)_________________________________
            if Bmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.findAndAddContactsByMid(op.param3)
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.findAndAddContactsByMid(op.param3)
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.findAndAddContactsByMid(op.param3)
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                    k6.findAndAddContactsByMid(op.param3)
                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
            if Bmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.findAndAddContactsByMid(op.param3)
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.findAndAddContactsByMid(op.param3)
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.findAndAddContactsByMid(op.param3)
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.findAndAddContactsByMid(op.param3)
                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.findAndAddContactsByMid(op.param3)
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.findAndAddContactsByMid(op.param3)
                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
#______________________Cmid_______________________________________
            if Cmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.findAndAddContactsByMid(op.param3)
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.findAndAddContactsByMid(op.param3)
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.findAndAddContactsByMid(op.param3)
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.findAndAddContactsByMid(op.param3)
                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.findAndAddContactsByMid(op.param3)
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                            k9.findAndAddContactsByMid(op.param3)
                                            k9.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.findAndAddContactsByMid(op.param3)
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            boy.kickoutFromGroup(op.param1,[op.param2])
                            boy.findAndAddContactsByMid(op.param3)
                            boy.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.findAndAddContactsByMid(op.param3)
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.findAndAddContactsByMid(op.param3)
                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#^^^^^^^^^^^^^^^^^^Dmid^^^^^^^^^^^^^^^^^^^^^^^
            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.findAndAddContactsByMid(op.param3)
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.findAndAddContactsByMid(op.param3)
                            k6.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                                k7.findAndAddContactsByMid(op.param3)
                                k7.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.findAndAddContactsByMid(op.param3)
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.findAndAddContactsByMid(op.param3)
                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.findAndAddContactsByMid(op.param3)
                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                            k4.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        boy.kickoutFromGroup(op.param1,[op.param2])
                        boy.findAndAddContactsByMid(op.param3)
                        boy.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.findAndAddContactsByMid(op.param3)
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.findAndAddContactsByMid(op.param3)
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.findAndAddContactsByMid(op.param3)
                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#Emid_______
            if Emid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.findAndAddContactsByMid(op.param3)
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.findAndAddContactsByMid(op.param3)
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.findAndAddContactsByMid(op.param3)
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k9.findAndAddContactsByMid(op.param3)
                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.findAndAddContactsByMid(op.param3)
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            boy.kickoutFromGroup(op.param1,[op.param2])
                                            boy.findAndAddContactsByMid(op.param3)
                                            boy.inviteIntoGroup(op.param1,[op.param3])
                                            k5.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.findAndAddContactsByMid(op.param3)
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.findAndAddContactsByMid(op.param3)
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.findAndAddContactsByMid(op.param3)
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#Fmid^^^^^^
            if Fmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.findAndAddContactsByMid(op.param3)
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.findAndAddContactsByMid(op.param3)
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.findAndAddContactsByMid(op.param3)
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.findAndAddContactsByMid(op.param3)
                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                    k6.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        boy.kickoutFromGroup(op.param1,[op.param2])
                                        boy.findAndAddContactsByMid(op.param3)
                                        boy.inviteIntoGroup(op.param1,[op.param3])
                                        k6.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k1.findAndAddContactsByMid(op.param3)
                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                            k6.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Fmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.findAndAddContactsByMid(op.param3)
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.findAndAddContactsByMid(op.param3)
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.findAndAddContactsByMid(op.param3)
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                            	pass
                return
#Gmid_____
            if Gmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.findAndAddContactsByMid(op.param3)
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.findAndAddContactsByMid(op.param3)
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.findAndAddContactsByMid(op.param3)
                                k10.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    boy.kickoutFromGroup(op.param1,[op.param2])
                                    boy.findAndAddContactsByMid(op.param3)
                                    boy.inviteIntoGroup(op.param1,[op.param3])
                                    k7.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.findAndAddContactsByMid(op.param3)
                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                        k7.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.findAndAddContactsByMid(op.param3)
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            k7.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Gmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.findAndAddContactsByMid(op.param3)
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.findAndAddContactsByMid(op.param3)
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.findAndAddContactsByMid(op.param3)
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                    k6.findAndAddContactsByMid(op.param3)
                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                    k7.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#Hmid^^^^
            if Hmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.findAndAddContactsByMid(op.param3)
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.findAndAddContactsByMid(op.param3)
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                boy.kickoutFromGroup(op.param1,[op.param2])
                                boy.findAndAddContactsByMid(op.param3)
                                boy.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.findAndAddContactsByMid(op.param3)
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.findAndAddContactsByMid(op.param3)
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.findAndAddContactsByMid(op.param3)
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k8.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Hmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.findAndAddContactsByMid(op.param3)
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.findAndAddContactsByMid(op.param3)
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.findAndAddContactsByMid(op.param3)
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.findAndAddContactsByMid(op.param3)
                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#(Imid)_________
            if Imid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.findAndAddContactsByMid(op.param3)
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            boy.kickoutFromGroup(op.param1,[op.param2])
                            boy.findAndAddContactsByMid(op.param3)
                            boy.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.findAndAddContactsByMid(op.param3)
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.findAndAddContactsByMid(op.param3)
                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                    k9.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.findAndAddContactsByMid(op.param3)
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.findAndAddContactsByMid(op.param3)
                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                            k9.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Imid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.findAndAddContactsByMid(op.param3)
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.findAndAddContactsByMid(op.param3)
                            k6.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                                k7.findAndAddContactsByMid(op.param3)
                                k7.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.findAndAddContactsByMid(op.param3)
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    k9.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#Jmid ______
            if Jmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        boy.kickoutFromGroup(op.param1,[op.param2])
                        boy.findAndAddContactsByMid(op.param3)
                        boy.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.findAndAddContactsByMid(op.param3)
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.findAndAddContactsByMid(op.param3)
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.findAndAddContactsByMid(op.param3)
                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                    k10.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.findAndAddContactsByMid(op.param3)
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.findAndAddContactsByMid(op.param3)
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            k10.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return
            if Jmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.findAndAddContactsByMid(op.param3)
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.findAndAddContactsByMid(op.param3)
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.findAndAddContactsByMid(op.param3)
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k9.findAndAddContactsByMid(op.param3)
                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                    k10.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                	pass
                return
#++++++++++++++++++++++++Protect Kick +++++++++++++++++++

        if op.type == 19:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in protectkick:
                     wait["blacklist"][op.param2] = True
                     G = random.choice(ABC).getGroup(op.param1)
                     random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                     k1.findAndAddContactsByMid(op.param3)
                     k1.inviteIntoGroup(op.param1,[op.param3])
                 else:
                   pass
              except:
                try:
                    G = random.choice(ABC).getGroup(op.param1)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    k2.findAndAddContactsByMid(op.param3)
                    k2.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                except:
                    pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = boy.getGroup(op.param1)
                contact = boy.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                boy.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = boy.getGroup(op.param1)
                contact = boy.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                boy.sendImageWithURL(op.param1, image)

#++++++++++++++++++++++++Protect Join ++++++++++++++++/
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        boy.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#===========Accepet===========#

            if op.param3 in mid:
                if op.param2 in Bots:
                    boy.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param3 in Amid:
                if op.param2 in Bots:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Bots:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bots:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bots:
                    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bots:
                    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Bots:
                    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Bots:
                    k7.acceptGroupInvitation(op.param1)                    
            if op.param3 in Hmid:
                if op.param2 in Bots:
                    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Bots:
                    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Bots:
                    k10.acceptGroupInvitation(op.param1)

#--------------------------------------------------------
            if op.param3 in mid:
                            if op.param2 in Amid:
                                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Bmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Cmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Dmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Emid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Fmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Gmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Hmid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Imid:
		                boy.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Jmid:
		                boy.acceptGroupInvitation(op.param1)

#--------------------------------------------------------
            if op.param3 in Amid:
                            if op.param2 in Dmid:
                                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Bmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Cmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Dmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Emid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Fmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Gmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Hmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Imid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Jmid:
		                k1.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
                            if op.param2 in Fmid:
                                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Emid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Cmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Dmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Emid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Fmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Gmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Hmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Imid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Jmid:
		                k2.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
                            if op.param2 in Dmid:
                                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Bmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Amid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Dmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Emid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Fmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Gmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Hmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Imid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Jmid:
		                k3.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Dmid:
                            if op.param2 in Fmid:
                                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Bmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Cmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Amid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Emid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Fmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Gmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Hmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Imid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Jmid:
		                k4.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Emid:
                            if op.param2 in Bmid:
                                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Bmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Cmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Dmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Amid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Fmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Gmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Hmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Imid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Jmid:
		                k5.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Fmid:
                            if op.param2 in Fmid:
                                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Bmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Cmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Dmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Emid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Jmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Gmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Hmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Imid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Jmid:
		                k6.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Gmid:
                            if op.param2 in Fmid:
                                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Bmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Cmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Dmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Emid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Hmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Imid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)               
#--------------------------------------------------------
            if op.param3 in Hmid:
                            if op.param2 in Fmid:
                                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Bmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Cmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Dmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Emid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Fmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Gmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Bmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Imid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Jmid:
		                k8.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Imid:
                            if op.param2 in Gmid:
                                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Bmid:
		                kI.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Cmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Dmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Emid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Fmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Gmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Hmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Dmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Jmid:
		                k9.acceptGroupInvitation(op.param1)
#___________batas ____________
            if op.param3 in Jmid:
                            if op.param2 in Imid:
                                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Bmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Cmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Dmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Emid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Fmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Gmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Hmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Dmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Amid:
		                k10.acceptGroupInvitation(op.param1)

#===========Cancel============#
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "BERHASIL LIKE BY ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱"
                            boy.sendMessage(to, str(ret_))
                            boy.sendMessage(msg.to, None, contentMetadata={"STKID":"17225909","STKPKGID":"1456919","STKVER":"1"}, contentType=7) 
                            channel.like(url[25:58], url[66:], likeType=1001)
                            channel.comment(url[25:58], url[66:], wait["message"])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(ABC).updateGroup(G)
                        invsend = 0
                        Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = random.choice(ABC).getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        random.choice(ABC).updateGroup(X)
            except:
                pass
       
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        boy.inviteIntoGroup(op.param1,[Zmid])
                        boy.inviteIntoGroup(op.param1,[admin])
                    else:
                       pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(ABC).sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

#___________________________________________________
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = boy.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            boy.sendMessage(msg.to, "「คฬคร кīкīใ в๏รร... ђคрมร вใ ๔มใม вคгม īกⅴīҭє ใคงī в๏รร...!!!」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                fira = boy.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                fa = str(fira.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':fira.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                wait["invite"] = False
                                break
                            except:
                                boy.sendText(msg.to,"ใī๓īҭ в๏รร...!!!")
                                wait["invite"] = False
                                break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            boy.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                boy.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    boy.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break

#_______________________________________ __________

        if op.type == 32:
            if op.param1 in protectantijs:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            boy.findAndAddContactsByMid(op.param1,[Zmid])
                            boy.kickoutFromGroup(op.param1,[op.param2])
                            boy.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                boy.findAndAddContactsByMid(op.param1,[Zmid])
                                boy.kickoutFromGroup(op.param1,[op.param2])
                                boy.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                boy.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if op.param3 in mid: #Kalo Admin ke Kick
              if op.param2 in Bots:
                pass
              if op.param2 in mid:
                pass
              else:
                  random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                  boy.inviteIntoGroup(op.param1,[op.param3])                
            if op.param3 in Zmid: #Akun Utama Ke Kick
                G = random.choice(ABC).getGroup(op.param1)
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(ABC).updateGroup(G)
                Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                random.choice(ABC).updateGroup(G)
                random.choice(ABC).updateGroup(G)
                wait["blacklist"][op.param2] = True

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                            random.choice(ABC).inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                                random.choice(ABC).inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                            random.choice(ABC).inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                                random.choice(ABC).inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                            random.choice(ABC).inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                                random.choice(ABC).inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                        random.choice(ABC).inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                            random.choice(ABC).inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                                random.choice(ABC).inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                        random.choice(ABC).inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                            random.choice(ABC).inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                                random.choice(ABC).inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                        random.choice(ABC).inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                            random.choice(ABC).inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                                random.choice(ABC).inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["AFreadPoint"]:
                   if op.param2 in Setmain["AFreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["AFreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = boy.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = boy.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        boy.sendImageWithURL(op.param1, image)
                        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12842257","STKPKGID":"1318245","STKVER":"1"}, contentType=7)
                        
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n❂͜͡☬➣ Pengirim : "
                                ret_ = "\n❂͜͡☬➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂͜͡☬➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Boy.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Boy.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "\n❂͜͡☬➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂͜͡☬➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂͜͡☬➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂͜͡☬➣ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "\n❂͜͡☬➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂͜͡☬➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂͜͡☬➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                                boy.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               boy.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   contact = boy.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, wait["Respontag"])
                           boy.sendImageWithURL(msg.to,image)
                           boy.sendMessage(msg.to, None, contentMetadata={"STKID":"12690684","STKPKGID":"1314362","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           boy.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           boy.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, "Jangan tag saya....")
                           boy.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"「Cek ID Sticker」\n❂͜͡☬➣ STKID : " + msg.contentMetadata["STKID"] + "\n❂͜͡☬➣ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❂͜͡☬➣ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"\n❂͜͡☬➣ Nama : " + msg.contentMetadata["displayName"] + "\n❂͜͡☬➣ MID : " + msg.contentMetadata["mid"] + "\n❂͜͡☬➣ Status : " + contact.statusMessage + "\n❂͜͡☬➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)


        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = boy.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n❂͜͡☬➣ Sticker ID : {}".format(stk_id)
                   ret_ += "\n❂͜͡☬➣ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n❂͜͡☬➣ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n❂͜͡☬➣ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n❂͜͡☬➣ By @⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = boy.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"\n❂͜͡☬➣ Nama : " + msg.contentMetadata["displayName"] + "\n❂͜͡☬➣ MID : " + msg.contentMetadata["mid"] + "\n❂͜͡☬➣ Status : " + contact.statusMessage + "\n❂͜͡☬➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        boy.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan anggota 🐲 รєใғв๏ҭ вұ: ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱ 🐲")
#===========ADD STAFF============#
                 if msg._from in owner:
                  if wait["addowner"] == True:
                    if msg.contentMetadata["mid"] in owner:
                        boy.sendMessage(msg.to,"Contact itu sudah jadi owner")
                        wait["addowner"] = True
                    else:
                        owner.append(msg.contentMetadata["mid"])
                        wait["addowner"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke owner")
                 if wait["dellowner"] == True:
                    if msg.contentMetadata["mid"] in owner:
                        owner.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"Berhasil menghapus dari owner")
                        wait["dellowner"] = True
                    else:
                        wait["dellowner"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan owner")
#===========ADD ADMIN============#
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        boy.sendMessage(msg.to,"ς๏กҭคςҭ īҭม รม๔คђ ♩ค๔ī ค๔๓īก")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        boy.sendMessage(msg.to," вєгђครīใ ๓єกค๓вคђкคก кє ค๔๓īก")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"вєгђครīใ ๓єกงђคрมร ๔คгī ค๔๓īก")
                    else:
                        wait["delladmin"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan admin")
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di Talkban")


#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = boy.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            boy.sendMessage(msg.to, "вєгђครīใ ๓єกค๓вคђкคก ғ๏ҭ๏")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = boy.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     boy.updateGroupPicture(msg.to, path)
                     boy.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ งг๏มр")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["AFfoto"]:
                            path = boy.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][mid]
                            boy.updateProfilePicture(path)
                            boy.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["AFfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Bmid in Setmain["AFfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Cmid in Setmain["AFfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Dmid in Setmain["AFfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Emid in Setmain["AFfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Fmid in Setmain["AFfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Gmid in Setmain["AFfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Hmid in Setmain["AFfoto"]:
                            path = k8.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Hmid]
                            k8.updateProfilePicture(path)
                            k8.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Imid in Setmain["AFfoto"]:
                            path = k9.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Imid]
                            k9.updateProfilePicture(path)
                            k9.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")
                        elif Jmid in Setmain["AFfoto"]:
                            path = k10.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Jmid]
                            k10.updateProfilePicture(path)
                            k10.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")                            
                        elif Zmid in Setmain["AFfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"ғ๏ҭ๏ вєгђครīใ ๔īгมвคђ")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)
                     path6 = k6.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     pathsw = sw.downloadObjectMsg(msg_id)                     
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k2.updateProfilePicture(path2)
                     k2.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k6.updateProfilePicture(path6)
                     k6.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k8.updateProfilePicture(path8)
                     k8.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k9.updateProfilePicture(path9)
                     k9.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")
                     k10.updateProfilePicture(path10)
                     k10.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")               
                     sw.updateProfilePicture(pathsw)
                     sw.sendMessage(msg.to, "вєгђครīใ ๓єกงมвคђ ғ๏ҭ๏ рг๏ғīใє в๏ҭ")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        boy.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage = help()
                               helpMessage1 = help1()
                               boy.sendMessage(msg.to, "Help \nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to,str(helpMessage))
                               boy.sendMessage(msg.to,str(helpMessage1))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                boy.sendMessage(msg.to, "รєใғв๏ҭ ๔īคкҭīғкคก")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                boy.sendMessage(msg.to, "รєใғв๏ҭ ๔īก๏กคкҭīғкคก")

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage2 = help2()
                               boy.sendMessage(msg.to, "Help Bots\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage2))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n ╚═══════════════════════╝")
                               boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage3 = helpbot()
                               boy.sendMessage(msg.to, "Help Bots\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage3))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n ╚═══════════════════════╝")
                               boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
                               
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage4 = infomeme()
                               boy.sendMessage(msg.to, "Help Fun\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage4))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")

                        if cmd == "un on":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "๔єҭєкรī มกรєก๔ ๔īคкҭīғкคก")
                                
                        if cmd == "un off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "๔єҭєкรī มกรєก๔ ๔īก๏กคкҭīғкคก")                                

                        elif cmd == "stat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━━━━━━\n┃┃          ❂͜͡☬➣ ร ҭ ค ҭ ม ร ❂͜͡☬➣\n┃┣━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["unsend"] == True: md+="┃┃❂͜͡☬➣ ✔️ มกรєก๔「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ มกรєก๔「OFF」\n"                                
                                if wait["sticker"] == True: md+="┃┃❂͜͡☬➣ ✔️ รҭīςкєг「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ รҭīςкєг「OFF」\n"
                                if wait["contact"] == True: md+="┃┃❂͜͡☬➣ ✔️ ς๏กҭคςҭ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ς๏กҭคςҭ「OFF」\n"
                                if wait["talkban"] == True: md+="┃┃❂͜͡☬➣ ✔️ ҭคใквคก「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ҭคใквคก「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃┃❂͜͡☬➣ ✔️ ก๏ҭคง「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ก๏ҭคง「OFF」\n"
                                if wait["detectMention"] == True: md+="┃┃❂͜͡☬➣ ✔️ гєรр๏ก「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ гєรр๏ก「OFF」\n"
                                if wait["Mentiongift"] == True: md+="┃┃❂͜͡☬➣ ✔️ гєรр๏กงīғҭ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ гєรр๏กงīғҭ「OFF」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃❂͜͡☬➣ ✔️ คมҭ๏♩๏īก「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ คมҭ๏♩๏īก「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃❂͜͡☬➣ ✔️ ♩๏īกҭīςкєҭ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ♩๏īกҭīςкєҭ「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃❂͜͡☬➣ ✔️ คมҭ๏ค๔๔「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ คมҭ๏ค๔๔「OFF」\n"                                
                                if wait["Timeline"] == True: md+="┃┃❂͜͡☬➣ ✔️ ҭī๓єใīกє「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ҭī๓єใīกє「OFF」\n"
                                if msg.to in welcome: md+="┃┃❂͜͡☬➣ ✔️ ฬєใς๏๓є「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ฬєใς๏๓є「OFF」\n"
                                if msg.to in simisimi: md+="┃┃❂͜͡☬➣ ✔️ รī๓īรī๓ī「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ รī๓īรī๓ī「OFF」\n"                                
                                if wait["autoLeave"] == True: md+="┃┃❂͜͡☬➣ ✔️ คมҭ๏ใєคⅴє「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ คมҭ๏ใєคⅴє「OFF」\n"
                                if msg.to in protectqr: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭมгใ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭมгใ「OFF」\n"
                                if msg.to in protectjoin: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭ♩๏īก「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭ♩๏īก「OFF」\n"
                                if msg.to in protectkick: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭкīςк「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭкīςк「OFF」\n"
                                if msg.to in protectcancel: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭςคกςєใ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭςคกςєใ「OFF」\n"
                                if msg.to in protectinvite: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭīกⅴīҭє「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭīกⅴīҭє「OFF」\n" 
                                if msg.to in protectantijs: md+="┃┃❂͜͡☬➣ ✔️ рг๏ҭєςҭคกҭī♩ร「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ рг๏ҭєςҭคกҭī♩ร「OFF」\n"
                                if msg.to in ghost: md+="┃┃❂͜͡☬➣ ✔️ งђ๏รҭ「ON」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ งђ๏รҭ「OFF」\n"                                                
                                boy.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━━━━━━━━━\n┃┃❧ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃❧ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ┗━━━━━━━━━━━━━━━━━")
                                boy.sendMessage(msg.to,"╔═══════════════════════╗\n ◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝"
)
                                boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")

                                
                        elif cmd == "creat" or text.lower() == 'creat':
                            if msg._from in admin:
                                boy.sendMessage(msg.to,"❂͜͡☬➣ īกī กīђ ςгєคҭ๏г в๏ҭ กұค...!!!") 
                                ma = ""
                                for i in creator:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "abo" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「รєใғв๏ҭ вұ: ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱」\n")
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd.startswith('penyewa'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2025
                                bln = 12    #isi bulannya yg sewa
                                hr = 11    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = boy.getContact(mid)
                                favoritelist = boy.getFavoriteMids()
                                grouplist = boy.getGroupIdsJoined()
                                contactlist = boy.getAllContactIds()
                                blockedlist = boy.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                sw.sendText("ue6d8f9ef8f820fad9c65bbb5d1ec714b", 'Cek dulu')
                                elapsed_time = time.time() - start
                                ryan = boy.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 īกғ๏г๓ครī รєใғв๏ҭ 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「Self Bots 」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               boy.sendMessage1(msg)

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "❂͜͡☬➣Nama : "+str(mi.displayName)+"\n❂͜͡☬➣MID : " +key1)
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "❂͜͡☬➣ กค๓ค : "+str(mi.displayName)+"\n❂͜͡☬➣ ๓ī๔ : " +key1+"\n❂͜͡☬➣ รҭคҭมร : "+str(mi.statusMessage))
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(boy.getContact(key1)):
                                   boy.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   boy.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               boy.sendMessage1(msg)

                        elif text.lower() == "hc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   boy.removeAllMessages(op.param2)
                                   boy.sendText(msg.to,'ςђคҭ ๔īђคрมร в๏รร...!!!')
                               except:
                                   pass

                        elif text.lower() == "rc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   k1.removeAllMessages(op.param2)
                                   k2.removeAllMessages(op.param2)
                                   k3.removeAllMessages(op.param2)
                                   k4.removeAllMessages(op.param2)
                                   k5.removeAllMessages(op.param2)
                                   k6.removeAllMessages(op.param2)
                                   k7.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   k9.removeAllMessages(op.param2)
                                   k10.removeAllMessages(op.param2)
                                   k1.sendText(msg.to," ςђคҭ ๔īвєгรīђкคก в๏รร...!!!")
                               except:
                                   pass

                        elif cmd.startswith("bc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = boy.getGroupIdsJoined()
                               for group in saya:
                                   boy.sendMessage(group,"=======[вг๏คҭςครҭ]=======\n\n"+pesan+"\n\nCreator : ◄]·✪line.me/R/ti/p/~mostarz✪·[►")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   boy.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   boy.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               boy.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "poin":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               boy.sendMessage(msg.to, "гєรҭคгҭ...!!!")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "run":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "в๏ҭ ҭєใคђ คкҭīғ รєใค๓ค" +waktu(eltime)
                               boy.sendMessage(msg.to,bot)
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n ◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")
                            
                        elif cmd == "gi":
                          if msg._from in admin:
                            try:
                                G = boy.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                boy.sendMessage(msg.to, "❂͜͡☬➣ в๏ҭ งг๏มр īกғ๏\n\n ❂͜͡☬➣ กค๓ค งг๏มр : {}".format(G.name)+ "\n❂͜͡☬➣ ī๔ งг๏มр : {}".format(G.id)+ "\n❂͜͡☬➣ рє๓вมคҭ : {}".format(G.creator.displayName)+ "\n❂͜͡☬➣ ฬคкҭม ๔īвมคҭ : {}".format(str(timeCreated))+ "\n❂͜͡☬➣ ♩ม๓ใคђ ๓є๓вєг : {}".format(str(len(G.members)))+ "\n❂͜͡☬➣ ♩ม๓ใคђ рєก๔īกง : {}".format(gPending)+ "\n❂͜͡☬➣ งг๏มр ợг : {}".format(gQr)+ "\n❂͜͡☬➣ งҭ๏มр ҭīςкєҭ : {}".format(gTicket))
                                boy.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                boy.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ig "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "ҭī๔คк ๔īҭє๓มкคก"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "❂͜͡☬➣ в๏ҭ งг๏มр īกғ๏\n"
                                ret_ += "\n❂͜͡☬➣ กค๓ค : {}".format(G.name)
                                ret_ += "\n❂͜͡☬➣ ī๔ : {}".format(G.id)
                                ret_ += "\n❂͜͡☬➣ ςгєคҭ๏г : {}".format(gCreator)
                                ret_ += "\n❂͜͡☬➣ ςгєคҭє๔ Time : {}".format(str(timeCreated))
                                ret_ += "\n❂͜͡☬➣ ๓є๓вєг : {}".format(str(len(G.members)))
                                ret_ += "\n❂͜͡☬➣ рєก๔īกง : {}".format(gPending)
                                ret_ += "\n❂͜͡☬➣ ợг : {}".format(gQr)
                                ret_ += "\n❂͜͡☬➣ ҭīςкєҭ : {}".format(gTicket)
                                ret_ += ""
                                boy.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("ime "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "❂͜͡☬➣ "+ str(no) + ". " + mem.displayName
                                boy.sendMessage(to,"❂͜͡☬➣ กค๓ค งг๏มр : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「ҭ๏ҭคใ %i ๓є๓вєг」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = boy.getGroup(i)
                                if ginfo == group:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
                                    boy.sendMessage(msg.to,"вєгђครīใ кєใมคг ๔คгī งг๏มр " +str(ginfo.name))

                        elif cmd == "fl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getAllContactIds()
                               for i in gid:
                                   G = boy.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ใīรҭ ҭє๓คก ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getGroupIdsJoined()
                               for i in gid:
                                   G = boy.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ใīรҭ งг๏มр ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gl1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"┏━━[ ใīรҭ งг๏มр ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "op":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "มгใ ҭєใคђ ๔īвมкค")

                        elif cmd == "cl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "มгใ ҭєใคђ ๔īҭมҭมр")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = k1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      k1.updateGroup(x)
                                   gurl = k1.reissueGroupTicket(msg.to)
                                   k1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "rjt":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = boy.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      boy.rejectGroupInvitation(gid)
                                  boy.sendMessage(to, "вєгђครīใ ҭ๏ใคк รєвคกұคк {} มก๔คกงคก งг๏มр ".format(str(len(ginvited))))
                              else:
                                  boy.sendMessage(to, "ҭī๔คк ค๔ค มก๔คกงคก ҭєгҭมก๔ค")

#===========BOT UPDATE============#
                        elif cmd == "ugp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                boy.sendMessage(msg.to,"кīгī๓ ғ๏ҭ๏กұค......")

                        elif cmd == "ub":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                k1.sendMessage(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "uf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AFfoto"][mid] = True
                                boy.sendMessage(msg.to,"кīгī๓ ғ๏ҭ๏กұค......")
                                
                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Amid] = True
                                k1.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Bmid] = True
                                k2.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Cmid] = True
                                k3.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Dmid] = True
                                k4.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Emid] = True
                                k5.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Fmid] = True
                                k6.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Gmid] = True
                                k7.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "8up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Hmid] = True
                                k8.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "9up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Imid] = True
                                k9.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                 
                        elif cmd == "10up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Jmid] = True
                                k10.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                                
                        elif cmd == "gup":
                            if msg._from in admin:
                                Setmain["AFfoto"][Zmid] = True
                                sw.sendText(msg.to,"кīгī๓ ғ๏ҭ๏กұค.......")
                               

                        elif cmd.startswith("mme: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boy.getProfile()
                                profile.displayName = string
                                boy.updateProfile(profile)
                                boy.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("1na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("2na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("3na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("4na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("5na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("6na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("7na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("8na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("9na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("10na: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

                        elif cmd.startswith("kna: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"กค๓ค ๔īงคกҭī ♩ค๔ī " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == '😆':
                          if msg._from in admin:
                               group = boy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "lb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"❂͜͡☬➣ ⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️\n\n"+ma+"\nҭ๏ҭคใ「%s」в๏ҭ " %(str(len(Bots))))

                        elif cmd == "la":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"❂͜͡☬➣ ⊰์◉⊱ ค๔๓īก τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏® ⊰์◉⊱™️ BOT\n\n❂͜͡☬➣Creator BOT:\n"+ma+"\n❂͜͡☬➣ค๔๓īก :\n"+mb+"\n❂͜͡☬➣รҭคғғ :\n"+mc+"\n❂͜͡☬➣ҭ๏ҭคใ「%s」❍✯͜͡⊰์◉⊱ ค๔๓īก τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏® ⊰์◉⊱™️✯͜͡❂➣" %(str(len(owner)+len(admin)+len(staff))))
                                boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝")
                                boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")

                        elif cmd == "lp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +boy.getGroup(group).name + "\n"                                    
                                boy.sendMessage(msg.to,"❂͜͡☬➣ ๔гคง๏ก рг๏ҭєςҭī๏ก \n\n❂͜͡☬➣ рг๏ҭєςҭ มгใ :\n"+ma+"\n❂͜͡☬➣ рг๏ҭєςҭ кīςк :\n"+mb+"\n❂͜͡☬➣ рг๏ҭєςҭ ♩๏īก :\n"+md+"\n❂͜͡☬➣ рг๏ҭєςҭ ςคกςєใ :\n"+mc+"\n❂͜͡☬➣ рг๏ҭєςҭ īกⅴīҭє :\n"+me+"\nҭ๏ҭคใ「%s」рг๏ҭєςҭ ұคกง คкҭīғ" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))
                                boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~mostarz✪·[► \n╚═══════════════════════╝")
                                boy.sendContact(to, "uf6b78cccb67849b1f543d1f838752049")

                        elif cmd == "bro":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                boy.sendText(msg.to," คвรєก вг๏ҭђєг'ร...!!!")
                                k1.sendMessage(msg.to,responsename1)
                                k2.sendMessage(msg.to,responsename2)
                                k3.sendMessage(msg.to,responsename3)
                                k4.sendMessage(msg.to,responsename4)
                                k5.sendMessage(msg.to,responsename5)
                                k6.sendMessage(msg.to,responsename6)
                                k7.sendMessage(msg.to,responsename7)
                                k8.sendMessage(msg.to,responsename8)
                                k9.sendMessage(msg.to,responsename9)
                                k10.sendMessage(msg.to,responsename10)
                                k1.sendText(msg.to," รє๓มค ђค๔īг в๏รร...!!!")

                        elif cmd == "sob":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
                                    boy.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)
                                    k5.acceptGroupInvitation(msg.to)
                                    k6.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                    K1.sendText(msg.to, "кīςкєг ๔๏กє รҭคұ ๔ī งг๏มр "+str(G.name))
                                except:
                                    pass
                                
    
                        elif cmd == "lur":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                G = boy.getGroup(msg.to)
                                ginfo = boy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                boy.updateGroup(G)
                                invsend = 0
                                Ticket = boy.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)
                        
                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = boy.getGroup(msg.to)
                                    boy.inviteIntoGroup(msg.to, [Zmid])
                                    boy.sendMessage(msg.to,"งг๏มр「"+str(ginfo.name)+"」 ค๓คก ๔คгī ♩ร ")
                                except:
                                    pass
                        
                        elif cmd == "balik":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                k1.sendText(msg.to, "рค๓īҭ ร๏в คұค๓ ร๏р вมกҭมҭ ... "+str(G.name))
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)
                                k4.leaveGroup(msg.to)
                                k5.leaveGroup(msg.to)
                                k6.leaveGroup(msg.to)
                                k7.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                                
                        elif cmd == "bme":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                G = boy.getGroup(msg.to)
                                boy.sendText(msg.to, "╠❂͜͡☬➣ Bye bye fams "+str(G.name))
                                boy.leaveGroup(msg.to)
                                
                        elif cmd.startswith("lgrup "):
                          if msg._from in owner:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                try:
                                    ginfo = boy.getGroup(group)
                                    gCreator = ginfo.creator.mid
                                    edora = boy.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '๓คคғ ๔īрคкรค кєใมคг '
                                    edor = str(edora.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':edora.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan+zxc + "กєхҭ ๓ค๓рīг ใคงī " 
                                    k1.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    k1.leaveGroup(group)
                                    k2.leaveGroup(group)
                                    k3.leaveGroup(group)
                                    k4.leaveGroup(group)
                                    k5.leaveGroup(group)
                                    k6.leaveGroup(group)
                                    k7.leaveGroup(group)
                                    k8.leaveGroup(group)
                                    k9.leaveGroup(group)
                                    k10.leaveGroup(group)
                                except:
                                    boy.sendMessage(msg.to, "งг๏มр īҭม ҭī๔คк ค๔ค ")
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ginfo = boy.getGroup(group)
                                gCreator = ginfo.creator.mid
                                edor = boy.getContact(gCreator)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'รมкรєร ใєคⅴє งг๏มр\nςгєคҭ๏г :  '
                                edora = str(edor.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':edor.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                ret_ += xpesan +zxc
                                ret_ += "กค๓ค งг๏มр : {}".format(G.name)
                                ret_ += "\nрєก๔īกงค : {}".format(gPending)
                                ret_ += "\n♩ม๓ใคђ ๓є๓вєг : {}".format(str(len(G.members)))
                                boy.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                boy.sendMessage(to, str(e))

                        elif cmd.startswith("pulang "):
                            if msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = boy.getGroupIdsJoined()
                                for i in gid:
                                    h = boy.getGroup(i).name
                                    if h == ng:
                                        k1.sendMessage(i, "รīใคђкคก ค๔๓īก īกⅴīҭє คҭคม ๓ครมккคก кє๓вคใī")
                                        k1.leaveGroup(i)
                                        k2.leaveGroup(i)
                                        k3.leaveGroup(i)
                                        k4.leaveGroup(i)
                                        k5.leaveGroup(i)
                                        k6.leaveGroup(i)
                                        k7.leaveGroup(i)
                                        k8.leaveGroup(i)
                                        k9.leaveGroup(i)
                                        k10.leaveGroup(i)
                                        boy.sendMessage(to,"вєгђครīใ кєใมคг ๔คгī " +h)

                        elif cmd == "kj":
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                ginfo = boy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                boy.updateGroup(G)
                                invsend = 0
                                Ticket = boy.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kb":
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                sw.leaveGroup(msg.to)


                        elif cmd == "sr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = boy.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = boy.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                boy.sendMessage(msg.to, " ❧ в๏ҭ รрєє๔ гєรр๏ก \n\n - งєҭ рг๏ғīใє\n   %.10f\n - งєҭ ς๏กҭคςҭ\n   %.10f\n - งєҭ งг๏มр\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               boy.sendMessage(msg.to, "рг๏งгєร รрєє๔...!!!")
                               elapsed_time = time.time() - start
                               boy.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k1.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k2.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k3.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k4.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k5.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k5.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k6.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k7.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k8.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k9.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               k10.sendMessage(msg.to, "{} ๔єҭīк".format(str(elapsed_time)))
                               boy.sendMessage(msg.to," рг๏งгєรร... รрєє๔ ๔๏กє...!!!")

                        elif cmd == "lu on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['AFreadPoint'][msg.to] = msg_id
                                 Setmain['AFreadMember'][msg.to] = {}
                                 boy.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['AFreadPoint'][msg.to]
                                 del Setmain['AFreadMember'][msg.to]
                                 boy.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu":
                          if msg._from in admin:
                            if msg.to in Setmain['AFreadPoint']:
                                if Setmain['AFreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['AFreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(boy.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        boy.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['AFreadPoint'][msg.to]
                                        del Setmain['AFreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['AFreadPoint'][msg.to] = msg.id
                                    Setmain['AFreadMember'][msg.to] = {}
                                else:
                                    boy.sendMessage(msg.to, "User kosong...")
                            else:
                                boy.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "s on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  boy.sendMessage(msg.to, "ςєк รī๔єг ๔īคкҭīғкคก\n\nҭคกงงคใ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n♩ค๓ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "s off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  boy.sendMessage(msg.to, "ςєк รī๔єг ๔īก๏กคкҭīғкคก\n\nҭคกงงคใ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n♩ค๓ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  boy.sendMessage(msg.to, "รม๔คђ ҭī๔คк คкҭīғ")

#===========Hiburan============#
                        elif cmd.startswith("musik: "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "? Pencarian Musik ?\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n? Total {} Pencarian ?".format(str(len(data["result"])))
                                      boy.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "? Pencarian Musik ?"
                                                         ret_ += "\n? Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n? Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n? Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n? Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n? Tunggu Musiknya Keluar ?"
                                                         boy.sendImageWithURL(to, str(data["result"]["img"]))
                                                         boy.sendMessage(to, str(ret_))
                                                         boy.sendAudioWithURL(to, str(data["result"]["mp3"][0]))


                        elif cmd.startswith("randomnumber: "):                            	
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")  
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                boy.sendMessage(msg.to,"Hasil : "+str(data["url"]))
                                
                                
                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              boy.sendMessage(msg.to, str(hasil))
        
                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://corrykalam.pw/api/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                boy.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                boy.sendMessage(msg.to, str(t))
                                boy.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("playlist "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n❧「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    boy.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            boy.sendMessage(msg.to, str(ret_))
                                            boy.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("lirik "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    boy.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        boy.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                        
        
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        boy.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                boy.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                boy.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                boy.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                            	
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            boy.sendImageWithURL(msg.to, image)
          

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                boy.sendVideoWithURL(msg.to, me)
                                boy.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                boy.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                boy.sendImageWithURL(msg.to, me)
                                boy.sendAudioWithURL(msg.to, shi)
                                boy.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                boy.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                boy.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                boy.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                boy.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "┏━━[ Profile Instagram ]"
                                        ret_ += "\n┃┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n┗━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        boy.sendMessage(to, str(ret_))
                                        boy.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    boy.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            boy.sendMessage(msg.to,"🐚 I N F O R M A S I 🐚\n\n"+"🐚 Date Of Birth : "+lahir+"\n🐚 Age : "+usia+"\n🐚 Ultah : "+ultah+"\n🐚 Zodiak : "+zodiak)

                        elif cmd.startswith("st: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["AFlimit"] = num
                                boy.sendMessage(msg.to,"ҭ๏ҭคใ รрค๓ҭคง ๔īมвคђ ๓єก♩ค๔ī " +strnum)

                        elif cmd.startswith("sc: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                boy.sendMessage(msg.to,"ҭ๏ҭคใ รрค๓ςคใใ ๔īมвคђ ๓єก♩ค๔ī " +strnum)

                        elif cmd.startswith("st "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["AFlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                boy.sendMessage1(msg)
                                            except Exception as e:
                                                boy.sendMessage(msg.to,str(e))
                                    else:
                                        boy.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "sc":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = boy.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                boy.sendMessage(msg.to, "вєгђครīใ ๓єกงīгī๓ {} มก๔คกงคก ςคใใ งг๏มр ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        boy.sendMessage(msg.to,str(e))
                                else:
                                    boy.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      k1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k2.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k3.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k4.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k5.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k6.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k7.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k8.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k9.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k10.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k1.sendMessage(midd, str(Setmain["AFmessage1"]))

                                  
                        elif 'Mbt' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               boy.sendMessage(msg.to,"⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱\n"+boy.authToken)
                               boy.sendMessage(msg.to,"K1\n"+k1.authToken)

#==============================================================================# 
                       

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = k1.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  k1.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = k1.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    k1.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'Wl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wl ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "рєกұค๓вมҭคก รม๔คђ คкҭīғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "ฬєใς๏๓є ๓รง ๔īคкҭīғкคก\n ๔ī งг๏มр : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「๔īคкҭīғкคก」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "ฬєใς๏๓є ๓รง ๔īก๏กคкҭīғкคก\n๔ī งг๏มр : " +str(ginfo.name)
                                    else:
                                         msgs = "рєกұค๓вมҭคก รม๔คђ ҭī๔คк คкҭīғ"
                                    boy.sendMessage(msg.to, "「๔īก๏กคкҭīғкคก」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Pu ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pu ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pk ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pk ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "рг๏ҭєςҭ кīςк รม๔คђ คкҭīғ"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "рг๏ҭєςҭ кīςк ๔īคкҭīғкคก\n๔ī งг๏มр: " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「๔īคкҭī๔кคก」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pj ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pj ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pc ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pc ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Pi ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pi ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'As ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('As ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "คกҭī ♩ร รม๔คђ คкҭīғ "
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "คกҭī ♩ร ๔īคкҭīғкคก\n๔ī งг๏มр : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "๔īคкҭīғкคก\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "คกҭī ♩ร ๔īก๏กคкҭīғкคก\n๔ī งг๏มр : " +str(ginfo.name)
                                    else:
                                         msgs = "คกҭī ♩ร รม๔คђ ҭī๔คк คкҭīғ "
                                    boy.sendMessage(msg.to, "๔īก๏กคкҭīғкคก \n" + msgs)
                                    
                        elif 'Dg ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dg ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "งђ๏รҭ รม๔คђ คкҭīғ "
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "งђ๏รҭ ๔īคкҭīғкคก\n๔ī งг๏มр : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "๔īคкҭīғкคก\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "งђ๏รҭ ๔īก๏กคкҭīғкคก\n๔ī งг๏มр : " +str(ginfo.name)
                                    else:
                                         msgs = "งђ๏รҭ รม๔คђ ๔īก๏กคкҭīғкคก"
                                    boy.sendMessage(msg.to, "๔īก๏กคкҭīғкคก\n" + msgs) 

                        elif 'Dp ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dp ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)                                      
                                  if msg.to in protectcancel:
                                      ginfo = boy.getGroup(msg.to)
                                      msgs = "รҭคҭมร : [ ๏ก]\n๔ī งг๏มр : " +str(ginfo.name)
                                      msgs += "\nรє๓มค รม๔คђ ๔īคкҭīғкคก"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = boy.getGroup(msg.to)
                                      msgs = "รҭคҭมร : [ ON ]\n๔ī งг๏มр : " +str(ginfo.name)
                                      msgs += "\nรє๓มค рг๏ҭєςҭī๏ก ๔īคкҭīғкคก"
                                  boy.sendMessage(msg.to, "「 รҭคҭมร рг๏ҭєςҭī๏ก 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "รҭคҭมร : [ ๏ғғ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nรє๓มค рг๏ҭєςҭī๏ก ๔īก๏กคкҭīғкคก"
                                    else:
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "รҭคҭมร : [ ๏ғғ ]\n๔ī งг๏มр : " +str(ginfo.name)
                                         msgs += "\nรє๓มค рг๏ҭєςҭī๏ก ๔īก๏กคкҭīғкคก"
                                    boy.sendMessage(msg.to, "「 รҭคҭมร рг๏ҭєςҭī๏ก 」\n" + msgs)

#===========KICKOUT============#
                        elif ("N " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = boy.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           boy.updateGroup(G)
                                           invsend = 0
                                           Ticket = boy.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = boy.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           boy.updateGroup(X)
                                       except:
                                           pass

                        elif ("K " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif  text.lower() == "virus" or text.lower () == "Crash":
                          if wait["selfbot"] == True:
                        #    if msg._from in admin:
                              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash!","Kamu asu ngecrash terus!","crash cresh crash cresh, bikin hp orang lag anjing!")
                              ngkol = random.choice(dia)
                              random.choice(ABC).sendText(msg.to,ngkol)
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              random.choice(ABC).sendText(msg.to,"Mampus!")
                              if msg.text in ["!cipok",".desah","!makan","!","?","!kickall",".kickall","Nuke","Cleanse","Ratakan","Mayhem","MB Mayhem","Kick all","kickall","!rata","play",".",","]:
                              	Peringatan = ("Manual kek jangan pake bot.","Cupu lu! Ratain pake bot!","Lain kali liat liat dulu~","ＴＥＲＣＹＤＵＣＫ")
                              Vonis = random.choice(Peringatan)
                              random.choice(ABC).sendText(msg.to, Vonis)
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              
                              # for x in key["MENTIONEES"]:
                            #        targets.append(x["M"])
                             #  for target in targets:
                              #     if target not in Bots:
                               #        try:
                                #           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                 #      except:
                                  #         pass
#===========ADMIN ADD============#
                        elif ("Adm " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"вєгђครīใ ๓єกค๓вคђкคก ค๔๓īก")
                                       except:
                                           pass

                        elif ("Owa " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           owner[target] = True
                                           f=codecs.open('owner.json','w','utf-8')
                                           json.dump(owner, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"вєгђครīใ ๓єกค๓вคђкคก ๏ฬกєг")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           boy.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admd " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"вєгђครīใ ๓єกงђคрมร ค๔๓īก")
                                       except:
                                           pass

                        elif ("Owd " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del owner[target]
                                           f=codecs.open('owner.json','w','utf-8')
                                           json.dump(owner, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"вєгђครīใ ๓єกงђคрมร ๏ฬกєг")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Boy:
                                       try:
                                           Bots.remove(target)
                                           boy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in creator:
                                wait["addadmin"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in creator:
                                wait["delladmin"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'fresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                wait["invite"] = False
                                boy.sendMessage(msg.to,"вєгђครīใ ๔ī гєғгєรђ....!!!")

                        elif cmd == "ca" or text.lower() == 'ca':
                                ma = ""
                                for i in admin:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "nt on" or text.lower() == 'nt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                boy.sendMessage(msg.to,"ก๏ҭคง ๔īคкҭīғкคก")

                        elif cmd == "nt off" or text.lower() == 'nt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                boy.sendMessage(msg.to,"ก๏ҭคง ๔īก๏กคкҭīғкคก")

                        elif cmd == "tl on" or text.lower() == 'tl on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                boy.sendMention(msg.to, "「 Status Timeline 」\nUser \nSilahkan kirim postingannya\nKetik timeline off jika sudah slesai")

                        elif cmd == "tl off" or text.lower() == 'tl off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                boy.sendMention(msg.to, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invi on" or text.lower() == 'invi on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invi off" or text.lower() == 'invi off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                boy.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                boy.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "re on" or text.lower() == 're on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                boy.sendMessage(msg.to,"คมҭ๏ гєรр๏กรє ๔īคкҭīғкคก")

                        elif cmd == "re off" or text.lower() == 're off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                boy.sendMessage(msg.to,"คมҭ๏ гєรр๏กรє ๔īก๏กคкҭīғкคก")
                                
                        elif cmd == "rg on" or text.lower() == 'rg on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                boy.sendMessage(msg.to,"คมҭ๏ гєรр๏กรє งīғҭ ๔īคкҭīғкคก")

                        elif cmd == "rg off" or text.lower() == 'rg off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                boy.sendMessage(msg.to,"คมҭ๏ гєรр๏กรє งīғҭ ๔īก๏กคкҭīғкคก")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                boy.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                boy.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                boy.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                boy.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                boy.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                boy.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "str on" or text.lower() == 'str on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                boy.sendMessage(msg.to,"๔єҭєкรī รҭīςкєг ๔īคкҭīғкคก...!!!")

                        elif cmd == "str off" or text.lower() == 'str off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                boy.sendMessage(msg.to,"๔єҭєςҭ รҭīςкєг ๔ī๓คҭīкคก...!!!")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                boy.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                boy.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = boy.getContact(i)
                                        boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = boy.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              boy.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set wl: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set re: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["AFmessage1"] = spl
                                  boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set si: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  boy.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["AFmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = boy.findGroupByTicket(ticket_id)
                                     boy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     boy.sendMessage(msg.to, "⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱📲 OTW MASUK KE GROUP : %s" % str(group.name))
                                     group1 = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     k1.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     k2.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k3.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     k4.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     k5.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = k6.findGroupByTicket(ticket_id)
                                     k6.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     k6.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     k7.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group8 = k8.findGroupByTicket(ticket_id)
                                     k8.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     k8.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = k9.findGroupByTicket(ticket_id)
                                     k9.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     k9.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group10 = k10.findGroupByTicket(ticket_id)
                                     k10.acceptGroupInvitationByTicket(group10.id,ticket_id)
                                     k10.sendMessage(msg.to, "Masuk : %s" % str(group.name))


    except Exception as error:
        print (error)
def autolike():
    count = 1
    while True:
        try:
           for posts in boy.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   boy.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k10.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          boy.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
