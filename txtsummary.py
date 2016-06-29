#txtsummary

import re


#1. Read in a text file.

ui = raw_input("Enter the name of the text file. Ex: filename.txt\n")

file = open(ui)
filec = file.read()
# filed = filec.decode("utf-8")
#filec = filec.encode("utf-8")
#print filec


#2. Count how many times each word appears in the entire text. 

#lowercase everything and remove everything except letters and spaces for easy
#word counting 
filecl = filec.lower()
chars = ['!', ',', '.', '?', '"']
for char in chars:
	fileraw = filecl.replace(char, "")
	filecl = fileraw


#turn the sting txt file into a list of words separated by spaces
wordlist = fileraw.split()
#print wordlist

#dictionary to store count of each word. {'word' : count}
wordcount = {}


#for every word in the file
for word in wordlist:

	#if the word has already been counted for
	if word in wordcount.keys():
	
		#add one to the count for that word
		wordcount[word] += 1
		
	#if this is the first time the word appears in the file
	else:
		wordcount[word] = 1
			
#print wordcount



#3. Calculate the average points in each sentence in the article.

#list of sentences from file
sentences = re.split(r'[.?!\n]\n*',filec)

#will be list of sentences with out empty spaces
sent_clean = []

#removes items in the list of sentences that may be empty spaces
#to avoid key errors 
for i in range(0, len(sentences)):
	if sentences[i] == '' or sentences[i] == ' ':
		sentences[i] = sentences[i]
	else:
		sent_clean.append(sentences[i])
		
#print sent_clean


#create dictionaries that store the sums of each sentence and the average of
#each sentence 
sums = {sent_clean[0] : 0}
averages = {}


#loop through each sentence and find average			
for sent in sent_clean:

	#create the key in both dictionaries for the current sentence
	sums[sent] = 0
	averages[sent] = 0
	
	#remove commas and make all lower case for easy word matching 
	sentr = sent.replace(',', '')
	sentr = sentr.lower()
	
	#list of words in the current sentence
	sentrl = sentr.split(' ')
	
	#for every word in sent
	for word in sentrl:
		
		#removes space from sentence if sentence starts with blank space
		if sentrl[0] == '':
			del sentrl[0]
		else:
			sentrl[0] = sentrl[0]
		
	
 	 	if word in sentrl:
 			sums[sent] += wordcount[word]
 			#print "%s: %d" % (word, wordcount[word])
  			
  		else:
  			sums[sent] += 0
  						
  	averages[sent] = sums[sent] / float(len(sentr.split(' ')))
  	
#print averages 


# 4. Print the 5 sentences with the lowest point average.

#list of tuples sorted by point average, that holds each sentence and its
#point average 
av_items =sorted(averages.items(), key=lambda x: x[1])

matches = []

print '\nThe 5 sentences with the lowest point average, from the file'
print '\'kendricklamar_mommavs2.txt\' are listed below in ascending order:\n'

for i in range(0, len(av_items)):
	if i <= 4:
		print av_items[i][0]
		match = re.findall(av_items[i][0] + '[.|?|!]', filec)
		matches.append(match)
	else:
		break
		

print "\nWith punctuation: "
for i in range(0, len(matches)):
	print ' '.join(matches[i])	

		
print '\n'


		



	


			
			
			
			
			
