class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            store[i] = store.get(i, 0) + 1
        
        sorted_store = sorted(store, key=lambda x: store[x], reverse=True)
        return sorted_store[:k]