from typing import List, DefaultDict
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams: DefaultDict = defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))