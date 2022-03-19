class Person():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(f'Name is {self.name} id is {self.id}')

    def details(self):
        print('details person')
        print(f'Name is {self.name} id is {self.id}')


class Employee(Person):
    def __init__(self, name, id, salary, role):
        self.name = name
        self.id = id
        self.salary = salary
        self.role = role
        Person.__init__(self, name, id)
    
    def details(self):
        print('Employee Details')
        print(f'Name is {self.name} id is {self.id} sal is {self.salary}')
    
a = Employee('naruto', 1, 1800000, 'Developer')
a.details()
a.display()
b = Person('naruto', 2)
b.details()