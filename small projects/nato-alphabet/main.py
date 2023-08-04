import pandas

# alphabet = pandas.read_csv(r'.\small projects\nato-alphabet\nato_phonetic_alphabet.csv')
# alphabet_dict = {}

# for (intex, row) in alphabet.iterrows():
#   letter = row['letter']
#   code = row['code']
#   alphabet_dict[letter] = code

# user_input = input('What word do you want to decipher?\n').upper()
# input_list = list(user_input)

# deciphered_input = [alphabet_dict[letter] for letter in input_list]
# print(deciphered_input)

data = pandas.read_csv(r'.\small projects\nato-alphabet\nato_phonetic_alphabet.csv')
phonetic_dict = { row.letter: row.code for (index, row) in data.iterrows() }

def generate():
  word = input('Enter a word: ').upper()
  try: 
    output_list = [ phonetic_dict[letter] for letter in word ]
  except KeyError:
    print('Letters only please.')
    generate()
  else:
    print(output_list)
    if (input('Try again? \n') == 'yes'):
      generate()
    
generate()