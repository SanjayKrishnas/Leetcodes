from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is in wordList
        if endWord not in wordList:
            return 0
        
        # Create set of words for O(1) lookups
        word_set = set(wordList)
        word_set.add(beginWord)  # Make sure beginWord is in the set
        
        # Create adjacency list more efficiently
        adj_list = defaultdict(list)
        
        # For each word, generate all possible one-character transformations
        for word in word_set:
            for i in range(len(word)):
                # Create a pattern with a wildcard for this position
                # e.g., "hit" -> "*it", "h*t", "hi*"
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word != word and new_word in word_set:
                        adj_list[word].append(new_word)
        
        # Now use your original BFS code
        visited = set()
        depth = 1

        level_order = deque()
        level_order.append(beginWord)
        visited.add(beginWord)

        while level_order:
            length = len(level_order)

            for i in range(length):
                cur_word = level_order.popleft()

                # Check if we reached end
                if cur_word == endWord: 
                    return depth

                cur_list = adj_list[cur_word]

                for word in cur_list:
                    if word in visited: 
                        continue
                    level_order.append(word)
                    visited.add(word)
            
            depth += 1
        
        return 0