class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+2], cost[i+1])
            
        return min(cost[0], cost[1])   
    
# OR WITH DP        
#         cost.append(1)
#         dp = defaultdict (int)
#         def child(index):
#             if index == len(cost)-1: 
#                 return cost[index]
            
#             if index > len(cost):
#                 return 
            
#             if dp[index]:
#                 return dp[index]
            
#             one = child(index+1)            
#             two = child(index+2)
            
#             if one and two:
#                 dp[index] = min(one , two) + cost[index]
#                 return dp[index]
            
#             elif one: 
#                 dp[index] = one + cost[index]
#                 return dp[index]
            
#             elif two:
#                 dp[index] = two + cost[index]
#                 return dp[index]
            
#             else:
#                 return 0
            
#         return min(child(0) , child(1)) - 1
