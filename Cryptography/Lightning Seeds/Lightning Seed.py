import random
flag = "4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227"

for seed in range(1000):
	random.seed(seed)
	encrypted = ''.join(f'{chr(int(flag[i] + flag[i + 1], 16) ^ random.randint(0,255))}' for i in range(0, len(flag), 2))
	if (encrypted[:5] == 'DOCTF'):
		print(encrypted)

