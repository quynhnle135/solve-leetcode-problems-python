from stack import Stack


class Solution:
    def is_valid_parentheses(self, parentheses):
        open_parentheses = Stack()
        for paren in parentheses:
            if paren in "[{(":
                open_parentheses.push(paren)
            else:
                if open_parentheses.is_empty():
                    return False
                if (paren == "]" and open_parentheses.pop() != "[") or (paren == "}" and open_parentheses.pop() != "{") or (paren == ")" and open_parentheses.pop() != "("):
                    return False
        return open_parentheses.is_empty()


my_solution = Solution()
print(my_solution.is_valid_parentheses("[]"))
print(my_solution.is_valid_parentheses("[)"))
print(my_solution.is_valid_parentheses("[{()}]"))

print("------")


def check_valid_parentheses(s):
    stack = []
    dict = {"}": "{", "]": "[", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        if char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
    return stack == []


print(check_valid_parentheses("[]"))
print(check_valid_parentheses("[)"))
print(check_valid_parentheses("[{()}]"))
