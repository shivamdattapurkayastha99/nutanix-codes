# top k frequent elements
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(collections.Counter(nums))
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse = 1)}
        
        final_list = []
        
        for i, key in enumerate(freq.keys()):
            if i == k:
              break
            final_list.append(key)
          
        return final_list