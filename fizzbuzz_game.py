start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
for i in range (start, end):
    if (i % 3 == 0 and i % 5 == 0):
        print(str(i) + " = FizzBuzz")
    else:
        if (i % 3 == 0):
            print(str(i) + " = Fizz")
        else:
            if (i % 5 == 0):
                print(str(i) + " = Buzz")