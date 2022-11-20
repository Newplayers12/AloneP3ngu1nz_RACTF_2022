#!curl https://files-digitaloverdose.ractf.cloud/challenge-files/5/ff2751f10958c82efb5079f29c07cd82/cipher.txt --output out.txt
m, n = 21, 22

def op(word, key):
    out = ''
    for i in range(len(word)):
        out += chr(ord(word[i]) ^ key)
    return out

cipher = open("out.txt", "r").read().encode('ascii')
length = len(cipher)
print('cipher length =',length)
x = cipher[:length//2]
y = cipher[length//2:]
print('first half =', x)
print('second half =', y)
other = ""
another = ""
for i in range(len(x)):
    other += chr(x[i] ^ y[i] ^ n)
    another += chr(x[i] ^ m ^ n)

print(f'flag is = {another + other}')

