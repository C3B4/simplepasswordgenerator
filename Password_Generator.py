import random
import os

dlugosc = input("Jaka ma być długość hasla: ")
ilosc = input("Jaka ma być ilość haseł: ")
znaki = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
password = ""

if dlugosc == "":
    dlugosc = 16
if ilosc == "":
    ilosc = 1

if int(dlugosc) < 1:
   print("Długość hasła nie może być któtsza niż 1")
if int(ilosc) < 1:
    print("Ilość haseł nie może być mniejsza niż 1")

for i in range(int(ilosc)):
    for x in range(int(dlugosc)):
        z = random.choice(znaki)
        password += z
    print(password)
    password = ""

os.system("pause")