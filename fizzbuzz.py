
# --- FizzBuzz ---
# Ziel dieser Aufgabe ist es, den folgenden Algorithmus zu implementieren:
#
# Fuer alle Zahlen von 1 bis n:
# - Wenn die Zahl durch 3 teilbar ist, soll der String "Fizz" ausgegeben werden.
# - Wenn die Zahl durch 5 teilbar ist, soll der String "Buzz" ausgegeben werden.
# - Wenn die Zahl durch 3 und 5 teilbar ist, soll der String "FizzBuzz" ausgegeben werden.
# - Wenn keines davon zutrifft, soll einfach nur die Zahl selbst ausgegeben werden.
# - Das Ergebnis der Aufgabe soll eine Python Liste sein, die alle Ausgaben von 1 bis n enthaelt.

FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz(number): 
    result = []
    for num in range(1, number + 1):
        if is_divisible_by_three(num) and is_divisible_by_five(num):
            result.append(f"{FIZZ}{BUZZ}")
        elif is_divisible_by_three(num):
            result.append(FIZZ)
        elif is_divisible_by_five(num):
            result.append(BUZZ)
        else:
            result.append(num)
    return result


def fizzbuzz_generator(number):
    for num in range(1, number + 1):
        yield compute_fizzbuzz_value_for(num)


def compute_fizzbuzz_value_for(number):
    if is_divisible_by_three(number) and is_divisible_by_five(number):
        return f"{FIZZ}{BUZZ}"
    if is_divisible_by_three(number):
        return FIZZ
    if is_divisible_by_five(number):
        return BUZZ
    return number


def is_divisible_by_five(number):
    return number % 5 == 0


def is_divisible_by_three(number):
    return number % 3 == 0


# Unit Tests

def test_three():
    assert list(fizzbuzz_generator(3)) == [1, 2, "Fizz"]


def test_seven():
    assert list(fizzbuzz_generator(7)) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7]


def test_twenty():
    assert list(fizzbuzz_generator(20)) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]


if __name__ == '__main__':
    test_three()
    test_seven()
    test_twenty()
