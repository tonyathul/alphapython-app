# 1st set prog
# a=10
# b=20
# c=a+b
# print(c)
# print(a+b)
# print(c*10)
# print(a+b+a+b)


# # File Handling
# # open file opening fun/ w write r read mode/ write write fun / close close fun
# myfile = open ("myfile.txt","w")
# myfile.write("helloworld")
# print("file created")
# myfile.close();

# 

# # Taking user data from terminal
# num1=input("enter 1st num: ")
# num2=input("enter 2st num: ")
# res=int(num1)+int(num2)
# # int(num2)-> typecasting to integers
# print(res)

# # Taking user data from terminal and print to file
num1=input("enter 1st num: ")
num2=input("enter 2st num: ")
res=int(num1)+int(num2)
# int(num2)-> typecasting
print(res)
myfile = open ("myfile.txt","w")
res=str(res)
# str(res)-> typecasting to string
myfile.write(res)
print("value added")
myfile.close();
