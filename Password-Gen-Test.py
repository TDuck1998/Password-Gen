import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

choice = input('Specify password length: ')
choice = int(choice)

for a in range(choice):
    password += random.choice(chars)

print(password)
