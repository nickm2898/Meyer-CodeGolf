def count(num):
    while num <= 100:
        test1 = num % 3
        test2 = num % 5
        if test1 == 0 and test2 == 0:
            print("FizzBuzz")
            num += 1
        elif test1 == 0:
            print("Fizz")
            num += 1
        elif test2 == 0:
            print("Buzz")
            num += 1
        else:
            print(num)
            num += 1


count(1)
