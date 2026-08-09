class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sortedS = ''.join(sorted(word))
            if sortedS not in groups:
                groups[sortedS] = []
            groups[sortedS].append(word)
        return list(groups.values())