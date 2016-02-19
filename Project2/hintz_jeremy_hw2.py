###
# Name and EID: 

# Jeremy Hintz
# jjh2595

#########
# Problem 1a:
from string import punctuation
import re

f = open('pg36.txt')
passage = f.read()
f.close()

punctuation_marks = set(punctuation)

# split into words
words = passage.split()

# remove punctuation and transform to lowercase 
for i in range(len(words)):
	words[i] = ''.join(c for c in words[i] if c not in punctuation_marks)
	words[i] = words[i].lower()

# count one-syllable words
one_syllable_word_count = 0
for word in words:
	if re.search(r"\b[^aeiouy\d]*[aeiouy]+[^aeiouy\d]*\b", word):
		one_syllable_word_count += 1

# print("COUNT: " + str(one_syllable_word_count))

# *** ANSWER: 38686

#########
# Problem 1b:

# "stole" is an example of a one-syllable word that our heuristic misses
# "pious" is an example of a two-syllable word that our heuristic says is one syllable

#########
# Problem 2:

# (a)

f = open('pg36.txt')
lines = f.readlines()
f.close()

for line in lines:
    if re.search(r"\s+\-?\d*\.?\d+\s+", line):
    	print(line)

print("\n--------------------\n")

# (b)

for line in lines:
    if re.search(r"\s+\-?\d*\.?\d+\s+", line):
    	words = line.split()
    	for word in words:
    		if re.search(r"\A\-?\d*\.?\d+$", word):
    			print(word)

print("\n--------------------\n")

# (c)

for line in lines:
    if re.search(r"forg[eo]t.*\b", line):
    	print(line)

print("\n--------------------\n")

# (d)

for line in lines:
    if re.search(r"\b.*[^aeiou][aeiou]{3}[^aeiou].*\b", line):
    	print(line)

#########
# You can do problems 3-5 on paper, if you like. 
# But please don't forget to put your name on the paper!
