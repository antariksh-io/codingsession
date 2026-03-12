# name = "Python Programming"
# print('z' in name)
# print('S' in name)
# n1 = int(input("Enter n1 value "))
# n2 = int(input("Enter n2 value "))
# n3 = int(input("Enter n3 value "))
# if n1>n2:
#     if n1>n3:
#        print("N1 is greater")
#     else:
#        print("N3 is greater") 
# else:
#     if n2>n3:
#         print("N2 is greater")
#     else:
#         print("n3 is greater")            

# # Minimum number 
# if n1<n2:
#     if n1<n3:
#        print("N1 is smaller")
#     else:
#        print("N3 is smaller") 
# else:
#     if n2<n3:
#         print("N2 is smaller")
#     else:
#         print("n3 is smaller")         

# in is a membership operator in Python
# membership operator = 1. in 2. not in 
# name = "Python Programming"
# print('z' in name)
# print('S' in name)

# for i in range(2,6):
#     print(i)
#     #it automatically increments the value of i by 1 and checks the condition until it reaches 5

# print("Giving increment condition to for loop")

# for i in range(1,10,2):
#     print(i)
#     #it automatically increments the value of i by 2 and checks the condition until it reaches 9    

# for i in range(50, 0 ,-1):
#     print(i)
#     #it automatically decrements the value of i by 1 and checks the condition until it reaches 1    

# for i in range(0,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10," ",)
#     #it automatically increments the value of i by 2 and checks the condition until it reaches 18

# no=int(input("Enter a number "))
# if no>0:
#     print("Number is positive")
# if no<0:
#     print("Number is negative")
# if no==0:
#     print("Number is zero")

# myList=["python","java","c++"]
# # print(myList)
# # print(type(myList))
# # print(myList[0])
# # print(myList[1])    
# # print(myList[2])
# # print(myList[-1])
# # print(myList[2:5])
# # print(myList[:5])
# # print(myList[1:])
# # print(myList[1:8:2])
# # print(myList[::-1])

# # myList.insert(1,"Raut")
# # print(myList)

# newList = myList.copy()
# print(newList)
# print(myList)

# # 2D list
# myList = [["python","Raut"],["8459281934"],[123456789,"SSS"]]
# print("Example of 2D list ")
# print(myList[0][0])
# print(myList[0][1])
# # print(myList[1][1])
# print(myList[1][0])
# print(myList[2][0])
# print(myList[2][1])

# list1 =["python","Raut"]
# print(list1*2)

# list2 = [50,25.50,'python']
# del list2[2]
# #deleting full list del list2
# # list2.clear() clears the list
# print(list2)

# # name = "python"
# # print(name)
# # myname=list(name) #typecasting 
# # print(myname)

# #Sorting exaample
# myList =[35,30,22,11,9,7,4,5,6,3,2,1,88]
# myList.sort()
# print(myList)

# #id function is used to return the address of variable memory address
# math = 50 
# phy = 50 
# print(id(math))
# print(id(phy))  
# eng = 30
# print(id(eng))

# mylist=[45,26,44,2,3,0,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# #check max value 

# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# num3 = int(input("Enter third number"))

# if num1>num2 and num1>num3:
#     print("Maximum numnber is : ", num1)
# if num2>num1 and num2>num3:
#     print("Maximum number is : ",num2)
# if num3>num1 and num3>num2:
#     print("Maximum number is : ",num3)
# else:
#     print("same numbers")

# #Pass or fail example
# phy = int( input("Enter marks of physics : "))
# maths = int(input("Enter marks of maths : "))
# chem = int(input("Enter marks of chemistry : "))

# total = phy + maths + chem
# percentage = total /3.0
# if percentage>=60:
#     print("Result is Passed ", percentage)
# else: 
#     print("Result is failed ",percentage)

# # days of the week

# day = input("Enter day of week: ")
# if day =="Monday" or day =="Tuesday" or day =="Wednesday" or day =="Thursday" or day =="Friday":
#     print("It is a weekday")
# else:
#     print("It is not a weekday")

# days = input("Enter day of week: ")
# if days == "Sunday" or days == "SUNDAY" or days =="sumday" or days =="Saturday" or days =="SATURDAY" or days =="saturday":
#     print("It's a weekend")
# else:
#         print("It's not a weekend")