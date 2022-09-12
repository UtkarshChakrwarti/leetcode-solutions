class Solution:
    def isValid(self, s: str) -> bool:
        str = list(s.strip(" ")) 

        p_open = ["(", "[", "{"]
        p_close = [")", "]", "}"]
        t = ""
        if p_close.count(str[0]):
            return False
        
        p_stack = []
        for i in str:
            if p_open.count(i):
                p_stack.append(i)

            elif i == ")":
                if len(p_stack) == 0:
                    return False
                else:
                 
                    t = p_stack.pop()
                    if t != "(":
                        return False
                
                
            elif i == "]":
                if len(p_stack) == 0:
                    return False
                else:
                    t = p_stack.pop()
                    if t != "[":
                        return False
                    
            elif i == "}":
                if len(p_stack) == 0:
                    return False
                else:
                    t = p_stack.pop()
                    if t != "{":
                        return False
                    

        if len(p_stack) == 0:
            return True
        
