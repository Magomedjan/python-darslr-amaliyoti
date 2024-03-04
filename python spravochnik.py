# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:18:01 2024

@author: Magomedjan
"""
                        #PYTHON BO"YICHA SPRAVOCHNIK 
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
            'print':"ekranga chqarish",
                   'items()':"lugat elementlarini chiqarish",
                   "keys()":"lug'at kalitini chiqarish"
                   
                   }

  
         lugat = input("pythonga oid suz kiriting: \n>>>").lower()
         print(Python.get(lugat,"Bunda so'z mavjud emas" ))
         
         #Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
         #ko'rinishda chiqaring.

         lg = input("pytonda tushunmagan komandani kiriting \n>>>").lower()
         kalit = Python.get(lg)
         if kalit == None:
             print("Bunda so'z mavjud emas")
         else:
             print(f"'{lg.title()}' suzini ma'nosi '{kalit}' so'zini bildiradi")