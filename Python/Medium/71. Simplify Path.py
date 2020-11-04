class Solution:
    def simplifyPath(self, path: str) -> str:
        direction_list = [i for i in path.split("/") if i != "" and i != "."]
        
        stack = []
        
        for i in direction_list:
            if i != "..":
                stack.append(i)
            else:
                if stack != []:
                    stack.pop()
        
        return "/"+"/".join(stack)