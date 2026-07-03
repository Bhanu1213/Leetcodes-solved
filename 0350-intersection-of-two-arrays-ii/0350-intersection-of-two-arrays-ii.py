class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1==nums2:return nums1
        com=[]
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                com.append(i)
        return com