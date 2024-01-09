#python Day 1
#how to print in python
print("Hello Journey !! : )")
print (63 * 56)
#learn about the functions
def maximum(a,b):
    if a >= b:
        return a
    else:
        return b
    
#Driver code
    
a = 2
b = 4
print(maximum(a,b))

#program to find the factorial of the numbers

def factorial(n):

    #single line to find out
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
#Driver code
num = 5
print("Factorial of ",num,"is",factorial(num))

def fact(x):
    if (x == 0 or x==1):
        return 1
    else:
        return (x * fact(x-1))
    
#Driver code
    
num = 6
print("Factorial of ",num,"is", fact(num))

#PRogarm to find the simple interest

def simple_interest(p ,t , r):
    print("Principal is : ",p)
    print("time period is : ",t)
    print("rate if interest is : ",r)

    si =(p * t * r)/100

    print("The simple interest is : ",si)
    return si
#Driver code
simple_interest(8 , 6 ,8)

#Program to check the armsstrong number

n=153
s = n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 =  sum1 + (r**b)
    n = n/10
if s ==  sum1:
    print("The given number is Armstrong number ")
else:
    print("Given number is not a armstrong number")

#lets check about fibonaacci series
    
def fibo(n):
    if n <= 0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
print(fibo(10))
#sum of array
arr = [12, 3 ,4 ,15]
ans= sum(arr)
print("sum of the array is :  " , ans)

#find out the largest nmber in the array

def largest(arr , n ):
    max = arr[0]
    for i in range(1 , n):
        if arr[i]>max:
            max =  arr[i]
    return max

#Driver code
arr = [10 , 324 , 45 , 90 , 9888]
n = len(arr)
Ans =  largest(arr , n)
print("Largest number among the given array is " , Ans)

#Write a program to swap the elements
def swappos(list , pos1 , pos2):
    list[pos1] , list[pos2] =  list[pos2] , list[pos1]
    return list

#Driver code
List = [23 , 65 , 19 , 90 ]
pos1 , pos2 = 1 ,3 

print(swappos(List , pos1 - 1 , pos2 - 1))

#ways to  find out the length of the list


li = [10  , 20  , 30]
n = len(li)
print("Length of the given list is : " ,  n)

def add( a , b):
    return a+b
print(add(3 , 2))

#Taking input from user 

n =  int(input("Enter the size of the list : "))
lst = list(map(int , input(
    "Enter the integer elements of list : ").strip().split()))[:n]
print('The list is : ' , lst) #Printing thge list


#Another way of taking input is follows 

name = input("Enter your name : ")
age = int(input("Enter your age : "))
marks =  float(input("Enter your marks :  "))

print("The name is : " , name)
print("The age is : " , age)
print("Marks is : " , marks)

#raw_input

a = Raw_input("Enter your name : ")
print(a)



