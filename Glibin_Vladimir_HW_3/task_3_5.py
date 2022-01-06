from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    for i in range(count):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        list_out = f'{random_index} {random_index_1} {random_index_2}'
        # list_out = ''
        print(list_out)

        # return list_out


print(get_jokes(3))
