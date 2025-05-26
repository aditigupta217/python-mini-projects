"""
dict = {
    "name" : "ADiti" ,  # key - value , no index, no order, mutable, no duplicate key
   "class" : "1st year", # 
   "Roll no" : 38,
}
print(dict)
print(dict["name"])

dict["class"] = "first"
dict["info"]= "you are chudal"
print(dict)

#dict  methods 
print(list(dict.keys()))
print (len (dict) ) 
print(list(dict.values()))
print((dict.values()))
print(dict.items())

print(dict["Roll no"])
print(dict.get("Roll no"))
new_dict = {"city" : "delhi"}
dict. update (new_dict)
print(dict)"""
# set are mutable  but elements are immutable

   # collection = {1,"hello","hello" ,2,3,4,5,6,7,8,9}
#print(collection)
#print(type(collection))    # no duplicate value count 
#print(len(collection))
    #collection = {} #empty dictonray
#collection = () # empty set
collection = set()
collection. add (1)
collection.add (2)
collection. add (2)
print(collection)

set1 = {11, 2, 3}
set2 = {12, 3, 4}
print (set1.union (set2)) #{1, 2, 3, 4}
print (set1)
print (set2)
print (set1.intersection (set2)) #{1, 2, 3, 4}