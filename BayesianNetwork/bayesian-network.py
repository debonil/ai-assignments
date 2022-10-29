""" 
Assignment on Bayesian Network
Subject: Artificial Intelligence 
Submitted by
Debonil Ghosh (M21AIE225)

"""
# Events and outcomes

A = {'a1': 0, 'a2': 1, 'a3': 2}
B = {'b1': 0, 'b2': 1}
C = {'c1': 0, 'c2': 1}
M = {'m1': 0, 'm2': 1, 'm3': 2}
X = {'x1': 0, 'x2': 1}
Y = {'y1': 0, 'y2': 1, 'y3': 2}


# Conditional Probabilities as per given Bayesian Network


pA = [0.4, 0.35, 0.25]
pB = [0.6, 0.4]
pC = [0.3, 0.7]

pM = [
    # m1, m2, m3
    [0.8, 0.15, 0.05],  # a1,b1,c1
    [0.75, 0.1, 0.15],  # a2,b1,c1
    [0.7, 0.25, 0.05],  # a3,b1,c1
    [0.6, 0.02, 0.2],  # a1,b2,c1
    [0.55, 0.25, 0.02],  # a2,b2,c1
    [0.4, 0.5, 0.01],  # a3,b2,c1
    [0.4, 0.1, 0.5],  # a1,b1,c2
    [0.1, 0.5, 0.4],  # a2,b1,c2
    [0.1, 0.2, 0.7],  # a3,b1,c2
    [0.1, 0.4, 0.5],  # a1,b2,c2
    [0.01, 0.01, 0.98],  # a2,b2,c2
    [0.01, 0.14, 0.85],  # a3,b2,c2
]

pX = [
    # x1, x2
    [0.25, 0.75],  # m1
    [0.90, 0.10],  # m2
    [0.28, 0.72],  # m3
]

pY = [
    # y1, y2, y3
    [0.8, 0.15, 0.05],  # m1
    [0.15, 0.25, 0.6],  # m2
    [0.02, 0.18, 0.8],  # m3
]


# Now need to find  𝑃(𝑎1|𝑥2, 𝑦3), 𝑃(𝑎2|𝑥2, 𝑦3), 𝑎𝑛𝑑 𝑃(𝑎3|𝑥2, 𝑦3)

# P( A| x2, y3 )= α(P(A) Sum-B P(B) Sum-C P(C) Sum-M P(M|A,B,C) P( x2 | M) P(y3 | M))


# P( x2 | M) P(y3 | M)


def f1(m):
    # print(f"M=m{m+1}\t|\t{pX[m][X['x2']]}\t*\t{pY[m][Y['y3']]}\t=\t{pX[m][X['x2']]*pY[m][Y['y3']]}")
    return pX[m][X['x2']]*pY[m][Y['y3']]


# Sum-M P(M|A,B,C) f1(M)

def f2(a, b, c):
    res = 0
    # str = ''
    for m in M.values():
        res += pM[a+b*3+c*6][m] * f1(m)
        # str += '( {} * {} ) + '.format(pM[a+b*3+c*6][m], f1(m))
    # print(f"∑_M〖 P(M│a{a+1}, b{b+1}, c{c+1}) * f1(M) 〗= {str[:-2]} = {res}")
    return res

# Sum-B P(B) Sum-C P(C) f2(a, b, c)


def f3(a):
    res = 0
    # str1 = ''
    # str2 = ''
    for b in B.values():
        for c in C.values():
            res += pB[b] * pC[c] * f2(a, b, c)
            # str1 += f'P(b{b+1})*P(c{c+1})*f2(a{a+1},b{b+1},c{c+1}) + '
            # str2 += '( {} * {} * {} ) + '.format(pB[b], pC[c], f2(a, b, c))
    # print(f"f3(a{a+1}) = {str1[:-2]} \n= {str2[:-2]} \n= {res}\n")
    return res


def f4(a):
    #print(f"f4(a{a+1}) = P(a{a+1}) * f3(a{a+1}) \n= {pA[a]} * {f3(a)} \n= {pA[a] * f3(a)}\n")
    return pA[a] * f3(a)


pAX2Y3 = 0
# str=''
for a in A.values():
    # str+= f'{f4(a)} +'
    pAX2Y3 += f4(a)

# print(f'Alpha = {str[:-2]}\n')

alpha = 1 / pAX2Y3

# print(f'pAX2Y3 = {pAX2Y3}\n')
print(f'Alpha = {alpha}\n')


for a in A.values():
    print(f'𝑃(𝑎{a+1}|𝑥2, 𝑦3) = {alpha * f4(a)}\n')
