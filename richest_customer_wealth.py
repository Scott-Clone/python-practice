class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return([sum(acc) for acc in accounts])


