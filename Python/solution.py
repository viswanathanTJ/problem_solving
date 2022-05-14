from collections import defaultdict
import heapq


def network_delay(times, n, k):
    adj_list = defaultdict(list)
        
    for x,y,w in times:
        adj_list[x].append((w, y))
    
    visited=set()
    heap = [(0, k)]
    while heap:
        travel_time, node = heapq.heappop(heap)
        visited.add(node)
        
        if len(visited)==n:
            return travel_time
        
        for time, adjacent_node in adj_list[node]:
            if adjacent_node not in visited:
                heapq.heappush(heap, (travel_time+time, adjacent_node))
            
    return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(network_delay(times, k))