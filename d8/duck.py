class Duck:
    def quack(self):
        print("quack")
        
class Person:
    def quack(self):
        print("not quack")
        
def make_it_quack(thing):
    thing.quack()
    
make_it_quack(Duck())
make_it_quack(Person())