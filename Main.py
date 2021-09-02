'''
Created on Sep 1, 2021

@author: ancas
'''

import time
import os
import subprocess

if __name__ == '__main__':
    pass

subprocess.call('', shell=True)
cmd = 'mode 80,20'
os.system(cmd)

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
      
      
gems = 0
starstot = 0
def printgems(final=0):
    print("\033[1;32;40m")
    screen_clear()
    if final == 1:
        print("\n\n\n\n\n\n\n")
    print("="*80)
    gems_print = "\033[0;0m Primogems: " + str(gems) + " " + "\033[1;32;40m"
    print(gems_print.center(96, "="))
    print("="*80)
    print("\033[0;0m")
    print("\n")
    
def printstars():
    screen_clear()
    print("="*80)
    gems_print = " Primogems: " + str(gems) + "        " + "Stars: " + str(starstot) + " "
    print(gems_print.center(80, "="))
    print("="*80)
    print("\n")

def doThis(n):
    global starstot
    global stars
    global gems
    
    for _ in  range(n):
        stars = input("How many stars are you able to earn from Floor " + str(int(9+_)) + "? (3/6/9)\n\n>> ")
        starstot += int(stars)
        gems += ((int(stars)/3)*100)
        printstars()
        if _ == n:
            pass

def doLogin(): 
    global gems
    gems += 60
    gems += 600                     #Patch Compensation 2.2
    gems += 300                     #Live Codes
def doAnniversary(): 
    global gems
    gems += 1600
    gems += 600                     #Patch Compensation 2.2
    gems += 300                     #Live Codes
def doEvents(): 
    global gems
    gems += 2760                    #All the In-Game Events
def doAllEvents():
    global gems
    gems += 5060

try:
    printgems()
    days = int(input("How long would you like to save Primogems? (Days)\n\n>> "))
    gems += (days*60)
    printgems()
    y = input("Do you have a Blessing of the Welkin Moon? (Y/N)\n\n>> ")
    if y.capitalize() == "Y":
        gems += (days*90)
    printgems()
    bp = input("Have you purchased a Battlepass for the current patch? (Y/N)\n\n>> ")
    if bp.capitalize() == "Y":
        if days >= 30:
            gems += 680
            gems += 640
        else:
            gems += (days/4)*160
    printgems()
    z = input("Select the Spiral Abyss Floor you are able to clear:\n(a) Floor 9\n(b) Floor 10\n(c) Floor 11\n(d) Floor 12\n(n) for none\n\n>> ").capitalize()
    printgems()
    
    if z == "A" or z == "(A)" or z == "(a)":
        doThis(1)
    elif z == "B" or z == "(B)" or z == "(b)":
        doThis(2)
    elif z == "C" or z == "(C)" or z == "(c)":
        doThis(3)
    elif z == "D" or z == "(D)" or z == "(d)":
        doThis(4)
    elif z == "N" or z == "(N)" or z == "(n)":
        pass
    else:
        raise ValueError()
    printgems()
    events = input("Do you attend events? (Y/N)\n\n>> ")
    printgems()
    if events.capitalize() == "Y":
        print("Which one?")
        print("(a) Mihoyo Web Login\n(b) Anniversary In-Game Login \n(c) In-Game Events\n(d) All Events\n(e) Choose Events Participation (One by One)\n\n")
        event = input(">> ").capitalize()
        if event == "A" or event == "(a)" or event == "(A)":
            doLogin()
        elif event == "B" or event == "(b)" or event == "(B)":
            doAnniversary()
        elif event == "C" or event == "(c)" or event == "(C)":
            doEvents()
        elif event == "D" or event == "(d)" or event == "(D)":
            doAllEvents()
        elif event == "E" or event == "(e)" or event == "(E)":
            screen_clear()
            a1 = input("\nWill you attend Daily Login Event? (Y\\N) \n\n>> ").capitalize()
            if a1 == "Y":
                gems += 60
            a2 = input("\nWill you attend Anniversary In-Game Login? (Y\\N) \n\n>> ").capitalize()
            if a2 == "Y":
                gems += 1600
            a3 = input("\nWill you attend Hyakunin Ikki? (Y\\N) \n\n>> ").capitalize()
            if a3 == "Y":
                gems += 420
            a4 = input("\nWill you attend Lunar Realm? (Y\\N) \n\n>> ").capitalize()
            if a4 == "Y":
                gems += 420
            screen_clear()
            a5 = input("\nWill you attend Spectral Secrets? (Y\\N) \n\n>> ").capitalize()
            if a5 == "Y":
                gems += 420
            a6 = input("\nWill you attend Moonchase? (Y\\N) \n\n>> ").capitalize()
            if a6 == "Y":
                gems += 600
            a7 = input("\nWill you use Live Codes? (Y\\N) \n\n>> ").capitalize()
            if a7 == "Y":
                gems += 300
            a8 = input("\nWill you use 2.2 Patch Compensation? (Y\\N) \n\n>> ").capitalize()
            if a8 == "Y":
                gems += 600
            gems += 600 #Patch Compensation 2.1
        printgems()    
        yn = input("Have you already used 2.1 Patch Compensation?\n>> ").capitalize()
        if yn == "Y":
            gems -= 600
        printgems()
except ValueError:
    input("Oops! That is not a valid input. \n\nTry again...")
    screen_clear()
    os.system("python " + "Main.py")
screen_clear()
print("Calculating final value.")
time.sleep(0.2)
screen_clear()
print("Calculating final value..")
time.sleep(0.2)
screen_clear()
print("Calculating final value...")
time.sleep(0.2)
screen_clear()
print("Calculating final value...")
time.sleep(0.2)
screen_clear()
print("Calculating final value....")
time.sleep(0.2)
screen_clear()
print("Calculating final value.....")
time.sleep(0.2)
screen_clear()
printgems(1)
input("\n\n\n\nContinue...")
screen_clear()
os.system('python "Main.py"')