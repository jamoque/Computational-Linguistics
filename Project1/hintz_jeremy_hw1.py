########
# Your name and EID:

# Jeremy Hintz - jjh2595

#########
# Problem 1:

# The following are invalid:

# (c) a variable name cannot contain an operator, such as -
# (e) def is a reserved word used to denote the start of a function
# (h) a variable may not contain whitespace
# Extra-credit: you should not use sum as a variable name because it would overload a function used to add up the elements of a list

#########
# Problem 2:

f = open('wells.txt', 'r')
passage = f.read()
f.close()
print(passage.count("of"))

# ANSWER: 6

#########
# Problem 3:

from string import punctuation

punctuation_marks = set(punctuation)
punctuation_marks.remove('-')
f = open('wells.txt', 'r')
passage = f.read()
f.close()
words = passage.split()
for i in range(len(words)):
	words[i] = ''.join(c for c in words[i] if c not in punctuation_marks)
print(words)

#########
# Problem 4:

present_participle_verb_count = 0
for word in words:
	if len(word) > 3 and word[-3:] == 'ing':
		present_participle_verb_count += 1

print(present_participle_verb_count)

# ANSWER: 10

#########
# Problem 5:

for i, word in enumerate(words):
	if len(word) > 3 and word[-3:] == 'ing':
		words[i] = word[:-3]
	elif len(word) > 1 and word[-1:] == 's':
		words[i] = word[:-1]
	elif len(word) > 2 and word[-2:] == 'ed':
		words[i] = word[:-2]

stemmed_passage = ' '.join(words)

print(stemmed_passage)

#########
# Problem 6:

START_STRING = '***START OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS***'
END_STRING = '***END OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS***'

f = open('pg768.txt')
bronte_string = f.read()
f.close()

start_index = bronte_string.index('***START')
end_index = bronte_string.index('***END')

trimmed_bronte = bronte_string[start_index+len(START_STRING):end_index]






