import random
from time import *
from datetime import datetime
import getpass
username = getpass.getuser()

#Other stuff
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#Intro
print("Welcome to PasswordGen! This is a very simple open-source program that quickly generates a 20-character password that works everywhere.")
sleep(1)

#Variables
lowercase = "abcdefghijklmnoprstquvxyz"
uppercase = "ABCDEFGHIJKLMNOPRSTQUVXYZ"
numbers = "1234567890"
symbols = "!@#$^%&*{}[];/,._-"
mixmash = "KkhJGFg884G'\[;'."
special = "ẞαλ§"

#Mixing and creating password
all = lowercase + uppercase + numbers + symbols + mixmash + special
length = 20
password = "".join(random.sample(all, length))

#Printing password 
print("Your randomly-generated password is " + password)
sleep(1)
save = input("Do you want to save the password? (y/n)\n")
#Log system
if save == "y":
    with open("Password.txt", "w") as file:
        file.write("Password saved by " + username + " at " + current_datetime + " is " + password)
    print("Password saved to Password.txt.")
    sleep(1)
    quit()
else:
    print("Password not saved,")
    sleep(1)
    quit

sleep(100)
