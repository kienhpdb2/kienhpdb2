import time
start_time = time.time()
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices # thuộc tính V là số đỉnh của đồ thị
        self.graph = defaultdict(list) # thuộc tính graph để lưu danh sách các cạnh
        self.trace = [-1] * vertices # mảng truy vết
        self.src=0 # đỉnh nguồn
        
    # thêm 1 cạnh vào đồ thị
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
     # in kết quả
    def printArr(self, dist):
        print("Vertex \t Distance from Source\tPath")
        for i in range(self.V):
            path = self.trace_path(self.trace, self.src, i)
            print("{} \t {}\t\t\t{}".format(i, dist[i], path))
    # hàm truy vết đường đi
    def trace_path(self, trace, s, u):
        if u != s and trace[u] == -1:
            return []
        path = [u]
        while trace[u] != -1:
            path.insert(0, trace[u])
            u = trace[u]
        return path

    def BellmanFord(self, src):
        self.src=src
         # B1: Khởi tạo khoảng cách từ src đến các đỉnh khác
        # là Inf
        dist = [float("inf")] * self.V
        dist[src] = 0
        # B2:Lặp lại quá trình tìm đường đi ngắn nhất cho tất cả các đỉnh 
        # trong đồ thị (V-1 lần lặp)
        for _ in range(self.V - 1):
             
            # Duyệt qua từng cạnh trong đồ thị, và nếu khoảng cách 
            # từ đỉnh s đến đỉnh v còn có thể cải thiện được 
            # thì cập nhật giá trị dist[v]
            for u in range(self.V):
                for v, w in self.graph[u]:
                    if dist[u] != float("inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        self.trace[v] = u
        # B3: Kiểm tra chu trình âm.

        cycle_flag = False  # biến cờ để theo dõi chu trình âm  
        for _ in range (2):
            for u in range(self.V):
                for v, w in self.graph[u]:
                    if dist[u] == float("-Inf"):
                        dist[v] = float("-Inf")
                        self.trace[v] = -1
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        if not cycle_flag:  # nếu chưa in thông báo
                            print("Graph contains negative weight cycle")
                            cycle_flag = True  # cập nhật biến cờ
                        dist[v] = float("-Inf")
                        self.trace[v] = -1

        self.printArr(dist)
if __name__ == '__main__':
    # g = Graph(6)
    # g.addEdge(0, 1, -1)
    # g.addEdge(0, 2, 4)
    # g.addEdge(1, 4, 1)
    # g.addEdge(2, 3, 30)
    # g.addEdge(3, 1, -2)
    # g.addEdge(4, 3, -3)
    # g.addEdge(5, 4, 1)
    # g.BellmanFord(0)
    n, m, s = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        u, v, w = map(int, input().split())
        g.addEdge(u, v, w)
    g.BellmanFord(s)

end_time = time.time()
total_time = end_time - start_time
print("Thời gian chạy: ", total_time, " giây")

