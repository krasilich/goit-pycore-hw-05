from task1 import caching_fibonacci
from task2 import sum_profit, generator_numbers

if __name__ == '__main__':
    # Example of usage Task 1
    # fib = caching_fibonacci()
    # print(fib(10))
    # print(fib(15))

    # Example of usage Task 2
    text = ("Загальний дохід працівника складається з декількох частин: 1000.01 "
            "як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
    print(sum_profit(text, generator_numbers))
