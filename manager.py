from morse_code_dict import MORSE_CODE


class Encrypter():
    def __init__(self):
        self.decrypted_message = None
        self.error = False
        self.invalid_letters = []

    def encrypt_message(self, message):
        self.invalid_letters = []
        self.encrypted_message = ""
        for character in message:
            try:
                self.encrypted_message = self.encrypted_message + MORSE_CODE[character] + " "
            except KeyError: # if character not in dictionary
                self.error = True
                self.invalid_letters.append(character)

    def decrypt_message(self, message):
        self.invalid_letters = []
        self.error = False
        self.decrypted_message = ""
        split_message = message.split(' / ')
        for word in split_message:
            split_word = word.split(' ')
            for character in split_word:
                try:
                    self.decrypted_message = self.decrypted_message + list(MORSE_CODE.keys())[
                        list(MORSE_CODE.values()).index(character)]
                except ValueError: # if code not in dictionary
                    self.error = True
                    self.invalid_letters.append(character)

            self.decrypted_message = self.decrypted_message + ' '
