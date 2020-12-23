def generous(i):
    a = 1
    x = 1
    acc = 1
    while acc+a*2 <= i:
        a*=2
        x+=1
        acc += a
        
        print(a)
    print("generous: " + str(x))
    return x

def stingy(i):
    a = 1
    b = 1
    x = 2
    acc = 2
    while (acc+a+b) <= i:
        c = a + b
        a = b
        b = c
        acc += c
        x+=1
    print("stringy: " + str(x))
    return x

def solution(i):
    return stingy(i)-generous(i)


print(solution(10))