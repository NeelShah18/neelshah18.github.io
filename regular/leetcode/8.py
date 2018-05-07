
n="01100110010"
b = '{:0{width}b}'.format(n, width=width)
ans=int(b[::-1], 2)
print(ans)
