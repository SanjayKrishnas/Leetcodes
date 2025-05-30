class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        in_deg = {}
        adj_list = {}

        #1. First get all the letters and put it into the adj_list
        for word in words:
            for char in word:
                if char not in adj_list:
                    adj_list[char] = []
                    in_deg[char] = 0
        
        #2. Generate our in_deg array and adj_list
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))
            found_diff = False

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].append(word2[j]) #this would be like n -> f
                    in_deg[word2[j]] += 1
                    found_diff = True
                    break
            
            if found_diff == False and len(word1) > len(word2): #ERROR: this cannot happen
                return ""
            
        
        letters = len(in_deg.keys())

        #3. Now run toposort
        queue = deque()
        for key in in_deg.keys(): #get all keys with in_deg 0
            if in_deg[key] == 0:
                queue.append(key)

        result = ""
        while queue:
            letter = queue.popleft()
            result += letter
            let_list = adj_list[letter]

            for let in let_list:
                in_deg[let] -= 1
                if in_deg[let] == 0: queue.append(let)
        
        if len(result) != letters: return "" #this means we have a cycle somewhere

        return result

        

        



        