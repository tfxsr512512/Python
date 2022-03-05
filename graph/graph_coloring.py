def getAdjMatrix(path):  # 处理文件
    edge = []
    pointNum = 0
    with open(path, 'r') as fp:
        for line in fp.readlines():  # 将文件处理为图的邻接矩阵表示
            if line.startswith('p'):
                pointNum = int(line.split()[2])
                for i in range(pointNum):  # 列一个pointNum*pointNum的全为0矩阵
                    edge.append([0 for i in range(pointNum)])
            if line.startswith('e') and pointNum > 0:
                edge[int(line.split()[1]) - 1][int(line.split()[2]) - 1] = 1
                edge[int(line.split()[2]) - 1][int(line.split()[1]) - 1] = 1
    return edge, pointNum


edge, pointNum = getAdjMatrix(r'test.txt')
print('')
for i in edge:
    print('    ', end='')
    for j in i:
        print(j, end='\t\t')
    print('\n')
colorNum = 0
disabled = []

# 初始化color列表，用以记录每个顶点的着色情况
color = []
for i in range(pointNum):
    color.append(0)
edgeNum = [sum(e) for e in edge]
for k in range(pointNum):
    # 获取顶点最大度的索引值
    maxEdgePoint = [i for i in range(pointNum) if edgeNum[i] == max(edgeNum) and edgeNum[i] != 0]
    # 遍历最大度
    for p in maxEdgePoint:
        if p not in disabled:
            # 选取还未着色且度最大的点p开始着色
            color[p] = colorNum + 1
            disabled.append(p)
            edgeNum[p] = 0
            # temp用于查找该颜色可用来着色的下一个顶点
            temp = edge[p]
            for i in range(pointNum):
                if i not in disabled:
                    if temp[i] == 0:
                        # 为不冲突的顶点着色
                        color[i] = colorNum + 1
                        disabled.append(i)
                        edgeNum[i] = 0
                        # 增加当前颜色的禁忌点
                        temp = [x + y for (x, y) in zip(edge[i], temp)]
            # 需要新颜色
            colorNum = colorNum + 1

    # 每个顶点都已经着色
    if 0 not in color:
        break
print(color)
print(colorNum)

import networkx as nx
import matplotlib.pyplot as plt

# 创建一个网络
network = nx.Graph()
node = [i for i in range(pointNum)]
print(node)
network.add_nodes_from(node)
for i in range(pointNum):
    for j in range(pointNum):
        if edge[i][j] == 1:
            network.add_edge(i, j)

# nx.draw_networkx(network, with_labels=True)
color_lists = ["gold", "violet", "limegreen", "darkorange", "red", "blue", "green"]
color_list = [0] * pointNum
for i in range(1, colorNum + 1):
    for j in range(pointNum):
        if color[j] == i:
            color_list[j] = color_lists[i]

nx.draw_networkx(network, node_color=color_list, with_labels=True)
plt.show()
