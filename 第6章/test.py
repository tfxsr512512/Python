n = 5  # 图有多少个点
m = 4  # 着色数
count = 0  # 方案数量
color = [0] * n

a = [[0, 1, 1, 1, 0],  # a数组代表无向图的邻接矩阵
     [1, 0, 1, 1, 1],
     [1, 1, 0, 1, 0],
     [1, 1, 1, 0, 1],
     [0, 1, 0, 1, 0]]


def OK(t):
    for j in range(len(a)):
        if a[t][j] == 1:
            if color[t] == color[j]:
                return False
    return True

def traceback(t):
    global count      # 使用全局变量
    oldvalue = 0
    if t == len(a):
        count = count+1
        return
    for i in range(1,m+1):      # i代表颜色
        oldvalue = color[t]
        color[t] = i
        if OK(t):
            traceback(t+1)
        color[t]=oldvalue


traceback(0)
print("count:",count)
