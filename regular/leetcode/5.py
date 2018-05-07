S = "I speak Goat Latin"

new_s = S.split(" ")
i=0
for word in new_s:
    i+= 1
    #print(word[0])
    if word[0].lower() in ['a','e','i','o','u']:
        print(word)
