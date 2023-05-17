from readfile import read_edge_list as read

def ucs(graph, cost, start, end, path):

	answer = 10 ** 8  # Lưu trữ giá thành

	queue = [[0, start]]  # Hàng đợi sắp xếp theo giá thành với giá trị khởi tạo đi từ start và cost = 0

	print("Xuất phát từ: ", start)
	print("Điểm đến tại: ", end)

	# Từ điển dùng để lưu các nút đã được thăm, key là nút, value là 1, xác định nút đã được thăm, tránh lặp
	visited = {}

	# Nếu hàng đợi ưu tiên còn nút
	while len(queue) > 0:

		# Sắp xếp hàng đợi TĂNG DẦN
		queue = sorted(queue)

		# Lấy phần tử cuối hàng đợi
		p = queue[-1]
		if p[1] not in path:
			path.append(p[1])

		# Sau khi lấy thì xóa phần tử đó đi
		del queue[-1]

		# Giá trị đầu tiên được nhân với -1
		p[0] *= -1
		# Nếu nút đang xét nằm trong tập đích
		if p[1] == end:
			path.append(p[1])
			# Cập nhật nút giá thấp hơn
			if answer > p[0]:
				answer = p[0]
				path.pop()
			return answer

		# p[1] tức là đỉnh đang xét, nếu chưa nằm trong tập ĐÃ THĂM thì duyệt nút con
		if p[1] not in visited:
			# Trả về số đỉnh lân cận của đỉnh p[1]
			for adj_node in graph[p[1]]:
				# Tính giá thành tới các đỉnh lân cận
				queue.append([(p[0] + int(cost[(p[1], adj_node)])) * -1, adj_node])
		visited[p[1]] = 1  # Đánh dấu đỉnh p[1] đã được GHÉ THĂM

	return answer  # Trả về danh sách chi phí tới các đỉnh trong goal


def help_ucs_run(data, start, end):

	path = []
	graph = {}
	cost = {}

	for key in data.keys():
		edge = [key]
		adj_nodes = []
		for index, (neighbor, weight) in enumerate(data[key].items()):
			adj_nodes.append(neighbor)
			edge.append(neighbor)
			if len(edge) == 2:
				cost[tuple(edge)] = weight
				edge.pop(1)
			if len(adj_nodes) == 2:
				graph[key] = adj_nodes

	print(graph)
	print(cost)
	answer = ucs(graph, cost, start, end, path)
	print("Giá thành nhỏ nhất từ " + str(start) + " tới " + str(end) + " = ", str(answer))
	print("Các đỉnh được thuật toán duyệt: ", path)


# if __name__ == '__main__':
# 	data = read("edge_list.txt")
# 	path = []
# 	graph = {}
# 	cost = {}
#
# 	for key in data.keys():
# 		edge = [key]
# 		adj_nodes = []
# 		for index, (neighbor, weight) in enumerate(data[key].items()):
# 			adj_nodes.append(neighbor)
# 			edge.append(neighbor)
# 			if len(edge) == 2:
# 				cost[tuple(edge)] = weight
# 				edge.pop(1)
# 			if len(adj_nodes) == 2:
# 				graph[key] = adj_nodes
#
# 	print(graph)
# 	print(cost)
#
# 	start = "A"
# 	end = "E"
# 	answer = ucs(start, end)
# 	print("Giá thành nhỏ nhất từ " + str(start) + " tới " + str(end) + " = ", str(answer))
# 	print("Các đỉnh được thuật toán duyệt: ", path)
