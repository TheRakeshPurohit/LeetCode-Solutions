# Time:  O(n)
# Space: O(1)

# two pointers, sliding window
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [-1]*(len(nums)-k+1)
        left = 0
        for right in xrange(len(nums)):
            if nums[right]-nums[left] != right-left:
                left = right
            if right-left+1 == k:
                result[left] = nums[right]
                left += 1
        return result