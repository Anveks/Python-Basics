import os # here we are using the path.join() method to specify the needed paths;

PLACEHOLDER = "[name]"
PATH = r'C:\Users\sylva\OneDrive\Documents\GitHub\Python-Basics\random_practices\mail-bot'
names = []

# extracting all the names from the names file:
with open(os.path.join(PATH, 'names.txt'), mode='r') as names_file:
    content_names = names_file.read()
    names.extend(content_names.split())

# open the starting letter:
with open(os.path.join(PATH, 'starting-random-letter.txt'), mode='r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # replace the [name] palceholder to a name from names list:  
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        # prepare the filename for each file:
        filename = f'letter_to_{name}.txt'
        # create the new_letter and save it in the ready-letters folder:
        with open(os.path.join(PATH, 'ready-letters', filename), mode='w') as completed_letter:
            completed_letter.write(new_letter)
