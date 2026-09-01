from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Start only if this is the beginning of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

                # Count consecutive numbers
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)
        return longest
