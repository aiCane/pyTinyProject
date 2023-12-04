# 从1到2020中这些数字中有多少个2（注意：不是问多少个数字里有2）

ans = 0
for i in range(1, 2021):
    ans += str(i).count("2")
print(ans)
