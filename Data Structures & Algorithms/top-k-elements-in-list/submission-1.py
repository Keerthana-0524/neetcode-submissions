class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
        sorted_elements=sorted(freq_map.items(),key=lambda item:item[1],reverse=True)
        return [sorted_elements[i][0] for i in range(k)]