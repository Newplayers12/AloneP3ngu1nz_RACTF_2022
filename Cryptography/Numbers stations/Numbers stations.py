a = [23, 8, 1, 20, 1]
# 23, 8, 1 ,20, 1

b = [23, 5, 9, 18, 4]
# 23, 5, 9, 18, 4

c = [19, 20, 1, 20, 9]
# 19, 20, 1, 20, 9

d = [15, 14]
# 15, 14

for brute in range(26): # brute force Caesar cipher
	for number in a:
		print(chr((number+ brute) % 26 + ord('a')), end = '')

	for number in b:
		print(chr((number+ brute) % 26 + ord('a')), end = '')

	for number in c:
		print(chr((number+ brute) % 26 + ord('a')), end = '')


	for number in d:
		print(chr((number+ brute) % 26 + ord('a')), end = '')
	print()