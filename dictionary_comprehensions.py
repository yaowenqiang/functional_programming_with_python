names = ['John','Charlotte', 'Joe','Alice']

names_dict = {name: name.upper() for name in names}
print(names_dict)

split_names = {name[0]: name[1:] for name in names}
print(split_names)

primes = [19,23,7,5]
number_dict = {float(p):p ** 2 for p in primes if p > 0}
print(number_dict)

capital_cities = {'england': 'london','japan':'tokyo','spain':'madroid'}
capitals = {k.title(): f'City of {v.title()}' for k,v in capital_cities.items()}
print(capitals)

capital_cities = {'england': 'london','japan':'tokyo','spain':'madroid'}
capitals = {k.title(): f'City of {v.title()}' for k,v in capital_cities.items()}
print(capitals)

city_capitals = {v:k for k,v in capital_cities.items() if k != 'england'}
print(city_capitals)

