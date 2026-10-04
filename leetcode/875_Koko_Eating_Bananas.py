#  Binary Search Implementation

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (mid + p - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
















# First attempt : 
    
# piles= [3,6,7,11]
# h = 8

# sum = 0 
    
# for k in range(1,max(piles)+1):
       
   
#         for p in piles:
#             output = (p+k -1)//k
#             sum += output
#             print(f"{p} ----->{output}")
            
#         print("________________")
#         print(sum)
        
#         print("________________")
#         if sum == h:
#             break
#         sum = 0
             
            
# print(f"Total ----> {sum}")
# print(f"Koko can eat with speed k = {k} in {h} hours without getting caught !")
    
    
# Second attempt : Clean and Correct but hitting TLE on large inputs
   # Linear : O(n)
        # for k in range(1, max(piles) + 1):
        #     hours = 0
        #     for p in piles:
        #         hours += (k + p - 1) // k
        #     if hours <= h:
        #         return k


