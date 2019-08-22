def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
    encrypted = ''
    for i in message:
        if i == ' ':
            encrypted = encrypted + ' '
        else:
            position = alphabet.index(i)
            encrypted = encrypted + cipher[position]
    return encrypted


def main():
    message = input("What would you like to encrypt? (letters/numbers only): ")
    cipher = "badcfehgjilknmporqtsvuxwzy967384521"
    encrypted = encrypt(message, cipher)
    print(encrypted)


if __name__ == "__main__":
    main()
