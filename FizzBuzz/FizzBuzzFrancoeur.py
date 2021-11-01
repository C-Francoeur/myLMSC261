def func(count):
    for i in range(count + 1):
        if i == 0 :
            print("")
        elif i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else :
            print(i)
func(100)
