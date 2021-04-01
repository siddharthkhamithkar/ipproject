#!/usr/local/bin/python
# coding: latin-1
#run the code before opening project_info.pdf
#I suggest running the code through the terminal/CMD rather than any IDE
#webbbrowser, random and mysql.connector libraries are required in order to run this code
import random as rd
import webbrowser
import time
import mysql.connector

score = mysql.connector.connect(user='', password='')
mycursor = score.cursor()
mycursor.execute('create database Score;')
mycursor.execute('create table Score (Name varchar(20), Attempts int);')
mycursor.execute('use Score;')

ran = rd.randint(0,101) #generates random number. Replace rd.randint(0,101) with any intiger to make the evaluation simpler, or if you've got time to kill, play along
choice = 'wrong'
print('--------------------------------------------------------------------')
attempt = 1
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
        attempt = attempt + 1
    elif val > ran:
        print
        print('This is larger than the number I was thinking of. Please try again.')
        print
        print('--------------------------------------------------------------------')#ditto
        attempt = attempt + 1
    else:
        print('Congratulations on getting the number right!')#prints when answer is right
        choice = 'correct'
time.sleep(1)
print('Thank you for playing this!')
time.sleep(1)
print('You took ', attempt, ' attempts!')
time.sleep(1)
name = raw_input('Oh yeah, I forgot to ask you for your name. What is it? ')
sql = "INSERT INTO Score (Name, No. of attempts) VALUES (%s, %s)"
val = (name, attempt)
time.sleep(1)
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
print('Executing...')
time.sleep(1)
print('10% done.')
time.sleep(1)
print('42% done.')
time.sleep(1)
print('76% done.')
time.sleep(3)
print('error: spilled drink on self.') #actually happens in real life with me'
time.sleep(1)
print('Damn it, screw this. I\'m not thirsty anymore.')
time.sleep(3)
print('Okay, now let\'s try again.')
time.sleep(2)
time.sleep(2)
print('Now bye, hope this was good!')
webbrowser.open_new('project_info.pdf') #this is technically not a part of the project, but I did it to automate it

#project by:
#Siddharth and Janhavi, 12D
#Thank you!
