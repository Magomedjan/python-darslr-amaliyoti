# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:27:14 2024

@author: Magomedjan
"""
#print("Dostlar ro'yxatini yaratish")
#dustlar = []
#n = 1
#while True:
#    savol = f"{n}-do'stingizni ismini kiriting \n> "
#    ism = input(savol)
#   dustlar.append(ism)
#    takror = input("Yana do'stingizni ismini kiritasizmi? ha|yo'q \n: ")
#    n +=1
#    if takror != 'ha':
#        break
#print(" Sizni do'stlaringiz: ", end='')
#for ism in dustlar:
#    print(ism.title(), end=', ')


        #Do'stlar va ularni yoshini kiritish
#print("Dustlarungini ismi va tyilini ro'yxatini tuzish")
#dustlar={}
#t=1
##ishora = True
#while ishora:
#    ism = input(f"{t}-do'stingizni ismini kiriting: ")
#    tyil = input(f"{t}-Do'stingizni tug'ilgan yilini kiriting: ")
#    yosh = 2024-int(tyil)
#    dustlar[ism] = yosh
#    savol = input("Yana do'stingizni kiritasizmi? \n(ha/yo'q) > ")
#    if savol == "yo'q":
#        ishora=False
#    t += 1    
#print("do'stlaringiz ro'yxati:")
#for i,ty in dustlar.items():
#    print(f"  - {i.title()} do'stingiz {ty} yoshda")
    
#cars = ['Lacetti', 'Nexia', 'Malibu', 'Toyota', 'Nexia', 'Audi', 'Lacetti', 'Nexia']
#for c in cars:
#    print(f"{c}, ", end=' ' )
#print("\n- farqi -")
#car = 'Audi'
#while car in cars:
#    cars.remove(car)
#for q in cars:
#    print(f"{q}, ", end=' ')

#talabalar = ["Nodir", "Botir", "Jamshid", "Valijon"]
#b_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba}ni bahosini kiriting : ")
#    print(f"{talaba} {baho} bilan baholandi")
#    b_talabalar[talaba]=int(baho)
#print("Talabalar reytibgi")
#for t,b in b_talabalar.items():
#    print(f" - {t} {b} baho oldi")
 

            #Amaliy mashg'ulot
    

# 1/Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
#   Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
#print("Buyurtma olish dasturi")
#zakaz = []
##n = 1
#while True:
#    mahsulot = input("Savatga kerakli mahsulotni kiriting: ")
#    print(f"{n}-mahsulot tanlandi")
##    zakaz.append(mahsulot)
#    n+=1
#    takror_s = input("Yana mahsulot tanlaysizmi? \nha/yo'q: ")
#    if takror_s != 'ha':
#        break
#print("Siz tanlagan mahsulotlar: ")
#for z in zakaz:
#    print(f" - {z} ")    

# 2/e-bozor uchun mahsulotlar va ularning narhlari lug'atini 
#   shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir 
#   nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
#print("e-bozor dasturi")
#e_bozor = {}
#n=1
#ishora = True
#while ishora:
#    mahsulot = input(f"{n}-mahsulotni kiriting: ")
#    narx = int(input(f"{mahsulot} narxini yozing: "))
#    e_bozor[mahsulot]=narx
#    tsurov = input("Yana mahsulot qo'shasizmi? ha/yo'q: ")
#    n += 1
#    if tsurov == "yo'q":
#        ishora = False
#print("Sizni mahsulatlaringiz ro'yxati:")
#for m,n in e_bozor.items():
#    print(f" - {m} mahsuloti, narxi {n} so'm.")



# 3/Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi 
#   ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar 
#   bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
#   Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, 
#   aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
    

e_bozor = {}
n=1
ishora = True
while ishora:
    mahsulot = input(f"{n}-mahsulotni kiriting: ")
    narx = int(input(f"{mahsulot} narxini yozing: "))
    e_bozor[mahsulot]=narx
    tsurov = input("Yana mahsulot qo'shasizmi? ha/yo'q: ")
    n += 1
    if tsurov == "yo'q":
        ishora = False
print("e-bozordagi mahsulatlar ro'yxati:")
for m,n in e_bozor.items():
    print(f" - {m} mahsuloti, narxi {n} so'm.")

zakaz = []
n = 1
while True:
    mahsulot = input("Savatga kerakli mahsulotni kiriting: ")
    print(f"{n}-mahsulot tanlandi")
    zakaz.append(mahsulot)
    n+=1
    takror_s = input("Yana mahsulot tanlaysizmi? \nha/yo'q: ")
    if takror_s != 'ha':
        break
while zakaz:
    buyurtma = zakaz.pop()
    if buyurtma in e_bozor.keys():
        narx = e_bozor[buyurtma]
        print(f" - {buyurtma.title()} - {narx} so'm")
    else:
        print(f"Kechirasiz, {buyurtma} mahsuloti bizda mavjid emas")
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    