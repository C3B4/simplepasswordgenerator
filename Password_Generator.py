import random
import os

leng = input("How long passwords should be: ")
count = input("What count of passwords should be: ")
characters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
password = ""

if leng == "":
    leng = 16
if count == "":
    count = 1

if int(leng) < 1:
   print("Passwords leng can't be smaller than 1")
if int(count) < 1:
    print("Passwords count can't be smaller than 1")

for i in range(int(count)):
    for x in range(int(leng)):
        z = random.choice(characters)
        password += z
    print(password)
    password = ""

os.system("pause")
