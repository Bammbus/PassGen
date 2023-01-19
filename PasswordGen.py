import random
from time import *

print("Welcome to PasswordGen! This is a very simple open-source program that quickly generates a 20-character password that works everywhere.")
sleep(1)

lowercase = "abcdefghijklmnoprstquvxyz"
uppercase = "ABCDEFGHIJKLMNOPRSTQUVXYZ"
numbers = "1234567890"
symbols = "!@#$^%&*{}[];/,._-"

all = lowercase + uppercase + numbers + symbols
length = 20
password = "".join(random.sample(all, length))

print("Your randomly-generated password is " + password)

sleep(100)