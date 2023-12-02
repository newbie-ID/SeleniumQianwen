import askQianWen

# 第一个参数 question:提问的问题
# 第二个参数 isVisible:爬取时是否显示 true代表显示 false代表不显示
print(askQianWen.askQianWen("你好", True))

for i in range(1, 13):
    ques = str(i) + "月有几天？"
    print(ques)
    print(askQianWen.askQianWen(ques, False))
