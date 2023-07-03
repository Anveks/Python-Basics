import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_length = len(alphabet)

def encrypt(user_text, user_shift):
    encrypted_text = ""

    for letter in user_text:  # Looping through the whole text
        
        if letter == ' ':  # Check for space character
            encrypted_text += ' '  # Append spaces as is
            continue  # Move to the next iteration

        if letter not in alphabet:
            encrypted_text += letter
            continue

        index = alphabet.index(letter)  # Getting index of each letter

        if direction == 'encode':
            new_index = (index + user_shift) % alphabet_length # modulo will give the remainder
        elif direction == 'decode':
            new_index = (index - user_shift) % alphabet_length
        else:
            print('Something went wrong... Check all the inputs and try again.')
            return

        letter = alphabet[new_index]
        encrypted_text += letter

    print(f'The result is: {encrypted_text}')

if shift > alphabet_length:
    print('The shift cannot exceed the alphabet length!')
else:
    encrypt(text, shift)