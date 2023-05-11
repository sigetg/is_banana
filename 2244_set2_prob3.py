#Author: George Sigety

import random
import string
import numpy

def is_bananna(six_word):
    six_word_list = list(six_word)
    letter_counts = []
    unique_letters = []
    unique_letters, letter_counts = numpy.unique(six_word_list, return_counts = True)
    if (3 in letter_counts) and (2 in letter_counts) and (1 in letter_counts):
        return True
    else:
        return False
        
# set a variable to the alphabet:
alphabet = list(string.ascii_lowercase)
#set the arrays to hold the 10^6 sequences of 6 letter words
six_word = ['','','','','','']
words = [None] * 10**6
i = 0
no_bananna = 0
#fill the array with 10^6 sequences of 6 random letters
while i < 10**6:
    x = 0
    while x < 6:
        six_word[x] = random.choice(alphabet)
        x += 1
    #count the number of words that are bananna words
    if (is_bananna(six_word)):
        no_bananna += 1
    six_word = ['','','','','','']
    i += 1

# solve for the probability using |E|/|S|
probability_bananna = no_bananna / 10**6

#print the probability
print(probability_bananna)