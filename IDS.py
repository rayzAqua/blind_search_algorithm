from collections import defaultdict
from readfile import read_edge_list as read

def dls(graph, start, end, maxDepth, visited):
    if start not in visited:
        visited.append(start)

    if start == end:
        return [start]

    if maxDepth <= 0:
        return None

    for neighbor, weight in graph[start].items():
        if neighbor not in visited:
            path = dls(graph, neighbor, end, maxDepth - 1, visited)
            if path is not None:
                return [start] + path

    return None


# Sử dụng thuật toán IDS để tìm kiếm đường đi từ đỉnh src đến đỉnh target với độ sâu tối đa là max-depth
def ids(graph, src, target, maxDepth):
    for depth in range(1, maxDepth+1):
        solution = dls(graph, src, target, depth, visited=[])
        if solution is not None:
            return solution, depth
    return None, maxDepth

def help_ids_run(graph, start, end, maxDepth):
    solution, depth = ids(graph, start, end, maxDepth)
    if solution is not None:
        print("Tìm thấy kết quả đi từ đỉnh " + start + " đến đỉnh " + end + " là", solution, "tại độ sâu là:", depth)
    else:
        print("Không tìm thấy đường đi tại đỉnh bắt đầu là " + str(start) + " với độ sâu là " + str(maxDepth));

# if __name__ == "__main__":
#     graph = read("edge_list.txt")
#
#     start = "A"
#     end = "E"
#     maxDepth = 4
#
#     solution, depth = ids(graph, start, end, maxDepth)
#     if solution is not None:
#         print("Tìm thấy kết quả đi từ đỉnh " + start + " đến đỉnh " + end + " là", solution, "tại độ sâu là:", depth)
#     else:
#         print("Không tìm thấy gì cả")
