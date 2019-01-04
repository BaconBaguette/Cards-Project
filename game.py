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

