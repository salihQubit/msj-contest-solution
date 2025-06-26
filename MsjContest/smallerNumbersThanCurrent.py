class Solution(object):
    def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0]*len(nums)
        count = 0
        j = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                else:
                    continue
            counts[i] = count
            count = 0
        return str(counts)
    numbers = [3,4,7,43,78,2,4,3,6,7,7,7]
    print(smallerNumbersThanCurrent(numbers))
