import random

#PASSWORD GENERATOR#
print('''
██████╗ ██╗    ██╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██║    ██║██╔════╝ ██╔════╝████╗  ██║
██████╔╝██║ █╗ ██║██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██║███╗██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ╚███╔███╔╝╚██████╔╝███████╗██║ ╚████║
╚═╝      ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝

''')

chars = '`¬!"£$%^&*()_+{}@~:>?<-=[];#./abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('welcome')
input('Press ENTER to continue')

choiceLen = input('Specify password length: ')
choiceLen = int(choiceLen)
choiceNum = input('How many passwords: ')
choiceNum = int(choiceNum)

print('-' * choiceLen)
print('DISPLAYING ' + str(choiceNum) + ' PASSWORDS')
print('-' * choiceLen)

if choiceNum <= 0:
    print('Error')
elif choiceLen <= 0:
    print('Error')
else:
    for a in range(choiceNum):
        password = ''
        for a in range(choiceLen):
            password += random.choice(chars)
        print('-' * choiceLen)
        print(password)
print('-' * choiceLen)
