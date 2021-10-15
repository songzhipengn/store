from threading import Thread

import time

import threading

a = threading.RLock()

Humburger = 500


class programmer(Thread):
    username = ""
    count = 0

    def run(self) -> None:

        global Humburger  # 使用全局变量
        while 1:  # 死循环
            if Humburger < 498:
                a.acquire()  # 锁上
                self.count = self.count + 1
                Humburger = Humburger + 1
                print("我告诉你们就剩", Humburger, "汉堡包，快卖没了~快抢啊，先到先得啊")
                # time.sleep(0.01)
                a.release()
            elif Humburger > 500:
                time.sleep(3)
                break
        print("目前货很紧，只有", Humburger, "个汉堡包！快抢啊你们》》")


class xiaofei(Thread):
    username = ""
    money = 100
    count = 0

    def run(self) -> None:
        global Humburger
        while 1:  # 死循环
            if self.money > 0 and Humburger > 0:
                a.acquire()
                self.count = self.count + 1
                self.money = self.money - 5
                Humburger = Humburger - 1
                print(self.username, "已经买了", self.count, "个汉堡包！", "就只有", self.money,"块钱了")
                # time.sleep(0.01)
                a.release()
            elif self.money == 0:
                a.acquire()
                print("木有钱啦，败光了")
                print(self.username, "已经买了", self.count, "个汉堡包！")
                a.release()
                break
            elif Humburger == 0:
                time.sleep(2)


p = programmer()
p.username = "小红"
p1 = programmer()
p1.username = "小妹妹"

p2 = programmer()
p2.username = "小美女"

p3 = xiaofei()
p3.username = "大美女"

p4 = xiaofei()
p4.username = "小姐姐"

p5 = xiaofei()
p5.username = "大姐姐"

p6 = xiaofei()
p6.username = "大胡子"

p7 = xiaofei()
p7.username = "小刀子"

p8 = xiaofei()
p8.username = "三驴子"

p.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p8.run()
