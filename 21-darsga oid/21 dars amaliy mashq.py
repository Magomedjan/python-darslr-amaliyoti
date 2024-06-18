# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:57:24 2024

@author: Magomedjan
"""



                        #AMALIYOT
                        
                        
                        
# 1/ Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
#    harfini katta harfga o'zgatiruvchi funksiya yozing. 

#ismlar = ['ali', 'vali', 'hasan', 'husan']
#katta_harf(ismlar)
#print(ismlar)
# Kutilgan natija: ['Ali', 'Vali', 'Hasan', 'Husan']

#def bosh_harf(matnlar):
#    """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
#        harfini katta harfga o'zgatiruvchi funksiya """
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()
#ismlar = ['ali', 'vali', 'hasan', 'husan']
#bosh_harf(ismlar)
#print(ismlar)        
        
   

# 2/ Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat 
#    qaytaradigan qilib o'zgartiring
def bosh_harf(matnlar):
    """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
       harfini katta harfga o'zgatiruvchi dva asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat 
       qaytaradigan funksiya """
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = bosh_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)
#Kutilgan natija: ['ali', 'vali', 'hasan', 'husan'] 
# ['Ali', 'Vali', 'Hasan', 'Husan']






# 3/ Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
#    foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat 
#    lug'at qaytaradigan qilib yozing.

talabalar = ['ali', 'vali', 'nabi', "g'ani"]

def bahola(ismlar):
    """Ismlarni baholab qaytaruvchi funksiya"""
    
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ni bahosi: ")
        baholar[ism] = int(baho)
    return baholar

baholar = bahola(talabalar)
print(talabalar)
print(baholar)





talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)



























