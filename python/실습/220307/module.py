class Fridge:
    def __init__(self):
        self.Open = False
        self.foods = []

    def open(self): # 1번, 냉장고 문을 연다.
        self.Open = True
        print ('냉장고 문을 열었어요')

    def put(self, thing):# 2번, 코끼리를 넣는다.
        if self.Open:
            self.foods.append(thing)
            print ('냉장고 속에 음식이 들어갔네')
        else:
            print('냉장고 문이 닫혀있어서 못넣겠어요')

    def close(self):# 3번, 냉장고 문을 닫는다. ^^;
        self.Open = False
        print("냉장고 문을 닫았어요")

class Food:
    pass