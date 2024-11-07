import random
import time
import string

name = str(input('Name: '))
letters = string.ascii_letters
result = ''

for letter in name:
    while True:
        I = random.choice(letters)
        print(result + I)
        if (I == letter):
            result += I
            break
        time.sleep(0.1)