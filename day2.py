name = "Vasu Patel"
age = 26
height = "5'10"
is_student = True

print (name)
print (age)
print (height)
print (is_student)
print(type(name))
print(type(age))
print(type(height))
#type() is used to describe the type of input this field takes or has

greeting = "Hello " + name
print(greeting)

print(f"My name is {name} and I am {age} years old")
#f-string used, the most common ways to create strings in python

#Building a calculator
#input() requires you to input a value in the terminal or wherever when the code is ran, so it will give the details inside it like a statement
#float() turns all intergers into decimals so you can do math with it and add decimal points
#Add space after the input fields so that it looks neat or you can even add a = 
num1 = float(input("Enter your first number = ")) 
num2 = float(input("Enter your second number = "))

print(num1 + num2)
print(num1 - num2)
print(num1/num2)
print(num1*num2)
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")