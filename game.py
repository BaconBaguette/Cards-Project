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

def setup():
	player1 = Player()
	opponent = AI()
	player1.create_hand()
	opponent.create_hand()
	
def play():
	player1 = Player()
	opponent = AI()
	player1.create_hand()
	opponent.create_hand()
	print "		Welcome to the game."
	print "Try to reduce the opponents health to zero."
	print "You start with the following cards in your hand"
	for i in player1.cards_in_hand:
		if getattr(i, "type") == "minion":
			print i
			print i.description
			print
	
play()