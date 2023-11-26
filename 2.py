class Employee:

    def __init__(self, name):
        self.__name = name  

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")

    def work(self):
        print(f"{self.name} работает")