# Jacob Price
# CS115U-J101
# Spring 2023
# Programming Assignment 3
#
#
# Program discription 
#
# This program will ask the user the day of their reservation, the hours portion
# time of their reservation(in military time 0-23), as well as the minutes
# portion time of their reservation, then the program will display when the  
# reservation the user entered is and if the restaurant will be opened or closed
# that day, if the restaurant is closed the program will display the next time 
# the restaurant will be open and the special of that day, if the restaurant is 
# open the program will display that its open and the special for that time
#
#
# Program Perconditions
#
# 1. the user will enter what day they want the reservation to be on, 
#    in a string format, to be called dayOfReservation
#
# 2. the user will enter the hours portion of when the reservation is,
#    in military time 0-23, to be called hourOfReservation
#
# 3. the user will enter the minutes portion of when the reservation is,
#    0-59, to be called minutesOfReservation
#
#
# Program Postconditions
#
# 1. the program will display the day and time (minutes & hours) the reservation
#    is placed on, the hours portion will be displayed in AM/PM
#
# 2. the program will display if the restaurant will be open or closed during
#    the time that the user has entered, if the restaurant is closed it will 
#    display that it is closed and the next time the restaurant is open as well
#    as thespecial for that day, if the restaurant is open the program will
#    display that it is open and the special for the day 





# Variable Dictionary
#
# 1. userDayOfReservation  ----  the day the reservation will be on, as given by
#                                the user, (monday,tuesday,wednesday,thursday,
#                                friday,saturday,sunday)
#
# 2. userHourOfReservation  ---  the hours portion of time the reservation will    
#                                be placed, as given by the user,
#                                a whole number(0-23)
#
# 3. userMinutesOfReservation -  the minutes portion of time the reservation
#                                will be on, as given by the user,
#                                a whole number(0-59)
#
# 4. dayOfReservation  ----  the day of the reservation after it has been data
#                            validated 
#
# 5. hourOfReservation  ---  the hour portion of time of the reservation after
#                            it has been validated 
#
# 6. minutesOfReservation -  the minutes portion of time of the reservation 
#                            after it has been validated 
#
# 7. morningOrNight  ------  the variable that stores whether the civilian time
#                            is in AM or PM 
#
# 8. civilianTime  --------  the time of the users reservation in a 12 hour 
#                            clock scale (AM/PM)
#
# 9. special  -------------  the special menu food item for each day and time 





# display the program name and version, as well as the creator of the program
# and the year the program was made
print('''Minerva's Mediterranean Restaurant Reservation Program, version 1.0
         (c) 2023, (Jacob Price)\n''')

# print a statement that asks the user to fill out the following questions
print("For your desired reservation, please: \n")


# Input Section using selection control structures for
# default range-checking data validatition


# ask for and get the day the user would like to make a reservation at
# the restaurant 
userDayOfReservation = input("Enter the day: ")

# check for what day the user inputed, first check for monday 
if userDayOfReservation == 'Monday':
    dayOfReservation = 'Monday'
    
# its not monday, now check for tuesday 
elif userDayOfReservation == 'Tuesday':
    dayOfReservation = 'Tuesday'
    
# its not tuesday, now check for wednesday 
elif userDayOfReservation == 'Wednesday':
    dayOfReservation = 'Wednesday'
    
# its not wednesday, now check for thursday 
elif userDayOfReservation == 'Thursday':
    dayOfReservation = 'Thursday'
    
# its not thursday, now check for friday 
elif userDayOfReservation == 'Friday':
    dayOfReservation = 'Friday'
    
# its not friday, now check for saturday
elif userDayOfReservation == 'Saturday':
    dayOfReservation = 'Saturday'
    
# its not saturday, now check for sunday
elif userDayOfReservation == 'Sunday':
    dayOfReservation = 'Sunday'
    
# the user did not enter a valid input, set day to default
else:
    dayOfReservation = 'Monday' 


# ask for and get the hours portion of the reservation from the user
# in military time
userHourOfReservation = int(input("Enter the hours portion of the time: "))

# see if the user entered a positive number that is less than 24
if userHourOfReservation >= 0 and userHourOfReservation <= 23:
    hourOfReservation = userHourOfReservation
# the user did not enter a valid number, set to default
else:
    hourOfReservation = 12


# ask for and get the minutes portion of the reservation from the user 
userMinutesOfReservation = int(input("Enter the minutes portion of the time: "))

# see if the user entered a positive number that is less than 60 
if userMinutesOfReservation > 0 and userMinutesOfReservation <= 59:
    minutesOfReservation = userMinutesOfReservation
    
elif userMinutesOfReservation == 0:
    minutesOfReservation = '00'
# the user did not enter a valid number, set to default 
else:
    minutesOfReservation = '00'


# Process Section


# determine if the military time the user put in will be in Am or PM
# in "civilian time" by seeing if hourOfReservation is greater than
# or equivalent to 12
if hourOfReservation >= 12:
    morningOrNight = 'PM.\n'
    
#  the hourOfReservation is less than 12 so the reservation will be in the AM
else:
    morningOrNight = 'AM.\n'




 # convert military time to a civilian 12 hour clock
if hourOfReservation == 0:
    civilianTime = 12
elif hourOfReservation > 12:
    civilianTime = hourOfReservation - 12
else:
    civilianTime = hourOfReservation



# Output Section

# display the day of the reservation and the time of the reservation in AM/PM
print('\nYou have requested a reservation for',dayOfReservation,'at', \
      civilianTime,':',minutesOfReservation,morningOrNight)



