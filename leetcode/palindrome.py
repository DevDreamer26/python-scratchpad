class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div =1 
        while x>= 10*div:
            div *= 10
        while x:
            if x // div != x % 10: return False
            x= (x%div)//10
            div = div/ 100
        return True




# Just fun here ----

# s = "A man, a plan, a canal: Panama"
# r = "racecar"

# cleaned_s = "".join(char for char in s if char.isalnum()).lower()
# cleaned_r = "".join(char for char in r if char.isalnum()).lower()


# print(cleaned_s)
# print(cleaned_r)


