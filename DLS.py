"""
    Depth-limited Search: Tìm kiếm giới hạn độ sâu
"""

from readfile import read_edge_list as read

def dls(graph, start, end, depth, visited=[]):

    # Đánh dấu nút đã được duyệt - khởi đầu bằng nút start
    if start not in visited:
        visited.append(start)

    # Nếu đúng là nút đích thì trả về start
    if start == end:
        return [start]

    # Nếu không tìm thấy nút đích mà depth == 0 thì trả về không tìm thấy gì cả
    if depth <= 0:
        return None

    # Lấy nút kề của nút start và kiểm tra xem nó đã được duyệt chưa, nếu chưa thì gọi đệ quy tiếp tục tìm
    # nút kề của nó. Lặp đi lặp lại đến khi tìm được nút đích hoặc depth == 0
    for neighbor, weight in graph[start].items():
        if neighbor not in visited:
            path = dls(graph, neighbor, end, depth-1, visited)
            # Nếu path không None có nghĩa là đệ quy đã trả về một nút (cụ thể là nút được lưu ở biến start)
            # và gán nó cho biến path. Sau đó, lấy path + với nút được lưu ở biến start tại lần gọi đệ quy trước đó,
            # ta thu được đường đi đến nút đích.
            if path is not None:
                return [start] + path

    return None


# if __name__ == "__main__":
#     # Đọc vào danh sách cạnh
#     graph = read("edge_list.txt")
#     start = "A"
#     end = "E"
#     depth = 2
#     print("Solutions:", dls(graph, start, end, depth))