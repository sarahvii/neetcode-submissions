class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        pointer = 0
        
        for num in nums:
            if num == val:
                num = val
            else:
                k += 1
                nums[pointer] = num
                pointer += 1

        return k
        