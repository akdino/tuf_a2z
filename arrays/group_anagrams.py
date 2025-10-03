from collections import defaultdict
def groupAnagrams(self, strs):
    hm=defaultdict(list)
    for i in strs:
        word="".join(sorted(i))
        hm[word].append(i)
    return list(hm.values())