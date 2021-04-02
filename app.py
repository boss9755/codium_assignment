# 1.Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
def function_A():
    for x in range(100):
        x = x+1
        if (x%3 == 0 and x%5 == 0):
            print("FizzBuzz", end = " ")
        elif (x%3 == 0):
            print("Fizz", end = " ")
        elif (x%5 == 0):
            print("Buzz", end = " ")
        else:
            print(x, end = " ")

# 2.Write a program that determine whether or not an integer input is a leap year.
def function_B():
    while(1):
        buffer = input("\nEnter year (Press 'Enter' to exit): ")
        if buffer == "":
            break
        year = int(buffer)
        if (year % 400 == 0):
            print("true")
        elif (year % 400 != 0 and year % 100 != 0 and year % 4 == 0):
            print("true")
        else:
            print("false")

# Write a program that produce the following output giving an integer input n.
# 3.1
def function_C1():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(n):
                for j in range(i+1):
                    print("*",end = "")
                print("")

# 3.2
def function_C2():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            k = 2*n-2
            for i in range(n):
                for j in range(k):
                    print(end = " ")
                k = k-2
                for j in range(i+1):
                    print("*", end = " ")
                print("")

# 3.3
def function_C3():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(1,n+1):
                for j in range(i,n):
                    print(" ", end="")
                print("*", end="")
                k = 1
                while k < 2 * (i - 1):
                    print(" ",end="")
                    k += 1
                if i == 1:
                    print("")
                else:
                    print('*')

# 3.4
def function_C4():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)

# 3.5
def function_C5():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)

# 3.6
def function_C6():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)

# Write a program that finds all prime numbers up to n for input n. 
def function_D():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            print(n,"->", end=" ")
            for i in range(2, n+1):
                if i > 1:
                    for j in range(2,i):
                        if (i % j == 0):
                            break
                    else:
                        print(i, end=" ")
        print("")

#function_A()
#function_B()
#function_C1()
#function_C2()
#function_C3()
#function_C4()
#function_D()