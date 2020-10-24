# 需求：生成电话号码
# 流程：中国电信号段
#        中国移动号段
#        中国联通号段
# 11位
# 第一位 1
# 第二位 3，4，5，7，8
# 第三位 根据第二位确定
# 后八位随机数字
# 分析需求，先找已知的条件，确定出不变规律和变化规律


import random


# 生成电话号码
def creat_phone():
    # 第二位
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位的值根据第二位来确定
    # 数组条件依赖可以用字典来产生对应关系进而取值
    # 例外可以看成条件肯定否定，用if语句
    # 产生一个有复杂条件的字符串需要分类分区
    # 依照条件产生后字符串拼接并以format进行格式条件链接
    # 问题和知识点联系练习
    # 程序自上向下执行
    # 注意缩进

    third = {3: random.randint(0, 9),
             4: [5, 7, 9][random.randint(0, 2)],
             5: [i for i in range(10) if i != 4][random.randint(0, 8)],
             # 列表生成，然后选取一个
             7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
             8: random.randint(0, 9)
             }[second]
    # 后八位随机抽取
    suffix = ""
    for x in range(8):
        suffix = suffix + str(random.randint(0, 9))

    # 0,1,2,,3,4
    # 拼接
    return "1{}{}{}".format(second, third, suffix)


# 调用

num = input("请输入生成的数量")
for index in range(0, int(num)):
    print(creat_phone())