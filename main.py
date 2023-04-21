import re
from morse_code_dict import MORSE_CODE


def encrypt_message(message):
    output = ""
    for character in message:
        # add an error if character not found
        output= output + MORSE_CODE[character] + " "
    return(output.strip())

def decrypt_message(message):
    output = ''
    split_message = message.split(' / ')
    for word in split_message:
        split_word = word.split(' ')
        for character in split_word:
            output = output + list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(character)]
        output = output + ' '
    return(output.strip())

####################

message = input('Enter your message: ').upper().strip()

import re
if re.search('[^_/. -]', message):
    print("Encrypting your message...\n")
    output = encrypt_message(message)
    print(f"Your message in morse code:\n{output}")
else:
    print("Deciphering morse code... \n ")
    output = decrypt_message(message)
    print(f"The message says:\n{output}")

