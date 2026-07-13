class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st=[]
        res=list(prices)
        for i,price in enumerate(prices):
            while st and prices[st[-1]]>=price:
                po_it=st.pop()
                res[po_it]-=price
            st.append(i)
        return res