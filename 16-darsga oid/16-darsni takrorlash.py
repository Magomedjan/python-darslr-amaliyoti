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

for malibu in malibus[15:30]:
    malibu['rangi']=['qora']
    
for malibu in malibus[30:]:
    malibu['rangi']=['qora']
    malibu['korobka']=['mexanika']
   
#for malibu in malibus:
#    print(malibu)

for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narxi']=40000
    else:
        malibu['narxi']=35000

for malibu in malibus:
    print(malibu)


                    #Lug'at ichida ro'yxat yaratish
                    

dasturchilar = {
                'ali':['c++', 'python'],
                'vali':['js', 'css', 'html'],
                'nabi':['php', 'SQL'],
                "g'ani":['python', 'php'],
                'maryam':['c++', 'c#']
                }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi : ", end='' )
    for til in tillar:
        print(f" {til.upper()} " , end='' )
        
        
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

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}."
          f"{info['tyil']} yilda tug'ilgan."
          f"\nMa'lumoti: {info['malumot']}. \nQuyidagi tillarni biladi: ")
    for til in info['tillar']:
        print(til.upper())




















































    