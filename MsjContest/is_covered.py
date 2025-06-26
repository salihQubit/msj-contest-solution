class Solution(object):
    def isCovered(self, ranges, left, right):
        x=[]
        for a in ranges:
            for b in range(a[0],a[1]+1):
                x.append(b)
        for a in range(left,right+1):
            if a not in x:
                return False
        return True