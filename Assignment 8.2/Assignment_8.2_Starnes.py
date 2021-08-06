# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Ryan Starnes
# Creation Date: 7/28/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#Removed indent from second through fourth line of print for proper output
	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	#Used spaces instead of tab
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	#Changed 'caves' to 'cave' to return correct value
	return cave

#Changed instances of 'chosenCave' to 'caveNumber' to be consitent 
#with the passed variable name 
def checkCave(caveNumber):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if caveNumber == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#Fixed missing parentheses around print output
		print('Gobbles you down in one bite!')


playAgain = 'yes'
#Used single '=' instead of '==' for checking equality
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#Changed from 'choosecave()' to 'chooseCave()'
	caveNumber = chooseCave()
	checkCave(caveNumber)
#Removed unecessary spaces
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#Add additional check in case no valid options are selected
	while playAgain != 'yes' and playAgain != 'y' and playAgain != 'no' and playAgain != 'n':
		print('Invalid selection, please try again')
		playAgain = input()
	#Changed " to ' for consistency
	#Added another check for 'n' to match 'yes' and 'y'
	if playAgain == 'no' or playAgain == 'n':
		#Fixed typo - 'planing' instead of 'playing'
		#Changed " to ' for consistency
		print('Thanks for playing')