def ubah_huruf(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
    result = []

    for char in sentence:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            is_upper = char.isupper()  # Cek apakah huruf besar
            char = char.upper()  # Ubah menjadi huruf besar untuk pencarian
            if char in alphabet:
                index = alphabet.index(char)
                shifted_char = shifted_alphabet[index]
                if not is_upper:
                    shifted_char = shifted_char.lower()  # Ubah kembali ke huruf kecil jika semula huruf kecil
                result.append(shifted_char)
            else:
                result.append(char)
        else:
            result.append(char)  # Tidak mengubah karakter selain huruf

    return ''.join(result)


if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB