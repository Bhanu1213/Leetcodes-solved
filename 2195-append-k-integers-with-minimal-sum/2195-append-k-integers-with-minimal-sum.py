class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # l=[]
        # i=1
        # while k!=0:
        #     if i not in nums:
        #         l.append(i)
        #         k-=1
        #     i+=1
        # return sum(l)
        ans, lo = 0, 1
        cnt = 0
        for num in sorted(nums):
            if num > lo:
                hi = min(num - 1, k - 1 + lo)
                cnt = hi - lo + 1
                ans += (lo + hi) * cnt // 2 
                k -= cnt
                if k == 0:
                    return ans
            lo = num + 1
        if k > 0:
            ans += (lo + lo + k - 1) * k // 2
        return ans
