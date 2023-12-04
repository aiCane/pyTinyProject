# 小明坚持每天跑步，正常情况下每天跑一公里，
# 如果这一天是周一或者月初（每月的一号），那么小明就会跑两公里
# （如果这一天既是周一，又是月初，小明也是跑两公里），
# 小明从2000年1月1日（周六）一直坚持到了2020年10月1日（周四），
# 请你计算一下小明共跑了多少公里？

from datetime import *
start = date(2000, 1, 1)
end = date(2020, 10, 2)
tmp = timedelta(days=1)
ans = 0
while start != end:
    if start.weekday() == 0 or start.day == 1:
        ans += 2
    else:
        ans += 1
    start = start + tmp
print(ans)
