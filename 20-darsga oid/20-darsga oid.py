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


#def tuliq_ism_chiqar(ism, familiya, sharif=''):
#    """Tuliq ism qaytarish funksiyasi"""
#    if sharif:
#        tuliq_ism = f"{ism} {sharif} {familiya}"
#    else:
#        tuliq_ism = f"{ism} {familiya}"
#    return tuliq_ism.title()
#talaba1 = tuliq_ism_chiqar('fayzullo', 'Ismatov', 'salimovich')
#talaba2 = tuliq_ism_chiqar("Olimjon", "ganiev")
#talaba3 = tuliq_ism_chiqar('Madi', 'Soliev', 'Alievich')
#print(f"Darsga kelmagan talabalar: \n -{talaba1} \n -{talaba2}")    
#print(f"Talaba {talaba3} darsga kechikib keldi")


#def avto_info(Kompaniya, modeli, rangi, uzqutisi, yili, narxi=None):
#    """avto bozor"""
#    avto = {'Kompaniya':Kompaniya,
#            'Model':modeli,
#            'Rang':rangi,
#            'Korobka':uzqutisi,
#            'Yil':yili,
#            'Narx':narxi            
#            }
##    return avto
#avto1 = avto_info('GM', 'Malibu', 'oq', 'avtomat', 2015)
##avto2 = avto_info('GM', 'Lacetti', 'qora', 'mexanika', 2023, 15000)
#avtolar = [avto1, avto2]
#print(avtolar[0]['Model'])
##print(avto1['Narx'])
#print(avto2['Narx'])
#print("Online bozorda mavjud avomashina modellari:")
#for avto in avtolar:
#    if avto['Narx']:
#        narx = avto['Narx']
#    else:
#        narx = "Noma'lum"
#    print(f"{avto['Rang'].title()} {avto['Model']} narxi: {narx} ")



#def oraliq(min, max, qadam = ''):
#    sonlar=[]
#    while min<max:
#        if qadam:
#            min += qadam
#        else:
#            min += 1
#        sonlar.append(min)
#    return sonlar        
        
#print(oraliq(0, 12, 4))
#print(oraliq(0, 12, 3))
#print(oraliq(0, 12, 2))
#print(oraliq(0, 12))




def avto_info(kompaniya, modeli, rangi, uzqutisi, yili, narxi=None):
    """avto bozor"""
    avto = {'kompaniya':kompaniya,
            'model':modeli,
            'rang':rangi,
            'korobka':uzqutisi,
            'yil':yili,
            'narx':narxi            
            }
    return avto
print("Avtosalonda mavjud avtomashinalar ro'yxatini shakllantiramiz")
avtolar = []
while True:
    print("Quyidagi ma'lumotlarni kiriting!")
    kompaniya = input('Avtokompaniya nomi: ')
    modeli = input('modeli: ')
    rangi = input('rangi: ')
    uzqutisi = input('uzatmalar qutisi turi: ')
    yili = input("Ishlab chiqarilgan yili: ")
    narxi = input('narxi: ')
    avtolar.append(avto_info(kompaniya, modeli, rangi, uzqutisi, yili, narxi))
    surov = input('Yana avto kiritasizmi? y/n ')
    if surov == 'n':
        break
    
print("Salonda mavjud avomashina modellari:")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['kompaniya'].title()} kompaniyasini {avto['model'].title()} "
          f" avtomashinasi, rangi-{avto['rang']}, {avto['yil']} yilda i/ch, "
          f"uzatmalar qutisi-{avto['korobka']}, narxi-{narx}$")

























































































