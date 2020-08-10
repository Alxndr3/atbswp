def collatz(number):
    if number % 2 != 1:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result


while True:
    try:
        num = int(input('Type an integer number: '))
        result = collatz(num)
        print(result)
        if result == 1:
            break
    except ValueError:
        print('You did not typed a valid number')
        continue
