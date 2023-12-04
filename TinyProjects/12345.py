# coding=utf-8
import random
import turtle

n = "臭老爸 "
m = "打"
random.seed()
xyz = random.randint(1, 100)


def Game1():
    guess = int(input("我有一个数字，来来来，猜中了有奖励。"))
    if guess == 1:
        print('啥？这么好猜吗？')
        print("没门儿，还想要奖励？走远了！")
    else:
        print("哈哈哈，现在的人都那么低下吗？这都猜不中！")
    print("游戏结束了，哈哈哈！")
    if guess != 1:
        abc = input("你想不想知道这是什么数字？")
        if abc == "想":
            print("其实就是 1 啦。")
        if abc == "不想":
            print("不知道活该！")
        else:
            print("你说啥？")


def Game2():
    try:
        times = 0
        thinking1 = input("我有一个游戏，你想不想玩？\n（回答'想'或者'不想'）:")
        if thinking1 == "想":
            print("好呀。好呀\n"
                  "这是一个猜数字的游戏\n"
                  "我有一个1至100的数字，你需要要猜它是几。放心，有很多次猜的机会呢！\n"
                  "不用担心～猜中了我会恭喜你的，如果错了的话我可以提醒你哟\n"
                  "(请输入数字)\n"
                  "开始吧:")
            while True:
                dad = int(input(""))
                times += 1;
                if dad < xyz:
                    print("小啦 小啦\n继续吧：")
                if dad > xyz:
                    print("大啦 大啦\n继续吧：")
                if abs(dad - xyz) < 5 and dad != xyz:
                    print("不过，已经很接近了哟～")
                if dad == xyz:
                    print("恭喜你，太棒了！")
                    print("猜了", times, "次")
                    break
                    # print("干啥呢？")
        if thinking1 == "不想":
            print("小学生钓鱼，愿者上钩～")
        # if thinking1 != "想" and thinking1 != "不想":
        if thinking1 not in ['想', '不想']:
            print("说什么鬼话")
    except:
        print("输入错误，游戏结束!")


def Game3():
    game = random.randint(50, 75)
    thinking2 = input("玩了那么久猜数字，你想不想玩拿珠子？（回答'想'或者'不想'）\n(至少两个人才能玩的哦。）")
    if thinking2 == "想":
        print("这儿还有一个游戏：拿珠子")
        print("这里有50到75个随机的珠子，前面的珠子是黑的，最后一个是白的。")
        print("每次能够拿1、2、3、4个珠子，谁先拿到白的珠子，谁就赢了。")
        print("现在有", game, "个珠子。")
        while True:
            takes = int(input("下一个"))
            if takes == 1 and game >= 1:
                game -= 1
            elif takes == 2 and game >= 2:
                game -= 2
            elif takes == 3 and game >= 3:
                game -= 3
            elif takes == 4 and game >= 4:
                game -= 4
            else:
                print("你干啥呢？重新输入！")
                print("只能输入数字1，2，4或者8哦～")
            if game == 0:
                print("You win.")
                break;
            print("还剩", game, "个。")
    if thinking2 != "想":
        print("那就精彩了")


def Game4():
    Alliance = [1, 1.1]
    list1 = ["屁妈", "老爸", "小亮"]
    print(Alliance)
    print(list1 in Alliance)
    print("小亮" in Alliance)
    if "屁妈" in list1:
        print('''"屁妈"是真的皮''')


def Game5():
    print("来吧，来个恶作剧。")
    thinking3 = input("会'死机'的游戏你来不来？")
    if thinking3 == "来":
        def harry(person):
            print("Goodbye" + person)
            print("")
            return Harry(person)

        def Harry(person):
            print("Hello " + person)
            return harry(person)

        harry("dad")


def Game6():
    def lalalalala():
        Answer2 = input("How many vowels are there?")
        if Answer2 == "There is one vowel." or "There are two vowels.":
            Answer3 = input("Is it short or long?")
            if Answer3 == "It is short?" or "It is long?":
                Answer4 = input("Say it.")
                Answer5 = input("Say the whole word.")
                if Answer4 == Answer5:
                    print("Good job.")
    print("(下面这个小程序有些问题，需要对问题完整的回答，任何一个方面都不能错~~)")
    print("                                                  :   :     ")
    print("                                         :   :   :          ")
    print("                                :   :   :                   ")
    print("                       :   :   :                            ")
    print("              :   :   :                                     ")
    print("     :   :   :                                              ")
    print(":   :                                                       ")
    thinking4 = input("你会英语吗？我这里有一个单词速成大法给你，要不要？")
    if thinking4 == "要":
        print("")
        Answer = input("Is there a dadada?")
        if Answer == "Yes,there is a dadada.":
            Answer1 = input("How many dadadas are there?")
            if Answer1 == "There is one dadada." or "There are two dadadas." or "There are three dadadas." or "There are fore dadadas." or "There are five dadadas.":
                lalalalala()
        if Answer == "No,there is not a dadada.":
            print("Sure.")
            lalalalala()
    elif thinking4 == "不要":
        print("这么好的东西不要，可惜可惜...")
    else:
        print("你在说什么？我听不懂。")


def Game7():
    turtle.left(90)     # 头
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(50)
    turtle.right(90)    # 手
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(70)
    turtle.forward(-140)
    turtle.forward(70)
    turtle.left(90)     # 腿
    turtle.forward(70)
    turtle.right(30)    # 左腿
    turtle.forward(80)
    turtle.forward(-80)
    turtle.left(60)     # 右腿
    turtle.forward(80)
    turtle.forward(-80)
    turtle.right(-150)
    turtle.forward(105)
    turtle.penup()
    while True:
        turtle.circle(0)


def Game8():
    list1 = []
    list2 = []
    print('给我几个数，我可以分辨哪些是奇数，哪些是偶数\n(当然，不要太多了，我会吃不消的)')
    while True:
        num1 = eval(input('现在，告诉我你的第一个数字吧:'))
        if num1 >= 10000:
            print('数字太大了，我处理不了这么大的数字')
            continue
        elif num1%2 != 0:
            list1.append(num1)
            break
        else:
            list2.append(num1)
            break
    while True:
        answer = input('你还有更多的数吗?\n(回答\'有\'或者\'没有\')')
        if answer == '有':
            number = eval(input('下一个是什么:'))
            while True:                                            # 此处有些问题，需改正
                if number >= 10000:
                    print('数字太大了，我处理不了这么大的数字')
                    continue
                elif number%2 != 0:
                    list1.append(number)
                    break
                else:
                    list2.append(number)
                    break
        elif answer == '没有':
            print('奇数有——' , list1)
            print('偶数有——' , list2)
            break



# Game1()
# Game2()
# Game3()
# Game4()
# Game5()
# Game6(）
# Game7()
Game8()