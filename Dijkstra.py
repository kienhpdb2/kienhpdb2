import time
start_time = time.time()
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # số đỉnh của đồ thị
        self.graph = defaultdict(list) # graph để lưu danh sách các cạnh
        self.src=0 # đỉnh nguồn
    # thêm 1 cạnh vào đồ thị
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
    # in kết quả
    def printArr(self, dist, trace):
        print("Vertex \t Distance from Source\tPath")
        for i in range(self.V):
            path = self.trace_path(trace, self.src, i)
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

    def dijkstra(self, src):
        self.src=src
        dist = [float("inf")] * self.V  # Khởi tạo khoảng cách từ đỉnh nguồn đến các đỉnh khác là vô cực
        dist[src] = 0  # Khoảng cách từ đỉnh nguồn đến chính nó là 0
        trace = [-1] * self.V  # Lưu đường đi từ đỉnh nguồn đến các đỉnh khác, ban đầu tất cả các đỉnh đều không có đường đi

        pq = []  # Priority queue để lấy đỉnh có khoảng cách ngắn nhất
        heapq.heappush(pq, (0, src))  # Đưa đỉnh nguồn vào priority queue

        while pq:
            # Lấy đỉnh có khoảng cách ngắn nhất từ đỉnh nguồn
            min_dist, u = heapq.heappop(pq)

            # Kiểm tra các đỉnh kề của đỉnh u
            for v, w in self.graph[u]:
                # Nếu có đường đi từ đỉnh nguồn đến v thông qua u và khoảng cách hiện tại của v lớn hơn khoảng cách mới
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    # Cập nhật khoảng cách từ đỉnh nguồn đến v và lưu đường đi từ u đến v
                    dist[v] = dist[u] + w
                    trace[v] = u
                    # Đưa v vào priority queue để tiếp tục tìm kiếm đỉnh có khoảng cách ngắn nhất
                    heapq.heappush(pq, (dist[v], v))

        self.printArr(dist, trace)

if __name__ == '__main__':
    # g = Graph(6)
    # g.addEdge(0, 1, 5)
    # g.addEdge(0, 2, 3)
    # g.addEdge(1, 3, 6)
    # g.addEdge(1, 4, 2)
    # g.addEdge(2, 1, 1)
    # g.addEdge(2, 4, 9)
    # g.addEdge(2, 5, 7)
    # g.addEdge(3, 4, 1)
    # g.addEdge(4, 5, 4)
    # g.dijkstra(0)
    n, m, s = map(int, input().split())
    g = Graph(n)
    for i in range(m):
            u, v, w = map(int, input().split())
            g.addEdge(u, v, w)

    g.dijkstra(s)
    
end_time = time.time()
total_time = end_time - start_time
print("Thời gian chạy: ", total_time, " giây")

