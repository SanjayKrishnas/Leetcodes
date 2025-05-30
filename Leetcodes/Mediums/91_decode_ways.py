class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def count_paths(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]

            one_path = count_paths(i + 1)
            two_path = 0

            if i + 1 < len(s):
                num = int(s[i:i+2])
                if num <= 26:
                    two_path = count_paths(i + 2)

            cache[i] = one_path + two_path
            return cache[i]

        return count_paths(0)