# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 07:15:35 2024

@author: User
"""

#son = 50
#if son >=0:
#    print("Musbat son!")
#else:
#    print('Manfiy son!')

#yosh = int(input('Yoshingiz nehchida'))
#if yosh <= 4:
#    narx = 'bepul'
##elif yosh <=12:
 #   narx = 5000
##elif yosh <= 18:
#   narx = 8000 
#else:
#    narx = 10000
#print(f"Sizga kirish {narx} so\'m")



#kun = input('Bugun haftani qaysi kuni?\n>')
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print("Bugun dam olish kuni")
#else:
#    print('Bugun ish kuni')
    
#kun = input('Bugun hafaning qaysi kuni? >')
#harorat = float(input('Havo harorati qanaqa? >')) 
#if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#    print('Bugun cho\'milishga bormiz')
#elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#    print("Bugun uyda qolamiz")
    

#narx = 15000 #ovaqatni narxi
#non = True #Mijoz non ilomadi
#salat = False #Mijoz salat oldi
#if non and salat: #agar non va salat olsa unda
#    narx = narx + 10000 # ovqatga qushimcha 1000 to'laydi
#elif non or salat: # non yo`ki salat ni brirni olsa, unda 
#    narx = narx + 5000 # ovqatni narxiga 5000 qoshiladi
    
#print(f"Sizga jami {narx} so'm bo'ldi") #faqatgina 10000 tolaydi
    
    
    
#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

#print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz
    










#narx = 15000 # mijoz 15 so'mga ovqat oldi
#choy = 0
#salat = 0
#non = 0
#kompot = 0
#assorti = 1
#if choy:
#    print("Mijoz choy oldi")
#    narx = narx + 5000
#if salat:
#    print("Mijoz salat oldi")
#    narx = narx + 7000
#if non:
#    print("Mijoz non oldi")
#    narx = narx + 3000
#if kompot:
#    print("Mijoz kompot oldi")
#    narx = narx + 5000
#if assorti:
#    print("Mijoz assorti oldi")
#    narx = narx + 10000    
#print(f"Mijozni jami to'lov {narx} so'm")




#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#zakaz = input("Nima ovqat eysiz? >>>  ")
#if zakaz.lower() not in menu:
#    print(f"Afsuski buyurtmangizdagi {zakaz} menuda yo'q")
#else:    
#    print(f"{zakaz} buyurtmangiz qabul qilindi")

    
#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]    
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"{taom} menuda bor. Buyurtma qabul qilindi")
#    else:
#        print(f"Kechirasiz, {taom} menuda mavjud emas")
        
                        #1 amalyot
                         
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#son = float(input("Juft son kiriting:>>>"))
#if son % 2 != 0:
#    print("Juft son kiriting")
#else:
#    print("Rahmat!")
    

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh = float(input("Yoshingiz nechida?>>> "))
#if yosh<=4 or yosh>=60:
#    narx = 0
#elif yosh <= 18:
#    narx = 10000
#elif yosh > 18 and yosh < 60:
#    narx = 20000
#print(f"Sizga chipta narxi {narx} so'm")



#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichik
#ligi haqida xabarni chiqaring
        #2-masala
#son1 = float(input("birinchi sonno kiritng:>>> "))
##son2 = float(input("ikkinchi sonni kiriting:>>> "))
#if son1 == son2:
#    print("ikkala son bir biriga teng")
#elif son1<son2:
#    print(f"{son1}<{son2} - 2 son katta")
#else:
#    print(f"{son1}>{son2} - 1 son katta")
    
  
    #3 -masala
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh 
#ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi 
#elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot 
#do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
    
#mahsulotlar = ['anor', 'olma', 'nok', 'banan', 'greypfrut', 'limon', 'mandarin', 'apelsin', 'kivi', 'anannas', 'shaftoli', "o'rik"]
##savat = [] # bo'sh royxat yaratish
#savat.append(input("Savatga 1-mahsolotni qo'shing: "))# savat ruyxatiga birinchi mahsulotni qushish
#savat.append(input("Savatga 2-mahsolotni qo'shing: "))# savat ruyxatiga 2 mahsulotni qushish       
#savat.append(input("Savatga 3-mahsolotni qo'shing: "))# savat ruyxatiga 3 mahsulotni qushish
#savat.append(input("Savatga 4-mahsolotni qo'shing: "))   # savat ruyxatiga 4 mahsulotni qushish 
#savat.append(input("Savatga 5-mahsolotni qo'shing: "))  # savat ruyxatiga 5 mahsulotni qushish 
#savat.append(input("Savatga 6-mahsolotni qo'shing: "))# savat ruyxatiga 6 mahsulotni qushish
#for mahsulot in savat: # savatdagi har bir mahsulot uchun
#    if mahsulot in mahsulotlar: # agar mahsulot mahsulotlar ro'yxatida bo'lsa, unda 
#        print(f"Do'konimizda {mahsulot} bor") #bor mahsulotni chiqaramiz
#    else: #aks xolda
#        print(f"Do'konimizda {mahsulot} yo'q")#mahsulot yo'q deymiz
    
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda 
#yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
#"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
#do'konimizda yo'q: ....." degan xabarni chiqaring.    

#mahsulotlar = ['un', 'shakar', 'grechka', "sariyog'", 'nuxat', 'gerkules', 'sovun', 
#               "yog'", 'kolbasa', 'makaron', 'ovsyanka', "tuxum"]
#savat = [] # bo'sh royxat yaratish 
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsolotni qo'shing: ")) #savat ro'yxatiga mijozni talabini kiritish
    
##bor_mahsulotlar = []# bo'sh royxat yaratish
#mavjud_emas = []   # bo'sh royxat yaratish 

#for tovar in savat:
##    if tovar in mahsulotlar:
#        bor_mahsulotlar.append(tovar) 
#    if tovar not in mahsulotlar:
#        mavjud_emas.append(tovar) 
        
#if mavjud_emas:
#    print ("Quyidagi mahsulotlar do'konimizda yo'q:")
#    for tovar in mavjud_emas:  
#        print(f"-{tovar}")
        
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
    
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi 
#login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning 
#tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login 
#tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

#foydalanuvchilar = ['Siara', 'Gani', 'Tarkas', 'Mullo', 'Said', 'Nor', "Xol"]
#login = input("Yangi login tanlang: ")
#if login in foydalanuvchilar:
#    print(f"{login} logini band, yangi login tanlang!")
#else:
#    print(f"Xush kelibsiz, {login.title()}!")
  
#Foydalanuvchidan Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
#2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 


#son = int(input("Biror butun sonni kiriting:>>> "))
#for n in range(2,11):
##    if not (son%n):
 #       print(f"{son} soni {n}ga qoldiqsiz bo'linadi")
        
    
#son = int(input("Istalgan butun son kiriting: "))

#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    
    
    

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    