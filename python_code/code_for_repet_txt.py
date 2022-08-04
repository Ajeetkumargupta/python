#import re
#file=open('repet_word.txt','r')
#list=re.findall(r'(\b\w+\b)\W+\1',file.read(),re.MULTILINE)
#print(list)

import re
import string
frequency = {}
document_text = open('repet_word.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z,A-Z]{1,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])
