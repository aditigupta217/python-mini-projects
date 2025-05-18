import random
import string     # string.ascii_letters, string.digits , string.punctuation , 

print(" Welcome to the password generator ")
charval = string.ascii_letters + string.digits + string.punctuation
pass_len = 12 

password = ""
for i in range(pass_len):
      password += random.choice(charval) 

print(" Your random password is : ",password )


