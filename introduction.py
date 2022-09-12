# print("Hello")
# print("\'mother's\'") [\ is kept to ignore some signs like {'} in words like mother's]
# print('mother\'s')
# print("\"mother\'s\"")
# print(1234)
# print(-1234)
# print(234.65)
# print("hello","ram","78",sep="-",end="?")
# ["sep"="-" to_seperate]
# print("Hello","Sita",",","how","are","you",end="?")
# ["end"=".,?,!" to_end_the_sentence"]

# name = "Ram"
# age = 18
# address = "Hadigaun"
# phone = 9800000000
# email = "ram12@gmail.com"
# print("My name is",name)
# print("I am",age)
# print("I live in",address)
# print("My phone number is",phone)
# print("My email is",email)

# name=input("Enter your name: ")
# age=input("Enter your age: ")
# address=input("Enter your address: ")
# email=input("Enter your email")
# print("Your name is",name)
# print("Your age is:")

# name='ram'
# age=20
# print("my name is {} age {}".format(name,age))
# print(f"my name is {name} age{age}")

#Dhanu sir
# 9843363725

# data type:
# x=23.4657
# print(f"{x:.2f}")
#
# x=2+3j [complex data type]
# print(x.real)
# print(x.imag)

# num[types:integer, float, complex]
# sum:
# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# print(f"Add: {x+y}")

# difference:
# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# print(f"Subtract: {x-y}")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# phone = input("Enter your number: ")
# address = input("Enter your address: ")
# print("Your name is",name)
# print("Your age is",age)
# print("Your number is",phone)
# print("Your address is",address)

# ctrl+alt+l [for necessary gaps]
# dir:return all the methods and attributes of object
# course='pyhton for beginners'
# print(course)
# print(type(course))
# print(dir(course)) [To see directory]
# print(course.upper()) [For all capital letters]
# print(course.capitalize()) [For Capital letter infront of subject]
# print(course.title()) [For capital letters infront of each word]
# course = '        pyhton for beginners'
# print(course.lstrip())

# user_name='' [for function name]
# userName='' [for variable name]
# myUserName=''
# UserName='' [for class name]

# for notes:
# 1. python.org
# 2. realpyhtontutorials

# data types;[int,float,str]
# boot,list,tuple,set,dict

# Boolean
# data=[12,34,'ram','sita',11.32,0.23]
# print(data[1],data[3])

# list;ordered, mutable, allows duplicate elements
# list is a collection which is ordered and changeable.
# Allows duplicate memebers.
#ctri+z=undo

# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(data[0][0])
# print(data[2][2])

# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12,
#      [13, 45, [67, 89]]]
# ]
# print(data[3][3][1])
# print(data[3])
# print(data[3][3])
# print(data[3][3][2])
# print(data[3][3][2][1])
#print(data[3][3][2][1])

#LIST:
#list, set,tuple,dictionary:

#data = ['ram','sita','nita']
#print(data.pop()) [to remove data given at end by default] [OR]
#data.pop()
#print(data)  [OR]
#print(data.pop(2)) [can be given position to remove data]
# data.append('hari')
# data.append('gita')
# print(data)

# data.insert(1,'shyam')  [to insert data in provided order]
# print(data)

# data.insert(2,'ravi')
#print(len(data)) [to know the length/number of data]
# print(data)
# print(dir(data))

# data=['ram','sita','hari','madan']
# data.remove('sita')
# print(data)

#data=['ram','sita','hari','laxmi']
#data.append(['gita','radha']) [append:to add]
#data.extend(['gita','radha'])  [extend:to remove brackrets]
#print(data.count('sita'))  [to count the number or size of given data in list]
#print(data.index('laxmi'))

# users=[
#     ['sita','gita','laxmi'],
#     ['ram','hari'],
# ]
 #remove laxmi from zero index
 #add shyam to first index

# users[0].remove('laxmi')
# users[1].append('shyam')
# print(users)

#data=['ram','hari','sita','laxmi','anil']
# data.sort()
# data.sort(reverse=False) [to sort data alphabetically]
# data.sort(reverse=True)
# print(data)

#data=['a','A','b','B']
#data.sort() [capital letters come first and then small letters]
#print(data)

# a='a'
# print(ord(a)) [OR]
# print(chr(97))

#users=[
#    ['sita','gita','laxmi'],
#     ['ram','hari'],
# ]
# users[0].remove('laxmi')
# users[1].append('shyam')
# a=users[0]
# b=[]
# b.extend(users[1])
# print(b)

#TUPLE:
#Tuple is immutable, ordered sequence of elements
#Tuple is collection which is ordered and unchangeable.
#Allows duplicate members.

#data=('ram','sita','hari','gita')
#data[0]='hari' ['tuple' object does not support item assignment]
# print(dir(data))
# print(data[2])


#[]=listt,{}=set,()=tuple


#SET:
#set is unordered collection of unique elements
# data={'ram','sita','gita','hari'}
# print(data)

# data={
#     'name':'ram',
#     'age': 20,
#     'address':'kathamndu'
# }
# print(data['name'])

# users=[
#     {'name':'ram','address':'kathamndu'},
#     {'name':'sita','address':'bhaktapur'},
#     {'name':'gita','address':'lalitpur'}
# ]
# print(f"Your name is:{users[0]['name']} and you live in {users[0]['address']}")
#print(f"Your name is:{users[1]['name']} and you live in {users[1]['address']}")
#likewise....

# student = {
#     'name': 'Sophia',
#             'province':{
#                 'province_name':'province 1',
#                 'district':{
#                     'district_name':'Bhojpur'
#                 }
#             }
# }
# print(f"My name is:{student['name']} and I live in{student['province']['province_name']} {student['province']['district']['district_name']}")

# data={
#     'name':'ram',
#     'age':20,
#     'address':'kathamndu'
}
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.get('name'))

#print(data['email'].append('ram12@gmail.com'))
#cannot append directly in dictionary so we should make object and append