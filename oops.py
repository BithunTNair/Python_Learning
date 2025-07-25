class MySampleClass:
    def hello(self,name):
        self.name=name
        print('Hello '+ name);
    def print_name(self):
        print(self.name)
x= MySampleClass();
name='Bithun'
x.hello(name);
x.print_name();

class Sample:
    def __init__(self):
        print('Hello');

a=Sample();
b= Sample();
      
class Students:
    year=2025
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def increment_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1  
Bithun= Students('Bithun',24,'trivandrum');
Anu= Students('Anu',25,'Kollam');
Bithun.increment_age();
Anu.relocate('Palakkad')
print(Anu.place);

print(Students.year);
Students.add_year();
print(Students.year);
