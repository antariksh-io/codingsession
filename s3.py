# for i in range(5):
#     print(i)

# for i in range(1,10,2):
#      print(i)
# for i in range(5,0,-1):
#       print(i)
# for i in range(1,11):
#     print(i*2, " ", i*3, " ", i*4, " ", i*5, " ", i*6, " ", i*7, " ", i*8)
# for i in range(1,11):
#     print(i*3)
# for i in range(1,11):
#     print(i*4)
# for i in range(1,11):
#     print(i*5)
# for i in range(1,11):
#     print(i*6)
# for i in range(1,11):
#     print(i*7)
# for i in range(1,11):
#     print(i*8)
# name = 'Python'
# data = ['a' , 'e' , 'i' , 'o' , 'u']
# vowel = 0
# cons = 0
# for i in name:
#     if i in data:
#        vowel += 1
#     else:
#        cons += 1
# print("Vowels: ", vowel)
# print("Consonants: ", cons)
# name = 'python programming'
# newname = ''
# for i in name:
#     if i not in newname:
#         newname += i
#         print(name)
#         print(newname)

# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# x = ['A', 'B', 'C']
# y =  ['A', 'B', 'C']
# z = [1, 2, 3,4]
# print(x == y)
# print(x == z)
# print(x !=z)

#printing the count of even and odd numbers in the list
# mylist = [2,5,8,4,1,9,8]
# even = 0
# odd = 0
# for i in mylist:
#     if i%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers: ", even)
# print("Odd numbers: ", odd) 

# val = [1,2,3,4,5,6,7,8,9]
# print(val.index(5))
# print(val.index(10))

# n = [1,2,3,4,5,6,7,8,9]
# print(n.count(5))
# print(n.count(10))

# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x == 2 or x==4 or x==6 or x==8 or x==10:
#         print(x, "is even")
#         break

# name = 'python programming'
# i=0
# for x in name:
#     if x == 'n':
#         print("the character 'n' is found at index: ",i, "value: ", x)   
#         break
#     i += 1
# for i in range(1, 6):
#     if i == 5:
#         break
#     print(i)

# print()

# for j in range(5, 0, -1):
#     if j == 3:
#         continue
#     print(j)

# for i, j in zip(range(1, 6), range(5, 0, -1)):
#         if i == 3 and j == 3:
#            continue
#         print(i, j)



# char = input("Enter a character: ")
# for _ in range(1):
#          print(f"ASCII code of '{char}' is {ord(char)}")

# if char.isupper():
#     print(f"'{char}' is an uppercase letter")
# elif char.islower():
#      print(f"'{char}' is a lowercase letter")
# elif char.isdigit():
#      print(f"'{char}' is a digit")
# else:
#      print(f"'{char}' is a special symbol")


# ch = ord(input("Enter a character: "))
# if 65 <= ch <= 90:
#     print("is an upppercase")
# elif ch >= 97 and ch <= 122:
#     print("is a lowercase")
# elif ch >= 48 and ch <= 57:
#     print("is a digit")
# else:
#     print("is a special symbol")

# v = ['a', 'e', 'i', 'o', 'u']
# w = input("enter the word where we will search for vowels: ")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vovels = ',found)
# print('unique vowels',len(found),'from the given word=',w)