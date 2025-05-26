#   class Students :
 #       name = "aditi"
  #      clas = "first year"

   # s1 = Students()
    #print(s1.name)

#methods
"""
class Student:
    def info (self,name,marks):
        self.name = name
        self.marks = marks
        print("adding the data")

s1 = Student("karand", 34)
print(s1.name)
print(s1.marks)

"""
# questionsssssssssss
class Students: 
    def __init__(self, name, marks):  # constructor
        self.name = name
        self.marks = marks

    def get_avg(self):  # correctly indented method
        total = 0
        for val in self.marks:
            total += val
        print(total / len(self.marks))

# Creating object
s1 = Students("karan", [34, 45, 56])
s1.get_avg()



