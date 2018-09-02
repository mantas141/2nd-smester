#!/usr/local/bin/python

class Person:
    def __init__(self, name, job=None, pay=0):
       self.name = name
       self.job = job
       self.pay = pay
    def giveRaise(self, percent):
       self.pay = int(self.pay * (1 + percent))
    def payTaxes(self, taxperc):
        self.pay = int(self.pay - (self.pay * taxperc))
    def __repr__(self):
       return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10): # Redefine at this level
        Person.giveRaise(self, percent + bonus) # Call Person's version

#run the test statements at the bottom only when the file is run for testing, not when the
#file is imported.
if __name__ == '__main__': # When run for testing only
     # self-test code
     bob = Person('Bob Smith', job='dev', pay=50000)
     sue = Person('Sue Jones', job='dev', pay=100000)
     print(bob.name, bob.pay)
     print(sue.name, sue.pay)
     tom = Manager('Tom Jones', 'mgr', 50000) 
     print(tom.name, tom.pay)

     print('--All three--')
     for obj in (bob, sue, tom): # Process objects generically
         obj.giveRaise(0) # Run this object's giveRaise
         obj.payTaxes(0.1)
         print(obj) # Run the common __repr__  

