# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:27:14 2024

@author: Magomedjan
"""
print("Dostlar ro'yxatini yaratish")
dustlar = []
n = 1
while True:
    savol = f"{n}-do'stingizni ismini kiriting \n> "
    ism = input(savol)
    dustlar.append(ism)
    takror = input("Yana do'stingizni ismini kiritasizmi? ha|yo'q \n: ")
    n +=1
    if takror != 'ha':
        break
print(" Sizni do'stlaringiz: ", end='')
for ism in dustlar:
    print(ism.title(), end=', ')


        #Do'stlar va ularni t yilini kiritish
print("Dustlarungini ismi va tyilini ro'yxatini tuzish")
dustlar={}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    tyil = input("Do'stingizni tug'ilgan yilini kiriting: ")
    dustlar[ism] = int(tyil)
    savol = input("Yana do'stingizni kiritasizmi? \n(ha/yo'q) > ")
    if savol == "yo'q":
        ishora=False
print("do'stlaringiz ro'yxati")
for i,ty in dustlar.items():
    print(f"{}")
    
    