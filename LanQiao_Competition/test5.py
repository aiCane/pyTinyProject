# 对一个字符串，对它进行冒泡排序使其为升序，
# 例如：对于lan，排序成aln需要交换一次（只能交换相邻的两个字母），对于qiao，排序成 aioq 就需要交换4次。
# 请找出冒泡排序时恰好需要交换100次的字符串，
# 如果有多个字符串满足条件，则找出最短的那个，
# 如果有多个满足条件而且还是最短的，则找出字典序最小的那个。

dic = {}

for i in range(1, 20):
    dic[str(i)] = int(i * (i - 1) / 2)

# print(sth["4"])
# print(sth["15"])

# print("onmlkjihgfidcba")
print("jonmlkihgfidcba")


# 参考验证代码：
# def bubble_sort(arr):
#     num = 0
#     for i in range(len(arr)-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 num += 1
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return num
#
#
# print(bubble_sort(list('jonmlkihgfedcba')))
