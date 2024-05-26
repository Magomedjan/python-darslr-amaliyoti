# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:46:46 2024

@author: Magomedjan
"""
                #20-MASHQ/TAKRORLASH

#def tuliq_ism(ism, familiya):
#    """Tuliq ism qaytarish funksiyasi"""
#    tuliq_ism = f"{ism} {familiya}"
#    return tuliq_ism.title()
#talaba1 = tuliq_ism('fayzullo', 'Ismatov')
#talaba2 = tuliq_ism("Olimjon", "ganiev")
#talaba3 = tuliq_ism('Madi', 'Soliev')
#print(f"Darsga kelmagan talabalar: \n -{talaba1} \n -{talaba2}")    
#print(f"Talaba {talaba3} darsga kechikib keldi")


def tuliq_ism_chiqar(ism, familiya, sharif=''):
    """Tuliq ism qaytarish funksiyasi"""
    if sharif:
        tuliq_ism = f"{ism} {sharif} {familiya}"
    else:
        tuliq_ism = f"{ism} {familiya}"
    return tuliq_ism.title()
talaba1 = tuliq_ism_chiqar('fayzullo', 'Ismatov', 'salimovich')
talaba2 = tuliq_ism_chiqar("Olimjon", "ganiev")
talaba3 = tuliq_ism_chiqar('Madi', 'Soliev', 'Alievich')
print(f"Darsga kelmagan talabalar: \n -{talaba1} \n -{talaba2}")    
print(f"Talaba {talaba3} darsga kechikib keldi")































































