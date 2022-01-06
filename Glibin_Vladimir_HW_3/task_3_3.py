def thesaurus(*args) -> dict:
    set_names = {name.title() for name in args}
    first_letter = [name[0].upper() for name in set_names]
    dict_out = {k: list() for k in first_letter}
    for name in set_names:
        dict_out[name[0]].append(name)
    return dict_out


print(thesaurus("Иван", "Мария", "петр", "Илья", "Илья", "Олег"))