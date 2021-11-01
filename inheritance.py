class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and age is " + str(self.age))



# input name age
name= str(input("Name : "))
age= int(input("Age : "))

# call the class
p1 = Person(name , age )
p1.myfunc()