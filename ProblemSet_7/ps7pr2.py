#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# TT Securities
#
# Computer Science 111
#

import math


def display_menu():
    """ prints a menu of options
    """
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation of prices')
    print('(5) Find the day when min prices occurs')
    print('(6) Determine if there are any prices above a threshold')
    print('(7) Find the best day to buy and sell a stock')
    print('(8) Quit')
    print()


def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list


def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return

    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])


def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]


## Add your functions for options 3-7 below.
def avg_price(prices):
    """takes a list of 1 or more prices and computes
        and returns the average price
    """
    sum = 0
    for i in range(len(prices)):
        sum += prices[i]
    return sum / len(prices)


def std_dev(prices):
    """takes a list of 1 or more prices and computes
        and returns the standard deviation of the prices.
    """
    sum_prices = 0
    average_price = avg_price(prices)
    price_list_len = len(prices)
    for i in range(len(prices)):
        sum_prices += ((prices[i] - average_price) ** 2)/price_list_len
    return math.sqrt(sum_prices)


def min_day(prices):
    """ takes a list of 1 or more prices and computes
        and returns the day (i.e., the index) of the minimum price.
    """
    min_price = prices[0]
    index = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            index = i
            min_price = prices[i]
    return index


def any_above(prices, value):
    """takes a list of 1 or more prices and an integer threshold, and
        uses a loop to determine if there are any prices above that threshold.
    """
    for i in range(len(prices)):
        if prices[i] > value:
            return True
    return False


def find_plan(prices):
    """takes a list of 2 or more prices, and that uses one or more loops to find the best days
        on which to buy and sell the stock whose prices are given in the list of prices.
    """
    day_of_min = min_day(prices)
    profit = 0
    max_day = day_of_min
    plan = [day_of_min,  max_day, profit]
    if day_of_min == len(prices) - 1:
        return plan
    else:
        for i in range(len(prices[plan[0]:])):
            if prices[i + plan[0]] > prices[plan[1]]:
                plan[1] = i + len(prices[:plan[0]])
                print(plan[1])
        plan[2] = prices[plan[1]] - prices[plan[0]]
    return plan


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is: ', average)
        elif choice == 4:
            standard_deviation = std_dev(prices)
            print('The standard deviation of all prices is: ', standard_deviation)
        elif choice == 5:
            day_of_min = min_day(prices)
            print('The min price is ', prices[day_of_min], ' on day ',day_of_min)
        elif choice == 6:
            threshold = int(input('Please enter a threshold: '))
            if any_above(prices, threshold):
                print('There is at least one price over ', threshold)
            else:
                print('There are no prices above ', threshold)
        elif choice == 7:
            buy_sell_plan = find_plan(prices)
            print('Buy on day ', buy_sell_plan[0], ' for ', prices[buy_sell_plan[0]])
            print('Sell on day ', buy_sell_plan[1], ' for ', prices[buy_sell_plan[1]])
            print('Total profit: ', buy_sell_plan[2])
        elif choice == 8:
            False
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')


def test():
    """test functions above"""
    # print(avg_price([10, 20, 18]))
    # print(avg_price([5, 8, 5, 3]))
    # print(std_dev([10, 20, 18]))
    # print(std_dev([5, 8, 5, 3]))
    # print(min_day([20, 10, 18]))
    # print(min_day([15, 18, 12, 22, 17]))
    # print(any_above([10, 20, 15], 5))
    # print(find_plan([15, 18, 12, 17, 213, 35, 300]))


# test()
tts()
