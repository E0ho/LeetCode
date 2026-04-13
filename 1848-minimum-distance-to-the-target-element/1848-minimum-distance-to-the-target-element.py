class Solution(object):
    def getMinDistance(self, nums, target, start):

        # Pointer 선언
        plus_idx = start
        minus_idx = start

        # 시작점
        if(nums[start] == target):
            return 0
        
        # 탐색 -> O(N)
        for i in range(1, len(nums)):
            if(plus_idx < len(nums) - 1):
                plus_idx += 1

            if(minus_idx != 0):
                minus_idx -= 1

            if(nums[plus_idx] == target or nums[minus_idx] == target):
                return i
        


# Input : nums, target, start
# Return : abs(i - start)

# i를 찾아라 : nums[i] == target
# abs(i - start)가 최소 : i와 start가 가까워야함

# nums[i] == target이 여러개 존재하는데 그 중 start 숫자와 가장 가까운 i 찾기

# start 숫자로 index 시작하기
# start 숫자에서 양방향 (-, +)로 각 pointer 이동
# target을 찾았을 때, pointer 이동 횟수 = 정답