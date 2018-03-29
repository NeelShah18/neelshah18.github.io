"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def main():
    l = [0,3,4,-1,1]
    i =0
    n = len(l)

    while i<n:
        val = l[i]
        if((val<=0) or (val>=n)):
            pass
        else:
            c = l[i]
            nextval = l[l[i]]
            while c != nextval:
                l[c] = c
                c = nextval
                if((c<=0) or (c>=n)):
                    pass
                else:
                    nextval = l[nextval]
        i=i+1
        print(l)
    ans = n
    print(ans)
    j =0 
    while j<n:
        print(j)
        print(l[j],j)
        if l[j]!=j:
            ans = j
            print(ans)
            break
        j = j+1
    print(ans)
    return None

if __name__=="__main__":
    main()
