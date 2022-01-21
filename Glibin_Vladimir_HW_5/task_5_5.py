# ```
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# ```

def get_uniq_numbers(src: list):
    tmp = set()
    uniq = set()
    for el in src:
        if el in tmp:
            uniq.discard(el)
        else:
            uniq.add(el)
            tmp.add(el)
    return [x for x in src if x in uniq]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
