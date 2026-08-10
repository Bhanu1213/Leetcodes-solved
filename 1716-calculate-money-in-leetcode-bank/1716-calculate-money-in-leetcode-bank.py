class Solution:
    def totalMoney(self, n: int) -> int:
        weeks=n//7
        remain_days=n%7
        week=28*weeks+7*(weeks*(weeks-1))//2
        remain=0
        money=weeks+1
        for i in range(remain_days):
            remain+=money+i
        return week+remain

