class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l1 = []
        flag = True
        for number in range(left,right+1,1):
            for part in str(number):
                if int(part)!=0 and int(number)%int(part)==0:
                    pass
                else:
                    flag=False
            if flag==True:
                l1.append(number)
            else:
                flag=True
        return l1
