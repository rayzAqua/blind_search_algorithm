
def read_edge_list(fileName):
    # Mở file để đọc
    file = open(fileName, "r")
    # Đọc từng dòng và lưu vào list data
    data = file.readlines()

    all_edges = []
    nodes = []
    adj_nodes_list = {}

    for edge in data:
        # Danh sách các cạnh
        edge = edge.strip().split(" ")
        all_edges.append(tuple(edge))
        # Danh sách các nút cha
        if edge[0] not in nodes:
            nodes.append(edge[0])

    # Duyệt qua toàn bộ danh sách nodes, tiến hành tìm ra tất cả các nút kề của node
    for node in nodes:
        adj_nodes = {}
        # Với một nút node, duyệt qua toàn bộ các cạnh có trong danh sách all_edges để tìm ra các nút kề của nút node
        # Chú ý cần phải xét hai chiều
        for edge in all_edges:
            # Vì là đồ thị vô hướng nên cần phải xét cả hai nút trong một cạnh (tương đương hai chiều của hai nút)
            # Lần lượt kiểm tra hai nút trong một cạnh để kiểm tra xem cạnh đó có đang chứa nút node đang xét không.
            # Nếu đúng là nó thì thêm nút còn lại vào danh sách nút kề.
            if edge[0] == node:
                adj_nodes[edge[1]] = edge[2]
            if edge[1] == node:
                adj_nodes[edge[0]] = edge[2]
        adj_nodes_list[node] = adj_nodes

    # Tạo ra danh sách kề với key là nút cha và value là danh sách các nút kề

    # Đóng file
    file.close()

    print("Edge Lists: ", all_edges)
    print("Nodes: ", nodes)
    print("Adjacency Nodes: ", adj_nodes_list)

    return adj_nodes_list

