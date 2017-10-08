## Run:  python sol.py | strings | grep flag

def str2bin(a):

    b = 0
    for i in range(8):
        b += int(a[7-i])*pow(2,i)

    return b

with open("littleschoolbus.bmp", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print b
# print 'b:', len(b)

## extract all digits from LSBs to MSBs in subsequent loops.
## LSB => range(1). LSB to MSB => range(8)
for j in range(1):

    l=[]
    for i in b:
        a = 1 if i & 2**j == 2**j else 0
        l+=[a]

    # print 'l:', len(l)

    for i in range(8):
        l = l[1:]
        strl = ''.join(str(e) for e in l)
        print(''.join(chr(str2bin(strl[8*k:8*k+8])) for k in xrange(len(strl)/8)))
