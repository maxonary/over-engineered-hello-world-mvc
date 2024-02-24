def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                char_code -= 97
                char_code %= 26
                char_code += 97
            elif char.isupper():
                char_code -= 65
                char_code %= 26
                char_code += 65
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text
