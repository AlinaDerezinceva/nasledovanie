class Employee(Person):

    def work(self):
        print(f"{self.name} работает")


p1 = Employee("Алиса")
print(p1.name)
p1.display_info()
p1.work()