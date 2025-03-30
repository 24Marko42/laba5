# Отсортировать последовательность целых чисел по убыванию
# модуля числа

def sort_by_abs_desc(numbers):
    return sorted(numbers, key=abs, reverse=True)

# key — это аргумент, который позволяет задать правило сортировки.
# Опция reverse=True меняет порядок сортировки с по возрастанию (по умолчанию) на по убыванию.

numbers = [3, -7, 2, -9, 1, 8, -6]
sorted_numbers = sort_by_abs_desc(numbers)
print(sorted_numbers)
