from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hashmap = defaultdict(int)
        for num in nums:
            count_hashmap[num]+=1
        # print(count_hashmap)
        result = sorted(count_hashmap,key=lambda x: count_hashmap[x],reverse=True)
        return result[:k]
