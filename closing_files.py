# f = open('test.txt', 'r')
# file_contents = f.read()
# f.close()

# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)

# using a context manager, we would to the same like so:
with open('test.txt', 'r') as f:
    file_contents = f.read()
    # We don't have to close it

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
