class Solution:
    def find_sum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    def find_sum_using_map(self, nums, target):
        hashmap = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return [-1, -1]

arr = [1, 2, 3, 4]
target = 3
my_solution = Solution()
print(my_solution.find_sum_using_map(arr, target))
print(my_solution.find_sum(arr, target))



