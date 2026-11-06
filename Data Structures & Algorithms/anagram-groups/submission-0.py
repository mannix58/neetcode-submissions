from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            tmp = ''.join(sorted(s))
            result[tmp].append(s)
        return list(result.values())
        # result = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     counts = Counter(s).elements()
        #     print(counts)
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
            
        #     result[tuple(counts)].append(s)
        # return list(result.values())