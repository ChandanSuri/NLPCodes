import nltk
import re

inp = input("Enter a string => ")
chars = re.findall('[^a-z|A-Z|0-9]+', inp)
if chars:
    print("There are invalid Characters present.")
else:
    print("There are no invalid characters present.")
print(chars)
