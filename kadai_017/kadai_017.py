class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print('大人である')
        else:
            print('大人ではない')


humans: list[Human] = []

humans.append(Human('Tanaka', 10))
humans.append(Human('Yamada', 20))
humans.append(Human('Hamada', 30))

for human in humans:
    human.check_adult()
