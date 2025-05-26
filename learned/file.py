f = open("pyt.txt" , "r")
data = f.read()   # f.readline()
print(data)
print(type(data))
f.close()

f = open("pyt.txt" , "w")  # override
f.write("namashte sabko bancha")
f.close()

f = open("pyt.txt" , "a")   # append 
f.write("\nnamasjdasjfkdfaa")
f.close()

f = open("pyt.txt" , "r+") # override in staring , read and write
f.write("helloo")
data = f.read()
print(data)
f.close()