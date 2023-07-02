
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(user_text, user_shift):
    alphabet_length = int(len(alphabet))
    encrypted_text = ""

    for letter in user_text: 
      index = int(alphabet.index(letter))
      
      if direction == 'encode':
        new_index = index + user_shift
        if (new_index > alphabet_length): new_index = user_shift - (alphabet_length - index)

      else:
        new_index = index - user_shift
        if (new_index < 0): new_index = abs(new_index)

      letter = alphabet[new_index]
      encrypted_text += letter

    print(encrypted_text)     

encrypt(text, shift)