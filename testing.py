class Employee:

    def __init__(self, first_name, last_name, pay, age):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.age = age


    def print_full_name(self):
        return self.first_name + " " + self.last_name


    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


employee1 = Employee("Srikar","Karra",500000,18)
print employee1.pay
employee1.apply_raise()
print employee1.pay
