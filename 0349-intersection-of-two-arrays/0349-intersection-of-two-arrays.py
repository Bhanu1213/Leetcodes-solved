class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        com=[]
        n1=set(nums1);n2=set(nums2)
        if len(n1)>len(n2): n1,n2=n2,n1
        for i in n1:
            if i in n2:
                com.append(i)
        return com
    