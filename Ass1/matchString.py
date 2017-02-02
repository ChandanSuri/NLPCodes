import re

inp = input("Enter a string => ")
if re.match('.*abbb.*', inp):
    print("Yes the string is present.")
else:
    print("No ! is's not present.")
