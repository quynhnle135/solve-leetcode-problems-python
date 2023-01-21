class Solution:
    def squareOfArray(self, arr):
        result = [0] * len(arr)
        index = len(arr) - 1
        left = 0
        right = len(arr) - 1
        while left <= right:
            left_squared = arr[left] ** 2
            right_squared = arr[right] ** 2
            if left_squared > right_squared:
                result[index] = left_squared
                index -= 1
                left += 1
            else:
                result[index] = right_squared
                index -= 1
                right -=1
        return result


arr = [1, 2, 3, 4]
my_solution = Solution()
print(my_solution.squareOfArray(arr))