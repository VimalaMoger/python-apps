from caesar_cipher_logo import logo
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode to encrypt or decode to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(original_text, shift_count):
    encoded_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encoded_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_count
            shifted_position %= len(alphabet)
            encoded_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {encoded_text}")

def decrypt(original_text, shift_count):
    decoded_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decoded_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_count
            shifted_position %= len(alphabet)
            decoded_text += alphabet[shifted_position]

    print(f"Here is the decoded result: {decoded_text}")

def caesar_cipher(direction, original_text, shift_count):
    cipher_text = ""
    if direction == "decode":
        shift_count *= -1       # b * -1 = -b

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_count  # a + (-b)
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {direction}d result: {cipher_text}")

if __name__ == '__main__':
    # encrypt(original_text=text, shift_count=shift)
    # decrypt(original_text=text, shift_count=shift)
    caesar_cipher(direction, text, shift)
