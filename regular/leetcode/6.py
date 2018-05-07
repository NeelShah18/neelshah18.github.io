import re


def check_pl():
    s1= "I am :IronnorI Ma, i"
    s2="Ab?/Ba"

    new_s = re.sub('[^0-9a-zA-Z]+','',s1.lower())
    print(new_s)
    for i in range(0,int(len(new_s)/2)):
        if new_s[i] != new_s[len(new_s)-i-1]:
            print('No')
            return False
        else:
            print('Done')
            return True

check_pl()
