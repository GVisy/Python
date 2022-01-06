def num_translate(num: str) -> str:
    """переводит числительное с английского на русский """
    num = {'zero': "нуль",
            "one": 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    print(num.get(input('Enter a value from zero to ten \n')))
    str_out = ""
    return str_out


# print(num.get(input('Enter a value from zero to ten \n')))
# input('Enter a value from zero to ten \n')
print(num_translate("one"))
print(num_translate("eight"))