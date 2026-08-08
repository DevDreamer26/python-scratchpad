x = int(input("Enter the number: "))

if x<0:
    print(f"{x} is not a perfect square because it is negative.")
    exit()

square_root = int(x**0.5)

if square_root * square_root == x:
    print(f"{x} is a perfect square.")
else:
    print(f"{x} is not a perfect square.")

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if num < 0:
#             return False

#         square_root = int(num**0.5)

#         return square_root * square_root == num

# solution = Solution()
# print(solution.isPerfectSquare(16)) 
# print(solution.isPerfectSquare(14))     