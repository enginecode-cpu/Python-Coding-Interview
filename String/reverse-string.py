from typing import  List

# 투포인터를 이용한 방법
def reverseString(s: List[str]) -> None:
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# reverse()를 이용한 방법
def reverseString2(s: List[str]) -> None:
    s.reverse()

strings = [s for s in 'helloworld']
reverseString(strings)
print(strings)