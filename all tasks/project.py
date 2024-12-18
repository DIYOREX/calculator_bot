db = {'salom*assalomu aleykum*somalekum': 'hello*hi*hova you*what\'s up'}


def mood() -> bool:
    return input('Do you wanna use dict  (yes/no) : ').startswith('y')


def swap(search: str, result: str, choice: str) -> tuple:
    if choice == '1':
        search, result = result, search
    return search, result


def get_item_as_list(message: str, splitter: str = '*') -> list:
    return message.split(splitter)


def run():
    _mood = True
    while _mood:
        choice = input('Do you use dict (en-uz/uz-en 1/2) : ')
        if choice not in ['1', '2']:
            print('Incorrect choice.Choice must be [1,2]')
            continue
        word = input('...')
        for search, result in db.items():
            search, result = swap(search, result, choice)  # choice = 1 , search
            keys = get_item_as_list(search)
            if word in keys:
                print(get_item_as_list(result))
                break
        else:
            print('Sorry.We do not find this word')
        _mood = mood()

    else:
        print('Come Back again')


if __name__ == '__main__':
    run()
