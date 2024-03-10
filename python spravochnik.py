# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:18:01 2024

@author: Magomedjan
"""
                        #PYTHON BO"YICHA SPRAVOCHNIK 
Python = {  "boolean":"mantiqiy qiymat",
            "float":"o'nlik son",
            "integer":"Butb son",
            "string":"matn",
            "del":"O'chirish",
            "for":"qayta qayta bajarish tcikli",
            'if':"agar funk", 
            'else':'aks holda',
            'in':"ichida",
            'title':"matnni bosh harf qilish",
            'input':"foydalnuvchi qiymatini kiritish",
            'print':"ekranga chqarish",
            'items()':"lugat elementlarini chiqarish",
            "keys()":"lug'at kalitini chiqarish",
            "sorted()":"Sortirovat qilish",
            "value()":"lug'at  qiymatini chiqarish",
            "set()":"takrorlashni olib tahslash",
            ".lower()":"matnni kichik harf qilish",
            ".get()":"lug'at ichidan chiqarb, javob berish"
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
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             