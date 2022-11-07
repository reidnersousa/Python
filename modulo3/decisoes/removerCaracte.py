# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word ="Gregory"
for letter in user_word:
   # print(letter)
    #print(user_word)
    user_word = user_word.upper()
    i=0
    # Complete the body of the for loop.
    while i < len(user_word):
        
        #print(user_word)
        #print(letter)
        if user_word[i] =="A" or  user_word[i]=="E" or user_word[i]=="O" or user_word[i]=="I" or user_word[i]=="U":
            
            user_word = user_word.replace(user_word[i],"")
            continue
            
        i +=1
    
    
print(user_word)
for letter in user_word:
    print(letter)