"""print(30+33)
print("hello")

A,B=2,3
txt = "@"
print((A+B)*txt) 

a,b=2,3
print(a//b,a/b)

a,b= 5,2
print(a%b)
a,b= -5,2
print(a%b)
a,b= 5,-2
print(a%b)

# string input
input1 = input("Name:")
print(input)
# int input
input2 = int(input("Age:"))
print(input)
#input float
input3 = float(input("marks:"))
print(input)

# if elif else 
age = int(input("age:"))
if(age<18):
    print("minor")
elif(age==18):
    print("18")
else:
    print("adult")

#single line if / ternary operater
#‹var> = ‹vall> if < condition> else ‹val2>
food = input("food:")
eat = "yes" if food == "cake" else "no"
print(eat)
print("jaaallbi") if food == "cake" else print("no");

#Clever If I Ternary Operator
#«var> = (false_val, true_val) [<condition»]
age = int(input("age:"))
vote = ("yes","no")[age<18]
print(vote)

# stringss
print("my name is Aditi \n  im in 1st year \t in ramdeobaba university")
str1="jay"
str2="shreeram"
print(str1+str2)
print(len(str1))
print(len(str2))
print(str2[3])
print(str2[3:6])
print(str2[3:])  # last tak
print(str2[:6])  # staring se
# count reverse stars from a p p l e
                         # -5 -4 -3 -2 -1
print(str2[-3:-1])  

str = " i m aditi gupta"
print(str.endswith("ta"))
print(str.capitalize())
print(str)
print(str.replace("aditi","sudhanshu"))
print(str.find("aditi"))
print(str.find("i"))
print(str.count("i"))

#list in python

marks = [46, 67, 68, 86, 86,97,96 ,95]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
student = ["karan", 89 , 98.23 , "good"]
print(student)
# list sllicing list_ namel starting_idx: ending_idx l #ending idx is not included
print(student[1:])
print(student[-4:])
#list methods

list = [1,2,3,4]
list.append(0)
print(list)
list.sort() 
print(list)
print(list.sort()) # change in orignal list not return any list
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
#list.insert( idx, el) #insert element at index
list.insert(3,9)
print(list)
list.remove(2)#element remove 
print(list)
list.pop(2) # index that remove
print(list)

#list = mutable
# string , tuple = immutable
tup = (1,2,3)
print(tup)
tup1 = (1,) # tuple , if (1) int , (1.0) float"""

#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,2,1]
dup = list.copy()
dup.reverse()
print(dup)
print(list)
if list == dup:
    print("palindrome")
else:
    print("not palindrome")
    
# WAP to count the number of students with the "A" grade in the following tuple.

tup = ("A", "B", "C" , "A",  "A", "C")
print(tup.count("A"))
