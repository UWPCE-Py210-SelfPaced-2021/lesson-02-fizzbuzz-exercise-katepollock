def fizz_buzz(n):
    """ param `n` is your upper bound parameter for generating numbers, use this variable with your range() function"""

    # Kate Pollock
    # Python 310
    # Assignment 2: FizzBuzz

    # Write a program that prints the numbers from 1 to 100 inclusive.
    # But for multiples of three print “Fizz” instead of the number.
    # For the multiples of five print “Buzz” instead of the number.
    # For numbers which are multiples of both three and five print “FizzBuzz” instead.

    for i in range(1, n + 1):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if s == '':
            print(i)
        else:
            print(s)


if __name__ == "__main__":
    fizz_buzz(100)
