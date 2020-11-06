from collections import Counter, defaultdict
from typing import List
import re

# 나의 풀이
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    countWord = Counter(words)
    answer = sorted(list(countWord.items()), key=lambda x: x[1], reverse=True)

    return answer[0][0]

# defaultdict를 이용한 풀이
def mostCommonWord2(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)

# Counter를 이용한 풀이
def mostCommonWord3(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    countWord = Counter(words)

    # most_common(1) : 가장 많이 등장한 단어의 첫번째 값을 추출한다.
    return countWord.most_common(1)[0][0]