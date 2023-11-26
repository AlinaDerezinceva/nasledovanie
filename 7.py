class WorkingStudent(Employee, Student):
    pass


ws = WorkingStudent("Вася")
ws.work()
ws.study()