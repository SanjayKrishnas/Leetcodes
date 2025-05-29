class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        all_tasks = []

        for i in range(len(tasks)):
            s, p = tasks[i]
            all_tasks.append((s, p, i))
        
        all_tasks.sort()

        heap = []

        t_processed = 0
        t_index = 0
        time = 0
        result = []

        while t_processed < len(tasks):
            if heap:
                t, i = heapq.heappop(heap)
                time += t
                result.append(i)
                t_processed += 1

                while t_index < len(all_tasks):
                    if all_tasks[t_index][0] <= time: #we can add the current task to the heap
                        adds, addt, addi = all_tasks[t_index]
                        heapq.heappush(heap, (addt, addi))
                        t_index += 1
                    else: #no more tasks to add
                        break

            else:
                time += (all_tasks[t_index][0] - time) #go to the time

                adds, addt, addi = all_tasks[t_index]
                heapq.heappush(heap, (addt, addi)) #add it to the heap
                t_index += 1
        
        return result

