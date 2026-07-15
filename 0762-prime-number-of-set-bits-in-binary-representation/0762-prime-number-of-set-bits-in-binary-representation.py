class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        primes={2,3,5,7,11,13,17,19,23}
        for i in range(left,right+1):
            b=bin(i).count("1")
            if b in primes:
                count+=1
        return count

