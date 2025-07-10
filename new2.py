class Employee:
    def work(self):
        print("work")
class Manager(Employee):
    def manage(self):
        print("manager")
a=Manager()
a.work()
a.manage()

