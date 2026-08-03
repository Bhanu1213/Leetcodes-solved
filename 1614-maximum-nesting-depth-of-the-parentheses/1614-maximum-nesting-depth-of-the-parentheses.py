class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        best=0
        for i in s:
            best=max(len(st),best)
            if i=="(":
                st.append(i)
            elif i==")":
                st.pop()
        return best
        