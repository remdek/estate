from django.utils.crypto import get_random_string


def generateRandomString(num, rus=False, digits=False):
    import random
    if rus:
        letters = 'цукенгзхфывапрлдячсмитбюЦУКЕНГЗХФЫВАПРЛДЯЧСМИТБЮ123456789'
        return ''.join((random.choice(letters) for i in range(num)))
    if digits:
        numbers = '123456789'
        return ''.join((random.choice(numbers) for i in range(num)))
    random = get_random_string(length=num)
    return random