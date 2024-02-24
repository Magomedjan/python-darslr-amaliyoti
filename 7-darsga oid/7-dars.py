# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:35:50 2024

@author: User
"""


#mevalar = ["olma", "anjir", 'shaftoli', "o'rik"] #Mevalar ro'yxati (matnlar)
#sonlar = ['bir', 'ikki', 3, 4, 5] #sonlar ro'yxati (sonlar va matnlar
#sonlar.sort()
#print(sonlar)
#mevalar.sort()
#print(mevalar)
#cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort(reverse=True)
#print(cars)

#Mehmonlar = ["Odil", "Hamid", "Temur", "Avazbek", "Farrux", "Shamsetdin"]
#print("sorted() qaytargan ro'yxat:", sorted(Mehmonlar))
#print("Asl ro'yxat o'zgarmas qoldi:", Mehmonlar)

narxlar = [12000, 18000, 10900, 22000, 25000, 36000, 25, 63.2] #Narxlar ro'yxati(sonlar)
#print(narxlar)
#narxlar.sort()
#print(narxlar)
#print(sorted(narxlar, reverse=True))
#mevalar = ["olma", "anjir", 'banan', 'shaftoli', "o'rik"] #Mevalar ro'yxati (matnlar)
#mevalar.reverse()
#print(mevalar)
#print("mevalar turlari", len(mevalar),"ta",       "avtomobillar soni", len(cars), "ta"   )
#sonlar = list (range(0, 10, 2))
juft_sonlar = list(range(0,21,2))# 20 gacha juft sonlarni belilash
toq_sonlar = list(range(1,22, 2))# 20 gacha toq sonlarni belgiash
#print("Jufr sonlar:", juft_sonlar)
#print("Toq sonlar:", toq_sonlar)

eng_arzon = min(narxlar)
eng_qimmat = max(narxlar)
summa = sum(narxlar)
#print("eng arzon narsa:", eng_arzon,".",  "eng qimmat narsa:", eng_qimmat,".",  "umumiy summasi:", summa,"."  )
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#my_cars = cars[1:4] # 1-indeskdan boshlab 3 ta element ajratib olamiz
#print("Mening masinalarim", my_cars) 
#arzon_narxlar = narxlar [6:8]
#print(arzon_narxlar)
#print(cars[:4])
#print(cars[1:])

sonlar = [1, 2, 3, 4, 5] #sonlar nomli ro'yxat yaratamiz
sonlar2 = sonlar [:] # sonlar ro'yxatidan nusxa olish
sonlar2.append(6) # 6 sonini qo'shish
sonlar2.append(7) # 7 sonini qo'shish
sonlar2.append(8) # 8 sonini qo'shish
#print("sonlar ro'yxati:",sonlar) 
#print("sonlar2 ro'yxati:",sonlar2)

tomonlar = (10, 20, 55,2)
#print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat 
#print(toys) 
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga aylantiramiz
toys.append("dragon")
toys.remove('bus')
toys[1] = 'mcquin'
toys = tuple(toys) 
#print(toys)


 #AMALIYOT
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
Davlatlar = ["Africa", "Arabia", "Australia", "Russia", "America", "Holland"]
print(Davlatlar)
#Ro'yxatning uzunligini konsolga chiqaring
print(range(Davlatlar))
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#Asl ro'yxatni qaytadan konsolga chiqaring
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#Ro'yxatdagi elementlar sonini hisoblang
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.





































