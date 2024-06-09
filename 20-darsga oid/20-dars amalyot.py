# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:42:15 2024

@author: Magomedjan
"""

    #Vazifalar
    
# 1/ Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#    email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
#    qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#    Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

#def user_info(ismi, familiyasi, t_yili, t_joyi, telefoni, e_maili=''):
#    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#    user = {'ism':ismi,
#            'familiya':familiyasi,
#            't_yil':t_yili,
#            't_joy':t_joyi,
#            'telefon':telefoni,
#            'e_mail':e_maili           
#            }
#    return user
#user1 = user_info('fayzullo', 'ismatov', 1972, 'vardonze', 997011111, 'dollar@gmail.com')
##print(f"{user1['ism'].title()} {user1['familiya'].title()}"
#      f" {user1['t_joy'].title()}da tug'ilgan, yoshi {2024-user1['t_yil']}da ")
    
   

# 2/ Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
#    va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar 
#    haqidagi ma'lumotni konsolga chiqaring.

#ef user_info(ismi, familiyasi, t_yili, t_joyi, telefoni=None, e_maili=''):
#    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#    user = {'ism':ismi,
#            'familiya':familiyasi,
#            't_yil':t_yili,
#            'yosh':2024 - t_yili,
#            't_joy':t_joyi,
#            'telefon':telefoni,
#            'e_mail':e_maili           
#            }
#    return user
##mijozlart bush ruyxatini shakillantirish
#mijozlar=[]
#while True:
#    print("Mijoz ma'lumotlarini kirirting: ")
#    ismi=input('Ismi: ')
#    familiyasi=input("Familiyasi: ")
#    t_yili=int(input("Tug'ilgan yili: "))
#    t_joyi=input("Tugilgan joyi: ")
#    telefoni=input("Telefoni ")
#    e_maili=input("e-mail: ")
#    mijozlar.append(user_info(ismi, familiyasi, t_yili, t_joyi, telefoni, e_maili))
#    surov = input("Yana mijoz qo'shsizmi? h/y: ")
#    if surov =='y':
#        break
#print("Mavjud mijoz haqida ma'lumotlar: ")
#for mijoz in mijozlar:
#    if mijoz['e_mail']:
#        e_mail=mijoz['e_mail']
#    else:
#        e_mail="mavjud emas"
#    print(f" - {mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['t_yil']} yil"
#          f" {mijoz['t_joy']}da tug'ilgan, {mijoz['yosh']} yoshda, telefoni:"
#          f" {mijoz['telefon']}, e-maili:{e_mail}") 
           



# 3/ Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing


#def kattasini_ber(x, y, z):
##    """son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
#    max = x
#    if y>=max:
#        max=y
#    if z>=max:
#        max=z
#    return max
#print(kattasini_ber(222, 55, 655))





# 4/ Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
#    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

#def aylana_ulcha(radius):
#    """ aylaning radiusini qabul qilib olib, uning radiusini, 
#    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#    aylana={'radiusi':radius,
#           'diametri':radius*2,
#           'perimetri':(radius*2)*3.14159,
#           'yuzi':(radius**2)*3.14159
#            }
#    return aylana #
#
#print(aylana_ulcha(22))




# 5/ Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
#    (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
#    musbat sonlar)
#def tubson_ber(min, max):
#    """tub sonlar ro'yxatini qaytaruvchi funksiya"""
#    tubson=[]
#    for son in (min, max):
#        if son%1 or son%son:
#            tubson.append(son)
#    return tubson
#print(tubson_ber(2, 4, 56, 78, 544, 2134))


def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
print(tub_sonlar_top(1, 44))




def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n <= 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, int(n**0.5) + 1):
                if n % x == 0:
                    tub = False
                    break
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar

print(tub_sonlar_top(1, 44))



#def tub_sonlar_top(min, max):
##    tub_sonlar = []
#    for n in range(max(min, 2), max + 1):
#        tub = True
#        # Оптимизированная проверка на простоту
#        for x in range(2, int(n ** 0.5) + 1):
##            if n % x == 0:
 #               tub = False
#                break
#        
#        if tub:
#            tub_sonlar.append(n)
#
#    return tub_sonlar
#print(tub_sonlar_top(1, 44))





















#6/ Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
#   ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
#   Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga 
#   teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
#   Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 
#   8, 13, 21, 34, 55,...





















































