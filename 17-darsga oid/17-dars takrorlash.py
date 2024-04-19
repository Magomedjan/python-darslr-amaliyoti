# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 07:56:08 2024

@author: User
"""

#ism=input('Ismingizni kiriting :')#

#savol=f"Salom {ism.title()}, yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh)
#hight = input("bo'yingiz necha metr? ")
#hight = float(hight)

son = 1
while son <=5:
    print(son, end=" ")
    son += 1
print("Dastur tugadi")


#print("Sonni kvadratini hisoblash dasturi")
#savol = "Biror sonni kiriting."    
#savol += "( Dasturdan chiqish uchun 'exit' yozing) >>>"
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#print("Dastur tugadi")


#print("Sonni kvadratini hisoblash dasturi")
#savol = "Biror sonni kiriting."    
#savol += "( dasturdan chiqish uchun 'exit' yozing) >>>"
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora= False
#    else:
#        print(float(qiymat)**2)
#print("Dastur tugadi")


#print("Sonni kvadratini hisoblash dasturi")
#savol = "Biror sonni kiriting."    
#savol += "( dasturdan chiqish uchun 'exit' yozing) >>>"
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print("Dastur tugadi")




# 1.Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
#   Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
savol = "O'zingiz yaxshi ko'rga kitoblarni kiriting." 
savol += "Dasturdan chiqish uchun 'stop' so'zini yozing > "
            #1-VARIANT
kitob = ''
while kitob != 'stop':
    kitob = input(savol)
    if kitob == 'stop':
        print("Dastur tugadi")
            
            #2-VARIANT
savol = "O'zingiz yaxshi ko'rga kitoblarni kiriting." 
savol += "Dasturdan chiqish uchun 'stop' so'zini yozing > "
while True:
    kitob = input(savol)
    if kitob == 'stop':
        break
print("Rahmat! Dastur tugadi")

            #3-Varinat (Avtor)
savol = "Sevgan kitobingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')     

 
# 2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
#   7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
#   18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
#   Shunday while tsikl yozingki, dastur foydalanuvchi 
#   yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi 
#   exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni
#   ham tekshiring).

#  1. Yuqoridagi dasturni turli usullarda yozib ko'ring (break, 
#   ishora, yoki shart tekshirish)

# 3.Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
#   Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib 
#   qolmoqda. Xatolarni to'g'rilay olasizmi?

#Copy
#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat<0:
#        continue
#    elif qiymat=='Exit':
#        break
#    else:
#        ildiz = float(qiymat)**(0.5)
#        print(f"{qiymat} ning ildizi {ildiz} ga teng")



































    