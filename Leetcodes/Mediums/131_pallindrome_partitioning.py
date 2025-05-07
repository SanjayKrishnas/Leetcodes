class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def palindromes(string, start, arr):
            # base case
            if start == len(string): 
                result.append(arr.copy())
                return

            # Try all possible substrings starting at index start
            for end in range(start, len(string)):
                # Check if substring s[start:end+1] is a palindrome
                substring = string[start:end+1]
                if substring == substring[::-1]:  # Check if it's a palindrome
                    arr.append(substring)
                    palindromes(string, end + 1, arr)
                    arr.pop()
            
            return
            
        palindromes(s, 0, [])
        return result
