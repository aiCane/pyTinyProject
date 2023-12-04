# 在一个给定的由数字 '0' 和 '2' 组成的矩阵中寻找横向往右、
# 纵向往下和斜向往右下的 '2020' 排列，
# 原题中给定的矩阵是300行300列的，
# 在一个txt文件中存放。

def check(s):
    return s == '2020'


matrix = []
s = input()
while '1' not in s:
    matrix.append(list(s))
    s = input()
n, m = len(matrix), len(matrix[0])
ans = 0
for i in range(n):
    for j in range(m):
        if i + 3 < n and check(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]):
            ans += 1
        if j + 3 < m and check(matrix[i][j:j+4]):
            ans += 1
        if i + 3 < n and j + 3 < m and check(matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]):
            ans += 1
print(ans)
