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
        parentheses = Stack()
        for paren in s:
            if paren in "([{":
                parentheses.push(paren)
            else:
                if parentheses.is_empty():
                    return False
                elif parentheses.pop() == "(" and paren != ")":
                    return False
                elif parentheses.pop() == "[" and paren != "]":
                    return False
                elif parentheses.pop() == "{" and paren != "}":
                    return False
        return True


s = "(((]]]"
my_solution = Solution()
print(my_solution.isValid(s))