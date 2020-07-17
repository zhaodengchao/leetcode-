'''二分查找'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left_pointer = 0
        right_pointer = n-1
        while left_pointer<= right_pointer:
            mid_pointer=(left_pointer+right_pointer)//2
            if target > nums[mid_pointer]:
                left_pointer=mid_pointer+1
            elif target < nums[mid_pointer]:
                right_pointer = mid_pointer-1
            else:
                return mid_pointer
        return -1

