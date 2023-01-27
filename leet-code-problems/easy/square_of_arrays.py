class Solution:
    def sortedSquared(self, arr):
        left = 0
        right = len(arr) - 1
        result = [0] * len(arr)
        index = len(result) - 1
        while left <= right:
            leftSquared = arr[left]**2
            rightSquared = arr[right]**2
            if leftSquared > rightSquared:
                result[index] = leftSquared
                index -=1
                left += 1
            else:
                rightSquared = arr[right]**2
                result[index] = rightSquared
                right -= 1
                index -= 1
        return result


arr = [1, 2, 3, 4]
my_solution = Solution()
print(my_solution.sortedSquared(arr))

