number = 15
generator = (number for number in range(1, number + 1, 2)
             if number % 2 != 0)
print(number)
