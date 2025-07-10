# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def work(self):
        print(f"{self.name} is a team member")

class Manager(Person):
    def manage(self):
        print(f"{self.name} is a manager")


class TeamLead(Employee, Manager):
    pass

lead = TeamLead("Pedro")
lead.work()   
lead.manage() 