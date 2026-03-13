#while loop

# username = " "
# password = " "
# while username != "admin" and password != "1234":
#     username = input("Enter username: ")
#     password = input("Enter password: ")
# print("Login successful!")

#cart program

# mycart = [10, 20, 200, 300, 800, 60, 700]
# for i in mycart:
#     if i > 400:
#         print("purchased item is: ")
#         continue
#     print(i)


# dictionary program

# mydict = { 101: "John", 102: "Alice", 103: "Bob", 104: "Eve", "105": "Charlie" }
# print(mydict)

# #with help of key we have to print the value
# a = mydict
# print(a)

# #we will replace old value with new value
# mydict[101] = "Eve"
# print(mydict)

# #  only print key x=0, 1
# for x in mydict:
#     print(x)    

# # printing key and value
# for x,y in mydict.items():
#     print(x, y)

# #if i have to add ne key and value pair in the dictionary
# mydict["mobile no"] = 1234567890
# print(mydict)


#if we want to represent binary data like image, audio, video etc we can use byte data type
# byte data type is immutable and it is used to represent binary data

#take input form user and check wethe the given string is a palindrome or not
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("string is a palindrome")
# else:
#     print("string is not a palindrome")

#take input from user and check whether the given input is anagram or not
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# if sorted(string1) == sorted(string2):
#     print("string is anagram")
# else:
#     print("string is not anagram")  

#nested for loop
# print 1 1 1
#  2 2 2
#  3 3 3

# using nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, end=" ")
    print()