class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self,abc):
    print("Hello my name is " + abc.name)

p1 = Person("uday",25)
p1.myfunc(p1)