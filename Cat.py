from Animal import Animal


class Cat(Animal):
    # 子类中定义"hair"属性
    def __init__(self):
        self.hair = "短毛"
        super().__init__("露露", "橘色", "2岁", "女")

    # 子类中定义"catch_mouse"方法
    def catch_mouse(self):
        print(f"{self.name}会抓老鼠")

    # 重写父类"animal_bark"方法
    def animal_bark(self):
        print(f"{self.name}饿了会喵喵叫")

    def animal_introduce(self):
        print(f"大家好，我是{self.name}今年{self.age}了是个{self.gender}宝宝长着{self.color}的{self.hair}。")


if __name__ == '__main__':
    # 实例化类
    cat = Cat()
    # 调用"catch_mouse"方法
    # cat.catch_mouse()
    # 调用重写的"animal_bark"方法
    cat.animal_introduce()
    cat.catch_mouse()
    cat.animal_bark()
