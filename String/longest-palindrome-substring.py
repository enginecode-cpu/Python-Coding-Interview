def expand(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1:right]

def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    answer = ''

    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        answer = max(
                    answer, 
                    expand(s, i, i+1),
                    expand(s, i, i+2),
                    key=len 
                )

    return answer

print(longestPalindrome('babad'))