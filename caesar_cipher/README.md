TODOs

I
Create a function called 'encrypt()' that takes 'original_text' and 'shift_count' as 2 inputs.
Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.

e.g.
plain_text = "hello"
shift_amount=1
encrypted encoded result should be: ifmmp
where each of the letters of 'hello' is shifted up by 1

II
Create a function called 'decrypt()' that takes 'original_text' and 'shift_count' as 2 inputs.
Inside the 'decrypt()' function, shift each letter of the 'original_text' backwards in the alphabet by the shift amount and print the decrypted text.

III
Combine the 'encrypt()' and 'decrypt()' functions into a  single function called 'caesar_cipher()'
Use the value of the user chosen direction variable to determine which functionality to use.
Call the 'caesar_cipher()' function instead of encrypt/decrypt and passing all three variables
e.g. direction, text, shift