#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*']

print("Welcome to Password Generator...")
num_letter = int(input("How many letters would you want in your password?: "))
num_sym = int(input("How many symbols do you want into your password"))
num_ = int(input("How many numbers would you like to have?: "))

password = ""

for char in range(1,num_letter+1):
    password += random.choice(letters)

for char in range(1, num_sym+1):
    password += random.choice(symbols)

for char in range(1, num_ +1):
    password += random.choice(num)


print("Your Password is:" ,password)