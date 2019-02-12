#
# ps6pr4.py (Problem Set 6, Problem 5)
#
# The Fibonacci sequence in Python
#
#


def fib(n):
    """takes an integer n as input, and that uses a loop to both:determine and print the first n Fibonacci numbers,
        compute and return the sum of those numbers
    """
    sum_fib = 1
    f_n_1 = 0
    f_n_2 = 1
    for i in range(n):
        if i == 0:
            print(f_n_1)
        elif i == 1:
            print(f_n_2)
        else:
            fib_num = f_n_1 + f_n_2
            f_n_1 = f_n_2
            f_n_2 = fib_num
            print(fib_num)
            sum_fib += fib_num
    return sum_fib


def main():
    """takes no inputs. The function should: ask the user how many Fibonacci numbers he or she wants to produce,
        call the fib function to generate and print those numbers,
        print the sum of the numbers (i.e., the value returned by fib).
    """
    n = input("How many Fibonacci numbers?: ")
    result = 'their sum is ' + str(fib(int(n)))
    print(result)


def test():
    """test functions above"""
    #print(fib(8))
    main()


test()
