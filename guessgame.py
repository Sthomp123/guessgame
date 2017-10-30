#!/usr/bin/env python3
# guessgame.py
# Steven Thompson
# 10/30/17
# Number guessing game

from random import randint
MIN = 1
MAX = 20
targetnumber = randint(MIN, MAX)

prompt = "Please guess a number from " + str(MIN) + " to " + str(MAX) + ": "
guess = int(input(prompt))
print(guess)