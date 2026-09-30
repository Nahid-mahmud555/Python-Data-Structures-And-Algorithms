class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        blank = set()
        for num in nums:
            if num in blank:
                return True
            blank.add(num)
        return False
