
def read_edge_list(fileName):
    # Mở file để đọc
    file = open(fileName, "r")
    # Đọc từng dòng và lưu vào list data
    data = file.readlines()
    data.sort()

    print(data)

    all_edges = []
    nodes = []
    adj_nodes_list = {}

    for edge in data:
        # Danh sách các cạnh
        edge = edge.strip().split(" ")
        if len(edge) > 1:
            all_edges.append(tuple(edge))
        else:
            edge.append(None)
            all_edges.append(tuple(edge))

        # Danh sách các nút cha
        for node in edge[0:2]:
            if node not in nodes and node is not None:
                nodes.append(node)

    nodes.sort()
    # Duyệt qua toàn bộ danh sách nodes, tiến hành tìm ra tất cả các nút kề của node
    for node in nodes:
        adj_nodes = {}
        # Với một nút node, duyệt qua toàn bộ các cạnh có trong danh sách all_edges để tìm ra các nút kề của nút node
        # Chú ý cần phải xét hai chiều
        # all_edges là list chứa các tuple, các tuple là các cạnh ghi trong file txt
        for edge in all_edges:
            # Vì là đồ thị vô hướng nên cần phải xét cả hai nút trong một cạnh (tương đương hai chiều của hai nút)
            # Lần lượt kiểm tra hai nút trong một cạnh để kiểm tra xem cạnh đó có đang chứa nút node đang xét không.
            # Nếu đúng là nó thì thêm nút còn lại vào danh sách nút kề.
            if edge[0] == node and edge[1] is not None:
                adj_nodes[edge[1]] = edge[2]

            if edge[1] == node:
                adj_nodes[edge[0]] = edge[2]

        adj_nodes_list[node] = adj_nodes

    # Tạo ra danh sách kề với key là nút cha và value là danh sách các nút kề

    # Đóng file
    file.close()

    print("Danh sách cạnh: ", all_edges)
    print("Danh sách các đỉnh: ", nodes)
    print("Danh sách các đỉnh lân cận và trọng số: ", adj_nodes_list)

    return nodes, adj_nodes_list

