# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def divisor():
    num = input('Enter a number to get divisors of:')
    numlist = []

    num = int(num)
    i = num

    while i > 0:
        if num % i == 0:
            numlist.append(i)
        i = i-1

    print(numlist)

def main():
    divisor()
    
main()
