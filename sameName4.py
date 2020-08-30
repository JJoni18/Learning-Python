import os, sys

os.system('cls')

def spam():
    print(eggs) #ERROR
    eggs = 'spam local'

eggs  'global'
spam()
