class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in {'{','(','['}:
                stack.append(ch)
            else:
                if not (len(stack) != 0 and self.compliment(stack.pop() + ch)):
                    return False
        if stack:
            return False
        return True


    def compliment(self, a: str) -> bool:
        if a in {'{}', '()', '[]'}:
            return True
        return False
