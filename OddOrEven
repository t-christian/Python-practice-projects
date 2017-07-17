# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

# Choose which problem to solve
def chooseProblem():
  choice = str(input('Select to check if a (S)ingle number is even/odd, or check if (T)wo numbers divide evenly'))
  if choice == 's' or choice == 'S':
    oddoreven()
  elif choice == 't' or choice == 'T':
    twonumcheck()
  # Make sure to use one of the selections.
  else:
    print('Invalid input')

def twonumcheck():
  num = int(input('Choose a number to be divided:'))
  check = int(input('Choose second number to divide by first number by:'))
  
  if num % check == 0:
    print(str(num) + ' divided by ' + str(check) + ' divides evenly.')
  else:
    print(str(num) + ' divided by ' + str(check) + ' leaves a remainder of ' + str(num % check)) 
    
def oddoreven():
  num = int(input('Choose a number to check if even or odd:'))
  
  if num % 2 == 0:
    print('The number ' + str(num) + ' is even.')
    # It should only be divisible by 4 if it's divisible by 2.
    if num % 4 == 0:
      print('Also, the number ' + str(num) + ' also is cleanly divisible by 4.')
  else:
    print('The number ' + str(num) + ' is odd.')
# In case other functions are added.    
def main():
  chooseProblem()
  
main()
