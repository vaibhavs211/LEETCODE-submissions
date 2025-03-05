class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mx = prices[0]
        mx_prof = 0
        local_prof = 0
        for p in prices:
            if p>mx:
                mx = p
            if p < mn:
                mn = p
                mx = p
            local_prof = mx-mn
            if local_prof > mx_prof:
                mx_prof = local_prof
        return mx_prof