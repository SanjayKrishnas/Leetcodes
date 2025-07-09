class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        #if skip == True then we already deleted a char
        def findPaliHelper(l, r, skip):
            if l >= r: return True

            if s[l] == s[r]:
                return findPaliHelper(l + 1, r - 1, skip)
            elif skip == True: #if they aren't equal and we ALREADY DELETED then return False
                return False
            else:
                return (findPaliHelper(l + 1, r, True) or findPaliHelper(l, r - 1, True))

            return False #shouldn't get here
            
        return findPaliHelper(0, len(s) - 1, False)
