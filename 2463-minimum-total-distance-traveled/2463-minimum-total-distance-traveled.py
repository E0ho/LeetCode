class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        # factory -> 슬롯 배열로 풀기
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)

        R, F = len(robot), len(slots)
        INF = 10**20

        # dp[i][j] : 앞 i개의 로봇, 앞 j개의 슬롯
        dp = [[INF] * (F + 1) for _ in range(R + 1)]
        
        for j in range(F + 1):
            dp[0][j] = 0  # 로봇 0개면 비용 0

        for i in range(1, R + 1):
            for j in range(1, F + 1):
                # 슬롯 j 안 쓰기
                dp[i][j] = dp[i][j-1]

                # 슬롯 개수는 로봇보다 적으면 안 됨
                if i <= j:
                    cost = abs(robot[i-1] - slots[j-1])
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)

        return dp[R][F]
        
        # Input : 로봇[위치], 공장[위치, 개수]

        # 핵심 : 로봇들의 이동을 최소화하기
        
        # 생각1 : 바로바로 공장에 도착한 로봇을 수리하는게 이득인가? 지나쳐야하는 경우가 있을까?
            # 로봇 위치 : 0, 10, 11 / 공장 위치 : [8, 1], [20, 2] 이라면, 10위치의 로봇을 무작정 가까운 8로 보내는건 손해 (0 위치 로봇이 20까지 가야함)
            # 즉, 무작정 가까운 공장으로 달리는건 X
        
        # 생각2 : DP 점화식 활용

        