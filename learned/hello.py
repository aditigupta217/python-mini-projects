#Loops
# while loop
"""count = 100
while count >=0:
    print(count)
    count = count - 1

number = 3
i=1
while i<= 10:
    print ( i*number)    
    i=i+1


#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i=1
list = []
while i<=10 :
     ab = print(i*i)
     list.append(i*i)
     i=i+1

print(list)
#Search for a number x in this tuple using loop:


## for loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # list 
for i in list:
    print(i)
    
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)  # tuple
for j in tup:
    print(j)

str = "Aditi Gupta"
for k in str:
    if(k =='i'):
        print("found")
        break 
    print(k)
print ("done")# else : print("not found")only when loop not have break, when loop travel complete then only else will execute

#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list1:
    print(i)

#Search for a number x in this tuple using loop:
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=36
for j in tup:
    if( j == x):
        print("found")
        break
    print(j)

# range start?, stop, step?)
seq = range(10)
for e in seq:
    print(e)    # 0 to 9
seq1 = range(1,11)
for p in seq1 :
    print (p)
seq2 = range(1,11,2)
for q in seq2:
    print(q)
for q in seq2: 
    pass        # no action , continoue to print after the pass things that are out of loop

fac = 1
for i in range (1,6):
    fac = fac * i 
print(fac)

# function and recursion
def calculate(a,b):   # parameters
    add = a+b
    print(add)

print(calculate(2,3)) # arguments # funcation call
print(calculate(3,4))
# bulid in function : print(), len(), max(), min(), sum(), sorted(), sorted()
print ("apnacollege", end=" ")  # in one lline both the sentence 
print ("shradhakhapra") #end = "\n

list = [ 1,2,3,4,5,6,7]
def printlist(a):
    print(len(a))
    for i in list:
        print(i ,end=" ")

printlist(list)


def fact(n):
    fact = 1
    for i in range (1,n+1):
        fact =i*fact
        print(fact) 

fact(8)

def converter(m):
    m = m*83
    print(m)
converter(78)   
    
input = int(input("enter the number"))
def fun(input):
    if(input%2==0):
        print("even")
    else:
        print("odd")


# recursion 

def show(n):
    if(n==0):
        return 1
    print(n)
    show(n-1)

fun(input)  """

def calc_sum(n):
  if(n == 0) :
    return 0
  return calc_sum(n-1) + n
print (calc_sum(5))

def length( list , ind):
  if (ind == len(list)):
    return 
  print(list[ind])
  length(list,ind+1)

fruits = [ "apple", "orange"," mango", "cherry" ," banana "]

length(fruits,0)