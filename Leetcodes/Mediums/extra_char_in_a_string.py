class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        cache = {}

        def substrings(i):
            if i >= len(s):
                return 0
            
            if i in cache: return cache[i]

            start = i
            
            # Initialize result to a large value instead of 0
            result = float('inf')
            
            # Try ending the current substring at different positions
            for end in range(start, len(s)):
                # Check if this substring is in dictionary
                if s[start:end+1] in dictionary:
                    # If in dictionary, no extra chars for this segment
                    extra_chars = substrings(end + 1)
                else:
                    # If not in dictionary, all chars are extra
                    extra_chars = (end - start + 1) + substrings(end + 1)
                
                # Update with minimum result
                result = min(result, extra_chars)
            
            # Store result for this starting position
            cache[start] = result
            return result
        
        return substrings(0)