# forma 1
def mayor(x,y):
    if x > y:
        return x
    return y

print(mayor(5,10))

a = 17
b = 16
c = 23
d = 20
# forma dos
maximo = mayor(a,b)
maximo = mayor(maximo, c)
maximo = mayor(maximo, d)
maxi = mayor(mayor(a,b), mayor(c,d))
# forma 3
print(maxi)
print(maximo)