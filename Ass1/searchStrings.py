
import nltk

inp = input("Enter a string to tokenize => ")
tokens = nltk.word_tokenize(inp)
search_str = input("Enter the string to be searched => ")
if tokens.__contains__(search_str):
    print("It contains the string.")
else:
    print("It does not contain the string.")
