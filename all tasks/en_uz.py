db = {
    ('hello', 'hi', 'howa', 'what\'s up'): ('salom', 'assalomu aleykum', ),
    'bread': 'non',
    ('money', 'cache', 'balance'): ('pul', 'soqqa', 'mablag\''),
    'friend': 'do\'st'
}


def en_uz(word: str):
    for key in db.keys():
        if word in key:
            return db[key]
    return None 
     
    
def uz_en(word: str):
    for key, value in db.items():
        if isinstance(value, tuple):  
            if word in value: 
                return key
        elif word == value:  
            return key
    return f"this {word} is not found in my dictionary"


print(en_uz('hi'))  
print(uz_en('non'))   


