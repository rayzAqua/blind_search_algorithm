"""
    Phần main
"""
from readfile import read_edge_list as read
from BFS import bfs
from DFS import dfs
from DLS import dls
from IDS import help_ids_run
from UCS_Final import help_ucs_run

def main():
    print("==========================================================================================================")
    print("CHUYÊN ĐỀ 2: THUẬT TOÁN TÌM KIẾM MÙ\n"
          "Chương trình được có thể thực các thuật toán tìm kiếm sau:\n"
          "1. Thuật toán Breadth-First Search (BFS) - Tìm kiếm theo chiều rộng.\n"
          "2. Thuật toán Depth-First Search (DFS) - Tìm kiếm theo chiều sâu.\n"
          "3. Thuật toán Depth-Limited Search (DLS) - Tìm kiếm theo chiều sâu với độ sâu giới hạn.\n"
          "4. Thuật toán Iterative Deepening Search (IDS) - Tìm kiếm theo chiều sâu với độ sâu giới hạn tăng dần.\n"
          "5. Thuật toán Uniform Cost Search (UCS) - Tìm kiếm theo chi phí thống nhất.")
    print("Đầu vào là một danh sách cạnh: edge_list.txt\n"
          "Đầu ra một mảng các nút đã được duyệt.")
    print("==========================================================================================================")

    while True:
        try:
            option = int(input("Hãy chọn từ 1 đến 5 để chạy thuật toán tương ứng: "))
            while option not in range(1, 6):
                option = int(input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: "))
            break
        except:
            print("Lựa chọn không hợp lệ !")

    print("==========================================================================================================")
    print("Input: ")
    nodes, graph = read("edge_list.txt")
    print("==========================================================================================================")

    if option == 1:
        while True:
            try:
                start = input("Nhập đỉnh bắt đầu trong danh sách nodes " + str(nodes) + " : ")
                while start not in nodes:
                    start = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        print("Kết quả sau khi thực hiện thuật toán BFS là:")
        bfs(graph, start)

    if option == 2:
        while True:
            try:
                start = input("Nhập đỉnh bắt đầu trong danh sách nodes " + str(nodes) + " : ")
                while start not in nodes:
                    start = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                end = input("Nhập đỉnh kết thúc trong danh sách nodes " + str(nodes) + " : ")
                while end not in nodes:
                    end = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        solution = dfs(graph, start, end)
        if solution is not None:
            print("Kết quả sau khi thực hiện thuật toán DFS là:", solution)
        else:
            print("Không tìm thấy đường đi!")

    if option == 3:
        while True:
            try:
                start = input("Nhập đỉnh bắt đầu trong danh sách nodes " + str(nodes) + " : ")
                while start not in nodes:
                    start = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                end = input("Nhập đỉnh kết thúc trong danh sách nodes " + str(nodes) + " : ")
                while end not in nodes:
                    end = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                depth = int(input("Nhập giới hạn độ sâu trong đoạn từ 0 đến 5: "))
                while depth not in range(0, 5):
                    depth = int(input("Lựa chọn bạn nhập không nằm trong đoạn [0, 5], hãy nhập lại: "))
                break
            except:
                print("Lựa chọn không hợp lệ !")

        solution = dls(graph, start, end, depth)
        if solution is not None:
            print("Kết quả sau khi thực hiện thuật toán DLS là:", solution)
        else:
            print("Không tìm thấy đường đi !")

    if option == 4:
        while True:
            try:
                start = input("Nhập đỉnh bắt đầu trong danh sách nodes " + str(nodes) + " : ")
                while start not in nodes:
                    start = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                end = input("Nhập đỉnh kết thúc trong danh sách nodes " + str(nodes) + " : ")
                while end not in nodes:
                    end = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                maxDepth = int(input("Nhập giới hạn độ sâu trong đoạn từ 0 đến 5: "))
                while maxDepth not in range(0, 5):
                    maxDepth = int(input("Lựa chọn bạn nhập không nằm trong đoạn [0, 5], hãy nhập lại: "))
                break
            except:
                print("Lựa chọn không hợp lệ !")

        help_ids_run(graph, start, end, maxDepth)

    if option == 5:
        while True:
            try:
                start = input("Nhập đỉnh bắt đầu trong danh sách nodes " + str(nodes) + " : ")
                while start not in nodes:
                    start = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        while True:
            try:
                end = input("Nhập đỉnh kết thúc trong danh sách nodes " + str(nodes) + " : ")
                while end not in nodes:
                    end = input("Lựa chọn bạn nhập không tồn tại, hãy nhập lại: ")
                break
            except:
                print("Lựa chọn không hợp lệ !")

        help_ucs_run(graph, start, end)


if __name__ == "__main__":
    main()
