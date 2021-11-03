sentence =  """finished files are the   
 result of years of scientific study   
 combined with the experience of years"""

words_freq ={} #dictionary for the counts
for word in sentence.split():
    if word not in words_freq:
        words_freq[word] =1
    else:
        words_freq[word] +=1

print (words_freq)
