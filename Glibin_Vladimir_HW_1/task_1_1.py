def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    sec = duration % 60
    mins = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400

    if days > 0:
        result = f'{days}дн {hours}час {mins} мин {sec}сек'
    elif hours > 0:
        result = f'{hours}час {mins} мин {sec}сек'
    elif mins > 0:
        result = f'{mins} мин {sec}сек'
    else:
        result = f'{sec}сек'
    return result


duration = int(input("Введите время в секундах: \n"))
result = convert_time(duration)
print(result)
