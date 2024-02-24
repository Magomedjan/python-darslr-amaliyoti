# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 06:51:22 2023

@author: User
"""

mevalar = ["olma", "anjir", 'shaftoli', "o'rik"] #Mevalar ro'yxati (matnlar)
narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2] #Narxlar ro'yxati(sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] #sonlar ro'yxati (sonlar va matnlar)
ismlar = [] #bo'sh ro'yxat
#print (narxlar [0] + narxlar[1])
mevalar.insert(3, 'ananas')
mevalar.insert(0, 'banan')
#print(mevalar)
cars = []
cars.append('Nexia')
cars.append('Lacetti')
cars.append('Malibu')
cars.append('Tracker')
del cars [0]
#print (cars)
cars.append('Nexia')
cars.append('Tico')
cars.append('Matiz')
#print(cars)
del cars [4]
#print(cars)
cars.remove('Nexia')
cars.append('Nexia-3')
#print(cars)
hayvonlar = ['it', 'mushuk', 'sigir', "qo'y", "quyon", 'mushuk']



#AMALIYOT
#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [1, 2 , 3, 230, -88, 55.5, 3000000, 5.0]


# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar.remove(5.0)
sonlar.insert(4, 222)
sonlar[5] = sonlar[5] - 12
del sonlar[5] 

sonlar.insert (5, 100)
#print(sonlar)
 

#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat 
#qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ["Imom G'azzoliy", "Az-Zamahshariy", "Mirzo Bobor", "Alisher Navoiy", "Amir Temur"]
z_shaxslar = ["Shayx Muhammad Yusuf", "Putin", "Bill Gayts", "Abror Muxtor Ali", "Sariq Dev"]

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
#quyidagi ko'rinishda chiqaring:

t_shaxs = t_shaxslar.pop(0)
#print(t_shaxslar)
#print(t_shaxs)
z_shaxs = z_shaxslar.pop(0)
#print("Men tarixiy shaxsalrdan", t_shaxs, "bilan, \nzamonaviy shaxslardan ", z_shaxs, "\nbilan suhbat qilishni hohlar edim")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi 
# -bo'lgan do'stlaringizni kiriting. 
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
#-Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida 
#-mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

friends = []
friends.append("Ermat")
friends.append("Zafar")
friends.append("Mardon")
friends.append("D'stmurod")
friends.append("Jo'rabek")
friends.append("Samad")
friends.append("G'olib")
friends.remove("G'olib")
friends.insert(0, "Shodi aka")
friends.insert(6, "Xudoyberdi")
mehmonlar = []
#mehmonlar.append(friends.pop(3))
#mehmonlar.append(friends.pop(1))
#mehmonlar.append(friends.pop(0))

#print(friends)
#print("\nKelagan mehmonlar: \n>>>", mehmonlar)

mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)

































