# 问题：给定 n 个学生的成绩，大于等于60的为及格，大于等于85的为优秀。请你统计这 n 名同学的及格率和优秀率。
# 输入格式：第一行一个数n，表示接下来有n行数据，接下来n行每行一个数m，代表该学生的成绩。
# 输出格式：两行，第一行一个数表示及格率，第二行一个数表示优秀率，都要求四舍五入。

n = int(input("n: "))
passed = 0
excellent = 0

for i in range(n):
    score = int(input("score" + str(i + 1) + ": "))
    if score >= 60:
        passed += 1
    if score >= 85:
        excellent += 1

print("passed:", round(passed / n * 100), "%")
print("excellent:", round(excellent / n * 100), "%")

# 参考代码和我的差不多
