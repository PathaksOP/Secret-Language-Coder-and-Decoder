import random

# Encoding:

phrase = input('Enter a phrase: ').strip().lower() 
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
list_input = []
list_output = []
index_space = phrase.find(' ') 
index_start = 0
# converting the phrase into list_input
while True:
    if index_space != -1 and index_space != index_start:
        list_input.append(phrase[index_start : index_space])
        index_start = index_space + 1 
        index_space = phrase.find(' ',index_start) 
    
    elif index_space == index_start:
        index_start += 1
        index_space = phrase.find(' ',index_start)

    elif index_space == -1:
        if index_start == len(phrase) - 1:
            list_input.append(phrase[index_start])
        else:
            list_input.append(phrase[index_start :])
        
        break

print(list_input)

def coder(list_input , list_output):
    for i in list_input:
        if len(i) <= 3:
            
            i = ' ' + i
            word = i[len(i) : 0 : -1]
            list_output.append(word)
        else:
            random_alpha = random.choices(alphabets , k = 6)
            
            random_chars = ''
            for x in random_alpha:
                random_chars = random_chars + x
            
            i = random_chars[:3] + i[3 : len(i)] + i[0:3] + random_chars[3:]

            list_output.append(i)


    phrase_new = ''
    for a in list_output:
        phrase_new = phrase_new + a + ' '

    return phrase_new.strip(' ')


output = coder(list_input , list_output)
print(output)
