# Exploring Conditional Code

'''
If Condition
    - it starts with word if, and it checks some condition, and if that condition is true, 
        then it will do the work that you have placed inside of it
        
        if condition:
            block of code to execute if the condition is true
'''

print("Hi")

name = input("what's your name? ")
print("it's nice to meet you, ", name)

answer = input("Are you enjoying the course? ")

if answer == "Yes":
    print("that's good to hear!")
    
print("final statement")