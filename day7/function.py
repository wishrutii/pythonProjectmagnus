#a=10
#b=20
#print(a+b)
#print(a*b)
#print(a/b) This code will give us the output individually in the order of print.
# to create a new function we write "def"
def add():
    a=10
    b=20
    print(a+b)

add() # we have to get out of the function indent and write "add()" then only the output will be executed.
    # in other words we have to call the function

def sub():
    a=20
    b=5
    print(a-b)

def multi():
    a=10
    b=30
    print(a*b)

def div():
    a=50
    b=5
    print(a/b)

multi()  # this is calling the function, we don't have to call all functions we can call any function that we want an output for like this.
sub()
