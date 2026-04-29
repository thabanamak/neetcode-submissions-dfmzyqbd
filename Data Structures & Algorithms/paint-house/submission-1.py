class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        #have to paint a certain amt of houses, no two adjacent houses can have same colour
        #recurse, to have gotten to an answer, '
        #we either chose the previous house with one colour so were left with two options
        #basically do if, for first house have freedom to paint any house
        #for houses after, make a dp[cost][colour], and colour must be previous house's colour

        memo = {}
        
        def dfs(house_idx, last_colour):
            state = (house_idx, last_colour)
            if house_idx == len(costs):
                return 0
            if state in memo:
                return memo[state]
            
            best = float('inf')
            for colour_idx in range(3):
                if colour_idx != last_colour:
                    cost = costs[house_idx][colour_idx] + dfs(house_idx + 1, colour_idx)
                    best = min(best, cost)
            memo[(state)] = best
            return best
                
                
        mincost = dfs(0, -1)
        return mincost

                
                


        