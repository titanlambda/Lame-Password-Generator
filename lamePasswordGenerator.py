#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importing "random" for random operations 
import random 

numberOfPasswordToBeGenerated = 50
words = ["wordA", "wordB", "wordC", "wordD", "wordE", "wordF", "wordG", "wordH", "wordI", "wordJ"]
special_characters = ['#', '$', '@', '*', '%']
startingNumber = 100
endingNumber = 999	

for x in range(0, numberOfPasswordToBeGenerated):
	wordIndex = random.randrange(0, len(words), 1)	
	charIndex = random.randrange(0, len(special_characters), 1)
	randomNumber = random.randrange(100, 999, 1)
	password = words[wordIndex] + special_characters[charIndex] + str(randomNumber)

#	print ("A random word from the list is : ",end="") 
#	print(words[wordIndex])
#
#	print ("A random char from the list is : ",end="") 
#	print(special_characters[charIndex])
#
#	print ("A random number from range is : ",end="") 
#	print (randomNumber) 
#	
#	print ("password is : ",end="") 
	print (password) 
