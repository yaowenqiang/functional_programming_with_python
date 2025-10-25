squares = (i ** 2 for i in range(1,6))
#print(f"Value yielded: {next(squares)}")
#rint(f"Value yielded: {next(squares)}")
#rint(f"Value yielded: {next(squares)}")
#rint(f"Value yielded: {next(squares)}")
#rint(f"Value yielded: {next(squares)}")
#rint(f"Value yielded: {next(squares)}")

#x = [next(squares) for _ in range(3)]
#print(x)

#for _ in range(5):
#    print(f"Value yielded: {next(squares)}")

for _ in range(5):
    try:
        print(f"Value yielded: {next(squares)}")
    except StopIteration:
        print('generator exhausted.')

ip_address = '192.168.1.1'
parsed = [i.replace('.', '-') for i in ip_address]
parsed = (i if i != '.' else '-' for i in ip_address)
#print(parsed)

x, y , z = next(parsed), next(parsed), next(parsed)
print(f'{x}{y}{z}')

for _ in range(4):
    print('item', next(parsed))
