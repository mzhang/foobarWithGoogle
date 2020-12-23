def major(s):
    return int(s.split(".")[0])

def minor(s):
    if len(s.split("."))==2:
        return int(s.split(".")[1])
    return -1

def revision(s):
    if len(s.split("."))==3:
        return int(s.split(".")[2])
    return -1

def solution(l):
    return sorted(l,key=lambda s: list(map(int,s.split('.'))))
        

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))