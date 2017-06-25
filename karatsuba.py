import math

def karatsuba(x, y):
    #Base case
    if x < 10 or y < 10:
        return x*y

    #Split into half size
    num_x, num_y = str(x), str(y)
    size = math.ceil(max(len(num_x), len(num_y))/2)
    pos_x, pos_y = int(len(num_x) - size), int(len(num_y) - size)
    a, b = int(num_x[:pos_x]), int(num_x[pos_x:])
    c, d = int(num_y[:pos_y]), int(num_y[pos_y:])

    #Call recursively
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    thirdTerm = karatsuba((a + b), (c + d))

    #Final calculation
    return (ac * 10**(size*2) +  (thirdTerm - ac - bd)* 10**(size) + bd)

print(karatsuba(120, 120))



