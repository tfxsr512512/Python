data = [9, 10, 33, 3, 5, 18, 4, 30, 25, 2, 11]
data2 = [8, 3, 2, 1, -5, 19, 2, 4, 6, 7, 11]
for i in data:
    for j in data2:
        if i + j == 10:
            print([i, j])
