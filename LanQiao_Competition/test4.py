# 在蛇形排列矩阵中，第20行第20列的数字是多少？蛇形排列方式如图所示：
#  1  2  6  7 15
#  3  5  8 14
#  4  9 13
# 10 12
# 11

row = {"1": 1}

for i in range(2, 50):
    if i % 2 != 0:
        row[str(i)] = row[str(i - 1)] + 1
    if i % 2 == 0:
        row[str(i)] = row[str(i - 1)] + 2 * (i - 1)

print(row[str((20 - 1) * 2)] + 20)

# 参考答案：定义两种遍历模式，一种是有↗方向，一种是↙方向，判断行号加上列号的和是单数还是偶数
# i = 0
# j = 0
# num = 0
# while True:
#     num += 1
#     if i == 19 and j == 19:
#         break
#     if (i+j)&1:
#         i += 1
#         if j > 0:
#             j -= 1
#     else:
#         j += 1
#         if i > 0:
#             i -= 1
# print(num)
