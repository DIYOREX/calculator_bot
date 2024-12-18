dictionary = {
    'apple': 'olma',
    'lion': 'sher',
    'people': 'odam',
    'laptop': 'noutbook',
}

while True:
    thing = input('Do you want to use this dictionary? Yes/No: ')
    if thing.lower() == 'no':
        break
    elif thing.lower() == 'yes':
        word = input("Enter a word: ").lower() 
        if word in dictionary:
            print(f"english => {word} : uzbek => {dictionary[word]}")
        else:
            print("This word is not found in the dictionary.")

          