# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:36:16 2024

@author: User
"""

#1/masala 
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
#chiroyli qilib konsolga chiqaring. 
i_lugat ={
    "boolean":"mantiqiy qiymat",
    "float":"o'nlik son",
    "integer":"butun son",
    "string":"matn",
    "del":"O'chirish",
    "for":"qayta qayta bajarish tcikli",
    'if':"agar funktciyasi", 
    'else':'aks holda',
    'in':"ichida",
    'title':"matnni bosh harf qilish",
    'input':"foydalnuvchi qiymatini kiritish",
    'print':"ekranga chqarish",
    'items()':"lugat elementlarini chiqarish",
    "keys()":"lug'at kalitini chiqarish",
    "sorted()":"Sortirovat qilish",
    "value()":"lug'at qiymatini chiqarish",
    "set()":"takrorlashni olib tahslash",
    ".lower()":"matnni kichik harf qilish",
    ".get()":"lug'at ichidan chiqarb, javob berish"
    }

#for k,q in sorted(i_lugat.items()):
#    print(f"{k.title()} - {q}")

#2/ Davlatlar va ularning poytaxtlari lug'atini tuzing. 
#Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
#alifbo ketma-ketligida konsolga chiqaring.     

davlat_poyt = {
    "AQSH":"Vashington D.C.",
    "O'zbekiston":"Toshkent",
    "Qozog'iston":"Ostona",
    "Tojikiston":"Dushanbe",
    "Turkmaniston":"Ashxabot",
    "Qirg'iziston":"Bishkek",
    "Afg'oniston":"Qobul",
    "RF":"Moskva",
    "Xitoy":"Pekin",
    "Mongoliya":"Ulan-bator",
    "Ukraina":"Kiyev",
    "Kanada":"Ottava",
    "Hindiston":"Dehli"
    }

print("Dunyo davatlari: ")
for dav in sorted(davlat_poyt.keys()):
    print(dav.upper())

print(" \nDavlatlar potaxtlari: ")    
for poy in sorted(davlat_poyt.values()):
    print(poy.title())
    


#3\ Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning 
#poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni 
#kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
    
#country = input("Qaysi davlatlarning poytaxtlarini bilishni istaysiz?: ").lower()
#capital = davlat_poyt.get(country)
#if capital == None:
#    print("Bizda bunday ma'lumot mavjud emas!")
#else:
#    print(f"{country.upper()}ning poytaxti {capital.title()}") 
    
#4\ Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
#   Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
#   taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
#   aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
    
menu = {
        "osh":25000,
        "osma sho'rva":20000,
        "tandir somsa":10000,
        "kosa somsa":30000,
        "choy":5000,
        'non':5000,
        'svejiy salat':10000,
        "tuzlama salat":15000,
        "ko'fta shashlik":12000,
        "kuskovoy shashlik mol go'shti":13000,
        "kuskovoy shashlik qo'y go'shti":13000,
        "Uygur jizi":50000,
        'oddiy jiz':48000,
        "lag'mon":33000,
        "tabaka":35000,
        "gril":43000,
        "setka baliq":65000,
        'qovurma baliq':60000
       }
print("3ta taomga buyurtma bering: ")
z_taom = []
z_taom["1-taom"] = input("1-taomni kiriting:>>>")
z_taom["2-taom"] = input("2-taomni kiriting:>>>")
z_taom["3-taom"] = input("3-taomni kiriting:>>>")
for t,n in z_taom.items():
    print(f"{t}:{n}")
taom = menu.get(n)
if taom == None:
    print(f"{n} menuda yo'q")
else:
    print()
 
       
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    