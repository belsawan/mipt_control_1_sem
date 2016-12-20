try:
    print('Я живой!')
except NameError:
    try:
        print('Ой, откуда здесь NameError?')
        raise IndexError
    except IndexError:
        print('Елы палы, а Index Error откуда мог вылезти?')