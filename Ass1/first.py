import nltk

inp = input("Enter a string to tokenize => ")
tokens = nltk.word_tokenize(inp)
sent_tokens = nltk.sent_tokenize(inp)
print(tokens)
print(sent_tokens)
