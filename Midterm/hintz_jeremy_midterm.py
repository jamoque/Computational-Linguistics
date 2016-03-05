# Midterm exam answers
#
# Name: Jeremy Hintz
# EID: jjh2595

# NOTE: TO VIEW OUTPUT FOR THE FOLLOWING PROBLEMS, SIMPLY SET THESE FLAGS TO TRUE OR FALSE
PRINT_OUTPUT = {'1': False, '2': False, '3a': False, '3b': False, '4': False, '5a': False, '5b': False, '5c': False}

#########
# Problem 1:

def summed_wordlength(words):
	"""returns the sum of the lengths of the strings"""
	return len(''.join(words))

if PRINT_OUTPUT['1']:
	print("1)")
	print(summed_wordlength(['hello', 'world!']))
	print(summed_wordlength(['friends', 'romans', 'and', 'countrymen']))
	print("-------------------------------------")

#########
# Problem 2:

import re

f = open('pg1184.txt')
lines = f.readlines()
f.close()

found = []

for line in lines:
    if re.search(r"\b((S|s)tand(s|ing)?|(S|s)tood)\b", line):
    	found.append(line)

if PRINT_OUTPUT['2']:
	print("2)")
	for line in found: print(line)
	print("-------------------------------------")

#########
# Problem 3a:

import nltk
from nltk.corpus import brown

brown_tagged_words = brown.tagged_words(categories = "news")

def simplify_tags(tagged_words):
	"""returns simplified tags for a list of pairs of words and their part of speech tags"""
	simple_tags = []

	for pair in tagged_words:
		tag = pair[1]
		simple_tag = tag[:2]
		simple_tags.append(str(simple_tag))

	return simple_tags

new_tags = simplify_tags(brown_tagged_words)

if PRINT_OUTPUT['3a']:
	print("3) a)")
	print(new_tags)
	print("-------------------------------------")

#########
# Problem 3b:

from string import punctuation

f = open('pg1184.txt')
passage = f.read()
f.close()

def find_prefixes(prefix, passage):
	"""returns words prefixed by a parameter prefix minus the prefix itself"""
	passage = passage.lower()
	punctuation_marks = set(punctuation)
	words = passage.split()

	# remove punctuation
	for i in range(len(words)):
		words[i] = ''.join(c for c in words[i] if c not in punctuation_marks)

	# collect words beginning with prefix, minus the prefix itself
	prefix_less_words = []
	for word in words:
		if len(word) > len(prefix) and word[:2] == prefix:
			prefix_less_words.append(word[2:])

	return prefix_less_words

prefix_less_words = find_prefixes('in', passage)

if PRINT_OUTPUT['3b']:
	print("3) b)")
	print(prefix_less_words)
	print("-------------------------------------")

# Two words where "in" is a prefix:
# 1. inflexible
# 2. inanimate

# Two words where "in" is not a prefix:
# 1. ink
# 2. innocence

#########
# Problem 4:

def find_verb_preposition_pairs(tagged_words, first, second):
	""" 
	takes a corpus of tagged words, and two tags: first and second

	returns a dictionary where the keys are verbs and the values
	are lists of prepositions
	"""
	verbs = {}

	for i, pair in enumerate(tagged_words):
		word, tag = pair
		if tag[:len(first)] == first:
			next_word, next_tag = tagged_words[i+1]
			if next_tag[:len(second)] == second:
				if word in verbs:
					verbs[word].append(next_word)
					verbs[word] = list(set(verbs[word]))
				else:
					verbs[word] = []
					verbs[word].append(next_word)

	return verbs

verbs = find_verb_preposition_pairs(brown_tagged_words, 'V', 'IN')

if PRINT_OUTPUT['4']:
	print("4)")
	ordered_list = sorted(verbs, key=lambda k: len(verbs[k]), reverse=True)
	for word in ordered_list:
		print(word + " : " + str(verbs[word]))
	print("-------------------------------------")

