#if
#elif
#else
#nested if else

#loop
#for
#while
#nested loop

#if statement: to check the condition and execute the statement
#if condition:
#   statement
#else
#   statement

#EXAMPLE:
# x=10
# if x>20:
#     print("x is greater than 20")
# else:
#     print("x is less than 20")

# x=10
# y=30
# z=5
# if x<y:
#     print("x is less than y")
# else z<y:
#     print("z is greater than y")

#EXAMPLE:
# nepali=int(input("Enter your marks: "))
# english=int(input("Enter your marks: "))
# maths=int(input("Enter your marks: "))
# science=int(input("Enter your marks: "))
# social=int(input("Enter your marks: "))
# total=nepali+english+maths+science+social
# print(f"add; {total}")
# percentage=total/5
# print(f"division; {percentage}")
#
# if percentage>=80:
#     print("Distinction,Excellent")
# elif percentage<80 and percentage>=60:
#     print("First division,Very good")
# elif percentage<60 and percentage>=50:
#     print("Second division,Good")
# elif percentage<50 and percentage>=40:
#     print("Third division,Not good enough")
# else:
#     print("Fail")

#EXAMPLE:
# nepali=int(input("Enter your marks: "))
# english=int(input("Enter your marks: "))
# maths=int(input("Enter your marks: "))
# science=int(input("Enter your marks: "))
# social=int(input("Enter your marks: "))
# total=nepali+english+maths+science+social
# print(f"add; {total}")
# per=total/5
# print(f"division; {per}")
#
# if per>=80:
#     print("Distinction")
# elif per<80 and per>=70:
#     print("First division")
# elif per<70 and per>=60:
#     print("Second division")
# elif per<60 and per>=50:
#     print("Third division")
# elif per<50 and per>=0:
#     print("Fail")

#HOMEWORK:
#1QUESTION(COMPUTER BAZAR):
#dell=20000, toshiba=30000, mac=50000
#giving options and making them select
#give them delivery option
#give them packaging option
# choice= int(input('Enter a number:'))
# if choice==1:
#     print('Dell')
#     price=20000
# elif choice==2:
#     print('Toshiba')
#     price=30000
# elif choice==3:
#     print('Mac')
#     price=50000
#
# qty=int(input('Enter the number of quantity:'))
#
# delivery= int(input('Enter the option(1-2)'))
# if delivery==1:
#     print('Home')
#     price=1000
# elif delivery==2:
#     print('Pickup')
#     price=0
#
#
# pkg=int(input('Enter the option(1-3)'))
# if pkg==1:
#     print('Plastic')
#     pkg_price=500
# elif pkg==2:
#     print('Bag')
#     pkg_price=1000
# elif pkg==3:
#     print('Gift Box')
#     pkg_price=5000
#
#
# location=(input('Enter location:'))
# if location=='Kathmandu':
#     price=price+price*0.13
# elif location=='Lalitpur':
#     price=0
# elif location=='Bhaktapur':
#     price=0
#
# print(price*qty + pkg_price )
#[PROPER ANSWER IN HOMEWORK.PY]