numbers = [15, 20, 8, 19, 25, 12]
result = list(filter(lambda x: x < 5, numbers))
result2 = list(map(lambda x: x / 2, numbers))
result3 = list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers)))


numbers2 = range(10, 100)  # Все двузначные числа

result4 = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0, numbers2)))
print(result)
print(result2)
print(result3)
print(result4)