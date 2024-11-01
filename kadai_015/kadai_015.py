class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printinfo(self) -> None:
        print(f"name: {self.name} age: {self.age}")


human = Human("Hiro", 33)
human.printinfo()
