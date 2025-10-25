"""
Action: Uppercase a name
Source: For each name in the 'names' list
Conditon: if that name is longer than 4 characters
"""

names = ['alex', 'charlotte', 'daniel', 'time']
uppered_names = [name.upper() for name in names if len(name) > 4]
print(uppered_names)

nums = [1,1,2,3,5,7,8,9,10,11]
square_over_5 = [i ** 2 for i in nums if i > 5]
print(square_over_5)

# reverse string

cities = ['London', 'Livepool','Leeds']
rev_cities = [city[::-1] for city in cities]
print(rev_cities)
