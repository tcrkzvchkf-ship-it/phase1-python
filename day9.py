# Classes and OOP

# What is a class:
# so far all the functions and variables have been floating loose. A class lets you bundle related data and functions
# together into one near package called an object

class Dog: # This is the blueprint. Everything indented inside it belongs to the Dog class.
    def __init__(self, name, breed, age):
        # This is the constructor — it runs automatically every time you create a new Dog. 
        # When you wrote Dog("Rex", "Labrador", 3) 
        # Python immediately called __init__ with those three values.
        self.name = name
        self.breed = breed
        self.age = age
        #This is how the object refers to itself. When you write self.name = name you're saying 
        # "store this name on this specific object."
        # That's why dog1.name is "Rex" and dog2.name is "Bella" — they're separate objects with separate data.
        # Think of self like saying "my" — self.name means "my name", self.breed means "my breed."

    def bark(self): # This is a method
        #A function inside a class is called a method. It always takes self as the first parameter so it knows 
        # which object is calling it. When you write dog1.bark() Python automatically passes dog1 as self
        print(f"{self.name} says woof!")
    
    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")
    
    def describe(self):
        print(f"{self.name} is a {self.breed} aged {self.age}")


dog1 = Dog("rex", "labrador", 3)
dog2 = Dog("bella", "poodle", 5)

dog1.bark()
dog2.bark()
dog2.describe()
dog1.birthday()
dog1.describe()



class TodoList: # This is the blueprint for what the todo list is gonna work like
    def __init__(self): 
        # so this def is using the __initi__ method where it will be called everytime you call TodoList
        self.tasks = [] 
        #this is just calling the tasks!

    def add_task(self, task_name): 
        # Here I am creating a new function where we are adding tasks with self and tasK_name as the parameters
    
        self.tasks.append({"task": task_name, "done": False})

        # this is appending or adding the tasks in this specific format

    def view_tasks(self):
        if len(self.tasks) == 0: #this will count the amount of takss you have
            print("No tasks yet!")
        for index, task in enumerate(self.tasks):
            if task["done"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{index + 1}. {task['task']} - {status}")

    def complete_task(self, index):
        self.tasks [index - 1]["done"] = True

    def delete_task(self, index):
        self.tasks.pop(index- 1)

    def task_count(self):
       return len(self.tasks)
    

todo = TodoList()
todo.add_task("Buy groceries")
todo.add_task("Call piyu")
todo.add_task("Call mom")
todo.view_tasks()
todo.complete_task(1)
todo.view_tasks()
todo.delete_task(2)
todo.view_tasks()
todo.view_tasks()
print(f"Total tasks: {todo.task_count()}")

    

