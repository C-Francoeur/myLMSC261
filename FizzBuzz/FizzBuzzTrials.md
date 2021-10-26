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

Next I tried to replace x with i. My DEFINED variable. I felt like an idiot for not realizing, but once I replaced it suddenly everything began to print again.

def func(count):
    for i in range(count + 1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
            print(count)

This led to...

FizzBuzz
Fizz
Buzz
100
Fizz
Fizz
Buzz
100

This mess.
I had A MILLION 100s, but I didn't want 100. I wanted 1-100. Then I realized I was printing the "count", NOT the integers, duhhh.

So I instead tried

def func(count):
    for i in range(count + 1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
            print(i)

This was ALOT closer, but still was a little wonky, i.e.

FizzBuzz
Fizz
Buzz
5
Fizz
Fizz
Buzz
10
Fizz
FizzBuzz
Fizz
Buzz
20

My next attempt was

def func(count):
    for i in range(count + 1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else :
            print(i)

I almost cried...
Just by adding a lil else statement to the end, I was able to print the WHOLE ENTIRE string of Fizzes, Buzzes, and FizzBuzzes. There was just one problem.

FizzBuzz
1
2
Fizz
4
Buzz

My zero value was being print as well, so I added a little extra code.

def func(count):
    for i in range(count + 1):
        if i == 0 :
            print(" ")
        elif i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else :
            print(i)
And, BOOM!

1
2
Fizz
4
Buzz

I DID IT!!!!!


Everything printed just as I wanted, and I was finally able to rest... a little...



To conclude, I was eventually able to get to the answer on my own. I always get frustrated when other people do things faster than me, but I did get everything to work in the end. Probably in the most basic way, but whatevs. At least my code prints?
I wish I could be more creative with my coding as I do find it rather embarrassing that I always seem to have the lowest common denominator when it comes to functioning code. I guess everyone starts somewhere though? And at least I always seem to come to an answer on my own in the end. Even though sometimes I wish people would just tell me whats wrong.

I will admit that coming to my own conclusion is satisfying though.
