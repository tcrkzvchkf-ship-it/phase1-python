def greet(): # "def" or definition defines the function, so in this case greet is the function or name and the code that you indent into it is what runs when you call the definition ex# greet()
    print("Hello, welcome!")

greet()
greet()
greet()
# You can call this function as many times as you want, its like creating a dictionary!


#name is a prameter so whevnever you call it, and give a name to the call inside the brackets it is what it will call out
def greet_person(name, greeting= "Hello"):
    print(f"{greeting} {name}!")

greet_person("Vasu")
greet_person("Vasu", "Good morning")


def add(num1, num2):
    return num1 + num2
#"return" sends the value back to wherever the function was called from. This is the difference between a function that just prints something and one that actually produces a value you can use.

result = add(5, 3)
print(result)
print(add(10, 20))



#Challenge Day 4


# Square of a number in a definition
def square(n):
    return n * n

print (square(30))


#Check if a number is even or odd with a true or false statement
def is_even(n):
    return True if n % 2 == 0 else False

print(is_even(5))
#you can write the above code like this as well:
def is_even(n):
    return n % 2 == 0 

print(is_even(5))


# C/F degrees

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print(celsius_to_fahrenheit(0))


#count vowels

def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0 # We set this up when we want to count something for a loop
    for letter in word:
        if letter in vowels:
            count += 1 # this is increase the count if it matches the for loop and the if statement within the loop
    return count

print(f"How many vowels in your word {count_vowels('python')}")

#max three

def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(20,9,5))
    

