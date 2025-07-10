class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #if we build a valid graph of the topological sort then we can then query it for the queuries

        hashmap = {} #this is going to map node value to the node
        
        #create the nodes for each course
        for i in range(0, numCourses):
            hashmap[i] = Node(i)

        for x, y in prerequisites:
            preNode = hashmap[x]
            toNode = hashmap[y]

            preNode.children.append(toNode)

        #process the graph
        dependencies = {} #val ->  to its dependencies
        def findDependencies(val):
            if val in dependencies: 
                return dependencies[val]

            result = set()
            curNode = hashmap[val]
            for children in curNode.children:

                childSet = findDependencies(children.val)
                for num in childSet:
                    result.add(num)
                
                result.add(children.val) #NOTE: don't forget to add the value of the child too lol
            
            dependencies[val] = result
            return result

        for i in range(numCourses):
            findDependencies(i)            

        print(dependencies)

        result = []
        for query in queries:
            x, y  = query
            if y in dependencies[x]:
                result.append(True)
            else:
                result.append(False)

        return result
