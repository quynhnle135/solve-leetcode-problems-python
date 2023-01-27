class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (right - left) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def search_in_2d_array_bs(self, matrix, target):
        for row in range(0, len(matrix)):
            if self.binarySearch(matrix[row], target):
                return True
        return False

    def searchIn2DArray(self, matrix, target):
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix[0])):
                if matrix[row][column] == target:
                    return True
        return False


    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        begin = 0
        end = m * n - 1
        while begin < end:
            mid = (begin + end) // 2
            if matrix[mid//m][mid%m] == target:
                return True
            elif target > matrix[mid//m][mid%m]:
                begin = mid + 1
            else:
                end = mid - 1
        return False



my_matrix = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
my_solution = Solution()
print(my_solution.searchMatrix(my_matrix, target=7))
# print(my_solution.searchIn2DArray(my_matrix, target=7))
# print(my_solution.search_in_2d_array_bs(my_matrix, target=7))
# print(my_solution.searchIn2DArray(my_matrix, target=12))
# print(my_solution.search_in_2d_array_bs(my_matrix, target=12))

# def print_2d_matrix(matrix):
#     for row in range(0, len(matrix)):
#         for column in range(0, len(matrix[0])):
#             print(matrix[row][column], end=" ")
#         print()
#
#
#
# print_2d_matrix(my_matrix)

