class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_store = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in strs_store:
                strs_store[key] = []
            strs_store[key].append(i)
            
        return list(strs_store.values())
                
