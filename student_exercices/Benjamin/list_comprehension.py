from string import ascii_lowercase as alphabet

text = 'this is a normal text'


def caesar_encrypt(some_text, delta):
    encrypted_text = ''

    for letter in some_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter_index += delta
            if letter_index // 25 > 1:
                letter_index -= 1
            letter_index %= 25
            encrypted_text += alphabet[letter_index]
        else:
            encrypted_text += letter

    return encrypted_text


def caesar_encrypt_short(some_text, delta):
    encrypted_text = ''.join([alphabet[(alphabet.index(letter) + delta) % 25] if letter in alphabet else letter for letter in some_text])
    return encrypted_text


print(caesar_encrypt_short(text, 1))
