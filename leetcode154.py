'''寻找旋转排序数组中的最小值 II'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            if nums[left]<nums[right]:
                right -= 1
            elif nums[left]>nums[right]:
                left += 1
            else:
                right -= 1
        return nums[left]
