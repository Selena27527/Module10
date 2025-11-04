class Animal:
    def speak(self):
        print("hello")
    def display(self):
         print("My name in Frank!")
    def move(self):
        print("running")

class Baby(Animal):
   def crawl(self):
       print("Baby says Dad!")
   def display(self):
        print("The baby is cute!")
   def move(self):
        print("crawl")

class Cow(Animal):
    def speak(self):
        print("Cow says Moo")
    def display(self):
        print("I am black and white!")
    def move(self):
        print("I move slow sometimes!")
    
class Aardvark(Animal):
    def speak(self):
        print("I don't make noise!")
    def display(self):
        print("I am ugly looking to some people!")
    def move(self):
        print("I walk funny")
    
def animal_attributes(a):
    if not isinstance(a, Animal):
        print("Not an Animal")
        return NotImplemented
    a.speak()
    a.move()
    a.display()
    
animal = Animal()
baby = Baby()
cow = Cow()
aardvark = Aardvark()
#person = Person()

animal_attributes(animal)
animal_attributes(baby)
animal_attributes(cow)
animal_attributes(aardvark)
#animal_attributes(person)