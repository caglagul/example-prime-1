def isprime(x):
    counter = 0
    for i in range(2, x):
        if x % i == 0:
            counter = counter + 1

    if counter == 0:
        print("True! It is a prime number.")

    else:
        print("False! It is not a prime number.")

while True:
    x = int(input("Enter a number:"))
    if x>0:
        if x % 2 == 0:
            print("This number is an even number.")
        else:
            print("This number is an odd number.")
    if x>1:
        isprime(x)
        break
    else:
        print("Please enter a number higher than 1.")
#commit