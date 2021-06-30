# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:47:43 2021

@author: Dilafruz
"""

# cars = ['bmw', 'damas', 'nexia','tiko', 'jentra', 'lasetti', 'captiva']
# cars.sort()
# print(cars)
# cars = ['bmw', 'Damas', 'nexia','tiko', 'jentra', 'lasetti', 'captiva']
# cars.sort()
# print(cars)
#cars = ['bmw', 'damas', 'nexia','tiko', 'jentra', 'lasetti', 'captiva']
# cars.sort(reverse=True)
# print(cars)


# print(sorted(cars))
# print(sorted(cars, reverse=True))
#sonlar = [28, 52, 96, 74, 35, 97, -45, 2.15]
# sonlar.sort()
# print(sonlar)
# print(sorted(sonlar))
# print(sorted(sonlar, reverse=True ))
# mevalar = ["banan", "apelsin", "mandarin", "ananas", "kivi"] 
# mevalar.reverse()
# print(mevalar)
# print("elementlar soni", len(mevalar))
# sonlar = list(range(10))
# print(sonlar)
# juft_sonl = list(range(0,20,2))
# toq_sonl = list(range(1,20,2))
# print("juft sonlar", juft_sonl)
# print("toq sonlar", toq_sonl)
# kotta = max(sonlar)
# kicik = min(sonlar)
# yeg = sum(sonlar)
# print("eng kichik", kicik, "eng katta", kotta, "yeg'indi", yeg)
# my_cars = cars[2:]
# #my_cars = cars[:5]
# print(my_cars)
# sonlar2 = sonlar[:]
# sonlar2.append(1)
# sonlar2.append(10)
# print("Bu sonlar 1", sonlar , "Bu sonlar2", sonlar2)
# print(cars[2:5])
# print(cars[0])
#print(cars[-1])
# cars = ('bmw', 'damas', 'nexia','tiko', 'jentra', 'lasetti', 'captiva')
# cars = list(cars)
# cars.append("malibu")
# cars.remove("tiko")
# cars[3] = "mersss"
# cars = tuple(cars)
# print(cars)
# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)
# davlatlar = ["Rassia", "AQSH", "Amesterdam","Fransiya","Ispaniya"]
# #dav = sorted(davlatlar, reverse=True)
# #print(dav)
# #davlatlar.reverse()
# davlatlar.sort(reverse=True)
# print(davlatlar)
#print("Ro'yhat uzunligi", len(davlatlar))
# juft_son = list(range(120, 1200))
# # eng_k = max(juft_son)
# # eng_kic = min(juft_son)
# # yegindi = sum(juft_son)
# # print(eng_k - eng_kic)
# #print(len(juft_son))
# boshi = juft_son[:20]
# orta = juft_son[530:550]
# oxir = juft_son[-20:]
# print("boshi", boshi, "\no'rtasi", orta, "\noxiri", oxir)
taomar = ["osh", "galubsi","manti","lagmon", "mastava"]
nonushta = taomar[:]
nonushta.remove("osh")
nonushta.append("tuxum")
nonushta.insert(0, "qaymoq v non")
nonushta = tuple(nonushta)
nonushta.append("kalbasa")
print("taomlar", taomar, "\nnonushta", nonushta)
