def calculate_factor(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * calculate_factor(value - 1)


def fibonacci(value):
    if value == 0 or value == 1:
        return value
    else:
        return fibonacci(value - 1) + fibonacci(value - 2)


print(calculate_factor(10))


print(fibonacci(10))

