#Code to determine how many words in sentence start and end with the same letter.


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
x = sentence.split() #Split every words from sentences

same_letter_count= 0
for n in x:
    if n[0]==n[-1]:  #Condition if the first letter and the last letter are the same
        same_letter_count+=1  #Number will be updated
        
print(same_letter_count)
