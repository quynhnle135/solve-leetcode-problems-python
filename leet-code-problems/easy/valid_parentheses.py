class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []


class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in dict.values():
                stack.append(char)
            if char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False

        return stack == []




s = "("
my_solution = Solution()
print(my_solution.isValid(s))
