class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ar=[first]
        for i in range(len(encoded)):
            k=encoded[i]^ar[-1]
            ar.append(k)
        return ar

        