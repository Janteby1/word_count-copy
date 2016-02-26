# python spell checker
'''
given a huge list of words that are all spelled correctly, called your dict 
have another list of words you want to spell check
basically you want to go through the list of words you have to find it in your dictionary, if you can not find it then you print it out saying it is spelled wrong
'''

''''
* Write a program that takes a filename and a second parameter called `n`
* Return a list in descending order of the most common words in the file
* `n` is the number of the "most common words" in the file.
'''

'''
my_list = ["jeff", "is", "programmer"]

# iterate through your list of words and check the spelling, printing the ones that are not spelled right 
for word in my_list:
	if word not in words: # can just use the not to find which are not spelled right 
		print (word)
'''


def word_stats(filename, n):
	from operator import itemgetter
	words_dic = {} 
	final_list = []

	# read in the article file
	with open("article.txt") as lines:
		# loop through the article line by line
		for line in lines:
			# split each line in the articel into words and put them in a list (by line)
			words_per_line = line.split (" ")

			# loop through each line worth of words
			for word in words_per_line:
				# strip everything to words
				clean_word = ''
				for letter in word:
					if letter.isalpha():
						clean_word += letter
				# print (clean_word)

				# if the word is already in your dictionary
				if clean_word == "":
					pass
				elif clean_word in words_dic:
					# add a value of +1
					words_dic[clean_word] +=1
				# else the word is not already in your dict 
				else:
					# add the word and give it a value of 1
					words_dic[clean_word] = 1

		# sort the list so that the words with the most count are at the end 
		final_list = (sorted(words_dic.items(), key=itemgetter(1)))

		# print hte top words, statrting from the end of the sorted lsit you created
		for i in range (1,n+1):
			print (final_list[-i])
			i -= 1

print (word_stats ("article.txt",10))

# mystats = (word_stats ("article.txt",5))



'''
def word_stats(filename, n):
	from operator import itemgetter
	words_dic = {} 
	final_dic = []
	with open("article.txt") as lines:
		for line in lines:
			words_per_line = line.split (" ")
			for word in words_per_line:
				clean_word = ''
				for letter in word:
					if letter.isalpha():
						clean_word += letter
				if clean_word == "":
					pass
				elif clean_word in words_dic:
					words_dic[clean_word] +=1
				else:
					words_dic[clean_word] = 1
		final_dic = (sorted(words_dic.items(), key=itemgetter(1)))

		for i in range (1,n+1):
			print (final_dic[-i])
			i -= 1
print (word_stats ("article.txt",10))
'''



'''
using library to solve it in one line - 

import re
from collections import Counter

with open('your_file.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words) # basically all solved in this line

'''
  