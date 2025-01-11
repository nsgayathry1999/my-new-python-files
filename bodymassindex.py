# excersie 3
# weight = float(input("enter your weight:"))
# height = float(input("enter your height:"))
# BMI = weight / (height * height)
# if BMI < 18.5:
#     print("you are Under Weight")
# elif BMI >= 18.5 and BMI < 24.9:
#     print("you are normal")
# elif BMI >= 25 and BMI < 29.9:
#     print("you are overweight")
# else:
#     print("Obese")
# print("your BMI is:",BMI)

# ##Exercise 4
# num_1=int(input("enter the first number:"))
# num_2=int(input("enter the second number:"))
# num_3=int(input("enter the first number:"))
# greatest=max(num_1,num_2,num_3)
# print("greatset among them is",greatest)

##exercise 5
# num=int(input("enter the number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print("factorial of given number is",factorial)

## exercise 6
# num=int(input("enter the number:"))
# rev=0
# while num>0:
#     x=num%10
#     rev=rev*10+x
#     num=num//10
#
# print("reverse number =",rev)

##exercise 7
num=int(input("enter the number:"))
print("multiples of the number=")
for i in range(1,11):
    print(num*i,end=" ")

##exercise 8
# while True:
#     value=input("enter a value:")
#     if value.lower()=="done":
#         print("done")
#         break
#         print(value)


## exercise 9

# for i in range(1,11):
#     if i%3==0 and 1%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

##exercise 10

# for i in range(5,0,-1):
#     for x in range(i,0,-1):
#         print(x,end=" " )
#     print()


