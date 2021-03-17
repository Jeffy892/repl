## Coding Exercise

# 1. Write a function that returns the maximum of two numbers
def max(a,b):
    if a > b:
        return a
    else:
        return b

print(max(5, 6))

# 2. Write a function called fizz_buzz that takes a number. 
def fizz_buzz(val):
    if val % 3 == 0:
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    elif (val % 3) == 0 and (val % 5) == 0:
        return "FizzBuzz"
    else:
        return val

for x in range(10): 
    print(fizz_buzz(x))

# 3.	Write a function for checking the speed of drivers. This function should have one parameter: speed. 

def checkSpeed(speed):
    points = 0
    if speed < 70:
        print("OK")
    elif speed > 70:
        speed_above_70 = speed - 70
        points += speed_above_70 / 5

        if points >= 12:
            print("Liscense Suspended!")

#for x in range(60, 300, 5):
#    day2.checkSpeed(x)


# 4. 4.	Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 

def showNumbers(limit):
    for x in range(0, limit+1):
        if x % 2 == 0:
            print("%d EVEN" % x)
        else:
            print("%d ODD" % x)

showNumbers(20)

# 5. 5.	Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20. 

def sumOfNum(limit):
    sum = 0
    for x in range(0, limit+1):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum
print(sumOfNum(20))

# 6. Write a function called show_stars(rows).

def show_stars(rows):
    for x in range(1, rows+1):
        print("*" * x)

show_stars(5)

# 7. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter. 

def prime(limit):
    for num in range(0, limit + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

prime(20)