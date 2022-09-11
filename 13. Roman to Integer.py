class Solution:
    def romanToInt(self, s: str) -> int:
        
        R_N = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        R_V = [1, 5, 10, 50, 100, 500, 1000]
        str_l = []
        str_l = list(s.strip(" "))
        sum = 0  
        while len(str_l) > 0 :
            
            if len(str_l) == 1:
                sum += R_V[R_N.index(str_l[0])]
                str_l.pop(0)
                break
            first_L  = str_l[0]
            second_L = str_l[1]
            if R_N.index(first_L) >= R_N.index(second_L) :
                sum += R_V[R_N.index(first_L)]
                str_l.pop(0)
            else:
                sum += R_V[R_N.index(second_L)] - R_V[R_N.index(first_L)]
                str_l.pop(0)
                str_l.pop(0)
        return sum
