scores = [
    ["alex", 99],
    ["rain", 19],
    ["jack", 23],
    ["lame", 26],
    ["make", 76],
    ["dd", 29],
    ["gg", 30]
]

s1 = sorted(scores, key=lambda i: i[1])
s2 = sorted(scores, key=lambda i: i[1], reverse=True)
print(scores)
print(s1)
print(s2)
