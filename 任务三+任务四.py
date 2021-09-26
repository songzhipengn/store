#
# #任务三
# #有下列人员数据库，请按要求实现
# # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
#



import math

names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
# #1.统计每个人的平均薪资

a = []
for b in names:
    a.append(b[0])
c = set(a)

for b in c:
    i = 0
    sum = 0
    for d in names:
        if d[0] == b:
            i += 1
            sum += d[5]
            print(f'{b}的平均工资为{sum / i}')

# #2、统计每个人的平均年龄
a = []
for b in names:
    a.append(b[0])
c = set(a)
for b in c:
    i = 0
    sum = 0
    for d in names:
        if d[0] == b:
            i += 1
            sum += int(d[1])
            print(f'{b}的平均年龄为{sum / i}')

# #3、公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.append(["刘备","45","男","220","ailibaba","500","30"])
print(names)

#4、统计公司男女人数
a = []
for b in names:
    a.append(b[4])
c = set(a)
for b in c:
    nan = 0
    nv = 0
    for d in names:
        if d[4] == b:
            if d[2] == "男":
                nan += 1
            elif d[2] == "女":
                nv += 1

    print(f"{b}公司有{nan}个男人，女性有{nv}个女人")

# #5、每个部门的人数
a = []
for b in names:
    a.append(b[6])
c = set(a)
for b in c:
    i = 0
    sum = 0
    for d in names:
        if d[6] == b:
            i += 1
    print(f'{b}部门有{i}人')

# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？
grade = [
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]
for b in grade:
    sum = 0
    for a in b:
        if isinstance(a,int):
            sum += a
    print(f"{b[0]}的总成绩为{sum}")


# 请对下列列表进行冒泡排序（网易测试开发笔试题）
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
def mp(b):
    i = 0
    while i < len(b) - 1:
        j = 0
        while j < len(b) - 1 - i:
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
            j += 1
        i += 1

mp(a)
print(a)

#任务四
#dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for i in dict.keys():
    print(i)

# #2、请循环遍历出所有的value
for j in dict.values():
    print(j)

 # 3、请在字典中增加一个键值对,"k4":"v4"
dict['k4'] = 'v4'
print(dict)

# 小明去超市购买水果，账单如下
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典
# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }
# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
# Friuts = {
# 	‘苹果’：12.3，  # 水果和单价
# 	‘草莓’：4.5，
#        ‘香蕉’：6.3，
#        ‘葡萄’：5.8，
#        ‘橘子’：6.4，
#        ‘樱桃’：15.8
# }
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money': ??
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': ??
#     }
# }
fruits = {
    '苹果': 32.8,
    '香蕉': 22,
    '葡萄': 15.5,
    '草莓': 4.5,
    '橘子': 6.4,
    '樱桃': 15.8
}
info = {
    '小明': {
        'fruits': {
            '苹果': 4,
            '草莓': 13,
            '香蕉': 10,
        }
    },
    '小刚': {
        'fruits': {
            '葡萄': 19,
            '橘子': 12,
            '樱桃': 30,
        }
    },
}
for k, v in info.items():
    money = 0
    for k2, v2 in v.items():
        for k3, v3 in v2.items():
            for k4, v4 in fruits.items():
                if k3 == k4:
                    money += v3 * v4
    print(f"{k}花了{money}元")
    info[k]['money'] = money
print(info)


#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
count = [10,21,56,10,21,56,56,56,56,21,56,56,56,10,56]

def counts(count):
    result = {}
    a = set(count)
    print(a)
    for value in a:
        m = 0
        for n in count:
            if value == n:
                m += 1
        result[value] = m
    return result
j = counts(count)
print(j)

# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
Classify = ['姓名', '年龄', '性别', '编号', '任职公司', '薪资', '部门编号']
a = {}
for i in names:
    a[i[0]] = {}
    for j in i:
        if i.index(j) == 0:
            continue
        for k in Classify:
            if Classify.index(k) == 0:
                continue
            elif i.index(j) == Classify.index(k):
                a[i[0]][k] = j
print(a)














