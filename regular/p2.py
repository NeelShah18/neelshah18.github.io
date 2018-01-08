"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
"""
By Neel Shah
website: https://github.com/NeelShah18
email: neelknightme@gmail.com
"""
class p2:
    def __init__(self):
        self.array = []
        return None
    
    def soltuion(self,array):
        self.array = array
        n = len(self.array)
        left = []
        right = [None]*n
        ans = []
        left.insert(0,int(1))
        j = 1
        for i in self.array:
            #print(str(left[j-1])+"--"+str(i))
            temp = int(left[j-1])*int(i)
            #print(temp)
            left.insert(j,int(temp))
            j= j+1
        #print(left) 
        right[n-1] = 1
        k = n-2
        while k>= 0:
            temp = int(right[k+1])*int(self.array[k+1])
            #print(temp,k)
            right[k]=int(temp)
            k=k-1
        #print(right)
        for (i,j) in zip(left,right):
            ans.append(int(i*j))
        print(ans)
        return None

def main():
    n = [1,2,3,4,5]
    s = p2()
    s.soltuion(n)
    return None

if __name__=="__main__":
    main() 