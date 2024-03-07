# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:16:02 2024

@author: Magomedjan
"""
#                                    15-dars

talaba_1={}

talaba_1['ism'] = "xujamurodov boburjon"
talaba_1['t_yil'] = 2003
talaba_1['t_kun'] = 10.09
talaba_1['t_joy'] = "buxoro"
talaba_1['tuman'] = 'shofirkon'
talaba_1['nation'] = "o'zbek"
talaba_1['inst'] = "Diplomatiya"
talaba_1['u_joy'] = 'Toshkent'
talaba_1['fakultet'] = 'jahon iqtisodiyoti'
talaba_1['kurs'] = 4
#print(talaba_1.items())
#for k, q in talaba_1.items():
#    print(f"   kalit: {k}")
#    print(f"   qiymat:{q} \n")
    
    
telephones = {
    "ali":"IPhone X",
    "vali":"Samsung Galaxy S23",
    "nosir":"Mi 13 Pro",
    "g'ani":"IPhone 15 pro Max",
    "nabi":"Samsung zet fold",
    "hodi":"IPhone X",
    "nodir":"Honor 6b",
    "shodi":"Samsung Galaxy S23",
    'lola':"Honor 6b"
    }
#for t, v in telephones.items():
#    print(f"          {t.title()}ning telefoni: {v} \n")
    
    
mahsulotlar = {
    "olma":12000,
    "anor":50000,
    "nok":20000,
    "banan":19000,
    "uzum":25000,
    "apeslin":15000
    }
#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
#    print(f"- {mahsulot}")

#print("\n Do'kondagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#    print(f" - {mahsulot}")

#shopping = ["baliq", "suv", "nok", "uzum", "sabzi", "olma"]
#for mahsulot in mahsulotlar:
#    if mahsulot in shopping:
#        print(f"\n-{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#print("\n Iltimos do'koningizga: ")
#for buyum in shopping:
#    if buyum not in mahsulotlar:
#        print(f"- {buyum.title()}")
#print(" mahsulotlarni ham olib keling!")
#sorted ni qullash
#print(sorted(mahsulotlar))

# Value() ni qo'llash
#print("Talabalar foydalanadigan telefonlar: ")
#for phone in sorted(telephones.values()):
#    print(f"{phone}\n")

print("Talabalar foydalanadigan telefonlar: ")
for phone in sorted(set(telephones.values())):
    print(phone)
    
                    #Set() ruyxati
toys = {"ball", 'car', 'car', 'bear', 'teddy', 'ball'}
print(toys)


























