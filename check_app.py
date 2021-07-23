"""
    @author : Goksu Aktas
    @date : 23.07.2021
    @version : 1.0.0
    @brief : This program check numbers from user positive or negative 
"""
print("##############################################")
print("Program Klavuzu")
print("##############################################")
print("Program sizden 5 adet sayı istemektedir")
print("Bu sayıların pozitif veya negatif olduklarına bakmaktadır")
print("----------------------------------------------")
a=[]
positive = 0
negative = 0
notr = 0
for i in range(0,5):
    sayi=int(input("Sayiyi Gir = "))
    a.append(sayi)
    if sayi>0:
        positive = positive + 1
        print("Positif")
    elif sayi==0:
        notr = notr + 1
        print("Nötr")
    else:
        negative = negative + 1
        print("Negatif")
a.sort()
print(a)
print(f"Positive = {positive} \nNegative = {negative} \nNotr = {notr}")



