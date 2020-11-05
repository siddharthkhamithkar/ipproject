#!/usr/local/bin/python
# coding: latin-1
#run the code before opening project_info.pdf
#I suggest running the code through the terminal/CMD rather than any IDE
#webbbrowser and random libraries are required in order to run this code
import random as rd
import webbrowser
import time
ran = rd.randint(0,101) #generates random number. Replace rd.randint(0,101) with any intiger to make the evaluation simpler, or if you've got time to kill, play along
choice = 'wrong'
print('--------------------------------------------------------------------')
while choice == 'wrong': #creates a while loop as the main part of the code, which ends when you guess the right number
    response = int(input('Please input a number between 0 and 100: ')) #takes input from the user
    print('--------------------------------------------------------------------')
    try:
        val = response
    except ValueError:
        print
        print('This is not the number I was thinking about! Try again.')
        print
        print('--------------------------------------------------------------------')
        continue
    if val < ran:
        print
        print('This is lower than the number I was thinking of. Please try again.')
        print
        print('--------------------------------------------------------------------') #prints this line when the value entered is wrong
    elif val > ran:
        print
        print('This is larger than the number I was thinking of. Please try again.')
        print
        print('--------------------------------------------------------------------')#ditto
    else:
        print('Congratulations on getting the number right!')#prints when answer is right
        choice = 'correct'
print('Thank you for playing this!')
print('I will now open the documentation for this project!')
print('--------------------------------------------------------------------')
#the following is just me making the code longer
time.sleep(2)
print('In some time...')
time.sleep(2)
print('Why isn\'t it happening?')
time.sleep(2)
print('Wait, I need to grab a drink. I\'m tired.')
time.sleep(1)
print('executing grabbing_drink.exe')
time.sleep(2)
print('Loading…\n█▒▒▒▒▒▒▒▒▒')
time.sleep(1)
print('10%\n███▒▒▒▒▒▒▒')
time.sleep(1)
print('80%\n███████▒▒▒')
time.sleep(3)
print('error: spilled drink on self.') #actually happens in real life with me
print('Damn it, screw this. I\'m not thirsty anymore.')
time.sleep(3)
print('Okay, now let\'s try again.')
time.sleep(2)
webbrowser.open_new(r'project_info.pdf') #this is technically not a part of the project, but I did it to automate it
time.sleep(2)
print('Now bye, hope this was good!')
#project by:
#Siddharth, Adhishri and Janhavi, 12D
#Thank you!
