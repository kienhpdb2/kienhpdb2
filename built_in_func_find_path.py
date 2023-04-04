import time
start_time = time.time()
from dijkstar import Graph, find_path

n, m, s = map(int, input().split())
g = Graph()
for i in range(m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)
        
for i in range(n):

    print (find_path(g, s, i))

end_time = time.time()
total_time = end_time - start_time
print("Thời gian chạy: ", total_time, " giây")

