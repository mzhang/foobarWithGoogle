def solution(l):
    counter = [0]*len(l)
    out = 0
    for i in range(len(l)):
        j=0
        for j in range(i):
            if l[i]%l[j]==0:
                counter[i]+=1
                out += counter[j]
    return out

print(solution([1,2,3,4,5,6]))