#importing iterator module for premuttion of the string
from itertools import permutations

#assigining the values to the list
l1=['Q','W','E','R','T','Y','U','I','O','P']
l2=['A','S','D','F','G','H','J','K','L']
l3=['Z','X','C','V','B','N','M']
l=[]

#creating a file to store all the 3 letter words generated by the lists 
f=open('words.txt','w+')

for i in range(0,10):                                      # loop for list l1
	s=l1[i]                                            # storing the i(th) letter of list l1 in s. ex s=Q
	for j in range(0,9):                               # loop for  list l2
		s=s+l2[j]                                  # adding the j(th) letter of list l2 in s. ex s=QA
		for k in range(0,7):                       # loop for list l3
			s=s+l3[k]                          # adding the k(th) lettet of list l3 in s. ex s=QAZ
		        #print(s)                            here s containg 3 letter word formed by all the 3 list

# this loop generates all the combination of words which can be formed by s. ex s='QAZ' then all permutation of this string will be 'QAZ', 'QZA', 'AQZ', 'AZQ', 'ZAQ', 'ZQA'
			for p in permutations(s):          
				y=''.join(p)               # join basically join all the letters from the combination to form word
				f.write(y+"\n")            # it writes the word in text file followed by new line

# replacing the last letter with a blank character in 's' so as to create a new word with new k(th) value in l3. ex 'QAZ' replaced by blank to form  'QA' and then new k(th) value from l3 will join s  'QAX'
			s=s.replace(l3[k],"")

# replacing the last letter with a blank character in 's' so as to create a new word with new j(th) value in l2. ex 'QA' replaced by blank to form  'Q' and then new j(th) value from l2 will join s  'QS'
		s=s.replace(l2[j],"")

# replacing the last letter with a blank character in 's' so as to create a new word with new i(th) value in l1. ex 'Q' replaced by blank to form  '' and then new i(th) value from l1 will join s  'W'
	s=s.replace(l1[i],"")

f.close()                                                  # after writing all the values to the file it will close the file
list1 = set(open("words.txt").read().split())              # opening and reading the file in which all the word generated by lists is stored and then creating set of this file

#Converting the words in dictionary in upper case
A=open('/usr/share/dict/american-english')

#creating a demo file for storing upper case words of dictionary
B=open('dict_upper.txt','w+')

l4=[x for x in A.read().split('\n')]                        # Reading the dictionary and storing the values in list l4
#print(len(l))
for i in l4:
	B.write(str(i).upper()+'\n')                       # storing words in demo.txt file

list2 = set(open("dict_upper.txt").read().split()) # opening the dictionary and reading it and then creating set for this file

common  = list1.intersection(list2)                        # this function basically return the values which will be common in both the files

print(common)                                              # printing the common values among them

f.close()
A.close()
B.close()
