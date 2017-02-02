import re

inp = input("Enter strings => ")
email = re.findall(' ([a-zA-z0-9]+)@+', inp)
full_email = re.findall('(\w+@\w+\.\w+)', inp)
print(email)
print(full_email)
