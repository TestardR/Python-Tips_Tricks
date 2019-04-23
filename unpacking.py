# # Normal
# items = (1, 2)

# print(items)

# Unpacking
a, b = (1, 2)
# print(a)
# print(b)

# Unpacking one variable
c, _ = (1, 2)
# print(c)

# Destucturing in JS
a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

# Unpacking and avoiding other variables
a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)

# Unpacking certain values, while doing other stuffs
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(c)
print(d)
