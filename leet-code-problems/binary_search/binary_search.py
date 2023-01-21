class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
my_solution = Solution()
print(my_solution.binarySearch(nums, 9))  # 8
print(my_solution.binarySearch(nums, 1))  # 0
print(my_solution.binarySearch(nums, 17))  # -1
print(my_solution.binarySearch(nums, 7))  # 6

