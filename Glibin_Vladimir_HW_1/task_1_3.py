# # a = ("Процент")
# # b = ("Процента")
# # c = ("Процентов")
#
# numbs = {11,12,13,14}
# for i in range(100):
#     i = i + 1
#     if i in numbs:
#         print(i, "процентов")
#     elif i % 10 == 1:
#         print(i, "процент")
#     elif i % 10 > 1 and i % 10 <5:
#         print(i, "процента")
#     else:
#         print(i, "процентов")
def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    base_message="{}процент{}"
    if number in range(11,15):
     return base_message.format(number,"ов")

    elif number%10 ==1:
        return base_message.format(number, "")
    elif 1<number%10<5:
        return base_message.format(number, "a")
    elif number>4:
        return base_message.format(number, "ов")

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))