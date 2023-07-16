from cat import Cat
from dog import Dog

cat = Cat()
dog = Dog()

dog_hello = dog.hello # Reference an method
dog_hello(cat)

cat.hello(dog)

cat.hello('Joël')

Cat.x()


