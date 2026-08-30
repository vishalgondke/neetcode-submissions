from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result=[]

        for s in strs:
            # print("sorted: ",sorted(s))
            sorted_s=tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        # print("anagram_map: ",anagram_map.values)
        for value in anagram_map.values():
            result.append(value)
        return result
