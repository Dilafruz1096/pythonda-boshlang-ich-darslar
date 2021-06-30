# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:58:32 2021

@author: Dilafruz
"""

# yosh = int(input("yoshingiz nechida"))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh<=65:
#     narx = 10000
# elif yosh>=65:
#     narx = 8000
    
# print(f"Sizga {narx} so'm")

# # if kun.lower() == "shanba" or kun.lower() == "yakshanba":
# #     print("Bugun dam olish kuni")
# # else:
# #     print("Bugun ish kuni")
# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Harorat qanday?>> "))
# if (kun.lower() == "yakshanba" or kun.lower() == "shanba" ) and harorat >= 30:
#     print("Chomilgani ketdik")
# elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
#         print("Bugun dam olamiz")
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")
# narx = 15000
# choy = False
# salad = True
# if choy and salad:
#     narx = narx + 10000
# elif choy or salad:
#     narx = narx + 5000
# print(narx)
# narx = 1500
# choy = True
# salad = False
# kompot = True
# non = True
# asarti = False
# if choy:
#     narx = narx + 3000
# if salad:
#     narx = narx + 6000
# if kompot:
#     narx = narx + 9000
# if non:
#     narx = narx + 2000
# if asarti:
#     narx = narx + 15000
# print(narx)
# menu = ["kabob", "osh", "bishteks" , "lagmon", "norin"]
# # ovqat = input("Nima ovqat yeysiz>>> ")
# # if ovqat.lower() not in menu:
# #      print("Bunday taom mavjud emas")
# # else:
# #    print("Buyurtma qabul qilindi")
# buyurtmalar = []
# if buyurtmalar:
#  for taom in buyurtmalar:
#     if taom in menu:
#         print(f"MenyudA {taom} bor")
#     else:
#         print(f"Kechirasiz menyuda {taom} yo'q")
# else:
#         print("Savatingiz bo'sh")
# son = int(input("Juft son kiriting>>> "))
# if son % 2  == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas")
# yoshingiz = int(input("Yoshingiz nechida"))
# if yoshingiz <= 4 or yoshingiz >= 60:
#     print("Sizga bepul")
# elif yoshingiz <= 18:
#     print("10000 so'm")
# else:
#     print("20000 so'm")
# son1 = float(input("1-sonni kiriting>>> "))
# son2 = float(input("2-sonni kiriting>>> "))
# if son1 == son2:
#     print(f"{son1} = {son2}")
# elif son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2:
#     print(f"{son1} < {son2}")
mahsulotlar = ["sabzi", "pamidor", "piyoz", "kartoshka", "bodring", "gosh", "balgarskiy", "karam", "chesnok", "guruch"]
savat = []
print("savatga 5 ta maxsulot kiriting:")
for n in range(5):
    savat.append(input(f"{n+1} maxsulot: "))
mahsulot_bor = []
mahsulot_yoq = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        mahsulot_bor.append(mahsulot)
else:
    mahsulot_yoq.append(mahsulot)
    
    if mahsulot_yoq:
         print("Bizning do'konimizda quyidagi mahsulotlar yo'q")
for mahsulot in mahsulot_yoq:
    print(mahsulot)
else:
    print("siz so'ragan barcha mahsulotlar do'konimizda bor")
            

    
    
    
    
#buyurtma = input("Sizga kerakli mahsulotlarni kiriting:>>> ") 

