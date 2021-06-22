# 一个随机漫步的类
from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self, num=5000):
        self.num = num
        # 生成随机数的数量，默认为5000
        self.x_value = [0]
        self.y_value = [0]
        # 起始值为（0.0）

    def point_walk(self):
        while len(self.x_value) < self.num:
            x_direction = choice([1, -1])
            x_disatance = choice([0, 1, 2, 3, 4])
            x_change = x_disatance*x_direction
            y_direction = choice([1, -1])
            y_disatance = choice([0, 1, 2, 3, 4])
            y_change = y_disatance * y_direction
            if(x_change == y_change == 0):
                continue
                # 不允许不改变
            else:
                self.x_value.append((self.x_value[-1] + x_change))
                self.y_value.append((self.y_value[-1] + y_change))


if __name__ == "__main__":
    ran = RandomWalk()
    ran.point_walk()
    number = list(range(ran.num))
    plt.figure(figsize=(10, 6))
    # 设置图片的大小
    plt.scatter(ran.x_value, ran.y_value, c=number, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='red', edgecolors='none', s=20)
    # plt.axes().get_xaxis().set_visible(False)
    # 隐藏x轴
    plt.show()
