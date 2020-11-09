
class Employee:

    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @first.setter
    def first(self, first):
        self.__first = first

    @last.setter
    def last(self, last):
        self.__last = last

    @first.deleter
    def first(self):
        print('Delete firstname!')
        self.__first = None

    @last.deleter
    def last(self):
        print('Delete lastname!')
        self.__last = None

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.__first, self.__last)

    @property
    def fullname(self):
        return '{} {}'.format(self.__first, self.__last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.__first = first
        self.__last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.__first = None
        self.__last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print("del emp_1.fullname")
del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = "Crazy"
emp_1.last = "Dave"

print(emp_1.fullname)

del emp_1.first

print(emp_1.fullname)

del emp_1.last

print(emp_1.fullname)
