#!/usr/local/bin/python

class FirstClass: # Define a class object
   def setdata(self, value): # Define class's methods
      self.data = value # self is the instance
   def display(self):
      print(self.data) # self.data: per instance

#The __init__ method is known as the constructor because of when it is run. It’s the
#most commonly used representative of a larger class of methods called operator overloading
#methods, which we’ll discuss in more detail in the chapters that follow. Such
#methods are inherited in class trees as usual and have double underscores at the start
#and end of their names to make them distinct. Python runs them automatically when
#instances that support them appear in the corresponding operations, and they are
#mostly an alternative to using simple method calls. They’re also optional: if omitted,
#the operations are not

x = FirstClass() # Make two instances
y = FirstClass()

x.setdata("King Arthur") # Call methods: self is x
#y.setdata(3.14159) # Runs: FirstClass.setdata(y, 3.14159)

x.display()

class Person:
   def __init__(self, name, jobs, age=None): # class = data + logic
      self.name = name
      self.jobs = jobs
      self.age = age
   def info(self):
      return (self.name, self.jobs) 


rec1 = Person('Bob', ['dev', 'mgr'], 40.5) # Construction calls
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.info()) # Attributes + methods

class PersonTyt:
    def __init__(self, name, job=None, pay=0):
       self.name = name
       self.job = job
       self.pay = pay
    def giveRaise(self, percent):
       self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
       return '[Person: %s, %s]' % (self.name, self.pay)

#run the test statements at the bottom only when the file is run for testing, not when the
#file is imported.
if __name__ == '__main__': # When run for testing only
     # self-test code
     bob = PersonTyt('Bob Smith')
     sue = PersonTyt('Sue Jones', job='dev', pay=100000)
     print(bob.name, bob.pay)
     print(sue.name, sue.pay)

class Manager(PersonTyt):
    def giveRaise(self, percent, bonus=.10): # Redefine at this level
        PersonTyt.giveRaise(self, percent + bonus) # Call Person's version

tom = Manager('Tom Jones', 'mgr', 50000) # Make a Manager: __init__
tom.giveRaise(.10)

print(tom)



class Secretaries(PersonTyt):
    def giveRaise(self, percent, bonus=.15):
        PersonTyt.giveRaise(self, percent + bonus)

barb = Secretaries('Barbara Jones', 'sec', 10000)
barb.giveRaise(0)

print(barb)