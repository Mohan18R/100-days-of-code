# text_to_morse.py

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '|'
}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')  # Handle characters that are not in the dictionary
            print(f"Warning: Character '{char}' not supported, ignoring.")
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    words = morse_code.split('|')
    decoded_message = []
    for word in words:
        characters = word.split()
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(char, '') for char in characters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

def is_morse_code(input_str):
    # Morse code characters include dots, dashes, spaces, and the separator '|'
    return all(char in '.-| ' for char in input_str)

def main():
    user_input = input("Enter text or Morse code: ")

    if is_morse_code(user_input):
        result = morse_to_text(user_input)
        print(f"Decoded Text: {result}")
    else:
        result = text_to_morse(user_input)
        print(f"Morse Code: {result}")

if __name__ == "__main__":
    main()
