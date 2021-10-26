I hate this project.

I tried to use int(integer), but found out that I needed to use a counter instead of a single value.

I took the lovely code.

def func(count):
  for i in range(count + 1):
    print(f"{count - i} Lovely!")
///
func(???)

and created some if else statements

if x % 3 == 0 and x % 5 == 0 :
           print("FizzBuzz")
       elif x % 3 == 0 :
           print("Fizz")
       elif x % 5 == 0 :
           print("Buzz")



I still couldn't get anything to print because I didn't know where in relation to my counter to put the statements.

I tried this

def func(count):
    for i in range(count + 1):
        if x % 3 == 0 and x % 5 == 0 :
            print("FizzBuzz")
        elif x % 3 == 0 :
            print("Fizz")
        elif x % 5 == 0 :
            print("Buzz")
        else print(count)

and This

def func(count):
    for i in range(count + 1):
        if x % 3 == 0 and x % 5 == 0 :
            print("FizzBuzz")
        elif x % 3 == 0 :
            print("Fizz")
        elif x % 5 == 0 :
            print("Buzz")
        else print(count)

        def func(count):
            for i in range(count + 1):
                if x % 3 == 0 and x % 5 == 0 :
                    print("FizzBuzz")
                elif x % 3 == 0 :
                    print("Fizz")
                elif x % 5 == 0 :
                    print("Buzz")
                else
                print(count)

The syntax error keeps on appearing between else and print and I have no idea why and it's extremely frustrating because it feels like no matter what I do I always end up with something wrong. Which is really, really sucky, because no one wants to feel like they're always wrong because when you feel like you're always wrong you feel like a idiot. And when you feel like an idiot you feel like you're never going to succeed and if you're never going to succeed anyways than whats the point in even trying in the first place.


After banging my head against the wall for what felt like hours I had a breakthrough

REMOVE THE LAST else

def func(count):
    for i in range(count + 1):
        if x % 3 == 0 and x % 5 == 0 :
            print("FizzBuzz")
        elif x % 3 == 0 :
            print("Fizz")
        elif x % 5 == 0 :
            print("Buzz")
            print(count)

This began printing my function but I ran into a new problem. x remained undefined.
