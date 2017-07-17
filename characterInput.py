# From http://www.practicepython.org/
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Stupid library to actually get the date
# TODO: figure out how to properly use datetime
import datetime

# Ask and figure out how old we are
# Only need year, but get exact date for practice
def getcurrentage():
    birthyear = input('What year were you born?')
    birthmonth = input('What month were you born? (1 to 12)')
    birthday = input('What day of the month were you born? (1 to 31)')

# return the three numbers we'll need
    return birthyear, birthmonth, birthday

def when100():
    #How old are we?
    birthyear,birthmonth,birthday = getcurrentage()
    
    # Which day is it? Only call when calculation is run
    # In case of weird stuff like running the program
    # a few seconds before midnight for best practices
    now = datetime.datetime.now()
    
    # Convert everything to a *&^@# string because it wouldn't work otherwise
    thisyear = str(now.year)
    thismonth = str(now.month)
    thisday = str(now.day)
    youryear = str(birthyear)
    yourmonth = str(birthmonth)
    yourday = str(birthday)
    year100 = str(int(birthyear) + 100)

    # TODO: Figure out exact point in the year in case their birthday has passed.
    # TODO: Get amount of days passed in year already?
    # TODO: Leap years?
    # TODO: Make list of month lengths?

    # List of months to convert gibberish to readable english
    months = ['January','February','March','April','May','June','July',
              'August','September','October','November','December']
              
    #Get month name from list at index minus one (No zero month)
    print ('Today is ' + months[int(thismonth)-1] + ' ' + thisday+ ', ' + thisyear)
    print ('You were born on ' + months[int(yourmonth)-1] + ' ' + yourday + ', ' + youryear)

    #Someone is going to put in a %$#$%@ year, plan ahead
    if (int(birthyear) + 100) < int(now.year):
        print("You turned 100 in " + year100)
    else:
        print ("You'll turn 100 in " + year100)

#Start from custom function in case more are added later
def main():
    when100()

main()
