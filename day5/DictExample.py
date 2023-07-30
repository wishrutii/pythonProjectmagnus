d1 = {101:'abc',102:'bcd',103:'cde'} # Dictionary also uses these curly brackets like set but here we are defining each
# key with a value inside the brackets so that's why it will take it as a type Dict.
print(type(d1))
print(d1[101]) # 101 is the key, and typing this will give the value of 101.
d1[104]='efg' # this is to replace the value of the key. 104 is not in the brackets but we can insert it.
d1[102]='xyz' # this will replace the value of the key 102.
print(d1)
d1.pop(103) # this will remove the value of 103 just like how it is in list.
print(d1)
