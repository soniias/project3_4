class Animals:
    def __init__(self, name, swim, fly, roar, walk):
        self.name = name
        self.swims = swim
        self.flies = fly
        self.roars = roar
        self.walks = walk

    def swim(self):
        if self.swims:
            return f"{self.name} вміє плавати"
        else:
            return f"{self.name} не вміє плавати"

    def fly(self):
        if self.flies:
            return f"{self.name} вміє літати"
        else:
            return f"{self.name} не вміє літати"

    def roar(self):
        if self.roars:
            return f"{self.name} вміє ричати"
        else:
            return f"{self.name} не вміє ричати"

    def walk(self):
        if self.walks:
            return f"{self.name} вміє ходити"
        else:
            return f"{self.name} не вміє ходити"

monkey = Animals("Мавпа", swim=True, fly=False, roar=False, walk=True)
bear = Animals("Ведмідь", swim=True, fly=False, roar=True, walk=True)
bird = Animals("Пташка", swim=True, fly=True, roar=False, walk=True)
zebra = Animals("Зебра", swim=False, fly=False, roar=False, walk=True)

print(monkey.fly())
print(bear.swim())
print(bird.roar())
print(zebra.walk())


import random
class Cars:
    def __init__(self, car, color, age, quality):
        self.car = car
        self.color = color
        self.age = age
        self.quality = quality

    def driving(self):
        state = random.randint(1, 2)
        if state == 1:
            return (f"{self.car} їде")
        elif state == 2:
            return (f"{self.car} зупинилась")

    # def breaking(self):
    #         return (f"{self.color}{self.car} зламався через те, що він {self.age}")

cars = Cars("Маршрутка", "Жовтра", "стара", "не дуже хороша")
lorry = Cars("Вантажівка", "Красна", "нова", "хороша")

print(cars.driving())
print(lorry.driving())
