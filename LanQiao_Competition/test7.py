# 原问题：在给定的字符串中，计算出现次数最多的字母和它的出现次数，如果出现次数最多的字母同时有多个，则找出字典序最小的。
# 输入格式：一行，代表所要统计的字符串。
# 输出格式：两行，第一行一个字符，是出现最多的字母，第二行一个整数，该字母的出现次数。

string = input("string: ")
maximum = -1
ans = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
       "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

for i in ans:
    num = string.count(i)
    if num >= maximum:
        maximum = num
        ans[i] = num

ans_char = sorted(ans.items(), key=lambda x: x[1], reverse=True)
print(ans_char[0][0])
print(ans_char[0][1])

# for i in ans:
#     if ans[i] == maximum:
#         sth.append(i)
# print(sth[0])
# print(maximum)

# 参考代码
# cnt = [0]*26
# s = input()
# for alpha in s:
#     cnt[ord(alpha) - ord('a')] += 1
# k = 0
# for i in range(26):
#     if cnt[i] > cnt[k]:
#         k = i
# print(chr(k+ord('a')))
# print(cnt[k])
