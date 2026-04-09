class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            a=[0]*26
            for j in i:
                a[ord(j)-ord('a')]+=1
            d[tuple(a)].append(i)
        return list(d.values())    