class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_g={}
        st=[]
        for num in nums2:
            while st and st[-1]<num:
                pop_e=st.pop()
                next_g[pop_e]=num
            st.append(num)
        return [next_g.get(i,-1) for i in nums1]
        