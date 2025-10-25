nums = [1,2,3,4]
floats = list(map(float, nums))
print(floats)

cities = ['amsterdam', 'leeds', 'newcastle']
keep = list(filter(lambda st: st.startswith('a') and len(st) > 4, cities))
print(keep)
