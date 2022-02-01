import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([a-zA-Z0-9\.\-\_]*)@([a-z\.\-\_]*\.(ru|com))')
    search = re.search(RE_MAIL, email)
    if search is None:
        raise ValueError('Error email')
    else:
        return {'username': search.group(1), 'domain': search.group(2)}


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
