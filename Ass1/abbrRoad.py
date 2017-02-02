
import re

inp = input("Enter a string to tokenize => ")
final_str = re.sub('Road', 'Rd.', inp)
print(final_str)
