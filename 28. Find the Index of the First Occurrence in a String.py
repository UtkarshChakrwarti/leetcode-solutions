def first_occurence(haystack: str, needle: str):
    
    haystack_list = list(haystack.strip(" "))    
    if len(needle) >= len(haystack):
        if needle == haystack:
            return 0
        return -1
    else:
        iter = len(haystack)-len(needle)
        needle_size = len(needle)
        for i in range(iter+1):
            
            if "".join(haystack_list[i:i+needle_size]) == needle:
                return i
            
            
    return -1 

haystack = "loveyou3000"
needle = "300"

print(first_occurence(haystack, needle))
