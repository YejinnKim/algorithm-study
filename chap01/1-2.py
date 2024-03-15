def max3(a, b, c):
	max = a
	if b > max: max = b
	if c > max: max = c
	return max

print(f'max(3, 2, 1) = {max(3, 2, 1)}')
