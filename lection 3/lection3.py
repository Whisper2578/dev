a = [1, 'привет', 3.5, [1, 2, 3], '', 3.5, 3.5]
b1 = [1, 2, 3, 4, 5, 6, -71, 0]
b2 = [1, 2, 3, 4, 5, 6, -71, 0]
b3 = ['1', '222', '33', '4444', '555', '66666', '-------71', '0']
new_b3 = sorted(b3, key=len)
new_b2 = b2.sort(reverse=True)

print(new_b3, b3)
print(new_b2, b2)


