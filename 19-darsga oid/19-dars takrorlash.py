# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:33:06 2024

@author: Magomedjan

"""

#def salom_ber():
##    """Salom berish funktsiyasi"""
##   print("Assalomu alaykum")
#
#salom_ber()

#def salom_ber(ism):
#    """Ismni qabul qilib, salom berish funktsiyasi"""
#    print(f"Assalomu alaykum hurmatli {ism.title()} aka!")

#print(print.__doc__)
#print(range.__doc__)


def fish_chiqar(familiya, ism, sharif):
    """Foydalanuvchi familiya, ism va sharifini to'liq chiqaruvchi funktsiya)"""
    print(f"Foydalanuvchi familiyasi: {familiya.title()}\n"
          f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi sharifi: {sharif.title()}"
            )
fish_chiqar('kamolova', 'sayyora', 'muxsinovna')

def yosh_hisobla(ism, tyil):
    """Foydalanuvchi tug'ilgan yilini chiqaruvchi funktsiya"""
    print(f"{ism.title()} {2024-tyil} yoshda")

yosh_hisobla('sayyora', 1979)
yosh_hisobla(tyil=1980, ism = 'olim')

def yoshni_hisobla(tyil, jyil=2024):
    



