# see what day of the week the user would like to make a reservation
if dayOfReservation == 'Monday':
    
    # set the special for monday 
    special = 'Hummus with Pita Bread.'
    
    # see if the restaurant will be open when the user requested 
    if hourOfReservation >= 11 and hourOfReservation < 15:
        print('''All right! We'll be open for lunch then!
Our special will be''',special)
        
    # the restaurant will not be open when the user requested    
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Monday.
At that time, our special will be Hummus with Pita Bread.''')
        
    # the restaurant will not be open when the user requested
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Tuesday.
At that time, our special will be Moussaka with Zucchini.''')
        
# see what day of the week the user would like to make a reservation
elif dayOfReservation == 'Tuesday':

    # set the special for tuesday 
    special = 'Moussaka with Zucchini.'
    
    # see if the restaurant will be open when the user requested
    if hourOfReservation >= 11 and hourOfReservation < 15:
        print('''All right! We'll be open for lunch then!
Our special will be''',special)
        
    # the restaurant will not be open when the user requested 
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Tuesday.
At that time, our special will be Moussaka with Zucchini.''')
        
    # the restaurant will not be open when the user requested 
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Wednesday.
At that time, our special will be Falafel with Tahini Sauce.''')
        
# see what day of the week the user would like to make a reservation        
elif dayOfReservation == 'Wednesday':
    
    # set the special for wednesday 
    special = 'Falafel with Tahini Sauce.'

    # see if the restaurant will be open when the user requested 
    if hourOfReservation >= 11 and hourOfReservation < 15:
        print('''All right! We'll be open for lunch then!
Our special will be''',special)

    # the restaurant will not be open when the user requested
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Wednesday.
At that time, our special will be Falafel with Tahini Sauce.''')

    # the restaurant will not be open when the user requested 
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Thursday.
At that time, our special will be Calamari with Tomatoes.''')
        
# see what day of the week the user would like to make a reservation        
elif dayOfReservation == 'Thursday':

    # set the special for thursday 
    special = 'Calamari with Tomatoes.'

    # see if the restaurant will be open when the user requested 
    if hourOfReservation >= 11 and hourOfReservation < 15:
        print('''All right! We'll be open for lunch then!
Our special will be''',special)

    # the restaurant will not be open when the user requested 
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Thursday.
At that time, our special will be Calamari with Tomatoes.''')

    # the restaurant will not be open when the user requested 
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Friday.
At that time, our special will be Souvlaki with Tzatziki Sauce.''')

# see what day of the week the user would like to make a reservation
elif dayOfReservation == 'Friday':

    # set the special for friday at lunch time 
    special = 'Souvlaki with Tzatziki Sauce.'

    # see if the restaurant will be open for lunch on friday 
    if hourOfReservation >= 11 and hourOfReservation < 15:
        print('''All right! We'll be open for lunch then!
Our special will be''',special)

    # the restaurant will not be open when the user requested 
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Friday.
At that time, our special will be Souvlaki with Tzatziki Sauce.''')

    # the restaurant will not be open when the user requested 
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Saturday.
At that time, our special will be Gyros with Onions.''')
        
# see what day of the week the user would like to make a reservation  
elif dayOfReservation == 'Saturday':

    # see if the restaurant will be open for lunch on saturday 
    if hourOfReservation >= 11 and hourOfReservation < 15:

        # set the special for lunch on saturday 
        special = 'Gyros with Onions.'

        # display the restaurant will be open and what the special will be 
        print('''All right! We'll be open for lunch then!
Our special will be''',special)

    # see if the restaurant will be open for dinner on saturday 
    elif hourOfReservation >= 17 and hourOfReservation < 23:

        # set the special for dinner on saturday 
        special = 'Spanakopita with Feta Cheese.'

        # display the restaurant will be open and what the special will be 
        print('''All right! We'll be open for dinner then!
Our special will be''',special)

    # the restaurant will not be open when the user requested 
    elif hourOfReservation < 11:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on Saturday.
At that time, our special will be Gyros with Onions.''')

    # the restaurant will not be open when the user requested 
    elif hourOfReservation >= 15 and hourOfReservation < 17:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 5 pm on Saturday.
At that time, our special will be Spanakopita with Feta Cheese.''')

    # the restaurant will not be open when the user requested 
    else:
        print('''Sorry! We won't be open then.
However, please join us when we next open at 9 am on Sunday.
At that time, our special will be Grape Leaves with Vegetables.''')
        
# see what day of the week the user would like to make a reservation 
elif dayOfReservation == 'Sunday':

    # set the special for sunday at brunch 
    special = 'Grape Leaves with Vegetables.'

    # see if the restaurant will be open when the user requested
    if hourOfReservation >= 9 and hourOfReservation < 14:
        print('''All right! We'll be open for brunch then!
Our special will be''',special)

    # the restaurant will not be open when the user requested 
    elif hourOfReservation < 9:
         print('''Sorry! We won't be open then.
However, please join us when we next open at 9 am on Sunday.
At that time, our special will be Grape Leaves with Vegetables.''')

    # the restaurant will not be open when the user requested 
    else:
         print('''Sorry! We won't be open then.
However, please join us when we next open at 11 am on monday.
At that time, our special will be Hummus with Pita Bread.''')

# display this is the end of the program and the version of the program
print("\nFinishing Minerva's Mediterranean Restaurant Reservation Program, \
version 1.0")
        
        
        
        
        
    



































            


















                         
