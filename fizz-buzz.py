def fizz_buzz(input: int):
    if not (input % 3) and not (input % 5):
        return "FizzBuzz"
    if not (input % 3) and (input % 5):
        return "Fizz"
    if (input % 3) and not (input % 5):
        return "Buzz"
    return input


print(fizz_buzz(5))
print(fizz_buzz(9))
print(fizz_buzz(15))
print(fizz_buzz(7))
