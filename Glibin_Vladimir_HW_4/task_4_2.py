import requests

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_text = response.text

    offset = response.text.find(code)

    if offset == -1:
        return
    offset_nominal = response.text.find('<Value>', offset) + 7
    nominal_str = ''

    for i in range(0, 7):
        nominal_char = response_text[i + offset_nominal]
        if nominal_char.isnumeric():
            nominal_str += nominal_char
        elif nominal_char == ',':
            nominal_str += '.'

    result_value = float(nominal_str)  ## здесь должно оказаться результирующее значение float
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))