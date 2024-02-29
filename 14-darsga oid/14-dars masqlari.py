# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:08:20 2024

@author: User
"""
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

#print(t)







#AMALIYOT
# 1/otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta \
#m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn 
#shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
#ukam = {'fio':"nurmuhamedov nodirbek bahodirovich", 'tyil':1981, 'tjoy':'buxoro', 'manzil':'Buxoro sh.', \
#        'mashgulot':'arab tili' }
#print(f" Ukamni ismi-sharifi {ukam['fio'].title()} {ukam['tyil']} yilda {ukam['tjoy']} shahrida tugilgan,{ukam['manzil']}da yahsaydi")

#otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
#tyil = otam['tyil']
#vil = otam['viloyat']
#print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")



# 2/Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi \
    #bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
#s_taom = {'otam':'shurva',
#          'k_opam':"shokolad",
#          'opam':'shahlik',
#          'ukam':'grill',
#          'xotinim':'ismaloq barak'}
#print(f" Otamning sevimli taomi {s_taom['otam']} \n Ukamnin sevimli taomi {s_taom['ukam']} \n xotinimni sevimli taomi {s_taom['xotinim']}")
    
#taomlar = {
#    'ali':'osh',
#    'vali':'shashlik',
#    'hasan':"lag'mon",
#    'husan':"mastava",
#    'olim':"somsa"
#    }
#
#taom = taomlar['ali']
#print(f"Alining sevimli taomi {taom}")



# 3/ Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
#(masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

Python = {'integer':'butun son', 
          'float':'unlik son', 
          'string':'matn', 
          'if':"agar funk", 
          'else':'aks holda',
          'for':"uchun",
          'in':"ichida",
          'del':"yo'q qilish",
          'title':"bosh harf",
          'input':"foydalnuvchi qiymat kiritishi",
          'print':"ekranga chqarish"}


# 4/Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan 
#chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

lugat = input("pythonga oid suz kiriting: \n>>>").lower()
print(Python.get(lugat,"Bunda so'z mavjud emas" ))
#if lugat in Python:
#    print('lugat')


#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
#ko'rinishda chiqaring.

lg = input("pytonda tushunmagan komandani kiriting \n>>>").lower()
kalit = Python.get(lg)
if kalit == None:
    print("Bunda so'z mavjud emas")
else:
    print(f"'{lg.title()}' suzini ma'nosi '{kalit}' so'zini bildiradi")






























































































