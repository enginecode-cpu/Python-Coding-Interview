from typing import List

# 브루트 포스
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] 

# in을 이용한 탐색
def twoSum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# 키 조회하는 방법
def twoSum3(nums: List[int], target: int) -> List[int]:
    numsMap = {}

    for i, num in enumerate(nums):
        numsMap[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in numsMap and i != numsMap[target - num]:
            return [i, numsMap[target - num]]

def twoSum4(nums: List[int], target: int) -> List[int]:
    numMap = {}

    for i, num in enumerate(nums):
        if target - num in numMap:
            return [numMap[target - num], i]
        numMap[num] = i

# 투 포인터를 이용
# 정렬된 상태에서 투 포인터를 이용할 수 있다
def twoSum5(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1

    while left != right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        
        else:
            return [left, right]