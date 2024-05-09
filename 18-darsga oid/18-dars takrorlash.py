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

talabalar = ["Nodir", "Botir", "Jamshid", "Valijon"]
b_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba}ni bahosini kiriting : ")
    print(f"{talaba} {baho} bilan baholandi")
    b_talabalar[talaba]=int(baho)
print("Talabalar reytibgi")
for t,b in b_talabalar.items():
    print(f" - {t} {b} baho oldi")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    