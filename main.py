from morse_code_dictionary import MORSE_CODE_DICTIONARY

# Take input
text = input('what would you like to convert to morse code?\n > ').upper()

# Convert input to morse code
code = ''
for character in text:
    if character not in MORSE_CODE_DICTIONARY.keys():
        print(f'Sorry, {character} isn\'t in my morse code alphabet. I left it as is')
        code = code + character + ' '
    else:
        code = code + MORSE_CODE_DICTIONARY[character] + ' '

print(code)
