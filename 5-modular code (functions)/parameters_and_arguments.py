# this is the third lesson on chapter 5
# this lesson about parameters and arguments

def wash_car(amount_paid): # the variable into (here) is called parameter
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")
    
    if(amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(12) # after we calling a function we write the value of the variable we wrote and this value is called argument

# so we can say the parameter is a variable, and argument is the value of this variable