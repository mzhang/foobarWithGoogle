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
    qSize = size
    for r in range(size):
        if all([v==0 for v in m[r]]):
            m[r][r]=1
            qSize-=1

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
    print(fr)
    
    import numpy as np # I want to check my solution with numpy

    mx = np.matrix(f)
    my = np.matrix(r)   
    print(mx*my)

    
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))

[0, 2, 1, 0, 0], 
[0, 0, 0, 3, 4], 
[0, 0, 1, 0, 0], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 1]
