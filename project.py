# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16V9IkPHWp8Z2UiLI2UNjwRTHchtixpy2
"""

import random

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

print( " ")


print ("Start guessing...\n")

#here we set the secret
l = ("atrocious","danger","horse","secret")
word=l[random.randrange(0,5,1)]
#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print ("\b "+char)    

        else:
    
        # if not found, print a dash
            print ("\b _"),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break              

    

    # ask the user go guess a character
    guess = input("guess a character:") 
    print("\n")
    
    if len(guess) > 1.0:
      print("Enter only one character")
    else:
    
    # set the players guess to guesses
      guesses += guess                    

    # if the guess is not found in the secret word
      if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
          turns -= 1        
 
    # print wrong
          print ("Wrong")    
 
    # how many turns are left
          print ("You have", + turns, 'more guesses\n') 
 
    # if the turns are equal to zero
          if turns == 0:           
    
        # print "You Loose"
              print ("You Loose")