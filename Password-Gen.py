import random

#PASSWORD GENERATOR#
chars = '`¬!"£$%^&*()_+{}@~:>?<-=[];#./abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

choiceLen = input('Specify password length: ')
choiceLen = int(choiceLen)
choiceNum = input('How many passwords: ')
choiceNum = int(choiceNum)

for a in range(choiceNum):
    password = ''
    for a in range(choiceLen):
        password += random.choice(chars)
    print(password)
