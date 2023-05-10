"""
    Depth-first Search: Tìm kiếm theo độ sâu
"""

from readfile import read_edge_list as read

def dfs(graph, start, end):

    """
        Khai báo lần lượt ngăn xếp LIFO và một mảng đánh dấu các nút đã được duyệt
    """
    # Khởi tạo ngăn xếp với nút start
    fringe = [start]
    # Mảng visited đánh dấu các nút đã được duyệt đồng thời cũng là đường đi của thuật toán
    visited = []

    # Khởi tạo vòng lặp
    while fringe:
        # Lấy ra nút đầu tiên của ngăn xếp (Last In First Out)
        node = fringe.pop(0)

        # Nếu nút đó là đích thì trả về mảng visited + [node]
        if node == end:
            return visited + [node]

        # Nếu nút node chưa được đánh dấu thì thêm nó vào mảng visited để đánh dấu là đã được duyệt
        if node not in visited:
            visited.append(node)

        # Tiến hành lấy các nút kề của nút node và thêm vào đầu danh sách fringe (LIFO)
        i = 0
        for neighbor, weight in graph[node].items():
            # Chỉ được thêm vào fringe nếu nút đó chưa được đánh dấu là visited
            if neighbor not in visited:
                fringe.insert(i, neighbor)
                i += 1

    # Nếu không tìm thấy gì thì trả về None
    return None

#
# if __name__ == "__main__":
#     # Đọc vào danh sách cạnh
#     graph = read("edge_list.txt")
#     start = "A"
#     end = "E"
#     print("Solutions:", dfs(graph, start, end))
