# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:43:31 2024

@author: Magomedjan

"""



                            #NESTING


car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narx':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narx':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narx':15000,
        'km':20000,
        'korobka':'mexanika'
        }


                        # Bitta mashinani ma'lumotlarini chiqarish
#car=car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} yil, {car['narx']}$"
#      )


                        #Ro'yxat ichida lug'at yaratish                        

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']} yil, {car['narx']}$"
          )
print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}"
         )


                    #Ro'yxat orqali lug'at yaratishni optom ishlashga qulayligi

malibus = []
for n in range(50):
    new_car = {
        "model":"malibu",
        "yil":2024,
        "rangi":None,
        "probeg":0,
        "narxi":None,
        "korobka":"avto"
        }
    malibus.append(new_car)


for malibu in malibus[:15]:
    malibu['rangi']=['qizil']

#for malibu in malibus:
#    print(malibu)

#for malibu in malibus[15:30]:
#    malibu['rangi']=['qora']
#    
#for malibu in malibus[30:]:
#    malibu['rangi']=['qora']
#    malibu['korobka']=['mexanika']
   
#for malibu in malibus:
#    print(malibu)

#for malibu in malibus:
#    if malibu['korobka']=='avto':
#        malibu['narxi']=40000
#    else:
#        malibu['narxi']=35000

#for malibu in malibus:
#    print(malibu)


                    #Lug'at ichida ro'yxat yaratish
                    

#dasturchilar = {
#                'ali':['c++', 'python'],
#                'vali':['js', 'css', 'html'],
#                'nabi':['php', 'SQL'],
#                "g'ani":['python', 'php'],
#                'maryam':['c++', 'c#']
#                }

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi : ", end='' )
#    for til in tillar:
#        print(f" {til.upper()} " , end='' )
        
        
                    #LUG'AT ICHIDA LUG'AT YARATISH
hamkasblar = {
                'ali':{'familiya':'valiev',
                       'tyil':1995,
                       'malumot':'oliy',
                       'tillar':['c++', 'python']},
                'vali':{'familiya':'aliev',
                       'tyil':2000,
                       'malumot':"o'rta maxsus",
                       'tillar':['js', 'css', 'html']},
                'hasan':{'familiya':'husanov',
                       'tyil':2003,
                       'malumot':"o'rta",
                       'tillar':['php', 'SQL']}
            }

#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}."
#          f"{info['tyil']} yilda tug'ilgan."
#          f"\nMa'lumoti: {info['malumot']}. \nQuyidagi tillarni biladi: ")
#    for til in info['tillar']:
#        print(til.upper())

                            #15 DARS AMALYIOTI

# 1/ Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta 
# mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida 
# saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir 
# shaxs haqidagi ma'lumotni konsolga chiqaring.

shaxs1 = {
          'ism':"Alisher",
          'sharif':'Navoiy',
          'tyil':'1441',
          'tjoy':'hirot',
          'faoliyat':'shoir',
          'ijodi':['Xamsa', 'Majolis un-nafois', 'Xazoyin ul-maoniy', 'Mahbub ul-qulub']
          } 

shaxs2 = {
          'ism':"Muhammad",
          'sharif':'al-Xorazmiy',
          'tyil':'780',
          'tjoy':'Xorazm',
          'faoliyat':'olim',
          'ijodi':['Fi xisab al-Xind', 'Aljabr val muqobala', 'Arifmetika', 'Zij']
          } 

shaxs3 = {
          'ism':"Abu Abdulloh Muhammad",
          'sharif':'Al Buxoriy',
          'tyil':'810',
          'tjoy':'Buxoro',
          'faoliyat':'muhaddis olim',
          'ijodi':['Al-jomeʼ as-Sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as-sagʻir', 'At-tarix al-avsat', 'At-tafsir al-kabir', 'Birrul volidayn', 'Asmo as-sahoba', 'Kunyalar' ]
          } 

shaxs4 = {
          'ism':"Stiv",
          'sharif':'Jobs',
          'tyil':'1955',
          'tjoy':'San Fransizko',
          'faoliyat':'ixtirochi-tadbirkor',
          'ijodi':['apple iphone', 'ipad', 'itune', 'imac', 'ipod']
          } 

shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]
for shaxs in shaxslar:
    print(f"\n{shaxs ['ism']} "
          f"{shaxs ['sharif']} " 
          f"{shaxs['tyil']} yilda " 
          f"{shaxs['tjoy']}da tug'ilgan. "
          f"Taniqli {shaxs['faoliyat']}. "
          f"Uning ijodi namunalari: ")
    for ijod in shaxs['ijodi']:
# 2/ Yuqoridagi lug'atlarga har bir shaxsning mashxur 
# asarlari ro'yxatini ham qo'shing. For tsikli yordamida
# muallifning ismi va uning asarlarini konsolga chiqaring.
    
       print (f" - {ijod.title()}")

# 3/ Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli 
# kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# uning sevimli kinolarini esa ro'yxat ko'rinishida 
# lug'artga saqlang.  Natijani konsolga chiqaring.

yaqinlar={
            'xotin':['Hukmdor Usmon', 'Mehmonjonlardan aylanay', 'Kelgindi kelin'],
            'nodir':['Vir va Zarra', 'Taksi 1-5', 'Snayper'],
            'akmal':['Terminator', 'Ikkili zarba', 'Begona']
            }
#for yaqin, kinolar in yaqinlar.items():
#    print(f"\n{yaqin.title()}ning eng sevimli kinolari: ")
#    for kino in kinolar:
#        print(f" - {kino}")
        

    
# 4/ Davlatlar degan lug'at yarating, lug'at ichida bir
# nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida 
# saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
                "o'zbekiston":{
                                'nomi':"O'zbekiston Respublikasi",
                                'davlat tuzumi':'Suveren demokratik davlat',
                                'poytaxti':'Toshkent',
                                'aholisi':36_000_000,
                                'maydoni':447_400,
                                'valyuta':"so'm"
                                },
                
                "qozog'iston":{
                                'nomi':"Qozog'iston Respublikasi",
                                'davlat tuzumi':'demokratik davlat',
                                'poytaxti':'Ostona',
                                'aholisi':20_000_000,
                                'maydoni':2_729_400,
                                'valyuta':"tenge"
                                },
                "rossiya":{
                                'nomi':"Rossiya federativ Respublikasi",
                                'davlat tuzumi':'demokratik davlat',
                                'poytaxti':'Moskva',
                                'aholisi':144_000_000,
                                'maydoni':17_100_000,
                                'valyuta':"rubl"
                                },
                "aqsh":{
                                'nomi':"Amerika qo'shma shtatlari",
                                'davlat tuzumi':'demokratik davlat',
                                'poytaxti':'Vashington',
                                'aholisi':334_000_000,
                                'maydoni':9_834_000,
                                'valyuta':"tenge"
                                },
            }

#for davlat, info in davlatlar.items():
#    if davlat.lower()=='aqsh':
#        davlat = davlat.upper()
#    else:
#        davlat = davlat.capitalize()
#    print(f"\n{davlat} - to'liq nomi: {info['nomi'].title()}, \n{info['davlat tuzumi']}.\n"
#          f"poytaxti: {info['poytaxti']} shahri.\n"
#          f"aholisi: {info['aholisi']}.\n"
#          f"maydoni: {info['maydoni']} kv*km.\n"
#          f"milliy valyutasi: {info['valyuta']}."
#          )



# 5/ Yuqoridagi dasturga o'zgartirish kiriting: 
# konsolga barcha davlatlarni emas, foydalanuvchi 
# so'ragan davlat haqida ma'lumot bering. Agar 
# davlat sizning lug'atingizda mavjud bo'lmasa, 
# "Bizda bu davlat haqida ma'lumot yo'q" degan 
# xabarni chiqaring.



davlat = input('Qiziqtiruvchi davlat nomini kiriting: \n>>>').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    
    print(f"\n{info['nomi'].title()}, \n{info['davlat tuzumi']}.\n"
          f"poytaxti: {info['poytaxti']}.\n"
          f"aholisi: {info['aholisi']}.\n"
          f"maydoni: {info['maydoni']} kv*km.\n"
          f"milliy valyutasi: {info['valyuta']}."
          )
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")











































    