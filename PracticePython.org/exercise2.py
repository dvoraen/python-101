#exercise2.py

number = input("Give me a number: ")
number = int(number)

if number % 2 == 0:
    print("The number %d is even!" % number)
    if number % 4 == 0:
        print("It's also a multiple of four!")
else:
    print("The number %d is odd!" % number)