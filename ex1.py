import os
import shutil

alphabet_string = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabet_string.split(" ")

#Create list of files
for letter in alphabet:
    os.chdir('Results')
    os.makedirs(letter)
    os.chdir('..')

#Grab a list of all the filenames that we want to move
list_of_filenames = os.listdir('original_files')

#Move the filenames
for current_file in list_of_filenames:
    
    #For the current file that we're moving, take the letter that it starts with
    #The destination of the file is equal to the letter that it starts with
    first_letter = current_file[0]

    #Move the file
    source_location = 'original_files/' + current_file
    destination_path = 'Results/' + first_letter

    shutil.copy(source_location,destination_path)

