# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:41:09 2024

@author: Magomedjan
"""

                #RO"YXAT QAYTARISH
                
def bahola(ismlar):
    """Ismlarni baholab qaytaruvchi funksiya"""
    baholar={}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} bahosini qo'ying: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'nabi', "g'ani"]
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

