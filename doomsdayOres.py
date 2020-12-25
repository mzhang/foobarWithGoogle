from fractions import Fraction
def gcd(a,b):
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
def matrixSubtract(p,q):
    result = p
    size = len(p)
    for r in range(size):
        for v in range(size):
            result[r][v]-=q[r][v]
    return result

def identity(qSize):
    i = [[0]*qSize for _ in range(qSize)]
    for j in range(qSize):
        i[j][j]=1
    return i

def matmult(a,b):
    zip_b = list(zip(*b))
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

def solution(m):
    size = len(m)
    if size < 2:
        return [1,1]
    qSize = size

    for r in range(size):
        if all([v==0 for v in m[r]]):
            m[r],m[-1] = m[-1],m[r]
            for c in range(size):
                m[c][r],m[c][-1]=m[c][-1],m[c][r]
            
    print(m)
    for r in range(size):
        if all([v==0 for v in m[r]]):
            m[r][r]=1
            qSize-=1
    
    for r in range(size):
        a = 0
        for v in range(size):
            a+=m[r][v]
        for v in range(size):
            m[r][v] = Fraction(m[r][v],a)            

    q=[m[i][:qSize] for i in range(qSize)]
    iq=matrixSubtract(identity(qSize),q)
    f=identity(qSize)
    for i in range(qSize):
        max = iq[i][i]
        maxRow = i
        for j in range(i+1,qSize):
            if iq[i][j] > max:
                max = iq[i][j]
                maxRow = j

        iq[i],iq[maxRow] = iq[maxRow],iq[i]
        f[i],f[maxRow] = f[maxRow],f[i]

        for j in range(qSize):
            if i != j:
                ratio = iq[j][i] / iq[i][i]
                for k in range(qSize):
                    iq[j][k]-=ratio*iq[i][k]
                    f[j][k]-=ratio*f[i][k]
    
    r=[m[i][qSize:] for i in range(qSize)]
    fr = matmult(f,r)

    lcm = fr[0][0].denominator

    print(iq)
    print(fr)    


    for v in fr[0]:
        lcm *= v.denominator / gcd(lcm, v.denominator)

    return [int(fr[0][i] * lcm) for i in range(len(fr[0]))] + [int(lcm)]

# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
# print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]))