# RESULTS:
# There are two verbs that have eleven different prepositions after them
# made : ['about', 'for', 'on', 'with', 'of', 'in', 'by', 'before', 'at', 'to', 'after']
# came : ['during', 'into', 'on', 'in', 'off', 'by', 'at', 'to', 'from', 'under', 'after']

#########
# Problem 5a:

from collections import defaultdict

f = open('pg345.txt')
passage = f.read()
f.close()

passage = passage.lower()
punctuation_marks = set(punctuation)
words = passage.split()
for i in range(len(words)):
	words[i] = ''.join(c for c in words[i] if c not in punctuation_marks)

word_frequencies = defaultdict(int)

for word in words:
	word_frequencies[word] += 1

if PRINT_OUTPUT['5a']:
	print("5) a)")
	print('-- WORDS: --')
	ordered_list = sorted(word_frequencies, key=lambda k: word_frequencies[k], reverse=True)
	for word in ordered_list[:10]:
		print(word + " : " + str(word_frequencies[word]))

# Top ten words and their frequencies:
# 1. the : 8036
# 2. and : 5896
# 3. i : 4712
# 4. to : 4540
# 5. of : 3738
# 6. a : 2961
# 7. in : 2558
# 8. he : 2543
# 9. that : 2455
# 10. it : 2141

bigrams = nltk.bigrams(words)

bigram_frequencies = defaultdict(int)

for bigram in bigrams:
	bigram_frequencies[bigram] += 1

if PRINT_OUTPUT['5a']:
	print('-- BIGRAMS: --')
	ordered_list = sorted(bigram_frequencies, key=lambda k: bigram_frequencies[k], reverse=True)
	for bigram in ordered_list[:10]:
		print(str(bigram) + " : " + str(bigram_frequencies[bigram]))
	print("-------------------------------------")


# 1. ('of', 'the') : 896
# 2. ('in', 'the') : 629
# 3. ('', '') : 526
# 4. ('to', 'the') : 383
# 5. ('and', 'the') : 340
# 6. ('and', 'i') : 329
# 7. ('on', 'the') : 324
# 8. ('it', 'was') : 311
# 9. ('it', 'is') : 303
# 10. ('van', 'helsing') : 299

#########
# Problem 5b:

def calculate_sentence_probability(sentence, word_frequencies, bigram_frequencies, passage_length):
	sentence_words = sentence.split()
	probability = 1.0
	probability *= float(word_frequencies[sentence_words[0]]) / float(passage_length)
	for i in range(1,len(sentence_words)):
		w1 = sentence_words[i-1]
		w2 = sentence_words[i]
		probability *= bigram_frequencies[(w1, w2)] / float(word_frequencies[w1])

	return probability


if PRINT_OUTPUT['5b']:
	print("5) b)")
	s = "there is a vampire in the room"
	print('PROBABILITY: ' + str(calculate_sentence_probability(s, word_frequencies, bigram_frequencies, len(words))))
	print("-------------------------------------")

#########
# Problem 5c:

def calculate_sentence_probability_v2(sentence, words, word_frequencies, bigrams, passage_length):
	sentence_words = sentence.split()
	bigram_frequencies = nltk.ConditionalFreqDist(nltk.bigrams(words))
	bigram_probabilities = nltk.ConditionalProbDist(bigram_frequencies, nltk.MLEProbDist)
	probability = 1.0
	probability *= float(word_frequencies[sentence_words[0]]) / float(passage_length)
	for i in range(1,len(sentence_words)):
		w1 = sentence_words[i-1]
		w2 = sentence_words[i]
		probability *= bigram_probabilities[w1].prob(w2)

	return probability



if PRINT_OUTPUT['5c']:
	print("5) c)")
	s = "there is a vampire in the room"
	print('PROBABILITY: ' + str(calculate_sentence_probability_v2(s, words, word_frequencies, bigrams, len(words))))
	print("-------------------------------------")
