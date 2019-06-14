def count(num):
    while num <= 100:
        if num == 1:
            print(num)
            num += 1
        test1 = (num % 4)
        test2 = (num % 5)
        test3 = ((num - 1) % 4)
        test4 = ((num - 1) % 5)
        test5 = ((num + 1) % 4)
        test6 = ((num + 1) % 5)
        if test1 == 0 and test6 == 0:
            print("FizzBuzz")
        elif test2 == 0 and test5 == 0:
            print("BuzzFizz")
        elif test1 == 0 and test2 == 0:
            print("BizzFuzz")
        elif test1 == 0 and not test4 == 0:
            print("Fizz")
        elif test2 == 0 and not test3 == 0:
            print("Buzz")
        elif test5 == 0 and test6 == 0:
            print("Bizz")
        elif test3 == 0 and test4 == 0:
            print("Fuzz")
        else:
            print(num)
        num += 1


count(1)
