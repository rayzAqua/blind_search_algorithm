"""
    Depth-limited Search - Tìm kiếm giới hạn độ sâu
"""

from readfile import read_edge_list as read

def DLS(graph, start, end):
    # Tìm kiếm theo chiều sâu:
    # Khởi tạo một danh sách rỗng, danh sách này sẽ chứa các nút đã được duyệt
    # Đầu tiên, thêm nút bắt đầu vào danh sách rỗng trên và tiến hành thêm các nút kề với nút bắt đầu vào danh sách O.
    # Lấy một nút kề đã được thêm vào danh sách theo thứ tự của bảng chữ cái alphabet
    # Tiếp tục thêm các nút kề của nút đó vào danh sách O, chú ý các nút được thêm vào phải đảm
    # bảo quy tắc Last In Fist Out và theo thứ tự alphabet
    # Lặp lại cho đến khi đến nút sâu nhất.
    # Tiến hành kiểm tra xem nút sâu nhất đó có phải là nút đích không ? Nếu đúng thì đó là kết quả đường đi
    # Nếu không thì tiếp tục duyệt qua các nút còn lại trong danh sách và lặp lại việc tìm kiếm nút sâu nhất
    # cho đến khi tìm ra được nút đích

    # Danh sách chứa các nút đã được duyệt qua
    visited = []
    # Danh sách chứa các nút đang đợi để được duyệt
    fringe = [start]

    while fringe:
        node = fringe.pop(0)
        if node not in visited:
            visited.append(node)
            if node == end:
                return visited
            for neighbor, weight in graph[node].items():
                if neighbor not in fringe:
                    fringe.append(neighbor)
            print(fringe)

    return None


if __name__ == "__main__":
    # Đọc vào danh sách cạnh
    graph = read("edge_list.txt")
    start = "A"
    end = "D"

    print("Solutions:", DLS(graph, start, end))
