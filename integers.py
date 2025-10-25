items = ['hello',"456", 123,4.5, [6,5,4], 10,2]
int_items = [i for i in items if isinstance(i, int)]
print(int_items)
