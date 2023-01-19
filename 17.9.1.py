numbers = input("Введите список чисел через пробел: ")
number = int(input("Введите любое число: "))
is_sort = False

try:
    if "," in numbers:
        raise ValueError
except ValueError:
    print("Ошибка при вводе данных. Попробуйте снова.")
    raise

numbers = list(map(int, numbers.split()))

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

try:
    if number > numbers[-1]:
        raise IndexError
except IndexError:
    print("Введенное вами число больше максимального числа указанного в списке, попробуйте снова.")
    raise

print("Отсортированный список чисел: ", numbers)
print()