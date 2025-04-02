# Get number of words from a file
# ------------------------------------------
def get_num_words (file):
    count = 0
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            count += 1
        print(f"Found {count} total words")

# Get number of characters from a file
def get_characters_count(files):
    alphabet = {}
    with open(files) as f:
        file_contents = f.read()
        characters = file_contents.lower()

        for letter in characters:
            alphabet[letter] = alphabet.get(letter, 0) + 1

    sorted_alphabet = dict(sorted(alphabet.items(),key=lambda x: x[1] ,reverse=True))
    for high in sorted_alphabet:
        print(f"{high}: {sorted_alphabet[high]}")
