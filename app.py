# Benjapol Suriyachantananont
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
            for i in range(1,n+1):
                print("*"*i)

# 3.2
def function_C2():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(1,n+1):
                print(" "*(n-i) + "*"*i)

# 3.3
def function_C3():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(1,n+1):
                if (i == 1):
                    print(" "*(n-i) + "*" + " "*(n-i))
                else:
                    print(" "*(n-i) + "*" + " "*(2*i-3) + "*")
# 3.4
def function_C4():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if (i == j or i+j == n+1):
                        print("*",end="")
                    else:
                        print(" ",end="")
                print()

# 3.5
def function_C5():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            for i in range(1,n+1) :
                if (i%2!=0):
                    x = (n - i)//2
                    print(" "*x + "*"*i + " "*x)
            for j in range(n-1, 0, -1) :
                if (j%2!=0):
                    x = (n-j)//2
                    print(" "*x + "*"*j + " "*x)
# 3.6
def function_C6():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)

            
# 4. What's the difference between else and finally in exception handling?
def function_D():
    print("In else, if exception is raised then this code will not run.")
    print("But in finally, if exception is raised then this code still run")

# Write a program that finds all prime numbers up to n for input n. 
def function_E():
    while(1):
        buffer = input("Enter the number (Press 'Enter' to exit): ")
        if buffer == "":
            break
        else:
            n = int(buffer)
            print(n,"->", end=" ")
            for i in range(2, n+1):
                for j in range(2,i):
                    if (i % j == 0):
                        break
                else:
                    print(i, end=" ")
        print()

while(1):
    print("\nWelcome to the program")
    print("Press '1' to answer Question 1")
    print("Press '2' to answer Question 2")
    print("Press '3.1' to answer Question 3.1")
    print("Press '3.2' to answer Question 3.2")
    print("Press '3.3' to answer Question 3.3")
    print("Press '3.4' to answer Question 3.4")
    print("Press '3.5' to answer Question 3.5")
    print("Press '3.6' to answer Question 3.6")
    print("Press '4' to answer Question 4")
    print("Press '5' to answer Question 5")
    select = input("Select the task (press 'Enter' to exit): ")
    if select == "":
        break
    else:
        if select == "1":
           function_A()
        elif select == "2":
            function_B()
        elif select == "3.1":
            function_C1()
        elif select == "3.2":
            function_C2()
        elif select == "3.3":
            function_C3()
        elif select == "3.4":
            function_C4()
        elif select == "3.5":
            function_C5()
        elif select == "3.6":
            function_C6()
        elif select == "4":
            function_D()
        elif select == "5":
            function_E()
        else:
            print("Please select again!")
