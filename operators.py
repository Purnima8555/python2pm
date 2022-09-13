#OPERATORS:
# arithmetic operators
# assignment operators
# comparision operators
# logical operators
# identity operators
# membership operators
# bitwise operators

#ARITHMETIC OPERATORS;+,-,/,*,

#IDENTITY OPERATORS: is, is not
#MEMBERSHIP OPERATORS: in, not in

#identity operators:
# a=10
# b=30
# c=a
# print(a is b)
# print(a is c)
# print(a is not b)
# print(a is not c)
#
# print(id(a))
# print(id(b))
# print(id(c))

#membership operators:
# name='Sophia'
# print('S' in name)
# print('i'not in name)
# print('z'in name)
# print('z' not in name)

# users=['sophia','james','jane','joe']
#check if sophia is in list
#check if ram is not in list
#check if hari is not in list

# print('sophia' in users) {can be given index, for example:print('sophia' in users[0]}
# print('ram' not in users)
# print('hari' not in users)

#BITWISE OPERATORS: [&,|,^,<<,>>,~]
#[to get binary values]
#print(bin(5))  [binary value:101]
# print(bin(6))   [binary value:110]
# print(5&6)
# print(bin(4))   [binary value:100]

# data=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#check if 5 is in the list
#check if 10 is not in the list
#check if 7 is not in the list

# print(5 in  data[1])
# print(10  not in data)
# print(7 not in data[2])

# a, *b=10, 20, 30, 40, 49   [* helps to keep all values in one; for eg,*a or *b]
# print(a)
# print(b)

#EXAMPLE PRACTISE:[1]
#nepali, english, maths, science, social
#total, percentage

# nepali=int(input("Enter your marks: "))
# english=int(input("Enter your marks: "))
# maths=int(input("Enter your marks: "))
# science=int(input("Enter your marks: "))
# social=int(input("Enter your marks: "))
# total=nepali+english+maths+science+social
# print(f"Addition: {total}")
# percentage=total/5
# print(f"Division: {percentage}")

#EXAMPLE[2]
#simple interest: p*t*r [p=1000,t=2,r=5]
# principle=int(input("Enter the value: "))
# time=int(input("Enter the value: "))
# rate=int(input("Enter the value: "))
# simple_interest=principle*time*rate/100
# print(f"Multiplication: {simple_interest}")

# time=int(input("Enter the value: "))
# rate=int(input("Enter the value: "))
# simple_interest=int(input("Enter the value: "))
# principle=100*simple_interest/time*rate
# print(f"pr: {principle}")
