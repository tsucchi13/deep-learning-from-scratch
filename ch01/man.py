class Man:
    def __init__(self, name, age):
        #生成されたインスタンスのインスタンス変数self.nameに引数nameを代入してる（生成された瞬間に）
        self.name = name
        self.age = age
        print("Initialized!（インスタンス生成されたから，コンストラクタ発動！）")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

    def showage(self):
        print(self.name + "は" + str(self.age) + "歳です")


m = Man("taro", 3)
m.hello()
m.goodbye()
m.showage()
