import nltk

inp = input("Enter a string to tokenize => ")
tokens = nltk.word_tokenize(inp)
for token in tokens:
    if token.startswith('a') or token.startswith('e'):
        print(token)
print("Ends...\n")
