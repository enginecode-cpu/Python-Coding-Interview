from typing import Deque

# pop()을 이용한 방법
def isPalidrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# deque를 이용한 방법
from collections import deque

def isPalindrome2(s: str) -> bool:
    strs: Deque = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 정규식 표현을 이용한 방법
import re

def isPalidrome3(s: str) -> bool:
    s = s.lower()
    # 정규식 표현을 이용한 문자 필터링
    # 문자나 숫자가 아닌 것은 ''으로 변경하는 것
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]