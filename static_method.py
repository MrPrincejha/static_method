class Employe:
    no_of_leaves = 8
    # constructor
    def __init__(self,nane,salary,role):
        self.name=nane
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
# alternative class method
    @classmethod
    def from_str(cls, string):

        return cls(*string.split("-"))
# static method
    @staticmethod
    def printgood(strig):
        print("this is good "+strig)


prince = Employe("Prince",20000,"software enginer")
piyush = Employe("piyush",70000,"Hacker")
rohan = Employe.from_str("rohan-200-chutiya")
print(rohan.salary)

prince.printgood("prince")




# ----------Abstraction--------(layers me torna)
# ----------enacpulation-------(implement ko hide karna)