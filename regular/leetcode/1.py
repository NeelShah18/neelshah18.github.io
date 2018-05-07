new_a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin", "zen", "gig", "msg"]
dic = {}
temp_list =[]
for letter,temp in zip(range(97,123),new_a):
    dic[chr(letter)] = temp

for word in words:
    new_word=""
    for charter in word:
        new_word = new_word+dic[charter]
    temp_list.append(new_word)
    new_word=""

print(temp_list)
print(set(temp_list))
