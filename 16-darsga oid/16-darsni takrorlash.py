# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:43:31 2024

@author: Magomedjan
"""
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

#car=car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} yil, {car['narx']}$"
#      )

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']} yil, {car['narx']}$"
          )
print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}"
         )












































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
#for malibu in malibus:
#    print(malibu)

    