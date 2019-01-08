"""
from modules import Minion, Player, AI
from time import sleep
import os

player1 = Player()
opponent = AI()

def turn():
	player1.show_hand_summ()
	sleep(1)
	player1.boardstate()
	sleep(2)

def play():
	print "      Welcome to the game"
	sleep(1)
	print "Try to reduce the opponents health to zero"
	print
	sleep(1)
	player1.create_hand()
	opponent.create_hand()
	player1.show_hand()
	sleep(2)
	while player1.is_alive() and opponent.is_alive():
		turn()
		sleep(5)
		
play()

"""

import player
import cards
from player import *
from cards import *
from time import sleep

	
def play():
	player1 = Player()
	opponent = AI()
	player1.create_hand()
	opponent.create_hand()
	print "         Welcome to the game."
	sleep(1)
	print "Try to reduce the opponents health to zero."
	sleep(1)
	print
	print "You both start with the 10 health and the following cards in hand"
	print
	sleep(1)
	for i in player1.cards_in_hand:
		print i
		print i.description
		print
		sleep(0.5)
	while player1.is_alive() and opponent.is_alive():
		player1.play_card()
		print
		sleep(2)
		opponent.play_card()
		print
		sleep(2)
		player1.minion_attack(opponent)
		print
		sleep(2)
		opponent.minion_attack(player1)
		print
		sleep(2)
		player1.boardstate()
		print
		sleep(1)
		opponent.boardstate()
		print
		sleep(1)
	if opponent.health <= 0:
		print "Congratulations!"
		print "   You Win!"
	else:
		print "Better luck next time!"
	
play()
print
raw_input("Press ENTER to exit")