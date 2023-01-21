class Solution:
    def isPalindrome(self, num):
        if num < 0:
            return False
        if num < 10:
            return True

        duplicated = num
        reversed = 0
        while duplicated > 0:
            digit = duplicated % 10
            reversed = reversed * 10 + digit
            duplicated //= 10
        return reversed == num


my_solution = Solution()
print(my_solution.isPalindrome(12))