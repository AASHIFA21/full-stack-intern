'''age=int(input("enter the num:"))
if age>=18:
    print("eligible")
else:
    print("not")
num=int(input("enter the num:"))
if num>0:
    print("positive")
else:
    print("negative")
num=int(input("enter the num:"))
if num==9:
    print("equal")
else:
    print("not equal")
text=(input("enter the text"))
if text=="apple":
    print("valid")
else:
    print("invalid")
day=(input("enter the text"))
if day=="sunday":
    print("holiday")
else:
    print("working day")

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")
year=int(input("enter the year"))
if (year % 4== 0):
    print("leap year")
else:
    print("not leap year")

age=int(input("enter the num:"))
weight=int(input("enter the weight:"))
if age>=18 and weight>=50:
 print("blood donote")
else:
    print("not donote")
age=int(input("enter the age:"))
if age>=18 and age<=50:
    print("eligible to get voter id")
else:
    print("not eligible to get voter id")
#elif
age=int(input("enter the age:"))
if age >= 5 and age<=15:
    print("ticket price 50")
elif age >=16 and age<=16:
    print(" ticket price 60")
elif age >=18 and age<=19:
    print("ticket price 80")
elif age >=20 and age<=22:
    print("ticket price 100")
else:
    print("not")'''
amount=int(input("enter the amount:"))
if amount >=5000 and amount<10000:
    print("20% discount")
elif amount >=10000 and amount<20000:
    print("50% discount")
elif amount >=20000:
    print("silver coin")
else:
    print("no discount")
