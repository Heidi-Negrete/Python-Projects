import random
import time

def displayIntro():
    print('You are in dark cave,')
    print('And in front of you the path has split two ways.', end="\n")

def choosePath():
    path = ''
    while path != '1' and path != '2':
        path = input('Which path will you take? (1 or 2) ')

    return path

def checkPath(chosenPath):
    print('You begin walking quickly down the path you have chosen...')
    time.sleep(2)
    print('It is dark and you hear only your own footsteps and pounding of your heart')
    time.sleep(2)
    print('A huge figure appears in front of you!...')
    print()
    time.sleep(2)

    friendlyPath = random.randint(1,2)

    if chosenPath == str(friendlyPath):
        print('Hey, it\'s me, Santa Claus. I\'ve been trying to give you this gift for days.')
        print('Santa hands you a teleportation device that will take you home in a second.')
        print('Phew. You\'re saved.')
    else:
        print('It\'s a vicious minotaur with glowering red eyes and huge horns')
        print('You see black as with one blow he crushes your head.')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    checkPath(choosePath())

    playAgain = input('Do you want to play again? (yes or no) ')
