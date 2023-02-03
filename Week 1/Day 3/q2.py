class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack, idx = [], 0
        while idx < len(path):
            if path[idx] == '..':
                if stack:
                    stack.pop()
            elif path[idx] == '.' or len(path[idx]) == 0:
                pass
            else:
                stack.append("/" + path[idx])
            idx += 1
        return "".join(stack) if len(stack) >= 1 else "/"