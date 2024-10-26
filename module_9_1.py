def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        # Получаем название функции
        func_name = func.__name__

        # Применяем функцию к списку и сохраняем результат в словаре
        results[func_name] = func(int_list)

    return results


def sum_(numbers):
    return sum(numbers)


def max_(numbers):
    return max(numbers)


def min_(numbers):
    return min(numbers)


def sorted_(numbers):
    return sorted(numbers)

def len_(numbers):
    return len(numbers)


# Пример использования



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))