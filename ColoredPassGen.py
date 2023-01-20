import random
from time import *
import sys
from termcolor import colored

introtext = (""Welcome to PasswordGen! This is a very simple open-source program that quickly generates a 20-character password that works everywhere.")
sleep(1)

lowercase = "abcdefghijklmnoprstquvxyz"
uppercase = "ABCDEFGHIJKLMNOPRSTQUVXYZ"
numbers = "1234567890"
symbols = "!@#$^%&*{}[];/,._-"

all = lowercase + uppercase + numbers + symbols
length = 20
password = "".join(random.sample(all, length))

print("Your randomly-generated password is " + password)
user_input = input('Would you like to save this password? (y/n) (Your choice closes the program.)')

if user_input.lower() == 'y':
    print('This password is saved in the log file. It can be found in the directory of the program.')

    exit()
    

elif user_input.lower() == 'n':
    print('You probably use a password manager then.')
else:
    print('I literally said type y/n.')
    exit()


sleep(100)
