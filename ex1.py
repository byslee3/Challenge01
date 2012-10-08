import os
import shutil

alphabet_string = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabet_string.split(" ")

for letter in alphabet:
    os.chdir('Results')
    os.makedirs(letter)
    os.chdir('..')


#Stop and allow us time to check our work
raw_input("Continue? ")

#Go through and do the commands in reverse
#So that we start out with a clean slate the next time we run the program
for letter in alphabet:
    os.chdir('Results')
    os.removedirs(letter)
    os.chdir('..')
