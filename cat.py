from python_oop.animal import Animal
class Cat( Animal):
    def __init__(self,hair="bingle"):
        self.name = "Tom"
        self.color = "blue"
        self.age = "20"
        self.sex = "male"
        self.hair = hair

    def grap(self):
        print("他会抓老鼠")

    def cry(self):
        print("也会喵喵叫")

if __name__ == '__main__':
    tom = Cat()
    print(f"有一只小猫叫{tom.name}，他的颜色是{tom.color},他的年龄是{tom.age},他的性别是{tom.sex},他的毛是{tom.hair}")
    tom.grap()
    tom.cry()