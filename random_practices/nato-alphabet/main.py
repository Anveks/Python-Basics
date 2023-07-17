import pandas

alphabet = pandas.read_csv(r'.\random_practices\nato-alphabet\nato_phonetic_alphabet.csv')
alphabet_dict = {}

for (intex, row) in alphabet.iterrows():
  letter = row['letter']
  code = row['code']
  alphabet_dict[letter] = code

user_input = input('What word do you want to decipher?\n').upper()
input_list = list(user_input)

deciphered_input = [alphabet_dict[letter] for letter in input_list]
print(deciphered_input)