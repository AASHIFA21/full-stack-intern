'''#concatenation
a="love"
b="python"
print(a+b)
#repetition
print("aashifaa "*5)
#indexing
name="python"
print(name[1])
#slicing
name="python"
print(name[0:5])
#length
text="usma"
print(text.upper())
text="USMA"
print(text.lower())
#replace
text="aashifa"
print(text.replace("fa","ka"))
#split
text="orange,banana,watermelon,chaerry"
print(text.split(","))
#join
text=['i','love','shawarma']
print(" ".join(text))
#strip
text="         aashifa        "
print(text.strip())
#operators
#arithmetic operator(+)
a=1000
b=500
print(a+b)
#comparison operator
print(50<20)
print(20>10)
#assignment operator
total=5000
total+=2000
print(total)
#membership oper
values=[1000,500,3000,200]
print(200 in values)
#bitwise
print(1 & 2)
#identity ope
a=2000
b=a
print(a is not b)
a=int(input("value:"))
b=int(input("value:"))
print(a+b)
a=int(input("compar:"))
b=int(input("compar:"))
print(a>b)
a=int(input("num:"))
b=int(input("num:"))
print(a is b)
a=["aashifa","anees","apple","banana","cherry","tomato","onion"]

print("apple" in a)'''
a = ["aashifa", "anees", "apple", "banana", "cherry", "tomato", "onion"]
text = input("Enter item to search: ")
print(text in a)
b =input("phone in (apple/vivo)")
print("vivo" in b)
