import collections
from readfile import read_edge_list as read

# Khai báo hàm BFS
'''
    Khởi tạo danh sách các đỉnh đã thăm, hàng đợi
    Gắn đỉnh thăm đầu tiên là root
    Trong khi hàng đợi còn, lấy đỉnh đầu tiên trong hàng đợi ra để duyệt

'''
def bfs(graph, start):
    visited, queue = set(), collections.deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()    # Lấy nút đầu tiên trong hàng đợi ra
        print(str(vertex) + "  ", end="")

        # Kiểm tra các nút lân cận của nút vừa lấy ra đã được duyệt hay chưa,
        # nếu chưa thì thêm vô danh sách duyệt và thêm vào hàng đợi
        for neighbour, weight in graph[vertex].items():
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# if __name__ == '__main__':
#
#     # Đọc vào danh sách cạnh
#     graph = read("edge_list.txt")
#     start = "A"
#     end = "E"
#     bfs(graph, start)