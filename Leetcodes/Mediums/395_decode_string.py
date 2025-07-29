class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(num, i): #should return things inside the parenthesis
            string = ""

            while i < len(s):
                if s[i] == '[':
                    i += 1
                    continue
                elif s[i] == ']':
                    break
                elif s[i].isalpha():
                    string += s[i]
                    i += 1
                elif s[i].isdigit():
                    next_num = ""
                    while s[i] != '[':
                        next_num += s[i]
                        i += 1

                    paren, j = helper(next_num, i)

                    string += paren
                    i = j + 1                
                
            result = ""
            for k in range(int(num)):
                result += string

            #print(result, i)
            return (result, i)

        result = ""
        i = 0
        
        while i < len(s):
            if s[i].isdigit(): #then we need to recurse
                num = ""
                while s[i] != '[':
                    num += s[i]
                    i += 1

                paren, j = helper(num, i)

                result += paren
                i = j + 1               
            elif s[i].isalpha():
                result += s[i]
                i += 1
        
        return result


#OR USE THE STACK METHOD OF GROWING STACK AND POPPING WHEN WE REACH A ]

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)