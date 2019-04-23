class Person():
    pass


person = Person()

# person.first = "Romain"
# person.last = "Testard"

# print(person.first)
# print(person.last)

first_key = 'first'
first_val = 'Romain'

# setattr(person, 'first', 'Romain')
setattr(person, first_key, first_val)
# print(person.first)

first = getattr(person, first_key)
# print(first)

# access data in a dictionary
person_info = {'first': 'Romain', 'last': 'Testard'}

for key, value in person_info.items():
    setattr(person, key, value)

# print(person.first)
# print(person.last)

for key in person_info.keys():
    print(getattr(person, key))
