class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def isDivisor(divisor, string):
            if len(string) % len(divisor) != 0: return False

            i = 0
            while i < len(string):
                if string[i:i+len(divisor)] != divisor:
                    return False

                i += len(divisor)
            
            return True

        if len(str1) < len(str2):
            smaller = str1
            larger = str2
        else:
            smaller = str2
            larger = str1

        result = ""
        cur = ""
        for c in smaller:
            cur += c

            #check if it is a divisor of cur 1
            if isDivisor(cur, smaller):
            #check if it is a divisor of cur 2
                if isDivisor(cur, larger):
                    result = cur
        
        return result