#types of loop:[for loop, while loop, nested loop]
#for loop;It is used to literate over a sequence (list, tuple, string) or other literable
#while loop;It is used to literate over a block of code as long as the test expression
#1example:
# x=1
# while x<=10:
#     print('Purnima',end=" ")   [end=""{to keep the loop in one line}]
#     x +=1  [to run the loop]

#2example:
# x=1
# while x<=10:
#     if x % 2 == 0:
#      print("Even numbers")
#     else:
#      print("Odd numbers")
#     x += 1
#AND:
# x=1
# total_even=0
# total_odd=0
# while x<=10:
#     if x%2 ==0:
#         total_even += 1
#         print(f"total even number is: {total_even}")
#     else:
#         total_odd += 1
#         print(f"total odd number is: {total_odd}")
#     x +=1

#TO CHECK IF THE ENTERED NUMBER IS ODD OR EVEN IN LOOP:
x=1
num=int(input("Enter a number: "))
while x<=10:
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num}is an odd number")
        x +=1

#TO ADD THE NUMBERS:
