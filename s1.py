# # # # # #why python is called as a dynamically typed language 
# # # # # a=[1,2,3,4,5,6]
# # # # # a[::2]=[10,12]
# # # # # print(a)

# # # # a=[1,2,3,4]
# # # # print(a[1:3:+1

# # # print(bool(3.14))
# # # print(bool(True))
# # # print(bool("4"))
# # # print(bool(0.444))
# # # print(bool(0))
# # # print(bool(True))

# # # num=[1,2,3,4,5]
# # # print(num[4: :-1])

# # # num=12345678
# # # a=num%10
# # # num=num//10
# # # b=num%10
# # # c=num//10
# # # d=num//10
# # # e=num//10
# # # f=num//10
# # # g=num//10
# # # h=num//10
# # # i=num//10
# # # rev=a*10000000+b*1000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i*1
# # # print(rev)

# # h = 5.9
# # inch = h*12 #h is height
# # cm = inch*2.52 
# # # print(inch)
# # # print(cm)

# # a={(1,2):1,(2,3):2,(4,5):3}
# # print(a[4,5])

# a={'a':1,'b':2,'c':3}

my_dist={}
my_dist[(1,2,4)]=8
my_dist[4,3,1]=10
my_dist[(1,2)]=12
sum=0
for k in my_dist:
    sum +=my_dist[k]
print(sum)
print(my_dist)
