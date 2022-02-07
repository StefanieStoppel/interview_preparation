
# --- FizzBuzz ---
# Ziel dieser Aufgabe ist es, den folgenden Algorithmus zu implementieren:
#
# Fuer alle Zahlen von 1 bis n:
# - Wenn die Zahl durch 3 teilbar ist, soll der String "Fizz" ausgegeben werden.
# - Wenn die Zahl durch 5 teilbar ist, soll der String "Buzz" ausgegeben werden.
# - Wenn die Zahl durch 3 und 5 teilbar ist, soll der String "FizzBuzz" ausgegeben werden.
# - Wenn keines davon zutrifft, soll einfach nur die Zahl selbst ausgegeben werden.
# - Das Ergebnis der Aufgabe soll eine Python Liste sein, die alle Ausgaben von 0 bis n enthaelt.

FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz(number): 
    result = []
    for number in range(1, number + 1):
        if is_divisible_by_three(number) and is_divisible_by_five(number) == 0:
            result.append(f"{FIZZ}{BUZZ}")
        elif is_divisible_by_three(number):
            result.append(FIZZ)
        elif is_divisible_by_five(number):
            result.append(BUZZ)
        else:
            result.append(number)
    return result

def is_divisible_by_five(number):
    return number % 5

def is_divisible_by_three(number):
    return number % 3 == 0


# Unit Tests

def test_three():
    assert fizzbuzz(3) == [1, 2, "Fizz"]

def test_seven():
    assert fizzbuzz(7) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7]

def test_twenty():
    assert fizzbuzz(20) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]

if __name__ == '__main__':
    test_three()
    test_seven()
    test_twenty()