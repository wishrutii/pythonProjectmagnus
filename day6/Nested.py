# a = int(input("enter the value of a:")) so if we only write input it will quite literally add the two values for eg: 1+1 = 11
# b = int(input("enter the value of b:")) but the int (integer) will make it add the values like in math.
# print(a+b)
user = input("enter the username:")
password = input("enter the password:")

if user=='python':
    if password=='welcome':
        print("login success")
    else:
        print("invalid password")
else:
    print("invalid username")


